#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mklegal.py — 배포된 privacy.html / terms.html 본문을 떼어 legal_bodies.json 복원.

genpages.py 는 legal_bodies.json 을 읽는데 그 파일이 저장소에 없어서 빌드가 멈춘다
(2026-11-26 확인). 본문 원문은 루트의 배포본 안에 그대로 있으므로 거기서 되살린다.
문구는 한 글자도 바꾸지 않는다. 결과를 tools/legal_bodies.json 에 쓴다.

실행: python tools/mklegal.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

EN = re.compile(r'<div data-l="en">(.*?)\n<a class="back"', re.S)
KO = re.compile(r'<div data-l="ko" hidden>(.*?)\n<a class="back"', re.S)

out = {}
for f in ('privacy.html', 'terms.html'):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    en, ko = EN.search(s), KO.search(s)
    assert en and ko, f'{f}: 본문 블록을 찾지 못했다'
    out[f] = [en.group(1), ko.group(1)]

p = os.path.join(HERE, 'legal_bodies.json')
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for f, (en, ko) in out.items():
    print(f'  {f:14} en {len(en):>6,}자  ko {len(ko):>6,}자')
print('wrote', p)
