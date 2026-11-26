#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""checkfacts.py — countryfacts.json 의 출처를 실제로 때려서 검증.

판정
  - sources[].url 전부 GET → 200 아니면 경고 목록
  - 국가별 sources 개수 < 2 → 실패(exit 1)
  - fetched 가 30일 초과 → 경고
결과는 work/factcheck_YYYYMMDD.txt 에 남긴다.

실행: python tools/checkfacts.py            (전수 검증)
      python tools/checkfacts.py --offline  (HTTP 생략, 개수·날짜만)
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
from buildfacts import fetch                      # 같은 fetch 재사용

TODAY = datetime.date.today()
OFFLINE = '--offline' in sys.argv
F = json.load(open('countryfacts.json', encoding='utf-8'))

lines, bad_http, thin, stale, nogov = [], [], [], [], []
seen = {}

for cc, v in F.items():
    if cc.startswith('_'):
        continue
    srcs = v.get('sources') or []
    if len(srcs) < 2:
        thin.append(f"{cc} sources={len(srcs)}")
    if not any(s.get('own_country_official') for s in srcs):
        nogov.append(cc)
    for s in srcs:
        u = s['url']
        try:
            d = (TODAY - datetime.date.fromisoformat(s.get('fetched', '1970-01-01'))).days
        except ValueError:
            d = 9999
        if d > 30:
            stale.append(f"{cc} {d}일 전 {u}")
        if OFFLINE:
            continue
        if u not in seen:
            st, final, _ = fetch(u)
            seen[u] = st
        st = seen[u]
        if st != 200:
            bad_http.append(f"{cc} HTTP {st} {u}")
        lines.append(f"{cc} {st} {u}")

n = len([c for c in F if not c.startswith('_')])
rep = [f"factcheck {TODAY.isoformat()}  국가 {n}개",
       f"URL 검증 {len(seen)}건 중 200 정상 {sum(1 for x in seen.values() if x == 200)}건 / 실패 {len(bad_http)}건"
       if not OFFLINE else "URL 검증 생략(--offline)",
       f"출처 2개 미만 국가 {len(thin)}개: {', '.join(thin) if thin else '없음'}",
       f"자국 공식 출처 없는 국가 {len(nogov)}개: {', '.join(nogov) if nogov else '없음'} (경고 — govsources.json 보강 대상)",
       f"30일 초과 출처 {len(stale)}건",
       ""] + bad_http + [""] + lines

out = f"work/factcheck_{TODAY.strftime('%Y%m%d')}.txt"
open(out, 'w', encoding='utf-8').write("\n".join(rep) + "\n")
print("\n".join(rep[:4]))
print('wrote', out)

if thin:
    print(f"\n실패: 출처가 2개 미만인 국가 {len(thin)}개 — 자국 공식 출처를 govsources.json 에 보강해야 한다.")
    sys.exit(1)
print("\n통과")
