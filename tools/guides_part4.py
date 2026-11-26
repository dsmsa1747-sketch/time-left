# -*- coding: utf-8 -*-
"""가이드 10~12. 표는 데이터에서 찍는다({{TAX_TABLE}}), 인용은 실측 출처만."""

GUIDES = [

# ─────────────────────────────── 10
{
 'slug': 'guide-cigarette-tax-share',
 'cat': 'money',
 'title_en': 'How much of a pack price is tax? Country by country, from WHO indicators',
 'desc_en': 'The recorded tax share of the pack price for every country where WHO publishes one, why the share matters more than the headline price, and how to read it.',
 'h1_en': 'How much of a pack price is tax?',
 'h1_ko': '담뱃값에서 세금은 얼마인가 — 나라별 비교',
 'sub_en': 'The recorded share for every country where WHO publishes one, next to the pack price we use.',
 'sub_ko': 'WHO가 공표한 나라의 세금 비중과, 이 사이트가 쓰는 한 갑 가격을 나란히.',
 'srcs': ['who_tax', 'who_tobacco', 'eu_tobacco'],
 'rel': [('prices.html', 'Prices in 31 countries', '31개국 담뱃값 비교'),
         ('guide-korea-cigarette-price-history.html', 'What is inside a Korean pack price', '한국 담뱃값에 들어 있는 것'),
         ('cost-of-smoking-united-kingdom.html', 'Smoking in the United Kingdom', '영국 — 담뱃값·규제·금연지원'),
         ('guide-using-quitminutes.html', 'How to read this calculator', '이 계산기를 제대로 쓰는 법')],
 'body_en': """
<p>Two packs can cost the same and mean completely different things. In one country most of the price is the
product; in another most of it is tax. The share is the part that reflects a decision somebody made, which is
why it is the more interesting number — and why WHO publishes it.</p>

<h2>Why the share is the policy number</h2>
<p>WHO's position is unhedged: evidence shows that significantly increasing tobacco excise taxes and prices is
the single most effective and cost-effective measure for reducing tobacco use, and raising taxes on tobacco
products which lead to increases in their price makes tobacco less affordable. A price rise that a smoker
experiences as a household budget problem is the mechanism working as designed.</p>

<p>The headline price alone cannot tell you whether a government is using that lever. A wealthy country can
have an expensive pack with a modest tax share; a middle-income country can have a cheaper pack where tax is
most of the price. The share separates policy from income levels.</p>

<h2>Recorded tax share, highest first</h2>
{{TAX_TABLE}}

<p>Source and limits: the tax share is from the WHO Global Health Observatory tobacco indicator series, with
the reference year in the last column; the pack price and USD figure are the values this site uses throughout,
including on each <a href="prices.html" data-keep>country page</a>. Countries are omitted when WHO publishes
no share for them — an empty row would imply a measurement that does not exist. Because the reference years
differ, read the table as a comparison of recorded policy rather than a same-day snapshot.</p>

<h2>How to read a tax share without over-reading it</h2>
<ul>
<li><strong>A share is not an amount.</strong> 70% of a cheap pack is less money than 50% of an expensive one.</li>
<li><strong>Shares move when prices move.</strong> If the product price rises and the tax does not, the share falls without any policy change.</li>
<li><strong>Reference years differ.</strong> Compare the share alongside the year, not in isolation.</li>
<li><strong>Currency conversion adds noise.</strong> The local price is the primary figure; the USD column is for comparison only.</li>
<li><strong>Taxes are not the only control.</strong> Smoke-free places, advertising bans, pack warnings and plain packaging are recorded separately, and appear on each country page.</li>
</ul>

<h2>What else sits around the tax line</h2>
<p>Price policy is one instrument among several. The European Commission describes EU-wide rules as necessary
given significant cross-border trade and the risk of diverging national legislation, and records that the
Tobacco Products Directive has governed the manufacture, display and sale of tobacco and related products
since May 2016. So a national tax share sits inside a regional regulatory frame as well as a national one,
which is part of why neighbouring countries often cluster in the table above.</p>

<h2>The health context WHO publishes alongside</h2>
<p>WHO's tobacco fact sheet records that tobacco kills more than 7 million people each year, including over 1.6
million non-smokers exposed to second-hand smoke, and states that there is no safe level of exposure to
second-hand tobacco smoke. That is the reason a tax line exists at all: the share inside a pack is
simultaneously a public health instrument and a line in a household budget.</p>

<h2>Turning the share into your own number</h2>
<p>A tax share is abstract until it is multiplied by a habit. Take the pack price for your country from the
table, multiply by how many packs you actually buy in a year, and apply the share: that product is roughly what
you contribute in tobacco tax annually. The <a href="index.html" data-keep>calculator</a> does the first half
of that arithmetic with your real price rather than the national average, and the
<a href="guide-korea-cigarette-price-history.html" data-keep>Korean breakdown</a> works through one country in
detail.</p>

<h2>Checklist for quoting any tax-share figure</h2>
<ul>
<li>Is it a share of the retail price, or an amount per pack?</li>
<li>Which year is it from, and has a scheduled increase happened since?</li>
<li>Does it cover all tobacco taxes, or only excise?</li>
<li>Is the pack size the same across the countries being compared?</li>
<li>Does the source publish the series, so the number can be re-checked later?</li>
</ul>
""",
 'body_ko': """
<p>같은 가격의 두 담배가 전혀 다른 것을 의미할 수 있습니다. 어떤 나라에서는 가격의 대부분이 제품이고, 다른
나라에서는 대부분이 세금입니다. 비중은 누군가의 결정이 반영된 부분입니다. 그래서 더 흥미로운 숫자이고, WHO가
그것을 공표하는 이유입니다.</p>

<h2>비중이 '정책 숫자'인 이유</h2>
<p>WHO의 입장에는 유보가 없습니다 — 담배 소비세와 가격을 크게 올리는 것이 담배 사용을 줄이는 가장 효과적이고
비용 효율적인 단일 조치라는 근거가 있으며, 담배 제품에 세금을 올려 가격이 오르면 담배의 구매 부담이 커진다는
것입니다. 흡연자가 가계 문제로 체감하는 가격 인상은 그 장치가 설계대로 작동하는 모습입니다.</p>

<p>겉으로 보이는 가격만으로는 그 나라 정부가 이 수단을 쓰고 있는지 알 수 없습니다. 소득이 높은 나라는 비싼 한
갑에 세금 비중이 낮을 수 있고, 중소득 국가는 더 싼 한 갑에서 세금이 가격의 대부분일 수 있습니다. 비중은 정책과
소득 수준을 분리해 줍니다.</p>

<h2>기록된 세금 비중 — 높은 순</h2>
{{TAX_TABLE}}

<p>출처와 한계: 세금 비중은 WHO 글로벌 보건 관측소의 담배 지표 시리즈이며 기준연도를 마지막 열에 적었습니다.
한 갑 가격과 USD 값은 이 사이트가 전체에서 쓰는 값으로, 각 <a href="prices.html" data-keep>국가 페이지</a>와
동일합니다. WHO가 비중을 공표하지 않은 나라는 표에서 빠집니다. 빈 칸은 존재하지 않는 측정값이 있는 것처럼
보이게 만들기 때문입니다. 기준연도가 서로 다르므로, 이 표는 같은 날의 스냅샷이 아니라 기록된 정책의 비교로
읽으십시오.</p>

<h2>과하게 읽지 않는 방법</h2>
<ul>
<li><strong>비중은 금액이 아니다.</strong> 싼 담배의 70%는 비싼 담배의 50%보다 적은 돈입니다.</li>
<li><strong>가격이 움직이면 비중도 움직인다.</strong> 제품 가격이 오르고 세금이 그대로면, 정책 변화 없이 비중이 내려갑니다.</li>
<li><strong>기준연도가 다르다.</strong> 비중은 연도와 함께 보십시오.</li>
<li><strong>환율 환산은 잡음을 더한다.</strong> 현지 가격이 기본값이고 USD 열은 비교용입니다.</li>
<li><strong>세금만이 규제는 아니다.</strong> 금연구역, 광고 금지, 경고그림, 평민포장은 별도 지표로 기록되며 각 국가 페이지에 있습니다.</li>
</ul>

<h2>세금 줄 주변에 있는 것들</h2>
<p>가격 정책은 여러 수단 중 하나입니다. 유럽연합 집행위원회는 국경을 넘는 상당한 교역과 국가별 법제 이탈 위험을
감안하면 EU 차원의 규칙이 필요하다고 설명하고, 담배제품지침(TPD)이 2016년 5월부터 담배 및 관련 제품의 제조·진열·
판매를 규율해 왔다고 기록합니다. 즉 한 나라의 세금 비중은 국가 틀 안에만 있는 것이 아니라 지역 규제 틀 안에도
있습니다. 위 표에서 인접 국가들이 자주 묶여 나타나는 이유의 일부입니다.</p>

<h2>WHO가 함께 공표하는 보건 맥락</h2>
<p>WHO 담배 팩트시트는 담배가 매년 700만 명 이상을 사망에 이르게 하며 그중 간접흡연에 노출된 비흡연자가 160만
명을 넘는다고 기록하고, 간접흡연에는 안전한 노출 수준이 없다고 명시합니다. 애초에 세금 줄이 존재하는 이유가
여기 있습니다. 한 갑 안의 비중은 공중보건 수단이면서 동시에 가계부의 한 줄입니다.</p>

<h2>비중을 내 숫자로 바꾸기</h2>
<p>세금 비중은 습관에 곱해지기 전까지 추상적입니다. 표에서 내 나라의 한 갑 가격을 가져와 1년에 실제로 사는 갑
수를 곱하고, 비중을 적용하십시오. 그 값이 대략 내가 1년에 내는 담배 세금입니다.
<a href="index.html" data-keep>계산기</a>는 국가 평균이 아니라 실제 지불 가격으로 그 계산의 앞 절반을 해 주고,
<a href="guide-korea-cigarette-price-history.html" data-keep>한국 분해</a>는 한 나라를 자세히 다룹니다.</p>

<h2>세금 비중 수치를 인용할 때 점검표</h2>
<ul>
<li>소매가 대비 비중인가, 갑당 금액인가</li>
<li>어느 해 기준이며, 그 뒤 예정된 인상이 있었는가</li>
<li>모든 담배 관련 세금을 포함하는가, 소비세만인가</li>
<li>비교 대상 국가들의 한 갑 개비 수가 같은가</li>
<li>출처가 시계열을 공표해 나중에 다시 확인할 수 있는가</li>
</ul>
""",
 'faq_en': [
  ('Which country taxes cigarettes most heavily?',
   'The table on this page lists the recorded tax share of the pack price, highest first, for every country where the WHO Global Health Observatory publishes one, with the reference year shown for each.'),
  ('Does a high tax share mean cigarettes are expensive there?',
   'Not necessarily. A share is not an amount: 70% of a cheap pack can be less money than 50% of an expensive one. Read the share next to the pack price, both of which are in the table.'),
  ('Why do governments raise tobacco taxes?',
   'WHO states that significantly increasing tobacco excise taxes and prices is the single most effective and cost-effective measure for reducing tobacco use, because higher prices make tobacco less affordable.')],
 'faq_ko': [
  ('어느 나라가 담배에 세금을 가장 많이 매기나요?',
   '이 페이지 표에 WHO 글로벌 보건 관측소가 비중을 공표한 모든 나라의 기록값이 높은 순으로 있고, 각 수치의 기준연도도 함께 표시했습니다.'),
  ('세금 비중이 높으면 그 나라 담배가 비싼 건가요?',
   '반드시 그렇지 않습니다. 비중은 금액이 아닙니다. 싼 담배의 70%가 비싼 담배의 50%보다 적은 돈일 수 있습니다. 비중은 표에 함께 있는 한 갑 가격과 같이 보십시오.'),
  ('정부는 왜 담배세를 올리나요?',
   'WHO는 담배 소비세와 가격을 크게 올리는 것이 담배 사용을 줄이는 가장 효과적이고 비용 효율적인 단일 조치이며, 가격이 오르면 구매 부담이 커진다고 기술합니다.')],
},

# ─────────────────────────────── 11
{
 'slug': 'guide-pregnancy-quit',
 'cat': 'help',
 'title_en': 'Smoking in pregnancy: what NHS publishes about the risks and the support',
 'desc_en': 'What NHS states about smoking during pregnancy, the benefits of stopping, what CDC says about e-cigarettes in pregnancy, and how to get support rather than advice from a web page.',
 'h1_en': 'Smoking, pregnancy and getting support',
 'h1_ko': '임신 중 금연 — 공식 기관이 공표한 위험과 지원',
 'sub_en': 'What the official pages state, and why this is a conversation with a midwife rather than a website.',
 'sub_ko': '공식 페이지에 적힌 내용, 그리고 왜 이것이 웹사이트가 아니라 의료진과의 대화인지.',
 'srcs': ['nhs_pregnancy', 'cdc_ecig', 'who_cessation_qa'],
 'rel': [('guide-nicotine-replacement.html', 'Compare nicotine replacement products', '니코틴 대체요법 비교'),
         ('guide-vaping-heated-tobacco.html', 'Vapes versus cigarettes', '전자담배 vs 일반담배'),
         ('guide-korea-quit-support.html', 'Free help in South Korea', '한국의 무료 금연지원'),
         ('quitlines.html', 'Free quitlines by country', '나라별 무료 금연상담전화')],
 'body_en': """
<p>This is the one guide on this site that is mostly a referral. Pregnancy changes which products are
appropriate, which medicines are safe and how quickly support should be arranged, and none of those are
questions a calculator can answer. What follows is what the official pages state, and where to take it.</p>

<div class="box warn"><p>Speak to your midwife, doctor or national stop-smoking service rather than planning
from this page. NHS states that stopping smoking will help both you and your baby immediately, and support in
pregnancy is a standard part of antenatal care in many countries.</p></div>

<h2>What NHS states about the risk</h2>
<p>The NHS page on stopping smoking in pregnancy states that every cigarette you smoke contains over 4,000
chemicals, many of which are dangerous, so smoking when you are pregnant harms your unborn baby, and that
cigarettes can restrict the essential oxygen supply to your baby. On the effects after birth, NHS notes that
babies are more likely to have problems keeping warm and are more likely to get infections, and that stopping
smoking reduces the risk of sudden infant death syndrome, also known as cot death.</p>

<h2>What NHS states about stopping</h2>
<p>The same page states that stopping smoking will help both you and your baby immediately, and that stopping
now will also help your baby later in life. Two features of that wording are worth noticing: the benefit is
described as immediate rather than deferred, and it is described for both people rather than framed as a
sacrifice by one of them.</p>

<div class="tw"><table><thead><tr><th>Question</th><th>What the official pages state</th></tr></thead><tbody>
<tr><td>Does smoking in pregnancy harm the baby?</td><td>NHS: smoking when you are pregnant harms your unborn baby; cigarettes can restrict the essential oxygen supply to your baby</td></tr>
<tr><td>Is there a benefit to stopping now?</td><td>NHS: stopping smoking will help both you and your baby immediately, and will also help your baby later in life</td></tr>
<tr><td>Does it reduce cot death risk?</td><td>NHS: stopping reduces the risk of sudden infant death syndrome, also known as cot death</td></tr>
<tr><td>Can I use e-cigarettes instead?</td><td>CDC: e-cigarettes should not be used by youth, young adults, or women who are pregnant</td></tr>
<tr><td>What about second-hand smoke around a child?</td><td>WHO: quitting decreases the excess risk of many diseases related to second-hand smoke in children, such as respiratory diseases including asthma, and ear infections</td></tr>
</tbody></table></div>

<h2>Why the household matters, not only the pregnancy</h2>
<p>WHO records that quitting smoking decreases the excess risk of many diseases related to second-hand smoke in
children, such as respiratory diseases including asthma and ear infections, and its tobacco fact sheet states
that there is no safe level of exposure to second-hand tobacco smoke. So the relevant unit is the home rather
than one person: a partner who keeps smoking indoors is part of the exposure, which is why services often
support both people together.</p>

<h2>Products and medicines: ask first</h2>
<p>Nicotine replacement products are not automatically appropriate in pregnancy, and prescription medicines
even less so. NHS guidance in general describes nicotine-free medicines as available from a stop-smoking
service or a GP, which is the correct route here too: the decision about whether to use any product, and at
what dose, belongs to a clinician who knows the pregnancy. Use the
<a href="guide-nicotine-replacement.html" data-keep>product comparison</a> to understand the categories before
that conversation, not to choose one in advance. On vapes specifically, CDC's statement is direct: they should
not be used by women who are pregnant — see the
<a href="guide-vaping-heated-tobacco.html" data-keep>vaping guide</a> for the three official positions side by
side.</p>

<h2>Practical steps that do not need a prescription</h2>
<ul>
<li>Tell your midwife or doctor at the next appointment, even if you have not stopped yet.</li>
<li>Ask what the stop-smoking service covers in your country, and whether a partner can join.</li>
<li>Make the home and the car smoke-free for everyone, not only for you.</li>
<li>Use the free counselling line for the hard evenings rather than waiting for the next appointment.</li>
<li>Write the plan for the two situations that have broken previous attempts — see <a href="guide-alcohol-cravings.html" data-keep>drinks and gatherings</a>.</li>
</ul>

<h2>What this page deliberately does not do</h2>
<p>It does not give doses, it does not list medicines as safe or unsafe in pregnancy, and it does not quantify
risk. Those are clinical judgments, and the standing rule on this site is that an unverified number is worse
than no number. What is sourced here is the NHS statement of harm and immediate benefit, the CDC position on
e-cigarettes in pregnancy, and the WHO record on second-hand smoke in children. For free national lines, see
the <a href="quitlines.html" data-keep>quitlines page</a>.</p>
""",
 'body_ko': """
<p>이 사이트에서 이 글은 대부분이 '연결'입니다. 임신은 어떤 제품이 적절한지, 어떤 약이 안전한지, 지원을 얼마나
빨리 받아야 하는지를 바꾸고, 그중 어느 것도 계산기가 답할 수 있는 질문이 아닙니다. 아래는 공식 페이지에 적힌
내용과, 그것을 어디로 가져가야 하는지입니다.</p>

<div class="box warn"><p>이 페이지로 계획을 세우지 말고 조산사·의사 또는 국가 금연지원 서비스와 상의하십시오.
NHS는 금연이 산모와 아기 모두에게 즉시 도움이 된다고 기술하며, 많은 나라에서 임신 중 금연 지원은 산전 관리의
표준적인 일부입니다.</p></div>

<h2>NHS가 기술한 위험</h2>
<p>NHS의 임신 중 금연 페이지는, 담배 한 개비에는 4,000가지가 넘는 화학물질이 들어 있고 그중 많은 것이 위험하므로
임신 중 흡연은 태아에게 해를 끼치며, 담배가 아기에게 가는 필수적인 산소 공급을 제한할 수 있다고 기술합니다.
출생 후 영향으로는 아기가 체온을 유지하는 데 문제가 생길 가능성이 높고 감염에 더 잘 걸릴 수 있다고 적고 있으며,
금연이 영아돌연사증후군(일명 cot death) 위험을 낮춘다고 기술합니다.</p>

<h2>NHS가 기술한 금연의 효과</h2>
<p>같은 페이지는 금연이 산모와 아기 모두에게 즉시 도움이 되며, 지금 끊는 것이 나중에 아기에게도 도움이 된다고
기술합니다. 이 표현에서 두 가지를 볼 만합니다. 효과가 미래로 유보되지 않고 '즉시'로 기술돼 있다는 점, 그리고 한
쪽의 희생이 아니라 두 사람 모두의 이득으로 기술돼 있다는 점입니다.</p>

<div class="tw"><table><thead><tr><th>질문</th><th>공식 페이지에 적힌 내용</th></tr></thead><tbody>
<tr><td>임신 중 흡연이 아기에게 해로운가</td><td>NHS: 임신 중 흡연은 태아에게 해를 끼치며, 담배가 아기에게 가는 필수 산소 공급을 제한할 수 있다</td></tr>
<tr><td>지금 끊으면 이득이 있는가</td><td>NHS: 금연은 산모와 아기 모두에게 즉시 도움이 되며, 나중에 아기에게도 도움이 된다</td></tr>
<tr><td>영아돌연사 위험이 줄어드는가</td><td>NHS: 금연은 영아돌연사증후군(cot death) 위험을 낮춘다</td></tr>
<tr><td>대신 전자담배를 써도 되는가</td><td>CDC: 전자담배는 청소년·청년·임신한 여성이 사용해서는 안 된다</td></tr>
<tr><td>아이 주변 간접흡연은 어떤가</td><td>WHO: 금연은 아동에서 간접흡연 관련 질환(천식 등 호흡기 질환, 중이염)의 초과 위험을 낮춘다</td></tr>
</tbody></table></div>

<h2>임신만이 아니라 '집'이 단위인 이유</h2>
<p>WHO는 금연이 아동에서 간접흡연과 관련된 여러 질환 — 천식을 포함한 호흡기 질환, 중이염 — 의 초과 위험을
낮춘다고 기록하고, 담배 팩트시트에서 간접흡연에는 안전한 노출 수준이 없다고 명시합니다. 그래서 관련된 단위는 한
사람이 아니라 집입니다. 실내에서 계속 피우는 배우자는 노출의 일부이고, 그래서 서비스들이 두 사람을 함께 지원하는
경우가 많습니다.</p>

<h2>제품과 약은 먼저 물어보기</h2>
<p>니코틴 대체 제품이 임신 중에 자동으로 적절한 것은 아니며, 처방약은 더욱 그렇습니다. NHS는 일반적으로 니코틴
없는 약을 금연 서비스나 일반의를 통해 받을 수 있다고 안내하는데, 여기서도 그 경로가 맞습니다. 어떤 제품을 쓸지,
어느 용량으로 쓸지는 그 임신을 아는 의료진의 판단입니다. <a href="guide-nicotine-replacement.html" data-keep>제품
비교</a>는 그 대화 전에 범주를 이해하는 데 쓰고, 미리 하나를 고르는 데 쓰지 마십시오. 베이프에 대해서는 CDC의
진술이 직접적입니다 — 임신한 여성은 사용해서는 안 된다. 세 기관의 입장을 나란히 본 것은
<a href="guide-vaping-heated-tobacco.html" data-keep>전자담배 가이드</a>에 있습니다.</p>

<h2>처방 없이 할 수 있는 실무적 조치</h2>
<ul>
<li>아직 끊지 못했더라도 다음 진료 때 조산사·의사에게 말한다</li>
<li>내 나라의 금연 서비스가 무엇을 지원하는지, 배우자도 함께 받을 수 있는지 묻는다</li>
<li>나만이 아니라 모두를 위해 집과 차를 금연 구역으로 만든다</li>
<li>힘든 저녁은 다음 진료를 기다리지 말고 무료 상담전화를 쓴다</li>
<li>지난 시도를 무너뜨린 두 상황에 대한 계획을 쓴다 — <a href="guide-alcohol-cravings.html" data-keep>술자리·모임</a></li>
</ul>

<h2>이 페이지가 일부러 하지 않는 것</h2>
<p>용량을 알려주지 않고, 임신 중 안전한 약·위험한 약을 목록으로 만들지 않고, 위험을 수치화하지 않습니다. 임상적
판단이고, 이 사이트의 상시 규칙은 확인되지 않은 숫자가 숫자 없는 것보다 나쁘다는 것입니다. 여기서 출처가 있는
것은 NHS의 위험·즉시 효과 진술, 임신 중 전자담배에 대한 CDC 입장, 아동 간접흡연에 대한 WHO 기록입니다. 나라별
무료 상담전화는 <a href="quitlines.html" data-keep>금연상담전화 페이지</a>에 있습니다.</p>
""",
 'faq_en': [
  ('What does NHS say about smoking during pregnancy?',
   'NHS states that every cigarette contains over 4,000 chemicals, many of them dangerous, so smoking when you are pregnant harms your unborn baby, and that cigarettes can restrict the essential oxygen supply to your baby.'),
  ('Is there any benefit to stopping late in pregnancy?',
   'NHS states that stopping smoking will help both you and your baby immediately, and that stopping now will also help your baby later in life. It also states that stopping reduces the risk of sudden infant death syndrome.'),
  ('Can I switch to e-cigarettes while pregnant?',
   'CDC states that e-cigarettes should not be used by youth, young adults, or women who are pregnant. Any product decision in pregnancy belongs to your midwife or doctor rather than to a web page.')],
 'faq_ko': [
  ('임신 중 흡연에 대해 NHS는 무엇을 말하나요?',
   'NHS는 담배 한 개비에 4,000가지가 넘는 화학물질이 들어 있고 그중 많은 것이 위험하므로 임신 중 흡연이 태아에게 해를 끼치며, 담배가 아기에게 가는 필수 산소 공급을 제한할 수 있다고 기술합니다.'),
  ('임신 후반에 끊어도 의미가 있나요?',
   'NHS는 금연이 산모와 아기 모두에게 즉시 도움이 되며 지금 끊는 것이 나중에 아기에게도 도움이 된다고 기술합니다. 또 금연이 영아돌연사증후군 위험을 낮춘다고 적고 있습니다.'),
  ('임신 중 전자담배로 바꿔도 되나요?',
   'CDC는 전자담배를 청소년·청년·임신한 여성이 사용해서는 안 된다고 기술합니다. 임신 중 제품 선택은 웹페이지가 아니라 조산사·의사의 판단입니다.')],
},

# ─────────────────────────────── 12
{
 'slug': 'guide-using-quitminutes',
 'cat': 'tool',
 'title_en': 'How to read this calculator: inputs, arithmetic, and what it cannot tell you',
 'desc_en': 'What the calculator asks for, how money and minutes are derived, where the country data comes from, what is not collected, and the limits of a population average.',
 'h1_en': 'How to read this calculator',
 'h1_ko': '이 계산기를 제대로 쓰는 법 — 숫자의 의미와 한계',
 'sub_en': 'Inputs, arithmetic, data sources, and the limits we will not paper over.',
 'sub_ko': '입력값, 계산 방식, 데이터 출처, 그리고 감추지 않을 한계.',
 'srcs': ['who_cessation_qa', 'who_tobacco', 'ucl_research'],
 'rel': [('guide-20-minutes-per-cigarette.html', 'Where the 20-minute figure comes from', '"20분" 숫자의 정체'),
         ('prices.html', 'Prices in 31 countries', '31개국 담뱃값 비교'),
         ('timeline.html', 'The recovery timeline', '회복 타임라인'),
         ('guide-cigarette-tax-share.html', 'Tax share of the pack price', '담뱃값 세금 비중')],
 'body_en': """
<p>A number is only useful if you know how it was made. This page documents what the calculator asks for, what
it does with it, where the country data comes from, and the four things it cannot tell you.</p>

<h2>What it asks for, and why</h2>
<div class="tw"><table><thead><tr><th>Input</th><th>Why it is needed</th><th>If you are unsure</th></tr></thead><tbody>
<tr><td>What you actually pay per pack</td><td>National averages are often wrong for an individual; your price is the one that matters</td><td>Use the price from the last pack you bought, not the table</td></tr>
<tr><td>Cigarettes per day</td><td>Drives both the money and the minutes</td><td>Use a normal week rather than your best week</td></tr>
<tr><td>When you started</td><td>Turns a daily figure into a cumulative one</td><td>An approximate year is enough; the arithmetic is linear</td></tr>
</tbody></table></div>

<h2>The arithmetic, in one paragraph</h2>
<p>Money is your pack price multiplied by the packs implied by your daily count, extended over whatever period
is being shown. Time is your cigarette count multiplied by an average minutes-per-cigarette estimate; because
such estimates are published separately for men and women, the site keeps two values and labels which one it
is using. Where a figure is derived rather than measured — per-cigarette cost, cost per year, minutes per pack
— it is arithmetic on your inputs, not a survey result. The derivation and its limits are set out in
<a href="guide-20-minutes-per-cigarette.html" data-keep>where the 20-minute figure comes from</a>.</p>

<h2>Where the country data comes from</h2>
<ul>
<li><strong>Pack prices</strong> for 31 countries, used on the <a href="prices.html" data-keep>price table</a> and each country page.</li>
<li><strong>Quitline numbers</strong> for the countries we have them for, on the <a href="quitlines.html" data-keep>quitlines page</a>.</li>
<li><strong>Regulatory indicators and tax share</strong> from the WHO Global Health Observatory tobacco indicator series, shown with the reference year on each country page and in the <a href="guide-cigarette-tax-share.html" data-keep>tax share guide</a>.</li>
<li><strong>Recovery timeline</strong> entries that follow the schedule WHO publishes: heart rate and blood pressure drop within 20 minutes, blood carbon monoxide falls to normal by 12 hours, circulation and lung function improve across 2 to 12 weeks, coughing and shortness of breath decrease over 1 to 9 months.</li>
</ul>

<h2>What is not collected</h2>
<p>The calculator runs in your browser. Your price, your count and your start date stay on your device; nothing
is uploaded, and there is no account to create. That is also why the figures do not follow you between devices
— the trade-off is deliberate. The site can be installed for offline use, in which case the calculator keeps
working without a connection.</p>

<h2>Four things it cannot tell you</h2>
<ul>
<li><strong>How long you will live.</strong> Minute figures are population averages, not individual predictions.</li>
<li><strong>What one cigarette did.</strong> Harm accumulates over years of exposure; the per-cigarette figure is an accounting convenience.</li>
<li><strong>Your clinical risk.</strong> That depends on history, genetics, other exposures and medical facts the calculator never sees.</li>
<li><strong>Whether you will succeed.</strong> Quit success varies by group and circumstance, and support changes the odds more than resolve does.</li>
</ul>

<div class="box"><p>Time Left is a calculator, not medical advice, and not a prediction. For personal medical
questions speak to a clinician. For the hard evenings, a free national quitline exists and is listed on this
site.</p></div>

<h2>The part of the output worth watching</h2>
<p>The cumulative figure is more useful than the daily one, for the same reason an odometer is more useful than
a speedometer when deciding whether to service a car. A daily cost is easy to absorb; ten years of it is the
number that changes decisions. WHO's framing of the benefit is also cumulative and age-indexed: compared with
people who continued smoking, quitting at about 30 gains almost 10 years of life expectancy, at about 40 gains
9 years, at about 50 gains 6 years, and at about 60 gains 3 years.</p>

<h2>How to check we are current</h2>
<ul>
<li>Every page carries a last-updated line and, on guides, a source-confirmation date.</li>
<li>Country pages show the reference year next to WHO indicator values rather than implying they are from today.</li>
<li>If a figure matters to a decision, open the linked source — every guide lists its sources with the date each was confirmed.</li>
<li>Where we could not verify something, the page says so instead of filling the gap. The context for why that matters is in WHO's own numbers: tobacco kills more than 7 million people each year, including over 1.6 million non-smokers exposed to second-hand smoke.</li>
</ul>
""",
 'body_ko': """
<p>숫자는 어떻게 만들어졌는지를 알 때만 쓸모가 있습니다. 이 페이지는 계산기가 무엇을 묻는지, 그것으로 무엇을
하는지, 국가 데이터가 어디서 오는지, 그리고 알려줄 수 없는 네 가지를 적어 둡니다.</p>

<h2>무엇을 묻고, 왜 묻는가</h2>
<div class="tw"><table><thead><tr><th>입력</th><th>왜 필요한가</th><th>모를 때</th></tr></thead><tbody>
<tr><td>실제로 내는 한 갑 가격</td><td>국가 평균은 개인에게 자주 틀립니다. 중요한 건 내 가격입니다</td><td>표가 아니라 마지막으로 산 한 갑의 가격을 쓰십시오</td></tr>
<tr><td>하루 흡연량</td><td>돈과 시간 양쪽을 결정합니다</td><td>가장 잘 참은 주가 아니라 평범한 한 주를 기준으로</td></tr>
<tr><td>시작 시점</td><td>하루 숫자를 누적 숫자로 바꿉니다</td><td>대략의 연도로 충분합니다. 계산은 선형입니다</td></tr>
</tbody></table></div>

<h2>계산 방식, 한 문단</h2>
<p>돈은 한 갑 가격에 하루 흡연량이 함의하는 갑 수를 곱하고, 보여주는 기간만큼 늘린 값입니다. 시간은 흡연 개수에
개비당 평균 분 추정치를 곱한 값입니다. 그런 추정치는 남녀를 나눠 공표되므로, 이 사이트는 두 값을 유지하고 어느
쪽을 쓰는지 표시합니다. 측정이 아니라 도출된 값(개비당 비용, 연간 비용, 한 갑당 분)은 입력값에 대한 산수이며
조사 결과가 아닙니다. 도출 과정과 한계는 <a href="guide-20-minutes-per-cigarette.html" data-keep>"20분" 숫자의
정체</a>에 정리했습니다.</p>

<h2>국가 데이터는 어디서 오는가</h2>
<ul>
<li><strong>한 갑 가격</strong> — 31개국. <a href="prices.html" data-keep>담뱃값 표</a>와 각 국가 페이지에서 씁니다.</li>
<li><strong>금연상담전화 번호</strong> — 확보한 나라에 대해 <a href="quitlines.html" data-keep>상담전화 페이지</a>에 있습니다.</li>
<li><strong>규제 지표와 세금 비중</strong> — WHO 글로벌 보건 관측소의 담배 지표 시리즈. 각 국가 페이지와 <a href="guide-cigarette-tax-share.html" data-keep>세금 비중 가이드</a>에 기준연도와 함께 표시합니다.</li>
<li><strong>회복 타임라인</strong> — WHO가 공표한 일정표를 따릅니다. 20분 안에 심박수와 혈압이 내려가고, 12시간이면 혈중 일산화탄소가 정상 수준으로 떨어지고, 2~12주에 혈액순환과 폐 기능이 향상되고, 1~9개월에 기침과 숨가쁨이 줄어듭니다.</li>
</ul>

<h2>수집하지 않는 것</h2>
<p>계산기는 브라우저 안에서 돕니다. 가격, 흡연량, 시작일은 사용자 기기에 남고 아무것도 업로드되지 않으며 만들
계정도 없습니다. 그래서 기기를 옮기면 숫자가 따라오지 않습니다. 의도한 교환입니다. 오프라인 사용을 위해 설치할
수 있고, 그 경우 연결 없이도 계산기가 작동합니다.</p>

<h2>알려줄 수 없는 네 가지</h2>
<ul>
<li><strong>얼마나 살지.</strong> 분 단위 수치는 인구 평균이며 개인에 대한 예측이 아닙니다.</li>
<li><strong>한 개비가 무엇을 했는지.</strong> 피해는 수년의 노출로 누적됩니다. 개비당 수치는 회계적 편의값입니다.</li>
<li><strong>임상적 위험.</strong> 병력·유전·다른 노출 등 계산기가 전혀 보지 못하는 사실에 달려 있습니다.</li>
<li><strong>성공할지 여부.</strong> 금연 성공률은 집단과 상황에 따라 다르고, 결심보다 지원이 확률을 더 많이 바꿉니다.</li>
</ul>

<div class="box"><p>Time Left는 계산기이며 의학적 조언도, 예측도 아닙니다. 개인의 건강 문제는 의료진과 상의
하십시오. 힘든 저녁에는 무료 국가 금연상담전화가 있고, 이 사이트에 목록이 있습니다.</p></div>

<h2>출력에서 지켜볼 부분</h2>
<p>누적 숫자가 하루 숫자보다 쓸모 있습니다. 차를 정비할지 결정할 때 속도계보다 주행거리계가 쓸모 있는 것과 같은
이유입니다. 하루 비용은 쉽게 흡수되지만, 그것의 10년치가 결정을 바꾸는 숫자입니다. WHO가 이득을 제시하는 방식도
누적이고 연령별입니다. 계속 피운 사람과 비교해 30세 무렵 금연하면 약 10년, 40세 9년, 50세 6년, 60세 3년의
기대수명을 얻습니다.</p>

<h2>최신인지 확인하는 방법</h2>
<ul>
<li>모든 페이지에 최종 업데이트 줄이 있고, 가이드에는 출처 확인일이 있습니다</li>
<li>국가 페이지는 WHO 지표 값 옆에 기준연도를 표시합니다. 오늘 수치인 척하지 않습니다</li>
<li>결정에 영향을 주는 수치라면 링크된 출처를 직접 열어 보십시오. 모든 가이드는 출처와 각 확인일을 함께 적습니다</li>
<li>확인하지 못한 것은 빈칸을 채우지 않고 그렇다고 적습니다. 그것이 중요한 이유는 WHO의 숫자에 있습니다 — 담배는 매년 700만 명 이상을 사망에 이르게 하고, 그중 간접흡연에 노출된 비흡연자가 160만 명을 넘습니다</li>
</ul>
""",
 'faq_en': [
  ('Does the calculator upload my data?',
   'No. It runs in your browser, your inputs stay on your device and there is no account to create. The trade-off is that figures do not follow you between devices.'),
  ('Why does it ask what I pay instead of using the national average?',
   'Because a national average is often wrong for an individual. The price from the last pack you bought produces a number that matches your own spending, which is the version that affects decisions.'),
  ('Can it predict how long I will live?',
   'No. The minute figures are population averages, not individual predictions, and clinical risk depends on history and other factors the calculator never sees. For personal medical questions, speak to a clinician.')],
 'faq_ko': [
  ('계산기가 내 데이터를 업로드하나요?',
   '아닙니다. 브라우저 안에서 돌고, 입력값은 사용자 기기에 남으며 만들 계정도 없습니다. 교환 조건은 기기를 옮기면 숫자가 따라오지 않는다는 점입니다.'),
  ('국가 평균 대신 왜 제가 내는 가격을 묻나요?',
   '국가 평균은 개인에게 자주 틀리기 때문입니다. 마지막으로 산 한 갑의 가격을 쓰면 내 실제 지출과 맞는 숫자가 나오고, 결정에 영향을 주는 쪽은 그 숫자입니다.'),
  ('제 수명을 예측할 수 있나요?',
   '아닙니다. 분 단위 수치는 인구 평균이며 개인 예측이 아닙니다. 임상적 위험은 병력 등 계산기가 보지 못하는 요인에 달려 있습니다. 개인의 건강 문제는 의료진과 상의하십시오.')],
},
]
