#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""genguides.py — 정보성 가이드 12편 + 허브(guides.html) 생성기.

손편집 금지. 본문은 guides_part*.py 의 데이터에서만 오고,
출처는 work/guide_probe.json 에서 **200 으로 실측된 URL** 만 쓴다.
(출처 키가 200 이 아니면 빌드를 멈춘다 — 확인 안 된 인용을 페이지에 올리지 않는다)

분량 게이트: 한국어 1,800자 이상 / 영어 900단어 이상. 미달이면 exit 1.

실행: python tools/genguides.py        (genpages.py 다음, autopages.py 앞)
"""
import json, os, re, sys, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

# genpages.py 상단(CSS/NAV/SCRIPT/page/SITE/UPD_*)만 가져온다 — 디자인 단일 소스
src = open('genpages.py', encoding='utf-8').read()
g = {}
exec(compile(src[:src.index('print("generating')], 'genpages.py', 'exec'), g)
SITE, page = g['SITE'], g['page']
UPD_EN, UPD_KO = g['UPD_EN'], g['UPD_KO']

from guides_part1 import GUIDES as G1
from guides_part2 import GUIDES as G2
from guides_part3 import GUIDES as G3
from guides_part4 import GUIDES as G4
GUIDES = G1 + G2 + G3 + G4

PROBE = json.load(open('work/guide_probe.json', encoding='utf-8'))
TODAY = datetime.date.today().isoformat()
MIN_KO, MIN_EN = 1800, 900

CATS = {
    'money': ('Money and numbers', '계산·돈'),
    'body':  ('Body and symptoms', '몸·증상'),
    'help':  ('Support and rules', '지원·제도'),
    'tool':  ('Using the tool', '도구'),
}

TAGS = re.compile(r'<[^>]+>')

# ── 데이터에서 찍는 표(사람이 숫자를 쓰지 않는다) ──
CF = json.load(open('countryfacts.json', encoding='utf-8'))
W = {x['c']: x for x in json.load(open('world.json'))}
CN = json.load(open('countries.json'))


def tax_table(lang):
    """담뱃값 대비 세금 비중 — WHO GHO 지표 + world.json 가격. 값 없는 나라는 빼고 찍는다."""
    rows = []
    for cc, v in CF.items():
        if cc.startswith('_') or not v.get('tax_share_pct') or cc not in W:
            continue
        x = W[cc]
        name = CN.get(cc, [cc, cc, ''])[0 if lang == 'en' else 1]
        rows.append((v['tax_share_pct'], v.get('tax_share_year'), name, x['local'], x['usd'], cc))
    rows.sort(reverse=True)
    head = (('Country', 'Pack price', 'USD', 'Tax share of price', 'Year') if lang == 'en'
            else ('국가', '한 갑 가격', 'USD', '가격 중 세금 비중', '기준연도'))
    body = "".join(
        f"<tr><td><a href=\"cost-of-smoking-{CN[cc][2]}.html\" data-keep>{html.escape(nm)}</a></td>"
        f"<td class='r'>{html.escape(loc)}</td><td class='r'>${usd:.2f}</td>"
        f"<td class='r'>{pct:g}%</td><td class='r'>{yr or '-'}</td></tr>"
        for pct, yr, nm, loc, usd, cc in rows)
    return (f"<div class=\"tw\"><table><thead><tr>"
            + "".join(f"<th{' class=\"r\"' if i else ''}>{h}</th>" for i, h in enumerate(head))
            + f"</tr></thead><tbody>{body}</tbody></table></div>"
            + (f"<p style=\"font-size:12.5px;color:#8B8270\">{len(rows)} countries with a published WHO tax-share figure.</p>"
               if lang == 'en' else
               f"<p style=\"font-size:12.5px;color:#8B8270\">WHO 세금 비중 수치가 공표된 {len(rows)}개국.</p>"))


def kr_table(lang):
    """한국 담뱃값 구조 — world.json 가격 + WHO 세금 비중. 연도별 연혁은 확인 전까지 쓰지 않는다."""
    x, v = W['KR'], CF['KR']
    pack, per = x['usd'], x['per']
    pct, yr = v.get('tax_share_pct'), v.get('tax_share_year')
    rows = ([('Pack price (20)', f"{x['local']} (${pack:.2f})"),
             ('Per cigarette', f"${pack / per:.2f}"),
             ('Pack a day, one year', f"${pack * 365:,.0f}"),
             ('Tax share of the price', f"{pct:g}% ({yr}, WHO)" if pct else 'not published'),
             ('Estimated tax in one pack', f"${pack * pct / 100:.2f}" if pct else '-')]
            if lang == 'en' else
            [('한 갑(20개비) 가격', f"{x['local']} (약 ${pack:.2f})"),
             ('개비당', f"${pack / per:.2f}"),
             ('하루 한 갑 1년', f"${pack * 365:,.0f}"),
             ('가격 중 세금 비중', f"{pct:g}% ({yr}년, WHO)" if pct else '미공표'),
             ('한 갑에 포함된 세금(추정)', f"약 ${pack * pct / 100:.2f}" if pct else '-')])
    body = "".join(f"<tr><td>{html.escape(k)}</td><td class='r'>{html.escape(str(val))}</td></tr>" for k, val in rows)
    return f"<div class=\"tw\"><table><tbody>{body}</tbody></table></div>"


def fill(h, lang):
    return (h.replace('{{TAX_TABLE}}', tax_table(lang))
             .replace('{{KR_TABLE}}', kr_table(lang)))


def plain(h):
    return re.sub(r'\s+', ' ', html.unescape(TAGS.sub(' ', h))).strip()


def src_of(keys):
    """실측된 출처만 반환. 하나라도 200 이 아니면 빌드 중단."""
    out = []
    for k in keys:
        v = PROBE.get(k)
        if not v or v['status'] != 200:
            sys.exit(f"출처 미검증: {k} (status={v['status'] if v else 'none'}) — guidesrc.py 를 먼저 돌려라")
        out.append(v)
    return out


def src_box(srcs, lang):
    lab = 'Sources' if lang == 'en' else '출처'
    chk = 'confirmed' if lang == 'en' else '확인일'
    items = "".join(
        f"<li><a href=\"{html.escape(s['url'])}\" rel=\"nofollow noopener\" target=\"_blank\">"
        f"{html.escape(s['title'][:90])}</a> — {chk} {s['fetched']}</li>" for s in srcs)
    return f"<h2>{lab}</h2><ul>{items}</ul>"


def faq_html(faq, lang):
    lab = 'Common questions' if lang == 'en' else '자주 묻는 질문'
    body = "".join(f"<h3>{html.escape(q)}</h3><p>{a}</p>" for q, a in faq)
    return f"<h2>{lab}</h2>{body}"


def rel_html(rel, lang):
    lab = 'Related' if lang == 'en' else '관련 글'
    items = "".join(f"<li><a href=\"{h}\" data-keep>{html.escape(t_en if lang == 'en' else t_ko)}</a></li>"
                    for h, t_en, t_ko in rel)
    return f"<h2>{lab}</h2><ul>{items}</ul>"


def ld_for(gd, srcs):
    u = f"{SITE}/{gd['slug']}.html"
    art = {"@type": "Article", "headline": gd['title_en'], "description": gd['desc_en'],
           "inLanguage": ["en", "ko"], "mainEntityOfPage": u,
           "author": {"@type": "Organization", "name": "Time Left 편집팀"},
           "publisher": {"@type": "Organization", "name": "Time Left", "url": SITE},
           "datePublished": TODAY, "dateModified": TODAY,
           "citation": [{"@type": "WebPage", "url": s['url'], "name": s['title'][:90]} for s in srcs]}
    faq = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in gd['faq_en']]}
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides.html"},
        {"@type": "ListItem", "position": 3, "name": gd['title_en'], "item": u}]}
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": [art, faq, bc]}, ensure_ascii=False)
            + '</script>')


os.makedirs('dist', exist_ok=True)
print("guides…")
short, made = [], []

for gd in GUIDES:
    srcs = src_of(gd['srcs'])
    be = (f"<h1>{html.escape(gd['h1_en'])}</h1>\n<p class=\"sub\">{html.escape(gd['sub_en'])}</p>\n"
          f"<p class=\"upd\">Last updated {UPD_EN} · sources confirmed {srcs[0]['fetched']}</p>\n"
          + fill(gd['body_en'], 'en') + faq_html(gd['faq_en'], 'en') + rel_html(gd['rel'], 'en')
          + src_box(srcs, 'en')
          + "<div class=\"box\"><p>Time Left is a calculator, not medical advice. "
            "For personal medical questions speak to a clinician or your national quitline.</p></div>"
          + "<p><a href=\"index.html\" data-keep><strong>Open the calculator →</strong></a></p>")
    bk = (f"<h1>{html.escape(gd['h1_ko'])}</h1>\n<p class=\"sub\">{html.escape(gd['sub_ko'])}</p>\n"
          f"<p class=\"upd\">최종 업데이트 {UPD_KO} · 출처 확인일 {srcs[0]['fetched']}</p>\n"
          + fill(gd['body_ko'], 'ko') + faq_html(gd['faq_ko'], 'ko') + rel_html(gd['rel'], 'ko')
          + src_box(srcs, 'ko')
          + "<div class=\"box\"><p>이 사이트는 계산기이며 의학적 조언이 아닙니다. "
            "개인의 건강 문제는 의료진 또는 금연상담전화에 문의하십시오.</p></div>"
          + "<p><a href=\"index.html\" data-keep><strong>계산기 열기 →</strong></a></p>")

    en_words = len(plain(be).split())
    ko_chars = len(re.sub(r'\s', '', plain(bk)))
    if en_words < MIN_EN or ko_chars < MIN_KO:
        short.append(f"{gd['slug']}: en {en_words}단어 / ko {ko_chars}자")

    page(gd['slug'] + '.html', f"{gd['title_en']} | Time Left", gd['desc_en'],
         be + ld_for(gd, srcs), bk)
    made.append(gd['slug'] + '.html')
    print(f"    en {en_words:>4}w  ko {ko_chars:>5}자  {gd['slug']}")

# ── 허브 ──
def hub(lang):
    out = []
    for key, (ten, tko) in CATS.items():
        rows = [x for x in GUIDES if x['cat'] == key]
        if not rows:
            continue
        out.append(f"<h2>{ten if lang == 'en' else tko}</h2><ul>")
        for x in rows:
            t = x['h1_en'] if lang == 'en' else x['h1_ko']
            d = x['sub_en'] if lang == 'en' else x['sub_ko']
            out.append(f"<li><a href=\"{x['slug']}.html\" data-keep><strong>{html.escape(t)}</strong></a><br>"
                       f"<span style=\"font-size:13px;color:#57503F\">{html.escape(d)}</span></li>")
        out.append("</ul>")
    return "".join(out)


hub_ld = ('<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": "Guides", "url": f"{SITE}/guides.html",
         "inLanguage": ["en", "ko"], "dateModified": TODAY,
         "hasPart": [{"@type": "Article", "headline": x['title_en'], "url": f"{SITE}/{x['slug']}.html"}
                     for x in GUIDES]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides.html"}]}]},
    ensure_ascii=False) + '</script>')

page('guides.html', 'Quit-smoking guides: cost, symptoms, support | Time Left',
     f'{len(GUIDES)} guides on what quitting does to your body, what the help costs in each country, '
     'and how to read the numbers in the calculator. Every fact is linked to an official source.',
     f"""<h1>Guides</h1>
