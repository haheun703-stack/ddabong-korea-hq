# EP01 실사 10컷 — 인터넷 공개 자료로 대체할 수 있나? (2026-09-13)

> 작성: Claude Code (조사·보고만) · 유료 호출 없음 · 생성 없음 · git 없음 · 이 파일 말고는 고친 파일 없음 · 권리 기록은 만들거나 고치지 않음
> 질문 (사용자): "왜 굳이 현장에 가서 찍나? 인터넷에 사진이 많은데 찾으면 되지 않나?"
> 근거: `08_REAL_FOOTAGE/SHOOT_PLAN_EP01_V01.md`, `15_QA/SHOOT_READINESS_20260913.md`, `07_SHOTS/shot_EP01_*.json` (REAL 10컷 + S08_SH002), `00_SYSTEM/standards/RIGHTS_STANDARD.md`, `05_HISTORY_DATABASE/rights/*.json`
> 크기 표기: **실측** = 원본을 임시 폴더(`$TMP/ddb_full`, 저장소 밖)에 내려받아 픽셀을 직접 읽은 값 · **API** = Commons가 알려준 값 (내려받지 않음)

---

## 결론 먼저

**인터넷 자료만으로 10컷을 모두 채울 수는 없다. 다만 여행을 통째로 없애고 "대부분은 사진, 몇 컷만 포기하거나 바꾸는" 방식은 가능하다.**

- **바로 대체 가능 (REPLACEABLE) 2컷**: S02_SH001 (왕릉군 경관), S09_SH003 (오프닝 구도 반복 — S01_SH002를 사진으로 가면 같은 사진을 다시 쓰면 됨)
- **부분 대체 (PARTIAL) 6컷**: 사진에 느린 줌·팬을 주면 쓸 수는 있지만, 움직임·현장음·정확한 구도, 또는 "천마총 봉분이어야 한다"는 조건 중 하나를 잃는다
- **현장 촬영 필요 (NEEDS_SHOOT) 2컷**: S01_SH001 (현대 경주 거리), S08_SH001 (산책·차량·카페 몽타주) — **움직임과 현장음이 이 컷의 목적 자체**인데, 쓸 수 있는 라이선스의 영상을 찾지 못했다

가장 크게 막히는 점:
1. **쓸 수 있는 영상이 사실상 없다.** Wikimedia Commons에서 경주·대릉원 영상을 검색하면 해당 장소 영상이 나오지 않는다. KTV·공유마당·한국관광콘텐츠랩에서도 공공누리 1유형이 붙은 대릉원 영상을 확인하지 못했다.
2. **GREEN(자유 사용) 사진 중에는 "깨끗한 천마총 봉분 정면" 사진이 없다.** 천마총 봉분이 가장 잘 나온 사진(De-Shao Liu, 6000×4000)은 CC BY-SA 4.0 = **YELLOW**.
3. **경주시 관광 사진은 수익 채널에 쓸 수 없다.** 경주시 사용범위규정에 "개인적, 공익적 용도로 사용이 가능"하다고만 적혀 있다 → 기존 기록 YELLOW를 **RED로 올려야 한다** (아래 §5).
4. **황금시간(석양) 봉분 사진 중 GREEN은 찾지 못했다.** 석양 사진은 CC BY-SA(YELLOW)뿐이다.

---

## 1. 요약 표

