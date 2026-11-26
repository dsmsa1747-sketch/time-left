#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autopages.py — 무인 프로그래매틱 SEO 생성기
world.json(담뱃값) + quitdata.json(금연상담전화·회복타임라인)에서
나라별 페이지를 자동 생성한다. 사람이 글을 쓰지 않는다.
실행: python3 autopages.py        (genpages.py 실행 후에 돌린다)
"""
import json, html, io, re, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

# genpages.py 상단(CSS/NAV/SCRIPT/page/SITE/UPD_*)만 가져온다 — 디자인 단일 소스
src = open('genpages.py', encoding='utf-8').read()
head = src[:src.index('print("generating')]
g = {}
exec(compile(head, 'genpages.py', 'exec'), g)
SITE, CSS, NAV, SCRIPT = g['SITE'], g['CSS'], g['NAV'], g['SCRIPT']
UPD_EN, UPD_KO = g['UPD_EN'], g['UPD_KO']
page = g['page']

W = json.load(open('world.json'))
Q = json.load(open('quitdata.json'))
QL, TL = Q['q'], Q['tl']

MIN_PER_STICK = 17          # UCL 2024 — 담배 1개비당 수명 약 17분(남성)

CN = json.load(open('countries.json'))   # {코드:[영문명, 한글명, slug]}

def names(cc):
    if cc in CN:
        return CN[cc][0], CN[cc][1]
    raw = QL.get(cc, [cc, ""])[0]
    return (raw.split(" / ")[-1].strip(), raw.split(" / ")[0].strip())

SLUG = {x['c']: 'cost-of-smoking-' + CN[x['c']][2] + '.html' for x in W}

# ── 나라별 고유 사실 (buildfacts.py 산출). 없으면 고유 섹션 없이 예전처럼 생성 ──
CF = json.load(open('countryfacts.json', encoding='utf-8')) if os.path.exists('countryfacts.json') else {}


def _v(d):
    """{'value':..,'year':..} → 값. 미확인·데이터없음 표기는 None."""
    if not isinstance(d, dict):
        return None
    v = d.get('value')
    return None if v in (None, '', '. . .', 'Not applicable', 'Not specified') else v


def _y(d):
    return d.get('year') if isinstance(d, dict) else None


def _row(label, val, year):
    return f"<tr><td>{label}</td><td>{val}</td><td class='r'>{year or '-'}</td></tr>"


def facts_blocks(cc, en, ko, yr_money, yd):
    """국가 고유 섹션(규제·지원·FAQ·출처) + 구조화데이터 + 고유 title/description.
    확인되지 않은 항목은 문장을 아예 만들지 않는다."""
    f = CF.get(cc)
    if not f:
        return "", "", "", None, None
    R, H = f['rules'], f['help']
    sf, wp, wg, pp = _v(R['smokefree_places']), _v(R['warning_pct']), _v(R['warning_graphic']), _v(R['plain_pack'])
    sf_n = R['smokefree_places']['value'] if isinstance(R['smokefree_places'], dict) else None
    a1, a2, a3 = _v(R['ad_tv_radio']), _v(R['ad_billboard']), _v(R['ad_internet'])
    tax, tax_y = f.get('tax_share_pct'), f.get('tax_share_year')
    tel = H.get('quitline')
    ns, ni = _v(H['nrt_sold']), _v(H['nrt_cost_covered'])
    op = H.get('official_page')
    chk = f['checked']

    def ynt(v, yes, no):
        return None if v is None else (yes if v is True else (no if v is False else str(v)))

    # ── 1. 규제 ──
    rows_en, rows_ko = [], []
    if sf_n is not None:
        rows_en.append(_row('Indoor public places with a complete smoking ban',
                            f"{sf_n} of {R['smokefree_places']['of']} categories tracked by WHO", _y(R['smokefree_places'])))
        rows_ko.append(_row('실내 공공장소 전면 금연',
                            f"WHO가 집계하는 {R['smokefree_places']['of']}개 유형 중 {sf_n}개", _y(R['smokefree_places'])))
    if wp is not None:
        rows_en.append(_row('Health warning size on a cigarette pack', f"{wp:g}% of the front and back", _y(R['warning_pct'])))
        rows_ko.append(_row('담뱃갑 경고 표시 면적', f"앞·뒷면의 {wp:g}%", _y(R['warning_pct'])))
    if wg is not None:
        rows_en.append(_row('Picture (graphic) warnings required', ynt(wg, 'Yes', 'No'), _y(R['warning_graphic'])))
        rows_ko.append(_row('경고 그림(사진) 의무', ynt(wg, '있음', '없음'), _y(R['warning_graphic'])))
    if pp is not None:
        rows_en.append(_row('Plain (standardised) packaging', ynt(pp, 'Mandatory', 'Not required'), _y(R['plain_pack'])))
        rows_ko.append(_row('무광고 단순포장', ynt(pp, '의무', '의무 아님'), _y(R['plain_pack'])))
    for lab_en, lab_ko, v, src in (('TV and radio advertising', 'TV·라디오 광고', a1, R['ad_tv_radio']),
                                   ('Billboards and outdoor advertising', '옥외·빌보드 광고', a2, R['ad_billboard']),
                                   ('Internet advertising', '인터넷 광고', a3, R['ad_internet'])):
        if v is not None:
            rows_en.append(_row(lab_en, ynt(v, 'Banned', 'Not banned'), _y(src)))
            rows_ko.append(_row(lab_ko, ynt(v, '금지', '금지 아님'), _y(src)))
    if tax is not None:
        rows_en.append(_row('Tax share of the price (most sold brand)', f"{tax:g}%", tax_y))
        rows_ko.append(_row('소매가 중 세금 비중(최다 판매 브랜드)', f"{tax:g}%", tax_y))

    sec1_en = sec1_ko = ""
    if rows_en:
        of = R['smokefree_places']['of'] if isinstance(R['smokefree_places'], dict) else 8
        p_en, p_ko = [], []

        # 문단은 데이터 구간에 따라 다른 문장을 쓴다(같은 사실, 다른 서술) — 31개 페이지가 같은 글이 되지 않게
        if sf_n is not None:
            if sf_n >= of:
                p_en.append(f"Every one of the {of} indoor public place categories the World Health Organization tracks is "
                            f"completely smoke-free here by national law. On this measure there is nothing stricter left to do.")
                p_ko.append(f"세계보건기구(WHO)가 집계하는 실내 공공장소 {of}개 유형이 국가 법으로 <strong>전부</strong> 전면 금연입니다. "
                            f"이 지표에서는 더 강하게 할 것이 남아 있지 않습니다.")
            elif sf_n >= of / 2:
                p_en.append(f"National law makes <strong>{sf_n} of {of}</strong> indoor public place categories completely "
                            f"smoke-free. {of - sf_n} categories are still left out, so indoor smoke is legal somewhere.")
                p_ko.append(f"국가 법은 실내 공공장소 {of}개 유형 중 <strong>{sf_n}개</strong>를 전면 금연으로 정합니다. "
                            f"{of - sf_n}개 유형은 빠져 있어 실내 흡연이 여전히 합법인 곳이 남습니다.")
            elif sf_n > 0:
                p_en.append(f"Only <strong>{sf_n} of {of}</strong> indoor public place categories are completely smoke-free "
                            f"under national law. In the other {of - sf_n}, whether the air indoors is clean is the owner's "
                            f"decision, not the law's.")
                p_ko.append(f"국가 법상 전면 금연인 실내 공공장소는 {of}개 유형 중 <strong>{sf_n}개</strong>뿐입니다. "
                            f"나머지 {of - sf_n}개에서는 실내 공기가 깨끗한지가 법이 아니라 업주의 선택에 달려 있습니다.")
            else:
                p_en.append(f"No national law makes any of the {of} indoor public place categories completely smoke-free. "
                            f"Local rules may go further, but nothing national is behind you when you ask someone to put it out.")
                p_ko.append(f"실내 공공장소 {of}개 유형 중 국가 법으로 전면 금연인 곳은 없습니다. "
                            f"지역 규정이 더 엄할 수는 있지만, 담배를 꺼 달라고 할 때 국가 법이 뒤를 받쳐주지는 않습니다.")

        if wp is not None:
            g_en = ("A photograph or graphic is required, not just wording." if wg is True else
                    "No picture is required, so the warning can be text only." if wg is False else "")
            g_ko = ("글자만으로는 안 되고 사진·그림이 반드시 들어가야 합니다." if wg is True else
                    "그림 의무가 없어 글자만으로도 됩니다." if wg is False else "")
            pp_en = ("The pack itself is standardised — brand colours, logos and promotional design are not allowed."
                     if pp is True else "Brand colours and logos are still allowed around it." if pp is False else "")
            pp_ko = ("담뱃갑 자체가 단순포장으로 통일돼 브랜드 색상·로고·판촉 디자인을 쓸 수 없습니다."
                     if pp is True else "브랜드 색상과 로고는 그 주변에 그대로 쓸 수 있습니다." if pp is False else "")
            if wp >= 75:
                p_en.append(f"<strong>{wp:g}%</strong> of the front and back of a pack has to be health warning. "
                            f"The pack is mostly warning and the brand gets what is left. {g_en} {pp_en}")
                p_ko.append(f"담뱃갑 앞·뒷면의 <strong>{wp:g}%</strong>가 건강 경고여야 합니다. "
                            f"담뱃갑은 경고가 주인이고 브랜드는 남은 자리를 씁니다. {g_ko} {pp_ko}")
            elif wp >= 50:
                p_en.append(f"Health warnings take <strong>{wp:g}%</strong> of the front and back — half the pack or more "
                            f"belongs to the message rather than the brand. {g_en} {pp_en}")
                p_ko.append(f"건강 경고가 앞·뒷면의 <strong>{wp:g}%</strong>를 차지합니다. 담뱃갑의 절반 이상이 "
                            f"브랜드가 아니라 경고 메시지의 몫입니다. {g_ko} {pp_ko}")
            else:
                p_en.append(f"Health warnings cover <strong>{wp:g}%</strong> of the front and back, so most of the pack is "
                            f"still design. {g_en} {pp_en}")
                p_ko.append(f"건강 경고는 앞·뒷면의 <strong>{wp:g}%</strong>만 덮기 때문에 담뱃갑 대부분은 여전히 디자인입니다. "
                            f"{g_ko} {pp_ko}")

        if tax is not None:
            if tax >= 70:
                p_en.append(f"Tax is <strong>{tax:g}%</strong> of the price of the most sold brand ({tax_y}). Most of what a "
                            f"smoker hands over at the counter is tax, not tobacco — which is why a tax decision changes this "
                            f"page faster than anything a manufacturer does.")
                p_ko.append(f"최다 판매 브랜드 소매가의 <strong>{tax:g}%</strong>가 세금입니다({tax_y}년). 계산대에서 내는 돈의 "
                            f"대부분이 담배값이 아니라 세금입니다. 그래서 이 페이지의 숫자는 제조사보다 세금 결정에 더 빨리 흔들립니다.")
            elif tax >= 50:
                p_en.append(f"Tax accounts for <strong>{tax:g}%</strong> of the price of the most sold brand ({tax_y}) — "
                            f"around half. The rest is manufacture, distribution and margin.")
                p_ko.append(f"세금은 최다 판매 브랜드 소매가의 <strong>{tax:g}%</strong>, 대략 절반입니다({tax_y}년). "
                            f"나머지는 제조·유통·마진입니다.")
            else:
                p_en.append(f"Tax is <strong>{tax:g}%</strong> of the price of the most sold brand ({tax_y}) — under half. "
                            f"A pack here is cheap largely because it is taxed lightly.")
                p_ko.append(f"세금은 최다 판매 브랜드 소매가의 <strong>{tax:g}%</strong>로 절반이 안 됩니다({tax_y}년). "
                            f"이 나라 담배가 싼 이유의 큰 몫은 세금이 가볍다는 데 있습니다.")

        sec1_en = (f"<h2>Tobacco rules in {html.escape(en)}</h2>"
                   + "".join(f"<p>{t}</p>" for t in p_en)
                   + "<div class=\"tw\"><table><thead><tr><th>Rule</th><th>Status</th><th class=\"r\">Year</th></tr></thead><tbody>"
                   + "".join(rows_en) + "</tbody></table></div>"
                   + f"<p class=\"upd\">Source: WHO Global Health Observatory tobacco control indicators. Checked {chk}.</p>")
        sec1_ko = (f"<h2>{html.escape(ko)}의 담배 규제</h2>"
                   + "".join(f"<p>{t}</p>" for t in p_ko)
                   + "<div class=\"tw\"><table><thead><tr><th>항목</th><th>내용</th><th class=\"r\">기준연도</th></tr></thead><tbody>"
                   + "".join(rows_ko) + "</tbody></table></div>"
                   + f"<p class=\"upd\">출처: WHO 국제보건관측소(GHO) 담배규제 지표. 확인일 {chk}.</p>")

    # ── 2. 금연 지원 ── (비용 지원 수준에 따라 다른 문장)
    help_en, help_ko = [], []
    cov = ni if ni in ('Fully', 'Partially') else (True if ni is True else (False if ni is False else None))
    nrt_ok = (ns is True)
    if tel:
        if cov == 'Fully' and nrt_ok:
            help_en.append(f"Two things are free here. The quitline answers on <strong>{html.escape(tel)}</strong> at no cost, "
                           f"and nicotine replacement — patches, gum, lozenges — is covered as well, so a serious attempt "
                           f"does not have to come out of your own pocket. Using counselling and medication together beats "
                           f"either one alone.")
            help_ko.append(f"여기서는 두 가지가 무료입니다. 금연상담전화 <strong>{html.escape(tel)}</strong>는 비용이 들지 않고, "
                           f"니코틴 대체요법(패치·껌·로젠지)도 비용이 지원됩니다. 제대로 한 번 끊어보려 할 때 본인 돈이 들지 "
                           f"않는다는 뜻입니다. 상담과 약을 함께 쓰면 어느 한쪽만 쓸 때보다 잘 됩니다.")
        elif cov == 'Partially' and nrt_ok:
            help_en.append(f"The quitline on <strong>{html.escape(tel)}</strong> is free. Nicotine replacement is sold legally "
                           f"and partly subsidised, so expect to pay something for patches or gum but not the full price. "
                           f"Counselling plus medication is the combination with the best record.")
            help_ko.append(f"금연상담전화 <strong>{html.escape(tel)}</strong>는 무료입니다. 니코틴 대체요법은 합법 판매되고 "
                           f"비용이 일부 지원되므로 패치나 껌에 얼마간은 내지만 전액은 아닙니다. 상담과 약을 함께 쓰는 조합이 "
                           f"가장 성적이 좋습니다.")
        elif cov is False and nrt_ok:
            help_en.append(f"Calling <strong>{html.escape(tel)}</strong> costs nothing, and that matters more here than usual: "
                           f"nicotine replacement is sold legally but the cost is not covered, so patches and gum come out of "
                           f"your own money. Budget for them the way you budgeted for cigarettes — it is still the cheaper month.")
            help_ko.append(f"<strong>{html.escape(tel)}</strong>로 전화하는 것은 무료이고, 이 나라에서는 그게 더 중요합니다. "
                           f"니코틴 대체요법은 합법 판매되지만 비용 지원이 없어 패치·껌 값은 본인이 냅니다. 담뱃값을 잡아두던 "
                           f"자리에 그 돈을 넣으십시오. 그래도 한 달 지출은 줄어듭니다.")
        else:
            help_en.append(f"A free quitline answers on <strong>{html.escape(tel)}</strong>. Counselling costs nothing, and "
                           f"talking to someone trained is the cheapest thing that measurably raises the odds of a quit "
                           f"attempt holding.")
            help_ko.append(f"무료 금연상담전화는 <strong>{html.escape(tel)}</strong>입니다. 상담 비용은 들지 않습니다. "
                           f"훈련받은 사람과 통화하는 것은 금연 성공 확률을 실제로 올리는 가장 값싼 방법입니다.")
    elif nrt_ok:
        help_en.append("There is no national quitline number on record for this country, but nicotine replacement — patches, "
                       "gum, lozenges — is sold legally, and a pharmacist can walk you through which one fits how much you smoke.")
        help_ko.append("이 나라의 전국 금연상담전화 번호는 확인된 자료가 없습니다. 다만 니코틴 대체요법(패치·껌·로젠지)은 "
                       "합법적으로 판매되므로 약사에게 흡연량에 맞는 제품을 상의할 수 있습니다.")
    if op:
        help_en.append(f"The official page for this country is "
                       f"<a href=\"{html.escape(op['url'])}\" rel=\"nofollow noopener\" target=\"_blank\">"
                       f"{html.escape(op['title'])}</a>. Numbers and programmes change; that page is where to check, "
                       f"and it is the one we verified on {chk}.")
        help_ko.append(f"이 나라의 공식 안내 페이지는 "
                       f"<a href=\"{html.escape(op['url'])}\" rel=\"nofollow noopener\" target=\"_blank\">"
                       f"{html.escape(op['title'])}</a>입니다. 번호와 지원 사업은 바뀌므로 확인은 그 페이지에서 하십시오. "
                       f"{chk}에 실제로 접속해 확인한 주소입니다.")
    else:
        help_en.append("We could not reach an official government page for this country on the day this page was built, so "
                       "the figures above rest on the WHO indicators alone. If you know the right official address, "
                       "the contact link at the bottom goes to a person.")
        help_ko.append("이 페이지를 만든 날 이 나라의 정부 공식 페이지에는 접속하지 못했습니다. 그래서 위 수치는 WHO 지표만을 "
                       "근거로 합니다. 맞는 공식 주소를 아시면 아래 문의 주소로 알려주십시오.")
    sec2_en = (f"<h2>What {html.escape(en)} does to help you quit</h2>" + "".join(f"<p>{t}</p>" for t in help_en)) if help_en else ""
    sec2_ko = (f"<h2>{html.escape(ko)}가 금연을 돕는 방법</h2>" + "".join(f"<p>{t}</p>" for t in help_ko)) if help_ko else ""

    # ── 3. FAQ (JSON-LD 와 같은 문장) ──
    faq = []
    faq.append((f"How much does a pack a day cost in {en} in a year?",
                f"하루 한 갑이면 {ko}에서 1년에 얼마입니까?",
                f"About {yr_money} a year at the pack price used on this page, plus roughly {yd} days of life "
                f"expectancy by the UCL estimate of 17 minutes a cigarette.",
                f"이 페이지가 쓰는 담뱃값 기준으로 1년에 약 {yr_money}입니다. 여기에 개비당 17분(UCL 추정)으로 계산한 "
                f"기대수명 약 {yd}일이 더해집니다."))
    if tel:
        faq.append((f"Is there a free quitline in {en}?",
                    f"{ko}에서 무료 금연상담을 받을 수 있습니까?",
                    f"Yes — {tel}. Counselling is free.",
                    f"받을 수 있습니다. {tel} 로 전화하면 되고 상담은 무료입니다."))
    if tax is not None:
        faq.append((f"How much of the cigarette price in {en} is tax?",
                    f"{ko} 담뱃값에서 세금은 얼마입니까?",
                    f"{tax:g}% of the price of the most sold brand, as recorded by WHO for {tax_y}.",
                    f"최다 판매 브랜드 소매가의 {tax:g}%입니다(WHO {tax_y}년 집계)."))
    elif wp is not None:
        faq.append((f"How big is the health warning on a pack in {en}?",
                    f"{ko} 담뱃갑 경고 표시는 얼마나 큽니까?",
                    f"It must cover {wp:g}% of the front and back of the pack.",
                    f"담뱃갑 앞·뒷면의 {wp:g}%를 덮어야 합니다."))
    faq_en = ("<h2>Questions</h2>" + "".join(f"<p><strong>{html.escape(q)}</strong><br>{a}</p>" for q, _, a, _ in faq)) if faq else ""
    faq_ko = ("<h2>자주 묻는 질문</h2>" + "".join(f"<p><strong>{html.escape(q)}</strong><br>{a}</p>" for _, q, _, a in faq)) if faq else ""

    # ── 4. 출처 ──
    src_items = "".join(
        f"<li><a href=\"{html.escape(s['url'])}\" rel=\"nofollow noopener\" target=\"_blank\">{html.escape(s['title'])}</a>"
        f" <span class=\"upd\">({s['fetched']})</span></li>" for s in f['sources'])
    src_en = f"<h2>Sources</h2><ul>{src_items}</ul><p class=\"upd\">Checked {chk}. Prices and quitline numbers change; "
    src_en += "the official page above is always the final word.</p>"
    src_ko = f"<h2>출처</h2><ul>{src_items}</ul><p class=\"upd\">확인일 {chk}. 담뱃값과 상담전화 번호는 바뀝니다. "
    src_ko += "최종 기준은 위의 공식 페이지입니다.</p>"

    # ── 5. 구조화 데이터 ──
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": f"What smoking costs in {en}",
         "author": {"@type": "Organization", "name": "Time Left 편집팀"},
         "publisher": {"@type": "Organization", "name": "Time Left"},
         "datePublished": chk, "dateModified": chk,
         "mainEntityOfPage": f"{SITE}/{SLUG[cc]}"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Prices worldwide", "item": f"{SITE}/prices.html"},
            {"@type": "ListItem", "position": 3, "name": en, "item": f"{SITE}/{SLUG[cc]}"}]}]}
    if faq:
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, _, a, _ in faq]})
    ld_html = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'

    # ── 6. 고유 title / description ──
    bits = []
    if tax is not None:
        bits.append(f"tax {tax:g}%")
    if wp is not None:
        bits.append(f"warnings {wp:g}%")
    if sf_n is not None:
        bits.append(f"smoke-free {sf_n}/{R['smokefree_places']['of']}")
    title = f"Smoking in {en}: price, rules and free help | Time Left"
    desc = (f"What a pack costs in {en}, what the law requires ("
            + ", ".join(bits) + ") and how to get free help to quit."
            + (f" Quitline {tel}." if tel else "")) if bits else None
    return (sec1_en + sec2_en + faq_en + src_en, sec1_ko + sec2_ko + faq_ko + src_ko, ld_html, title, desc)


def money(v):
    return f"${v:,.0f}" if v >= 100 else f"${v:,.2f}"


def hm(minutes):
    """분 → '3일 7시간' / '3 days 7 hours'"""
    d, r = divmod(int(minutes), 1440)
    h = r // 60
    return d, h


def country_page(x):
    cc = x['c']
    en, ko = names(cc)
    per = x['per']
    pack = x['usd']
    stick = pack / per
    day, wk, mo, yr, ten = pack, pack * 7, pack * 30, pack * 365, pack * 3650
    mp = MIN_PER_STICK * per                      # 한 갑당 잃는 분
    my = mp * 365                                 # 1년(하루 한 갑)
    yd, yh = hm(my)
    td, th = hm(my * 10)
    tel = QL.get(cc, ["", ""])[1]

    # 나라별 회복 타임라인 5개
    tl_en = "".join(f"<li><span class='t'>{t['en'][0]}</span><span>{html.escape(t['en'][1])}</span></li>" for t in TL[:5])
    tl_ko = "".join(f"<li><span class='t'>{t['ko'][0]}</span><span>{html.escape(t['ko'][1])}</span></li>" for t in TL[:5])

    tel_en = (f"<div class='box'><p><strong>Free quitline in {html.escape(en)}:</strong> "
              f"<span class='tel'><a href='tel:{tel.replace(' ', '')}'>{html.escape(tel)}</a></span> — "
              f"counselling at no charge. <a href='quitlines.html' data-keep>All {len(QL)} countries →</a></p></div>") if tel else ""
    tel_ko = (f"<div class='box'><p><strong>{html.escape(ko)} 무료 금연상담전화:</strong> "
              f"<span class='tel'><a href='tel:{tel.replace(' ', '')}'>{html.escape(tel)}</a></span> — 상담은 무료입니다. "
              f"<a href='quitlines.html' data-keep>{len(QL)}개국 전체 →</a></p></div>") if tel else ""

    sec_en, sec_ko, ld_html, t_uniq, d_uniq = facts_blocks(cc, en, ko, money(yr), yd)

    others = [y for y in W if y['c'] != cc]
    others.sort(key=lambda y: -y['usd'])
    lnk_en = " · ".join(f"<a href='{SLUG[y['c']]}' data-keep>{y['f']} {html.escape(names(y['c'])[0])}</a>" for y in others)
    lnk_ko = " · ".join(f"<a href='{SLUG[y['c']]}' data-keep>{y['f']} {html.escape(names(y['c'])[1])}</a>" for y in others)

    tbl_en = f"""<div class="tw"><table><thead><tr><th>Period</th><th class="r">Money</th><th class="r">Life</th></tr></thead><tbody>
