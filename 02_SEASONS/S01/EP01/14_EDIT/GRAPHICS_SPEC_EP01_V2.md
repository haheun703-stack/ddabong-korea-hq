# EP01 GRAPHICS SPEC v2 — 경주 왕릉 / 천마총

> 문서 상태 **DRAFT v2** (2026-09-13, Claude Code) · 사용자 승인 전
> 원본(legacy, APPROVED): `episodes/ep01-graphics-spec.html` (2026-08-16, G01–G12) — **이 문서는 legacy HTML 을 수정하지 않는다.**
> 근거: `05_SCRIPT/SCRIPT_ROUGHCUT_DELTA.md` (X2 · X3) · `07_SHOTS/shot_*.json` (`pipeline = ORIGINAL_GRAPHIC` 11 샷 + AI 라벨 샷) · `05_HISTORY_DATABASE/facts|sources|rights|locations` · `00_SYSTEM/standards/HISTORY_ACCURACY_STANDARD.md`
> 판정 규칙 (D-010): 내용·사실·해석 차이 → Script/Fact 우선 · 타이밍·컷 배치 차이 → Rough Cut 우선.

---

## 1. 머리말

### 1.1 v2 의 범위
- **v2 = legacy G01–G12 그대로 + G13 신규 (금관 위치 단면, X3).**
- legacy 에서 내용이 바뀐 곳은 이미 결정된 것만 반영한다: **G06 화면 문구 → `OCCUPANT: UNCERTAIN`** (X2, D-010). 그 밖의 legacy 문구·모션 지시는 그대로 옮겼다.
- 타임코드(TC)와 길이는 **샷 JSON (러프컷 v1 기준)** 값을 쓴다. 내레이션 녹음 후 재조정된다. legacy TC 와 다른 곳은 §5 에 보고만 하고 고치지 않았다.
- Legacy on-screen text is mostly English; G05 step names and G08 description lines are Korean in legacy — English versions 미정. (이 문서의 설명은 한국어.)

### 1.2 공통 화면 규격 (legacy 에서 그대로)

| 항목 | 값 | 출처 |
|---|---|---|
| Master | 3840×2160 UHD, 16:9. 그래픽 원본은 4K 기준으로 제작 | legacy |
| Frame rate | 23.976 또는 25fps 중 촬영 기준과 통일 (확정값 미정 (편집 시 결정)) | 러프컷 v1 시퀀스 세팅 |
| 트랙 | V3 = Graphics / captions / source labels | 러프컷 v1 |
| Safe area | 중요 텍스트는 좌우 7%, 상하 7% 안쪽. 한 화면 핵심 문구는 3~7단어 우선 (모바일 가독성) | legacy |
| Brand color | DDABONG Red `#E10612` · Korea Blue `#003478` · 기본 배경 흰색 / 짙은 남색 | legacy |
| Motion | 다큐멘터리식 8~12프레임 페이드·슬라이드. 과도한 줌/글리치 금지 | legacy |
| Source label | 아카이브/유물 출처는 화면 하단에 작게, YouTube 설명란에는 전체 크레딧 | legacy |
| Font (서체·굵기·크기) | **미정 (편집 시 결정)** — legacy 에 지정 없음 | — |
| 남색 배경 정확한 HEX | **미정 (편집 시 결정)** — legacy 는 "짙은 남색" 만 기재 (Korea Blue 와 동일 여부 불명) | — |
| 텍스트 색 | legacy 에서 텍스트 색이 지정된 것은 **G01 흰색 텍스트뿐**. G09 는 텍스트 색이 아니라 약 70~80% 흰색 **배경** 박스(또는 어두운 반투명 박스). 그 외 모든 그래픽의 텍스트 색 **미정 (편집 시 결정)** | legacy |
| 제작 원칙 | 그래픽은 역사 자료를 '멋있게 바꾸는' 장치가 아니라 이해를 돕는 장치. 실제 발굴사진·유물과 충돌하는 디테일은 넣지 않는다 | legacy |

### 1.3 공통 사실 규칙 (HISTORY_ACCURACY_STANDARD)
- 화면 문구는 연결된 fact 의 `confidence` 를 넘지 않는다.
- `INTERPRETIVE` (`hedge_required = true`) 주장은 화면에 올릴 경우 반드시 `MAY HAVE / MIGHT HAVE / IT IS POSSIBLE THAT` 류 hedge 를 붙인다. **G01–G13 중 INTERPRETIVE fact 를 직접 문구로 쓰는 그래픽은 없다.** INTERPRETIVE 주장을 그래픽 문구로 새로 올리지 않는다.
- 역사 AI 장면은 `AI VISUAL RECONSTRUCTION` (G09). 강한 해석 장면은 `INTERPRETIVE RECONSTRUCTION` 병기.
- 특정 왕 이름으로 피장자를 표기하지 않는다 (`CLM_EP01_OCCUPANT_006`).
- 박물관·기관 도면/사진을 트레이싱하지 않는다. 검증된 fact 로 새로 그린다.
- 권리 RED 자산은 어떤 그래픽의 배경·참조 이미지로도 쓰지 않는다 (§4).

---

## 2. 그래픽별 명세 (G01–G13)

### 요약표