| 샷 | 필요 | 가장 좋은 후보 | 라이선스 | 크기 | 판정 |
|---|---|---|---|---|---|
| EP01_S01_SH001 (8초) | 현대 경주 거리, 차·사람이 지나감, 현장음 1초 먼저, 봉분은 안 보이거나 일부만 | 해당 영상 없음. 사진 후보: Hwangnam-dong Gobungun 01 (건물 옆 봉분, 겨울) | PD (PD-self) | 3648×2736 실측 | **NEEDS_SHOOT** |
| EP01_S01_SH002 (10초) | 카페·도로 → 봉분이 드러남(리빌), 사람으로 크기 비교, 끝 프레임 고정 | 대릉원 20160724 01 (소나무 사이로 봉분, 여름) / Hwangnam-dong Gobungun 01 | CC0 / PD | 3264×1836 실측 / 3648×2736 실측 | **PARTIAL** |
| EP01_S02_SH001 (11초) | 대릉원 봉분 무리 경관 3–4컷, 전부 고정 | Daereungwon Tomb Complex (B. Gagnon) / gary4now 2장 / 대릉원 20160724 08 | CC0 / CC BY 3.0 / CC0 | 5018×3345 실측 / 1824×1368 실측 / 3264×1836 실측 | **REPLACEABLE** |
| EP01_S03_SH001 (13초) | 천마총 외관 와이드 → 표지(이름) → 입구 쪽 느린 접근 | 표지·입구: 대릉원 천마총 20160724 155901 (GREEN) · 외관 와이드: 慶州-大陵苑-天馬塚 (YELLOW) | CC0 / CC BY-SA 4.0 | 3264×1836 실측 / 6000×4000 API | **PARTIAL** |
| EP01_S06_SH007 (4초) | 뒤에서 멀리 **천마총 봉분**을 바라봄, H05와 같은 35mm·1.5 m, 느린 접근 | GREEN: 대릉원 20160724 05 (단독 봉분, 어느 고분인지 미확인) · YELLOW: 慶州-大陵苑-天馬塚 | CC0 / CC BY-SA 4.0 | 3264×1836 실측 / 6000×4000 API | **PARTIAL** |
| EP01_S06_SH011 (4초) | 지금의 봉분 + 관람객(작게, 뒷모습) | gary4now (봉분 사이 사람 1명 아주 작게) / Tumuli Park Entrance-02 (정문+관람객, 봉분 없음) | CC BY 3.0 / CC BY 3.0 | 1824×1368 실측 / 3645×2728 실측 | **PARTIAL** |
| EP01_S08_SH001 (15초) | 산책·사진 찍는 사람·차량·카페 몽타주 8–12클립, 현장음 | 해당 영상 없음. 사진: Korea-Gyeongju-Daeneungwon-Tumuli Park-01 (봉분+도로·차량, 겨울, 세로) | CC BY 2.0 | 2304×3072 실측 | **NEEDS_SHOOT** |
| EP01_S08_SH003 (5초) | H07 매치컷 착지. 천마총 봉분, 삼각대 고정, 봉분 약간 오프축, 35mm·1.6 m·tilt 0, 사람 없음, 중간 톤 빛, 초록 풀 | YELLOW: 慶州-大陵苑-天馬塚 (가장 적합) · GREEN: 대릉원 20160724 05 / Daereungwon Tomb Complex | CC BY-SA 4.0 / CC0 / CC0 | 6000×4000 API / 3264×1836 실측 / 5018×3345 실측 | **PARTIAL** (YELLOW 수용 시 REPLACEABLE) |
| EP01_S09_SH003 (6초) | S01_SH002 끝 프레임과 같은 구도, 움직임 0 | S01_SH002에 쓴 **같은 사진** 재사용 | S01_SH002 후보와 같음 | 같음 | **REPLACEABLE** (S01_SH002를 사진으로 갈 때만) |
| EP01_S09_SH004 (11초) | 석양·골든아워 왕릉 히어로 와이드, 옆빛, 사람 없음 | GREEN 석양 없음. YELLOW: Trees surrounded by grassy tumuli at sunset in Daereungwon (B. Morin) · GREEN 대낮 대체: Daereungwon Tomb Complex | CC BY-SA 4.0 / CC0 | 6720×4200 API / 5018×3345 실측 | **PARTIAL** |

**개수: REPLACEABLE 2 · PARTIAL 6 · NEEDS_SHOOT 2**

---

## 2. H07 매치컷 — "사진을 먼저 고르고, AI 그림을 그 사진 구도에 맞춰 만들면 되지 않나?"

**답: 방식 자체는 된다. 오히려 편하다.** 사진이 이미 있으므로 AI 정지 이미지(H07, `EP01_S08_SH002`)를 그 사진의 봉분 윤곽·위치·지평선 높이에 맞춰 만들면 되고, 현장 촬영 뒤로 미룰 이유(D-018 "현장 SH003 착지 구도 촬영 뒤 생성")가 사라진다. S08_SH003 자체가 움직임 0인 고정 컷이라, 사진으로 바꿔도 잃는 것은 풀·구름의 미세한 움직임과 현장음 정도다 (현장음은 따로 깔면 됨).

**하지만 조건을 모두 채우는 GREEN 사진은 없다.** 후보별로 보면:

