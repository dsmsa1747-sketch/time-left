# QuitMinutes 생성기 (무인 루프의 심장)

사람이 글을 쓰지 않는다. 데이터에서 페이지·카피·영상이 자동으로 나온다.
이 폴더가 저장소에 있으면 세션이 바뀌어도 누구나 같은 결과를 재생산할 수 있다.

## 파일
- `genpages.py`   — 기본 6페이지(about/timeline/prices/quitlines/privacy/terms) 생성. 디자인 단일 소스.
- `autopages.py`  — 국가별 페이지 31개 + prices 링크 주입 + sitemap 재생성 + sw 캐시 버전 +1
- `contentbank.py` — 발행 큐(contentbank.json) 생성. 국가×앵글×언어 조합. 풀링3:키1, 하루 2개 슬롯.
- `render.py`     — 1080x1920 세로 영상 렌더. 데이터 타이포그래피, 카운트업, ease-in-out 줌.
- `countries.json` / `world.json` / `quitdata.json` — 원천 데이터. 담뱃값이 바뀌면 여기만 고친다.

## 실행 순서 (저장소 루트에서)
```
python tools/genpages.py      # dist/ 6페이지
python tools/autopages.py     # dist/ 국가 31페이지 + sitemap 38 + sw 버전업
python tools/contentbank.py   # contentbank.json (172개)
python tools/render.py 0 172  # out/*.mp4  (약 13초/개)
```
※ `autopages.py`는 sitemap에 https://quitminutes.com 을 직접 쓴다.
  `__SITE__` 자리표시자를 쓰지 않으므로 setup.py를 따로 돌릴 필요가 없다.

## render.py 필요 패키지
`pip install pillow numpy` + 시스템에 `ffmpeg`, 폰트 `fonts-noto-cjk`.
윈도우면 Noto Sans/Serif CJK KR 경로를 render.py 상단 SERIF/SANS/BLACK 에서 바꿔준다.

## 담뱃값이 바뀌면
`world.json` 의 usd/local/per 만 고치고 `autopages.py` → `contentbank.py` → `render.py` 순으로 다시 돌린다.
31개 페이지, 172개 카피, 172개 영상이 전부 새 숫자로 다시 만들어진다.

## 경고그림
제5기 만료 2026-12-22 → 제6기 이미지로 `warn5.json` 교체 필요.

---

# QuitMinutes 카드뉴스 (제작비 $0 · 무한 재생성)

- `cards/<id>/01..05.png` — 1080×1350. 인스타 피드·캐러셀, 스레드, 페이스북
- `pins/<id>.png` — 1000×1500. 핀터레스트 2:3
- `<id>` 는 `q/contentbank.json` 의 항목 id 와 같다 → 캡션·해시태그·링크를 그대로 재사용

43세트(영어 31 / 한국어 12) · 카드 215장 · 핀 43장.
담뱃값이 바뀌면 `tools/world.json` 만 고치고 `python cards.py 0 43` 재실행하면 전부 새 숫자로 다시 나온다.

필요 패키지: pillow, numpy / 폰트: fonts-noto-cjk, fonts-noto-color-emoji