<tr><td>One cigarette</td><td class="r">{money(stick)}</td><td class="r">{MIN_PER_STICK} min</td></tr>
<tr><td>One pack ({per})</td><td class="r">{money(day)}</td><td class="r">{mp:,} min</td></tr>
<tr><td>One week</td><td class="r">{money(wk)}</td><td class="r">{mp*7/1440:.1f} days</td></tr>
<tr><td>One month</td><td class="r">{money(mo)}</td><td class="r">{mp*30/1440:.1f} days</td></tr>
<tr><td>One year</td><td class="r">{money(yr)}</td><td class="r">{yd} days {yh} h</td></tr>
<tr><td>Ten years</td><td class="r">{money(ten)}</td><td class="r">{td} days</td></tr>
</tbody></table></div>"""
    tbl_ko = f"""<div class="tw"><table><thead><tr><th>기간</th><th class="r">돈</th><th class="r">수명</th></tr></thead><tbody>
<tr><td>1개비</td><td class="r">{money(stick)}</td><td class="r">{MIN_PER_STICK}분</td></tr>
<tr><td>한 갑({per}개비)</td><td class="r">{money(day)}</td><td class="r">{mp:,}분</td></tr>
<tr><td>1주</td><td class="r">{money(wk)}</td><td class="r">{mp*7/1440:.1f}일</td></tr>
<tr><td>1개월</td><td class="r">{money(mo)}</td><td class="r">{mp*30/1440:.1f}일</td></tr>
<tr><td>1년</td><td class="r">{money(yr)}</td><td class="r">{yd}일 {yh}시간</td></tr>
<tr><td>10년</td><td class="r">{money(ten)}</td><td class="r">{td}일</td></tr>
</tbody></table></div>"""

    body_en = f"""<h1>What smoking costs in {html.escape(en)} {x['f']}</h1>
