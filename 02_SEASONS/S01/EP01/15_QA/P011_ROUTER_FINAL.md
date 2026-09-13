# P-011 라우터 최종 잠금 — D-024

> 2026-09-13 · 사용자 승인 · 스크립트 `00_SYSTEM/tools/p011_router_lock.py`

## 결과

| 파이프라인 | P4 판정 | 최종 (D-024) |
|---|---|---|
| REAL_SHOOT | 10 | 10 |
| ARCHIVE | 20 | 20 |
| ORIGINAL_GRAPHIC | 11 | 11 |
| BLENDER_FLOW | 6 | **4** (H02 · H02b · H04 · H05) |
| FLOW_VEO | — | **2** (H01 · H03) |
| AI_STILL | 1 | **2** (H06 · H07) |
| HIGGSFIELD | 1 | **0 (EP01 잠금)** |

46 ACCEPTED · 3 OVERRIDDEN. AI 8컷 45초 (≈11%, 모두 ≤6초).

## EP01 재현 원칙

- 공간 위계·규모 중요 → **BLENDER_FLOW**
- 행동 중심, 공간 중간 → **FLOW_VEO**
- 움직임 적은 정보 컷 → **AI_STILL**
- 증거 중심 → **ARCHIVE**
- 현재 장소 → **REAL_SHOOT**
- 설명 도식 → **ORIGINAL_GRAPHIC**
- 극단 카메라·과장된 reveal 이 핵심이 아닌 다큐 톤 → **Higgsfield 0건**

## 변경 2건

- `EP01_S04_SH004` H01 목재 준비: BLENDER_FLOW → **FLOW_VEO** — 사람 움직임 중심, 공간 정밀도 중간, 단일 행동.
- `EP01_S05_SH005` H03 부장품 준비: BLENDER_FLOW → **FLOW_VEO** — 손 동작·소품 제스처 중심, 카메라 단순.

## 주의 (판정과 별개)

1. YELLOW_ACTIVE 권리 `RTS_GNM_OTHER_OBJECTS_001` (S02_SH003 · S05_SH001) — 편집 확정 전 해소 필수.
2. Flow/Veo 자동 연결 도구 없음 — 실제 생성은 별도 승인 + 별도 Money Gate (크레딧 체계 다름).
3. Blender 자동화(P7) 전 — BLENDER_FLOW 4건은 `10_BLENDER/camera_*` 초안 기준 수작업 허용.
4. 의존성: Master Frame S04 (H01 · H02 · H02b) · S06 (H04 · H05 · H06), H07 은 SH003 실사 구도 뒤.

## 49건

