#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dupcheck.py — 국가 페이지 본문 중복도 측정(5-gram Jaccard).

애드센스 '가치 없는 콘텐츠' 판정의 핵심이 31개 페이지의 동일 구조였다.
얼마나 달라졌는지 숫자로 본다. 고치는 도구가 아니라 재는 도구다.

  전체본문  = 페이지 전체(공용 계산기·타임라인 블록 포함, 이 블록들은 유지가 원칙)
  고유구간  = 나라별 고유 섹션(규제~출처)만 잘라낸 것

실행: python tools/dupcheck.py [대상폴더=dist] [표본쌍수=10]
"""
import glob, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
d = sys.argv[1] if len(sys.argv) > 1 else 'dist'
pairs_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
random.seed(20261126)


def text(html_s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', html_s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def uniq_part(html_s):
    """영어 본문 중 'Tobacco rules in' ~ 'Other countries' 사이 = 이번에 새로 만든 고유 구간"""
    i = html_s.find('<h2>Tobacco rules in')
    j = html_s.find('<h2>Other countries</h2>')
    return html_s[i:j] if 0 <= i < j else ''


def grams(t, n=5):
    w = t.split()
    return {' '.join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def jac(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


files = sorted(glob.glob(os.path.join(d, 'cost-of-smoking-*.html')))
full = {f: grams(text(open(f, encoding='utf-8').read())) for f in files}
uniq = {f: grams(text(uniq_part(open(f, encoding='utf-8').read()))) for f in files}

pairs = random.sample([(a, b) for i, a in enumerate(files) for b in files[i + 1:]], min(pairs_n, len(files) * (len(files) - 1) // 2))
print(f'국가 페이지 {len(files)}개 · 표본 {len(pairs)}쌍 (5-gram Jaccard)')
fs, us = [], []
for a, b in pairs:
    x, y = jac(full[a], full[b]), jac(uniq[a], uniq[b])
    fs.append(x)
    us.append(y)
    print(f'  {os.path.basename(a)[16:-5]:<16} vs {os.path.basename(b)[16:-5]:<16} 전체 {x:.3f}  고유구간 {y:.3f}')
print(f'\n평균  전체 {sum(fs)/len(fs):.3f}  고유구간 {sum(us)/len(us):.3f}')
print(f'최대  전체 {max(fs):.3f}  고유구간 {max(us):.3f}')
print('기준: 고유구간 <= 0.35 목표. 전체본문은 공용 계산기·타임라인 블록을 유지하라는 지시 때문에 높게 나온다.')