<p class="sub">A pack costs {html.escape(x['local'])} (about {money(pack)}). At a pack a day, here is the money and the time.</p>
<p class="upd">Last updated {UPD_EN}</p>

<p>A pack of {per} cigarettes in {html.escape(en)} costs roughly <strong>{money(pack)}</strong>, which works out to
{money(stick)} per cigarette. A 2024 analysis from University College London put the cost of a single cigarette at about
<strong>{MIN_PER_STICK} minutes</strong> of life expectancy for men — so one pack is around {mp:,} minutes,
or {mp/60:.1f} hours.</p>

{tbl_en}

<p>Read the bottom row again. Ten years of a pack a day in {html.escape(en)} is <strong>{money(ten)}</strong> and roughly
<strong>{td} days</strong> — about {td/365:.1f} years — of life expectancy. Those are averages across large
populations, not a prediction about any one person. They are useful for the same reason a speed limit is useful:
not because it tells you exactly what will happen, but because the direction is not in doubt.</p>

{tel_en}

<h2>What changes when you stop</h2>
<p>Recovery starts faster than most people expect. The first items are measured in minutes, not years.</p>
<ul class="tl">{tl_en}</ul>
<p><a href="timeline.html" data-keep>See the full recovery timeline →</a></p>

<h2>Run your own numbers</h2>
<p>The figures above assume exactly one pack a day starting today. If you smoke more, less, or have smoked for
twenty years already, the calculator uses your own numbers — the date you started, what you actually pay,
how many you actually smoke — and it keeps counting. Nothing is uploaded; it stays on your phone.</p>
<p><a href="index.html" data-keep><strong>Open the calculator →</strong></a></p>

