#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""buildfacts.py — countryfacts.json 생성 (사람이 사실을 쓰지 않는다).

입력
  work/who_raw.json   WHO GHO 공식 지표 원자료 (whofacts.py)
  govsources.json     나라별 공식 페이지 후보 URL
  quitdata.json       금연상담전화 번호
출력
  countryfacts.json   autopages.py 가 읽는 나라별 사실
  work/gov_probe.json 공식 페이지 실측 결과 원자료(상태코드·최종URL·키워드 적중)

규칙
  - 확인 못 한 값은 null. 템플릿은 null 이면 그 문장을 만들지 않는다.
  - 2022년(WHO 2023 보고서) 지표만 현재 규제로 쓴다. 2014년치 지표는 낡아서 버린다.
  - 공식 페이지는 200 + 담배/금연 키워드 적중까지 통과해야 sources 에 들어간다.
  - 상담전화 번호는 그 나라 공식 페이지 본문에서 숫자가 확인되면 verified=true 로 표시한다.

실행: python tools/buildfacts.py [--force-probe]
"""
import json, os, re, sys, datetime, urllib.request, urllib.error, ssl

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
TODAY = datetime.date.today().isoformat()
PROBE = 'work/gov_probe.json'
UA = 'Mozilla/5.0 (compatible; quitminutes-factbot/1.0; +https://quitminutes.com)'

# 담배·금연 관련 페이지임을 확인하는 키워드(언어별). 하나라도 있으면 통과.
KW = ['tobacco', 'smoking', 'smoke-free', 'quit', 'cigarette', 'vaping', 'nicotine',
      '금연', '담배', '禁煙', 'たばこ', 'タバコ', 'tabac', 'tabak', 'tabaco', 'tabacco',
      'rauch', 'røyk', 'snus', 'tutun', 'tütün', 'sigara', 'курен', 'табак', 'сигарет',
      'thuốc lá', 'merokok', 'rokok', 'tembakau', 'tabagismo', 'fumo', 'roken',
      'تبغ', 'التدخين', 'palenie', 'papieros']

WHO_YEAR_OK = {2020, 2022}          # 2014년치는 쓰지 않는다
# 둘 다 2026-11-26 실측 200. 앞쪽은 실제 데이터 엔드포인트, 뒤쪽은 WHO 담배 팩트시트.
CITE = [('https://ghoapi.azureedge.net/api/W26_plain_packaging_A',
         'WHO Global Health Observatory - tobacco control indicator API (MPOWER series)'),
        ('https://www.who.int/news-room/fact-sheets/detail/tobacco',
         'WHO fact sheet - Tobacco')]


def fetch(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE          # 일부 정부 사이트 체인 불량 — 존재 확인 목적
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en,ko;q=0.8'})
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            body = r.read(400_000)
            enc = r.headers.get_content_charset() or 'utf-8'
            return r.status, r.geturl(), body.decode(enc, 'replace')
    except urllib.error.HTTPError as e:
        return e.code, url, ''
    except Exception as e:                   # DNS·TLS·타임아웃 전부 실패로 기록
        return 0, url, f'__ERR__{type(e).__name__}: {e}'


def probe_gov(gov, phones):
    """후보 URL 을 순서대로 실제 GET. 200 + 담배/금연 키워드 통과한 첫 URL 만 채택."""
    if os.path.exists(PROBE) and '--force-probe' not in sys.argv:
        return json.load(open(PROBE, encoding='utf-8'))
    out = {}
    for cc, v in gov.items():
        if cc.startswith('_'):
            continue
        title, urls = v['title'], v['urls']
        tried = []
        rec = None
        for url in urls:
            status, final, text = fetch(url)
            low = text.lower()
            hit = [k for k in KW if k in low]
            tried.append({'url': url, 'status': status, 'kw': len(hit),
                          'err': text[9:120] if text.startswith('__ERR__') else ''})
            tel = phones.get(cc)
            tel_ok = False
            if tel:
                digits = re.sub(r'\D', '', tel)
                page_digits = re.sub(r'\D', '', re.sub(r'<[^>]+>', ' ', text))
                tel_ok = len(digits) >= 4 and digits in page_digits
            if status == 200 and hit:
                rec = {'url': url, 'final': final, 'title': title, 'status': status,
                       'kw': hit[:4], 'ok': True, 'tel_verified': tel_ok, 'fetched': TODAY}
                break
        if rec is None:
            rec = {'url': urls[0], 'final': urls[0], 'title': title,
                   'status': tried[-1]['status'] if tried else 0, 'kw': [], 'ok': False,
                   'tel_verified': False, 'fetched': TODAY}
        rec['tried'] = tried
        out[cc] = rec
        mark = 'OK ' if rec['ok'] else 'FAIL'
        print(f"  {cc} {mark} {rec['status']:>3} kw={len(rec['kw']):>2} tel={'Y' if rec['tel_verified'] else '-'} {rec['url'][:58]}")
    json.dump(out, open(PROBE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out


def main():
    raw = json.load(open('work/who_raw.json', encoding='utf-8'))
    gov = json.load(open('govsources.json', encoding='utf-8'))
    phones = {c: v[1] for c, v in json.load(open('quitdata.json', encoding='utf-8'))['q'].items() if v and len(v) > 1}
    iso = json.load(open('work/who_iso3.json', encoding='utf-8')) if os.path.exists('work/who_iso3.json') else None
    if iso is None:
        sys.path.insert(0, HERE)
        from whofacts import ISO3 as iso

    print('공식 페이지 실측…')
    gp = probe_gov(gov, phones)

    def who(cc, key):
        """WHO 지표값 — 연도 기준 통과한 것만. (값, 연도) 또는 (None, None)"""
        for code, blk in raw['indicators'].items():
            if blk['key'] != key:
                continue
            r = blk.get('by_country', {}).get(iso[cc])
            if not r or r['year'] not in WHO_YEAR_OK:
                return None, None
            return r['value'], r['year']
        return None, None

    def num(v):
        """'Not specified' 같은 비수치 응답은 미확인(None)으로 버린다."""
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    def yn(v):
        return None if v is None else (True if str(v).strip().lower() == 'yes' else
                                       False if str(v).strip().lower() == 'no' else str(v))

    facts = {'_meta': {'built': TODAY,
                       'who_fetched': raw['fetched'],
                       'who_note': 'rules/tax 값은 WHO GHO 지표 원본. 연도는 각 항목 year 에 있다.',
                       'policy': '확인 못 한 항목은 null — 페이지에서 해당 문장을 만들지 않는다.'}}

    for cc in iso:
        sf, sf_y = who(cc, 'smokefree_places')
        wp, wp_y = who(cc, 'warning_pct')
        wg, wg_y = who(cc, 'warning_graphic')
        pp, pp_y = who(cc, 'plain_pack')
        tx, tx_y = who(cc, 'tax_share')
        ql, ql_y = who(cc, 'quitline')
        ns, ns_y = who(cc, 'nrt_sold')
        ni, ni_y = who(cc, 'nrt_covered')
        a1, a1_y = who(cc, 'ad_tv_radio')
        a2, a2_y = who(cc, 'ad_billboard')
        a3, a3_y = who(cc, 'ad_internet')

        g = gp.get(cc, {})
        sources = [{'url': u, 'title': t, 'fetched': raw['fetched'],
                    'quote': 'WHO Global Health Observatory indicator values for this country (MPOWER series).'}
                   for u, t in CITE]
        if g.get('ok'):
            sources.insert(0, {'url': g['final'] or g['url'], 'title': g['title'],
                               'fetched': g['fetched'], 'own_country_official': True,
                               'quote': f"official page, HTTP 200, tobacco/quit keywords found: {', '.join(g['kw'])}"})

        facts[cc] = {
            'checked': TODAY,
            'rules': {
                'smokefree_places': (None if num(sf) is None else {'value': int(num(sf)), 'of': 8, 'year': sf_y}),
                'warning_pct': (None if num(wp) is None else {'value': num(wp), 'year': wp_y}),
                'warning_graphic': None if wg is None else {'value': yn(wg), 'year': wg_y},
                'plain_pack': None if pp is None else {'value': yn(pp), 'year': pp_y},
                'ad_tv_radio': None if a1 is None else {'value': yn(a1), 'year': a1_y},
                'ad_billboard': None if a2 is None else {'value': yn(a2), 'year': a2_y},
                'ad_internet': None if a3 is None else {'value': yn(a3), 'year': a3_y},
                'age_limit': None,                 # 미확인 — 공식 출처 확보 후 채운다
                'retail_license': None,
            },
            'help': {
                'quitline': phones.get(cc),
                'quitline_verified_on_official_page': bool(g.get('tel_verified')),
                'quitline_who': None if ql is None else {'value': yn(ql), 'year': ql_y},
                'nrt_sold': None if ns is None else {'value': yn(ns), 'year': ns_y},
                'nrt_cost_covered': None if ni is None else {'value': yn(ni), 'year': ni_y},
                'official_page': ({'url': g['final'] or g['url'], 'title': g['title']} if g.get('ok') else None),
                'free_meds': None,
                'cost_to_user': None,
                'programs': None,
            },
            'price_history': [],                   # 회차 2 — 국가별 공식 세제자료 확인 후
            'tax_share_pct': (None if num(tx) is None else round(num(tx) * 100, 1)),
            'tax_share_year': tx_y,
            'sources': sources,
        }

    json.dump(facts, open('countryfacts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n2 = sum(1 for c, v in facts.items() if not c.startswith('_') and len(v['sources']) >= 2)
    tel = sum(1 for c, v in facts.items() if not c.startswith('_') and v['help']['quitline_verified_on_official_page'])
    print(f"\ncountryfacts.json  {len(facts)-1}개국 · sources>=2 {n2}개국 · 상담전화 공식페이지 확인 {tel}개국")


if __name__ == '__main__':
    main()