| 후보 | 봉분 | 수평 | 윤곽 선명도 | 사람 | 해상도 | 계절·빛 | 문제 |
|---|---|---|---|---|---|---|---|
| **慶州-大陵苑-天馬塚.jpg** (De-Shao Liu, 2018-08-27) | **천마총 맞음** (입구에 天馬塚 글자) | 곧음 (정면) | 매우 선명 — 흐린 하늘 배경에 둥근 윤곽 전체 | 없음 | 6000×4000 (API) | 여름, 초록 풀, 흐린 날 중간 톤 빛 → H07의 "neutral daylight"와 잘 맞음 | **CC BY-SA 4.0 = YELLOW.** 봉분이 정가운데 → 오프축으로 만들려면 좌우를 잘라야 함 (6000 폭이라 여유 있음). 앞에 입구 구조물·보도블록 광장 |
| **대릉원 20160724 05.jpg** (Daniel Mietchen, 2016-07-24) | 단독 봉분, **어느 고분인지 미확인** (천마총 입구는 안 보임) | 곧음 | 꼭대기 윤곽은 맑은 하늘 배경에 선명 | 없음 | 3264×1836 실측 (휴대폰 사진) | 여름, 초록 풀, 맑음 | 봉분 아랫부분을 배롱나무·비석·벤치가 가림. 봉분 정가운데. 4K로 크게 쓰기엔 해상도 부족 (1080p는 가능) |
| **Daereungwon Tomb Complex.jpg** (Bernard Gagnon, 2022-10-06) | 봉분 3개가 겹침 | 곧음 | 선명하나 **단독 봉분이 아님** | 없음 | 5018×3345 실측 | 10월 초, 초록 풀, 흐림 | 겹친 봉분이라 "같은 모양의 봉분 하나"로 넘어가는 H07 연출과 다름 |
| Hwangnamdaechong Tomb.jpg (Bernard Gagnon, 2022-10-06) | 황남대총 (쌍봉) | 곧음 | 매우 선명 | 없음 | 4860×3240 실측 | 10월 초, 초록 | **천마총이 아님** (쌍봉 모양), 앞에 연못. D-026 장소 lock (`LOC_CHEONMACHONG_V01`, 지름 47 m / 높이 12.7 m)과 안 맞음 |

선택지:
- **A. YELLOW 수용** → 慶州-大陵苑-天馬塚.jpg 로 S08_SH003 착지 + H07 구도 기준. 가장 깔끔하다. 단, CC BY-SA의 "같은 조건으로 공유" 의무가 편집된 영상에 어떻게 걸리는지 불명확하고 (기존 YELLOW 기록들의 미결 이슈와 같음), **이 사진을 AI 생성의 구도 참고 이미지로 넣으면 H07 그림까지 2차적 저작물 논란이 번질 수 있다.** 참고 이미지로 직접 넣지 말고 "봉분 위치·지평선 높이 수치"만 옮겨 적는 방식을 권한다 (제안).
- **B. GREEN만 사용** → 대릉원 20160724 05.jpg. 천마총이라는 확인이 없으므로 D-026(착지 = 천마총 봉분)과 H07 장소 lock을 느슨하게 바꾸는 결정이 필요하다.
- **C. S08_SH003 한 컷만 현장 촬영** (현재 계획).

---

## 3. 샷별 상세

### EP01_S01_SH001 — 현대 경주 거리 (8초) → NEEDS_SHOOT

- **필요**: 평범한 경주 거리, 차·사람이 지나감 (`human_motion` 30), 현장음이 화면보다 1초 먼저 (`notes`). 봉분은 안 보이거나 일부만.
- **찾은 것**:
  - 경주 거리 영상: Commons 검색("Gyeongju filetype:video", "경주 filetype:video", "Daereungwon filetype:video")에서 **경주 거리 영상 없음**. 걸린 것은 무관한 영상뿐. 공개 도메인인 미 공군 영상 "2025 Korean Security, History, Cultural Immersion Program (968608).webm" (1920×1080, 60초, PD)이 하나 있으나 내용이 경주인지 **확인하지 못함** — 확인할 가치는 낮다.
  - 사진: `File:Hwangnam-dong Gobungun 01.JPG` (Abasaa, 2016-02-21, `{{PD-self}}`, 3648×2736 실측) — 건물 옆에 봉분, **누런 겨울 풀**, 봉분이 크게 보여 "봉분이 안 보이는 거리"라는 목적과 다름. `File:Gyeongju Station platform 4.jpg` (CC0, 4032×3024 API) — 역 승강장, 거리 아님.
- **판정 이유**: 이 컷의 역할은 "움직이는 평범한 일상 + 소리"다. 사진에 줌을 주면 목적이 사라진다. 경주가 아닌 일반 거리 영상(스톡)은 이번 조사 범위의 라이선스(KOGL 1 / CC0 / CC BY)로 확인하지 못했다.

### EP01_S01_SH002 — 카페·도로에서 봉분 리빌 (10초) → PARTIAL

