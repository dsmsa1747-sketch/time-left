#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adsense.py — QuitMinutes 광고 일괄 적용 (저장소 루트에서 실행)

왜 필요한가:
  setup.py 는 index.html 한 장에만 광고를 켠다. 그런데 검색 트래픽은
  국가 페이지 31개와 소개·타임라인·담뱃값·상담전화 페이지로 들어온다.
  그 37장에 광고 코드가 하나도 없으면 수익이 나지 않는다.
  이 스크립트는 사이트의 모든 .html 에 애드센스 코드를 넣는다.

사용법
  승인 전 (게시자 ID만 있을 때 — 자동 광고로 시작):
      python3 adsense.py ca-pub-XXXXXXXXXXXXXXXX
  승인 후 (광고 단위 4개를 만든 뒤):
      python3 adsense.py ca-pub-XXXXXXXXXXXXXXXX --slots 111,222,333,444

여러 번 실행해도 안전하다(중복 삽입 없음).
"""
import re, sys, os, argparse, pathlib, glob

HERE = pathlib.Path(__file__).resolve().parent
MARK = "<!--QM-ADS-->"

ap = argparse.ArgumentParser()
ap.add_argument('client', help='ca-pub-XXXXXXXXXXXXXXXX')
ap.add_argument('--slots', default=None, help='승인 후에만. quit,smoke,ledger,calc 순서 4개')
a = ap.parse_args()

if not re.fullmatch(r'ca-pub-\d{10,}', a.client):
    sys.exit('게시자 ID 형식 오류. ca-pub- 로 시작하는 숫자여야 합니다.')

SNIPPET = (MARK + '\n'
           '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
           '?client=%s" crossorigin="anonymous"></script>\n' % a.client)

# ── 1) 모든 html 의 </head> 앞에 삽입 ──
pages = sorted(glob.glob(str(HERE / '*.html')))
added, skipped = 0, 0
for p in pages:
    s = open(p, encoding='utf-8').read()
    if MARK in s:
        skipped += 1
        continue
    if '</head>' not in s:
        print('  ! </head> 없음, 건너뜀:', os.path.basename(p))
        continue
    s = s.replace('</head>', SNIPPET + '</head>', 1)
    open(p, 'w', encoding='utf-8').write(s)
    added += 1
print('1) 광고 스크립트 삽입: 신규 %d장 · 이미있음 %d장 (전체 %d장)' % (added, skipped, len(pages)))

# ── 2) index.html 의 앱 내부 광고 설정 ──
ip = HERE / 'index.html'
h = open(ip, encoding='utf-8').read()
h = re.sub(r'client:\s*"[^"]*"', 'client: "%s"' % a.client, h, count=1)
# 심사자가 보고 혼동할 수 있는 가짜 ID 주석 제거
h = h.replace('/* 예: "ca-pub-0000000000000000" */', '')
h = h.replace('ca-pub-0000000000000000', '')
if a.slots:
    sl = [x.strip() for x in a.slots.split(',')]
    if len(sl) != 4 or not all(x.isdigit() for x in sl):
        sys.exit('--slots 는 숫자 4개를 쉼표로. 예: --slots 111,222,333,444')
    h = re.sub(r'slots:\s*\{[^}]*\}',
               'slots: { quit:"%s", smoke:"%s", ledger:"%s", calc:"%s" }' % tuple(sl), h, count=1)
    print('2) 앱 내부 광고 4자리 설정 완료 (승인 후 모드)')
else:
    print('2) 앱 내부 client 설정 완료. 슬롯은 비어 있음 → 자동 광고로 동작 (승인 전 모드)')
open(ip, 'w', encoding='utf-8').write(h)

# ── 3) ads.txt ──
(HERE / 'ads.txt').write_text(
    'google.com, %s, DIRECT, f08c47fec0942fa0\n' % a.client.replace('ca-', ''), encoding='utf-8')
print('3) ads.txt 생성')

# ── 4) 서비스워커 캐시 버전 올림 (옛 버전이 광고 없는 페이지를 계속 보여주지 않게) ──
sp = HERE / 'sw.js'
if sp.exists():
    sw = open(sp, encoding='utf-8').read()
    m = re.search(r'timeleft-v(\d+)', sw)
    if m:
        n = int(m.group(1)) + 1
        open(sp, 'w', encoding='utf-8').write(re.sub(r'timeleft-v\d+', 'timeleft-v%d' % n, sw))
        print('4) 서비스워커 캐시 v%d' % n)

# ── 5) 자가 검증 ──
bad = [os.path.basename(p) for p in pages if MARK not in open(p, encoding='utf-8').read()]
leftover = sum(open(p, encoding='utf-8').read().count('ca-pub-0000000000000000') for p in pages)
print()
print('검증 — 광고 미삽입 페이지:', bad if bad else '없음 ✔')
print('검증 — 가짜 ID 잔여:', leftover)
print('검증 — ads.txt:', (HERE / 'ads.txt').read_text(encoding='utf-8').strip())
if bad or leftover:
    sys.exit('검증 실패. 커밋하지 마세요.')
print('\n완료. 커밋·푸시하면 전 페이지에 광고가 올라갑니다.')
