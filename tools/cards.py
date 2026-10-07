#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cards.py — QuitMinutes 카드뉴스 자동 생성기 (제작비 $0 · 무한 · 사람이 글 안 씀)

영상(render.py)과 같은 데이터·같은 팔레트에서 카드뉴스를 만든다.
한 세트 = 5장: 훅 → 숫자 → 비교 → 회복 → CTA

출력
  cards/<id>/01..05.png   1080x1350  (인스타 피드·캐러셀, 스레드)
  pins/<id>.png           1000x1500  (핀터레스트 2:3)

실행
  python3 cards.py [시작index] [개수] [--lang en|ko]
"""
import json, os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SERIF = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
SANS  = '/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
BLACK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
KR = 1

# 앱과 동일한 천당/지옥 팔레트
HELL, HELL_T, HELL_D = (10, 8, 7), (237, 230, 220), (148, 136, 126)
HEAV, HEAV_T, HEAV_D = (246, 243, 236), (23, 21, 15), (87, 80, 63)
GREEN, RED = (44, 122, 86), (168, 42, 30)
SITE = "quitminutes.com"
MIN = 17

W = json.load(open('world.json'))
CN = json.load(open('countries.json'))
Q = json.load(open('quitdata.json'))
QL, TL = Q['q'], Q['tl']
BANK = json.load(open('contentbank.json'))['items']

_fc = {}
def F(p, s):
    k = (p, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(p, s, index=KR)
    return _fc[k]

_vig = {}
def vignette(img, size, color=(58, 8, 4), strength=.55):
    w, h = size
    if size not in _vig:
        y, x = np.mgrid[0:h, 0:w].astype(np.float32)
        r = np.sqrt(((x - w/2)/(w*.72))**2 + ((y - h/2)/(h*.62))**2)
        _vig[size] = np.clip((r - .30)/.95, 0, 1)**1.7
    img.paste(Image.new('RGB', size, color), (0, 0),
              Image.fromarray((_vig[size]*strength*255).astype(np.uint8), 'L'))

def wrap(d, text, font, maxw):
    """공백 + 글자 단위 혼합 줄바꿈 (한국어 대응)"""
    out, line = [], ""
    for wd in text.split():
        t = (line + " " + wd).strip()
        if d.textlength(t, font=font) <= maxw or not line: line = t
        else: out.append(line); line = wd
    if line: out.append(line)
    res = []
    for ln in out:
        while d.textlength(ln, font=font) > maxw and len(ln) > 1:
            c = len(ln)
            while c > 1 and d.textlength(ln[:c], font=font) > maxw: c -= 1
            res.append(ln[:c]); ln = ln[c:]
        if ln: res.append(ln)
    return res


def card(size, dark, big=None, big_c=None, head=None, head_size=78,
         subs=None, foot=True, page=None, pages=None, flag=None):
    w, h = size
    img = Image.new('RGB', size, HELL if dark else HEAV)
    if dark: vignette(img, size)
    d = ImageDraw.Draw(img)
    T  = HELL_T if dark else HEAV_T
    D  = HELL_D if dark else HEAV_D
    cx, pad = w//2, int(w*.085)
    blocks = []
    fi = flag_img(flag, int(w*.20)) if flag else None
    if big:
        bs = int(w*.215)
        bf = F(BLACK, bs)
        while bs > 40 and d.textlength(big, font=bf) > w - pad*2:   # 폭 자동 맞춤
            bs = int(bs*.93); bf = F(BLACK, bs)
        blocks.append((big, bf, big_c or T, int(h*.030)))
    if head:
        hf = F(SERIF, int(w*head_size/1080))
        for ln in wrap(d, head, hf, w - pad*2):
            blocks.append((ln, hf, T, int(h*.012)))
    if subs:
        sf = F(SANS, int(w*.050))
        blocks.append(("", sf, D, int(h*.018)))
        for s in subs:
            for ln in wrap(d, s, sf, w - pad*2):
                blocks.append((ln, sf, D, int(h*.008)))
            blocks.append(("", sf, D, int(h*.014)))
    fh = (fi.height + int(h*.030)) if fi else 0
    tot = sum((f.getbbox('Ay')[3]-f.getbbox('Ay')[1] + int(f.size*.30) if t else 0) + g
              for t, f, c, g in blocks)
    y = int(h*.42) - (tot + fh)//2
    if fi:
        img.paste(fi, (cx - fi.width//2, y), fi); y += fi.height + int(h*.030)
    for t, f, c, g in blocks:
        if t:
            d.text((cx, y), t, font=f, fill=c, anchor='ma')
            y += (f.getbbox('Ay')[3]-f.getbbox('Ay')[1]) + int(f.size*.30)
        y += g
    if foot:
        d.text((cx, h - int(h*.085)), SITE, font=F(SANS, int(w*.034)), fill=D, anchor='ma')
    if page and pages:
        d.text((w - pad, int(h*.055)), f"{page}/{pages}",
               font=F(SANS, int(w*.030)), fill=D, anchor='ra')
    return img


EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
_ef = None
def flag_img(ch, px):
    """국기 이모지를 투명 PNG로 — 폰트가 없거나 실패하면 None"""
    global _ef
    try:
        if _ef is None: _ef = ImageFont.truetype(EMOJI, 109)
        t = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(t).text((80, 80), ch, font=_ef, anchor='mm', embedded_color=True)
        bb = t.getbbox()
        if not bb: return None
        t = t.crop(bb)
        r = px / max(t.size)
        return t.resize((max(1, int(t.width*r)), max(1, int(t.height*r))), Image.LANCZOS)
    except Exception:
        return None


def money(v): return f"${v:,.0f}" if v >= 100 else f"${v:,.2f}"


def make_set(item, size=(1080, 1350), outdir='cards'):
    cc, lang, ko = item['country'], item['lang'], item['lang'] == 'ko'
    x = next(r for r in W if r['c'] == cc)
    en_n, ko_n, _ = CN[cc]
    name = ko_n if ko else en_n
    per, pack = x['per'], x['usd']
    yr, ten = pack*365, pack*3650
    mp = MIN*per
    yd = int(mp*365//1440)
    tel = QL.get(cc, ["", ""])[1]
    t0, t1 = TL[0], TL[3] if len(TL) > 3 else TL[1]
    k = 'ko' if ko else 'en'

    if ko:
        c = [
          dict(dark=True,  head=f"{name}에서 담배가 가져가는 것", head_size=86, flag=x['f']),
          dict(dark=True,  big=money(yr), big_c=RED, head="하루 한 갑, 1년치 돈",
               subs=[f"한 갑 {money(pack)} · 10년이면 {money(ten)}"]),
          dict(dark=True,  big=f"{yd}일", head="1년에 잃는 기대수명",
               subs=[f"1개비 약 {MIN}분 · 한 갑 {mp:,}분",
                     "2024년 UCL 분석(남성 기준) · 인구 평균이며 개인 예측이 아닙니다"]),
          dict(dark=False, head="끊으면 달라지는 것", head_size=82,
               subs=[f"{t0['ko'][0]} — {t0['ko'][1]}", f"{t1['ko'][0]} — {t1['ko'][1]}",
                     (f"{name} 무료 금연상담전화 {tel}" if tel else "")]),
          dict(dark=False, head="남은 시간", head_size=108,
               subs=["내 숫자로 계산해 보세요", "무료 · 가입 없음", SITE]),
        ]
    else:
        c = [
          dict(dark=True,  head=f"What smoking costs in {en_n}", head_size=86, flag=x['f']),
          dict(dark=True,  big=money(yr), big_c=RED, head="a year, at a pack a day",
               subs=[f"A pack is {money(pack)} · ten years is {money(ten)}"]),
          dict(dark=True,  big=f"{yd} days", head="of life expectancy, per year",
               subs=[f"About {MIN} minutes per cigarette · {mp:,} minutes a pack",
                     "UCL 2024, men. Population averages, not a prediction about one person."]),
          dict(dark=False, head="What changes when you stop", head_size=82,
               subs=[f"{t0['en'][0]} — {t0['en'][1]}", f"{t1['en'][0]} — {t1['en'][1]}",
                     (f"Free quitline in {en_n}: {tel}" if tel else "")]),
          dict(dark=False, head="Time Left", head_size=108,
               subs=["Run your own numbers", "Free · no sign-up", SITE]),
        ]

    d = os.path.join(outdir, item['id'])
    os.makedirs(d, exist_ok=True)
    paths = []
    for i, spec in enumerate(c, 1):
        spec = {kk: vv for kk, vv in spec.items() if vv not in (None, "")}
        if 'subs' in spec: spec['subs'] = [s for s in spec['subs'] if s]
        img = card(size, page=i, pages=len(c), **spec)
        p = os.path.join(d, f"{i:02d}.png")
        img.save(p, optimize=True)
        paths.append(p)
    return paths


def make_pin(item, outdir='pins'):
    """핀터레스트용 2:3 한 장 — 세트의 2번(숫자) 카드를 세로로"""
    os.makedirs(outdir, exist_ok=True)
    cc, ko = item['country'], item['lang'] == 'ko'
    x = next(r for r in W if r['c'] == cc)
    en_n, ko_n, _ = CN[cc]
    name = ko_n if ko else en_n
    yr = x['usd']*365
    yd = int(MIN*x['per']*365//1440)
    if ko:
        img = card((1000, 1500), True, big=money(yr), big_c=RED,
                   head=f"{name} · 하루 한 갑 1년", subs=[f"그리고 기대수명 {yd}일", SITE])
    else:
        img = card((1000, 1500), True, big=money(yr), big_c=RED,
                   head=f"{en_n} · a pack a day, one year", subs=[f"and {yd} days of life expectancy", SITE])
    p = os.path.join(outdir, item['id'] + '.png')
    img.save(p, optimize=True)
    return p


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    lang = 'ko' if '--lang' in sys.argv and sys.argv[sys.argv.index('--lang')+1] == 'ko' else None
    pool = [i for i in BANK if i['angle'] == 'price' and (lang is None or i['lang'] == lang)]
    s = int(args[0]) if args else 0
    n = int(args[1]) if len(args) > 1 else 2
    for it in pool[s:s+n]:
        make_set(it); make_pin(it)
        print(f"{it['id']} {it['flag']} {it['lang']}  카드 5장 + 핀 1장")
    print(f"\n대상 풀: {len(pool)}세트 (price 앵글 기준)")
