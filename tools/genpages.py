import json, html
SITE = "https://quitminutes.com"
UPD_EN, UPD_KO = "27 September 2026", "2026년 9월 27일"

CSS = """*{box-sizing:border-box}
html{background:#F6F3EC}
body{margin:0;background:#F6F3EC;color:#17150F;font-family:"Noto Sans KR",system-ui,-apple-system,sans-serif;font-size:15px;line-height:1.75}
.w{max-width:760px;margin:0 auto;padding:26px 20px 80px}
a{color:#7A5A22}
nav.top{display:flex;flex-wrap:wrap;gap:4px;align-items:center;border-bottom:1px solid #DED7C8;padding-bottom:14px;margin-bottom:26px}
nav.top a{font-size:12.5px;color:#57503F;text-decoration:none;padding:6px 10px;border-radius:6px}
nav.top a:hover{background:#EFEAE0;color:#17150F}
nav.top a.home{font-weight:700;color:#17150F}
nav.top .sp{flex:1}
h1{font-family:"Noto Serif KR",serif;font-weight:900;font-size:28px;letter-spacing:-.025em;margin:0 0 8px;line-height:1.3;text-wrap:balance}
h2{font-family:"Noto Serif KR",serif;font-weight:900;font-size:19px;margin:34px 0 10px;letter-spacing:-.02em}
h3{font-size:15.5px;font-weight:700;margin:22px 0 6px}
.sub{color:#57503F;font-size:14px;margin:0 0 4px}
.upd{color:#8B8270;font-size:11.5px;margin:0 0 28px}
p,li{color:#3A342C}
ul,ol{padding-left:20px}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin:0;min-width:100%}
.tw table{min-width:440px}
th{text-align:left;font-size:11px;letter-spacing:.1em;color:#8B8270;font-weight:600;padding:0 10px 9px 0;border-bottom:1px solid #DED7C8;white-space:nowrap}
td{padding:9px 10px 9px 0;border-bottom:1px solid #EAE4D6;vertical-align:top}
th.r,td.r{text-align:right;padding-right:0;font-variant-numeric:tabular-nums;white-space:nowrap}
tr:hover td{background:#F1ECE1}
.flag{margin-right:7px}
.tel{font-weight:700;color:#2C7A56;font-variant-numeric:tabular-nums;white-space:nowrap}
.tel a{color:inherit;text-decoration:none}
.box{background:#FFFFFF;border:1px solid #DED7C8;border-radius:10px;padding:16px 18px;margin:20px 0}
.box p{margin:0;font-size:13.5px}
.box.warn{background:#FBF3F1;border-color:#E2C4BD}
.tl{list-style:none;padding:0;margin:18px 0}
.tl li{display:grid;grid-template-columns:110px 1fr;gap:16px;padding:12px 0;border-bottom:1px solid #EAE4D6}
.tl .t{font-weight:700;color:#2C7A56;font-variant-numeric:tabular-nums}
.lang{display:flex;gap:2px;background:#FFFFFF;border:1px solid #DED7C8;border-radius:7px;padding:2px;margin-left:auto}
.lang button{appearance:none;border:0;background:transparent;cursor:pointer;font-family:inherit;font-size:11.5px;font-weight:600;color:#8B8270;padding:5px 10px;border-radius:5px}
.lang button[aria-pressed="true"]{background:#EFEAE0;color:#17150F}
.back{display:inline-block;margin-top:36px;font-size:13.5px;font-weight:700;color:#17150F;text-decoration:none;border-bottom:2px solid #C6BCA8;padding-bottom:2px}
[hidden]{display:none!important}
@media(max-width:520px){.tl li{grid-template-columns:1fr;gap:2px}
 .tw table{font-size:12.5px}
 th,td{padding-right:8px}
 h1{font-size:24px}}"""

