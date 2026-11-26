#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""checkld.py — 생성된 HTML 의 JSON-LD 유효성 검사.

각 페이지의 ld+json 블록을 json.loads 로 통과시키고 필수 키를 본다.
리치결과 테스트(로그인·외부 의존)는 하지 않는다 — JSON 유효성까지만 보증한다.

실행: python tools/checkld.py [대상폴더=dist]
"""
import json, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
d = sys.argv[1] if len(sys.argv) > 1 else 'dist'
BLK = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
REQ = ('@context', '@type')

bad, ok, pages = [], 0, 0
for p in sorted(glob.glob(os.path.join(d, '*.html'))):
    s = open(p, encoding='utf-8').read()
    blocks = BLK.findall(s)
    if not blocks:
        continue
    pages += 1
    for i, b in enumerate(blocks):
        try:
            o = json.loads(b)
        except json.JSONDecodeError as e:
            bad.append(f'{os.path.basename(p)} #{i} JSON 파싱 실패: {e}')
            continue
        nodes = o.get('@graph', [o]) if isinstance(o, dict) else o
        if isinstance(o, dict) and '@context' not in o:
            bad.append(f'{os.path.basename(p)} #{i} @context 없음')
        for nd in nodes:
            if not isinstance(nd, dict) or '@type' not in nd:
                bad.append(f'{os.path.basename(p)} #{i} @type 없음')
                continue
            t = nd['@type']
            need = {'Article': 'headline', 'FAQPage': 'mainEntity', 'BreadcrumbList': 'itemListElement',
                    'WebSite': 'name', 'WebApplication': 'name'}.get(t)
            if need and need not in nd:
                bad.append(f"{os.path.basename(p)} #{i} {t}: '{need}' 없음")
        ok += 1

print(f'ld+json 블록 {ok}개 / 페이지 {pages}개 · 문제 {len(bad)}건')
for x in bad[:30]:
    print('  -', x)
sys.exit(1 if bad else 0)
