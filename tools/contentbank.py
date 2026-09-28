#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contentbank.py — 무인 콘텐츠 뱅크 생성기
사람이 카피를 쓰지 않는다. 데이터(담뱃값·수명·회복타임라인) × 앵글 조합으로
발행 그대로 가능한 패키지를 자동 생성한다. 제작비 $0 (기존 영상 6클립 재조합).

출력: contentbank.json  — n8n이 읽어서 발행하는 큐
실행: python3 contentbank.py [개수]
"""
import json, os, sys, hashlib, datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://quitminutes.com"
MIN = 17                                   # UCL 2024, 개비당 분(남성)

W  = json.load(open('world.json'))
CN = json.load(open('countries.json'))
Q  = json.load(open('quitdata.json'))
QL, TL = Q['q'], Q['tl']

# 보유 클립 6개 — 추가 제작비 없음
CLIP = {'smoke':'v/smoke.mp4', 'surgery':'v/surgery.mp4', 'tray':'v/tray.mp4',
        'lungs':'v/lungs.mp4', 'dawn':'v/dawn.mp4', 'field':'v/field.mp4'}

# 지침: 발행 4개 중 풀링 3 : 키 1
ANGLES = ['price', 'minutes', 'recovery', 'key']
KIND   = {'price':'pull', 'minutes':'pull', 'recovery':'pull', 'key':'key'}

# 컷 구성 — 훅(충격) → 전환 → 회복(밝음). 줌은 ease-in-out만.
CUTS = {
 'price':    [('tray',0,2.0,'광학 줌인 ease-in-out'), ('smoke',0,2.5,'등속 금지'),
              ('dawn',0,2.0,'밝기 상승'), ('field',0,2.5,'가족·미소')],
 'minutes':  [('smoke',0,2.0,'슬로우'), ('surgery',0,2.5,'패턴 브레이크 · whoosh'),
              ('lungs',0,2.5,'회복 전환'), ('dawn',0,2.0,'해 뜨는 컷')],
 'recovery': [('lungs',0,2.5,'회복 시작'), ('dawn',0,2.0,'광량 증가'),
              ('field',0,3.0,'가족과 웃는 장면'), ('dawn',2,1.5,'클로징')],
 'key':      [('tray',0,1.5,'훅 숫자 크게'), ('smoke',0,2.0,'대비'),
              ('field',0,2.5,'미소'), ('dawn',0,2.0,'CTA 카드')],
}

DISC = {'en': "Educational information, not medical advice. Free to use, no account.",
        'ko': "의학적 조언이 아닌 정보 제공용입니다. 무료이며 계정이 필요 없습니다."}

TAGS = {'en': ["#quitsmoking","#stopsmoking","#smokefree","#quittingsmoking","#healthjourney",
               "#lungs","#nosmoking","#quitnow"],
        'ko': ["#금연","#금연챌린지","#담배끊기","#금연성공","#건강관리","#금연일기","#절연","#금연앱"]}


def money(v):
    return f"${v:,.0f}" if v >= 100 else f"${v:,.2f}"


def pkg(x, angle, lang):
    cc   = x['c']
    en, ko, slug = CN[cc]
    name = en if lang == 'en' else ko
    per  = x['per']
    pack = x['usd']
    yr   = pack * 365
    ten  = pack * 3650
    mp   = MIN * per
    yd   = int(mp * 365 // 1440)
    tel  = QL.get(cc, ["", ""])[1]
    url  = f"{SITE}/cost-of-smoking-{slug}.html?lang={lang}"

    if angle == 'price':
        if lang == 'en':
            hook  = f"{money(yr)} a year. Same habit, {name}."
            lines = [f"A pack in {name}: {money(pack)}",
                     f"One year, a pack a day: {money(yr)}",
                     f"Ten years: {money(ten)}"]
            cap   = (f"{money(yr)} a year is what a pack a day costs in {name} at today's prices. "
                     f"Ten years is {money(ten)}. The page below has the same table for {len(W)} countries, "
                     f"plus the free quitline number.")
        else:
            hook  = f"1년에 {money(yr)}. {name} 기준입니다."
            lines = [f"{name} 한 갑 {money(pack)}", f"하루 한 갑 1년 {money(yr)}", f"10년이면 {money(ten)}"]
            cap   = (f"{name}에서 하루 한 갑이면 1년에 {money(yr)}, 10년이면 {money(ten)}입니다. "
                     f"아래 페이지에 {len(W)}개국 같은 표와 무료 금연상담전화 번호가 있습니다.")
    elif angle == 'minutes':
        if lang == 'en':
            hook  = f"{MIN} minutes. Per cigarette."
            lines = [f"One cigarette: about {MIN} minutes of life",
                     f"One pack of {per}: {mp:,} minutes",
                     f"A pack a day for a year: {yd} days"]
            cap   = (f"A 2024 University College London analysis estimated about {MIN} minutes of life "
                     f"expectancy per cigarette for men. A pack of {per} is {mp:,} minutes. A year of that is "
                     f"about {yd} days. Population averages, not a prediction about one person.")
        else:
            hook  = f"{MIN}분. 한 개비당입니다."
            lines = [f"1개비 = 약 {MIN}분", f"한 갑({per}개비) = {mp:,}분", f"하루 한 갑 1년 = 약 {yd}일"]
            cap   = (f"2024년 UCL 분석은 담배 1개비가 남성 기준 기대수명 약 {MIN}분을 가져간다고 추정했습니다. "
                     f"{per}개비 한 갑이면 {mp:,}분, 1년이면 약 {yd}일입니다. "
                     f"인구 집단 평균이며 특정 개인에 대한 예측은 아닙니다.")
    elif angle == 'recovery':
        a, bb, c = TL[0], TL[1], TL[3] if len(TL) > 3 else TL[2]
        k = 'en' if lang == 'en' else 'ko'
        if lang == 'en':
            hook  = f"{a['en'][0]} after the last one."
            lines = [f"{a['en'][0]} — {a['en'][1]}", f"{bb['en'][0]} — {bb['en'][1]}", f"{c['en'][0]} — {c['en'][1]}"]
            cap   = ("Recovery does not start in years. It starts in minutes. The full WHO-based timeline "
                     f"and the free quitline for {name} are on the page below.")
        else:
            hook  = f"마지막 담배 후 {a['ko'][0]}."
            lines = [f"{a['ko'][0]} — {a['ko'][1]}", f"{bb['ko'][0]} — {bb['ko'][1]}", f"{c['ko'][0]} — {c['ko'][1]}"]
            cap   = (f"회복은 몇 년 뒤가 아니라 몇 분 뒤에 시작됩니다. WHO 기준 전체 타임라인과 "
                     f"{name} 무료 금연상담전화가 아래 페이지에 있습니다.")
    else:  # key — 전환
        if lang == 'en':
            hook  = "How much have you already lost?"
            lines = ["Enter the year you started",
                     "It counts money and minutes, live",
                     "Free · no account · nothing uploaded"]
            cap   = (f"Put in the year you started and what a pack costs you. It shows the money and the "
                     f"time so far, and keeps counting. Free, no sign-up, nothing leaves your phone. "
                     f"{name} prices and quitline included.")
        else:
            hook  = "지금까지 얼마를 잃었을까요?"
            lines = ["피우기 시작한 연도만 입력", "돈과 시간이 실시간으로 쌓입니다",
                     "무료 · 계정 없음 · 업로드 없음"]
            cap   = (f"시작한 연도와 한 갑 가격만 넣으면 지금까지의 돈과 시간이 나오고 계속 세어줍니다. "
                     f"무료, 가입 없음, 휴대폰 밖으로 나가지 않습니다. {name} 가격과 금연상담전화 포함.")

    tags = TAGS[lang][:6] + ([f"#{slug.replace('-','')}"] if angle != 'key' else [])
    pid  = hashlib.sha1(f"{cc}{angle}{lang}".encode()).hexdigest()[:10]

    return {
        "id": pid, "country": cc, "flag": x['f'], "angle": angle, "kind": KIND[angle],
        "lang": lang, "hook": hook, "text_lines": lines,
        "caption": cap + "\n\n" + DISC[lang] + "\n" + url,
        "hashtags": tags, "link": url,
        "quitline": tel,
        "video": {"aspect": "9:16", "target_sec": round(sum(c[2] for c in CUTS[angle]), 1),
                  "cuts": [{"clip": CLIP[c[0]], "in": c[1], "sec": c[2], "note": c[3]} for c in CUTS[angle]],
                  "rules": ["줌은 ease-in-out만 (등속=AI 티)", "무빙 전환에 whoosh",
                            "중간 패턴 브레이크 1컷", "제품/브랜드 소개 컷 금지",
                            "No smoothing / No beauty filter / No artificial glow"]},
        "platforms": ["instagram_reels", "youtube_shorts", "tiktok", "x"],
        "status": "queued"
    }


# ── 언어별 대상 국가 ──
RANK = sorted(W, key=lambda r: -r['usd'])
KO_CC = [x for x in RANK if x['usd'] >= 8] + [x for x in RANK if x['c'] == 'KR']   # 상위가격 + 한국

# ── 순서 배치: 앵글은 풀링3:키1 4주기, 국가는 매 슬롯 회전(같은 나라 연속 방지) ──
def lay(cs, lang):
    n, out = len(cs), []
    for i in range(n * 4):
        a = ANGLES[i % 4]
        out.append((cs[(i // 4 + i % 4) % n], a, lang))
    return out

order = []
en, ko = lay(RANK, 'en'), lay(KO_CC, 'ko')
for i in range(max(len(en), len(ko))):          # EN/KO 교차 발행
    if i < len(en): order.append(en[i])
    if i < len(ko): order.append(ko[i])

bank = [pkg(*o) for o in order]

# 발행 슬롯 배정 — 하루 2개, 간격 규칙 준수(계정 안전)
start = datetime.date.today() + datetime.timedelta(days=1)
for i, b in enumerate(bank):
    d = start + datetime.timedelta(days=i // 2)
    b["slot"] = f"{d.isoformat()}T{'09' if i % 2 == 0 else '19'}:10:00+09:00"

limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(bank)
bank = bank[:limit]

json.dump({"generated": datetime.datetime.now().isoformat(timespec='seconds'),
           "site": SITE, "count": len(bank), "items": bank},
          open('contentbank.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pull = sum(1 for b in bank if b['kind'] == 'pull')
print(f"콘텐츠 패키지 {len(bank)}개 생성 (풀링 {pull} : 키 {len(bank)-pull})")
print(f"발행 기간: {bank[0]['slot'][:10]} → {bank[-1]['slot'][:10]}  (하루 2개)")
print(f"언어: EN {sum(1 for b in bank if b['lang']=='en')} / KO {sum(1 for b in bank if b['lang']=='ko')}")
print("파일: contentbank.json")