SCRIPT = """(function(){
  var L=(navigator.language||"en").toLowerCase().indexOf("ko")===0?"ko":"en";
  try{var q=new URLSearchParams(location.search).get("lang");if(q==="ko"||q==="en")L=q;}catch(e){}
  function set(l){L=l;document.documentElement.lang=l;
    document.querySelectorAll("[data-l]").forEach(function(e){e.hidden=e.getAttribute("data-l")!==l;});
    document.querySelectorAll(".lang button").forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.set===l));});
    document.querySelectorAll("a[data-keep]").forEach(function(a){
      try{var u=new URL(a.href,location.href);u.searchParams.set("lang",l);a.href=u.pathname+u.search;}catch(e){}});
  }
  document.querySelectorAll(".lang button").forEach(function(b){b.onclick=function(){set(b.dataset.set);};});
  set(L);
})();"""

NAV = """<nav class="top">
<a class="home" href="index.html" data-keep>Time Left</a>
<a href="timeline.html" data-keep data-l="en">Recovery timeline</a><a href="timeline.html" data-keep data-l="ko" hidden>회복 타임라인</a>
<a href="prices.html" data-keep data-l="en">Prices worldwide</a><a href="prices.html" data-keep data-l="ko" hidden>나라별 담뱃값</a>
<a href="quitlines.html" data-keep data-l="en">Quitlines</a><a href="quitlines.html" data-keep data-l="ko" hidden>금연상담전화</a>
<a href="about.html" data-keep data-l="en">About</a><a href="about.html" data-keep data-l="ko" hidden>소개</a>
<div class="sp"></div>
<div class="lang" role="group" aria-label="Language">
<button data-set="en" aria-pressed="true">EN</button><button data-set="ko" aria-pressed="false">한국어</button>
</div>
</nav>"""

def page(fname, title, desc, body_en, body_ko):
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#F6F3EC">
<link rel="canonical" href="{SITE}/{fname}">
<link rel="alternate" hreflang="en" href="{SITE}/{fname}?lang=en">
<link rel="alternate" hreflang="ko" href="{SITE}/{fname}?lang=ko">
<link rel="alternate" hreflang="x-default" href="{SITE}/{fname}">
<link rel="icon" href="favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Time Left">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:url" content="{SITE}/{fname}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700&family=Noto+Serif+KR:wght@900&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="w">
{NAV}
<div data-l="en">{body_en}
<a class="back" href="index.html" data-keep>← Open the calculator</a></div>
<div data-l="ko" hidden>{body_ko}
<a class="back" href="index.html" data-keep>← 계산기 열기</a></div>
</div>
<script>{SCRIPT}</script>
</body>
</html>"""
    open('dist/'+fname, 'w', encoding='utf-8').write(doc)
    print(f'  {fname:16} {len(doc):>7,} bytes')

print("generating…")

W = json.load(open('world.json'))
Q = json.load(open('quitdata.json'))

# ─────────── prices.html ───────────
rows_en, rows_ko = [], []
for x in sorted(W, key=lambda r: -r['usd']):
    per   = x['per']
    stick = x['usd']/per
    mins  = 17*per            # minutes of life in one pack (men, UCL 2024)
    yr    = x['usd']*365
    rows_en.append(f"<tr><td><span class='flag'>{x['f']}</span>{x['c']}</td>"
                   f"<td class='r'>{x['local']}</td><td class='r'>${x['usd']:.2f}</td>"
                   f"<td class='r'>{per}</td><td class='r'>${stick:.2f}</td>"
                   f"<td class='r'>${yr:,.0f}</td></tr>")
    rows_ko.append(f"<tr><td><span class='flag'>{x['f']}</span>{x['c']}</td>"
                   f"<td class='r'>{x['local']}</td><td class='r'>${x['usd']:.2f}</td>"
                   f"<td class='r'>{per}</td><td class='r'>${stick:.2f}</td>"
                   f"<td class='r'>${yr:,.0f}</td></tr>")

p_en = f"""<h1>What a pack of cigarettes costs, country by country</h1>
<p class="sub">{len(W)} countries · pack price, price per cigarette, and what a pack a day costs in a year</p>
<p class="upd">Last updated {UPD_EN}</p>

