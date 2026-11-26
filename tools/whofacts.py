#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""whofacts.py — WHO GHO(공식 OData)에서 나라별 담배규제 지표 원자료를 받아 저장.

사람이 숫자를 쓰지 않는다. countryfacts.json 의 rules/tax 값은 전부 여기서 나온다.
원자료를 work/who_raw.json 에 그대로 남긴다(집계 기준이 바뀌어도 API 재호출 불필요).

실행: python tools/whofacts.py          (캐시 있으면 건너뜀)
      python tools/whofacts.py --force  (다시 받기)
"""
import json, os, sys, urllib.request, urllib.error, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
os.makedirs('work', exist_ok=True)
RAW = 'work/who_raw.json'
API = 'https://ghoapi.azureedge.net/api/'

# 우리가 쓰는 지표만. 코드 → (의미 키, 설명)
IND = {
    'P_count_places_sf':        ('smokefree_places',  '국가 금연법이 전면 금연으로 지정한 장소 수(8곳 중)'),
    'W2_pc_front_back_A':       ('warning_pct',        '담뱃갑 주표시면 중 경고 표시 의무 비율(앞뒤 평균, %)'),
    'W10_graphic_A':            ('warning_graphic',    '경고에 사진·그림 포함 의무'),
    'W26_plain_packaging_A':    ('plain_pack',         '무광고 단순포장(plain packaging) 의무'),
    'R_total_tax_estimate':     ('tax_share',          '가장 많이 팔리는 담배 소매가 중 총 세금 비중'),
    'O_Quitline':               ('quitline',           '무료(수신자부담) 금연상담전화 운영'),
    'O_NRT_sold':               ('nrt_sold',           '니코틴 대체요법 합법 판매'),
    'O_NRT_ins':                ('nrt_covered',        '니코틴 대체요법 비용 지원'),
    'E1_nat_tv_radio':          ('ad_tv_radio',        'TV·라디오 담배광고 금지'),
    'E5_billboards':            ('ad_billboard',       '옥외·빌보드 담배광고 금지'),
    'E6_pt_of_sale':            ('ad_pos',             '판매점 내 담배광고 금지'),
    'E7_internet':              ('ad_internet',        '인터넷 담배광고 금지'),
    'E21_vending_machines':     ('vending_ban',        '담배 자판기 전면 금지'),
    'E25_ban_display_pt_of_sale': ('display_ban',      '판매점 담배 진열 금지'),
}

ISO3 = {'AU': 'AUS', 'NZ': 'NZL', 'GB': 'GBR', 'NO': 'NOR', 'FR': 'FRA', 'CA': 'CAN',
        'CH': 'CHE', 'NL': 'NLD', 'DK': 'DNK', 'DE': 'DEU', 'US': 'USA', 'SE': 'SWE',
        'AT': 'AUT', 'IT': 'ITA', 'ES': 'ESP', 'PT': 'PRT', 'AE': 'ARE', 'MX': 'MEX',
        'PL': 'POL', 'JP': 'JPN', 'KR': 'KOR', 'ZA': 'ZAF', 'BR': 'BRA', 'IN': 'IND',
        'PK': 'PAK', 'NG': 'NGA', 'EG': 'EGY', 'RU': 'RUS', 'VN': 'VNM', 'ID': 'IDN',
        'TR': 'TUR'}


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'quitminutes-factbot/1.0 (+https://quitminutes.com)'})
    return json.loads(urllib.request.urlopen(req, timeout=60).read())


def pull():
    want = set(ISO3.values())
    out = {'fetched': datetime.date.today().isoformat(), 'source': API, 'indicators': {}}
    for code, (key, desc) in IND.items():
        try:
            rows = get(API + code)['value']
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            print(f'  {code:28} 실패 {e}')
            out['indicators'][code] = {'key': key, 'desc': desc, 'error': str(e), 'by_country': {}}
            continue
        # 나라별 최신 연도 1건만
        best = {}
        for r in rows:
            cc = r.get('SpatialDim')
            if r.get('SpatialDimType') != 'COUNTRY' or cc not in want:
                continue
            y = r.get('TimeDim') or 0
            if cc not in best or y > best[cc]['year']:
                best[cc] = {'year': y, 'value': r.get('Value'), 'num': r.get('NumericValue')}
        out['indicators'][code] = {'key': key, 'desc': desc, 'by_country': best}
        print(f'  {code:28} {len(best):>2}/31개국  예) KOR={best.get("KOR", {}).get("value")}')
    json.dump(out, open(RAW, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', RAW)


if __name__ == '__main__':
    if os.path.exists(RAW) and '--force' not in sys.argv:
        print(RAW, '이미 있음 (--force 로 다시 받기)')
    else:
        pull()
