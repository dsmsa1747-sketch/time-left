# -*- coding: utf-8 -*-
"""가이드 7~9. 확인된 출처(work/guide_probe.json)에서만 인용한다.
확인 못 한 평균치(체중 증가 폭 등)는 쓰지 않고, 쓰지 않았다는 사실을 페이지에 적는다."""

GUIDES = [

# ─────────────────────────────── 7
{
 'slug': 'guide-weight-gain',
 'cat': 'body',
 'title_en': 'Weight after quitting smoking: what is listed, what is not, and the order of priorities',
 'desc_en': 'Weight gain is listed by MedlinePlus as a short-term withdrawal effect. What that means in practice, why we do not publish an average figure, and what CDC says about the health trade-off.',
 'h1_en': 'Weight after quitting, and the order of priorities',
 'h1_ko': '금연 후 체중 — 무엇이 기록돼 있고 무엇이 아닌가',
 'sub_en': 'A listed withdrawal effect, not a reason to keep smoking. What is sourced and what is not.',
 'sub_ko': '기록된 금단 영향이지만 계속 피울 이유는 아닙니다. 출처가 있는 것과 없는 것.',
 'srcs': ['medlineplus', 'cdc_benefits', 'nhs_quit'],
 'rel': [('guide-withdrawal-symptoms.html', 'Withdrawal symptoms, stage by stage', '금단증상 단계별 대처'),
         ('guide-first-72-hours.html', 'The first 72 hours', '금연 첫 72시간'),
         ('guide-alcohol-cravings.html', 'Drinking, dinners and cravings', '술자리에서 담배 안 피우는 법'),
         ('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교')],
 'body_en': """
<p>Weight is the most common reason people give for delaying a quit attempt, and it is also the easiest topic
to fill with invented numbers. This page keeps to what a public health service actually publishes, says plainly
what we could not source, and then deals with the practical question.</p>

<h2>What is actually published</h2>
<p>MedlinePlus, the consumer health service of the US National Library of Medicine, states that when you stop
or cut back on smoking you may have short-term effects such as irritability, anxiety, moodiness,
<strong>weight gain</strong> or trouble sleeping, and that these are called withdrawal symptoms. That is the
sourced claim: weight gain appears on the official list of short-term withdrawal effects, in the same list as
sleep disruption and irritability.</p>

<div class="box"><p><strong>What we are not publishing.</strong> We do not state an average number of
kilograms, because on the confirmation date shown at the top of this page we could not retrieve a figure from a
verifiable public health source. A number you cannot source is worse than no number, so the row stays empty
until it can be filled. Everything below treats weight as a listed effect of unknown individual
magnitude.</p></div>

<h2>Why it happens at all, in the terms the list uses</h2>
<p>Three of the items on the withdrawal list interact. Appetite changes and more frequent snacking are reported
alongside irritability and disrupted sleep, and those two make food decisions worse in a way that has nothing
to do with metabolism. In other words, part of the problem in the first weeks is a tired, irritable person
making choices at 11pm, and that part is addressable without any dietary theory.</p>

<div class="tw"><table><thead><tr><th>What changes</th><th>Why it matters for weight</th><th>Practical response</th></tr></thead><tbody>
<tr><td>Appetite and snacking</td><td>The most direct route; hand-to-mouth routine looks for a replacement</td><td>Decide the replacement in advance rather than at the moment of the craving</td></tr>
<tr><td>Disrupted sleep</td><td>Tired decisions are worse decisions, late in the day</td><td>Treat sleep as part of the quit plan, not a separate project</td></tr>
<tr><td>Irritability</td><td>Food used as the fastest available relief</td><td>Use the fast-acting nicotine product as instructed instead</td></tr>
<tr><td>Routine gaps</td><td>The smoke break was also a walk and a break</td><td>Keep the break, remove the cigarette: step outside, walk the same route</td></tr>
</tbody></table></div>

<h2>The order of priorities, stated by CDC</h2>
<p>CDC's summary of the evidence is blunt about what quitting does: it reduces the risk of premature death and
can add as much as ten years to life expectancy; it reduces the risk for many adverse health effects including
cardiovascular disease, chronic obstructive pulmonary disease, cancer and poor reproductive health outcomes;
and even people who have smoked for many years or have smoked heavily will benefit from quitting. CDC also
records that the risk of coronary heart disease falls sharply one to two years after cessation.</p>

<p>That is the trade-off in its honest form. A listed short-term withdrawal effect of unspecified size on one
side, and that list of risk reductions on the other. The sequencing that follows is the standard one: stop
smoking first, address weight afterwards, and do not run two difficult projects in the same month.</p>

<h2>A practical plan for the first weeks</h2>
<ul>
<li>Pick the replacement for the hand-to-mouth routine before you need it, and keep it within reach.</li>
<li>Keep the break, drop the cigarette. The smoke break was partly a walk; walking still works.</li>
<li>Use the fast-acting nicotine product when the craving arrives rather than eating through it.</li>
<li>Protect sleep for the first two weeks; the withdrawal list includes sleep for a reason.</li>
<li>Weigh yourself no more than once a week if at all, so one day's number does not become a reason to smoke.</li>
<li>Do not start a restrictive diet in the same week as a quit attempt.</li>
</ul>

<h2>What to do if the weight becomes the problem</h2>
<div class="box warn"><p>If weight change is significant, rapid or distressing, or if you have a condition
where weight matters clinically — diabetes, heart disease, an eating disorder history, pregnancy — this is a
question for a clinician rather than a web page. NHS frames quitting as something that works better with the
right support at every stage, including staying smoke free; your doctor, a pharmacist or a stop-smoking service
can handle both issues at once.</p></div>

<h2>The sentence worth keeping</h2>
<p>NHS states plainly that it is never too late to quit and that it is easier to stop smoking with the right
support. Weight is a reason to get support, not a reason to postpone. If the plan is "I will quit after I lose
weight", the honest version of that plan is usually "I will keep smoking", and the cost of that version is
visible in the <a href="index.html" data-keep>calculator</a> and on the
<a href="prices.html" data-keep>price table</a>.</p>

<p>For the symptoms that accompany the weight question, see
<a href="guide-withdrawal-symptoms.html" data-keep>withdrawal symptoms stage by stage</a>, and for the opening
few days see <a href="guide-first-72-hours.html" data-keep>the first 72 hours</a>.</p>
""",
 'body_ko': """
<p>체중은 금연을 미루는 이유로 가장 자주 언급되는 주제이고, 동시에 근거 없는 숫자로 채우기 가장 쉬운
주제입니다. 이 페이지는 공공 보건서비스가 실제로 공표한 내용만 쓰고, 출처를 찾지 못한 부분은 그렇다고 밝힌 뒤
실무적인 질문을 다룹니다.</p>

<h2>실제로 공표된 것</h2>
<p>미국 국립의학도서관의 소비자 건강정보 서비스 MedlinePlus는, 담배를 끊거나 줄이면 짜증·불안·기분 변화·
<strong>체중 증가</strong>·수면 장애 같은 단기적 영향이 나타날 수 있고 이를 금단증상이라고 부른다고 기술합니다.
출처가 있는 주장은 이것입니다. 체중 증가는 공식적인 단기 금단 영향 목록에, 수면 장애와 짜증과 나란히 올라
있습니다.</p>

<div class="box"><p><strong>싣지 않는 것.</strong> 평균 몇 킬로그램이라는 수치는 쓰지 않았습니다. 이 페이지
상단의 확인일 기준으로 검증 가능한 공공 보건 출처에서 그 수치를 받지 못했기 때문입니다. 출처를 댈 수 없는
숫자는 숫자가 없는 것보다 나쁩니다. 채울 수 있을 때까지 그 칸은 비워 둡니다. 아래 내용은 체중을 '개인별 크기를
알 수 없는, 목록에 있는 영향'으로 다룹니다.</p></div>

<h2>왜 생기는가 — 목록의 용어 안에서</h2>
<p>금단 목록의 항목 세 개가 서로 맞물립니다. 식욕 변화와 간식 증가는 짜증과 수면 장애와 함께 보고되고, 뒤의 두
가지는 대사와 무관한 방식으로 음식 선택을 나쁘게 만듭니다. 즉 초기 몇 주의 문제 일부는 '피곤하고 짜증 난 사람이
밤 11시에 하는 선택'이고, 그 부분은 어떤 식이 이론 없이도 다룰 수 있습니다.</p>

<div class="tw"><table><thead><tr><th>무엇이 바뀌는가</th><th>체중과 어떻게 연결되는가</th><th>실무적 대응</th></tr></thead><tbody>
<tr><td>식욕과 간식</td><td>가장 직접적인 경로. 손에서 입으로 가는 습관이 대체물을 찾는다</td><td>욕구가 온 순간이 아니라 미리 대체물을 정해 둔다</td></tr>
<tr><td>수면 장애</td><td>피곤한 결정은 나쁜 결정이고, 주로 늦은 시간에 내려진다</td><td>잠을 별개 과제가 아니라 금연 계획의 일부로 다룬다</td></tr>
<tr><td>짜증</td><td>가장 빠른 위안으로 음식을 쓰게 된다</td><td>대신 속효성 니코틴 제품을 설명서대로 쓴다</td></tr>
<tr><td>사라진 루틴</td><td>흡연 시간은 걷기이자 휴식이기도 했다</td><td>휴식은 남기고 담배만 뺀다. 밖에 나가 같은 경로를 걷는다</td></tr>
</tbody></table></div>

<h2>우선순위 — CDC가 기술한 대로</h2>
<p>CDC는 금연이 하는 일을 분명하게 요약합니다. 조기 사망 위험을 낮추고 기대수명을 최대 10년까지 늘릴 수 있으며,
심혈관질환·만성폐쇄성폐질환(COPD)·암·생식 건강 악화를 포함한 여러 유해 영향의 위험을 낮추고, 오래 피웠거나 많이
피운 사람도 금연으로 이득을 얻는다는 것입니다. CDC는 또 관상동맥 심장질환 위험이 금연 후 1~2년에 급격히
떨어진다고 기록합니다.</p>

<p>정직한 형태의 거래는 이렇습니다. 한쪽에는 크기가 특정되지 않은 단기 금단 영향 하나, 다른 쪽에는 위에 적은
위험 감소 목록. 여기서 따라오는 순서는 표준적인 그것입니다. 먼저 담배를 끊고, 체중은 그 다음에 다루고, 어려운
과제 두 개를 같은 달에 돌리지 않는 것입니다.</p>

<h2>초기 몇 주의 실무 계획</h2>
<ul>
<li>손에서 입으로 가는 습관의 대체물을 필요해지기 전에 정하고, 손 닿는 곳에 둔다</li>
<li>휴식은 남기고 담배는 뺀다. 흡연 시간의 절반은 걷기였고, 걷기는 여전히 작동한다</li>
<li>욕구가 올 때 먹는 것으로 버티지 말고 속효성 니코틴 제품을 쓴다</li>
<li>첫 2주는 잠을 지킨다. 금단 목록에 수면이 들어 있는 이유가 있다</li>
<li>체중은 재더라도 주 1회 이하로. 하루치 숫자가 담배를 피울 이유가 되지 않게</li>
<li>금연 시도와 같은 주에 제한적인 다이어트를 시작하지 않는다</li>
</ul>

<h2>체중이 실제 문제가 되면</h2>
<div class="box warn"><p>체중 변화가 크거나 빠르거나 괴로울 때, 또는 당뇨·심장질환·섭식장애 이력·임신처럼
체중이 임상적으로 중요한 상태라면 이것은 웹페이지가 아니라 의료진의 질문입니다. NHS는 금연을 모든 단계에서
적절한 지원이 있을 때 더 쉬워지는 일로 설명하며, 여기에는 금연 유지 단계도 포함됩니다. 의사·약사 또는 금연
서비스는 두 문제를 한 번에 다룰 수 있습니다.</p></div>

<h2>남겨 둘 문장</h2>
<p>NHS는 금연에 늦은 때가 없으며, 적절한 지원이 있으면 금연이 더 쉬워진다고 분명하게 씁니다. 체중은 지원을
받을 이유이지 미룰 이유가 아닙니다. 계획이 "살을 빼고 나서 끊겠다"라면, 그 계획의 정직한 번역은 보통 "계속
피우겠다"이고, 그 번역의 비용은 <a href="index.html" data-keep>계산기</a>와
<a href="prices.html" data-keep>담뱃값 표</a>에 그대로 보입니다.</p>

<p>체중 문제와 함께 오는 증상은 <a href="guide-withdrawal-symptoms.html" data-keep>금단증상 단계별 대처</a>에,
초반 며칠은 <a href="guide-first-72-hours.html" data-keep>금연 첫 72시간</a>에 있습니다.</p>
""",
 'faq_en': [
  ('Is weight gain after quitting a real effect?',
   'MedlinePlus lists weight gain among the short-term effects that may occur when you stop or cut back on smoking, alongside irritability, anxiety, moodiness and trouble sleeping, and calls them withdrawal symptoms.'),
  ('How much weight will I gain?',
   'This page does not publish an average figure, because no figure could be retrieved from a verifiable public health source on the confirmation date shown at the top. Individual change varies and is a question for a clinician if it matters medically for you.'),
  ('Should I diet and quit at the same time?',
   'The standard sequencing is to stop smoking first and address weight afterwards, rather than running two difficult projects in the same month. CDC records that quitting reduces the risk of premature death and can add as much as ten years to life expectancy.')],
 'faq_ko': [
  ('금연 후 체중 증가는 실제로 있는 일인가요?',
   'MedlinePlus는 담배를 끊거나 줄일 때 나타날 수 있는 단기적 영향으로 짜증·불안·기분 변화·수면 장애와 함께 체중 증가를 열거하고, 이를 금단증상이라고 부릅니다.'),
  ('몇 킬로그램 늘어나나요?',
   '이 페이지는 평균 수치를 싣지 않습니다. 상단의 확인일 기준으로 검증 가능한 공공 보건 출처에서 그 수치를 받지 못했기 때문입니다. 개인별 변화는 다르며, 의학적으로 중요한 상황이라면 의료진의 질문입니다.'),
  ('다이어트와 금연을 같이 해도 되나요?',
   '표준적인 순서는 먼저 금연하고 체중은 그 다음에 다루는 것입니다. 어려운 과제 두 개를 같은 달에 돌리지 않는 쪽입니다. CDC는 금연이 조기 사망 위험을 낮추고 기대수명을 최대 10년까지 늘릴 수 있다고 기록합니다.')],
},

# ─────────────────────────────── 8
{
 'slug': 'guide-alcohol-cravings',
 'cat': 'body',
 'title_en': 'Drinking, dinners and cravings: getting through the situation that breaks most quit attempts',
 'desc_en': 'A written plan for drinks, work dinners and gatherings: the five-minute rule, refusal sentences, a three-week plan, and what NHS says about handling cravings.',
 'h1_en': 'Drinking, dinners and cravings',
 'h1_ko': '술자리·회식에서 담배 안 피우는 법',
 'sub_en': 'The situation that breaks most attempts, and a plan written before you are in it.',
 'sub_ko': '가장 많은 시도를 깨뜨리는 상황, 그리고 그 안에 들어가기 전에 쓰는 계획.',
 'srcs': ['nhs_cravings', 'nhs_quit', 'medlineplus'],
 'rel': [('guide-withdrawal-symptoms.html', 'Withdrawal symptoms, stage by stage', '금단증상 단계별 대처'),
         ('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('guide-first-72-hours.html', 'The first 72 hours', '금연 첫 72시간'),
         ('quitlines.html', 'Free quitlines by country', '나라별 무료 금연상담전화')],
 'body_en': """
<p>Most quit attempts do not end at home. They end in a specific chair, at a specific hour, usually with a
drink in hand and somebody else smoking outside. This page is about that situation, and the useful thing about
it is that it is predictable — which means it can be planned for in advance rather than negotiated at the
table.</p>

<h2>Why this situation is different from withdrawal</h2>
<p>Withdrawal is a symptom that fades. A drinks table is a trigger, and triggers do not fade on their own. NHS
material on staying smoke free separates the tasks: handling cravings, managing withdrawal symptoms, and
getting back on track if you slip up. The drinks table belongs to the first and third of those, which is why
willpower spent on the second does not help here.</p>

<p>There is also a mechanical reason the situation is hard. The cues are stacked: a place, a time of day, other
people smoking, a routine that has been repeated hundreds of times, and reduced caution. None of those is
nicotine, which is why people who are comfortable on day ten still lose an attempt in week three.</p>

<h2>A plan, written before you go</h2>
<div class="tw"><table><thead><tr><th>Moment</th><th>What usually happens</th><th>What to decide now</th></tr></thead><tbody>
<tr><td>Before you leave</td><td>No plan, because it feels unnecessary</td><td>Fast-acting product in your pocket; decide your drink count; set a leaving time</td></tr>
<tr><td>First drink</td><td>The strongest cue arrives early</td><td>Use the product with the first drink, not after the first craving</td></tr>
<tr><td>Someone goes outside</td><td>Automatic following, no decision made</td><td>Pre-decide: you stay at the table, or you go out without smoking</td></tr>
<tr><td>Someone offers one</td><td>Improvised answer, social pressure</td><td>One short refusal sentence, rehearsed</td></tr>
<tr><td>Late in the evening</td><td>Tired, less cautious, the attempt looks abstract</td><td>Leave at the pre-set time rather than renegotiating it</td></tr>
</tbody></table></div>

<h2>Refusal sentences that end the topic</h2>
<ul>
<li>"I stopped. I am not doing one."</li>
<li>"Thanks, I am on day nine and I am not restarting the count."</li>
<li>"I will come out, but I am not smoking."</li>
<li>"If I have one tonight, I will be buying a pack tomorrow."</li>
</ul>
<p>Short sentences work better than explanations. An explanation invites a negotiation; a flat statement does
not. And if someone pushes anyway, repeating the same sentence verbatim is more effective than a second,
better-argued version.</p>

<h2>The five-minute rule, applied to a table</h2>
<p>A craving is an event with an end rather than a state. In a drinks situation, the version that works is:
step away from the table for five minutes, drink water, use the fast-acting product as instructed, and
reassess when the five minutes are up. NHS pages on cravings include former smokers describing exactly this
substitution — one describes using lozenges to help with cravings. The point is not the product, it is that
the hand-to-mouth routine gets an answer that is not a cigarette.</p>

<h2>A three-week plan</h2>
<ul>
<li><strong>Week 1:</strong> skip the situation entirely if you can. This is the cheapest decision available and nobody will remember.</li>
<li><strong>Week 2:</strong> attend, but with a shorter stay, a drink limit and a product in your pocket.</li>
<li><strong>Week 3:</strong> attend normally with the plan written down. If you have already done weeks 1 and 2, the cues have lost some power.</li>
<li><strong>Every week:</strong> tell one person at the table. The social cost of restarting in front of someone who knows is a useful counterweight.</li>
</ul>

<h2>If you slip</h2>
<p>NHS treats getting back on track after a slip as a normal part of the process rather than a failure state,
and CDC's position is that it is never too late to quit. The practical rule is that the second cigarette
matters more than the first: one cigarette at a table is an incident, and a pack bought the next morning is a
relapse. Deal with the morning, not with the guilt.</p>

<p>It also helps to know that quit success rates are lower than most people assume even with support, which
makes a failed attempt a common outcome rather than a personal verdict — see the figures quoted in
<a href="guide-20-minutes-per-cigarette.html" data-keep>where the 20-minute figure comes from</a>. If the
situation keeps winning, the answer is more support rather than more resolve: a
<a href="quitlines.html" data-keep>free counselling line</a> and two
<a href="guide-nicotine-replacement.html" data-keep>nicotine products instead of one</a>.</p>
""",
 'body_ko': """
<p>대부분의 금연 시도는 집에서 끝나지 않습니다. 특정한 의자, 특정한 시간, 보통 손에 술이 있고 누군가는 밖에서
담배를 피우는 자리에서 끝납니다. 이 페이지는 그 상황에 대한 것이고, 이 상황의 쓸모 있는 점은 예측 가능하다는
것입니다. 즉 테이블에서 협상하는 대신 미리 계획할 수 있습니다.</p>

<h2>이 상황이 금단과 다른 이유</h2>
<p>금단은 약해지는 증상입니다. 술자리는 방아쇠이고, 방아쇠는 저절로 약해지지 않습니다. NHS의 금연 유지 자료는
할 일을 나눕니다 — 흡연 욕구를 다루는 일, 금단증상을 관리하는 일, 한 번 피웠을 때 다시 궤도로 돌아오는 일.
술자리는 첫 번째와 세 번째에 속합니다. 두 번째에 쓴 의지가 여기서 도움이 되지 않는 이유입니다.</p>

<p>이 상황이 어려운 기계적인 이유도 있습니다. 신호가 겹쳐 있습니다. 장소, 시간대, 담배를 피우는 다른 사람,
수백 번 반복된 습관, 그리고 떨어진 경계심. 어느 것도 니코틴이 아닙니다. 그래서 10일째에 편안했던 사람이 3주째에
시도를 잃습니다.</p>

<h2>가기 전에 쓰는 계획</h2>
<div class="tw"><table><thead><tr><th>순간</th><th>보통 일어나는 일</th><th>지금 정해 둘 것</th></tr></thead><tbody>
<tr><td>나가기 전</td><td>필요 없어 보여서 계획이 없다</td><td>주머니에 속효성 제품, 술 잔 수, 나올 시각을 정한다</td></tr>
<tr><td>첫 잔</td><td>가장 강한 신호가 일찍 온다</td><td>첫 욕구 뒤가 아니라 첫 잔과 함께 제품을 쓴다</td></tr>
<tr><td>누가 밖으로 나갈 때</td><td>결정 없이 자동으로 따라 나간다</td><td>미리 정한다 — 자리에 남는다, 또는 나가도 피우지 않는다</td></tr>
<tr><td>누가 권할 때</td><td>즉흥적인 대답, 사회적 압력</td><td>연습해 둔 짧은 거절 문장 하나</td></tr>
<tr><td>늦은 시간</td><td>피곤하고 경계심이 떨어지고 금연이 추상적으로 보인다</td><td>정해 둔 시각에 나온다. 그 시각을 다시 협상하지 않는다</td></tr>
</tbody></table></div>

<h2>주제를 끝내는 거절 문장</h2>
<ul>
<li>"끊었습니다. 한 개비도 안 피웁니다."</li>
<li>"고맙지만 9일째예요. 날짜 다시 세기 싫습니다."</li>
<li>"같이 나가는 건 괜찮은데, 저는 안 피웁니다."</li>
<li>"오늘 한 개비 피우면 내일 한 갑 삽니다."</li>
</ul>
<p>짧은 문장이 설명보다 잘 통합니다. 설명은 협상을 초대하고, 단정은 그러지 않습니다. 그래도 밀어붙이면, 더 잘
논증한 두 번째 문장보다 같은 문장을 그대로 반복하는 편이 효과적입니다.</p>

<h2>테이블에 적용한 5분 규칙</h2>
<p>흡연 욕구는 상태가 아니라 끝이 있는 사건입니다. 술자리에서 통하는 형태는 이렇습니다. 5분간 자리를 벗어나고,
물을 마시고, 속효성 제품을 설명서대로 쓰고, 5분이 지난 뒤 다시 판단합니다. NHS의 흡연 욕구 관련 페이지에는
바로 이 대체를 설명하는 금연 경험자들의 말이 실려 있습니다. 한 사람은 욕구를 넘기는 데 로젠지를 썼다고 말합니다.
요점은 제품이 아니라, 손에서 입으로 가는 습관에 담배가 아닌 답을 준다는 것입니다.</p>

<h2>3주 계획</h2>
<ul>
<li><strong>1주차:</strong> 가능하면 그 자리를 아예 건너뜁니다. 가장 값싼 결정이고, 아무도 기억하지 않습니다.</li>
<li><strong>2주차:</strong> 참석하되 짧게 머물고, 잔 수를 정하고, 주머니에 제품을 넣습니다.</li>
<li><strong>3주차:</strong> 계획을 적어 두고 평소대로 참석합니다. 1·2주차를 거쳤다면 신호의 힘이 조금 빠져 있습니다.</li>
<li><strong>매주:</strong> 그 자리의 한 사람에게 말해 둡니다. 아는 사람 앞에서 다시 피우는 사회적 비용이 쓸모 있는 균형추가 됩니다.</li>
</ul>

<h2>한 번 피웠다면</h2>
<p>NHS는 실수 뒤 궤도로 돌아오는 것을 실패 상태가 아니라 과정의 정상적인 일부로 다루고, CDC의 입장은 금연에
늦은 때가 없다는 것입니다. 실무 규칙은 두 번째 담배가 첫 번째보다 중요하다는 것입니다. 술자리의 한 개비는
사건이고, 다음 날 아침에 산 한 갑은 재흡연입니다. 죄책감이 아니라 아침을 처리하십시오.</p>

<p>지원을 받아도 금연 성공률이 대부분의 사람이 생각하는 것보다 낮다는 사실을 아는 것도 도움이 됩니다. 실패한
시도는 개인에 대한 판결이 아니라 흔한 결과라는 뜻입니다. 수치는
<a href="guide-20-minutes-per-cigarette.html" data-keep>"20분" 숫자의 정체</a>에 인용해 두었습니다. 상황이 계속
이긴다면 답은 더 강한 결심이 아니라 더 많은 지원입니다.
<a href="quitlines.html" data-keep>무료 상담전화</a>와
<a href="guide-nicotine-replacement.html" data-keep>한 가지가 아니라 두 가지 제품</a>.</p>
""",
 'faq_en': [
  ('Why do so many quit attempts end at a drinks table?',
   'Because the cues are stacked: a familiar place, a time of day, other people smoking, a routine repeated hundreds of times and reduced caution. NHS material treats handling cravings and recovering from a slip as separate tasks from managing withdrawal symptoms.'),
  ('What do I say when someone offers me a cigarette?',
   'Use one short rehearsed sentence rather than an explanation, and repeat the same sentence if pressed. An explanation invites a negotiation; a flat statement ends the topic.'),
  ('I smoked one at a party. Is the attempt over?',
   'NHS treats getting back on track after a slip as part of the process, and CDC states that it is never too late to quit. The practical rule is that the second cigarette matters more than the first: deal with the next morning rather than the guilt.')],
 'faq_ko': [
  ('왜 금연 시도가 술자리에서 그렇게 많이 끝나나요?',
   '신호가 겹쳐 있기 때문입니다. 익숙한 장소, 시간대, 담배를 피우는 다른 사람, 수백 번 반복된 습관, 떨어진 경계심. NHS 자료는 욕구 대응과 실수 후 복귀를 금단증상 관리와는 별개의 과제로 다룹니다.'),
  ('담배를 권하면 무슨 말을 해야 하나요?',
   '설명 대신 연습해 둔 짧은 문장 하나를 쓰고, 계속 권하면 같은 문장을 그대로 반복하십시오. 설명은 협상을 초대하고, 단정은 주제를 끝냅니다.'),
  ('모임에서 한 개비 피웠습니다. 시도는 끝난 건가요?',
   'NHS는 실수 뒤 복귀를 과정의 일부로 다루고, CDC는 금연에 늦은 때가 없다고 기술합니다. 실무 규칙은 두 번째 담배가 첫 번째보다 중요하다는 것입니다. 죄책감이 아니라 다음 날 아침을 처리하십시오.')],
},

# ─────────────────────────────── 9
{
 'slug': 'guide-vaping-heated-tobacco',
 'cat': 'help',
 'title_en': 'Vapes and e-cigarettes versus cigarettes: what WHO, CDC and NHS actually say',
 'desc_en': 'What e-cigarettes are, how WHO describes the regulatory gap and youth use, what CDC states about safety, and the narrow case NHS makes for vapes as a quitting route.',
 'h1_en': 'Vapes and e-cigarettes versus cigarettes',
 'h1_ko': '전자담배·베이프 vs 일반담배 — 공식 기관들이 실제로 하는 말',
 'sub_en': 'Three official positions, side by side, including where they disagree.',
 'sub_ko': '세 기관의 공식 입장을 나란히. 서로 다른 지점까지.',
 'srcs': ['who_ecig_qa', 'cdc_ecig', 'nhs_treatments'],
 'rel': [('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('guide-withdrawal-symptoms.html', 'Withdrawal symptoms, stage by stage', '금단증상 단계별 대처'),
         ('guide-pregnancy-quit.html', 'Smoking, pregnancy and support', '임신 중 금연과 지원'),
         ('prices.html', 'Prices in 31 countries', '31개국 담뱃값 비교')],
 'body_en': """
<p>This is the one topic in quitting where credible public health bodies say visibly different things, and
summarising them into a single verdict would be dishonest. So this page puts the three positions side by side
and marks where they diverge.</p>

<h2>What the product is</h2>
<p>WHO describes e-liquids as products that may or may not contain nicotine but do not contain tobacco, and
places e-cigarettes within the broader categories of ENDS and ENNDS, which also include products such as
e-cigars and e-pipes. CDC states that e-cigarettes come in many shapes and sizes and that most e-cigarettes
contain nicotine.</p>

<h2>The three positions, side by side</h2>
<div class="tw"><table><thead><tr><th>Body</th><th>Position as published</th></tr></thead><tbody>
<tr><td>WHO</td><td>Describes these as harmful products and highlights a regulatory gap: 88 countries have no minimum age at which e-cigarettes can be bought and 74 countries have no regulations in place. Reports an alarming increase in use among children and young people, with rates exceeding adult use in many countries, and notes marketing to children through social media and influencers with at least 16,000 attractive flavours.</td></tr>
<tr><td>CDC</td><td>States that there are no safe tobacco products, including e-cigarettes, and that e-cigarettes should not be used by youth, young adults, or women who are pregnant.</td></tr>
<tr><td>NHS</td><td>States that using nicotine vapes can be a good way to quit smoking because they give you the nicotine hit without the harmful chemicals that come from burning tobacco, while also stating that vapes are not completely harmless, that they are safer than cigarettes, and that children and non-smokers should never vape.</td></tr>
</tbody></table></div>

<h2>How to read the disagreement</h2>
<p>The three statements are less contradictory than they look, because they answer different questions. NHS is
answering "what should an adult who currently smokes use to stop", and in that comparison the reference point
is a lit cigarette. WHO and CDC are answering "what should public policy do about a product category that is
being marketed to children", and in that comparison the reference point is not smoking at all. Both reference
points are legitimate; the error is quoting one body's answer as if it addressed the other's question.</p>

<ul>
<li>If you are an adult smoker choosing a quitting route, the NHS framing is the relevant one, with its two caveats attached.</li>
<li>If the question is about a young person, every one of the three bodies points the same way: do not start.</li>
<li>If the question is pregnancy, CDC states directly that e-cigarettes should not be used by women who are pregnant — see <a href="guide-pregnancy-quit.html" data-keep>the pregnancy guide</a>.</li>
</ul>

<h2>Where vapes sit next to the other products</h2>
<p>NHS places nicotine vapes alongside nicotine replacement therapies rather than apart from them: NRT comes as
patches, gum, sprays or lozenges, patches and mouth sprays weaken withdrawal symptoms, and the recommended
approach is to combine a fast-acting source with a slow-acting one. NHS also describes vapes as a way to slowly
cut down on nicotine. For the full comparison of forms, see the
<a href="guide-nicotine-replacement.html" data-keep>product guide</a>.</p>

<div class="box"><p><strong>On heated tobacco products.</strong> This page does not make claims about heated
tobacco products. On the confirmation date shown at the top we could not retrieve a WHO fact sheet or other
official page on that category at a working URL, and the rule on this site is that an unverified source means
no published claim. Regulation of these products also differs sharply by country; your
<a href="prices.html" data-keep>country page</a> records the indicators we do have.</p></div>

<h2>Checklist before using a vape to quit</h2>
<ul>
<li>Am I an adult who currently smokes? If not, all three bodies say do not start.</li>
<li>Do I have a plan to reduce nicotine over time, rather than an indefinite substitution?</li>
<li>Have I checked what is legal and age-restricted where I live? WHO records that many countries have no minimum age or no regulations at all.</li>
<li>Am I pregnant or planning to be? CDC states these should not be used in pregnancy.</li>
<li>Have I considered a patch plus a fast-acting product instead, which is what NHS recommends combining?</li>
</ul>

<h2>The one line all three agree on</h2>
<p>None of the three bodies describes any of these products as harmless. CDC's formulation is the shortest:
there are no safe tobacco products, including e-cigarettes. NHS's caveat says the same thing in comparative
form: not completely harmless, but safer than cigarettes. Keeping both halves of that sentence is the honest
way to use it — and the cost side of the comparison is on the
<a href="index.html" data-keep>calculator</a>, which counts what the current habit costs today.</p>
""",
 'body_ko': """
<p>금연 주제 가운데 신뢰할 만한 공공보건 기관들이 눈에 보이게 다른 말을 하는 거의 유일한 영역입니다. 이것을
하나의 결론으로 요약하는 것은 정직하지 않습니다. 그래서 이 페이지는 세 입장을 나란히 두고, 갈라지는 지점을
표시합니다.</p>

<h2>이 제품이 무엇인가</h2>
<p>WHO는 전자담배 액상(e-liquid)을 니코틴을 포함할 수도 있고 아닐 수도 있지만 담배(tobacco)는 들어 있지 않은
제품으로 설명하고, 전자담배를 e-시가·e-파이프 같은 제품을 포함하는 ENDS·ENNDS라는 더 넓은 범주 안에 둡니다.
CDC는 전자담배의 모양과 크기가 매우 다양하며 대부분의 전자담배에 니코틴이 들어 있다고 기술합니다.</p>

<h2>세 기관의 입장, 나란히</h2>
<div class="tw"><table><thead><tr><th>기관</th><th>공표된 입장</th></tr></thead><tbody>
<tr><td>WHO</td><td>이 제품들을 유해한 제품으로 기술하며 규제 공백을 지적합니다. 88개국은 전자담배 구매 최소 연령이 없고, 74개국은 관련 규제가 전혀 없습니다. 아동·청소년 사용이 우려스럽게 증가해 많은 나라에서 성인 사용률을 넘어섰다고 보고하고, 최소 1만 6천 가지 향과 소셜미디어·인플루언서를 통한 아동 대상 마케팅을 지적합니다.</td></tr>
<tr><td>CDC</td><td>전자담배를 포함해 안전한 담배 제품은 없으며, 전자담배는 청소년·청년·임신한 여성이 사용해서는 안 된다고 기술합니다.</td></tr>
<tr><td>NHS</td><td>니코틴 베이프가 담배를 태울 때 나오는 유해물질 없이 니코틴을 제공하므로 금연 방법이 될 수 있다고 하면서, 동시에 완전히 무해하지는 않고 담배보다 안전하며, 아동과 비흡연자는 절대 사용해서는 안 된다고 기술합니다.</td></tr>
</tbody></table></div>

<h2>이 불일치를 읽는 방법</h2>
<p>세 진술은 보이는 것보다 덜 모순적입니다. 서로 다른 질문에 답하고 있기 때문입니다. NHS는 "지금 담배를 피우는
성인이 끊기 위해 무엇을 쓸 것인가"에 답하고 있고, 그 비교의 기준점은 불붙은 담배입니다. WHO와 CDC는 "아동을
향해 마케팅되는 제품 범주에 공공정책이 무엇을 해야 하는가"에 답하고 있고, 그 비교의 기준점은 아무것도 피우지
않는 상태입니다. 두 기준점 모두 정당합니다. 오류는 한 기관의 답을 다른 기관의 질문에 대한 답처럼 인용하는
것입니다.</p>

<ul>
<li>지금 담배를 피우는 성인이 금연 경로를 고르는 상황이라면 NHS의 틀이 해당되며, 두 가지 유보 조건이 함께 붙습니다.</li>
<li>청소년에 대한 질문이라면 세 기관 모두 같은 방향을 가리킵니다 — 시작하지 말 것.</li>
<li>임신에 대한 질문이라면 CDC는 임신한 여성이 전자담배를 사용해서는 안 된다고 직접 기술합니다. <a href="guide-pregnancy-quit.html" data-keep>임신 가이드</a>를 보십시오.</li>
</ul>

<h2>베이프는 다른 제품들 옆에서 어디에 있는가</h2>
<p>NHS는 니코틴 베이프를 니코틴 대체요법과 떨어뜨리지 않고 같은 줄에 둡니다. NRT는 패치·껌·스프레이·로젠지
형태로 나오고, 패치와 구강 스프레이는 금단증상을 약화시키며, 권장되는 방식은 속효성 공급원과 지속형 공급원을
함께 쓰는 것입니다. NHS는 또 베이프를 니코틴을 천천히 줄여 나가는 방법으로 설명합니다. 제형별 전체 비교는
<a href="guide-nicotine-replacement.html" data-keep>제품 가이드</a>에 있습니다.</p>

<div class="box"><p><strong>궐련형 전자담배(히팅 제품)에 대하여.</strong> 이 페이지는 가열식 담배 제품에 대한
주장을 하지 않습니다. 상단의 확인일 기준으로 그 범주에 대한 WHO 팩트시트나 다른 공식 페이지를 작동하는 URL에서
받지 못했고, 이 사이트의 규칙은 확인되지 않은 출처는 곧 공표하지 않는다는 것입니다. 이 제품들의 규제는 나라마다
크게 다릅니다. 보유한 지표는 각 <a href="prices.html" data-keep>국가 페이지</a>에 기록돼 있습니다.</p></div>

<h2>베이프로 금연을 시도하기 전 점검표</h2>
<ul>
<li>나는 지금 담배를 피우는 성인인가? 아니라면 세 기관 모두 시작하지 말라고 말한다</li>
<li>무기한 대체가 아니라 니코틴을 줄여 나갈 계획이 있는가</li>
<li>내가 사는 곳의 합법 여부와 연령 제한을 확인했는가? WHO는 최소 연령이나 규제가 아예 없는 나라가 많다고 기록한다</li>
<li>임신 중이거나 계획 중인가? CDC는 임신 중 사용하지 말아야 한다고 기술한다</li>
<li>NHS가 권하는 조합 — 패치 + 속효성 제품 — 을 먼저 검토했는가</li>
</ul>

<h2>세 기관이 같은 말을 하는 한 줄</h2>
<p>세 기관 중 어느 곳도 이 제품들을 무해하다고 설명하지 않습니다. CDC의 표현이 가장 짧습니다 — 전자담배를
포함해 안전한 담배 제품은 없다. NHS의 유보 조건은 같은 말을 비교형으로 합니다 — 완전히 무해하지는 않지만
담배보다는 안전하다. 그 문장의 두 부분을 모두 유지하는 것이 정직한 사용법입니다. 비교의 비용 쪽은
<a href="index.html" data-keep>계산기</a>에 있습니다. 지금의 습관이 오늘 얼마인지를 셉니다.</p>
""",
 'faq_en': [
  ('Are vapes safer than cigarettes?',
   'NHS states that nicotine vapes are safer than cigarettes and can be a good way to quit because they deliver nicotine without the harmful chemicals from burning tobacco, while also stating that they are not completely harmless. CDC states that there are no safe tobacco products, including e-cigarettes.'),
  ('Why do WHO and NHS seem to disagree?',
   'They answer different questions. NHS is comparing a vape with a lit cigarette for an adult who smokes; WHO is assessing a product category marketed to children, where the comparison is with not using anything. WHO records that 88 countries have no minimum purchase age and 74 have no regulations.'),
  ('Does this page cover heated tobacco products?',
   'No. On the confirmation date shown at the top, no official fact sheet for that category could be retrieved at a working URL, and this site does not publish claims without a verified source.')],
 'faq_ko': [
  ('베이프가 담배보다 안전한가요?',
   'NHS는 니코틴 베이프가 담배보다 안전하며, 태울 때 나오는 유해물질 없이 니코틴을 제공하므로 금연 방법이 될 수 있다고 하면서 완전히 무해하지는 않다고 명시합니다. CDC는 전자담배를 포함해 안전한 담배 제품은 없다고 기술합니다.'),
  ('WHO와 NHS는 왜 다른 말을 하는 것처럼 보이나요?',
   '서로 다른 질문에 답하기 때문입니다. NHS는 담배를 피우는 성인에게 베이프와 불붙은 담배를 비교하고, WHO는 아동을 향해 마케팅되는 제품 범주를 평가하며 기준점이 "아무것도 쓰지 않는 상태"입니다. WHO는 구매 최소 연령이 없는 나라가 88개국, 규제가 없는 나라가 74개국이라고 기록합니다.'),
  ('이 페이지가 궐련형 전자담배도 다루나요?',
   '아닙니다. 상단의 확인일 기준으로 그 범주의 공식 팩트시트를 작동하는 URL에서 받지 못했고, 이 사이트는 확인된 출처 없이 주장을 싣지 않습니다.')],
},
]
