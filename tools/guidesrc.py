#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guidesrc.py — 가이드 12편이 쓸 출처를 실제로 받아서 검증·발췌한다.

사람이 사실을 쓰지 않는다. 여기서 200 으로 확인되고 발췌가 잡힌 URL 만
guidesources.json 에 들어가고, genguides.py 는 그것만 인용한다.

출력
  work/guide_probe.json   원자료(상태코드·최종URL·제목·발췌 후보)
  work/guide_probe.txt    사람이 읽는 요약

실행: python tools/guidesrc.py            (전수)
      python tools/guidesrc.py --only who (부분)
"""
import json, os, re, sys, datetime, html as H, ssl, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
from buildfacts import UA                         # 같은 UA 재사용


def fetch(url):
    """상태코드·최종URL·본문. 선언 charset 이 틀린 정부 사이트가 있어 인코딩을 추정한다."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en,ko;q=0.8'})
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            raw = r.read(500_000)
            cands = [r.headers.get_content_charset() or 'utf-8', 'utf-8', 'euc-kr', 'cp949', 'shift_jis']
            best, best_bad = '', 10 ** 9
            for enc in cands:
                try:
                    t = raw.decode(enc, 'replace')
                except LookupError:
                    continue
                bad = t.count('�')
                if bad < best_bad:
                    best, best_bad = t, bad
                if bad == 0:
                    break
            return r.status, r.geturl(), best
    except urllib.error.HTTPError as e:
        return e.code, url, ''
    except Exception as e:
        return 0, url, f'__ERR__{type(e).__name__}: {e}'

TODAY = datetime.date.today().isoformat()

# key: (url, 발췌에 쓸 키워드)
CAND = {
 'who_tobacco':      ('https://www.who.int/news-room/fact-sheets/detail/tobacco', ['kills', 'million']),
 'who_cessation_qa': ('https://www.who.int/news-room/questions-and-answers/item/tobacco-health-benefits-of-smoking-cessation', ['minutes', 'hours', 'benefit']),
 'who_tax':          ('https://www.who.int/activities/raising-taxes-on-tobacco', ['tax', 'price']),
 'cdc_quit':         ('https://www.cdc.gov/tobacco/campaign/tips/quit-smoking/index.html', ['quit']),
 'cdc_benefits':     ('https://www.cdc.gov/tobacco/about/benefits-of-quitting.html', ['benefit', 'quit']),
 'cdc_nrt':          ('https://www.cdc.gov/tobacco/campaign/tips/quit-smoking/quit-smoking-medications/index.html', ['medication', 'nicotine']),
 'nhs_quit':         ('https://www.nhs.uk/better-health/quit-smoking/', ['quit', 'support']),
 'nhs_treatments':   ('https://www.nhs.uk/conditions/stop-smoking-treatments/', ['patch', 'gum', 'nicotine']),
 'nhs_cravings':     ('https://www.nhs.uk/live-well/quit-smoking/10-self-help-tips-to-stop-smoking/', ['craving', 'alcohol']),
 'nhs_pregnancy':    ('https://www.nhs.uk/pregnancy/keeping-well/stop-smoking/', ['pregnan', 'baby']),
 'ucl_research':     ('https://www.ucl.ac.uk/epidemiology-health-care/research/behavioural-science-and-health', ['smok', 'research']),
 'ucl_news_quit':    ('https://www.ucl.ac.uk/news/2026/nov/women-middle-age-less-likely-quit-smoking-successfully', ['smok', 'quit']),
 'kr_guide':         ('https://www.nosmokeguide.go.kr/', ['금연', '담배']),
 'kr_ncc':           ('https://nosmk.khealth.or.kr/nsk/ntcc/index.do', ['금연', '지원']),
 'jp_mhlw':          ('https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/tobacco/index.html', ['たばこ', '禁煙']),
 'eu_tobacco':       ('https://health.ec.europa.eu/tobacco/overview_en', ['tobacco']),
 'ca_tobacco':       ('https://www.canada.ca/en/health-canada/services/smoking-tobacco.html', ['tobacco', 'quit']),
 'who_ecig_qa':      ('https://www.who.int/news-room/questions-and-answers/item/tobacco-e-cigarettes', ['e-cigarette', 'nicotine', 'children']),
 'cdc_ecig':         ('https://www.cdc.gov/tobacco/e-cigarettes/index.html', ['e-cigarette', 'nicotine']),
 'medlineplus':      ('https://medlineplus.gov/quittingsmoking.html', ['withdrawal', 'weight', 'quit']),
}

ONLY = None
if '--only' in sys.argv:
    ONLY = sys.argv[sys.argv.index('--only') + 1]

TAG = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
STRIP = re.compile(r'<[^>]+>')


def text_of(body):
    b = TAG.sub(' ', body)
    b = STRIP.sub(' ', b)
    b = H.unescape(b)
    return re.sub(r'\s+', ' ', b).strip()


def title_of(body):
    m = re.search(r'<title[^>]*>(.*?)</title>', body, re.S | re.I)
    return re.sub(r'\s+', ' ', H.unescape(m.group(1))).strip()[:160] if m else ''


def quotes(txt, kws, n=4):
    out = []
    for s in re.split(r'(?<=[.!?。])\s+|(?<=다\.)\s+', txt):
        s = s.strip()
        if not (40 <= len(s) <= 300):
            continue
        if any(k.lower() in s.lower() for k in kws):
            out.append(s)
        if len(out) >= n:
            break
    return out


def main():
    res = {}
    for key, (url, kws) in CAND.items():
        if ONLY and ONLY not in key:
            continue
        st, final, body = fetch(url)
        txt = text_of(body) if st == 200 else ''
        res[key] = {'url': url, 'status': st, 'final': final, 'fetched': TODAY,
                    'title': title_of(body) if st == 200 else '',
                    'len': len(txt), 'quotes': quotes(txt, kws) if txt else []}
        print(f"{st:>4} q={len(res[key]['quotes'])} {key:18} {res[key]['title'][:60]}")

    os.makedirs('work', exist_ok=True)
    json.dump(res, open('work/guide_probe.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open('work/guide_probe.txt', 'w', encoding='utf-8') as f:
        for k, v in res.items():
            f.write(f"== {k} [{v['status']}] {v['url']}\n{v['title']}\n")
            for q in v['quotes']:
                f.write(f"  - {q}\n")
            f.write("\n")
    ok = sum(1 for v in res.values() if v['status'] == 200 and v['quotes'])
    print(f"\n사용 가능(200+발췌) {ok} / {len(res)}  → work/guide_probe.json")


if __name__ == '__main__':
    main()
