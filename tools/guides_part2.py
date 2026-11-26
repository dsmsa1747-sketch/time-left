# -*- coding: utf-8 -*-
"""가이드 4~6. 확인된 출처(work/guide_probe.json)에서만 인용한다."""

GUIDES = [

# ─────────────────────────────── 4
{
 'slug': 'guide-20-minutes-per-cigarette',
 'cat': 'money',
 'title_en': 'Where the "20 minutes per cigarette" figure comes from, and what it cannot tell you',
 'desc_en': 'How per-cigarette life expectancy estimates are built, why the male and female figures differ, what WHO publishes about years gained by quitting, and the limits of population averages.',
 'h1_en': 'Where "one cigarette, 20 minutes" comes from',
 'h1_ko': '"담배 한 개비 = 20분"은 어떤 숫자인가',
 'sub_en': 'How the arithmetic works, what WHO publishes about years gained, and what an average cannot promise.',
 'sub_ko': '계산 방식, WHO가 공표한 기대수명 이득, 그리고 평균이 약속할 수 없는 것.',
 'srcs': ['who_cessation_qa', 'ucl_research', 'ucl_news_quit'],
 'rel': [('guide-using-quitminutes.html', 'How to read this calculator', '이 계산기를 제대로 쓰는 법'),
         ('timeline.html', 'The recovery timeline', '회복 타임라인'),
         ('prices.html', 'Prices in 31 countries', '31개국 담뱃값 비교'),
         ('guide-first-72-hours.html', 'The first 72 hours', '금연 첫 72시간')],
 'body_en': """
<p>This site converts cigarettes into minutes. That conversion deserves an explanation, because a sentence like
"one cigarette costs about twenty minutes of life" is easy to repeat and easy to misread. The arithmetic is
simple. The interpretation is where people go wrong, in both directions — treating it as a prophecy, or
dismissing it as a slogan.</p>

<h2>What the figure is</h2>
<p>A per-cigarette minute estimate is population arithmetic. You start from the difference in average life
expectancy between people who smoke and people who do not, divide by the number of cigarettes an average
smoker smokes over a smoking lifetime, and you get an average number of minutes per cigarette. Estimates of
this kind are reported separately for men and women, because both the life expectancy gap and typical
consumption differ. That is why this site uses two values rather than one and labels which is which.</p>

<div class="tw"><table><thead><tr><th>Input</th><th>What it is</th><th>Why it varies</th></tr></thead><tbody>
<tr><td>Life expectancy gap</td><td>Average years of life expectancy difference between smokers and non-smokers</td><td>Cohort, country, decade, and how heavily that cohort smoked</td></tr>
<tr><td>Lifetime cigarettes</td><td>How many cigarettes an average smoker consumes across the smoking years</td><td>Daily consumption, age at starting, age at stopping</td></tr>
<tr><td>Result</td><td>Average minutes of life expectancy per cigarette</td><td>Moves with either input; reported separately for men and women</td></tr>
</tbody></table></div>

<h2>What it is not</h2>
<ul>
<li><strong>Not a countdown for you.</strong> It is a population average. No individual's remaining life is being debited in real time by a fixed number of minutes.</li>
<li><strong>Not a causal claim about one cigarette.</strong> Harm from smoking accumulates over years of exposure. The per-cigarette figure is an accounting convenience for a long-run effect, not a measurement of what a single cigarette does.</li>
<li><strong>Not a reason to think small reductions are pointless.</strong> The honest reading cuts both ways: an average promises no one a specific outcome, and it also does not excuse the direction of the effect, which is not in dispute.</li>
<li><strong>Not interchangeable between sexes.</strong> A figure quoted without saying whether it is the male or the female estimate is being quoted loosely.</li>
</ul>

<div class="box"><p><strong>A note on sourcing.</strong> The widely circulated 2024 analysis behind the
17-minute and 22-minute estimates came from researchers in the UCL Research Department of Behavioural Science
and Health, a department whose research covers tobacco and alcohol use among other public health topics. On the
confirmation date shown at the top of this page, the original press release URL for that analysis did not
resolve (HTTP 404), so this page does not quote it. The department page and a current UCL smoking-cessation
news item are cited instead, and the interpretation below rests on figures WHO publishes directly.</p></div>

<h2>The figure WHO publishes instead</h2>
<p>For an authoritative number on what quitting buys, WHO's question-and-answer page on the health benefits of
smoking cessation states it in years rather than minutes, measured against people who continued smoking:
quitting at about 30 gains almost 10 years of life expectancy, at about 40 gains 9 years, at about 50 gains 6
years, and at about 60 gains 3 years. WHO also records that people who quit smoking after a heart attack
reduce their chances of having another heart attack by 50%.</p>

<p>Those four numbers are more useful than any per-cigarette estimate, for two reasons. They are stated in the
unit decisions are actually made in, and they are indexed to age — which answers the question most long-term
smokers are really asking, which is whether it is too late.</p>

<h2>Why minutes still work better on a screen</h2>
<p>Years are the right unit for a policy document and the wrong unit for a Tuesday afternoon. "You would gain
six years" is abstract. "This pack is about six hours" is a size you can hold. That is the only reason this
site uses minutes: the same information at a scale that fits one decision. The calculator shows money and time
together and keeps counting rather than presenting a single total, because the running aggregate is what makes
a per-unit figure feel real.</p>

<h2>Quit success is not uniform either</h2>
<p>Averages hide variation on the quitting side as well. A November 2026 UCL news item reports that
middle-aged women aged 45 to 60 had the lowest quit success at 18.1%, compared with 22.3% among younger women
and 20.6% among older women, and that the lowest success was among middle-aged women from more deprived
backgrounds at 15.8%. The researchers note that women in mid-life often face a combination of pressures that
can make quitting particularly challenging, and that women from more disadvantaged backgrounds are also more
likely to have higher levels of nicotine dependence, which can make quitting harder.</p>

<p>The practical reading is not pessimistic. It means a failed attempt is a common outcome rather than a
personal verdict, and that support is what moves those percentages: free coaching, a stop-smoking service, two
nicotine replacement products instead of one. See the
<a href="guide-nicotine-replacement.html" data-keep>product comparison</a> and the
<a href="quitlines.html" data-keep>free quitline list</a>.</p>

<h2>Checklist: using the number honestly</h2>
<ul>
<li>State whether you are quoting the male or the female estimate.</li>
<li>Treat it as a population average, never as a personal countdown.</li>
<li>Use WHO's years-gained figures when the question is "is it too late for me".</li>
<li>Do not stack the per-cigarette figure on top of other estimates to produce a dramatic total; the inputs overlap.</li>
<li>Check the date on every figure, including ours — see <a href="guide-using-quitminutes.html" data-keep>how this calculator works</a>.</li>
</ul>
""",
 'body_ko': """
<p>이 사이트는 담배를 분으로 환산합니다. 그 환산에는 설명이 필요합니다. "담배 한 개비가 수명 약 20분" 같은
문장은 옮기기 쉽고 오해하기도 쉽습니다. 계산은 단순합니다. 문제는 해석이고, 사람들은 양쪽으로 틀립니다.
예언으로 받아들이거나, 구호로 치부합니다.</p>

<h2>이 숫자가 무엇인가</h2>
<p>개비당 분 추정치는 인구 집단 산수입니다. 흡연자와 비흡연자의 평균 기대수명 차이에서 출발해, 평균적인
흡연자가 흡연 기간 동안 피우는 담배 개수로 나누면 개비당 평균 분이 나옵니다. 이런 추정치는 남성과 여성을 나눠
보고됩니다. 기대수명 차이와 평균 소비량이 둘 다 다르기 때문입니다. 그래서 이 사이트도 하나가 아니라 두 값을
쓰고, 어느 쪽 값인지 표시합니다.</p>

<div class="tw"><table><thead><tr><th>입력</th><th>무엇인가</th><th>왜 달라지는가</th></tr></thead><tbody>
<tr><td>기대수명 차이</td><td>흡연자와 비흡연자의 평균 기대수명 격차</td><td>코호트·국가·연대, 그 집단의 흡연량</td></tr>
<tr><td>평생 흡연 개수</td><td>평균 흡연자가 흡연 기간 동안 피우는 담배 수</td><td>하루 흡연량, 시작 연령, 중단 연령</td></tr>
<tr><td>결과</td><td>개비당 평균 기대수명 분</td><td>두 입력 중 하나만 바뀌어도 변함. 남녀 따로 보고</td></tr>
</tbody></table></div>

<h2>이 숫자가 아닌 것</h2>
<ul>
<li><strong>개인의 카운트다운이 아니다.</strong> 인구 평균입니다. 누군가의 남은 생이 실시간으로 정해진 분만큼 차감되고 있는 것이 아닙니다.</li>
<li><strong>한 개비에 대한 인과 진술이 아니다.</strong> 흡연의 피해는 수년간의 노출로 누적됩니다. 개비당 수치는 장기 효과를 회계적으로 나눈 편의값이며, 한 개비가 하는 일을 측정한 값이 아닙니다.</li>
<li><strong>조금 줄이는 것이 무의미하다는 근거가 아니다.</strong> 정직한 독법은 양쪽에 적용됩니다. 평균은 개인에게 특정 결과를 약속하지 않지만, 효과의 방향을 면제해 주지도 않습니다.</li>
<li><strong>남녀 값을 섞어 쓸 수 없다.</strong> 남성 추정치인지 여성 추정치인지 밝히지 않은 인용은 느슨한 인용입니다.</li>
</ul>

<div class="box"><p><strong>출처에 대한 메모.</strong> 17분·22분 추정치의 근거로 널리 인용되는 2024년 분석은
담배와 알코올 사용 등 공중보건 주제를 다루는 UCL 행동과학·보건 연구부 연구진이 발표한 것입니다. 다만 이 페이지
상단의 확인일 기준으로 그 분석의 원 보도자료 URL이 열리지 않았습니다(HTTP 404). 그래서 이 페이지는 그 보도자료를
인용하지 않습니다. 대신 해당 연구부 페이지와 현재 열리는 UCL 금연 연구 기사를 출처로 달고, 아래 해석은 WHO가
직접 공표한 수치에 근거합니다.</p></div>

<h2>WHO가 대신 공표하는 숫자</h2>
<p>금연이 무엇을 되돌려 주는지에 대한 권위 있는 숫자를 원한다면, WHO의 '금연의 건강상 이득' 질의응답 페이지가
분 대신 연(年) 단위로 제시합니다. 계속 피운 사람과 비교해, 30세 무렵 금연하면 기대수명 약 10년, 40세 무렵 9년,
50세 무렵 6년, 60세 무렵 3년을 얻습니다. WHO는 또 심근경색 후 금연한 사람의 재발 확률이 50% 낮아진다고
기록합니다.</p>

<p>이 네 숫자는 어떤 개비당 추정치보다 쓸모 있습니다. 이유는 두 가지입니다. 실제로 결정이 이뤄지는 단위로
표현돼 있고, 연령별로 정리돼 있습니다. 장기 흡연자가 진짜로 묻는 질문 — "지금은 너무 늦었나" — 에 대한
답이기 때문입니다.</p>

<h2>그런데도 화면에서는 '분'이 더 잘 작동하는 이유</h2>
<p>연(年)은 정책 문서에 맞는 단위이고, 화요일 오후에는 맞지 않는 단위입니다. "6년을 얻습니다"는 추상적이고,
"이 한 갑이 약 6시간입니다"는 손에 쥘 수 있는 크기입니다. 이 사이트가 분을 쓰는 이유는 그것뿐입니다. 같은
정보를 한 번의 결정에 맞는 축척으로 보여주는 것입니다. 계산기는 돈과 시간을 함께 보여주고, 한 번의 총액을
던지는 대신 계속 셉니다. 누적이 보여야 단위당 숫자가 실감되기 때문입니다.</p>

<h2>금연 성공률도 균일하지 않다</h2>
<p>평균은 금연하는 쪽의 편차도 가립니다. 2026년 11월 UCL 기사는 45~60세 중년 여성의 금연 성공률이 18.1%로
가장 낮았고, 더 젊은 여성은 22.3%, 더 나이 든 여성은 20.6%였으며, 사회경제적으로 더 취약한 중년 여성에서는
15.8%로 가장 낮았다고 보고합니다. 연구진은 중년 여성이 금연을 특히 어렵게 만드는 여러 압력에 동시에 놓이는
경우가 많고, 더 취약한 배경의 여성은 니코틴 의존도가 높을 가능성도 커서 금연이 더 어려울 수 있다고
설명합니다.</p>

<p>이 숫자의 실천적 독법은 비관이 아닙니다. 실패한 시도는 개인에 대한 판결이 아니라 흔한 결과라는 뜻이고,
그 비율을 움직이는 것은 지원이라는 뜻입니다. 무료 코칭, 금연 서비스, 한 가지가 아니라 두 가지 NRT 제품.
<a href="guide-nicotine-replacement.html" data-keep>제품 비교</a>와
<a href="quitlines.html" data-keep>무료 상담전화 목록</a>을 보십시오.</p>

<h2>점검표: 이 숫자를 정직하게 쓰는 법</h2>
<ul>
<li>인용할 때 남성 추정치인지 여성 추정치인지 밝힌다</li>
<li>개인의 카운트다운이 아니라 인구 평균으로 다룬다</li>
<li>"나는 늦었나"라는 질문에는 WHO의 연령별 기대수명 이득 수치를 쓴다</li>
<li>개비당 수치를 다른 추정치와 겹쳐 쌓아 극적인 총합을 만들지 않는다(입력이 중복된다)</li>
<li>우리 것을 포함해 모든 수치의 날짜를 확인한다 — <a href="guide-using-quitminutes.html" data-keep>이 계산기가 작동하는 방식</a></li>
</ul>
""",
 'faq_en': [
  ('Does one cigarette really take 20 minutes off my life?',
   'It is a population average, not a personal countdown. The estimate divides the average life expectancy gap between smokers and non-smokers by the cigarettes an average smoker consumes over a lifetime, and it is reported separately for men and women.'),
  ('How many years does quitting give back?',
   'WHO states that compared with people who kept smoking, quitting at about 30 gains almost 10 years of life expectancy, at about 40 gains 9 years, at about 50 gains 6 years, and at about 60 gains 3 years.'),
  ('Why does this site show two different per-cigarette figures?',
   'Because estimates of this kind are reported separately for men and women. Both the life expectancy gap and typical lifetime consumption differ, so a single blended number would hide which group it describes.')],
 'faq_ko': [
  ('담배 한 개비가 정말 수명 20분을 가져가나요?',
   '개인의 카운트다운이 아니라 인구 평균입니다. 흡연자와 비흡연자의 평균 기대수명 격차를, 평균 흡연자가 평생 피우는 담배 수로 나눈 추정치이며 남성과 여성을 나눠 보고합니다.'),
  ('금연하면 몇 년을 돌려받나요?',
   'WHO는 계속 피운 사람과 비교해 30세 무렵 금연 시 약 10년, 40세 9년, 50세 6년, 60세 3년의 기대수명 이득을 제시합니다.'),
  ('이 사이트는 왜 개비당 수치를 두 개 쓰나요?',
   '이런 추정치는 남녀를 나눠 보고하기 때문입니다. 기대수명 격차와 평생 흡연량이 모두 다르므로, 하나로 합친 숫자는 그 값이 어느 집단을 설명하는지 가려 버립니다.')],
},

# ─────────────────────────────── 5
{
 'slug': 'guide-korea-quit-support',
 'cat': 'help',
 'title_en': 'Free quit-smoking support in South Korea: what exists and how to start',
 'desc_en': 'The public quit-smoking services published by Korean health authorities - local health centre clinics, the outreach service, the national counselling channel - and where cost coverage is recorded.',
 'h1_en': 'Free quit-smoking support in South Korea',
 'h1_ko': '한국의 무료 금연지원 — 무엇이 있고 어떻게 시작하는가',
 'sub_en': 'Health centre clinics, the outreach service and the national counselling channel, as published by Korean health authorities.',
 'sub_ko': '보건소 금연클리닉, 찾아가는 금연지원서비스, 국가 금연상담 채널.',
 'srcs': ['kr_ncc', 'kr_guide', 'cdc_quit'],
 'rel': [('cost-of-smoking-south-korea.html', 'Smoking in South Korea: price, rules and free help', '대한민국 — 담뱃값·규제·금연지원'),
         ('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('guide-korea-cigarette-price-history.html', 'What is inside a Korean pack price', '한국 담뱃값에 들어 있는 것'),
         ('quitlines.html', 'Free quitlines by country', '나라별 무료 금연상담전화')],
 'body_en': """
<p>Korea runs quit-smoking support as a public service rather than a market, which means the first step is
usually administrative rather than medical: you contact a service, and the service tells you which programme
you qualify for. This page lists what the Korean health authorities publish on their own sites, and nothing
else.</p>

<h2>The services the national programme publishes</h2>
<p>금연두드림, the national quit-smoking support site, lists among its services a <strong>local health centre
quit-smoking clinic</strong> (보건소 금연클리닉), described as health centre counsellors supporting you from the
decision to quit through to success, and an <strong>outreach quit-smoking service</strong>
(찾아가는 금연지원서비스), described as going directly to smokers who find it hard to come to a programme. The
same site states that it currently operates menus and materials for infant smoking-harm prevention and school
smoking prevention projects.</p>

<p>금연길라잡이, the national quit-smoking information service, publishes a short check that recommends a
suitable support service, and a counselling route: a quitline KakaoTalk channel through which you can receive
one-to-one quit counselling.</p>

<div class="tw"><table><thead><tr><th>Route</th><th>What it is, as published</th><th>How to start</th></tr></thead><tbody>
<tr><td>Local health centre clinic</td><td>Health centre counsellors support you from decision to success</td><td>Contact the health centre for the district where you live or work</td></tr>
<tr><td>Outreach service</td><td>Goes directly to smokers who find it hard to attend a programme</td><td>Through the national programme site</td></tr>
<tr><td>National counselling channel</td><td>Quitline counselling, including a KakaoTalk channel for one-to-one counselling</td><td>The number is on our <a href="quitlines.html" data-keep>quitlines page</a></td></tr>
<tr><td>Service matching check</td><td>A short check that recommends a suitable support service</td><td>On the national information site</td></tr>
</tbody></table></div>

<h2>What a counselling line is actually for</h2>
<p>CDC's summary applies to any country's quitline: quitlines provide free coaching over the phone, and it is
never too late to quit. The reason to use one is not that the advice is secret. It is that a call can be timed
to a specific day and a specific trigger, which no web page can. If you are reading this in the middle of a
craving, the call is the shorter path.</p>

<h2>Cost, and where it is recorded</h2>
<p>Whether cessation medication is paid for by the state is a country-level fact, and WHO's country indicators
record both whether nicotine replacement is legally sold and whether its cost is covered. We publish the
recorded value for Korea on the <a href="cost-of-smoking-south-korea.html" data-keep>South Korea page</a>
rather than restating it here, because that page is regenerated from the indicator data and this one is not.
For how the products differ, see the <a href="guide-nicotine-replacement.html" data-keep>comparison
guide</a>.</p>

<div class="box"><p>Programme names, eligibility rules and medication supply change over time. Confirm current
terms with the health centre or the national programme before planning around them. This page records what the
official sites published on the confirmation date shown at the top.</p></div>

<h2>What to prepare before the first contact</h2>
<ul>
<li>How many cigarettes a day, and for how many years — services ask this first.</li>
<li>The two situations that broke your previous attempts, if there were previous attempts.</li>
<li>Current medicines and conditions, for the medication conversation.</li>
<li>Your district, because clinic access is organised through health centres.</li>
<li>Your actual daily spend, which the <a href="index.html" data-keep>calculator</a> turns into the number you will see every day.</li>
</ul>

<h2>Why the public route is usually the cheaper one</h2>
<p>A pack-a-day habit in Korea costs a predictable amount per year, and that figure sits on the
<a href="cost-of-smoking-south-korea.html" data-keep>country page</a> next to the recorded tax share. Against
that, the services above are provided as part of the national programme. The comparison is not subtle, and it
is the same comparison in every country with a funded programme — which is why the
<a href="prices.html" data-keep>price table</a> and the quitline list sit next to each other on this site.</p>

<h2>If you are helping someone else</h2>
<p>The outreach service exists precisely because attendance, not willingness, is the bottleneck. If the person
you are helping cannot or will not go to a clinic, the published route is the outreach programme rather than
more persuasion. The counselling channel is one-to-one, which matters for people who will not sit in a group.
Nothing on this page requires a diagnosis or a referral to begin.</p>
""",
 'body_ko': """
<p>한국은 금연지원을 시장이 아니라 공공 서비스로 운영합니다. 그래서 첫걸음이 의학적이기보다 행정적입니다.
서비스에 연락하면, 어느 프로그램에 해당하는지를 알려줍니다. 이 페이지는 한국 보건당국이 자신들의 사이트에
공표한 내용만 정리합니다.</p>

<h2>국가 프로그램이 공표한 서비스</h2>
<p>국가 금연지원 사이트 금연두드림은 서비스로 <strong>보건소 금연클리닉</strong>을 "금연 결심부터 성공까지
보건소 금연상담사가 도와드립니다"로, <strong>찾아가는 금연지원서비스</strong>를 "금연프로그램에 찾아오기 어려운
흡연자에게 직접 찾아갑니다"로 안내합니다. 같은 사이트는 현재 유아 흡연위해예방사업과 학교 흡연예방 관련
메뉴·자료실을 운영 중이라고 표시하고 있습니다.</p>

<p>국가 금연정보 서비스 금연길라잡이는 간단한 검사로 알맞은 금연지원 서비스를 추천받는 기능과, 상담 경로를
제공합니다. 금연상담전화 카카오 채널을 통해 1:1 금연상담을 받을 수 있다고 안내합니다.</p>

<div class="tw"><table><thead><tr><th>경로</th><th>공표된 내용</th><th>시작 방법</th></tr></thead><tbody>
<tr><td>보건소 금연클리닉</td><td>금연 결심부터 성공까지 보건소 금연상담사가 지원</td><td>거주지 또는 직장 소재지 보건소에 문의</td></tr>
<tr><td>찾아가는 금연지원서비스</td><td>프로그램에 찾아오기 어려운 흡연자에게 직접 방문</td><td>국가 금연지원 사이트 경유</td></tr>
<tr><td>국가 금연상담 채널</td><td>전화 상담. 카카오 채널로 1:1 상담 가능</td><td>번호는 <a href="quitlines.html" data-keep>금연상담전화 페이지</a>에 있음</td></tr>
<tr><td>서비스 추천 검사</td><td>알맞은 금연지원 서비스를 추천하는 짧은 검사</td><td>국가 금연정보 사이트에서</td></tr>
</tbody></table></div>

<h2>상담전화는 무엇에 쓰는 것인가</h2>
<p>CDC의 요약은 어느 나라의 금연상담전화에도 적용됩니다 — 금연상담전화는 전화로 무료 코칭을 제공하며, 금연에
늦은 때는 없다는 것입니다. 전화를 쓰는 이유는 거기에만 있는 비밀 조언 때문이 아닙니다. 특정한 날, 특정한
방아쇠에 맞출 수 있다는 점 때문입니다. 웹페이지는 그걸 할 수 없습니다. 지금 흡연 욕구 중에 이 글을 읽고
있다면, 전화가 더 짧은 길입니다.</p>

<h2>비용은 어디에 기록돼 있는가</h2>
<p>금연 치료제 비용을 국가가 부담하는지는 국가 단위 사실이고, WHO의 국가별 지표에는 니코틴 대체요법이 합법적으로
판매되는지와 그 비용이 보장되는지가 기록돼 있습니다. 한국의 기록값은 여기서 다시 쓰지 않고
<a href="cost-of-smoking-south-korea.html" data-keep>대한민국 페이지</a>에 그대로 싣습니다. 그 페이지는 지표
데이터에서 다시 생성되고 이 페이지는 그렇지 않기 때문입니다. 제품별 차이는
<a href="guide-nicotine-replacement.html" data-keep>비교 가이드</a>에 있습니다.</p>

<div class="box"><p>프로그램 이름, 지원 대상 기준, 약제 공급 조건은 바뀝니다. 계획을 세우기 전에 보건소나 국가
프로그램에 현재 조건을 확인하십시오. 이 페이지는 상단 확인일 기준으로 공식 사이트에 공표된 내용을
기록합니다.</p></div>

<h2>첫 연락 전에 준비할 것</h2>
<ul>
<li>하루 몇 개비, 몇 년 — 서비스가 가장 먼저 묻습니다</li>
<li>지난 시도를 무너뜨린 두 가지 상황(시도 경험이 있다면)</li>
<li>복용 중인 약과 기저질환 — 약제 상담을 위해</li>
<li>거주 구·시 — 클리닉 이용이 보건소 단위로 조직돼 있습니다</li>
<li>하루 실제 지출액 — <a href="index.html" data-keep>계산기</a>가 매일 보게 될 숫자로 바꿔 줍니다</li>
</ul>

<h2>공공 경로가 보통 더 저렴한 이유</h2>
<p>한국에서 하루 한 갑 습관의 연간 비용은 예측 가능한 금액이고, 그 수치는
<a href="cost-of-smoking-south-korea.html" data-keep>국가 페이지</a>에 기록된 세금 비중과 함께 있습니다. 그
금액과 비교하면, 위에 적은 서비스는 국가 프로그램의 일부로 제공됩니다. 비교가 미묘하지 않습니다. 재정이
투입된 프로그램이 있는 모든 나라에서 같은 비교이고, 그래서 이 사이트는
<a href="prices.html" data-keep>담뱃값 표</a>와 상담전화 목록을 나란히 둡니다.</p>

<h2>다른 사람을 돕는 경우</h2>
<p>찾아가는 서비스가 존재하는 이유는 병목이 의지가 아니라 '방문'이기 때문입니다. 돕고 있는 사람이 클리닉에 갈
수 없거나 가지 않으려 한다면, 공표된 경로는 더 많은 설득이 아니라 방문형 프로그램입니다. 상담 채널은
1:1입니다. 집단 프로그램에 앉지 않을 사람에게는 이 점이 중요합니다. 이 페이지의 어떤 경로도 시작하기 위해
진단서나 의뢰서를 요구하지 않습니다.</p>
""",
 'faq_en': [
  ('What free quit-smoking services does Korea publish?',
   'The national programme site lists a local health centre quit-smoking clinic, described as counsellors supporting you from the decision to quit through to success, and an outreach service that goes directly to smokers who find it hard to attend a programme.'),
  ('How do I get counselling without visiting anywhere?',
   'The national quit-smoking information service publishes a quitline KakaoTalk channel for one-to-one counselling, plus a short check that recommends which support service suits you. The quitline number is listed on our quitlines page.'),
  ('Is quit medication free in Korea?',
   'Cost coverage is a country-level fact recorded in WHO indicator data, and we publish the recorded value for Korea on the South Korea country page rather than restating it here. Confirm current supply terms with the health centre.')],
 'faq_ko': [
  ('한국이 공표한 무료 금연지원 서비스는 무엇인가요?',
   '국가 금연지원 사이트는 "금연 결심부터 성공까지 보건소 금연상담사가 도와드립니다"로 안내되는 보건소 금연클리닉과, 프로그램에 찾아오기 어려운 흡연자에게 직접 찾아가는 찾아가는 금연지원서비스를 제시합니다.'),
  ('방문 없이 상담받을 방법이 있나요?',
   '국가 금연정보 서비스는 1:1 금연상담을 위한 금연상담전화 카카오 채널과, 알맞은 지원 서비스를 추천하는 짧은 검사를 공표하고 있습니다. 상담전화 번호는 이 사이트 금연상담전화 페이지에 있습니다.'),
  ('한국에서 금연 치료제는 무료인가요?',
   '비용 보장 여부는 WHO 지표 데이터에 기록된 국가 단위 사실이며, 한국의 기록값은 대한민국 국가 페이지에 그대로 싣습니다. 현재 공급 조건은 보건소에 확인하십시오.')],
},

# ─────────────────────────────── 6
{
 'slug': 'guide-withdrawal-symptoms',
 'cat': 'body',
 'title_en': 'Withdrawal symptoms when you stop smoking: what they are, how long they last, what to do',
 'desc_en': 'The short-term withdrawal effects listed by MedlinePlus, how they map onto the first weeks, the five-minute rule for cravings, and when to involve a clinician.',
 'h1_en': 'Withdrawal symptoms, stage by stage',
 'h1_ko': '금단증상 단계별 대처 — 증상·기간·대처',
 'sub_en': 'What is a symptom, what is a trigger, and which part gets better on its own.',
 'sub_ko': '무엇이 증상이고 무엇이 방아쇠인지, 어느 부분이 저절로 나아지는지.',
 'srcs': ['medlineplus', 'nhs_cravings', 'who_cessation_qa'],
 'rel': [('guide-first-72-hours.html', 'The first 72 hours', '금연 첫 72시간'),
         ('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('guide-alcohol-cravings.html', 'Drinking, dinners and cravings', '술자리에서 담배 안 피우는 법'),
         ('guide-weight-gain.html', 'Weight after quitting', '금연 후 체중')],
 'body_en': """
<p>Two different things happen when you stop smoking and they are easy to confuse. One is recovery, which runs
on a schedule nobody feels. The other is withdrawal, which is what you do feel and which ends. Most relapse
decisions get made while mistaking the second for the first.</p>

<h2>The symptoms, as listed by a public health service</h2>
<p>MedlinePlus, the consumer health service of the US National Library of Medicine, states that when you stop
or cut back on smoking you may have short-term effects such as irritability, anxiety, moodiness, weight gain or
trouble sleeping, and that these are called withdrawal symptoms.</p>

<div class="tw"><table><thead><tr><th>Symptom</th><th>What it looks like day to day</th><th>What usually helps</th></tr></thead><tbody>
<tr><td>Irritability</td><td>Short fuse over small things, usually worst in the first days</td><td>Tell the people around you in advance; it is information, not an apology</td></tr>
<tr><td>Anxiety</td><td>Restlessness, difficulty settling</td><td>Movement, and a steady nicotine baseline if you are using a patch</td></tr>
<tr><td>Moodiness</td><td>Flat or volatile mood that does not match events</td><td>Judge yourself on behaviour rather than mood for the first weeks</td></tr>
<tr><td>Trouble sleeping</td><td>Waking in the night, lighter sleep</td><td>Treat sleep as part of the plan; do not stack a new sleep deficit on top</td></tr>
<tr><td>Weight gain</td><td>Increased appetite, more snacking</td><td>See <a href="guide-weight-gain.html" data-keep>the weight guide</a>; the order of priorities matters</td></tr>
<tr><td>Cravings</td><td>Short waves tied to places and routines</td><td>The five-minute rule below, plus a fast-acting product</td></tr>
</tbody></table></div>

<h2>Symptom or trigger</h2>
<p>A symptom comes from your body adjusting. A trigger comes from your calendar. The difference decides what
works. Symptoms fade with time and are helped by a steady baseline, which is why NHS guidance pairs a patch
with a fast-acting product. Triggers do not fade on their own; they are specific situations, and they are
beaten by a plan for that situation — the evening after dinner, the car, the balcony, the first drink. NHS
material on staying smoke free is explicit that the job is handling cravings, managing withdrawal symptoms, and
getting back on track if you slip up. Three different jobs, not one.</p>

<h2>The five-minute rule</h2>
<ul>
<li>Set a timer for five minutes instead of deciding whether to smoke.</li>
<li>Leave the place you are in. Most cravings are attached to a location.</li>
<li>Drink water, or use your fast-acting product as instructed.</li>
<li>When the timer ends, reassess. The decision has usually made itself.</li>
<li>If it has not, use the free counselling line rather than negotiating alone.</li>
</ul>

<p>The point of the rule is not stoicism. It is that a craving is an event with a duration, and that almost
nobody is still inside the same craving five minutes later. The rule converts an open-ended question into a
short wait.</p>

<h2>What is happening underneath, on WHO's schedule</h2>
<p>While withdrawal is at its loudest, measurable recovery is quiet. WHO records that heart rate and blood
pressure drop within 20 minutes, blood carbon monoxide falls to normal by 12 hours, circulation improves and
lung function increases across 2 to 12 weeks, and coughing and shortness of breath decrease over 1 to 9 months.
None of those are felt as events. Knowing the schedule exists is the counterweight to the symptom list: the
discomfort is front-loaded and the benefit is back-loaded.</p>

<h2>When to involve a clinician</h2>
<div class="box warn"><p>Ask for medical help rather than waiting if symptoms are severe or persistent, if
sleep loss is affecting your safety at work or while driving, if a mental health condition is destabilising, or
if you take medicines whose effects may change when you stop smoking. A pharmacist, your doctor or your
national quitline can advise. This page is information, not a diagnosis.</p></div>

<h2>The relapse point most people miss</h2>
<p>The highest-risk moment is not day two. It is the week when symptoms have faded enough that the products
feel unnecessary while the situational triggers are still fully intact — a first drink, a stressful week, a
holiday. That is the week to keep the patch on and the plan written down. See
<a href="guide-alcohol-cravings.html" data-keep>drinking, dinners and cravings</a> for the situation that
breaks the most attempts, and <a href="guide-first-72-hours.html" data-keep>the first 72 hours</a> for the
opening stretch.</p>
""",
 'body_ko': """
<p>담배를 끊으면 두 가지 다른 일이 동시에 일어나고, 둘은 혼동되기 쉽습니다. 하나는 회복이고, 아무도 느끼지
못하는 일정표로 진행됩니다. 다른 하나는 금단이고, 느껴지며 끝이 있습니다. 대부분의 재흡연 결정은 두 번째를
첫 번째로 착각한 상태에서 내려집니다.</p>

<h2>공공 보건서비스가 적어 놓은 증상 목록</h2>
<p>미국 국립의학도서관의 소비자 건강정보 서비스 MedlinePlus는, 담배를 끊거나 줄이면 짜증·불안·기분 변화·체중
증가·수면 장애 같은 단기적 영향이 나타날 수 있고 이를 금단증상이라고 부른다고 기술합니다.</p>

<div class="tw"><table><thead><tr><th>증상</th><th>일상에서 어떻게 보이는가</th><th>보통 도움이 되는 것</th></tr></thead><tbody>
<tr><td>짜증</td><td>작은 일에 폭발. 보통 초반 며칠이 가장 심함</td><td>주변에 미리 알린다. 사과가 아니라 정보 전달이다</td></tr>
<tr><td>불안</td><td>안절부절, 가라앉지 않음</td><td>움직이기. 패치를 쓰는 경우 니코틴 기본선 유지</td></tr>
<tr><td>기분 변화</td><td>사건과 맞지 않는 무기력 또는 기복</td><td>초기 몇 주는 기분이 아니라 행동으로 자신을 평가</td></tr>
<tr><td>수면 장애</td><td>밤에 깸, 얕은 잠</td><td>잠을 계획의 일부로 다루고, 새 수면 부족을 겹치지 않게</td></tr>
<tr><td>체중 증가</td><td>식욕 증가, 간식 늘어남</td><td><a href="guide-weight-gain.html" data-keep>체중 가이드</a> 참조. 우선순위의 순서가 중요</td></tr>
<tr><td>흡연 욕구</td><td>장소·습관에 묶인 짧은 파도</td><td>아래 5분 규칙 + 속효성 제품</td></tr>
</tbody></table></div>

<h2>증상인가, 방아쇠인가</h2>
<p>증상은 몸이 적응하면서 생깁니다. 방아쇠는 일정표에서 옵니다. 이 구분이 무엇이 통할지를 결정합니다. 증상은
시간이 지나면 약해지고 일정한 기본선이 도움이 됩니다. NHS가 패치와 속효성 제형을 짝지으라고 안내하는 이유입니다.
방아쇠는 저절로 약해지지 않습니다. 특정 상황이고, 그 상황에 대한 계획으로만 꺾입니다. 식후 저녁, 차 안, 베란다,
첫 잔. NHS의 금연 유지 자료는 할 일이 세 가지라고 분명히 적습니다 — 흡연 욕구를 다루는 일, 금단증상을 관리하는
일, 한 번 피웠을 때 다시 궤도로 돌아오는 일.</p>

<h2>5분 규칙</h2>
<ul>
<li>피울지 말지를 결정하는 대신 5분 타이머를 켠다</li>
<li>지금 있는 장소를 떠난다. 욕구는 대부분 위치에 붙어 있다</li>
<li>물을 마시거나 속효성 제품을 설명서대로 쓴다</li>
<li>타이머가 끝나면 다시 판단한다. 보통 결정은 이미 내려져 있다</li>
<li>그래도 남아 있으면 혼자 협상하지 말고 무료 상담전화를 쓴다</li>
</ul>

<p>이 규칙의 요점은 인내심이 아닙니다. 흡연 욕구는 지속 시간이 있는 사건이고, 5분 뒤에도 같은 욕구 안에 있는
사람은 거의 없다는 사실입니다. 규칙은 끝이 없는 질문을 짧은 기다림으로 바꿉니다.</p>

<h2>그 아래에서 진행되는 것 — WHO의 일정표</h2>
<p>금단이 가장 시끄러울 때, 측정 가능한 회복은 조용합니다. WHO는 20분 안에 심박수와 혈압이 내려가고, 12시간이면
혈중 일산화탄소가 정상 수준으로 떨어지며, 2~12주에 걸쳐 혈액순환이 좋아지고 폐 기능이 향상되고, 1~9개월에 기침과
숨가쁨이 줄어든다고 기록합니다. 어느 것도 사건으로 느껴지지 않습니다. 그 일정표가 있다는 사실을 아는 것이 증상
목록에 대한 균형추입니다. 불편은 앞에 몰려 있고 이득은 뒤에 있습니다.</p>

<h2>의료진이 필요한 때</h2>
<div class="box warn"><p>증상이 심하거나 오래 지속될 때, 수면 부족이 업무·운전 안전에 영향을 줄 때, 정신건강
질환이 불안정해질 때, 금연으로 효과가 달라질 수 있는 약을 복용 중일 때는 기다리지 말고 도움을 요청하십시오.
약사·의사 또는 국가 금연상담전화가 안내할 수 있습니다. 이 페이지는 정보이며 진단이 아닙니다.</p></div>

<h2>대부분이 놓치는 재흡연 지점</h2>
<p>가장 위험한 순간은 둘째 날이 아닙니다. 증상이 충분히 가라앉아 제품이 불필요해 보이는데 상황 방아쇠는 그대로
남아 있는 주입니다. 첫 술자리, 스트레스가 몰린 주, 연휴. 그 주에 패치를 유지하고 계획을 적어 두어야 합니다.
가장 많은 시도를 깨뜨리는 상황은 <a href="guide-alcohol-cravings.html" data-keep>술자리에서 담배 안 피우는
법</a>에, 초반 구간은 <a href="guide-first-72-hours.html" data-keep>금연 첫 72시간</a>에 있습니다.</p>
""",
 'faq_en': [
  ('What are the withdrawal symptoms of quitting smoking?',
   'MedlinePlus lists short-term effects such as irritability, anxiety, moodiness, weight gain and trouble sleeping, and calls them withdrawal symptoms. They are described as short-term effects rather than lasting harm.'),
  ('How long does a craving last?',
   'Cravings arrive as short waves rather than a continuous state, which is why the five-minute rule works: set a timer, leave the place that triggered it, and reassess when the timer ends instead of deciding during the craving.'),
  ('Is there a point where relapse risk rises again?',
   'The common pattern is the week when symptoms have faded enough that nicotine products feel unnecessary while situational triggers are still intact - a first drink, a stressful week, a holiday. NHS material treats handling cravings, managing symptoms and recovering from a slip as three separate tasks.')],
 'faq_ko': [
  ('금연 금단증상에는 어떤 것이 있나요?',
   'MedlinePlus는 짜증·불안·기분 변화·체중 증가·수면 장애 같은 단기적 영향을 열거하고 이를 금단증상이라고 부릅니다. 지속적 손상이 아니라 단기 영향으로 기술돼 있습니다.'),
  ('흡연 욕구는 얼마나 지속되나요?',
   '욕구는 계속되는 상태가 아니라 짧은 파도로 옵니다. 그래서 5분 규칙이 통합니다. 타이머를 켜고, 방아쇠가 된 장소를 떠나고, 욕구 중에 결정하지 말고 타이머가 끝난 뒤 다시 판단하십시오.'),
  ('재흡연 위험이 다시 올라가는 시점이 있나요?',
   '흔한 양상은 증상이 가라앉아 니코틴 제품이 불필요해 보이는데 상황 방아쇠는 그대로인 주입니다. 첫 술자리, 스트레스가 몰린 주, 연휴. NHS 자료는 욕구 대응·증상 관리·실수 후 복귀를 서로 다른 세 가지 일로 다룹니다.')],
},
]