- **필요**: 건물·나무 뒤에서 옆으로 움직여 봉분을 드러냄, 지나가는 사람으로 크기 비교, 끝 프레임 고정. 구도는 S09_SH003에서 다시 씀.
- **후보**:
  1. `File:대릉원 20160724 01.jpg` — Daniel Mietchen, 2016-07-24 14:16, `{{self|cc-zero}}` (CC0), **3264×1836 실측**. 소나무 줄기·가지 사이로 초록 봉분이 보임. 여름. 사진 위를 옆으로 천천히 이동하면 "나무 뒤에서 드러나는" 느낌은 흉내 낼 수 있다.
     <https://commons.wikimedia.org/wiki/File:대릉원_20160724_01.jpg>
  2. `File:Hwangnam-dong Gobungun 01.JPG` — Abasaa, 2016-02-21, `{{PD-self}}`, **3648×2736 실측**. 도로·건물과 봉분이 한 화면 ("현대 + 봉분" 대비). 겨울, 누런 풀.
     <https://commons.wikimedia.org/wiki/File:Hwangnam-dong_Gobungun_01.JPG>
  3. `File:Korea-Gyeongju-Daeneungwon-Tumuli Park-01.jpg` — Kok Leng Yeo (Flickr), 2008-12-24 16:12, `{{cc-by-2.0}}` + Flickr 검토 통과, **2304×3072 실측 (세로)**. 봉분 위에서 내려다본 도로·차·건물과 봉분들. 겨울. 세로라 가로 영상에 쓰려면 크게 잘라야 함.
     <https://commons.wikimedia.org/wiki/File:Korea-Gyeongju-Daeneungwon-Tumuli_Park-01.jpg>
- **잃는 것**: 실제 카메라 이동으로 생기는 원근 변화(가까운 나무와 먼 봉분이 다르게 움직이는 효과), 크기 비교용 사람, 카페/도로 현장음. 후보 1은 여름·초록, 후보 2·3은 겨울·누런 풀이라 **섞어 쓰면 계절이 튄다.**

### EP01_S02_SH001 — 대릉원 봉분 무리 경관 3–4컷 (11초) → REPLACEABLE

- **필요**: 넓은 봉분 무리, 망원으로 겹친 봉분, 하늘 배경 낮은 앵글. 전부 고정 (`human_motion` 10). 월성·사찰은 선택 (D-026).
- **후보**:
  1. `File:Daereungwon Tomb Complex.jpg` — Bernard Gagnon, 2022-10-06, `{{self|cc-zero}}` (CC0), **5018×3345 실측**. 봉분 3개가 겹친 초록 경관, 흐린 하늘. 4K에서도 잘라 쓸 여유 있음.
     <https://commons.wikimedia.org/wiki/File:Daereungwon_Tomb_Complex.jpg>
  2. `File:Gyeongju National Park, Korea - panoramio - gary4now.jpg` — gary4now (Panoramio), 2010-08-26, `{{cc-by-3.0|gary4now}}` + Panoramio 검토 통과, **1824×1368 실측**. 초록 들판 위 봉분 3개 + 뒤로 겹겹이 산. 경관은 가장 아름답지만 **폭 1824라 1080p 화면(1920)보다 작다** → 약간 확대 필요, 4K 불가. 같은 작가의 `... gary4now (1).jpg` (1824×1368 실측, CC BY 3.0) = 산책로 옆 겹친 봉분, 여름 초록.
     <https://commons.wikimedia.org/wiki/File:Gyeongju_National_Park,_Korea_-_panoramio_-_gary4now.jpg>
  3. `File:대릉원 20160724 08.jpg` — Daniel Mietchen, 2016-07-24 14:32, CC0, **3264×1836 실측**. 두 봉분 사이 골짜기, 여름.
     <https://commons.wikimedia.org/wiki/File:대릉원_20160724_08.jpg>
  - 참고 GREEN: `File:Hwangnamdaechong Tomb.jpg` (Bernard Gagnon, CC0, 4860×3240 실측, 10월, 연못 앞 쌍봉).
- **판정 이유**: 원래 고정 컷이라 사진 + 아주 느린 줌으로 거의 같은 효과. 계절은 7–10월 초록으로 맞출 수 있다. CC BY 사진은 화면이나 설명란에 출처 표시 필요.

### EP01_S03_SH001 — 천마총 외관·표지·입구 (13초) → PARTIAL

- **필요**: 외관 와이드 → 표지(이름) 클로즈업 → 입구 쪽 느린 접근.
- **후보**:
  1. (표지·입구, GREEN) `File:대릉원 천마총 20160724 155901.jpg` — Daniel Mietchen, 2016-07-24 15:59, CC0, **3264×1836 실측**. 설명: "The entrance to the Cheonmachong tomb, displaying the Chinese letters 天馬塚." 天馬塚 석판 + 입구 + 위로 봉분 꼭대기. 여름, 파란 하늘.
     <https://commons.wikimedia.org/wiki/File:대릉원_천마총_20160724_155901.jpg>
  2. (외관 와이드, YELLOW) `File:慶州-大陵苑-天馬塚.jpg` — De-Shao Liu (Terry850324), 2018-08-27, CC BY-SA 4.0, **6000×4000 (API, 미측정)**. 천마총 봉분 정면 전체 + 입구. 흐림, 초록.
     <https://commons.wikimedia.org/wiki/File:慶州-大陵苑-天馬塚.jpg>
  3. (외관 와이드, YELLOW) `File:천마총.jpg` — Symtux, CC BY-SA 4.0, **4000×3000 (API)**. 맑은 날 봉분 정면, 해가 화면 안에 들어와 역광.
  - GREEN 외관 와이드 후보 `File:Heavenlyhorsetomb1.jpg` (NW-Photos.com, CC BY 2.0)는 **761×567 실측** — 영상에 쓰기엔 너무 작고, 4월 앙상한 나무·누런 풀.
