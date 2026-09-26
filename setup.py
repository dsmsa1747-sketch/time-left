#!/usr/bin/env python3
"""
Time Left — 배포 마무리 스크립트

사용법 (배포 주소를 알게 된 직후 1회):
    python3 setup.py https://내주소.github.io/time-left

광고·제휴 ID가 생겼을 때 (나중에 다시 실행해도 됨):
    python3 setup.py https://내주소 --adsense ca-pub-0000000000000000 \
        --slots 1111111111,2222222222,3333333333,4444444444 \
        --amazon timeleft-20

하는 일
  1) canonical·og:url·og:image·sitemap·robots 의 __SITE__ 를 실제 주소로 교체
  2) --adsense 를 주면 광고를 켜고 ads.txt 를 생성
  3) --amazon 을 주면 해외 제휴를 켬 (한국은 코드에서 항상 제외됨)
  4) 서비스워커 캐시 버전을 올려 옛 버전이 남지 않게 함
"""
import re, sys, os, argparse, pathlib

HERE = pathlib.Path(__file__).resolve().parent

def read(p):  return (HERE/p).read_text(encoding='utf-8')
def write(p, s): (HERE/p).write_text(s, encoding='utf-8'); print('  wrote', p)

ap = argparse.ArgumentParser()
ap.add_argument('site', help='배포 주소 (예: https://user.github.io/time-left)')
ap.add_argument('--adsense', default=None, help='ca-pub-XXXXXXXXXXXXXXXX')
ap.add_argument('--slots', default=None, help='quit,smoke,ledger,calc 순서 슬롯 ID 4개 (쉼표)')
ap.add_argument('--amazon', default=None, help='Amazon Associates 추적 ID')
a = ap.parse_args()

site = a.site.rstrip('/')
if not site.startswith('https://'):
    sys.exit('주소는 https:// 로 시작해야 합니다.')

print('1) 도메인 설정:', site)
for f in ['index.html', 'sitemap.xml', 'robots.txt']:
    if (HERE/f).exists():
        write(f, read(f).replace('__SITE__', site))

if a.adsense:
    if not re.fullmatch(r'ca-pub-\d{10,}', a.adsense):
        sys.exit('애드센스 ID 형식이 잘못됐습니다. ca-pub- 로 시작하는 숫자여야 합니다.')
    slots = (a.slots or '').split(',')
    if len(slots) != 4 or not all(s.strip().isdigit() for s in slots):
        sys.exit('--slots 에 슬롯 ID 4개를 쉼표로 주세요. 예: --slots 111,222,333,444')
    q, sm, le, ca = [s.strip() for s in slots]
    print('2) 애드센스 설정:', a.adsense)
    h = read('index.html')
    h = h.replace('client: "",', 'client: "%s",' % a.adsense)
    h = h.replace('slots: { quit:"", smoke:"", ledger:"", calc:"" }',
                  'slots: { quit:"%s", smoke:"%s", ledger:"%s", calc:"%s" }' % (q, sm, le, ca))
    write('index.html', h)
    write('ads.txt', 'google.com, %s, DIRECT, f08c47fec0942fa0\n' % a.adsense.replace('ca-', ''))
else:
    print('2) 애드센스 미설정 — 광고는 표시되지 않고 구글에 요청도 보내지 않습니다.')

if a.amazon:
    print('3) 아마존 제휴 설정:', a.amazon, '(한국 사용자에게는 항상 숨겨집니다)')
    write('index.html', read('index.html').replace('tag: "",', 'tag: "%s",' % a.amazon))
else:
    print('3) 제휴 미설정 — 제품 칸은 숨겨집니다.')

sw = read('sw.js')
m = re.search(r'timeleft-v(\d+)', sw)
n = int(m.group(1)) + 1
write('sw.js', re.sub(r'timeleft-v\d+', 'timeleft-v%d' % n, sw))
print('4) 서비스워커 캐시 v%d 로 올림' % n)

left = [f for f in ['index.html','sitemap.xml','robots.txt']
        if (HERE/f).exists() and '__SITE__' in read(f)]
print()
print('남은 __SITE__:', left if left else '없음 ✔')
print('완료. 이 폴더를 그대로 다시 올리면 됩니다.')