<p>The price of the same habit varies by more than ten times depending on where you live. In Australia a pack-a-day
smoker spends more on cigarettes in a year than many people spend on a used car. In Turkey the same habit costs
roughly a twentieth of that. Below is the comparison, with the per-cigarette figure worked out, because that is the
number that matters when someone asks you for one.</p>

<div class="box"><p><b>How to read this.</b> USD figures are converted at 2026 rates and move with the exchange rate.
The local price is the one to trust. "Per cigarette" is the pack price divided by the number of sticks in it — not
every country sells packs of 20.</p></div>

<div class="tw"><table>
<thead><tr><th>Country</th><th class="r">Local price</th><th class="r">USD</th><th class="r">Sticks</th><th class="r">Per stick</th><th class="r">A year, pack a day</th></tr></thead>
<tbody>{''.join(rows_en)}</tbody>
</table></div>

<h2>What the money is not the whole story</h2>
<p>A pack of 20 also costs about <b>340 minutes of life</b> — roughly five and a half hours — using the 17-minutes-per-cigarette
figure from University College London's 2024 analysis. A pack a day for a year is about <b>86 days</b>. That number does not
change with the exchange rate, and it is the same in every country on this table.</p>

<h2>Sources and caveats</h2>
<ul>
<li>Pack prices: public sources, 2026. Prices change frequently, often with tax rises — check your own.</li>
<li>Life-minutes: University College London, 2024. About 17 minutes per cigarette for men, 22 for women. It is a
population average, not a prediction about any individual.</li>
<li>Annual figures assume one pack every day for 365 days.</li>
</ul>"""

p_ko = f"""<h1>나라별 담뱃값 — 한 갑, 한 개비, 그리고 1년</h1>
<p class="sub">{len(W)}개국 · 갑당 가격, 개비당 가격, 하루 한 갑 1년 비용</p>
<p class="upd">최종 갱신 {UPD_KO}</p>

<p>같은 습관인데 사는 곳에 따라 값이 열 배 넘게 차이 납니다. 호주에서 하루 한 갑을 피우면 1년에
중고차 한 대 값이 나갑니다. 튀르키예에서는 그 이십분의 일쯤입니다. 아래 표에 개비당 가격까지
계산해 두었습니다. 누가 한 개비만 달라고 할 때 실제로 의미 있는 숫자는 그것이기 때문입니다.</p>

<div class="box"><p><b>보는 법.</b> 달러 환산액은 2026년 환율 기준이라 환율 따라 움직입니다. 믿을 것은
현지 가격입니다. "개비당"은 갑 가격을 개비 수로 나눈 값이고, 모든 나라가 20개비들이를 파는 것은 아닙니다.</p></div>

<div class="tw"><table>
<thead><tr><th>국가</th><th class="r">현지 가격</th><th class="r">USD</th><th class="r">개비</th><th class="r">개비당</th><th class="r">하루 한 갑 · 1년</th></tr></thead>
<tbody>{''.join(rows_ko)}</tbody>
</table></div>

<h2>돈이 전부가 아닙니다</h2>
<p>20개비 한 갑은 <b>약 340분의 수명</b>, 다섯 시간 반쯤이기도 합니다. 유니버시티 칼리지 런던의
2024년 분석에서 나온 개비당 17분을 적용한 값입니다. 하루 한 갑을 1년이면 <b>약 86일</b>입니다.
이 숫자는 환율로 변하지 않고, 위 표의 어느 나라에서나 똑같습니다.</p>