- **잃는 것**: 입구 쪽 실제 접근 움직임 (줌으로 대신). GREEN만 쓰면 외관 와이드가 비고, 와이드를 채우려면 YELLOW가 필요. 천마총 내부는 어느 쪽이든 해당 없음.

### EP01_S06_SH007 — H05 시선을 이어받아 멀리 천마총 봉분 보기 (4초) → PARTIAL

- **필요**: H05와 같은 방향·눈높이 (35mm · 1.5 m), 매우 느린 접근 또는 고정. D-026: 대상 = 천마총 봉분.
- **후보**: 위 §2 표와 같음 — YELLOW `慶州-大陵苑-天馬塚.jpg` (천마총 확실), GREEN `대릉원 20160724 05.jpg` (CC0, 3264×1836 실측, 어느 고분인지 미확인).
  <https://commons.wikimedia.org/wiki/File:대릉원_20160724_05.jpg> — 페이지 원문: "This file is made available under the Creative Commons CC0 1.0 Universal Public Domain Dedication."
- **잃는 것**: 4초짜리 짧은 컷이라 사진 + 느린 줌이면 화면상 차이는 작다. 문제는 "천마총이어야 한다"는 조건 — GREEN으로는 확인 불가. 그리고 H05가 아직 생성 전이라, 사진을 먼저 고르면 **H05도 그 사진 방향에 맞춰 만들어야** 한다 (가능하고 오히려 쉬움).

### EP01_S06_SH011 — 지금의 봉분과 관람객 (4초) → PARTIAL

- **필요**: 와이드, 관람객은 작게·뒷모습 (`human_motion` 20), 얼굴 식별 불필요.
- **후보**:
  1. `File:Gyeongju National Park, Korea - panoramio - gary4now.jpg` — CC BY 3.0, 1824×1368 실측. 두 봉분 사이 멀리 사람 1명이 **아주 작게** 보임. 여름.
  2. `File:Korea-Gyeongju-Tumuli Park-Entrance-02.jpg` — Grete Howard (Flickr), 2008-10-11, `{{cc-by-3.0}}`, **3645×2728 실측**. 대릉원 정문을 걸어 들어가는 관람객 뒷모습. **봉분은 안 보임**. 가을. Commons 페이지에 Flickr 라이선스 검토 표시가 **없어서** 원본 Flickr 페이지 확인이 추가로 필요.
     <https://commons.wikimedia.org/wiki/File:Korea-Gyeongju-Tumuli_Park-Entrance-02.jpg>
- **잃는 것**: 움직이는 사람 (이 컷의 뜻 = "지금도 사람들이 이 봉분을 본다"). "봉분 + 관람객이 한 화면에 잘 보이는" GREEN 사진은 찾지 못했다.

### EP01_S08_SH001 — 산책·사진·차량·카페 몽타주 (15초) → NEEDS_SHOOT

- **필요**: 8–12개 클립 × 8–15초, 대부분 고정·가끔 느린 이동, **현장음을 다시 앞으로** (`human_motion` 40, 10컷 중 가장 높음).
- **찾은 것**: 해당 장소 영상 없음 (S01_SH001과 같은 검색 결과). 사진 후보 `Korea-Gyeongju-Daeneungwon-Tumuli Park-01.jpg` (CC BY 2.0, 2304×3072 실측, 봉분 너머 도로·차량, 겨울, 세로), `Tumuli Park Entrance-02.jpg` (관람객), `Hwangnam-dong Gobungun 01.JPG` (도로·건물).
- **판정 이유**: 사진 몇 장으로 15초 몽타주를 만들면 슬라이드쇼로 보이고, 사진마다 계절(겨울 누런 풀 / 가을 / 여름)이 달라 이어 붙이기 어렵다. 현장음도 없다.

### EP01_S08_SH003 — H07 매치컷 착지 (5초) → PARTIAL (YELLOW 수용 시 REPLACEABLE)

