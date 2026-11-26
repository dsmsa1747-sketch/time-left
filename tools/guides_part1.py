# -*- coding: utf-8 -*-
"""가이드 1~3. 숫자·일정·규제 내용은 work/guide_probe.json 으로 실측된 출처에서만 왔다.
확인되지 않은 수치는 쓰지 않는다(빈칸이 틀린 숫자보다 낫다)."""

GUIDES = [

# ─────────────────────────────── 1
{
 'slug': 'guide-first-72-hours',
 'cat': 'body',
 'title_en': 'The first 72 hours after your last cigarette, hour by hour',
 'desc_en': 'What WHO and CDC say happens in the body in the first three days after quitting smoking, what withdrawal feels like, and five things to do when a craving hits.',
 'h1_en': 'The first 72 hours after your last cigarette',
 'h1_ko': '금연 첫 72시간 — 시간대별로 몸에서 일어나는 일',
 'sub_en': 'What changes at 20 minutes, 12 hours and 3 days, and what to do when it gets hard.',
 'sub_ko': '20분·12시간·3일에 무엇이 바뀌는지, 힘들 때 무엇을 하는지.',
 'srcs': ['who_cessation_qa', 'cdc_benefits', 'medlineplus'],
 'rel': [('guide-withdrawal-symptoms.html', 'Withdrawal symptoms, stage by stage', '금단증상 단계별 대처'),
         ('timeline.html', 'The full recovery timeline', '전체 회복 타임라인'),
         ('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('quitlines.html', 'Free quitlines by country', '나라별 무료 금연상담전화')],
 'body_en': """
<p>Most people quit for the first three days and then decide the rest based on how those three days went.
That is the wrong order, but it is how it actually happens. So it is worth knowing in advance what the first
72 hours are, what is real physiology and what is withdrawal, and which parts get better on their own.</p>

<p>The timings below are not our estimates. They come from the WHO question-and-answer page on the health
benefits of smoking cessation, which lists the beneficial changes by the time since the last cigarette.</p>

<h2>The first day</h2>
<div class="tw"><table><thead><tr><th>Time since last cigarette</th><th>What WHO lists</th></tr></thead><tbody>
<tr><td>Within 20 minutes</td><td>Heart rate and blood pressure drop</td></tr>
<tr><td>12 hours</td><td>The carbon monoxide level in your blood drops to normal</td></tr>
<tr><td>2 to 12 weeks</td><td>Circulation improves and lung function increases</td></tr>
<tr><td>1 to 9 months</td><td>Coughing and shortness of breath decrease</td></tr>
</tbody></table></div>

<p>Two things are worth noticing about that table. First, the first entry is measured in minutes, which is the
single most useful fact about quitting: the body does not wait for a milestone, and nothing has to be earned.
Second, nothing in the first 72 hours is dramatic from the outside. Blood pressure and carbon monoxide are not
things you feel. What you feel in the first three days is mostly withdrawal, and withdrawal is a separate
process from recovery running on a different clock.</p>

<h2>What withdrawal actually is</h2>
<p>MedlinePlus, the consumer health service of the US National Library of Medicine, puts it plainly: when you
stop or cut back on smoking, you may have short-term effects such as irritability, anxiety, moodiness, weight
gain or trouble sleeping, and these are called withdrawal symptoms. Two words in that sentence do the work.
<strong>Short-term</strong>, because the symptoms have an end date even when it does not feel that way at hour
30. And <strong>effects</strong>, not damage — nothing in that list is an injury, which is why the standard
advice is to get through them rather than to treat them as a reason to stop quitting.</p>

<p>The practical consequence: in the first 72 hours, judge yourself on behaviour, not on mood. Mood is the
symptom. Behaviour is the thing you control.</p>

<h2>Hour by hour, roughly</h2>
<ul class="tl">
<li><span class="t">0-4 h</span><span>Heart rate and blood pressure start to fall. Cravings arrive in waves, usually a few minutes long, triggered by routine more than by nicotine.</span></li>
<li><span class="t">4-12 h</span><span>Carbon monoxide clears toward normal. The first difficult evening: the habit is tied to specific moments — after a meal, in the car, with coffee or alcohol.</span></li>
<li><span class="t">12-24 h</span><span>Irritability and restlessness are common. Sleep is often disrupted. This is usually the hardest single stretch for people who smoked on waking.</span></li>
<li><span class="t">24-48 h</span><span>Appetite often increases. Concentration dips. Cravings are still frequent but each one is no longer a surprise.</span></li>
<li><span class="t">48-72 h</span><span>For most people the peak has passed and the frequency of cravings begins to drop, while situational triggers stay. Circulation and lung function improvements have started but are measured in weeks, not days.</span></li>
</ul>

<h2>Five things that work during a craving</h2>
<ul>
<li><strong>Wait it out on a timer.</strong> A craving is an event with an end, not a state. Four minutes on a phone timer is longer than most of them last.</li>
<li><strong>Change the room.</strong> Most cravings are triggered by a place and a routine. Leaving the trigger usually ends the craving faster than resisting it inside the trigger.</li>
<li><strong>Use a product, not willpower, if you have one.</strong> NHS guidance is that nicotine replacement weakens withdrawal symptoms, and that combining a fast-acting form with a patch works better than either alone. See the <a href="guide-nicotine-replacement.html" data-keep>comparison guide</a>.</li>
<li><strong>Call the free line.</strong> CDC states that quitlines provide free coaching over the phone. It costs nothing and it is designed for exactly this hour.</li>
<li><strong>Keep the number in front of you.</strong> Not the money you will save in ten years — the number for today. That is what the <a href="index.html" data-keep>calculator</a> is for.</li>
</ul>

<h2>Day three checklist</h2>
<ul>
<li>Did I remove cigarettes, lighters and ashtrays from the house and the car?</li>
<li>Do I have a plan for the two situations that broke previous attempts?</li>
<li>Do I have the quitline number saved, or an appointment booked with a stop-smoking service?</li>
<li>Have I told one person who will ask me about it on day seven?</li>
<li>Am I treating sleep and food as part of the plan rather than as separate problems?</li>
</ul>

<h2>What not to conclude from three good days</h2>
<p>CDC's summary of the evidence is that quitting reduces the risk of premature death and can add as much as ten
years to life expectancy, and that risk of coronary heart disease falls sharply one to two years after
cessation. Those are the real payoffs, and none of them are visible at 72 hours. The first three days are not
the reward; they are the entry fee. The useful mental model is that you are not trying to feel better by Friday
— you are trying to still be a non-smoker in March.</p>

<p>A slip is also not the end of an attempt. CDC's position is that it is never too late to quit, which applies
to the fourth attempt as much as to the first. What matters after a slip is how quickly the next cigarette is
refused, not how clean the record is.</p>
""",
 'body_ko': """
<p>많은 사람이 사실상 3일만 금연하고, 나머지는 그 3일이 어땠는지를 보고 결정합니다. 순서가 거꾸로지만 현실은
그렇습니다. 그래서 첫 72시간에 무엇이 일어나는지, 어디까지가 회복이고 어디까지가 금단인지 미리 알아두는 것이
도움이 됩니다.</p>

<p>아래 시간표는 저희 추정치가 아닙니다. 세계보건기구(WHO)의 '금연의 건강상 이득' 질의응답 페이지가 마지막
담배 이후 경과 시간별로 제시한 변화입니다.</p>

<h2>첫째 날</h2>
<div class="tw"><table><thead><tr><th>마지막 담배 이후</th><th>WHO가 제시한 변화</th></tr></thead><tbody>
<tr><td>20분 이내</td><td>심박수와 혈압이 내려간다</td></tr>
<tr><td>12시간</td><td>혈중 일산화탄소 농도가 정상 수준으로 떨어진다</td></tr>
<tr><td>2~12주</td><td>혈액순환이 좋아지고 폐 기능이 향상된다</td></tr>
<tr><td>1~9개월</td><td>기침과 숨가쁨이 줄어든다</td></tr>
</tbody></table></div>

<p>이 표에서 두 가지를 보십시오. 첫째, 첫 항목의 단위가 '분'입니다. 금연에 대해 가장 쓸모 있는 사실이 여기
있습니다. 몸은 어떤 기념일을 기다리지 않고, 무엇을 증명해야 시작되는 것도 아닙니다. 둘째, 첫 72시간 동안
겉으로 드라마틱한 일은 없습니다. 혈압과 일산화탄소는 느껴지는 것이 아닙니다. 3일 동안 실제로 느끼는 것은
대부분 금단이고, 금단은 회복과 다른 시계로 돌아가는 별개의 과정입니다.</p>

<h2>금단은 무엇인가</h2>
<p>미국 국립의학도서관의 소비자 건강정보 서비스 MedlinePlus는 이렇게 씁니다 — 담배를 끊거나 줄이면 짜증,
불안, 기분 변화, 체중 증가, 수면 장애 같은 단기적 영향이 나타날 수 있고, 이것을 금단증상이라고 부른다.
이 문장에서 중요한 단어는 두 개입니다. <strong>단기적</strong>이라는 말 — 30시간째에는 그렇게 느껴지지
않더라도 끝이 있다는 뜻입니다. 그리고 <strong>영향</strong>이라는 말 — 손상이 아니라는 뜻입니다. 그래서
표준적인 권고는 금단을 치료 대상이 아니라 '지나갈 구간'으로 다루는 것입니다.</p>

<p>실천적 결론은 이렇습니다. 첫 72시간에는 기분이 아니라 행동으로 자신을 평가하십시오. 기분은 증상이고,
행동은 통제할 수 있는 영역입니다.</p>

<h2>대략의 시간대별 흐름</h2>
<ul class="tl">
<li><span class="t">0~4시간</span><span>심박수와 혈압이 내려가기 시작합니다. 흡연 욕구는 파도처럼 오고, 보통 몇 분이면 지나갑니다. 니코틴보다 '습관의 순간'이 방아쇠입니다.</span></li>
<li><span class="t">4~12시간</span><span>일산화탄소가 정상 쪽으로 빠집니다. 첫 번째 힘든 저녁입니다. 식후, 차 안, 커피나 술자리처럼 특정 장면에 묶인 습관이 드러납니다.</span></li>
<li><span class="t">12~24시간</span><span>짜증과 안절부절함이 흔합니다. 잠이 자주 깹니다. 기상 직후에 피우던 사람에게는 보통 이 구간이 가장 힘듭니다.</span></li>
<li><span class="t">24~48시간</span><span>식욕이 늘고 집중이 떨어집니다. 욕구는 여전히 자주 오지만 더 이상 '예상 못 한 일'은 아닙니다.</span></li>
<li><span class="t">48~72시간</span><span>대부분의 사람에게 정점이 지나고 욕구의 빈도가 줄기 시작합니다. 다만 상황 방아쇠는 남습니다. 혈액순환·폐 기능 개선은 시작됐지만 단위가 주(週)입니다.</span></li>
</ul>

<h2>욕구가 올 때 실제로 통하는 다섯 가지</h2>
<ul>
<li><strong>타이머를 켜고 기다린다.</strong> 흡연 욕구는 상태가 아니라 사건입니다. 끝이 있습니다. 휴대폰 타이머 4분이면 대부분의 욕구보다 깁니다.</li>
<li><strong>방을 바꾼다.</strong> 욕구는 장소와 습관이 함께 당깁니다. 방아쇠 안에서 참는 것보다 방아쇠를 떠나는 것이 빠릅니다.</li>
<li><strong>의지 대신 제품을 쓴다.</strong> 영국 NHS는 니코틴 대체요법이 금단증상을 약화시키며, 속효성 제형과 패치를 함께 쓰는 것이 어느 한쪽만 쓰는 것보다 낫다고 안내합니다. <a href="guide-nicotine-replacement.html" data-keep>비교 가이드</a>를 보십시오.</li>
<li><strong>무료 전화를 쓴다.</strong> 미국 CDC는 금연상담전화가 전화로 무료 코칭을 제공한다고 명시합니다. 비용이 없고, 바로 이 시간을 위해 만들어진 서비스입니다.</li>
<li><strong>숫자를 눈앞에 둔다.</strong> 10년 뒤 모을 돈이 아니라 오늘의 숫자입니다. <a href="index.html" data-keep>계산기</a>가 그 용도입니다.</li>
</ul>

<h2>3일째 점검표</h2>
<ul>
<li>집과 차에서 담배·라이터·재떨이를 치웠는가</li>
<li>지난 시도를 무너뜨린 두 가지 상황에 대한 계획이 있는가</li>
<li>금연상담전화 번호를 저장했거나 보건소 금연클리닉 예약을 했는가</li>
<li>7일째에 나에게 물어볼 사람 한 명에게 말했는가</li>
<li>잠과 식사를 별개 문제가 아니라 계획의 일부로 다루고 있는가</li>
</ul>

<h2>3일이 잘 갔다고 해서 결론 내리지 말 것</h2>
<p>CDC는 근거를 요약해, 금연이 조기 사망 위험을 낮추고 기대수명을 최대 10년까지 늘릴 수 있으며, 관상동맥
심장질환 위험은 금연 후 1~2년에 급격히 떨어진다고 기술합니다. 진짜 보상은 그쪽이고, 72시간에는 아무것도
보이지 않습니다. 첫 3일은 보상이 아니라 입장료입니다. 쓸모 있는 기준은 '금요일까지 기분이 좋아지는 것'이
아니라 '3월에도 비흡연자인 것'입니다.</p>

<p>한 번 피운 것이 시도의 끝도 아닙니다. CDC의 입장은 금연에 늦은 때는 없다는 것이고, 이는 첫 시도만큼
네 번째 시도에도 적용됩니다. 실수 뒤에 중요한 것은 기록이 깨끗한지가 아니라 다음 한 개비를 얼마나 빨리
거절하는지입니다.</p>
""",
 'faq_en': [
  ('When is withdrawal at its worst?',
   'Most people describe the first 24 to 72 hours as the hardest stretch, with cravings arriving in short waves. MedlinePlus lists irritability, anxiety, moodiness, weight gain and trouble sleeping as short-term withdrawal effects rather than lasting harm.'),
  ('What actually changes in the first day?',
   'WHO lists two measurable changes inside 24 hours: heart rate and blood pressure drop within 20 minutes, and blood carbon monoxide falls to a normal level by 12 hours. Neither is something you can feel, which is why day one feels like withdrawal rather than recovery.'),
  ('Is it worth quitting if I have smoked for decades?',
   'CDC states that even people who have smoked for many years or smoked heavily will benefit from quitting, and that quitting can add as much as ten years to life expectancy. WHO puts the gain at about six years for someone quitting around age 50 and about three years at around 60.')],
 'faq_ko': [
  ('금단은 언제 가장 심한가요?',
   '대부분 첫 24~72시간을 가장 힘든 구간으로 말하며, 흡연 욕구는 짧은 파도처럼 옵니다. MedlinePlus는 짜증·불안·기분 변화·체중 증가·수면 장애를 지속적 손상이 아닌 단기 금단 영향으로 분류합니다.'),
  ('첫날에 실제로 바뀌는 것은 무엇인가요?',
   'WHO는 24시간 안의 변화로 두 가지를 제시합니다. 20분 안에 심박수와 혈압이 내려가고, 12시간이면 혈중 일산화탄소가 정상 수준으로 떨어집니다. 둘 다 느껴지지 않는 변화라서 첫날은 회복보다 금단으로 체감됩니다.'),
  ('수십 년 피웠는데 지금 끊어도 의미가 있나요?',
   'CDC는 오래 피웠거나 많이 피운 사람도 금연으로 이득을 얻으며, 금연이 기대수명을 최대 10년까지 늘릴 수 있다고 기술합니다. WHO는 50세 무렵 금연 시 약 6년, 60세 무렵 약 3년의 기대수명 이득을 제시합니다.')],
},

# ─────────────────────────────── 2
{
 'slug': 'guide-nicotine-replacement',
 'cat': 'help',
 'title_en': 'Nicotine replacement compared: patches, gum, lozenges, spray, prescription medicines',
 'desc_en': 'How patches, gum, lozenges and mouth spray differ, why NHS recommends combining a patch with a fast-acting product, and where nicotine-free prescription medicines fit.',
 'h1_en': 'Nicotine replacement compared, and when to combine two',
 'h1_ko': '니코틴 대체요법 비교 — 패치·껌·로젠지·스프레이·처방약',
 'sub_en': 'Fast-acting versus slow-acting, what NHS says about combining them, and what to ask a clinician.',
 'sub_ko': '속효성과 지속형의 차이, NHS가 권하는 병용, 의료진에게 물어볼 것.',
 'srcs': ['nhs_treatments', 'cdc_nrt', 'medlineplus'],
 'rel': [('guide-first-72-hours.html', 'The first 72 hours', '금연 첫 72시간'),
         ('guide-withdrawal-symptoms.html', 'Withdrawal symptoms, stage by stage', '금단증상 단계별 대처'),
         ('guide-korea-quit-support.html', 'Free help in South Korea', '한국의 무료 금연지원'),
         ('quitlines.html', 'Free quitlines by country', '나라별 무료 금연상담전화')],
 'body_en': """
<p>Nicotine replacement therapy (NRT) is the least interesting part of quitting and the part most often skipped.
NHS guidance states that nicotine has been safely used in stop-smoking products for years, and that NRT
products such as patches and mouth sprays weaken withdrawal symptoms. That is the entire pitch: the products do
not make the decision for you, they lower the height of the wall.</p>

<h2>The one distinction that matters</h2>
<p>Every product is either slow-acting or fast-acting, and the choice is not about preference.</p>

<div class="tw"><table><thead><tr><th>Form</th><th>Speed</th><th>What it is for</th><th>Practical notes</th></tr></thead><tbody>
<tr><td>Patch</td><td>Slow, steady</td><td>Baseline nicotine through the day, so withdrawal does not build</td><td>Applied once a day; nothing to do when a craving hits</td></tr>
<tr><td>Gum</td><td>Fast</td><td>A specific craving, a specific trigger</td><td>Needs correct use rather than continuous chewing</td></tr>
<tr><td>Lozenge</td><td>Fast</td><td>Same as gum, without chewing</td><td>Discreet; one former smoker quoted by NHS used lozenges for cravings</td></tr>
<tr><td>Mouth spray</td><td>Fastest of the oral forms</td><td>Sudden, intense cravings</td><td>NHS names mouth spray specifically as a fast-acting partner for a patch</td></tr>
<tr><td>Nicotine vape</td><td>Fast</td><td>Replacing the smoking routine as well as the nicotine</td><td>NHS: safer than cigarettes but not completely harmless; children and non-smokers should never vape</td></tr>
<tr><td>Nicotine-free medicines</td><td>Prescription</td><td>Blocking the effects of nicotine in the brain</td><td>From a stop-smoking service or GP; varenicline is available again in the UK alongside a newer option, cytisine</td></tr>
</tbody></table></div>

<h2>Why NHS recommends two products, not one</h2>
<p>The NHS stop-smoking treatments page is unusually direct about this: the best approach is to combine a
fast-acting source of nicotine, like a mouth spray, with a slow-acting source, like a patch, that eases you out
of dependence without tipping you into withdrawal. Read the logic rather than the brand names. A patch cannot
respond to an event; a spray cannot hold a baseline for sixteen hours. Using only the fast form means you spend
the day climbing out of withdrawal, and using only the patch means you have nothing for the moment that
actually breaks attempts.</p>

<p>If you have tried NRT before and concluded it does not work, it is worth checking which of the two halves
you were missing. "Patch only" and "gum only" are the two most common versions of a failed NRT attempt.</p>

<h2>Where prescription medicines fit</h2>
<p>NHS describes nicotine-free medicines as mostly working by blocking the effects of nicotine in your brain,
making smoking less enjoyable, and says they may be available from a local stop-smoking service or a GP. Two
points follow. First, these are a different mechanism from NRT, not a stronger version of it. Second, they
require a clinician, which means the realistic first step is an appointment rather than a shop.</p>

<div class="box warn"><p>This page compares categories, not doses or brands. Dosing, interactions, pregnancy,
heart conditions and age limits are clinical questions. Ask a pharmacist, your doctor or your national quitline
before starting, and follow the product instructions rather than this page.</p></div>

<h2>What the products cost you</h2>
<p>Cost is where the country you live in decides the answer. WHO's country-level indicators record both whether
NRT is legally sold and whether its cost is covered, and the answer varies from fully covered to not covered at
all. Rather than guess, we publish the recorded value on each country page — see the
<a href="prices.html" data-keep>price and support table</a> and then the page for your country. For a worked
example of a national programme, see <a href="guide-korea-quit-support.html" data-keep>free help in South
Korea</a>.</p>

<p>One number is worth putting next to the price of any product: what you currently spend on cigarettes. For a
pack-a-day smoker the comparison is rarely close, and the <a href="index.html" data-keep>calculator</a> will
show the daily figure rather than an annual abstraction.</p>

<h2>Checklist before you start</h2>
<ul>
<li>Have I chosen one slow-acting product and one fast-acting product?</li>
<li>Do I know how to use the fast-acting one correctly, including how long to wait for effect?</li>
<li>Have I checked whether a stop-smoking service or clinic in my country supplies these free or subsidised?</li>
<li>Have I asked a pharmacist or clinician about my own medical conditions and medicines?</li>
<li>Do I have a plan for week three, when the products are still needed but motivation is lower?</li>
</ul>

<h2>Two mistakes that make NRT look useless</h2>
<p>The first is stopping the product the moment the worst of withdrawal passes, which removes the baseline just
as situational triggers take over. The second is under-dosing out of caution so that the patch is a gesture
rather than a replacement. CDC frames quit medicines as one of several proven approaches that can help with
cravings and can be used with or without coaching — which is a reminder that the products and the support are
additive, and that the free coaching line is not a lesser option.</p>
""",
 'body_ko': """
<p>니코틴 대체요법(NRT)은 금연에서 가장 재미없는 부분이고, 그래서 가장 자주 생략되는 부분입니다. 영국 NHS는
니코틴이 금연 보조제에 오랫동안 안전하게 사용돼 왔으며, 패치나 구강 스프레이 같은 NRT 제품이 금단증상을
약화시킨다고 안내합니다. 이것이 전부입니다. 제품이 결심을 대신해 주지는 않지만, 넘어야 할 벽의 높이를
낮춥니다.</p>

<h2>중요한 구분은 하나다</h2>
<p>모든 제형은 지속형이거나 속효성이며, 이 선택은 취향 문제가 아닙니다.</p>

<div class="tw"><table><thead><tr><th>제형</th><th>작용 속도</th><th>무엇을 위한 것인가</th><th>실무 메모</th></tr></thead><tbody>
<tr><td>패치</td><td>느리고 일정함</td><td>하루 동안 기본 니코틴을 유지해 금단이 쌓이지 않게 함</td><td>하루 한 번 부착. 욕구가 올 때 할 수 있는 조치가 없음</td></tr>
<tr><td>껌</td><td>빠름</td><td>특정 순간, 특정 방아쇠</td><td>계속 씹는 것이 아니라 정해진 사용법대로 써야 함</td></tr>
<tr><td>로젠지(정제)</td><td>빠름</td><td>껌과 같은 용도, 씹지 않음</td><td>눈에 덜 띔. NHS 페이지의 금연 경험자 인용에도 로젠지로 욕구를 넘겼다는 사례가 있음</td></tr>
<tr><td>구강 스프레이</td><td>경구 제형 중 가장 빠름</td><td>갑작스럽고 강한 욕구</td><td>NHS가 패치와 짝지을 속효성 제형으로 직접 지목</td></tr>
<tr><td>니코틴 베이프</td><td>빠름</td><td>니코틴과 함께 '피우는 행동'까지 대체</td><td>NHS: 담배보다 안전하지만 완전히 무해하지는 않음. 아동·비흡연자는 사용 금지</td></tr>
<tr><td>니코틴 없는 처방약</td><td>처방 필요</td><td>뇌에서 니코틴의 작용을 차단</td><td>금연 서비스나 일반의 경유. 영국에서는 바레니클린이 다시 공급되며 새 선택지로 시티신이 있음</td></tr>
</tbody></table></div>

<h2>NHS가 한 가지가 아니라 두 가지를 권하는 이유</h2>
<p>NHS 금연 보조제 페이지는 이 부분을 분명하게 씁니다 — 가장 좋은 방법은 구강 스프레이처럼 빠르게 작용하는
니코틴 공급원과, 패치처럼 느리게 작용하는 공급원을 함께 써서 금단으로 넘어가지 않으면서 의존에서 빠져나오는
것이다. 제품명보다 논리를 보십시오. 패치는 사건에 반응할 수 없고, 스프레이는 16시간의 기본선을 유지할 수
없습니다. 속효성만 쓰면 하루 종일 금단에서 기어올라오게 되고, 패치만 쓰면 시도를 실제로 깨뜨리는 그 순간에
쓸 것이 없습니다.</p>

<p>전에 NRT를 써 봤는데 효과가 없었다고 결론 내렸다면, 두 절반 중 어느 쪽이 빠져 있었는지 확인해 볼 만합니다.
'패치만' 과 '껌만' 이 실패한 NRT 시도의 가장 흔한 두 형태입니다.</p>

<h2>처방약의 자리</h2>
<p>NHS는 니코틴 없는 약들이 대체로 뇌에서 니코틴의 작용을 차단해 흡연을 덜 즐겁게 만드는 방식으로 작용하며,
지역 금연 서비스나 일반의를 통해 받을 수 있다고 설명합니다. 두 가지가 따라옵니다. 첫째, 이것은 NRT의 강한
버전이 아니라 다른 작용 기전입니다. 둘째, 의료진이 필요합니다. 즉 현실적인 첫걸음은 약국 진열대가 아니라
진료 예약입니다.</p>

<div class="box warn"><p>이 페이지는 제형의 범주를 비교하며 용량이나 제품명을 권하지 않습니다. 용량, 약물
상호작용, 임신, 심장질환, 연령 제한은 임상적 판단이 필요한 문제입니다. 시작 전에 약사·의사 또는 금연상담
전화에 문의하고, 이 페이지보다 제품 설명서를 따르십시오.</p></div>

<h2>제품 비용은 사는 나라가 결정한다</h2>
<p>WHO의 국가별 지표에는 NRT가 합법적으로 판매되는지, 그리고 그 비용이 보장되는지가 기록돼 있고, 답은 전액
보장부터 전혀 보장되지 않음까지 나라마다 다릅니다. 추측하지 않고, 각 국가 페이지에 기록된 값을 그대로
표시합니다. <a href="prices.html" data-keep>가격·지원 표</a>에서 해당 국가 페이지로 들어가 보십시오.
국가 프로그램의 실제 예시는 <a href="guide-korea-quit-support.html" data-keep>한국의 무료 금연지원</a>에
있습니다.</p>

<p>어떤 제품의 가격이든 그 옆에 함께 둘 숫자가 하나 있습니다. 지금 담배에 쓰는 돈입니다. 하루 한 갑이면 비교가
팽팽한 경우는 드뭅니다. <a href="index.html" data-keep>계산기</a>는 연간 추상치가 아니라 오늘의 금액을
보여줍니다.</p>

<h2>시작 전 점검표</h2>
<ul>
<li>지속형 하나와 속효성 하나를 골랐는가</li>
<li>속효성 제형의 정확한 사용법과 효과까지 걸리는 시간을 아는가</li>
<li>내 나라의 금연 서비스·보건소가 이것을 무료 또는 일부 지원으로 주는지 확인했는가</li>
<li>내 기저질환과 복용 약에 대해 약사·의료진에게 물었는가</li>
<li>제품은 아직 필요하지만 동기는 떨어지는 3주차 계획이 있는가</li>
</ul>

<h2>NRT가 쓸모없어 보이게 만드는 두 가지 실수</h2>
<p>첫째는 금단의 정점이 지나는 순간 제품을 끊는 것입니다. 상황 방아쇠가 주도권을 가져가는 바로 그 시점에
기본선을 치워버리는 셈입니다. 둘째는 조심스러워서 용량을 너무 낮게 쓰는 것입니다. 그러면 패치가 대체가 아니라
제스처가 됩니다. CDC는 금연 치료제를 흡연 욕구에 도움이 될 수 있는 여러 검증된 접근 중 하나로 설명하며,
코칭과 함께 쓰거나 따로 쓸 수 있다고 안내합니다. 제품과 지원은 서로를 대체하지 않고 더해지며, 무료 상담전화는
열등한 선택지가 아니라는 뜻입니다.</p>
""",
 'faq_en': [
  ('Should I use a patch or gum?',
   'NHS guidance is to combine them: a fast-acting form such as a mouth spray for cravings plus a slow-acting patch that eases you out of dependence without tipping you into withdrawal. Using only one of the two is the most common form of a failed NRT attempt.'),
  ('Are nicotine vapes an acceptable way to quit?',
   'NHS states that nicotine vapes can be a good way to quit because they deliver nicotine without the harmful chemicals from burning tobacco, while also stating that they are not completely harmless and that children and non-smokers should never vape.'),
  ('What are the nicotine-free medicines?',
   'NHS describes them as medicines that mostly work by blocking the effects of nicotine in the brain, making smoking less enjoyable, available through a local stop-smoking service or a GP. In the UK, varenicline is available again alongside a newer option called cytisine.')],
 'faq_ko': [
  ('패치를 써야 하나요, 껌을 써야 하나요?',
   'NHS는 병용을 권합니다. 욕구가 올 때 쓰는 구강 스프레이 같은 속효성 제형과, 금단으로 넘어가지 않게 의존에서 빠져나오도록 돕는 지속형 패치를 함께 쓰는 방식입니다. 둘 중 하나만 쓰는 것이 실패한 NRT 시도의 가장 흔한 형태입니다.'),
  ('니코틴 베이프로 끊어도 되나요?',
   'NHS는 니코틴 베이프가 담배를 태울 때 나오는 유해물질 없이 니코틴을 제공하므로 금연 방법이 될 수 있다고 하면서, 동시에 완전히 무해하지는 않으며 아동과 비흡연자는 절대 사용해서는 안 된다고 명시합니다.'),
  ('니코틴이 없는 처방약은 무엇인가요?',
   'NHS는 이 약들이 대체로 뇌에서 니코틴의 작용을 차단해 흡연을 덜 즐겁게 만들며, 지역 금연 서비스나 일반의를 통해 받을 수 있다고 설명합니다. 영국에서는 바레니클린이 다시 공급되고 있고 시티신이라는 새 선택지도 있습니다.')],
},

# ─────────────────────────────── 3
{
 'slug': 'guide-korea-cigarette-price-history',
 'cat': 'money',
 'title_en': 'What is inside a Korean pack price: tax share, per-cigarette cost, and why price is the policy lever',
 'desc_en': 'The verified parts of the Korean pack price - WHO tax share, price per cigarette, a year of a pack a day - and why WHO calls tobacco taxation the single most effective measure.',
 'h1_en': 'What is inside a Korean pack price',
 'h1_ko': '한국 담뱃값에 들어 있는 것 — 세금 비중과 가격의 구조',
 'sub_en': 'Tax share, cost per cigarette, and what WHO says about price as a policy lever.',
 'sub_ko': '세금 비중, 개비당 가격, 그리고 WHO가 말하는 가격 정책의 효과.',
 'srcs': ['who_tax', 'who_tobacco', 'kr_guide'],
 'rel': [('guide-cigarette-tax-share.html', 'Tax share of the pack price, country by country', '나라별 담뱃값 세금 비중'),
         ('cost-of-smoking-south-korea.html', 'Smoking in South Korea: price, rules and free help', '대한민국 — 담뱃값·규제·금연지원'),
         ('guide-korea-quit-support.html', 'Free help in South Korea', '한국의 무료 금연지원'),
         ('prices.html', 'Prices in 31 countries', '31개국 담뱃값 비교')],
 'body_en': """
<p>A pack price looks like one number and is actually three: the product, the tax, and the retailer. This page
publishes only the parts we can source, which for South Korea means the pack price we use across the site and
the tax share recorded in WHO's country indicators. Where a figure is not published, we leave it out rather
than estimate it.</p>

<h2>The Korean pack, as recorded</h2>
{{KR_TABLE}}

<p>The tax share comes from the WHO Global Health Observatory tobacco indicator series, with the reference year
shown in the table. The pack price is the figure used throughout this site, including on the
<a href="cost-of-smoking-south-korea.html" data-keep>South Korea page</a> and in the
<a href="prices.html" data-keep>31-country table</a>. The per-cigarette and annual figures are arithmetic on
those two inputs, not survey data.</p>

<h2>Why the tax share is the interesting line</h2>
<p>WHO's position on tobacco taxation is not hedged: evidence shows that significantly increasing tobacco
excise taxes and prices is the single most effective and cost-effective measure for reducing tobacco use, and
raising taxes on tobacco products which lead to increases in their price makes tobacco less affordable. That is
the mechanism behind every price rise that smokers experience as a personal budget problem — it is designed to
be a budget problem.</p>

<p>It also explains why the tax share, rather than the headline price, is the number to watch. A country can
have a high nominal price because it is wealthy, or because its tax policy is aggressive. The share separates
the two. The <a href="guide-cigarette-tax-share.html" data-keep>country comparison guide</a> lists the recorded
share for every country where WHO publishes one.</p>

<h2>What a price rise does to a daily habit</h2>
<div class="tw"><table><thead><tr><th>If the pack price rises by</th><th>Extra cost of a pack a day over a year</th></tr></thead><tbody>
<tr><td>5%</td><td>5% of the annual figure in the table above</td></tr>
<tr><td>10%</td><td>10% of the annual figure</td></tr>
<tr><td>20%</td><td>20% of the annual figure</td></tr>
</tbody></table></div>
<p>The row that matters is the one you are already paying. Because the annual cost of a daily pack is a simple
multiple, every percentage point of price increase is also a percentage point of an already large annual number
— which is exactly why WHO treats price as the strongest lever available to a government.</p>

<h2>What this page does not claim</h2>
<div class="box"><p>We do not publish a year-by-year Korean price history here. A table of annual prices and
tax changes requires official year-series data from the Korean tax and health authorities, and on the date
shown at the top of this page we could not retrieve those series from a verifiable public endpoint. Rather than
reconstruct the history from memory or secondary reporting, the table is withheld until the official series is
confirmed. The two figures above — current pack price and WHO tax share — are the parts that are sourced.</p></div>

<h2>Where to see the Korean numbers in context</h2>
<p>Three places on this site are relevant. The <a href="cost-of-smoking-south-korea.html" data-keep>South Korea
page</a> carries the price, the recorded regulatory indicators and the national quitline. The
<a href="prices.html" data-keep>price table</a> puts Korea next to 30 other countries, which is the fastest way
to see that the same habit costs several times more or less depending only on location. And the
<a href="index.html" data-keep>calculator</a> uses what you actually pay rather than the national average,
which is usually the version of the number that changes behaviour.</p>

<h2>Checklist: reading any pack-price claim</h2>
<ul>
<li>Is the price a current retail price, and for how many cigarettes?</li>
<li>Is the tax figure a share of the retail price or an amount per pack?</li>
<li>What is the reference year, and has there been a scheduled increase since?</li>
<li>Is the currency converted, and at what rate and date?</li>
<li>Does the source publish the series, or is it a single quoted number?</li>
</ul>

<h2>The background WHO publishes alongside the tax argument</h2>
<p>WHO's tobacco fact sheet records that tobacco kills more than 7 million people each year, including over 1.6
million non-smokers exposed to second-hand smoke, and states that there is no safe level of exposure to
second-hand tobacco smoke. Price policy exists in that context: the tax share inside a pack is a public health
instrument and a line in a household budget at the same time, which is why both numbers belong on the same
page. Korean smokers can also use the public quit support described by the national quit-smoking information
service, 금연길라잡이, including its one-to-one counselling channel — set out in the
<a href="guide-korea-quit-support.html" data-keep>Korean support guide</a>.</p>
""",
 'body_ko': """
<p>담뱃값은 숫자 하나처럼 보이지만 실제로는 세 가지입니다. 제품, 세금, 유통. 이 페이지는 출처를 댈 수 있는
부분만 싣습니다. 한국의 경우 이 사이트가 쓰는 한 갑 가격과, WHO 국가 지표에 기록된 세금 비중입니다. 공표된
수치가 없는 항목은 추정하지 않고 비워 둡니다.</p>

<h2>기록된 한국의 한 갑</h2>
{{KR_TABLE}}

<p>세금 비중은 WHO 글로벌 보건 관측소(GHO)의 담배 규제 지표 시리즈에서 왔고, 기준연도를 표에 함께
표시했습니다. 한 갑 가격은 이 사이트 전체에서 쓰는 값으로,
<a href="cost-of-smoking-south-korea.html" data-keep>대한민국 페이지</a>와
<a href="prices.html" data-keep>31개국 표</a>에 쓰는 것과 같습니다. 개비당 금액과 연간 금액은 이 두 입력값에
대한 산수이며 조사 결과가 아닙니다.</p>

<h2>세금 비중이 흥미로운 줄인 이유</h2>
<p>담배 과세에 대한 WHO의 입장에는 애매한 표현이 없습니다 — 담배 소비세와 가격을 크게 올리는 것이 담배 사용을
줄이는 가장 효과적이고 비용 효율적인 단일 조치라는 근거가 있으며, 담배 제품에 세금을 올려 가격이 오르면 담배의
구매 부담이 커진다는 것입니다. 흡연자가 '내 가계 문제'로 체감하는 모든 가격 인상의 작동 원리가 여기 있습니다.
가계 문제가 되도록 설계된 것입니다.</p>

<p>그래서 눈에 보이는 가격보다 세금 비중이 지켜볼 숫자입니다. 어떤 나라는 소득이 높아서 가격이 높고, 어떤
나라는 과세가 강해서 높습니다. 비중은 그 둘을 구분해 줍니다. WHO가 비중을 공표한 모든 나라의 값은
<a href="guide-cigarette-tax-share.html" data-keep>나라별 세금 비중 가이드</a>에 표로 있습니다.</p>

<h2>가격 인상이 하루 습관에 하는 일</h2>
<div class="tw"><table><thead><tr><th>한 갑 가격이 오르면</th><th>하루 한 갑 1년치 추가 부담</th></tr></thead><tbody>
<tr><td>5%</td><td>위 표 연간 금액의 5%</td></tr>
<tr><td>10%</td><td>연간 금액의 10%</td></tr>
<tr><td>20%</td><td>연간 금액의 20%</td></tr>
</tbody></table></div>
<p>중요한 줄은 이미 내고 있는 줄입니다. 하루 한 갑의 연간 비용은 단순 곱셈이기 때문에, 가격 인상 1%p는 이미
큰 연간 금액의 1%p이기도 합니다. WHO가 가격을 정부가 쓸 수 있는 가장 강한 수단으로 보는 이유가 바로
이것입니다.</p>

<h2>이 페이지가 주장하지 않는 것</h2>
<div class="box"><p>여기에는 연도별 한국 담뱃값 인상 연혁 표를 싣지 않았습니다. 연도별 가격·세제 변화 표를
만들려면 한국 조세·보건 당국의 공식 연도 시계열 자료가 필요하고, 이 페이지 상단에 표시된 확인일 기준으로 그
시계열을 검증 가능한 공개 경로에서 받지 못했습니다. 기억이나 2차 보도로 연혁을 복원하는 대신, 공식 시계열이
확인될 때까지 표를 보류합니다. 위의 두 수치(현재 한 갑 가격, WHO 세금 비중)가 출처가 있는 부분입니다.</p></div>

<h2>한국 숫자를 맥락 속에서 보는 곳</h2>
<p>이 사이트에서 관련된 곳은 세 군데입니다. <a href="cost-of-smoking-south-korea.html" data-keep>대한민국
페이지</a>에는 가격, 기록된 규제 지표, 국가 금연상담전화가 있습니다.
<a href="prices.html" data-keep>담뱃값 표</a>는 한국을 다른 30개국 옆에 놓습니다. 같은 습관의 비용이 위치만으로
몇 배씩 달라진다는 것을 가장 빠르게 보는 방법입니다. 그리고 <a href="index.html" data-keep>계산기</a>는 국가
평균이 아니라 실제로 내는 금액을 씁니다. 보통 행동을 바꾸는 쪽은 그 숫자입니다.</p>

<h2>점검표: 담뱃값 주장을 읽을 때</h2>
<ul>
<li>그 가격이 현재 소매가인가, 그리고 몇 개비 기준인가</li>
<li>세금 수치가 소매가 대비 비중인가, 갑당 금액인가</li>
<li>기준연도는 언제이며, 그 뒤 예정된 인상이 있었는가</li>
<li>환율로 환산한 값인가, 어떤 환율과 어느 날짜 기준인가</li>
<li>출처가 시계열을 공표하는가, 아니면 인용된 단일 숫자인가</li>
</ul>

<h2>WHO가 과세 논리와 함께 공표하는 배경</h2>
<p>WHO 담배 팩트시트는 담배가 매년 700만 명 이상을 사망에 이르게 하며 그중 간접흡연에 노출된 비흡연자가 160만
명을 넘는다고 기록하고, 간접흡연에는 안전한 노출 수준이 없다고 명시합니다. 가격 정책은 그 맥락에 있습니다.
한 갑 안의 세금 비중은 공중보건 수단이면서 동시에 가계부의 한 줄입니다. 두 숫자가 같은 페이지에 있어야 하는
이유입니다. 한국의 흡연자는 국가 금연정보 서비스 금연길라잡이가 안내하는 공공 금연지원(1:1 상담 채널 포함)도
쓸 수 있습니다. <a href="guide-korea-quit-support.html" data-keep>한국 금연지원 가이드</a>에 정리해
두었습니다.</p>
""",
 'faq_en': [
  ('How much of a Korean pack price is tax?',
   'The WHO Global Health Observatory tobacco indicator series records a tax share for South Korea; the exact figure and its reference year are shown in the table on this page, alongside the pack price used across this site.'),
  ('Why do governments keep raising tobacco prices?',
   'WHO states that significantly increasing tobacco excise taxes and prices is the single most effective and cost-effective measure for reducing tobacco use, because higher prices make tobacco less affordable.'),
  ('Where is the year-by-year Korean price history?',
   'It is deliberately not published here. Building that table requires official year-series data from Korean tax and health authorities, and that series was not retrievable from a verifiable public endpoint on the confirmation date shown at the top of this page.')],
 'faq_ko': [
  ('한국 담뱃값에서 세금은 얼마인가요?',
   'WHO 글로벌 보건 관측소의 담배 지표 시리즈에 대한민국의 세금 비중이 기록돼 있습니다. 정확한 수치와 기준연도는 이 페이지 표에 한 갑 가격과 함께 표시했습니다.'),
  ('정부는 왜 계속 담뱃값을 올리나요?',
   'WHO는 담배 소비세와 가격을 크게 올리는 것이 담배 사용을 줄이는 가장 효과적이고 비용 효율적인 단일 조치이며, 가격이 오르면 담배의 구매 부담이 커진다고 기술합니다.'),
  ('연도별 담뱃값 인상 연혁 표는 왜 없나요?',
   '의도적으로 싣지 않았습니다. 그 표를 만들려면 한국 조세·보건 당국의 공식 연도 시계열이 필요하고, 이 페이지 상단의 확인일 기준으로 검증 가능한 공개 경로에서 받지 못했습니다. 확인되면 추가합니다.')],
},
]
