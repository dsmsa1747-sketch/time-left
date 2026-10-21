import re, sys, glob, os
d = sys.argv[1] if len(sys.argv) > 1 else '.'
MARK = "<!--QM-ADS-->"
n = 0
for p in sorted(glob.glob(os.path.join(d, '*.html'))):
    s = open(p, encoding='utf-8').read()
    if MARK not in s: continue
    s2 = re.sub(re.escape(MARK) + r'\s*\n?<script[^>]*adsbygoogle\.js[^>]*>\s*</script>\s*\n?', '', s)
    if s2 != s: open(p, 'w', encoding='utf-8').write(s2); n += 1
ip = os.path.join(d, 'index.html')
if os.path.exists(ip):
    h = open(ip, encoding='utf-8').read()
    h = re.sub(r'client:\s*"ca-pub-\d+"', 'client: ""', h)
    open(ip, 'w', encoding='utf-8').write(h)
a = os.path.join(d, 'ads.txt')
if os.path.exists(a): os.remove(a)
sp = os.path.join(d, 'sw.js')
if os.path.exists(sp):
    sw = open(sp, encoding='utf-8').read()
    m = re.search(r'timeleft-v(\d+)', sw)
    if m: open(sp,'w',encoding='utf-8').write(re.sub(r'timeleft-v\d+','timeleft-v%d'%(int(m.group(1))+1), sw))
left = sum(len(re.findall(r'ca-pub-\d{10,}', open(p,encoding='utf-8').read())) for p in glob.glob(os.path.join(d,'*.html')))
print(f"제거: {n}장 | ads.txt: {'삭제' if not os.path.exists(a) else '남음'} | ca-pub 잔여: {left}")
sys.exit(1 if left else 0)