<h2>출처와 한계</h2>
<ul>
<li>담뱃값: 2026년 공개자료. 세금 인상 등으로 자주 바뀌니 직접 확인하세요.</li>
<li>수명 분: University College London, 2024. 남성 약 17분, 여성 약 22분.
집단 평균이며 개인에 대한 예측이 아닙니다.</li>
<li>연간 금액은 365일 매일 한 갑 기준입니다.</li>
</ul>"""

page('prices.html',
     'Cigarette Prices by Country — Per Pack, Per Cigarette, Per Year | Time Left',
     f'Pack prices in {len(W)} countries with the per-cigarette cost worked out, plus what a pack a day costs over a year. Updated 2026.',
     p_en, p_ko)

# ─────────── quitlines.html ───────────
qs = sorted(Q['q'].items(), key=lambda kv: kv[1][0])
def qrows():
    out=[]
    for code,(name,tel) in qs:
        tel_link = tel.replace(' ','').replace('-','')
        out.append(f"<tr><td>{html.escape(name)}</td><td class='r tel'>"
                   f"<a href='tel:{tel_link}'>{html.escape(tel)}</a></td></tr>")
    return ''.join(out)

q_en = f"""<h1>Stop-smoking helplines, {len(qs)} countries</h1>
<p class="sub">National quitlines you can call for free or low-cost help</p>
<p class="upd">Last updated {UPD_EN}</p>

<p>Most countries run a national quitline. They are usually free, usually staffed by trained counsellors, and in many
countries they can arrange nicotine replacement or medication at no cost. People who use one are measurably more
likely to still be smoke-free a year later than people who try alone.</p>

<div class="box"><p><b>You do not have to be ready to quit to call.</b> Counsellors talk to people who are still
undecided every day. You can ask what the options are and hang up without committing to anything.</p></div>

<div class="tw"><table>
<thead><tr><th>Country</th><th class="r">Number</th></tr></thead>
<tbody>{qrows()}</tbody>
</table></div>

<h2>If your country is not listed</h2>
<p>Ask a pharmacist or your doctor — in most countries they can refer you, and in many they can prescribe
nicotine replacement or medication directly. The World Health Organization also maintains country-level
tobacco control information that usually names the national service.</p>

<h2>What a quitline actually does</h2>
<ul>
<li>Talks through what has and has not worked for you before</li>
<li>Helps set a quit date and plan around the situations that usually break it</li>
<li>Explains the difference between patches, gum, lozenges and prescription medication</li>
<li>In many countries, arranges those at reduced cost or free</li>
<li>Calls you back — scheduled follow-up is a large part of why they work</li>
</ul>

<div class="box warn"><p>Numbers change. If one does not connect, search for your country's health ministry
rather than assuming the service has closed. Corrections are welcome at
<a href="mailto:dsmsa1747@gmail.com">dsmsa1747@gmail.com</a>.</p></div>"""

q_ko = f"""<h1>전 세계 금연상담전화 {len(qs)}개국</h1>
<p class="sub">무료 또는 저비용으로 도움받을 수 있는 각국 공식 상담전화</p>
<p class="upd">최종 갱신 {UPD_KO}</p>

<p>대부분의 나라가 국가 금연상담전화를 운영합니다. 보통 무료이고, 훈련받은 상담사가 받으며,
여러 나라에서 니코틴 보조제나 약물을 무상으로 연결해 줍니다. 상담전화를 이용한 사람은 혼자
시도한 사람보다 1년 뒤까지 금연을 유지할 확률이 유의하게 높습니다.</p>

<div class="box"><p><b>끊을 준비가 돼야 거는 곳이 아닙니다.</b> 상담사들은 아직 망설이는 사람과
매일 이야기합니다. 어떤 방법이 있는지만 물어보고 끊으셔도 됩니다.</p></div>

<div class="tw"><table>
<thead><tr><th>국가</th><th class="r">번호</th></tr></thead>
<tbody>{qrows()}</tbody>
</table></div>

<h2>한국에서는</h2>
<p><b>금연상담전화 1544-9030</b> 이 국가 서비스입니다. 이와 별도로 전국 보건소에서
<b>금연클리닉</b>을 무료로 운영하며, 상담과 함께 니코틴 보조제를 제공합니다.
병·의원 금연치료는 건강보험이 적용되고, 프로그램을 끝까지 이수하면 본인부담금을 돌려받습니다.</p>

<h2>상담전화가 실제로 해주는 일</h2>
<ul>
<li>전에 무엇이 통했고 무엇이 안 통했는지 같이 짚어줍니다</li>
<li>금연 시작일을 정하고, 늘 무너지던 상황에 대한 계획을 세웁니다</li>
<li>패치·껌·트로키·처방약의 차이를 설명해 줍니다</li>
<li>여러 나라에서 그것들을 무료 또는 저렴하게 연결해 줍니다</li>
<li>다시 전화를 걸어줍니다 — 이 후속 연락이 효과의 큰 부분입니다</li>
</ul>