{sec_en}

<h2>Other countries</h2>
<p style="font-size:13px;line-height:2.1">{lnk_en}</p>
<p><a href="prices.html" data-keep>Compare all {len(W)} countries in one table →</a></p>
{ld_html}"""

    body_ko = f"""<h1>{html.escape(ko)}에서 담배가 가져가는 것 {x['f']}</h1>
<p class="sub">한 갑 {html.escape(x['local'])}(약 {money(pack)}). 하루 한 갑 기준, 돈과 시간입니다.</p>
<p class="upd">최종 업데이트 {UPD_KO}</p>

<p>{html.escape(ko)}에서 {per}개비 한 갑은 약 <strong>{money(pack)}</strong>, 개비당 {money(stick)}입니다.
2024년 유니버시티 칼리지 런던(UCL) 분석은 담배 1개비가 남성 기준 기대수명 약
<strong>{MIN_PER_STICK}분</strong>을 가져간다고 추정했습니다. 한 갑이면 약 {mp:,}분, {mp/60:.1f}시간입니다.</p>

{tbl_ko}

<p>맨 아래 줄을 다시 보십시오. {html.escape(ko)}에서 하루 한 갑을 10년 피우면 <strong>{money(ten)}</strong>,
그리고 기대수명 약 <strong>{td}일</strong>(약 {td/365:.1f}년)입니다. 이 숫자는 대규모 인구 집단의 평균이며
특정 개인에게 그대로 일어난다는 예측이 아닙니다. 제한속도가 유용한 이유와 같습니다 —
정확히 무슨 일이 일어날지 알려주기 때문이 아니라, 방향이 분명하기 때문입니다.</p>

