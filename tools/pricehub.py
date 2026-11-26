#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pricehub.py — prices.html 을 데이터 허브로 바꾼다 (autopages.py 다음에 돌린다).

하는 일
  1) 31개국 표를 열 7개로 교체: 현지가 · USD · 개비당 · 하루 한 갑 1년 · 세금 비중 · 무료 상담전화 · 상세 링크
  2) 검색(국가명) + 정렬(가격/세금비중) — 외부 라이브러리 없이 인라인 JS
  3) "데이터 갱신 이력" 표와 인용 안내 문단 추가
손편집 금지: 값은 world.json / countryfacts.json / quitdata.json 에서만 온다.

실행: python tools/pricehub.py
"""
import json, os, re, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

TODAY = datetime.date.today().isoformat()
W = json.load(open('world.json', encoding='utf-8'))
CF = json.load(open('countryfacts.json', encoding='utf-8'))
CN = json.load(open('countries.json', encoding='utf-8'))
QL = json.load(open('quitdata.json', encoding='utf-8'))['q']

# 갱신 이력 — 새 줄을 위에 추가한다(날짜 · 바뀐 것 · 근거)
HISTORY = [
    (TODAY, '31 countries re-checked; tax share and quitline columns added',
     '31개국 재확인, 세금 비중·상담전화 열 추가',
     'tools/countryfacts.json (WHO GHO indicators) + tools/world.json'),
]

MARK = '<!--AUTO-PRICE-HUB-->'
TABLE = re.compile(r'<div class="tw"><table>.*?</table></div>', re.S)


def rows(lang):
    out = []
    for x in sorted(W, key=lambda r: -r['usd']):
        cc = x['c']
        name = CN.get(cc, [cc, cc, ''])[0 if lang == 'en' else 1]
        slug = CN.get(cc, [cc, cc, ''])[2]
        v = CF.get(cc, {})
        pct = v.get('tax_share_pct')
        tel = (QL.get(cc) or ['', ''])[1]
        stick = x['usd'] / x['per']
        yr = x['usd'] * 365
        link = (f"<a href=\"cost-of-smoking-{slug}.html\" data-keep>"
                + ('details' if lang == 'en' else '상세') + "</a>") if slug else ''
        out.append(
            f"<tr data-name=\"{html.escape(name.lower())}\" data-usd=\"{x['usd']:.4f}\" "
            f"data-tax=\"{pct if pct else 0}\">"
            f"<td><span class='flag'>{x['f']}</span>{html.escape(name)}</td>"
            f"<td class='r'>{html.escape(x['local'])}</td>"
            f"<td class='r'>${x['usd']:.2f}</td>"
            f"<td class='r'>${stick:.2f}</td>"
            f"<td class='r'>${yr:,.0f}</td>"
            f"<td class='r'>{f'{pct:g}%' if pct else '-'}</td>"
            f"<td class='r'>{f'<span class=\"tel\">{html.escape(tel)}</span>' if tel else '-'}</td>"
            f"<td class='r'>{link}</td></tr>")
    return "".join(out)


def controls(lang):
    if lang == 'en':
        ph, s1, s2, s3 = 'Search a country', 'Price', 'Tax share', 'Name'
        note = 'Tax share: WHO Global Health Observatory indicator, reference year on each country page. Dash = not published.'
    else:
        ph, s1, s2, s3 = '국가명 검색', '가격', '세금 비중', '국가명'
        note = '세금 비중: WHO 글로벌 보건 관측소 지표이며 기준연도는 각 국가 페이지에 있습니다. 대시(-)는 미공표.'
    return (f"<p><input class=\"pf\" type=\"search\" placeholder=\"{ph}\" "
            f"style=\"padding:8px 10px;border:1px solid #DED7C8;border-radius:7px;font:inherit;width:220px\"> "
            f"<button class=\"ps\" data-k=\"usd\">{s1} ↓</button> "
            f"<button class=\"ps\" data-k=\"tax\">{s2} ↓</button> "
            f"<button class=\"ps\" data-k=\"name\">{s3} ↑</button></p>"
            f"<p style=\"font-size:12.5px;color:#8B8270\">{note}</p>")


def head(lang):
    h = (('Country', 'Pack price', 'USD', 'Per cigarette', 'Pack a day, 1 year', 'Tax share', 'Free quitline', '')
         if lang == 'en' else
         ('국가', '한 갑 가격', 'USD', '개비당', '하루 한 갑 1년', '세금 비중', '무료 상담전화', ''))
    return "".join(f"<th{' class=\"r\"' if i else ''}>{c}</th>" for i, c in enumerate(h))


def history_block(lang):
    cap = 'Data update history' if lang == 'en' else '데이터 갱신 이력'
    hd = (('Date', 'What changed', 'Basis') if lang == 'en' else ('날짜', '바뀐 것', '근거'))
    body = "".join(f"<tr><td>{d}</td><td>{html.escape(en if lang == 'en' else ko)}</td>"
                   f"<td style=\"font-size:12px\">{html.escape(src)}</td></tr>"
                   for d, en, ko, src in HISTORY)
    cite = ('<h2>Citing this table</h2><p>Quote the local pack price with its currency, state the date you '
            'read it, and link this page. Pack prices are the values used across this site; USD figures are '
            'for comparison only and depend on the conversion applied. Tax share values come from WHO '
            'indicator data with their own reference year, so a row can mix a current price with an earlier '
            'tax year — read both columns together.</p>'
            if lang == 'en' else
            '<h2>이 표를 인용할 때</h2><p>현지 통화 기준 한 갑 가격과 읽은 날짜를 함께 적고 이 페이지를 '
            '링크해 주십시오. 한 갑 가격은 이 사이트 전체에서 쓰는 값이며, USD 값은 비교용으로 환산 방식에 '
            '따라 달라집니다. 세금 비중은 WHO 지표 데이터이고 자체 기준연도가 있어, 한 줄에 현재 가격과 '
            '이전 연도의 세금 비중이 섞일 수 있습니다. 두 열을 함께 읽으십시오.</p>')
    return (f"<h2>{cap}</h2><div class=\"tw\"><table><thead><tr>"
            + "".join(f"<th>{c}</th>" for c in hd)
            + f"</tr></thead><tbody>{body}</tbody></table></div>{cite}")


JS = """<script>(function(){
document.querySelectorAll('.pf').forEach(function(inp){
  inp.oninput=function(){var q=inp.value.trim().toLowerCase();
    var tb=inp.closest('[data-l]').querySelector('table tbody');
    tb.querySelectorAll('tr').forEach(function(tr){
      tr.hidden=!!q&&tr.dataset.name.indexOf(q)<0;});};});
document.querySelectorAll('.ps').forEach(function(b){
  b.onclick=function(){var k=b.dataset.k,tb=b.closest('[data-l]').querySelector('table tbody');
    var rs=[].slice.call(tb.querySelectorAll('tr'));var asc=b.dataset.asc==='1';b.dataset.asc=asc?'0':'1';
    rs.sort(function(x,y){var a,c;
      if(k==='name'){a=x.dataset.name;c=y.dataset.name;return asc?(a<c?1:-1):(a>c?1:-1);}
      a=parseFloat(x.dataset[k]);c=parseFloat(y.dataset[k]);return asc?a-c:c-a;});
    rs.forEach(function(tr){tb.appendChild(tr);});};});
})();</script>"""


p = open('dist/prices.html', encoding='utf-8').read()
if MARK in p:
    print("  prices.html   ← 이미 허브로 교체됨(건너뜀)")
    raise SystemExit(0)

langs = ['en', 'ko']
found = TABLE.findall(p)
if len(found) < 2:
    raise SystemExit(f"실패: prices.html 에서 표를 2개 찾지 못했다(찾은 수 {len(found)})")

i = 0
def repl(m):
    global i
    lang = langs[i] if i < len(langs) else langs[-1]
    i += 1
    return (f"{MARK}{controls(lang)}<div class=\"tw\"><table><thead><tr>{head(lang)}</tr></thead>"
            f"<tbody>{rows(lang)}</tbody></table></div>")

p = TABLE.sub(repl, p, count=2)

# 갱신 이력 + 인용 안내를 각 언어 블록 끝(계산기 링크 앞)에 넣는다
for lang in langs:
    anchor = '<a class="back" href="index.html" data-keep>' + ('← Open the calculator' if lang == 'en' else '← 계산기 열기')
    j = p.index(anchor)
    p = p[:j] + history_block(lang) + "\n" + p[j:]

p = p.replace('</body>', JS + '\n</body>')
open('dist/prices.html', 'w', encoding='utf-8').write(p)
print(f"  prices.html   ← 허브 교체: {len(W)}개국 x 7열 + 검색/정렬 + 갱신이력")
