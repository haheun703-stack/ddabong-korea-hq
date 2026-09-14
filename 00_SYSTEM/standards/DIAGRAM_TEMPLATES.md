# DIAGRAM_TEMPLATES — 파이프라인 B: 3D 도해 템플릿 4종 (GT-01 ~ GT-04)

> 문서 버전 **v0.1 ACTIVE** (2026-09-14, Claude Code · **ACTIVE 승격 D-035 #8**) · 근거: D-033 #1 #5 · 벤치마크 `BENCHMARK_ARCHDICT_GYEONGHOERU_20260914.md` (화면 55% 가 단면·오버헤드·치수선·X 표시)
> 관계: 에피소드별 `GRAPHICS_SPEC_*` 의 G 항목이 여기 GT 템플릿을 **인용**한다 (예: EP01 G04 = GT-01 적용). legacy `episodes/ep01-graphics-spec.html` 은 수정하지 않는다.
> 공통 규격은 `GRAPHICS_SPEC_EP01_V2.md` §1.2 (4K · safe area · 브랜드 색 · 8–12프레임 페이드) 를 그대로 따른다. 렌더는 `BLENDER_STANDARD.md`.

---

## 공통 규칙

- 도해는 **③ FACT · ④ CONTEXT** 단계에서만 주인공이다 (STORY_ENGINE_STANDARD §2). ⑤⑥ 에서는 인물 컷의 보조.
- 모든 숫자는 `fact_id` 와 함께. 화면 숫자 = fact 값 그대로 (반올림 시 표기 "≈").
- 박물관·기관 도면 트레이싱 금지. fact 로 새로 그린다 (HISTORY_ACCURACY).
- 치수선·강조 색: **DDABONG Red `#E10612`** 하나만. 물·지반 등 재질 색은 VISUAL_STYLE_BIBLE.
- 한 화면 핵심 문구 3–7 단어, 영어 우선 (외국인 시청자).

## GT-01 · 단면 컷어웨이 (Cross-section cutaway)

| 항목 | 값 |
|---|---|
| 용도 | 구조·지반·층위 설명. "겉은 흙, 안은 무엇" |
| 구성 | 대상 물체를 수직으로 잘라 층을 드러냄. 카메라 15–25° 부감, 잘린 면은 살짝 밝게 |
| 모션 | 2.5–4초. 흙 → 강돌 → 목곽 순서로 벗겨지거나 쌓임. 8–12프레임 페이드 |
| 라벨 | 층 이름 영어 3단어 이내 + GT-03 치수선 |
| EP01 적용 | G04 적석목곽 단면 (`CLM_EP01_STRUCT_004` · `CLM_CHEONMACHONG_LAYOUT_001`), G13 금관 위치 (GT-01 변형: 치수선 없음 · 금관은 브랜드 레드 대신 금색, D-026 #5 · GRAPHICS_SPEC_EP01_V2) |
| 벤치마크 대응 | 지반·물 단면 (g1-4, g3-3, g7-5) |

## GT-02 · 오버헤드 도식 (Overhead schematic)

| 항목 | 값 |
|---|---|
| 용도 | 배치·규모 비교·위치. "어디에, 얼마나 크게" |
| 구성 | 정사영 또는 30° 아이소메트릭. 비교 대상(축구장·건물·사람) 을 같은 축척으로 옆에 |
| 모션 | 2–3초. 대상 윤곽이 먼저, 비교 대상이 슬라이드 인 |
| 라벨 | 대상 이름 + 축척 바 |
| EP01 적용 | G03 왕릉군 개념도 (`CLM_EP01_TUMULI_002`), G02 지도 |
| 벤치마크 대응 | 연못 128×113 m 오버헤드 (g3-7), 기둥 48개 배열 (g5-8) |

## GT-03 · 빨간 치수선 · 숫자 카드 (Red dimension line · Number card)

| 항목 | 값 |
|---|---|
| 용도 | 추상 설명을 물체로. 연도·크기·개수 |
| 구성 | (a) 치수선: 끝 마커 + 수치, 대상 위에 오버레이. (b) 숫자 카드: 연도·개수를 화면 1/3 높이로 크게, 배경은 실사/도해 위 어둡게 |
| 모션 | 치수선 0.6–0.8초 그려짐, 숫자는 카운트 없이 즉시 (다큐 톤) |
| 라벨 | 단위 필수 (m · cm · kg · 년). fact_id 화면 밖 메타 |
| EP01 적용 | G04 에 47 m / 12.7 m / 6.6×4.2 m 추가 (제안, `STORY_ENGINE_EP01.md` ③) · 연도 카드 1973 |
| 벤치마크 대응 | "1412" 대형 숫자 (g3-4), 용 146.5 cm 치수 (g8-1) |

## GT-04 · 틀린 답 X → 맞는 답 (Rejected answer)

| 항목 | 값 |
|---|---|
| 용도 | **② REJECTED OBVIOUS ANSWER 전용.** 상식 처방을 화면에 세우고 FACT 로 지운다 |
| 구성 | 좌: 상식 답 도식 (회색), 우: 사실 도식. 좌측에 빨간 X 가 0.4초에 그어지고 회색이 더 어두워짐 |
| 모션 | 답 하나당 4–8초. 최대 3개 연속 |
| 라벨 | 좌 "Maybe: {obvious}" / 우 "Actually: {fact}" (영어 5단어 이내) |
| EP01 적용 | 현재 없음. ② 신설 시 (a) "More kings?" → 56 kings vs hundreds of mounds **(56 = UNSOURCED, fact 신설 전 화면 사용 금지)** (b) "Spare land?" → next to the palace |
| 벤치마크 대응 | 물 퍼내기 X · 흙 덮기 X (g2-6~9), 빨간 X 마크 (g7-8, g8-4) |

## 산출 방식

- Blender 씬 템플릿 4개를 `04_BLENDER_LIBRARY/templates/GT-0x/` 에 두는 것이 목표 (현재 **없음**, 다음 작업). 이 문서는 명세만.
- 에피소드 G 항목은 `template: GT-0x` 필드를 갖는다 (GRAPHICS_SPEC v3 부터).

## 미결 (사용자 결정 필요)

- 도해 재질·배경 톤 (흰 배경 vs 짙은 남색) — GRAPHICS_SPEC v2 §1.2 미정 항목과 함께.
- GT-04 의 "Maybe / Actually" 문구 확정.