{tel_ko}

<h2>끊으면 무엇이 달라지는가</h2>
<p>회복은 생각보다 빨리 시작됩니다. 첫 항목들의 단위는 년이 아니라 분입니다.</p>
<ul class="tl">{tl_ko}</ul>
<p><a href="timeline.html" data-keep>전체 회복 타임라인 보기 →</a></p>

<h2>내 숫자로 계산하기</h2>
<p>위 숫자는 오늘부터 하루 정확히 한 갑을 기준으로 합니다. 더 피우거나 덜 피우거나,
이미 20년을 피웠다면 계산기가 회장님 본인의 숫자 — 시작한 날짜, 실제로 내는 가격,
실제 개비 수 — 로 계산하고 계속 세어줍니다. 아무것도 업로드되지 않고 휴대폰에만 남습니다.</p>
<p><a href="index.html" data-keep><strong>계산기 열기 →</strong></a></p>

{sec_ko}

<h2>다른 나라</h2>
<p style="font-size:13px;line-height:2.1">{lnk_ko}</p>
<p><a href="prices.html" data-keep>{len(W)}개국 한 표로 비교 →</a></p>"""

    page(SLUG[cc],
         t_uniq or f"What smoking costs in {en} ({money(pack)} a pack) | Time Left",
         d_uniq or (f"A pack in {en} costs about {money(pack)}. A pack a day is {money(yr)} and {yd} days of life expectancy a year. "
                    f"Free quitline number and recovery timeline included."),
         body_en, body_ko)
    return SLUG[cc]


print("무인 국가 페이지 생성…")
made = [country_page(x) for x in sorted(W, key=lambda r: -r['usd'])]

# ── prices.html 에 국가 페이지 링크 블록 주입 (중복 주입 방지) ──
MARK = "<!--AUTO-COUNTRY-LINKS-->"
p = open('dist/prices.html', encoding='utf-8').read()
if MARK not in p:
    def block(lang):
        items = " · ".join(
            f"<a href='{SLUG[y['c']]}' data-keep>{y['f']} {html.escape(names(y['c'])[0 if lang=='en' else 1])}</a>"
            for y in sorted(W, key=lambda r: -r['usd']))
        h = ("<h2>Country by country</h2><p>A page for each country with its own figures, quitline number and timeline.</p>"
             if lang == 'en' else
             "<h2>나라별 상세</h2><p>나라마다 자체 숫자·금연상담전화·회복 타임라인이 있는 페이지가 있습니다.</p>")
        return f"{MARK}\n{h}\n<p style=\"font-size:13px;line-height:2.1\">{items}</p>\n"
    for lang in ('en', 'ko'):
        anchor = f'<a class="back" href="index.html" data-keep>' + ('← Open the calculator' if lang == 'en' else '← 계산기 열기')
        i = p.index(anchor)
        p = p[:i] + block(lang) + p[i:]
    open('dist/prices.html', 'w', encoding='utf-8').write(p)
    print(f"  prices.html   ← 국가 링크 {len(W)}개 주입")
else:
    print("  prices.html   ← 이미 주입됨(건너뜀)")

# ── sitemap.xml 재생성 ──
BASE = ['index.html', 'timeline.html', 'prices.html', 'quitlines.html', 'about.html', 'privacy.html', 'terms.html']
today = datetime.date.today().isoformat()
u = []
for f in BASE + made:
    loc = SITE + '/' if f == 'index.html' else SITE + '/' + f
    pr = '1.0' if f == 'index.html' else ('0.8' if f in BASE else '0.7')
    u.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
             f"    <changefreq>weekly</changefreq>\n    <priority>{pr}</priority>\n"
             f"    <xhtml:link rel=\"alternate\" hreflang=\"en\" href=\"{loc}?lang=en\"/>\n"
             f"    <xhtml:link rel=\"alternate\" hreflang=\"ko\" href=\"{loc}?lang=ko\"/>\n  </url>")
open('dist/sitemap.xml', 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(u) + "\n</urlset>\n")
print(f"  sitemap.xml   ← {len(BASE)+len(made)} URL")

# ── 서비스워커 캐시 버전 +1 (새 페이지가 즉시 보이게) ──
# dist/sw.js 가 없으면 배포본(루트)에서 씨드한다 — 새 클론에서도 빌드가 멈추지 않게
if not os.path.exists('dist/sw.js') and os.path.exists('../sw.js'):
    open('dist/sw.js', 'w', encoding='utf-8').write(open('../sw.js', encoding='utf-8').read())
sw = open('dist/sw.js', encoding='utf-8').read()
m = re.search(r'timeleft-v(\d+)', sw)
if m:
    nv = int(m.group(1)) + 1
    sw = sw.replace(m.group(0), f'timeleft-v{nv}')
    open('dist/sw.js', 'w', encoding='utf-8').write(sw)
    print(f"  sw.js         ← timeleft-v{nv}")

# ── IndexNow 제출용 URL 목록 (로그인 불필요) ──
open('indexnow-urls.txt', 'w', encoding='utf-8').write(
    "\n".join([SITE + '/'] + [SITE + '/' + f for f in BASE[1:] + made]) + "\n")
print(f"\n완료: 국가 페이지 {len(made)}개 · indexnow-urls.txt {len(BASE)+len(made)}개")
