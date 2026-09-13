# CURRENT STATUS — 지금 어디까지 왔나

> **매 작업마다 갱신한다.** 이 파일 하나만 읽으면 어느 봇/AI 창을 열어도 바로 이어갈 수 있어야 한다.
> 갱신: 2026-09-13 (Claude Code, D-023 반영 · P2 완료) · 마지막 사용자 승인: 2026-09-11 (P0 범위·EP01 파일 유지·push 전 확인 → D-007)
> 읽는 순서: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` → `BOT_BOOTSTRAP_PROMPT.md` → **이 문서** → `OS_INDEX.md` → `02_SEASONS/S01/EP01/episode.json`

---

## 지금 우선 작업

**사용자 손에 있는 것**
- ~~P-001~~ EP01 예산 **₩40,000 확정 (D-015)** → Money Gate OPEN.
- P-002 에피소드 ID 자릿수 (`EP01` 유지 vs `EP001` 통일).
- P-003 표준 문서 언어 (P0 초안은 한글 본문 + 영문 키/ID).
- `p1-continuity` → main 병합 시점 (D-012: 다음 검수 게이트 전까지 보류).

- ~~P-009~~ 원로 옷 색 muted blue · 과대 bronze 확정 (D-015), PROBABLE 유지.

- **다음 순서 (D-016)**: ① 배치 1 Work 판정 → ② hero 배경 기와지붕 시대 위반 여부 → ③ H07 정지/영상 매치컷 결정 → ④ Master Pack 확장 → ⑤ Web HQ 는 main 병합 때. 생성 시 **Sent Prompt Rule** (저장 → 그대로 전송 → 기록 연결, 어기면 FAIL).
- **2026-09-13 전체 검수 수정 1–5 완료 (유료 없음, `6c66f13` push)** → `02_SEASONS/S01/EP01/15_QA/REVIEW_FIX_20260913.md`. 실제 전송 프롬프트 버전화 · provider job 기록 · 검증기 Money Gate 규칙 · negative 25개 보강 · 예산 소진 일치. 검증 244/244.
- **P-012** 크레딧→KRW 환산율 — **임시 미정 (사용자 2026-09-11)**: 플랜 월 요금·월 크레딧 수 확인 전까지 크레딧 단위로만 기록, 원화 소진율 계산 안 함.
- **배치 1 판정 (D-017)**: front · three_quarter_left · full_body APPROVED. hero V03 (배경 편집) **APPROVED** → **4장 완료**. 나머지 6 + back_view 는 새 approval 필요. 배치 1 승인 호출 6/8 사용.
- ~~P-011~~ **라우터 49건 잠금 (D-024)**: 46 ACCEPTED · H01·H03 → FLOW_VEO · H07 AI_STILL · **EP01 Higgsfield 0건**. 실제 AI 생성은 별도 승인 + Money Gate.
- YELLOW_ACTIVE 1건 (`RTS_GNM_OTHER_OBJECTS_001`) — 편집 확정 전 필수 해소 (D-014).

**봇이 바로 갈 수 있는 것**
- graphics-spec v2 (G13 추가) — legacy HTML 은 수정하지 않고 새 문서로.
- P5 Review UI / P6 Money Gate 어댑터 설계 (유료 없음).

**유료 생성 현황 (D-015)**: Money Gate OPEN (₩40,000 / 소진 44.12 credits, KRW 환산 P-012). **P2 Character Master 완료 (D-023)**: 원로 FULL 10/10 · 노동자 LITE 3/3 · 시종 LITE 3/3 전부 CHARACTER_MASTER_APPROVED. 라우터 잠금 (D-024). 다음 유료는 Master Frame S04 · S06 → AI 샷 (Flow/Veo 는 별도 비용 게이트).

## P2 사전 점검 — Pre-flight (2026-09-11 · DONE, 생성 0)

리포트 `02_SEASONS/S01/EP01/15_QA/P2_PREFLIGHT_REPORT.md`. 순서(사용자 고정): Lock 확인 → Master Pack 요구 → 복식 TBD → Reference Set → FULL/LITE → Master Frame 후보 → **사람 승인** → 유료 생성.

| 단계 | 결과 |
|---|---|
| Character lock 3 · Costume lock 3 | 영문 전용, character 인스턴스와 일치. 전부 DRAFT → 승인 대기 (항목 A) |
| Master Pack 요구 ↔ 프롬프트 | 17 = 17 (원로 10 + back_view 1 · 노동자 3 · 시종 3) |
| 복식 TBD | 0. 잔여 INTERPRETIVE = P-009 (옷 색·과대), lock 은 hedge 상태 |
| Reference Set | 3층 계보 (Master Pack → Master Frame → AI 샷). S05_SH005 프롬프트의 유령 참조 `EP01_S05_MASTER_V01` 제거. 검증기에 `reference_images` 실존 규칙 추가 (음성 테스트 통과) |
| FULL / LITE | 원로 FULL · 군중 2 LITE_CROWD 유지, 승격 대상 없음 (사람 확인 항목 C). H02 푸시인이 특정 얼굴에 머물면 재검토 |
| Master Frame 후보 | S04 · S06 DRAFT 2 (Master Pack 승인 뒤 생성) |
| 승인 | **D-015**: A✔ lock 6 APPROVED · B✔ muted blue + bronze · C✔ LITE 유지 · D✔ back_view 보조 · E 보류(AI 샷 직전) · F✔ ₩40,000 OPEN |

## P2 준비 — 프롬프트·카메라·마스터프레임 초안 (2026-09-11 · DONE, 생성 0)

| 항목 | 산출 | 상태 |
|---|---|---|
| Lock 라이브러리 (§8) | `06_PROMPT_LIBRARY/locks/` 11 조각 — GLOBAL · ERA `SILLA_EARLY_V01` · LOCATION `LOC_CHEONMACHONG_V01` · COSTUME 3 · CHARACTER 3 · STYLE · NEGATIVE | DRAFT (GLOBAL/STYLE/NEGATIVE 는 정본 인용이라 APPROVED) |
| Master Pack 프롬프트 | `11_AI_STILLS/prompt_PRM_MP_*` 17 — 원로 10 + 뒷모습 1 · 노동자 3 · 시종 3 (IMAGE) | DRAFT |
| AI 샷 프롬프트 | `12_AI_VIDEO/` 6 (H01–H05) · `11_AI_STILLS/` 2 (H06 · H07) — legacy APPROVED 팩을 shot_delta 로, lock 조립 `assembled_text` 저장 | DRAFT |
| 카메라 | `10_BLENDER/camera_CAMERA_EP01_*_V01.json` 8 (렌즈·높이·모션·배우 위치·키 비율) — 수동 초안 | DRAFT |
| Master Frame | `07_SHOTS/master_frame_EP01_S04_MASTER_V01` · `_S06_MASTER_V01` (path 없음, 승인 전) | DRAFT |
| 검증 | camera / prompt / master_frame 인스턴스 + 상호참조 (shot ↔ camera ↔ prompt ↔ master_frame) → 231/231 PASS | DONE |

## P4 — Shot Router (2026-09-11 · DONE · **최종 잠금 D-024 2026-09-13**)

| 항목 | 산출 | 상태 |
|---|---|---|
| 라우터 판정 | `07_SHOTS/router_decision_RTR_EP01_*_V01.json` 49건 — 점수 6종 + recommended/fallback/reason/rule | `PENDING` |
| 재판정 결과 | legacy Higgsfield 8 → **HIGGSFIELD 1** (H07 매치컷) · **BLENDER_FLOW 6** (H01–H05) · **AI_STILL 1** (H06) | 샷 `pipeline` 갱신, `status = ROUTED` |
| 최종 구성 (D-024) | REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · **HIGGSFIELD 0** | 46 ACCEPTED · 3 OVERRIDDEN (H01 · H03 · H07) · `15_QA/P011_ROUTER_FINAL.md` |
| 권리 등급 | `rights.usage_tier` ACTIVE / BACKUP_ONLY — YELLOW_ACTIVE 1 · YELLOW_BACKUP 3 | D-014 |
| 자동 FAIL 추가 | BACKUP_ONLY 참조 · AI 샷 라우터 없음 · 샷 파이프라인 ≠ 판정(OVERRIDDEN 아님) | 음성 테스트 통과 |
| 리포트 | `15_QA/P4_ROUTER_REPORT.md` | DONE |
| 검증 | 196/196 PASS, refs OK | DONE |

## P3 — Source/Rights Ledger (2026-09-11 · DONE, 브랜치 `p1-continuity`)

| 항목 | 산출 | 상태 |
|---|---|---|
| SOURCE | research-v2 S1–S6 전부 `05_HISTORY_DATABASE/sources/` (복식 7건 포함 총 13) | DONE |
| FACT | `facts/CLM_EP01_*_001–013` (FACT 9 · INTERPRETIVE 4, hedge 필수) + 천마총 배치 1 + 복식 8 = 22 | DONE |
| RIGHTS | `rights/` 11 — GREEN 5 (NRICH 1973 · 금관 2 · 허리띠 · 천마도) · YELLOW 4 · RED 2 (2019 간행물 · UNESCO/NHK) | DONE, YELLOW 는 P-010 |
| 샷 연결 | 49 샷 전부 `fact_ids` + `evidence_role` (PRIMARY 16 · SUPPORTING 21 · CONTEXT 9 · NONE 3), ARCHIVE 20 샷 전부 `rights_ids` | DONE |
| 자동 FAIL 규칙 | `validate.py ledger_rules()`: 출처 미연결 / ARCHIVE 권리 미연결 / RED 권리 사용 / 샷 등급 > 근거 등급(과도한 해석) / AI 라벨 누락 / INTERPRETIVE 사실 hedge 누락 | DONE (음성 테스트 통과) |
| 리포트 | `02_SEASONS/S01/EP01/15_QA/P3_LEDGER_REPORT.md` (스크립트 생성) | DONE |
| 검증 | 147/147 PASS, refs OK, FAIL 0 | DONE |

---

## P1 — Continuity Engine (2026-09-11 · **COMPLETE — APPROVED WITH CONDITIONS** D-008~D-012)

브랜치 `p1-continuity` (`6a60b1b` `a89734b` origin push 완료, main 병합 보류). **Web HQ 는 main 만 배포하므로 P1 COMPLETE 표시는 병합 시점에 동기 반영** (사용자 결정, 2026-09-11). P2 백로그: P-008 인물 가시성 필드. 조건: Lite Crowd Pack (D-008) · AI 컷 5–6초 (D-009) · 러프컷 임시 기준 + DELTA 정리 (D-010) · 복식 TBD 게이트 (D-011).
**P2 COMPLETE — Character Master** (원로 D-019 · 군중 D-023, 2026-09-13).

| 항목 | 산출 | 상태 |
|---|---|---|
| ERA | `05_HISTORY_DATABASE/era/` `SILLA_EARLY` · `EXCAVATION_1973` · `PRESENT_DAY` | DONE |
| LOCATION | `locations/` 대릉원 · 천마총(치수 47 m/12.7 m, 목곽 6.6×4.2 m) · 경주 도심 · 국립경주박물관 | DRAFT |
| COSTUME | `costumes/` 노동자 · 시종 · 원로 `_A01` — **D-011 근거 확정 완료** (PROBABLE, fact_ids 연결) | DRAFT |
| FACT / SOURCE (복식) | `facts/CLM_SILLA_COSTUME_001–008` · `sources/SRC_*` 7건 (국사편찬위·삼국사기 색복·국립중앙박물관·민족문화대백과·전통문화포털·1976 직물 논문·짚신 토기 보도) | DONE |
| CHARACTER | `characters/` 원로 1인 (FULL) + 군중 2그룹 (LITE_CROWD) | DRAFT |
| Master Pack 요구 목록 | `characters/EP01_MASTER_PACK_REQUIREMENTS.md` | DONE |
| 씬·샷 분해 | `02_SEASONS/S01/EP01/07_SHOTS/` 씬 9 · 샷 49 (러프컷 v1 기준 + D-009 분할 + X3 G13 추가, 합계 425초 = 7:05) | `BROKEN_DOWN` / `PLANNED` |
| 대본↔러프컷 차이 | `02_SEASONS/S01/EP01/05_SCRIPT/SCRIPT_ROUGHCUT_DELTA.md` X1–X4 **4/4 RESOLVED** (X3 → G13 금관 위치 단면 신규, S4 근거) | DONE |
| 검증 | `validate.py` 인스턴스 + ID 상호참조 + Master Pack 등급 + 복식 TBD 게이트 → 119/119 PASS, refs OK | DONE |

샷 구성 (49): REAL 10 · ARCHIVE 20 · GRAPHIC 11 · HIGGSFIELD 8 (AI 45초 ≈ 11%, 모든 AI 컷 ≤ 6초). 백로그: G13 은 graphics-spec v2 에 추가 필요 (legacy HTML 수정 금지).
`fact_ids` 는 비어 있다 (P3 에서 연결). 출처는 샷 `notes` 에 research-v2 S1–S6 번호로 표기.

## P0 — OS 정본 문서·스키마 (2026-09-11 · DONE, push 완료 `6a7158a`)

폴더 골격 · 29 스키마 · EP01 매니페스트 · 운영 문서 4종 · 표준 22개 v0.1 DRAFT · OS_INDEX + Web HQ.

---

## EP01 「경주 왕릉 / 천마총」 — Why Are Giant Tombs Everywhere in This Korean City? (ACTIVE)

**현재 게이트: `REAL_SHOOT`** (프리프로덕션 ≈91%) · 매니페스트 `02_SEASONS/S01/EP01/episode.json` · Web HQ `episodes/ep01-gyeongju-tombs.html`

| 단계 | 산출물 | 상태 |
|---|---|---|
| RESEARCH | `episodes/ep01-research-verified-v2.md` | APPROVED |
| SCRIPT | `episodes/ep01-production-script-v2.md` (v1은 PREVIOUS) | APPROVED |
| SHOTLIST | `ep01-visual-assets`, `ep01-graphics-spec` (G01–G12) | APPROVED |
| SCENE_BREAKDOWN | `02_SEASONS/S01/EP01/07_SHOTS/` 씬 9 · 샷 49 | DRAFT (P1, 조건부 승인) |
| SOURCE_FACT_QA | `05_HISTORY_DATABASE/{sources,facts,rights}/` + `15_QA/P3_LEDGER_REPORT.md` | DONE (P3) · YELLOW_ACTIVE 1건 편집 전 해소 |
| SHOT_ROUTER | `07_SHOTS/router_decision_*` 49 + `15_QA/P4_ROUTER_REPORT.md` | DONE (P4) · **잠금 D-024** |
| REAL_SHOOT | `ep01-field-shoot-plan` 체크리스트 | 계획 APPROVED · **촬영 미실행** |
| ARCHIVE | `ep01-archive-photos` (1973 NRICH), `ep01-artifact-library` | 선별 APPROVED · 파일 다운로드 미실행 |
| AI 재현 | legacy `ep01-higgsfield-prompts` 7컷 → 라우터 D-024: BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · Higgsfield 0 | Character Master 승인 완료 (D-023) · 다음 Master Frame S04 · S06 → AI 샷 (별도 승인) |
| ROUGH_CUT | `ep01-premiere-roughcut` 0:00–7:05 | 설계 APPROVED |

**다음 실제 작업 (순서)**
1. 경주 현장 촬영 (좁은 주제 + 넓은 클러스터 촬영: 불국사·다보탑/석가탑·석굴암·첨성대·박물관·월정교/동궁). 매치컷 착지 구도(`EP01_S08_SH003`)는 반드시 삼각대로 찍고 `LOC_GYEONGJU_DAEREUNGWON_V01.spatial_lock.match_cut_frame` 에 기록.
2. 유물/아카이브 실제 파일 다운로드·정리 → `02_SOURCES/` 에 `source.json` / `rights.json` 인스턴스.
3. 필요한 Higgsfield 컷만 선별 생성 (Character Master Pack + Money Gate 승인 후).
4. 내레이션 녹음 → Premiere 러프컷 → 수정 → 공개.

**주의**: OS 예시의 `EP001_HWANGNYONGSA` 는 템플릿. 활성 EP01 을 덮어쓰지 않는다 (D-006).

---

## Money Gate

| 항목 | 값 |
|---|---|
| EP01 예산 | **₩40,000** (D-015) — `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` |
| 소진 | 44.12 credits (23 호출: 원로 13 · 군중 10) — KRW 환산 P-012 |
| 게이트 상태 | `OPEN` — 배치 1 승인 `APR_EP01_MP_ELITE_BATCH1_001` |

---

## 검수 요청 (needs_review)

- `00_SYSTEM/standards/*.md` 22개 v0.1 DRAFT — 사용자 승인 시 ACTIVE (P-004).
- P1 인스턴스 전체 DRAFT — 특히 `CHAR_SILLA_ELITE_OBSERVER_01` 인물 설정(피장자·왕 아님)과 복식 방향.

---

## 차단 / 미결

- ~~예산 미확인~~ → D-015 ₩40,000 OPEN. 배치 1 생성은 Higgsfield 연결(MCP 인증) 필요.
- Blender 로컬 브리지(P7) 없음 → `camera.json` 은 수동 작성 단계.
- ~~복식 세부 근거 미확보~~ → 2026-09-11 해소 (D-011 게이트 통과). 잔여: 짚신 출처가 언론 보도 → P3 에서 박물관 페이지로 교체 권장.

---

## 최근 변경 (최신순)

- **2026-09-13 사용자** — **D-024.** P-011 종결: 라우터 49건 잠금 (46 ACCEPTED · H01 · H03 → FLOW_VEO · H07 AI_STILL), `FLOW_VEO` 스키마 추가, **EP01 Higgsfield 0건**. 검증기: 라우터 PENDING 샷 generation FAIL.

- **2026-09-13 사용자** — **D-023.** 군중 2단계 4장 APPROVE → 노동자·시종 CHARACTER_MASTER_APPROVED → **P2 Character Master 완료** (캐릭터 3/3). EP01 누적 44.12 credits.

- **2026-09-13 Claude Code** — 군중 2단계 4장 생성 (8 credits, 승인 10/12), 봇 판정 전부 PASS (참조 얼굴이 따라옴 · 노동자 걷기 정면 · 시종 옷감 새것 느낌 메모). `08_GENERATION_CACHE/EP01/MP_CROWD/REVIEW_CROWD_STEP2.md` → **사용자 확인 대기**. EP01 소진 44.12 credits.

- **2026-09-13 사용자** — **D-022.** 군중 full_body 2장 APPROVED (노동자 V02 · 시종 V04). 2단계 4장 진행.

- **2026-09-13 Claude Code** — 시종 full_body: 편집 2회 PARTIAL → 방법 A (명시 여밈 문구로 새로 생성) PASS. 군중 1단계 2장 준비 완료 (노동자 V02 · 시종 V04), **사용자 확인 대기**. 군중 승인 6/12, EP01 소진 36.12 credits.

- **2026-09-13 Claude Code** — 군중 full_body 편집 (사용자 OK, 4 credits, 승인 4/9): 노동자 공구 제거 PASS · 시종 PARTIAL (여자만 옷고름 제거) → 재편집 V04·PATCH_002 저장, **사용자 OK 대기**. EP01 소진 32.12 credits.

- **2026-09-13 Claude Code** — 군중 1단계 full_body 2장 생성 (4 credits, 승인 2/9). 노동자: 현대 쇠 공구처럼 보임 · 시종: 조선식 옷고름 → 각 편집 FIX 문장(V03)·PATCH 저장, **사용자 OK 대기**. `08_GENERATION_CACHE/EP01/MP_CROWD/REVIEW_CROWD_STEP1.md`. EP01 소진 28.12 credits.

- **2026-09-13 사용자** — **D-020.** 군중 LITE 6장 APPROVE (`APR_EP01_MP_CROWD_001`, 최대 9 호출). 1단계 full_body 2장부터.

- **2026-09-13 사용자** — **D-019.** 배치 2 7장 APPROVE → 원로 Master Pack 10/10, `CHARACTER_MASTER_APPROVED`. 다음 군중 LITE 6.

- **2026-09-13 Claude Code** — **배치 2 생성 (D-018).** 원로 나머지 7장 (three_quarter_right · profile · neutral_standing · walking · costume_detail · expression_sheet · back_view) — V02 문장 그대로 전송, 7/7 성공, 14 credits (승인 10 호출 중 7). 봇 판정 전부 PASS (profile 방향 반대 · back_view 비계 금속관 의심 · 모자 약간 높음 메모). 검수 시트 `08_GENERATION_CACHE/EP01/MP_ELITE/REVIEW_BATCH2.md` → **사람 검수 대기**. EP01 소진 합계 24.12 credits.

- **2026-09-13 사용자** — **D-018.** 배치 2 (원로 나머지 7장) APPROVE · H07 → AI_STILL (OVERRIDDEN) · Higgsfield 크레딧은 다른 작업과 공용, EP01 소진은 job 기록 합계로만.

- **2026-09-13 사용자 + Claude Code** — **D-017 배치 1 판정.** front · three_quarter_left · full_body APPROVED. hero 는 배경 조선식 기와지붕만 FIX → `PRM_…_HERO_V04` 저장 후 그대로 전송, 기존 이미지 편집 1회 (2 credits, 승인 6/8) → `MP_ELITE_HERO_V03_5de27748.png` 사용자 APPROVE → 배치 1 4장 완료. 소진 합계 10.12 credits.

- **2026-09-13 사용자** — **D-016.** `6c66f13` p1-continuity push 승인 (main 보류, 유료 정지 유지). Sent Prompt Rule 정본화 (AGENT_RULES §1 #8). 우선순위: 배치 1 Work 판정 → hero 기와지붕 → H07 → Master Pack 확장 → Web HQ(병합 시).

- **2026-09-13 Claude Code** — 전체 검수(09-11) 수정 1–5, 유료 생성 0. ① Higgsfield job 원문 복구 → 실제 전송 프롬프트 `HERO_V02`(soul_2 시도) · `HERO_V03` · `FRONT/THREE_QUARTER_LEFT/FULL_BODY_V02` + `PATCH_MP_ELITE_HERO_001` (재시도가 실패 항목 외 모델·전문까지 바꿨음을 기록) ② `generation.provider_job` (표시명 Nano Banana Pro = job type `nano_banana_2`) + `provider_jobs/HF_*.json` ③ 검증기 Money Gate 규칙 (승인·승인 범위·시도 수·전송 프롬프트 = assembled_text·cost 합계·episode 예산·Master Pack 슬롯·patch 역참조·negative ⊇ lock Forbidden) — 음성 테스트 12종 ④ negative 21개 보강 (시대·복식 lock 금지 항목, 이미 보낸 V01 4개는 기록으로 동결) ⑤ episode 예산 spent null. 스크립트 8개 `00_SYSTEM/tools/legacy_20260911/` 로 이동. 검증 244/244.

- **2026-09-11 사용자** — 공식 상태 고정: P2 배치 1 사람 검수 대기 (Work 창 위임, 판정만) / 유료 생성 정지 유지 / P-012 임시 미정, 크레딧 단위 기록.

- **2026-09-11 Claude Code** — **첫 유료 생성.** 원로 Master Pack 배치 1: hero V01 REJECTED(갑옷 인물·다홍·워터마크) → V02 PASS, front · three_quarter_left · full_body (hero 참조) PASS. 5 호출 8.12 credits. generation.json 5, cost 갱신, character MASTER_IN_PROGRESS, 검수 시트. P-012 등록.

- **2026-09-11 사용자** — **D-015.** P2 사전 점검 A–F 승인: lock 6 APPROVED, 원로 muted blue + bronze (PROBABLE 유지), LITE_CROWD 유지, back_view 보조 이미지, P-011 은 AI 샷 직전, **예산 ₩40,000 Money Gate OPEN**. Master Pack 은 원로 4장 배치부터.
- **2026-09-11 Claude Code** — D-015 반영: 복식 lock·인스턴스 갱신, 프롬프트 13 재조립, cost/approval 인스턴스, 검증기 캐시 등록, 배치 1 브리프 `11_AI_STILLS/MP_BATCH1_BRIEF.md`.

- **2026-09-11 Claude Code** — P2 사전 점검 완료 (`15_QA/P2_PREFLIGHT_REPORT.md`): lock·요구·TBD·Reference Set·등급·Master Frame 후보 점검, S05 유령 master_frame 참조 제거, 검증기 reference_images 규칙 추가. 생성 0. 검증 231/231. 승인 대기 A–F.
- **2026-09-11 Claude Code** — H: 드라이브 끊김 복구: fsck 통과, index.lock 정리, ba55720 push. D:\ddabong-korea-hq 비상용 클론 생성 (작업 클론은 H: 유지).

- **2026-09-11 Claude Code** — P2 준비: lock 11 · Master Pack 프롬프트 17 · AI 샷 프롬프트 8 · 카메라 8 · master_frame 2. 생성 0. 검증 231/231.
- **2026-09-11 Claude Code** — P4 Shot Router 완료 (D-014): 49 판정, Higgsfield 8 → 1, 권리 usage_tier, 검증 규칙 3종 추가, 리포트. 검증 196/196. P-011 등록.
- **2026-09-11 사용자** — **D-014.** `e5c4d39` push, 권리 등급 YELLOW_ACTIVE/BACKUP, P4 진입, 라우터 감독 기준.
- **2026-09-11 Claude Code** — P3 Source/Rights Ledger 완료 (D-013): 출처 13 · 사실 22 · 권리 11, 49 샷 fact/rights/evidence_role 연결, 자동 FAIL 규칙 6종, 리포트. 검증 147/147.
- **2026-09-11 사용자** — **D-013.** `b918b24` push, P3 진입, `evidence_role` 필드.
- **2026-09-11 Claude Code** — SCRIPT_ROUGHCUT_DELTA 4/4 정리: X2 문구 반영, X3 금관 위치 단면 G13 신규 샷 (`EP01_S07_SH005`, NRICH S4 근거 `CLM_CHEONMACHONG_LAYOUT_001`), 천마총 location 배치 정보 보강. 검증 119/119.
- **2026-09-11 Claude Code** — 복식 Historical QA (D-011 게이트 통과): 출처 7 · 사실 8 인스턴스, 복식 3종 전 항목 근거 등급 표기. 검증 115/115. P-009 등록.
- **2026-09-11 Claude Code** — D-008~D-012 반영: 스키마 `master_pack_tier`, 검증기 등급·복식 TBD 게이트, S04·S06 AI 컷 분할 (43 → 48 샷), SCRIPT_ROUGHCUT_DELTA, Web HQ P1 COMPLETE / P2 NEXT.
- **2026-09-11 사용자** — **D-008~D-012.** P1 APPROVED WITH CONDITIONS. `6a60b1b` → `origin/p1-continuity` push, main 병합 보류.
- **2026-09-11 Claude Code** — P1 완료 (브랜치 `p1-continuity`): era 3 · location 4 · costume 3 · character 3 · Master Pack 요구 목록 · 씬 9/샷 43 · validate.py 상호참조 검사. P-005~P-007 등록.
- **2026-09-11 Claude Code** — P0 완료·push (`6a7158a`): 폴더 골격, 29 스키마, EP01 매니페스트, 운영 문서 4종, 표준 22개 DRAFT, OS_INDEX + Web HQ 페이지.
- **2026-09-11 사용자** — **D-007.** P0 범위 = 핵심 완성 + 나머지 골격 / EP01 파일 제자리 유지 + 매니페스트 / 커밋 후 push 전 확인.
- **2026-09-11 (이전 세션)** — **D-004~D-006.** 정본 v0.1 채택, 캐릭터 스타일 B Documentary Reenactment, EP01 = 경주 왕릉/천마총, 황룡사는 예시. Bootstrap Prompt + Web HQ bot-handoff 페이지.
- **2026-08-16** — EP01 프리프로덕션 페이지 9종 완료 (research v2 · script v2 · visual · field shoot · archive · artifacts · higgsfield · graphics · roughcut).
- **2026-08-14 사용자** — **D-001~D-003.** 브랜드명 DDABONG KOREA · 슬로건 STORIES BEHIND KOREA · 핵심 콘셉트 · 파일럿 3편 (경주 왕릉 → 신라 금관 → 온돌).