<div class="box warn"><p>번호는 바뀝니다. 연결이 안 되면 서비스가 없어졌다고 단정하지 마시고
해당국 보건당국을 찾아보세요. 정정 제보는 <a href="mailto:dsmsa1747@gmail.com">dsmsa1747@gmail.com</a>.</p></div>"""

page('quitlines.html',
     f'Stop-Smoking Helplines in {len(qs)} Countries — National Quitline Numbers | Time Left',
     f'A directory of national stop-smoking helplines for {len(qs)} countries, with what a quitline does and how to reach one. Free to call in most countries.',
     q_en, q_ko)

# ─────────── timeline.html ───────────
def tl(lang):
    out=[]
    for t in Q['tl']:
        a,b = t[lang]
        out.append(f"<li><span class='t'>{html.escape(a)}</span><span>{html.escape(b)}</span></li>")
    return ''.join(out)

t_en = f"""<h1>What happens to your body after your last cigarette</h1>
<p class="sub">The World Health Organization recovery timeline, from twenty minutes to fifteen years</p>
<p class="upd">Last updated {UPD_EN}</p>

<p>Recovery starts faster than most people expect. The first measurable change happens before you have finished
the hour. Below is the timeline as the World Health Organization publishes it.</p>

<ol class="tl">{tl('en')}</ol>

<h2>What this timeline is, and is not</h2>
<p>It describes <b>what happens on average</b>. It is not a promise about any one person. How long you smoked, how
much, your genetics, and what else you have been exposed to all change the picture. Two people who quit on the same
day do not recover on the same schedule.</p>

<div class="box warn"><p><b>Lungs do not return to new.</b> This is worth being straight about, because a lot of
quitting advice is not. Scarring and emphysema do not reverse. What the evidence shows is that the damage
<i>stops accumulating</i>, that cilia regrow and the airways clear themselves again, and that long-term disease risk
falls a great deal. That is a smaller claim than "your lungs heal completely" — and it is the true one.</p></div>

<h2>The parts people find most surprising</h2>
<h3>Twenty minutes</h3>
<p>Heart rate and blood pressure drop. Nicotine is a stimulant and its effect on the cardiovascular system starts
unwinding almost immediately.</p>
<h3>Twelve hours</h3>
<p>Carbon monoxide in the blood returns to normal. Carbon monoxide binds to haemoglobin in place of oxygen, so this
is the point at which blood starts carrying a normal amount of oxygen again.</p>
<h3>Two weeks to three months</h3>
<p>Circulation improves and lung function begins to rise. This is usually when people notice stairs and walking
uphill feel different.</p>
<h3>Ten years</h3>
<p>The risk of dying from lung cancer is about half that of someone who kept smoking. Not zero — half.</p>

<h2>Quitting later still works</h2>
<p>There is a common belief that after a certain age or a certain number of years there is no point. The evidence
does not support it. The benefit is smaller the longer you smoked, but it is present at every age studied, including
in people who quit in their sixties and seventies.</p>

<h2>Sources</h2>
<ul>
<li>Recovery timeline: World Health Organization.</li>
<li>Life-minutes per cigarette: University College London, 2024 — about 17 minutes for men, 22 for women.</li>
<li>This page is information, not medical advice. For what applies to you specifically, talk to a doctor or
pharmacist, or call your country's <a href="quitlines.html" data-keep>national quitline</a>.</li>
</ul>"""

t_ko = f"""<h1>마지막 담배 이후, 몸에서 일어나는 일</h1>
<p class="sub">세계보건기구(WHO) 회복 타임라인 — 20분부터 15년까지</p>
<p class="upd">최종 갱신 {UPD_KO}</p>