| G | 이름 | 샷 ID | TC (러프컷 v1) | 길이 | 근거 fact | 신뢰도 | hedge |
|---|---|---|---|---|---|---|---|
| G01 | OPEN 질문 카드 | `EP01_S01_SH003` | 0:18–0:25 | 7초 (카드 노출 1.5~2초) | `CLM_EP01_TOMBS_001` | FACT | 불필요 |
| G02 | MAP Korea → Gyeongju | `EP01_S01_SH004` | 0:25–0:42 | 17초 (모션 2.5~3.5초) | `CLM_EP01_TOMBS_001` | FACT | 불필요 |
| G03 | LANDSCAPE 왕릉군 개념도 | `EP01_S02_SH002` | 0:53–1:05 | 12초 | `CLM_EP01_TUMULI_002` | FACT | 불필요 |
| G04 | STRUCTURE 적석목곽 단면 | `EP01_S04_SH002` | 2:24–2:32 | 8초 | `CLM_EP01_STRUCT_004` · `CLM_CHEONMACHONG_LAYOUT_001` | FACT | 불필요 |
| G05 | BUILD 조성 4단계 | `EP01_S04_SH003` | 2:32–2:48 | 16초 (단계당 0.8~1.2초) | `CLM_EP01_STRUCT_004` | FACT | 불필요 |
| G06 | UNCERTAINTY 피장자 카드 | `EP01_S03_SH005` | 2:04–2:15 | 11초 | `CLM_EP01_OCCUPANT_006` | FACT (불확실성 자체가 사실) | 문구 자체가 불확실 표기 |
| G07 | EVIDENCE 금문화 핵심어 | `EP01_S05_SH002` | 3:36–3:52 | 16초 | `CLM_EP01_GOLD_007` | FACT (박물관 해석 인용 형태로만) | 불필요, 단 출처 라벨 필수 |
| G08 | METHOD FACT/CONTEXT/INTERPRETATION | `EP01_S06_SH001` | 4:20–4:27 | 7초 | 없음 (방법론 카드) | 해당 없음 | 해당 없음 |
| G08 계열 | NO DIRECT QUOTATION | `EP01_S06_SH008` | 4:58–5:03 | 5초 | 없음 | 해당 없음 | 해당 없음 |
| G09 | AI LABEL | AI 샷 8개 오버레이 (전용 샷 없음) | 각 AI 샷 | 샷 길이 (최소 2초 노출) | 샷별 | — | — |
| G10 | THEN/NOW 매치컷 | `EP01_S08_SH002` → `EP01_S08_SH003` (편집 전환, ORIGINAL_GRAPHIC 아님) | 6:20–6:30 | 5초 + 5초 | `CLM_EP01_MOUND_011` (SH002, INTERPRETIVE) · `CLM_EP01_TOMBS_001`/`MODERN_012` (SH003) | PROBABLE (`S08_SH002.historical_confidence`) | 전환 자체에는 문구 없음 |
| G11 | END 엔드카드 | `EP01_S09_SH005` (G12 와 한 샷) | 6:59–7:05 | 6초 합계 (G11 3~4초) | 없음 | 해당 없음 | 해당 없음 |
| G12 | CREDITS 출처 슬레이트 | `EP01_S09_SH005` (G11 뒤) | 6:59–7:05 | 6초 합계 (G12 2~3초) | EP01 전체 source (§4) | — | — |
| **G13** | **금관 위치 단면 (단순화 도식)** | `EP01_S07_SH005` | 5:42–5:45 | **3초** | `CLM_CHEONMACHONG_LAYOUT_001` | FACT | 배치는 불필요 · 해당 내레이션은 "may have" hedge 로 해결 (§5 #15, D-026) |

---

### G01 · OPEN — 질문 카드
- **사용 샷**: `EP01_S01_SH003` · 7초 · TC 0:18–0:25 · evidence_role SUPPORTING
- **화면 문구** (legacy 그대로):
  ```
  WHY ARE GIANT TOMBS
  EVERYWHERE IN THIS CITY?
  ```
- **레이아웃/애니메이션**: 현대 경주 + 왕릉 실사(V1 = 봉분 와이드, SH002 연장) 위에 흰색 텍스트. 카드 노출 1.5~2초. 로고는 넣지 않거나 아주 작게. "tombs" 직전 0.3초 음악 드롭 (러프컷). 7초 샷 안에서 카드 인/아웃 위치는 미정 (편집 시 결정).
- **근거**: `CLM_EP01_TOMBS_001` (FACT) — 경주에 신라 왕릉군이 집중, 도시 경관의 일부. 출처 `SRC_UNESCO_GYEONGJU_001`.
- **hedge**: 불필요 (질문형 문구).
- **출처 표기**: 화면 표기 없음. 배경 실사가 자체 촬영(GREEN, 증빙 "self-shot / original footage / source file retained" 기록 시 — D-026)이면 크레딧 불필요, 백업 A1/A2 (YELLOW) 사용 시 §4 에 따름.
- **금지**: "EVERYWHERE" 를 수치(무덤 개수)로 바꾸지 않는다 — 개수는 fact 에 없음. 미스터리/호러 톤 금지.

### G02 · MAP — Korea → Gyeongju
- **사용 샷**: `EP01_S01_SH004` · 17초 · TC 0:25–0:42 · SUPPORTING
- **화면 문구**: `SILLA CAPITAL` (경주 점/라벨). 국가·도시 라벨 표기 형식(`KOREA`, `GYEONGJU`)은 legacy 제목 "Korea → Gyeongju" 에서 따옴; 정확한 라벨 문구는 미정 (편집 시 결정).
- **레이아웃/애니메이션**: 동아시아 최소 지도 → 대한민국 강조 → 경주에 점/라벨 → `SILLA CAPITAL`. 모션 2.5~3.5초. 카메라 줌보다 벡터 스케일 전환. 맵 전환용 짧은 whoosh 1회만 (러프컷).
- **근거**: `CLM_EP01_TOMBS_001` (FACT). `SILLA CAPITAL` 은 `SRC_UNESCO_GYEONGJU_001` 요약("신라 도읍")에 있으나 fact 본문에는 명시되지 않음 → §5 #9.
- **hedge**: 불필요.
- **출처 표기**: 지도 베이스맵 출처 미정 (편집 시 결정) — 자체 제작 벡터 권장, 외부 지도 사용 시 권리 레코드 필요.
- **금지**: 주변 국가 국경/정치정보는 최소화. 고대 신라 영역 경계선을 그리지 않는다 (fact 없음).

### G03 · LANDSCAPE — 왕릉군 개념도
- **사용 샷**: `EP01_S02_SH002` · 12초 · TC 0:53–1:05 · PRIMARY
- **화면 문구**: `ROYAL TOMB GROUPS` + 봉분 아이콘.
- **레이아웃/애니메이션**: 목적 = "몇 개의 무덤"이 아니라 왕릉군이 도시 경관을 이룬다는 점을 이해시킨다. 정확한 GIS 복제 대신 자체 단순화 도식. 대본 v2: 3개 그룹을 도식적으로 강조, 조밀한 관광지도 아님. 등장 모션 세부 미정 (편집 시 결정; 공통 8~12프레임 페이드 적용).
- **근거**: `CLM_EP01_TUMULI_002` (FACT) — 대릉원지구 왕릉 3개 그룹, 대부분 돔형 봉분. 출처 `SRC_UNESCO_GYEONGJU_001`.
- **hedge**: 불필요.
- **출처 표기**: 도식 자체는 출처 라벨 불필요. 설명란에 UNESCO 인용 가능 (텍스트 인용만).
- **금지**: GIS/실측 복제 금지 · 봉분 개수·정확한 배치 표현 금지 (`LOC_GYEONGJU_DAEREUNGWON_V01.unverified_do_not_invent`) · UNESCO 영상·사진 사용/트레이싱 금지 (RED).

### G04 · STRUCTURE — 적석목곽 구조 단면
- **사용 샷**: `EP01_S04_SH002` · 8초 · TC 2:24–2:32 · PRIMARY
- **화면 문구**: legacy 에 확정 문구 없음 → 레이어 라벨 영문 표기는 미정 (편집 시 결정). 치수 표기 시 fact 값만: coffin 2.15×0.8 m · wooden chamber 6.6×4.2 m · mound 47 m across, 12.7 m high.
- **레이어 (확정, D-026)**: **coffin → wooden chamber → stone/gravel → earth mound** (관 → 목곽 → 돌/자갈 → 흙 봉분, 대본 v2 L47 기준). **별도 부장품 층 없음** — 부장품은 관·목곽 주변에 놓인 모습으로만 표시. legacy 의 "부장품 공간" 층은 쓰지 않는다 (§5 #6).
- **레이아웃/애니메이션**: 아래부터 한 층씩 쌓기. 실제 1973 발굴사진(`EP01_S04_SH001`, NRICH GREEN)과 번갈아 보여줌. 낮은 목재/돌 질감 SFX 아주 약하게 (러프컷).
- **근거**: `CLM_EP01_STRUCT_004` (FACT, `SRC_GNM_CHEONMA_EXHIBITION_001` · `SRC_NRICH_CHEONMACHONG_DICT_001`) · `CLM_CHEONMACHONG_LAYOUT_001` (FACT). "자갈(gravel)" 표현은 `CLM_EP01_TUMULI_002` (UNESCO) 근거 — 이 샷의 fact_ids 에는 없음 (§5 #7).
- **hedge**: 불필요.
- **출처 표기**: 도식 하단 소형 라벨 권장 여부 미정 (편집 시 결정). 설명란: 국립경주박물관 · 국립문화유산연구원 (텍스트 인용).
- **금지**: 박물관 도면을 그대로 트레이싱하지 않고 검증 사실로 새로 그림 (legacy) · **돌무지 높이·두께 수치 금지** (`unverified_do_not_invent`) · 봉분 비율은 47 m / 12.7 m 준수 · **목곽·관의 세로 비율은 도식일 뿐, 높이 스케일을 암시하지 않는다** (vertical proportions schematic only; no height scale implied — 6.6×4.2 m · 2.15×0.8 m 는 평면 크기이며 목곽·관 높이 fact 없음) · 2019 NRICH 간행물 도면 캡처 금지 (RED).

### G05 · BUILD — 무덤 조성 4단계
- **사용 샷**: `EP01_S04_SH003` · 16초 · TC 2:32–2:48 · PRIMARY
- **화면 문구** (legacy 그대로, 영문 표기는 미정 (편집 시 결정) — legacy 는 한국어 단계명만 기재):
  ```
  STEP 1  목곽/관 준비
  STEP 2  부장품 배치
  STEP 3  돌무지 축조
  STEP 4  흙 봉분 완성
  ```
- **레이아웃/애니메이션**: 각 단계 0.8~1.2초. AI 재현 H01/H02/H03 (`EP01_S04_SH004`–`SH006`, `EP01_S05_SH005`) 과 연결 — legacy 의 'Higgsfield' 표기는 D-024 로 대체 (H01·H03 FLOW_VEO, H02·H02b BLENDER_FLOW, EP01 Higgsfield 0건). 설명 구간, 음악 단순 (러프컷). 16초 샷 대비 단계 합계 3.2~4.8초 → 나머지 시간 처리 미정 (편집 시 결정) (§5 #3).
- **근거**: `CLM_EP01_STRUCT_004` (FACT) — 목곽에 관 → 위에 돌 → 흙 봉분. STEP 2 부장품 위치는 `CLM_CHEONMACHONG_LAYOUT_001` · `CLM_EP01_GOODS_005` 가 뒷받침하나 이 샷 fact_ids 에 없음 (§5 #7).
- **hedge**: 불필요 (단계 순서는 구조 fact). 단 단계 사이 시간·인력은 표기하지 않는다.
- **출처 표기**: G04 와 동일.
- **금지**: **조성 기간, 작업 인원 수, 의례 순서 표기 금지** (`unverified_do_not_invent`) · 장례가 "조직된 사회적 행사였다" 식 해석 문구 금지 (`CLM_EP01_FUNERAL_008` = INTERPRETIVE; 쓸 경우 반드시 `MAY HAVE` hedge, 단 이 그래픽에는 넣지 않음).

### G06 · UNCERTAINTY — 피장자 불확실 카드 (X2 반영)
- **사용 샷**: `EP01_S03_SH005` · 11초 · TC 2:04–2:15 · PRIMARY
- **화면 문구** (Script 우선, D-010 X2):
  ```
  OCCUPANT: UNCERTAIN
  ```
  보조 문구 (선택, legacy 러프컷 문구): `WHO WAS BURIED HERE?` — 보조로만. legacy 2행 `UNKNOWN WITH CERTAINTY` 는 주 문구에서 대체됨; 보조로 병기할지 미정 (편집 시 결정).
- **레이아웃/애니메이션**: 'Mystery' 연출을 과도하게 하지 말고 DDABONG 의 신뢰성 표시로 사용 (legacy). 음악 축소, 1초 정적감 (러프컷).
- **근거**: `CLM_EP01_OCCUPANT_006` (FACT) — 규모·유물로 보아 왕 또는 왕에 준하는 인물로 추정되나 신원은 확정되지 않음. 출처 `SRC_NRICH_CHEONMACHONG_DICT_001`.
- **hedge**: fact 는 hedge_required=false (불확실성 자체가 사실). "왕 또는 왕급" 을 화면에 추가할 경우 `PROBABLY` / `LIKELY` 를 반드시 붙인다 (fact 본문이 "probably").
- **출처 표기**: 화면 라벨 여부 미정 (편집 시 결정). 설명란: 국립문화유산연구원 「한국고고학사전」.
- **금지**: 특정 왕 이름·후보 왕 목록 표기 금지 · `UNKNOWN` 을 "아무도 모른다 / 미스터리" 톤으로 과장 금지.

### G07 · EVIDENCE — 신라 금문화 핵심어
- **사용 샷**: `EP01_S05_SH002` · 16초 · TC 3:36–3:52 · PRIMARY (에피소드 핵심 문장)
- **화면 문구**:
  ```
  SACREDNESS · LEGITIMACY · AUTHORITY
  ```
  하단 출처 라벨: `Gyeongju National Museum`
- **레이아웃/애니메이션**: 대본 v2 "Three restrained words". 음악 가장 명료하게 (러프컷). 단어별 순차 등장 여부 미정 (편집 시 결정).
- **근거**: `CLM_EP01_GOLD_007` (FACT) — **박물관 공식 해석을 인용하는 형태로만 FACT**. 출처 `SRC_GNM_SILLA_GOLD_001` (국립경주박물관 「신라, 황금의 나라」).
- **hedge**: hedge_required=false. 대신 **출처 귀속이 hedge 역할** → 출처 라벨 `Gyeongju National Museum` 은 생략 불가. 내레이션 "The museum describes…" 와 짝.
- **출처 표기**: 화면 하단 `Gyeongju National Museum` (필수) + 설명란 전체 크레딧.
- **금지**: 출처 라벨 없이 단독 사실 진술처럼 표시 금지 · 단어 추가 금지 (예: `MEMORY`, `ORDER` — 이는 `CLM_EP01_MOUND_011` / `CLM_EP01_ORDER_010` INTERPRETIVE 영역) · 반짝 SFX 금지 (러프컷).

### G08 · METHOD — FACT / CONTEXT / INTERPRETATION
- **사용 샷**: `EP01_S06_SH001` · 7초 · TC 4:20–4:27 · evidence_role NONE
- **화면 문구** (legacy 그대로):
  ```
  FACT            유적·유물·발굴기록.
  CONTEXT         당시 사회·기술·장례 조건.
  INTERPRETATION  근거를 바탕으로 당시 선택의 의미를 재구성.
  ```
  (설명행 영문화 여부 미정 (편집 시 결정). 대본 v2 는 소형 라벨 `INTERPRETATION` 만 지시.)
- **레이아웃/애니메이션**: 영상 전체의 신뢰 장치. legacy = 4:20 전후 2초 카드 **또는** 화면 모서리 작은 라벨. 샷은 7초 → 카드형/라벨형 선택 미정 (편집 시 결정) (§5 #3).
- **근거**: fact 없음 (방법론). D-003 FACT → CONTEXT → INTERPRETATION 선례.
- **hedge / 출처**: 해당 없음.
- **금지**: 이 카드 뒤 H04–H06 해석 구간에서 AI 라벨(G09)을 생략하는 근거로 쓰지 않는다.

### G08 계열 · NO DIRECT QUOTATION (legacy 번호 없음)
- **사용 샷**: `EP01_S06_SH008` · 5초 · TC 4:58–5:03 · NONE
- **화면 문구** (대본 v2 · 러프컷):
  ```
  NO DIRECT QUOTATION
  ```
- **레이아웃/애니메이션**: 짧게 → 실제 발굴사진으로 복귀 (러프컷, `EP01_S06_SH009`). 추측 제한을 보여줌. 세부 미정 (편집 시 결정).
- **근거**: fact 없음. 내레이션 "We do not have a Silla text saying…" 의 보조. 이어지는 내레이션은 `CLM_EP01_ORDER_010` (INTERPRETIVE, "allows us to ask whether" 형태만).
- **금지**: 가상의 인용문을 화면에 띄우지 않는다 (예: "Build this mound to prove that order continues." 를 따옴표 카드로 제시 금지 — 실제 사료처럼 보임).
- **번호**: legacy G01–G12 에 없음. 별도 G 번호 부여 여부 미정 (§5 #2).

### G09 · AI LABEL — AI Visual Reconstruction
- **사용 샷** (전용 샷 없음, `ai_label` 필드가 있는 AI 샷 8개에 오버레이):

  | 샷 | H | TC | 길이 | ai_label |
  |---|---|---|---|---|
  | `EP01_S04_SH004` | H01 | 2:48–2:54 | 6초 | AI Visual Reconstruction |
  | `EP01_S04_SH005` | H02 | 2:54–3:00 | 6초 | AI Visual Reconstruction |
  | `EP01_S04_SH006` | H02 | 3:00–3:06 | 6초 | AI Visual Reconstruction |
  | `EP01_S05_SH005` | H03 | 4:08–4:12 | 4초 | AI Visual Reconstruction |
  | `EP01_S06_SH002` | H04 | 4:27–4:33 | 6초 | AI Visual Reconstruction |
  | `EP01_S06_SH005` | H05 | 4:43–4:49 | 6초 | **INTERPRETIVE RECONSTRUCTION** (notes: 두 라벨 모두 표시) |
  | `EP01_S06_SH010` | H06 | 5:10–5:16 | 6초 | AI Visual Reconstruction |
  | `EP01_S08_SH002` | H07 | 6:20–6:25 | 5초 | AI Visual Reconstruction |

- **화면 문구**: `AI VISUAL RECONSTRUCTION` · 보조 `INTERPRETIVE RECONSTRUCTION` (H05 는 두 줄 모두).
- **레이아웃**: 좌하단. 약 70~80% 흰색 배경 또는 어두운 반투명 박스. AI 장면 시작 후 최소 2초 이상 보이게 (legacy). 모든 AI 샷 ≥ 4초이므로 조건 충족 가능. 라벨 서체·크기 미정 (편집 시 결정).
- **근거**: HISTORY_ACCURACY_STANDARD 규칙 2. H04/H05/H06 구간 내레이션은 `CLM_EP01_FUNERAL_008` · `CLM_EP01_DISPLAY_009` · `CLM_EP01_ORDER_010` · `CLM_EP01_MOUND_011` (모두 INTERPRETIVE, hedge 필수) — 이 구간 자막/그래픽 문구를 추가할 경우 `MAY HAVE` 형태 필수.
- **금지**: AI 샷에서 라벨 생략 · 라벨을 safe area 밖에 배치 · AI 컷 끝에서 실제 자료로 복귀할 때 라벨을 실제 자료 위에 남겨두기.
- **G13 에는 적용하지 않음** (G13 은 AI 생성물이 아닌 자체 도식; 대신 `SIMPLIFIED DIAGRAM` 라벨).

### G10 · THEN/NOW — 과거 → 현재 매치컷
- **사용 샷**: `EP01_S08_SH002` (H07 AI 과거 봉분, 5초, 6:20–6:25) → `EP01_S08_SH003` (현재 봉분 실사, 5초, 6:25–6:30). **ORIGINAL_GRAPHIC 샷이 아니라 편집 전환** (§5 #4).
- **화면 문구**: 없음. H07 쪽에는 G09 라벨.
- **구성**: H07 AI 봉분과 실제 **천마총 봉분** (대릉원 안, D-026) 의 크기/위치가 비슷하도록 정렬 (legacy). SH003 실사 구도(삼각대 고정, 봉분 약간 오프축)를 먼저 찍어 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame` 에 기록 (D-026) → 그 구도에 맞춰 H07 생성 (Generate Late).
- **전환**: 디졸브보다 하드 매치컷 또는 4~6프레임 짧은 디졸브. 효과음 최소 (legacy) · "효과음 없이 컷 자체로 승부" (러프컷).
- **근거**: SH003 = `CLM_EP01_TOMBS_001` · `CLM_EP01_MODERN_012` (FACT). SH002 H07 = `CLM_EP01_STRUCT_004` (FACT, 봉분 스케일) + `CLM_EP01_MOUND_011` (INTERPRETIVE).
- **hedge**: 전환에 문구 없음. 문구를 추가한다면 `MOUND_011` 관련 표현은 `MAY HAVE` 필수.
- **금지**: 과거 봉분을 현재 봉분보다 크게/다른 형태로 과장 금지 (47 m / 12.7 m 스케일) · `match_cut_frame` 미기록 상태에서 H07 생성 금지.

### G11 · END — 엔드 카드
- **사용 샷**: `EP01_S09_SH005` (G12 와 한 샷) · 6초 합계 · TC 6:59–7:05
- **화면 문구** (legacy 그대로):
  ```
  DDABONG KOREA
  STORIES BEHIND KOREA
  ```
  + 다음 화 예고 1줄 (문구 미정 (편집 시 결정) — EP02 주제 미확정).
- **레이아웃/애니메이션**: 마스터 로고 + 다음 화 예고 1줄. 3~4초. 첫 영상에서는 구독 CTA 보다 브랜드 기억 우선. 로고 사운드 1회, 과도한 CTA 없음 (러프컷). 마스터 로고 파일 경로 미정 (편집 시 결정).
- **근거 / hedge**: 해당 없음.
- **금지**: 과도한 구독/알림 CTA.

### G12 · CREDITS — 출처/라이선스 엔드 슬레이트
- **사용 샷**: `EP01_S09_SH005` (G11 뒤) · G12 부분 2~3초
- **화면 문구** (legacy 그대로, 최종은 **사용한 파일만** 기입):
  ```
  NRICH 1973 excavation photos — KOGL Type 1
  Gyeongju National Museum artifacts — applicable KOGL Type 1 assets
  ```
  v2 추가 후보 (실제 사용 시에만, 권리 레코드 attribution_text 기준 → §4):
  ```
  Cheonmado (Heavenly Horse painting) — Public Domain, via Wikimedia Commons
  ```
- **표기 형식**: 화면 슬레이트는 위의 **legacy 짧은 형식**을 쓴다. YouTube 설명란에는 각 권리 레코드의 `attribution_text` 를 **글자 그대로 전문** 기입한다 (§4.2). 주의: GREEN 레코드 전부 `proof: null` — 파일별 라이선스 캡처 저장 전에는 최종 확정 불가.
- **레이아웃**: 영상 끝 2~3초 요약 + 상세 출처는 설명란 (legacy). 서체·열 구성 미정 (편집 시 결정).
- **근거**: §4 목록.
- **금지**: 사용하지 않은 자산 기재 금지 · RED 자산 기재·사용 금지 · YELLOW 미해소 자산(`RTS_GNM_OTHER_OBJECTS_001` 등) 을 GREEN 처럼 기재 금지.

---

## 3. G13 · 금관 위치 단면 — 단순화 도식 (신규, X3)

### 3.1 기본 정보
| 항목 | 값 |
|---|---|
| 사용 샷 | `EP01_S07_SH005` (ORIGINAL_GRAPHIC · PRIMARY · spatial_accuracy 90) |
| TC / 길이 | 5:42–5:45 (러프컷 v1 기준) · **3초** |
| 앞/뒤 샷 | 앞 `EP01_S07_SH002` 출토 현장 (ARCHIVE, NRICH 1973, 4초) → **G13** → 뒤 `EP01_S07_SH003` 금관 (MUSEUM, GNM KOGL 1) |
| 해당 내레이션 | "But originally, this was not an object made for a museum. It may have belonged to a burial system of status, ceremony, and identity." (대본 v2 5:20–6:05, hedge 반영 D-026) |
| 대본 v2 지시 | `[GRAPHIC]` Tomb cross-section with crown position as a simplified illustration, **only if archaeologically supported.** |
| 판정 | X3 RESOLVED (D-010) — S4(`SRC_NRICH_CHEONMACHONG_DICT_001`)로 뒷받침됨 |
| 근거 fact | `CLM_CHEONMACHONG_LAYOUT_001` · **FACT** · hedge_required **false** |
| fact 출처 | `SRC_NRICH_CHEONMACHONG_DICT_001` (국립문화유산연구원 「한국고고학사전」 천마총, EXCAVATION_REPORT) · `SRC_GNM_CHEONMA_EXHIBITION_001` (국립경주박물관 특별전 「천마, 다시 날다」, MUSEUM) |
| 성격 라벨 | **단순화 도식** — 실측 도면 아님, AI 생성물 아님 |

### 3.2 fact 원문 (그릴 수 있는 범위의 상한)
> 천마총 피장자는 목관 안에 머리를 동쪽으로 두고 금관·귀걸이·경흉식·과대 등을 착용한 상태였다. 부장품 궤는 머리맡(동쪽)에 목관과 T자로 놓였고, 금제관모·백화수피 관모는 목관 밖 석단 동남쪽 모서리에 있었다.
>
> fact notes: **G13 단면 그래픽은 이 배치(머리 동쪽·금관 착용·머리맡 부장궤)만 그린다. 그 밖의 세부는 그리지 않는다.**
> shot notes: 그리는 것 = 목관 안 피장자 머리 동쪽 + 머리 위 금관 + 머리맡 부장궤 T자. 그 외 세부 금지.

### 3.3 그리는 것 (4개 요소만)

| # | 요소 | 표현 | 근거 |
|---|---|---|---|
| 1 | 목관 (coffin) | 단순 사각형 윤곽 1개 (치수 라벨 없음) | `LAYOUT_001` "목관 안" |
| 2 | 피장자 머리 위치 = **동쪽** | 목관 안 동쪽 끝에 머리 위치 표시 + 방위 표시 `E` (또는 `EAST` 화살표) | `LAYOUT_001` "머리를 동쪽으로" |
| 3 | 금관 **착용** 상태 | 머리 위치에 금관 아이콘/금색 표시 (착용 = 머리 위치와 겹침) | `LAYOUT_001` "금관 … 착용한 상태" |
| 4 | 부장품 궤 (grave-goods chest) | 목관 **머리맡(동쪽)** 에 목관과 **T자** 로 놓인 사각형 | `LAYOUT_001` "머리맡(동쪽)에 목관과 T자" · 소스 S4 요약: 궤는 남북 장축 (T자와 일치) |

- 선택 요소: 목곽(wooden chamber) 외곽선 — 윤곽선만, 치수 라벨 없음. SH005 는 `CLM_EP01_STRUCT_004` 를 연결하지 않으므로 (§5 #14) 넣으려면 연결이 먼저 필요. 넣을지 여부 미정.

### 3.4 그리지 않는 것 / "미표시" 처리

| 항목 | fact/소스 상태 | G13 처리 |
|---|---|---|
| 귀걸이·경흉식·과대 착용 | `LAYOUT_001` 에 있음 | **그리지 않음** — fact/shot notes 가 금관만 허용. 착장품 전체를 표현하지 않음 |
| 금제관모·백화수피 관모 (목관 밖 석단 동남 모서리) | `LAYOUT_001` 에 있음 | **그리지 않음** — notes 가 허용한 3요소 밖. (금관과 혼동 위험) |
| 석단 (stone platform) | `LAYOUT_001` 에 이름만 등장, 형태·크기 없음 | 그리지 않음 |
| 환두대도 (왼쪽 허리 아래) | 소스 S4 요약 · location 에만 있음, **fact 본문에 없음** | 그리지 않음 |
| 금팔찌·반지·요패 | 소스 S4 요약에만 있음 | 그리지 않음 |
| 피장자 신체 자세·체형·얼굴·유골 | 어디에도 없음 | 그리지 않음. 머리 위치 표시만 (사람 형상 상세 묘사 금지). 표시 형태(원형 마커 / 최소 윤곽) 미정 (편집 시 결정) |
| 피장자 신원·성별·나이 | `CLM_EP01_OCCUPANT_006`: 신원 불확실 | 표기 금지. 라벨은 `OCCUPANT` 만 |
| 부장품 궤 안의 내용물 | fact 에 개별 배치 없음 (`GOODS_005` 는 "피장자와 궤에 부장" 까지만) | 궤는 빈 사각형. 내용물 아이콘 금지 |
| 부장품 궤 치수 1.8×1.0 m | `SRC_GNM_CHEONMA_EXHIBITION_001` 요약 · location 에 있음, **fact 본문에 없음** | 치수 라벨 표기 안 함. 궤와 목관의 크기 비교를 도식에 암시하지 않음 (SH005 연결 fact 에 크기 정보 없음) |
| 돌무지·흙 봉분 층 | G04 영역 (`STRUCT_004`) | G13 에는 넣지 않음 (3초 안에 요소 과다). 넣을지 미정 (편집 시 결정) |
| 돌무지 높이·두께, 조성 기간, 작업 인원, 의례 순서 | `unverified_do_not_invent` | 절대 표기 금지 |
| 매장 시점의 의례 장면 | 없음 | 금지 |

### 3.5 형식 — 동서 단면 + 작은 평면 인서트 (확정, D-026)
- **주 화면 = 동서 방향 옆 단면 (east–west side cross-section)**: 머리 동쪽 · 머리 위치에 착용한 금관 · 머리맡(동쪽 끝)의 부장품 궤까지 보여준다 (요소 #1–#4 의 위치 관계).
- **작은 평면 인서트 (top-down plan inset)**: 목관과 궤의 **T자 배치만** 보여준다. T자는 인서트에서만 표현한다 (단면으로는 T자 표현 불가).
- 역할 분리: 단면 = 머리 동쪽 / 금관 착용 / 머리맡 궤 · 인서트 = T자. 인서트에는 목관·궤 윤곽과 방위 `E` 표시 외 새 요소를 넣지 않는다.
- 어느 쪽이든 §3.3 의 4요소와 방위 표시 외에는 추가하지 않는다. 기존 금지사항 (치수 라벨 없음 · 높이 스케일 없음 · fact 범위 안) 은 단면과 인서트 모두에 그대로 적용.
- **세로 비율은 도식일 뿐, 높이 스케일을 암시하지 않는다** (vertical proportions schematic only; no height scale implied). 어떤 fact 에도 목관·궤·목곽 높이가 없다.

### 3.6 화면 문구 (제안 — 사용자 승인 필요, legacy 에 선례 없음)
3초 · **화면 전체 합계 3~7단어** 원칙에 맞춘 최소안 (합계 7단어):
```
SIMPLIFIED DIAGRAM                      ← 좌하단 또는 상단 소형, 필수 (2)
GOLD CROWN                              ← 머리 위치의 금관 표시 옆 (2)
GRAVE-GOODS CHEST                       ← 궤 옆 (2)
E →                                     ← 방위 화살표 (1)
```
- 출처 라벨은 **설명란으로 이동** (기본안). 화면에 꼭 넣는다면 짧은 형식 `Based on NRICH · Gyeongju National Museum` 만 쓰고, 그만큼 위 라벨을 줄여 합계 7단어 이내 유지.
- `COFFIN` 라벨 추가 시 7단어 초과 → 넣지 않는 것이 기본. 최종 문구는 §6 A.
- 최종 문구·서체·배치는 미정 (편집 시 결정).

### 3.7 레이아웃/애니메이션
- 앞 샷(출토 현장 사진)에서 짧은 페이드로 진입 → 목관 윤곽 → 금관 표시 → 궤 T자 순으로 공통 8~12프레임 페이드. 3초 안에 완결되어야 하므로 순차 등장은 최소화. 정확한 프레임 배분 미정 (편집 시 결정).
- 색: 금관 표시만 금색 계열 강조, 나머지는 선화. 금색 HEX 미정 (편집 시 결정). 브랜드 레드 `#E10612` 를 금관 대신 쓰지 않는다 (유물 색 오인).
- 뒤 샷 `EP01_S07_SH003` 금관 실물로 하드컷 → "도식 → 실제 유물" 순서 (Evidence Before Imagination 과 충돌 없음: 앞에 실제 발굴사진, 뒤에 실제 유물).

### 3.8 hedge
- `CLM_CHEONMACHONG_LAYOUT_001` = FACT, hedge_required=false → 배치 자체에는 hedge 불필요.
- **내레이션 hedge 해결 (D-026)**: 해석적 문장이고 SH005 에 연결 fact 가 없으므로 대본을 "It may have belonged to a burial system of status, ceremony, and identity." 로 수정함 (§5 #15). G13 화면에 `STATUS` · `CEREMONY` · `IDENTITY` · `POWER` 등 의미 라벨을 붙이지 않는다 (붙이면 INTERPRETIVE 를 FACT 도식에 섞게 됨).
- 피장자를 `KING` 으로 라벨하지 않는다 (`OCCUPANT_006`). 필요 시 `OCCUPANT` 만.

### 3.9 출처 표기
- 화면: 기본은 출처 라벨 없음 (설명란으로 이동). 넣을 경우 `Based on NRICH · Gyeongju National Museum` (§3.6).
- 설명란: 국립문화유산연구원 「한국고고학사전」 천마총 · 국립경주박물관 특별전 「천마, 다시 날다」 — **텍스트 인용만**.
- 권리: 두 소스 모두 `rights_id = null` (연구 인용). `SRC_GNM_CHEONMA_EXHIBITION_001` 전시 자료 일부는 공공누리 4유형 → **도면·사진 트레이싱/캡처 금지**. NRICH 2019 간행물 「천마총, 발굴조사의 기록」 도면은 **RED** → 참조 이미지로도 사용 금지.

### 3.10 금지사항 (G13)
1. §3.3 의 4요소 (+ 선택: 목곽 윤곽) 외 어떤 유물·구조도 그리지 않는다.
2. 박물관·NRICH 도면을 트레이싱하지 않는다. 형태는 fact 문장으로부터 새로 그린다.
3. 사실적 인체·얼굴·유골 묘사 금지. AI 생성 금지 (자체 도식).
4. 금관 형태를 상세 묘사하지 않는다 (아이콘 수준). 실제 금관 모습은 뒤 샷 실물이 담당.
5. 치수 라벨 전부 표기 금지 (목관·목곽·궤·석단). SH005 는 `LAYOUT_001` 만 연결하며 그 fact 에 치수가 없다 (§5 #14).
6. `SIMPLIFIED DIAGRAM` 라벨 없이 내보내지 않는다.
7. 피장자 신원·왕 이름·의미 해석 라벨 금지.

---

## 4. G12 출처 슬레이트 — 소스 목록 · 권리 경고

### 4.1 EP01 fact 가 참조하는 소스 (텍스트 인용 대상, 설명란 크레딧)
EP01 fact = `CLM_EP01_*` 13건 + `CLM_CHEONMACHONG_LAYOUT_001`.

| source_id | 제목 | 기관 | 참조 fact | 비고 |
|---|---|---|---|---|
| `SRC_UNESCO_GYEONGJU_001` | UNESCO World Heritage — Gyeongju Historic Areas | UNESCO World Heritage Centre | TOMBS_001 · TUMULI_002 · MOUND_011 · MODERN_012 | **텍스트 인용만. 영상·사진 All Rights Reserved (RED)** |
| `SRC_GNM_CHEONMA_EXHIBITION_001` | 특별전 「천마, 다시 날다」 — 천마총 구조·부장품 | 국립경주박물관 | LAYOUT_001 · EXCAV_003 · FUNERAL_008 · GOODS_005 · STRUCT_004 | 전시 자료 일부 공공누리 4유형 → 이미지 재사용은 별도 권리 확인 |
| `SRC_GNM_SILLA_GOLD_001` | 「신라, 황금의 나라」 | 국립경주박물관 | GOLD_007 · DISPLAY_009 · ORDER_010 · MOUND_011 | G07 화면 출처 라벨 대상 |
| `SRC_NRICH_CHEONMACHONG_DICT_001` | 한국고고학사전 「천마총」 | 국립문화유산연구원 | LAYOUT_001 · OCCUPANT_006 · STRUCT_004 | G13 주 근거 |
| `SRC_NRICH_CONFERENCE_2023_001` | 『천마총과 동아시아 고분문화』 학술대회 자료집 (2023) | 국립문화유산연구원 | FUNERAL_008 · ORDER_010 · RITES_013 | 전문 미열람 — 특정 결론 귀속 금지. RITES_013 은 used_in 비어 있음 |
| `SRC_KOREA_KR_CHEONMADO_001` | 천마총 천마도 정부 설명 | korea.kr 정책브리핑 | GOODS_005 | — |

참고 (EP01 화면 주장 근거가 아니라 복식 Historical QA, D-011 용 — 슬레이트 포함 여부 미정 (편집 시 결정)): `SRC_AKS_ENCYKOREA_BOKSIK_001` (한국학중앙연구원) · `SRC_NAHF_SILLA_CLOTHING_001` (국사편찬위원회) · `SRC_SAMGUKSAGI_SAEKBOK_001` (김부식 편 / 국사편찬위원회) · `SRC_NMK_GEUMNYEONGCHONG_RIDER_001` (국립중앙박물관) · `SRC_KCULTURE_SILLA_TOU_001` (한국공예·디자인문화진흥원) · `SRC_KHAN_STRAW_SHOE_POTTERY_001` (경향신문) · `SRC_KPEA_CHEONMACHONG_TEXTILE_001` (육영수·김상용).

### 4.2 영상 이미지 자산 권리 (G12 화면 크레딧 대상 — 실제 사용한 것만)

| rights_id | 자산 | 라이선스 | 상태 | 샷 참조 | 슬레이트 문구 (attribution_text) |
|---|---|---|---|---|---|
| `RTS_NRICH_1973_PHOTOS_001` | 1973 천마총 발굴사진 | KOGL Type 1 | GREEN · ACTIVE | S03_SH002/003, S04_SH001/007, S05_SH003, S06_SH003/009, S07_SH002, S09_SH001 | Source: National Research Institute of Cultural Heritage (NRICH), Cheonmachong excavation photographs, 1973, KOGL Type 1. |
| `RTS_GNM_GOLD_CROWN_001` | 천마총 금관 | KOGL Type 1 | GREEN · ACTIVE | S02_SH003, S03_SH004, S05_SH001/006, S06_SH004/006, S07_SH001/003/004, S09_SH002 | Source: Gyeongju National Museum, Gold crown from Cheonmachong, KOGL Type 1. |
| `RTS_GNM_GOLD_GIRDLE_001` | 천마총 금허리띠 | KOGL Type 1 | GREEN · ACTIVE | S05_SH001/004 | Source: Gyeongju National Museum, Gold girdle from Cheonmachong, KOGL Type 1. |
| `RTS_WIKI_CHEONMADO_001` | 천마도 | Public Domain Mark | GREEN · ACTIVE | S02_SH003, S03_SH004 | Cheonmado (Heavenly Horse painting), Public Domain, via Wikimedia Commons. |
| `RTS_GNM_OTHER_OBJECTS_001` | 귀걸이·유리·토기·말갖춤 | 페이지별 확인 (KOGL 1 또는 4) | **YELLOW** (편집 확정 전 필수 해소, D-014) | S02_SH003, S05_SH001 | attribution_text 없음 → 해소 전 기재 불가. 4유형이면 사용 금지 |
| `RTS_WIKI_GOLD_CROWN_002` | 금관 (Commons) | CC BY 2.0 | GREEN · BACKUP_ONLY | 없음 | 저작자명 미확정 — 백업 사용 시에만 |
| `RTS_WIKI_DAEREUNGWON_001` | 대릉원 2006 | CC BY-SA 2.0 | YELLOW · BACKUP_ONLY | 없음 | SA 수용 결정 전 사용 금지 |
| `RTS_WIKI_CHEONMACHONG_ENTRANCE_001` | 천마총 입구 | CC BY-SA 2.0 | YELLOW · BACKUP_ONLY | 없음 | 동일 |
| `RTS_GYEONGJU_CITY_IMAGE_001` | 경주시 관광 이미지 | 출처표시, 상업 범위 불명확 | YELLOW · BACKUP_ONLY | 없음 | 수익화 사용은 서면 확인 후 |

- 화면 슬레이트 = legacy 짧은 형식 · 설명란 = 위 `attribution_text` **글자 그대로**.
- **GREEN 레코드 4건 모두 `proof: null`** — 파일별 라이선스 캡처 저장 필요.

legacy G12 2행 `Gyeongju National Museum artifacts — applicable KOGL Type 1 assets` 는 금관·금허리띠(GREEN)는 해당, `RTS_GNM_OTHER_OBJECTS_001` (YELLOW) 은 해소 전 포함 불가.

### 4.3 RED — 이미지로 절대 등장 금지 (연구 참고만)

| rights_id | 자산 | 이유 | 영향 그래픽 |
|---|---|---|---|
| **`RTS_NRICH_2019_PUBLICATION_001`** | 국립문화유산연구원 「천마총, 발굴조사의 기록」 (2019) | KOGL Type 4 — 상업·변경 불가. 캡처·재사용 금지 | G04 · G05 · **G13** 도면 참조/트레이싱 금지. G12 에 이미지 크레딧으로 기재 금지 |
| **`RTS_UNESCO_NHK_VIDEO_001`** | UNESCO / NHK 경주 영상 | All rights reserved. 리핑 금지 | G01 · G03 배경/참조 금지. `SRC_UNESCO_GYEONGJU_001` 은 텍스트 인용만 |

---

## 5. 정합성 점검 — legacy spec ↔ 샷 JSON / 대본 v2 (보고만, 수정하지 않음)

| # | 항목 | legacy spec | 샷 JSON / 기타 | 차이 종류 (D-010) | 비고 |
|---|---|---|---|---|---|
| 1 | G06 화면 문구 | `WHO WAS BURIED HERE?` / `UNKNOWN WITH CERTAINTY` | `OCCUPANT: UNCERTAIN` (X2) | 내용 → Script 우선 | 이미 RESOLVED. v2 반영함 |
| 2 | 번호 없는 카드 | G01–G12 에 없음 | `EP01_S06_SH008` `NO DIRECT QUOTATION` (ORIGINAL_GRAPHIC, "G08 계열") | 번호 체계 누락 | 대본 v2 GRAPHICS #8 에는 있음. G 번호 부여 여부 결정 필요 |
| 3a | G01 길이 | 0:18–0:25, 카드 1.5~2초 | SH003 7초 | 타이밍 | 샷 7초 = 배경 포함 구간으로 해석 가능. 충돌 아님 |
| 3b | G02 TC | 0:25–0:45 (20초), 모션 2.5~3.5초 | 0:25–0:42, 17초 | 타이밍 → Rough Cut 우선 | legacy TC 는 러프컷 이전 |
| 3c | G03 TC | 0:45–1:05 (20초) | 0:53–1:05, 12초 (0:42–0:53 은 S02_SH001 실사) | 타이밍 | — |
| 3d | G04 TC | 2:15–2:45 (30초) | 2:24–2:32, 8초 (2:15–2:24 은 S04_SH001 발굴사진) | 타이밍 | legacy "발굴사진과 번갈아" 는 SH001→SH002 로 분리됨 |
| 3e | G05 길이 | TC 없음, 단계당 0.8~1.2초 (합 3.2~4.8초) | 16초 | 타이밍 | 16초 안의 나머지 11초 이상 처리 미정. 단계당 시간 늘릴지 결정 필요 |
| 3f | G06 TC | 1:55–2:10 | 2:04–2:15, 11초 | 타이밍 | — |
| 3g | G07 TC | 3:45–4:05 | 3:36–3:52, 16초 | 타이밍 | — |
| 3h | G08 길이·형식 | 4:20 전후 **2초 카드 또는 모서리 라벨** | 4:20–4:27, 7초 전용 샷 | 타이밍/형식 | 대본 v2 는 "Small label `INTERPRETATION`" → 라벨형·카드형 결정 필요 |
| 3i | G11+G12 | G11 3~4초 + G12 2~3초 (5~7초) | S09_SH005 한 샷 6초 | 타이밍 | 범위 안. G11/G12 분할 지점 미정 |
| 4a | G09 샷 | "AI 장면 좌하단 라벨" | 전용 샷 없음. 8개 AI 샷 `ai_label` 필드로 구현 | 구조 차이 | 누락 아님. ORIGINAL_GRAPHIC 11 샷 목록에는 안 잡힘 |
| 4b | G09 H05 이중 라벨 | `INTERPRETIVE RECONSTRUCTION` 보조 라벨 "함께 고려" | `EP01_S06_SH005.ai_label` 값은 `INTERPRETIVE RECONSTRUCTION` 한 개, notes 는 "둘 다 표시" | 필드/notes 불일치 | 필드가 단일 문자열이라 AI VISUAL RECONSTRUCTION 이 필드상 빠짐 |
| 4c | G10 샷 | "6:10 전후" | `EP01_S08_SH002` (AI_STILL) + `SH003` (REAL_SHOOT), 6:20–6:30. ORIGINAL_GRAPHIC 아님 | 타이밍 + 구조 | 편집 전환이므로 그래픽 샷 목록에 없음 |
| 4d | G10 위치 (대본) | — | 대본 v2 는 매치컷을 4:20–5:20 MINDSET 구간 끝 (`[REAL] Match cut from reconstructed mound to modern mound`) 에 둠. 러프컷·샷은 S08 6:20 | 배치 → Rough Cut 우선 | **SCRIPT_ROUGHCUT_DELTA X1–X4 에 기재 안 됨** |
| 5 | G13 | 없음 | `EP01_S07_SH005` 3초 (X3) | 신규 | v2 에 추가함 |
| 6 | G04 레이어 순서 | 관 → 목곽 → **부장품 공간** → 돌/자갈 → 흙 봉분 | 샷 purpose: 관 → 목곽 → 돌무지 → 흙 봉분 (부장품 층 없음) · `LOC_CHEONMACHONG_V01.layer_order`: [coffin + grave-goods chest] → wooden chamber → stones → earth mound | 내용 (구조 표현) → Script 우선 | **판정 근거: 대본 v2 L47** `coffin → wooden chamber → stone/gravel → earth mound` (별도 부장품 층 없음) → D-010 (내용 차이 = Script 우선) 에 따라 대본 순서가 기준. fact `LAYOUT_001` (궤는 목관 머리맡, 목곽 안) 과도 일치. legacy 의 별도 "부장품 공간" 층은 제외 → **RESOLVED (D-026)**: coffin → wooden chamber → stone/gravel → earth mound, 부장품은 관·목곽 주변 배치로만 표시 |
| 7a | G04 fact_ids | "돌/자갈" | fact_ids = STRUCT_004 · LAYOUT_001. "자갈(gravel)" 은 `CLM_EP01_TUMULI_002` 에만 있음 | 근거 연결 누락 | **gravel 유지** (대본 v2 L47 `stone/gravel`). `CLM_EP01_TUMULI_002` 를 `EP01_S04_SH002.fact_ids` 에 연결해야 함 (샷 JSON 수정은 이 문서 범위 밖) |
| 7b | G05 fact_ids | STEP 2 부장품 배치 | fact_ids = STRUCT_004 뿐. 부장품 위치 근거 `LAYOUT_001` / `GOODS_005` 미연결 | 근거 연결 누락 | — |
| 8 | G13 명칭 | — | purpose "금관 위치 **단면**" 이나 근거 사실(머리 동쪽·T자)은 평면 관계 | 형식 → 내용 변경 | 대본 v2 L161 · fact notes · purpose 모두 cross-section. T자는 평면도 필요, 긴 동서 단면은 머리 동쪽·금관·머리맡 궤만 표현 가능. **RESOLVED (D-026)**: 동서 옆 단면 + T자만 보여주는 작은 평면 인서트 (§3.5) |
| 9 | G02 `SILLA CAPITAL` | 라벨 있음 | 근거 `CLM_EP01_TOMBS_001` 본문에 "신라 도읍" 없음 (소스 `SRC_UNESCO_GYEONGJU_001` 요약에만 있음) | 근거 텍스트 부족 (부분 지지) | `CLM_EP01_GOLD_007` ("built huge tombs in the capital") 이 부분적으로 뒷받침. 완전한 해결은 `CLM_EP01_TOMBS_001` 본문에 "Silla capital" 추가 (UNESCO 요약이 뒷받침) |
| 10 | 대본 v2 추가 그래픽 (샷 없음) | — | `ROYAL TOMBS · SILLA` (대본 0:00 구간 minimal text — G01 은 0:18 이므로 충돌 아님) · `Cheonma = Heavenly Horse` · `Empty ground cross-section` · "date + site plan" (1973 사진 대체) — 전용 ORIGINAL_GRAPHIC 샷 없음 | extra script graphic with no shot | 기록만. DELTA 에는 기재 안 됨 |
| 11 | G08 계열 카드 대본 문구 | — | 대본 v2 GRAPHICS #8 = `INTERPRETATION / NO DIRECT QUOTATION` 를 한 항목으로 묶음 · 샷은 SH001(G08) 과 SH008 로 분리 | 배치 | 충돌 아님, 기록만 |
| 12 | 1973 사진 권리 표기 | legacy G12 "NRICH 1973 excavation photos — KOGL Type 1" | `RTS_NRICH_1973_PHOTOS_001` = GREEN, 그러나 `EP01_S03_SH002.notes` 는 "사진마다 라이선스 확인 (C1 YELLOW)" | 권리 표기 불일치 | 샷 notes 가 P3 이전 문구로 보임. 파일별 proof 캡처 여부 확인 필요 (rights `proof: null`) |
| 13 | 총 길이 | — | 샷 49개 합계 425초 (7:05) — CURRENT_STATUS 와 일치 | 일치 | — |
| 14 | G13 치수 근거 | — | **SH005 does not link STRUCT_004** — `EP01_S07_SH005.fact_ids` = `LAYOUT_001` 만. 목관·목곽 치수는 STRUCT_004, 궤 1.8 m 는 어떤 fact 에도 없음 | 근거 연결 누락 | G13 에서 치수 라벨·크기 비교 전부 제거함 (§3.3, §3.10 #5) |
| 15 | G13 내레이션 hedge | — | "It belonged to a burial system of status, ceremony, and identity" (대본 v2 5:20–6:05) = 해석적 진술. SH005 에 이를 뒷받침하는 fact 없음, hedge 없음 | 내용 (해석 무hedge) | **RESOLVED (D-026)**: 대본 수정 → "It may have belonged to a burial system of status, ceremony, and identity." (DELTA X5) |

---

## 6. 미결 — 소유자 결정 목록

**Blocking (편집 착수 전 필요)**
- **A** G13 화면 문구 (§3.6) — 형식은 해결됨: 동서 단면 + T자 평면 인서트 (D-026)
- ~~**B** G04 레이어 순서~~ → 해결됨 (D-026): coffin → wooden chamber → stone/gravel → earth mound, 별도 부장품 층 없음 (§5 #6)
- **C** G08 카드형 vs 모서리 라벨형 · G05 16초 사용 방식 (§5 #3e, #3h)
- **D** G05 / G04 / G08 영문 문구
- **E** 스타일 시트 1장: 서체 · 남색/금색 HEX · 텍스트 색 · 로고 파일
- **F** H05 이중 `ai_label` (§5 #4b) — G13 내레이션 hedge 는 해결됨 (D-026, §5 #15)

**Can wait (나중에 결정 가능)**
- 인/아웃 지점, TC (내레이션 녹음 후)
- G04 / G06 화면 출처 라벨 여부
- G11 다음 화 예고 1줄
- `NO DIRECT QUOTATION` 의 G 번호 (§5 #2)
- 지도 라벨 표기 (G02)
- 슬레이트에 참고 소스 (복식 QA 소스) 포함 여부
- `RTS_GNM_OTHER_OBJECTS_001` YELLOW 해소 — 최종 편집 전
- `EP01_S03_SH002` notes 권리 문구 (§5 #12)