| Shot | 초 | 목적 | 라우터 권고 | 최종 | 사람 판정 | AI 비용 |
|---|---|---|---|---|---|---|
| EP01_S01_SH001 | 8 | 현대 경주 거리 — 봉분은 아직 안 보이거나 일부만 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S01_SH002 | 10 | 카페/도로에서 봉분 리빌, 사람으로 크기 비교 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S01_SH003 | 7 | G01 질문 카드 — 봉분 와이드 위 타이틀 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S01_SH004 | 17 | G02 Korea → Gyeongju → SILLA CAPITAL 지도 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S02_SH001 | 11 | 왕릉군·월성·사찰 등 역사경관 3–4컷 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S02_SH002 | 12 | G03 왕릉군 개념도 (자체 단순화 도식) | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S02_SH003 | 20 | 유물 몽타주 금관 → 유리잔 → 말다래 (컷당 1–1.5초) | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S03_SH001 | 13 | 천마총 외관·표지·입구 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S03_SH002 | 15 | 1973 조사단·발굴현장 흑백사진 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S03_SH003 | 5 | 유물 수습 현장 사진 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S03_SH004 | 6 | 금관 → 천마도 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S03_SH005 | 11 | G06 OCCUPANT: UNCERTAIN 카드 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S04_SH001 | 9 | 구조가 드러난 발굴현장 사진 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S04_SH002 | 8 | G04 적석목곽 단면 — 관 → 목곽 → 돌무지 → 흙 봉분 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S04_SH003 | 16 | G05 무덤 조성 4단계 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S04_SH004 | 6 | H01 목재 준비 — 무덤이 '공사'였다는 감각 | BLENDER_FLOW | **FLOW_VEO** | OVERRIDDEN | 있음 |
| EP01_S04_SH005 | 6 | H02 돌 운반 — 규모와 노동력 | BLENDER_FLOW | **BLENDER_FLOW** | ACCEPTED | 있음 |
| EP01_S04_SH006 | 6 | H02 조직된 작업 와이드 | BLENDER_FLOW | **BLENDER_FLOW** | ACCEPTED | 있음 |
| EP01_S04_SH007 | 9 | 실제 발굴사진으로 복귀 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S05_SH001 | 21 | 금관·관모·금허리띠·가슴걸이 몽타주 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S05_SH002 | 16 | G07 SACREDNESS · LEGITIMACY · AUTHORITY | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S05_SH003 | 8 | 허리띠 출토현장 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S05_SH004 | 8 | 현재 유물 (허리띠) | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S05_SH005 | 4 | H03 부장품 준비 — '무엇을 넣을지 골랐다' | BLENDER_FLOW | **FLOW_VEO** | OVERRIDDEN | 있음 |
| EP01_S05_SH006 | 8 | 실제 금관으로 하드컷 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S06_SH001 | 7 | G08 FACT / CONTEXT / INTERPRETATION | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S06_SH002 | 6 | H04 장례 준비 — 역할별 배치로 위계를 보여줌 (핵심 순간) | BLENDER_FLOW | **BLENDER_FLOW** | ACCEPTED | 있음 |
| EP01_S06_SH003 | 5 | 1973 목곽·매장 공간 발굴사진 — 재현 뒤 실제 증거 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S06_SH004 | 5 | 금제 장신구 디테일 — 사람은 가도 지위의 표시는 남는다 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S06_SH005 | 6 | H05 관찰자 시점 — 사람 머릿속이 아니라 '문제 상황' (핵심 순간) | BLENDER_FLOW | **BLENDER_FLOW** | ACCEPTED | 있음 |
| EP01_S06_SH006 | 5 | 금관 디테일 — rank · legitimacy · authority | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S06_SH007 | 4 | 현재 봉분을 멀리서 바라보는 시점 — H05 시선을 실사로 이어받기 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S06_SH008 | 5 | NO DIRECT QUOTATION 카드 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S06_SH009 | 7 | 실제 발굴사진 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S06_SH010 | 6 | H06 거의 완성된 봉분 와이드 — 권위가 '보이는 형태'가 됨 | AI_STILL | **AI_STILL** | ACCEPTED | 있음 |
| EP01_S06_SH011 | 4 | 현재 봉분과 관람객 — 지금도 산 사람들에게 보이는 봉분 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S07_SH001 | 18 | 박물관 조명 아래 금관 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S07_SH002 | 4 | 출토 현장 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S07_SH003 | 7 | 금관 | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S07_SH004 | 13 | 금관 디테일 홀드 (+ 질문 자막 1줄 선택) | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S07_SH005 | 3 | G13 금관 위치 단면 — 피장자 머리 동쪽, 금관 착용, 머리맡 부장궤 (단순화 도식) | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
| EP01_S08_SH001 | 15 | 산책·사진·차량·카페 몽타주 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S08_SH002 | 5 | H07 과거 봉분 — 매치컷 셋업 | HIGGSFIELD | **AI_STILL** | OVERRIDDEN | 있음 |
| EP01_S08_SH003 | 5 | 현재 봉분 — 매치컷 착지 (G10) | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S09_SH001 | 6 | 발굴 (3단 교차 ①) | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S09_SH002 | 6 | 금관 (3단 교차 ②) | ARCHIVE | **ARCHIVE** | ACCEPTED | 없음 |
| EP01_S09_SH003 | 6 | 현재 봉분 — 오프닝 구도 회수 (3단 교차 ③) | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S09_SH004 | 11 | 석양·골든아워 왕릉 히어로 와이드 | REAL_SHOOT | **REAL_SHOOT** | ACCEPTED | 없음 |
| EP01_S09_SH005 | 6 | G11 엔드카드 → G12 출처 슬레이트 | ORIGINAL_GRAPHIC | **ORIGINAL_GRAPHIC** | ACCEPTED | 없음 |