<p>회복은 생각보다 빨리 시작됩니다. 첫 번째 측정 가능한 변화는 한 시간도 지나기 전에 일어납니다.
아래는 세계보건기구가 발표한 타임라인 그대로입니다.</p>

<ol class="tl">{tl('ko')}</ol>

<h2>이 타임라인이 말하는 것과 말하지 않는 것</h2>
<p><b>평균적으로 일어나는 일</b>을 설명합니다. 개인에 대한 약속이 아닙니다. 얼마나 오래, 얼마나 많이
피웠는지, 유전, 그 밖의 노출이 결과를 바꿉니다. 같은 날 끊은 두 사람이 같은 속도로 회복하지 않습니다.</p>

<div class="box warn"><p><b>폐는 새것으로 돌아가지 않습니다.</b> 이건 분명히 해두겠습니다. 금연 안내문 중에
그렇지 않은 것이 많기 때문입니다. 이미 생긴 흉터와 폐기종은 되돌아가지 않습니다. 근거가 보여주는 것은
손상이 <i>더 쌓이지 않는다</i>는 것, 섬모가 다시 자라 기도가 스스로 청소된다는 것, 장기적인 질병 위험이
크게 떨어진다는 것입니다. "폐가 완전히 깨끗해진다"보다 작은 주장이고, 이쪽이 사실입니다.</p></div>

<h2>사람들이 가장 놀라는 대목</h2>
<h3>20분</h3>
<p>심박수와 혈압이 떨어집니다. 니코틴은 각성제이고, 심혈관계에 준 영향이 거의 즉시 풀리기 시작합니다.</p>
<h3>12시간</h3>
<p>혈중 일산화탄소가 정상으로 돌아옵니다. 일산화탄소는 산소 대신 헤모글로빈에 달라붙기 때문에,
이 시점부터 피가 다시 정상적인 양의 산소를 나릅니다.</p>
<h3>2주~3개월</h3>
<p>순환이 좋아지고 폐 기능이 오르기 시작합니다. 계단이나 오르막이 달라졌다고 느끼는 시점이 보통 여기입니다.</p>
<h3>10년</h3>
<p>폐암으로 사망할 위험이 계속 피운 사람의 절반 수준이 됩니다. 0이 아니라 절반입니다.</p>

<h2>늦게 끊어도 효과가 있습니다</h2>
<p>몇 살이 넘으면, 몇 년을 피웠으면 소용없다는 말이 흔한데 근거가 뒷받침하지 않습니다. 오래 피울수록
회복 폭이 작아지는 것은 맞지만, 연구된 모든 연령대에서 이득이 확인됩니다. 60대·70대에 끊은 사람도 포함해서입니다.</p>

<h2>출처</h2>
<ul>
<li>회복 타임라인: 세계보건기구(WHO)</li>
<li>개비당 수명: University College London, 2024 — 남성 약 17분, 여성 약 22분</li>
<li>이 페이지는 정보이며 의학적 조언이 아닙니다. 본인에게 해당하는 내용은 의사·약사와 상의하시거나
<a href="quitlines.html" data-keep>각국 금연상담전화</a>로 문의하세요.</li>
</ul>"""

page('timeline.html',
     'What Happens After You Quit Smoking — The WHO Recovery Timeline | Time Left',
     'The World Health Organization timeline from 20 minutes to 15 years after your last cigarette, with an honest note on what does and does not reverse.',
     t_en, t_ko)

# ─────────── about.html ───────────
a_en = f"""<h1>About Time Left</h1>
<p class="sub">A free stop-smoking tool. No account, no server, no data collection.</p>
<p class="upd">Last updated {UPD_EN}</p>

<h2>Why this exists</h2>
<p>Most stop-smoking material talks in abstractions — "smoking is harmful", "quitting is good for you". Those
statements are true and almost nobody changes because of them. What moves people is a specific number about their
own life: how much money has already gone, how much time has already gone, and what is still recoverable.</p>
<p>Time Left does that arithmetic. You enter your age, when you started, how much you smoke and what a pack costs
where you live. It shows you the total, and then it shows you the World Health Organization recovery timeline
counting up from your last cigarette.</p>

