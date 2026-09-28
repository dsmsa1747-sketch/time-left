#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py — 무인 영상 렌더러 (제작비 $0 · AI 티 없음 · 저작권 이슈 없음)
contentbank.json 의 패키지를 1080x1920 세로 영상으로 직접 렌더한다.
데이터 타이포그래피 방식: 앱의 천당/지옥 팔레트 + 실제 숫자 카운트업.
줌은 전부 ease-in-out (등속 금지 — 등속은 AI 티).

실행: python3 render.py [시작index] [개수]
출력: out/<id>.mp4
"""
import json, os, sys, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS = 1080, 1920, 30
SERIF = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
SANS  = '/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
BLACK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
KR = 1                                            # ttc 안 한국어 페이스 index

# 앱과 동일한 팔레트
HELL  = (10, 8, 7);     HELL_T = (237, 230, 220); HELL_D = (148, 136, 126)
HEAVEN= (246, 243, 236); HEAV_T = (23, 21, 15);   HEAV_D = (87, 80, 63)
GREEN = (44, 122, 86);  RED = (168, 42, 30)

_fc = {}
def F(path, size):
    k = (path, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(path, size, index=KR)
    return _fc[k]

def ease(t):                                       # ease-in-out
    t = max(0.0, min(1.0, t)); return t * t * (3 - 2 * t)

def wrap(d, text, font, maxw):
    out, line = [], ""
    for wd in text.split():
        t = (line + " " + wd).strip()
        if d.textlength(t, font=font) <= maxw or not line: line = t
        else: out.append(line); line = wd
    if line: out.append(line)
    return out

def wrap_cjk(d, text, font, maxw):
    """한국어는 공백이 적어 글자 단위로도 접는다"""
    if d.textlength(text, font=font) <= maxw: return [text]
    lines = wrap(d, text, font, maxw)
    res = []
    for ln in lines:
        while d.textlength(ln, font=font) > maxw and len(ln) > 1:
            cut = len(ln)
            while cut > 1 and d.textlength(ln[:cut], font=font) > maxw: cut -= 1
            res.append(ln[:cut]); ln = ln[cut:]
        if ln: res.append(ln)
    return res

_VIG = None
def vignette(img, color, strength=0.55):
    """부드러운 방사형 비네트 — 링 없음"""
    global _VIG
    if _VIG is None:
        y, x = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((x - W / 2) / (W * 0.72)) ** 2 + ((y - H / 2) / (H * 0.62)) ** 2)
        _VIG = np.clip((r - 0.30) / 0.95, 0, 1) ** 1.7
    a = (_VIG * strength * 255).astype(np.uint8)
    img.paste(Image.new('RGB', (W, H), color), (0, 0), Image.fromarray(a, 'L'))


_BG = {}
def bgcache(bg, hell):
    k = (bg, hell)
    if k not in _BG:
        im = Image.new('RGB', (W, H), bg)
        if hell: vignette(im, (58, 8, 4), 0.55)
        _BG[k] = im
    return _BG[k]


def card(bg, txt_c, dim_c, headline, hf_path, hf_size, sub=None, big=None,
         big_c=None, foot=None, hell=False, scale=1.0):
    img = bgcache(bg, hell).copy()
    d = ImageDraw.Draw(img)
    cx = W // 2
    blocks = []
    if big:
        bf = F(BLACK, int(268 * scale))
        blocks.append(('big', big, bf, big_c or txt_c, 40))
    hf = F(hf_path, int(hf_size * scale))
    for ln in wrap_cjk(d, headline, hf, W - 130):
        blocks.append(('h', ln, hf, txt_c, 18))
    if sub:
        sf = F(SANS, int(62 * scale))
        for s in sub:
            for ln in wrap_cjk(d, s, sf, W - 150):
                blocks.append(('s', ln, sf, dim_c, 10))
            blocks.append(('gap', '', sf, dim_c, 26))
    tot = 0
    for kind, t, f, c, gap in blocks:
        tot += (f.getbbox('Ay')[3] - f.getbbox('Ay')[1] if t else 0) + gap + (int(f.size * .32) if t else 0)
    y = int(H * 0.40) - tot // 2
    for kind, t, f, c, gap in blocks:
        if t:
            d.text((cx, y), t, font=f, fill=c, anchor='ma')
            y += (f.getbbox('Ay')[3] - f.getbbox('Ay')[1]) + int(f.size * .32)
        y += gap
    if foot:
        ff = F(SANS, 46)
        d.text((cx, H - 250), foot, font=ff, fill=dim_c, anchor='ma')
    return img


def zoomed(img, p, z0=1.0, z1=1.13):
    """ease-in-out 광학 줌인 — 1프레임 산출"""
    z = z0 + (z1 - z0) * ease(p)
    w, h = int(W * z), int(H * z)
    big = img.resize((w, h), Image.LANCZOS)
    return big.crop(((w - W) // 2, (h - H) // 2, (w - W) // 2 + W, (h - H) // 2 + H))


def num_fmt(v, kind):
    if kind == 'money': return f"${v:,.0f}"
    if kind == 'days':  return f"{v:,.0f}"
    return f"{v:,.0f}"


def build(item, outdir='out'):
    lang, ang = item['lang'], item['angle']
    ko = lang == 'ko'
    hook = item['hook']; lines = item['text_lines']
    site = "quitminutes.com"

    # 카운터에 쓸 숫자 — 앵글별로 가장 센 수치를 뽑는다
    import re
    def grab(pat, src):
        m = re.search(pat, src)
        return m.group(0) if m else None
    joined = " ".join(lines)
    if ang == 'price':
        target = grab(r'\$[\d,]+', lines[1]) or grab(r'\$[\d,]+', hook)
        clabel = ("한 해에 사라지는 돈" if ko else "gone in one year")
        cval = float(re.sub(r'[^\d.]', '', target or '0')); ckind = 'money'
    elif ang == 'minutes':
        target = grab(r'[\d,]+', lines[1])
        clabel = ("한 갑이 가져가는 분" if ko else "minutes, one pack")
        cval = float(re.sub(r'[^\d.]', '', target or '0')); ckind = 'num'
    elif ang == 'recovery':
        target = "20"
        clabel = ("분 만에 시작됩니다" if ko else "minutes. That's all it takes to start")
        cval = 20.0; ckind = 'num'
    else:
        target = None
        clabel = ("무료 · 계정 없음 · 업로드 없음" if ko else "Free · no account · nothing uploaded")
        cval = 0.0; ckind = 'num'

    HF = SERIF
    c1 = card(HELL, HELL_T, HELL_D, hook, HF, 136, hell=True, foot=site)
    c3 = card(HEAVEN, HEAV_T, HEAV_D,
              (lines[0] if ang != 'key' else ("지금까지 잃은 시간과 돈" if ko else "The time and money so far")),
              HF, 104, sub=lines[1:], foot=site)
    c4 = card(HEAVEN, HEAV_T, GREEN,
              ("남은 시간" if ko else "Time Left"), HF, 124,
              sub=[("무료 · 가입 없음" if ko else "Free · no sign-up"),
                   site], foot=None)

    SEG = [(c1, 2.4, 1.0, 1.10),
           ('counter', 2.2, 0, 0),
           (c3, 2.2, 1.06, 1.0),
           (c4, 2.0, 1.0, 1.06)]

    p = subprocess.Popen(
        ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
         '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-pix_fmt', 'yuv420p',
         '-movflags', '+faststart', f'{outdir}/{item["id"]}.mp4'], stdin=subprocess.PIPE)

    for seg in SEG:
        n = int(seg[1] * FPS)
        if seg[0] == 'counter':
            for i in range(n):
                pr = ease(i / max(1, n - 1))
                v = cval * pr
                fr = card(HELL, HELL_T, HELL_D, clabel, SANS, 62,
                          big=num_fmt(v, ckind), big_c=(RED if ang == 'price' else HELL_T),
                          hell=True, foot=site)
                p.stdin.write(fr.tobytes())
        else:
            img, _, z0, z1 = seg
            for i in range(n):
                p.stdin.write(zoomed(img, i / max(1, n - 1), z0, z1).tobytes())
    p.stdin.close(); p.wait()
    return f'{outdir}/{item["id"]}.mp4'


if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    bank = json.load(open('contentbank.json'))['items']
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    for it in bank[s:s + n]:
        f = build(it)
        sz = os.path.getsize(f)
        print(f"{it['id']} {it['flag']} {it['lang']} {it['angle']:9} {sz:>8,} B  {f}")