- **필요**: §2 참고. 천마총 봉분, 삼각대 고정, 봉분 약간 오프축, 35mm · 1.6 m · tilt 0, 사람 없음, 중간 톤 자연광, 초록 풀 (H07 프롬프트 "same-shaped green mound").
- **후보·평가**: §2 표. 가장 적합한 사진은 YELLOW (`慶州-大陵苑-天馬塚.jpg`), GREEN은 천마총 확인이 없거나 단독 봉분이 아님.
- **참고**: 사진으로 가면 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame` 값은 "촬영 기록" 대신 **사진에서 잰 값**(봉분 꼭대기·좌우 끝의 화면 % 위치, 지평선 높이 %)으로 채우게 된다. 렌즈·높이·방위각은 사진에서 정확히 알 수 없다 (EXIF가 없으면 추정).

### EP01_S09_SH003 — 오프닝 구도 반복 (6초) → REPLACEABLE (조건부)

- **필요**: S01_SH002 끝 프레임과 같은 위치·렌즈·높이, 움직임 0.
- **판정 이유**: S01_SH002를 사진으로 가면, 같은 사진을 그대로 다시 쓰면 되므로 **구도가 오히려 완벽하게 일치**한다. 계획서의 "엔딩은 늦은 오후 빛" 제안은 색보정으로 흉내만 가능. 반대로 **S01_SH002를 현장에서 찍으면 이 컷도 반드시 같은 자리에서 찍어야 한다** (둘을 따로 결정할 수 없음).

### EP01_S09_SH004 — 석양·골든아워 왕릉 히어로 와이드 (11초) → PARTIAL

- **필요**: 옆에서 빛이 드는 넓은 봉분 와이드, 망원 겹친 봉분 1컷, 사람 없음 (엔딩 여운).
- **후보**:
  1. (YELLOW) `File:Trees surrounded by grassy tumuli at sunset in Daereungwon Tomb Complex of Gyeongju ...` — Basile Morin, CC BY-SA 4.0, **6720×4200 (API)**. 제목상 대릉원 석양. **썸네일은 열어보지 못함** — 사용 전 확인 필요.
  2. (YELLOW, 부적합) `File:Sunset over the Tumuli Park in Gyeongju Historic Site Wolseong District South Korea.jpg` — Basile Morin, CC BY-SA 4.0, 6720×4085 (API). 썸네일 확인 결과 **봉분이 거의 안 보이는 발굴지·산 풍경** → 이 컷에는 맞지 않음.
  3. (GREEN, 대낮) `File:Daereungwon Tomb Complex.jpg` — CC0, 5018×3345 실측. 흐린 낮. 색보정으로 따뜻하게 만들 수는 있으나 "옆빛 석양"은 되지 않는다.
  - 참고: `File:Korea-Gyeongju-Daeneungwon-Tumuli Park-01.jpg` (CC BY 2.0, 16:12 겨울 오후 따뜻한 빛, 세로, 도로·차량 포함) — 사람·차가 없어야 하는 조건과 맞지 않음.
- **잃는 것**: GREEN으로는 석양 빛 없음. 11초짜리 엔딩이라 사진이 오래 머물면 정지 화면 느낌이 강하다.

---

## 4. 확인한 출처별 결과 (찾지 못한 것도 기록)

| 출처 | 결과 | 라이선스 판정 |
|---|---|---|
| **Wikimedia Commons** (분류: Cheonmachong, Daereungwon, Hwangnam daechong, Nodong-ri tombs, Noseo-ri tombs, Gyeongju Historic Areas + 검색) | 사진은 많음. 그러나 대부분 **CC BY-SA** (riNux 2006, Christophe95 2018, De-Shao Liu 2018, hyolee2 2015, Heera7 2019, Basile Morin 2024 등 = YELLOW). GREEN은 Daniel Mietchen 2016 (CC0, 휴대폰 3264×1836), Bernard Gagnon 2022 (CC0, 고해상도 3장), yeowatzup / Kok Leng Yeo 2008 겨울 (CC BY 2.0), gary4now 2010 (CC BY 3.0, 1824 폭), Abasaa 2016 겨울 (PD), Grete Howard 2008 (CC BY 3.0). **경주·대릉원 영상 없음, 현장음 없음.** | 파일마다 다름 |
| **한국관광공사 포토코리아** (phoko.visitkorea.or.kr) | "Gyeongju Daereungwon Ancient Tomb Complex" 검색 결과 **178건**. 이용약관에 1–4유형 설명 있음 (1유형 = 상업 사용·변경 가능, 2유형 = 상업 금지 등). 그러나 **목록에 항목별 유형 표시가 보이지 않고, 다운로드는 회원가입·로그인 필요**. 약관에 "Downloaded photos may not be distributed to 3rd party without the consent of KTO" 문구가 있어 영상 안에 넣는 것이 이 조항에 걸리는지도 확인 필요. | **BLUE (확인 중)** — 로그인해서 항목별 유형을 봐야 함. 가장 유망한 추가 출처 |
| 한국관광콘텐츠랩 (api.visitkorea.or.kr) | 공공데이터포털 소개에 "공공누리 1유형", "이용허락범위 제한 없음". 사이트가 자바스크립트로만 열려 **대릉원 사진·영상 항목을 직접 확인하지 못함**. | BLUE |
| **경주시 관광자원 영상이미지** (gyeongju.go.kr/gyeongjuimage) | 사용범위규정 원문: "이 사진자료는 경주시가 저작권을 갖고 있으며, 사진자료 사용 시 출처(경주시)를 분명히 기재하셔야 합니다." / "사진 다운로드 시 개인적, 공익적 용도로 사용이 가능하며" / 하단 "Copyright(C) 2019 경주시 관광자원 영상이미지. All rights reserved." 공공누리 표시 없음. | **RED** (수익 채널 = 개인·공익 용도 아님) |
| KTV / e영상역사관 | KTV 안내: 공공누리 표시가 없는 자료는 한국정책방송원과 사전 협의 후 사용. 대릉원·천마총 영상 중 공공누리 표시가 붙은 것을 **찾지 못함** (e영상역사관 검색 주소는 404). | 해당 없음 |
| 공유마당 (gongu.copyright.or.kr) | 검색 결과 페이지가 "콘텐츠 준비중"으로 열림. 검색엔진으로는 천마도(어문 항목)만 확인, **대릉원 사진·영상 확인 못함**. | 해당 없음 |
| 국가유산청 / 국가유산포털 | Commons에 올라온 국가유산청 KOGL 1유형 사진은 `경주 봉황대.jpg` (857×571 실측, 너무 작음)뿐. 2023 천마총 50주년 사진공모전 수상작은 공개 라이선스 확인 없음. | 봉황대 사진 GREEN이나 크기 부족 |
| Korea.net | 이번 조사에서 대릉원 항목을 찾지 못함 (CC BY-SA가 많아 어차피 YELLOW). | — |

**현장 참고 (촬영을 할 경우)**: 검색 중 확인 — 2026-09-04 ~ 09-27 매일 19:30부터 "국가유산 미디어아트 경주 대릉원"이 열려 미추왕릉·황남대총·천마총·90호분에 영상을 비춘다 (경북일보 기사). 이 기간에 가면 저녁 컷(S09_SH004 늦은 시간, 선택 야간 컷)에 조명·인파가 섞일 수 있다. 뉴스 사진·영상은 RED이므로 자료로는 쓰지 않는다.

---

## 5. 사용자 결정 필요

1. **여행을 할지 말지**
   - **안 A — 여행 취소, 사진으로 전환**: REPLACEABLE 2 + PARTIAL 6은 사진으로 채우고, NEEDS_SHOOT 2컷(S01_SH001, S08_SH001)은 대본에서 빼거나 다른 방식으로 바꾼다. 오프닝(0:00–0:18)과 6:05–6:20 몽타주가 "움직임·현장음 없는 사진"이 되므로 **"현대 경주가 살아 움직인다"는 대비 효과가 크게 약해진다.**
   - **안 B — 짧은 촬영만**: NEEDS_SHOOT 2컷 + 계획상 가장 중요한 S08_SH003(매치컷 착지)·S01_SH002/S09_SH003(오프닝·엔딩 반복)만 찍고, S02_SH001 · S03_SH001(표지) · S06_SH007 · S06_SH011 · S09_SH004는 사진으로 대신 채우거나 백업으로 둔다. 촬영 시간이 크게 줄고 골든아워까지 기다릴 필요가 없어진다.
   - **안 C — 원래 계획대로 전부 촬영**, 사진은 백업.
2. **CC BY-SA(YELLOW)를 받아들일지** — 받아들이면 S03_SH001 외관 와이드, S06_SH007, S08_SH003, S09_SH004가 훨씬 좋아진다 (특히 천마총 정면 `慶州-大陵苑-天馬塚.jpg`). 기존 기록 두 건의 미결 이슈("Share-Alike 의무 수용 여부 결정 필요")와 같은 결정이다.
3. **H07 순서를 뒤집을지** (사진 먼저 → AI 그림을 사진에 맞춤). 뒤집으면 D-018의 "SH003 실사 구도 확보 뒤 생성" 문구를 바꾸는 결정이 필요하다. GREEN만 쓸 경우 D-026 "착지 = 천마총 봉분"도 느슨하게 바꿔야 한다.
4. **포토코리아 로그인 확인을 할지** — 사용자가 회원 가입 후 대릉원 178건의 유형을 확인하면 GREEN(1유형) 고해상도 사진·석양 사진이 나올 가능성이 있다. 조사 에이전트는 로그인할 수 없다.
5. **계절 통일** — 사진으로 가면 여름~초가을 초록 사진(Mietchen 7월, gary4now 8월, Gagnon 10월 초)으로만 통일하고, 겨울 사진(yeowatzup, Kok Leng Yeo, Abasaa)은 섞지 않기를 권한다. H07 프롬프트가 "green mound"이므로 초록 쪽이 맞다.

---

## 6. 권리 기록 변경 제안 (만들지도 고치지도 않음 — 승인 후 별도 작업)

**기존 기록 수정 제안**
- `RTS_GYEONGJU_CITY_IMAGE_001`: `status` YELLOW → **RED**, `commercial_use` UNKNOWN → NO. 근거: 사용범위규정 원문 "사진 다운로드 시 개인적, 공익적 용도로 사용이 가능하며" + "All rights reserved". `proof`에 `https://www.gyeongju.go.kr/gyeongjuimage/page.do?mnu_uid=2409` 저장본 추가.
- `RTS_WIKI_DAEREUNGWON_001`, `RTS_WIKI_CHEONMACHONG_ENTRANCE_001`: 변경 없음 (YELLOW 유지). 다만 CHEONMACHONG_ENTRANCE는 800×600이라 영상용으로 작다 — 천마총 백업을 `慶州-大陵苑-天馬塚.jpg`(6000×4000)로 바꾸는 것을 검토.