<h2>How it works</h2>
<ul>
<li><b>Everything stays in your browser.</b> There is no server and no account. Your age, your smoking history and
your daily record are held in your device's local storage and never transmitted. We could not read them if we wanted to.</li>
<li><b>It works offline.</b> Once loaded it installs as a web app and keeps running without a connection.</li>
<li><b>It is free.</b> Advertising pays for it. Nothing you enter is passed to an advertiser or used for targeting.</li>
<li><b>Two languages.</b> English and Korean, switched automatically by your browser setting.</li>
<li><b>{len(W)} countries' real prices and {len(qs)} countries' quitlines</b> are built in, so the numbers are in your
own currency and the helpline is one you can actually dial.</li>
</ul>

<h2>Where the numbers come from</h2>
<div class="tw"><table>
<thead><tr><th>Figure</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Minutes of life per cigarette</td><td>University College London, 2024 — about 17 minutes for men, 22 for women</td></tr>
<tr><td>Recovery timeline</td><td>World Health Organization</td></tr>
<tr><td>Life expectancy baseline</td><td>2024 national life table; adjustable in the app</td></tr>
<tr><td>Pack warning images</td><td>Korean Ministry of Health and Welfare, 5th round (valid to 22 December 2026)</td></tr>
<tr><td>Cigarette prices</td><td>Public sources, 2026</td></tr>
<tr><td>Quitline numbers</td><td>National health services of each listed country</td></tr>
</tbody>
</table></div>

<h2>What this tool is careful not to claim</h2>
<div class="box warn"><p>Every figure here is a <b>population average</b>, not a forecast about you. Bodies differ.
And lungs do not return to new — scarring does not reverse. What stops is the accumulation of new damage. We would
rather say the smaller true thing than the larger comforting one, because an app that overstates its case is an app
you stop believing.</p></div>

<h2>Age rating</h2>
<p>The app contains the official pack warning photographs, which are graphic surgical and disease images. They stay
blurred until you choose to reveal them. Suitable for ages 15 and over.</p>

<h2>Who makes it</h2>
<p>Time Left is built and maintained by DS Company (디에스컴퍼니), a one-person operation in South Korea.
It is not affiliated with any tobacco company, pharmaceutical company, health authority or advertiser.
No advertiser has any influence over the content or the figures.</p>

<h2>Contact</h2>
<p>Corrections, a quitline number that has changed, a price that is wrong, or anything else:
<a href="mailto:dsmsa1747@gmail.com">dsmsa1747@gmail.com</a></p>
<p>See also the <a href="privacy.html" data-keep>Privacy Policy</a> and <a href="terms.html" data-keep>Terms of Use</a>.</p>"""

a_ko = f"""<h1>Time Left 소개</h1>
<p class="sub">무료 금연 도구. 계정도, 서버도, 데이터 수집도 없습니다.</p>
<p class="upd">최종 갱신 {UPD_KO}</p>

<h2>왜 만들었나</h2>
<p>금연 안내문은 대부분 추상적으로 말합니다 — "흡연은 해롭습니다", "금연은 좋습니다". 맞는 말이고
그 말 때문에 바뀌는 사람은 거의 없습니다. 사람을 움직이는 것은 자기 인생에 대한 구체적인 숫자입니다.
돈이 얼마나 나갔는지, 시간이 얼마나 갔는지, 그리고 아직 되찾을 수 있는 것이 무엇인지.</p>
<p>Time Left 는 그 계산을 합니다. 나이, 시작한 나이, 하루 흡연량, 사는 곳의 담뱃값을 넣으면 합계를
보여주고, 마지막 담배 시각부터 세계보건기구 회복 타임라인을 세어 올립니다.</p>

