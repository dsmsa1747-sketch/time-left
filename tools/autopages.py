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

<h2>Other countries</h2>
<p style="font-size:13px;line-height:2.1">{lnk_en}</p>
<p><a href="prices.html" data-keep>Compare all {len(W)} countries in one table →</a></p>"""

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

<h2>다른 나라</h2>
<p style="font-size:13px;line-height:2.1">{lnk_ko}</p>
<p><a href="prices.html" data-keep>{len(W)}개국 한 표로 비교 →</a></p>"""

    page(SLUG[cc],
         f"What smoking costs in {en} ({money(pack)} a pack) | Time Left",
         f"A pack in {en} costs about {money(pack)}. A pack a day is {money(yr)} and {yd} days of life expectancy a year. "
         f"Free quitline number and recovery timeline included.",
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