**새 기록 후보 (GREEN — 기존 GNM 기록처럼 `proof`에 페이지 저장본 필요)**

| 제안 rights_id | 파일 (Commons) | 작가 | 라이선스 | 실측 크기 | 쓰일 샷 |
|---|---|---|---|---|---|
| RTS_WIKI_DAEREUNGWON_GAGNON_2022_001 | Daereungwon Tomb Complex.jpg | Bernard Gagnon | CC0 1.0 | 5018×3345 | S02_SH001, S09_SH004(대낮 대체), S08_SH003(대체) |
| RTS_WIKI_HWANGNAMDAECHONG_GAGNON_2022_001 | Hwangnamdaechong Tomb.jpg | Bernard Gagnon | CC0 1.0 | 4860×3240 | S02_SH001 |
| RTS_WIKI_DAEREUNGWON_MIETCHEN_2016_01 / _05 / _08 | 대릉원 20160724 01 / 05 / 08.jpg | Daniel Mietchen | CC0 1.0 | 각 3264×1836 | S01_SH002·S09_SH003 / S06_SH007·S08_SH003 / S02_SH001 |
| RTS_WIKI_CHEONMACHONG_SIGN_MIETCHEN_2016_001 | 대릉원 천마총 20160724 155901.jpg | Daniel Mietchen | CC0 1.0 | 3264×1836 | S03_SH001 |
| RTS_WIKI_GYEONGJU_GARY4NOW_2010_001 / _002 | Gyeongju National Park, Korea - panoramio - gary4now.jpg / (1).jpg | gary4now | CC BY 3.0 (출처 표시) | 각 1824×1368 | S02_SH001, S06_SH011 |
| RTS_WIKI_HWANGNAMDONG_ABASAA_2016_001 | Hwangnam-dong Gobungun 01.JPG | Abasaa | PD (PD-self) | 3648×2736 | S01_SH002 (겨울) |
| RTS_WIKI_NOSEODONG_KOKLENGYEO_2008_001 | Korea-Gyeongju-Daeneungwon-Tumuli Park-01.jpg | Kok Leng Yeo | CC BY 2.0 (출처 표시) | 2304×3072 | S01_SH002 / S08_SH001 (겨울) |
| RTS_WIKI_TUMULI_ENTRANCE_HOWARD_2008_001 | Korea-Gyeongju-Tumuli Park-Entrance-02.jpg | Grete Howard | CC BY 3.0 — **Flickr 원본 라이선스 재확인 필요 (Commons 검토 표시 없음)** | 3645×2728 | S06_SH011 |

**새 기록 후보 (YELLOW — Share-Alike 결정 뒤에만)**
- 慶州-大陵苑-天馬塚.jpg (De-Shao Liu, CC BY-SA 4.0, 6000×4000 API) — S03_SH001 외관, S06_SH007, S08_SH003
- Trees surrounded by grassy tumuli at sunset in Daereungwon ... (Basile Morin, CC BY-SA 4.0, 6720×4200 API) — S09_SH004, **내용 확인 먼저**

**BLUE (확인 중)**: 포토코리아 대릉원 178건 — 로그인 후 항목별 공공누리 유형 확인.

CC BY 출처 표시 문구 예 (제안): "Photo: gary4now, CC BY 3.0, via Wikimedia Commons". CC0·PD는 표시 의무가 없지만 기록에는 작가·URL을 남긴다.