<p class="sub">{len(GUIDES)} guides. Every number is linked to the official page it came from.</p>
<p class="upd">Last updated {UPD_EN}</p>
<p>The calculator gives you one number. These pages explain where it comes from, what happens in your body
after you stop, what the available help costs, and how much of a pack price is tax. Nothing here is medical
advice and nothing is behind a login.</p>
{hub('en')}
<p><a href="prices.html" data-keep>Prices in 31 countries →</a> · <a href="quitlines.html" data-keep>Free quitlines →</a></p>
{hub_ld}""",
     f"""<h1>가이드</h1>
<p class="sub">{len(GUIDES)}편. 모든 수치는 출처 페이지 링크와 함께 표기합니다.</p>
<p class="upd">최종 업데이트 {UPD_KO}</p>
<p>계산기는 숫자 하나를 보여줍니다. 이 글들은 그 숫자가 어디서 왔는지, 담배를 끊은 뒤 몸에서 무엇이 일어나는지,
각 나라에서 받을 수 있는 도움이 얼마인지, 담뱃값에서 세금이 얼마인지를 설명합니다. 의학적 조언이 아니며
로그인도 필요하지 않습니다.</p>
{hub('ko')}
<p><a href="prices.html" data-keep>31개국 담뱃값 →</a> · <a href="quitlines.html" data-keep>무료 금연상담전화 →</a></p>""")
made.append('guides.html')

print(f"  가이드 {len(GUIDES)}편 + 허브 1 = {len(made)}개")
open('work/guides_made.txt', 'w', encoding='utf-8').write("\n".join(made) + "\n")

if short:
    print("\n실패: 분량 미달 — 한국어 1,800자 / 영어 900단어")
    for s in short:
        print("  ", s)
    sys.exit(1)
print("분량 게이트 통과")