<h2>어떻게 동작하나</h2>
<ul>
<li><b>전부 브라우저 안에만 있습니다.</b> 서버도 계정도 없습니다. 나이·흡연 이력·매일의 기록은
기기 저장소에만 있고 전송되지 않습니다. 저희가 보고 싶어도 볼 수 없습니다.</li>
<li><b>오프라인에서 돕니다.</b> 한 번 열면 앱처럼 설치되어 연결 없이도 작동합니다.</li>
<li><b>무료입니다.</b> 광고로 운영됩니다. 입력하신 내용은 광고주에게 넘어가지 않고 타게팅에도 쓰이지 않습니다.</li>
<li><b>한국어·영어</b> 를 브라우저 설정에 따라 자동 전환합니다.</li>
<li><b>{len(W)}개국 실제 담뱃값과 {len(qs)}개국 금연상담전화</b> 가 들어 있어, 금액은 본인 통화로,
상담전화는 실제로 걸 수 있는 번호로 나옵니다.</li>
</ul>

<h2>숫자의 출처</h2>
<div class="tw"><table>
<thead><tr><th>항목</th><th>출처</th></tr></thead>
<tbody>
<tr><td>개비당 수명</td><td>University College London, 2024 — 남성 약 17분, 여성 약 22분</td></tr>
<tr><td>회복 타임라인</td><td>세계보건기구(WHO)</td></tr>
<tr><td>기대수명 기준</td><td>2024년 생명표. 앱에서 직접 조정 가능</td></tr>
<tr><td>담뱃갑 경고그림</td><td>보건복지부 제5기 (2026년 12월 22일까지 유효)</td></tr>
<tr><td>담뱃값</td><td>2026년 공개자료</td></tr>
<tr><td>금연상담전화</td><td>각국 보건당국</td></tr>
</tbody>
</table></div>

<h2>이 앱이 하지 않는 주장</h2>
<div class="box warn"><p>여기 모든 수치는 <b>집단 평균</b>이며 회장님 개인에 대한 예측이 아닙니다.
몸은 사람마다 다릅니다. 그리고 폐는 새것으로 돌아가지 않습니다 — 이미 생긴 흉터는 되돌아가지 않습니다.
멈추는 것은 새로운 손상의 축적입니다. 크고 듣기 좋은 말보다 작고 사실인 말을 하겠습니다.
과장하는 앱은 결국 믿지 않게 되기 때문입니다.</p></div>

<h2>연령 등급</h2>
<p>앱에는 공식 담뱃갑 경고그림이 들어 있습니다. 수술 장면과 질환 사진이라 수위가 높아, 직접 누르실
때까지 흐리게 가려 둡니다. 15세 이상 이용가입니다.</p>

<h2>만드는 곳</h2>
<p>Time Left 는 디에스컴퍼니(DS Company)가 만들고 운영합니다. 한국의 1인 사업장입니다.
담배회사·제약회사·보건당국·광고주 어느 쪽과도 제휴 관계가 없습니다. 어떤 광고주도 내용이나
수치에 영향을 주지 않습니다.</p>

<h2>문의</h2>
<p>바뀐 상담전화 번호, 틀린 가격, 그 밖의 정정 제보:
<a href="mailto:dsmsa1747@gmail.com">dsmsa1747@gmail.com</a></p>
<p><a href="privacy.html" data-keep>개인정보처리방침</a> ·
<a href="terms.html" data-keep>이용약관</a> 도 함께 보세요.</p>"""

page('about.html',
     'About Time Left — A Free Stop-Smoking Calculator | Time Left',
     'Who makes Time Left, where every figure comes from, and what the tool deliberately does not claim. No account, no server, nothing you enter is collected.',
     a_en, a_ko)

# ─────────── privacy / terms — 기존 본문 그대로, 새 틀로 재발행 ───────────
L = json.load(open('legal_bodies.json'))
page('privacy.html',
     'Privacy Policy — Nothing You Enter Is Collected | Time Left',
     'Everything you type into Time Left stays in your own browser. No server, no account, no database. How advertising works and how to opt out of personalised ads.',
     L['privacy.html'][0], L['privacy.html'][1])
page('terms.html',
     'Terms of Use — Not Medical Advice | Time Left',
     'Time Left is an information and motivation tool, not medical advice. Every figure is a population average, not a forecast about any individual.',
     L['terms.html'][0], L['terms.html'][1])
