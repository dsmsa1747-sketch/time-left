# checkguides.py - numeric pass/fail gate for the 12 info guides + hub.
# Run from the repo root or from tools/ ; it looks for the pages in ../ then ./dist.
import json, os, re, sys, datetime

SLUGS = [
    'guide-first-72-hours', 'guide-nicotine-replacement', 'guide-korea-cigarette-price-history',
    'guide-20-minutes-per-cigarette', 'guide-korea-quit-support', 'guide-withdrawal-symptoms',
    'guide-weight-gain', 'guide-alcohol-cravings', 'guide-vaping-heated-tobacco',
    'guide-cigarette-tax-share', 'guide-pregnancy-quit', 'guide-using-quitminutes',
]
MIN_KO, MIN_EN = 1800, 900          # guides
HUB_KO, HUB_EN = 600, 300           # guides.html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIRS = [ROOT, os.path.join(HERE, 'dist'), os.getcwd()]


def find(fname):
    for d in DIRS:
        p = os.path.join(d, fname)
        if os.path.exists(p):
            return p
    return None


def lang_block(html, lang):
    """Body text of the <div data-l="LANG"> content block (nav/footer excluded)."""
    i = html.find('data-l="%s"' % lang, html.find('<div'))
    best = ''
    for m in re.finditer(r'<div[^>]*data-l="%s"[^>]*>' % lang, html):
        seg = html[m.end():]
        depth, pos = 1, 0
        for t in re.finditer(r'</?div\b', seg):
            depth += 1 if t.group(0) == '<div' else -1
            if depth == 0:
                pos = t.start()
                break
        cand = seg[:pos] if pos else seg
        if len(cand) > len(best):
            best = cand
    return best


def strip(html):
    html = re.sub(r'<(script|style)\b.*?</\1>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = re.sub(r'&[a-z]+;|&#\d+;', ' ', html)
    return re.sub(r'\s+', ' ', html).strip()


def check(fname, min_ko, min_en, is_hub=False):
    p = find(fname)
    if not p:
        return dict(file=fname, ok=False, why='missing')
    html = open(p, encoding='utf-8').read()
    ko = strip(lang_block(html, 'ko'))
    en = strip(lang_block(html, 'en'))
    ko_n = len(ko)
    en_n = len(en.split())
    body = lang_block(html, 'ko') + lang_block(html, 'en')
    h2 = len(re.findall(r'<h2\b', body))
    tables = len(re.findall(r'<table\b', body))
    src = len(re.findall(r'href="https?://(?!quitminutes\.com)', body))
    ld_types, ld_ok, faq_n = [], True, 0
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(blob)
        except Exception:
            ld_ok = False
            continue
        nodes = d.get('@graph', [d])
        for nd in nodes:
            ld_types.append(nd.get('@type'))
            if nd.get('@type') == 'FAQPage':
                faq_n = len(nd.get('mainEntity', []))
    fails = []
    if ko_n < min_ko:
        fails.append('ko<%d' % min_ko)
    if en_n < min_en:
        fails.append('en<%d' % min_en)
    if not is_hub:
        if h2 < 5:
            fails.append('h2<5')
        if tables < 1:
            fails.append('no-table')
        if src < 2:
            fails.append('sources<2')
        if faq_n < 3:
            fails.append('faq<3')
        for t in ('Article', 'FAQPage'):
            if t not in ld_types:
                fails.append('no-%s' % t)
    if not ld_ok:
        fails.append('ld-parse')
    return dict(file=fname, ko=ko_n, en=en_n, h2=h2, tables=tables, src=src, faq=faq_n,
                ld=','.join(t for t in ld_types if t), ok=not fails, why=' '.join(fails))


def main():
    rows = [check(s + '.html', MIN_KO, MIN_EN) for s in SLUGS]
    rows.append(check('guides.html', HUB_KO, HUB_EN, is_hub=True))
    w = max(len(r['file']) for r in rows)
    lines = ['%-*s %6s %6s %3s %3s %4s %3s  %-28s %s'
             % (w, 'file', 'ko', 'en', 'h2', 'tbl', 'src', 'faq', 'ld+json', 'verdict')]
    for r in rows:
        lines.append('%-*s %6s %6s %3s %3s %4s %3s  %-28s %s'
                     % (w, r['file'], r.get('ko', '-'), r.get('en', '-'), r.get('h2', '-'),
                        r.get('tables', '-'), r.get('src', '-'), r.get('faq', '-'),
                        r.get('ld', '-'), 'PASS' if r['ok'] else 'FAIL ' + r['why']))
    bad = [r['file'] for r in rows if not r['ok']]
    lines.append('')
    lines.append('files=%d pass=%d fail=%d' % (len(rows), len(rows) - len(bad), len(bad)))
    if bad:
        lines.append('FAILED: ' + ', '.join(bad))
    out = '\n'.join(lines)
    print(out)
    wd = os.path.join(HERE, 'work')
    os.makedirs(wd, exist_ok=True)
    stamp = datetime.date.today().strftime('%Y%m%d')
    open(os.path.join(wd, 'guides_check_%s.txt' % stamp), 'w', encoding='utf-8').write(out + '\n')
    print('saved: tools/work/guides_check_%s.txt' % stamp)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
