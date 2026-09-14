# CURRENT STATUS — 지금 어디까지 왔나

> **매 작업마다 갱신한다.** 이 파일 하나만 읽으면 어느 봇/AI 창을 열어도 바로 이어갈 수 있어야 한다.
> 갱신: 2026-09-14 오후 (Claude Code, D-035~D-043 · EP01 현재 시점 실사 10샷 전부 정지 이미지 확정) · 마지막 사용자 승인: 2026-09-14 (D-043 M2 V02 OK)
> 읽는 순서: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` → `BOT_BOOTSTRAP_PROMPT.md` → **이 문서** → `OS_INDEX.md` → `02_SEASONS/S01/EP01/episode.json`

---

## 지금 우선 작업

**2026-09-14 진행 (D-033 승인, 순서 1–3 샘플 완료 · 커밋 `61679a5`)**
1. ✔ 벤치마크 `09_ANALYTICS/benchmarks/BENCHMARK_ARCHDICT_GYEONGHOERU_20260914.md` (사용자 판정: 현장 촬영 0, 실사풍 = 사진→AI 재구성).
2. ✔ **D-033** 제작 방식 전환: 파이프라인 A (사진→AI) · B (3D 도해) 표준화, 인물 10% 유지, 스토리 엔진 템플릿.
3. ✔ 샘플 (DRAFT → 검수 통과 후 ACTIVE, D-034 #4): `standards/STORY_ENGINE_STANDARD.md` (7단계) + `EP01/03_STORY/STORY_ENGINE_EP01.md` (② 만 빈 칸) · `standards/PHOTO_AI_STANDARD.md` + `tools/photo_search.py` + `06_PROMPT_LIBRARY/templates/PHOTO_AI_REDESIGN_V01.md` + `shot.photo_ai` 스키마·검증 규칙 (부정 테스트 통과) · `standards/DIAGRAM_TEMPLATES.md` (GT-01~04).
4. 사진 후보 `EP01/15_QA/PHOTO_AI_CANDIDATES_20260914.md`: **GREEN 은 대릉원 경관 1장뿐** (Gagnon CC0 5018×3345). 천마총·석양·관람객은 YELLOW 만 → 수치만 옮기거나 촬영.
5. **다음**: 순서 4 전체 검수 (멀티 에이전트 + 반박, D-029) → 순서 5 EP01 시험 준비. **D-034 결정 완료**: ② 는 EP02 부터 · GREEN 없는 샷은 YELLOW 수치만 → 촬영 · A 첫 유료 시험 = S02_SH001 1장 (커넥터 재인증 뒤, 라우터 OVERRIDE·rights·prompt 선행) · 표준 3개는 검수 뒤 ACTIVE. **전체 검수 (D-029) 2026-09-14 완료** → `15_QA/REVIEW_FIX_20260914.md`.
6. ✔ **전체 검수 완료 (2026-09-14)** → `15_QA/REVIEW_FIX_20260914.md`: 치명 1 (photo_ai 규칙 YES/True) 포함 A 항목 26건 수정, 검증기 규칙 +6, tools 30개 legacy 이동, rights +1 (Gagnon CC0). 검증 336/336.
7. ✔ **D-035 (2026-09-14 오후)**: 보고서 §4 B 8건 전부 권고대로 승인 → 반영 완료. PRESENT lock 쌍 신설 · 라벨 `AI Visual Reconstruction (present-day, photo-based)` · I2V_MOTION 확장 · S02_SH001 시험 절차 · approval `prompt_ids`/`expected_attempts` 필수 + AI 컷 ≤ 6초 규칙 (photo_ai 예외) · `delegated` 필드 + D-030 한도 규칙 · CAMERA 기본값 · 표준 3개 ACTIVE. 검증 338/338, 부정 테스트 5/5.
8. ✔ **파이프라인 A 시험 1장 완료 · D-037 사용자 OK (2026-09-14 오후)**: `EP01_S02_SH001` V01 LOOK_APPROVED — `08_GENERATION_CACHE/EP01/AI_STILL/PA_S02_SH001_V01_9cbd059e.png` (2752×1536, 2 credits, Nano Banana 2 = D-036 파이프라인 A 기본). 검수 시트 `AI_STILL/REVIEW_PA_S02_SH001_V01.md`. EP01 누적 68.12 credits.
9. ✔ **D-038 현장 촬영 제외 → 전부 자체 제작** (사용자 "직접 촬영 말고"). REAL 9샷 → 파이프라인 A. GREEN 원본 +5 (CC0, `02_SEASONS/S01/EP01/02_SOURCES/`). **D-039 배치 1 (8장, 16 credits) 생성 완료** → `08_GENERATION_CACHE/EP01/AI_STILL/PA_*_V01_*.png` · 검수 시트 `AI_STILL/REVIEW_PA_BATCH1_20260914.md`. 봇 판정 PASS 7 · PARTIAL 1 → **D-040 사용자 8장 전부 OK → 7샷 LOOK_APPROVED** (파이프라인 A 누적 9/9 승인, 실패 0). D-026 완화 (착지 = 대릉원 봉분). EP01 누적 84.12 credits, 잔액 1658.58.
10. ✔ **D-041 캡처 21장 = RED** (유튜브 화면, `경주 사진 모음/` git 제외, 구도 연구만). **배치 2 텍스트 전용 4장 생성 완료** (8 credits): S01_SH001 거리 · S08_SH001 몽타주 M1·M2·M3 → `08_GENERATION_CACHE/EP01/AI_STILL/PA_S01_SH001_*.png` · `PA_S08_SH001_M*_*.png`, 검수 시트 `AI_STILL/REVIEW_PA_BATCH2_20260914.md`. → **D-042** 3장 OK + M2 재생성 (위임, 2 credits) → **D-043** M2 V02 OK. **REAL 10샷 전부 LOOK_APPROVED (파이프라인 A 14 생성 · 13 승인 · 28 credits).** 움직임은 I2V (P-012 뒤). EP01 누적 94.12 credits, 잔액 1648.58, 위임 누적 2/20.

**사용자 손에 있는 것**
- ~~P-001~~ EP01 예산 **₩40,000 확정 (D-015)** → Money Gate OPEN.
- P-002 에피소드 ID 자릿수 (`EP01` 유지 vs `EP001` 통일).
- P-003 표준 문서 언어 (P0 초안은 한글 본문 + 영문 키/ID).
- `p1-continuity` → main 병합 시점 (D-012: 다음 검수 게이트 전까지 보류).

- ~~P-009~~ 원로 옷 색 muted blue · 과대 bronze 확정 (D-015), PROBABLE 유지.

- ~~다음 순서 (D-016)~~ 전부 완료 (D-017~D-027): ① 배치 1 Work 판정 → ② hero 배경 기와지붕 시대 위반 여부 → ③ H07 정지/영상 매치컷 결정 → ④ Master Pack 확장 → ⑤ Web HQ 는 main 병합 때. 생성 시 **Sent Prompt Rule** (저장 → 그대로 전송 → 기록 연결, 어기면 FAIL).
- **2026-09-13 전체 검수 수정 1–5 완료 (유료 없음, `6c66f13` push)** → `02_SEASONS/S01/EP01/15_QA/REVIEW_FIX_20260913.md`. 실제 전송 프롬프트 버전화 · provider job 기록 · 검증기 Money Gate 규칙 · negative 25개 보강 · 예산 소진 일치. 검증 244/244.
- **P-012** 크레딧→KRW 환산율 — **임시 미정 (사용자 2026-09-11)**: 플랜 월 요금·월 크레딧 수 확인 전까지 크레딧 단위로만 기록, 원화 소진율 계산 안 함.
- **배치 1 판정 (D-017)**: front · three_quarter_left · full_body APPROVED. hero V03 (배경 편집) **APPROVED** → **4장 완료**. ~~나머지 6 + back_view 는 새 approval 필요~~ → D-019 로 원로 FULL 10/10 완료.
- ~~P-011~~ **라우터 49건 잠금 (D-024)**: 46 ACCEPTED · H01·H03 → FLOW_VEO · H07 AI_STILL · **EP01 Higgsfield 0건**. 실제 AI 생성은 별도 승인 + Money Gate.
- ~~YELLOW_ACTIVE 1건~~ **해소 (2026-09-13)**: `RTS_GNM_OTHER_OBJECTS_001` → 유리잔·금제 관모·가슴걸이·천마무늬 말다래 GREEN 1유형 분리 (페이지 원문 proof 저장), 원본은 BACKUP_ONLY. 유리잔·말다래 해상도 **해결** — e뮤지엄 1유형 3000px급 페이지로 출처 교체 (2026-09-13). 가슴걸이 2000×3000·금제 관모 3000×2000 실측 → 4건 모두 1080p 가능.

**봇이 바로 갈 수 있는 것**
- ~~graphics-spec v2 (G13 추가)~~ 완료 → `14_EDIT/GRAPHICS_SPEC_EP01_V2.md` (2026-09-13).
- 파이프라인 A 선행 작업 (라우터 OVERRIDE · rights 인스턴스 · PRESENT lock — B-1 결정 뒤) · GT-0x Blender 템플릿.
- P5 Review UI / P6 Money Gate 어댑터 설계 (유료 없음).

**유료 생성 현황 (D-015)**: Money Gate OPEN (₩40,000 / 소진 94.12 credits, KRW 환산 P-012). **P2 Character Master 완료 (D-023)**: 원로 FULL 10/10 · 노동자 LITE 3/3 · 시종 LITE 3/3 전부 CHARACTER_MASTER_APPROVED. 라우터 잠금 (D-024). Master Frame 3장 APPROVED (D-027) · H06 완료 (D-031). 파이프라인 A 시험 1장 완료 (D-037, 68.12 credits). **다음 유료 = 미정 (사용자 지시 대기)**, 영상 H01–H05 는 P-012 뒤.

## P2 사전 점검 — Pre-flight (2026-09-11 · DONE, 생성 0)

리포트 `02_SEASONS/S01/EP01/15_QA/P2_PREFLIGHT_REPORT.md`. 순서(사용자 고정): Lock 확인 → Master Pack 요구 → 복식 TBD → Reference Set → FULL/LITE → Master Frame 후보 → **사람 승인** → 유료 생성.

| 단계 | 결과 |
|---|---|
| Character lock 3 · Costume lock 3 | 영문 전용, character 인스턴스와 일치. **6 APPROVED (D-015)** |
| Master Pack 요구 ↔ 프롬프트 | 17 = 17 (원로 10 + back_view 1 · 노동자 3 · 시종 3) |
| 복식 TBD | 0. 잔여 INTERPRETIVE = P-009 (옷 색·과대), lock 은 hedge 상태 |
| Reference Set | 3층 계보 (Master Pack → Master Frame → AI 샷). S05_SH005 프롬프트의 유령 참조 `EP01_S05_MASTER_V01` 제거. 검증기에 `reference_images` 실존 규칙 추가 (음성 테스트 통과) |
| FULL / LITE | 원로 FULL · 군중 2 LITE_CROWD 유지, 승격 대상 없음 (사람 확인 항목 C). H02 푸시인이 특정 얼굴에 머물면 재검토 |
| Master Frame 후보 | S04 · S06 DRAFT 2 (Master Pack 승인 뒤 생성) |
| 승인 | **D-015**: A✔ lock 6 APPROVED · B✔ muted blue + bronze · C✔ LITE 유지 · D✔ back_view 보조 · E 보류(AI 샷 직전) · F✔ ₩40,000 OPEN |

## P2 준비 — 프롬프트·카메라·마스터프레임 초안 (2026-09-11 · DONE, 생성 0)

| 항목 | 산출 | 상태 |
|---|---|---|
| Lock 라이브러리 (§8) | `06_PROMPT_LIBRARY/locks/` 11 조각 — GLOBAL · ERA `SILLA_EARLY_V01` · LOCATION `LOC_CHEONMACHONG_V01` · COSTUME 3 · CHARACTER 3 · STYLE · NEGATIVE | **11 APPROVED (D-015)** |
| Master Pack 프롬프트 | `11_AI_STILLS/prompt_PRM_MP_*` 17 — 원로 10 + 뒷모습 1 · 노동자 3 · 시종 3 (IMAGE) | DRAFT |
| AI 샷 프롬프트 | `12_AI_VIDEO/` 6 (H01–H05) · `11_AI_STILLS/` 2 (H06 · H07) — legacy APPROVED 팩을 shot_delta 로, lock 조립 `assembled_text` 저장 | DRAFT |
| 카메라 | `10_BLENDER/camera_CAMERA_EP01_*_V01.json` 8 (렌즈·높이·모션·배우 위치·키 비율) — 수동 초안 | DRAFT |
| Master Frame | `07_SHOTS/master_frame_EP01_S04_MASTER_V01` · `_S06_MASTER_OPEN_CHAMBER_V01` · `_S06_MASTER_MOUND_BUILDING_V01` — **3장 APPROVED (D-027)** | APPROVED |
| 검증 | camera / prompt / master_frame 인스턴스 + 상호참조 (shot ↔ camera ↔ prompt ↔ master_frame) → 231/231 PASS | DONE |

## P4 — Shot Router (2026-09-11 · DONE · **최종 잠금 D-024 2026-09-13**)

| 항목 | 산출 | 상태 |
|---|---|---|
| 라우터 판정 | `07_SHOTS/router_decision_RTR_EP01_*_V01.json` 49건 — 점수 6종 + recommended/fallback/reason/rule | ACCEPTED 46 · OVERRIDDEN 3 (D-024) |
| 재판정 결과 (역사, D-014 시점 — 최종은 아래 D-024) | legacy Higgsfield 8 → HIGGSFIELD 1 · BLENDER_FLOW 6 · AI_STILL 1 | 샷 `pipeline` 갱신, `status = ROUTED` |
| 최종 구성 (D-024) | REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · **HIGGSFIELD 0** | 46 ACCEPTED · 3 OVERRIDDEN (H01 · H03 · H07) · `15_QA/P011_ROUTER_FINAL.md` |
| 권리 등급 | `rights.usage_tier` ACTIVE / BACKUP_ONLY — YELLOW_ACTIVE 0 · YELLOW_BACKUP 4 (2026-09-13) | D-014 |
| 자동 FAIL 추가 | BACKUP_ONLY 참조 · AI 샷 라우터 없음 · 샷 파이프라인 ≠ 판정(OVERRIDDEN 아님) | 음성 테스트 통과 |
| 리포트 | `15_QA/P4_ROUTER_REPORT.md` | DONE |
| 검증 | 196/196 PASS, refs OK | DONE |

## P3 — Source/Rights Ledger (2026-09-11 · DONE, 브랜치 `p1-continuity`)

| 항목 | 산출 | 상태 |
|---|---|---|
| SOURCE | research-v2 S1–S6 전부 `05_HISTORY_DATABASE/sources/` (복식 7건 포함 총 13) | DONE |
| FACT | `facts/CLM_EP01_*_001–013` (FACT 9 · INTERPRETIVE 4, hedge 필수) + 천마총 배치 1 + 복식 8 = 22 | DONE |
| RIGHTS | `rights/` **15 (2026-09-13 GNM 분리 후)** — GREEN 9 (ACTIVE 8 · BACKUP 1) · YELLOW 4 (BACKUP) · RED 2 (2019 간행물 · UNESCO/NHK) | DONE, YELLOW 는 P-010 |
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
| CHARACTER | `characters/` 원로 1인 (FULL) + 군중 2그룹 (LITE_CROWD) | CHARACTER_MASTER_APPROVED (D-019 · D-023) |
| Master Pack 요구 목록 | `characters/EP01_MASTER_PACK_REQUIREMENTS.md` | DONE |
| 씬·샷 분해 | `02_SEASONS/S01/EP01/07_SHOTS/` 씬 9 · 샷 49 (러프컷 v1 기준 + D-009 분할 + X3 G13 추가, 합계 425초 = 7:05) | `BROKEN_DOWN` / `PLANNED` |
| 대본↔러프컷 차이 | `02_SEASONS/S01/EP01/05_SCRIPT/SCRIPT_ROUGHCUT_DELTA.md` X1–X4 **4/4 RESOLVED** (X3 → G13 금관 위치 단면 신규, S4 근거) | DONE |
| 검증 | `validate.py` 인스턴스 + ID 상호참조 + Master Pack 등급 + 복식 TBD 게이트 → 119/119 PASS, refs OK | DONE |

샷 구성 (49, P1 당시 HIGGSFIELD 8 → D-024 최종): REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · HIGGSFIELD 0 (AI 45초 ≈ 11%, 모든 AI 컷 ≤ 6초). 백로그: G13 은 graphics-spec v2 에 추가 필요 (legacy HTML 수정 금지).
`fact_ids` 는 P3 에서 49샷 전부 연결 완료. 출처는 샷 `notes` 에 research-v2 S1–S6 번호로도 표기.

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
| SOURCE_FACT_QA | `05_HISTORY_DATABASE/{sources,facts,rights}/` + `15_QA/P3_LEDGER_REPORT.md` | DONE (P3) · YELLOW_ACTIVE 해소 (2026-09-13) |
| SHOT_ROUTER | `07_SHOTS/router_decision_*` 49 + `15_QA/P4_ROUTER_REPORT.md` | DONE (P4) · **잠금 D-024** |
| REAL_SHOOT | `ep01-field-shoot-plan` 체크리스트 | 계획 APPROVED · **촬영 미실행** |
| ARCHIVE | `ep01-archive-photos` (1973 NRICH), `ep01-artifact-library` | 선별 APPROVED · 파일 다운로드 미실행 |
| AI 재현 | legacy `ep01-higgsfield-prompts` 7컷 → 라우터 D-024: BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · Higgsfield 0 | Character Master 승인 완료 (D-023) · 다음 Master Frame S04 · S06 → AI 샷 (별도 승인) |
| ROUGH_CUT | `ep01-premiere-roughcut` 0:00–7:05 | 설계 APPROVED |

**다음 실제 작업 (순서)**
1. 경주 현장 촬영 — **필수는 대릉원·천마총 (D-026 #4, 월성·사찰은 선택)**. 계획 `08_REAL_FOOTAGE/SHOOT_PLAN_EP01_V01.md`, 준비 점검 `15_QA/SHOOT_READINESS_20260913.md`. **D-032: 다음 주 짧은 촬영 (꼭 찍기 5컷), TODO `02_SEASONS/S01/EP01/08_REAL_FOOTAGE/SHOOT_TODO_EP01_20260913.md`.** 매치컷 착지 구도(`EP01_S08_SH003`)는 반드시 삼각대로 찍고 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame (D-026)` 에 기록.
2. 유물/아카이브 실제 파일 다운로드·정리 → `05_HISTORY_DATABASE/sources/` · `rights/` 인스턴스 (EP01 `02_SOURCES/` 폴더는 비어 있음).
3. AI 샷: H06 사진 완료 (D-031). 영상 H01–H05 는 P-012 (실제 청구액·월 크레딧) 확정 + Money Gate 승인 후 (D-028 Higgsfield · Kling 3.0). H07 은 현장 촬영 뒤.
4. 내레이션 녹음 → Premiere 러프컷 → 수정 → 공개.

**주의**: OS 예시의 `EP001_HWANGNYONGSA` 는 템플릿. 활성 EP01 을 덮어쓰지 않는다 (D-006).

---

## Money Gate

| 항목 | 값 |
|---|---|
| EP01 예산 | **₩40,000** (D-015) — `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` |
| 소진 | 94.12 credits (48 호출: 원로 13 · 군중 10 · 기준 그림 8 · AI 샷 3 · 파이프라인 A 14) — KRW 환산 P-012 |
| 게이트 상태 | `OPEN` — 최신 승인 `APR_EP01_PA_004` (D-042 위임, 1/1 사용) · 사진 위임 한도 사용 2/20 credits |

---

## 검수 요청 (needs_review)

- `00_SYSTEM/standards/*.md` 27개 v0.1 DRAFT (2026-09-14 STORY_ENGINE · PHOTO_AI · DIAGRAM_TEMPLATES 추가) — 사용자 승인 시 ACTIVE (P-004).
- P1 인스턴스 전체 DRAFT — 특히 `CHAR_SILLA_ELITE_OBSERVER_01` 인물 설정(피장자·왕 아님)과 복식 방향.

---

## 차단 / 미결

- ~~예산 미확인~~ → D-015 ₩40,000 OPEN. 파이프라인 A 시험: Higgsfield 커넥터 작동 확인 (2026-09-14), 선행 = B 8건 결정 (PRESENT lock 쌍).
- Blender 로컬 브리지(P7) 없음 → `camera.json` 은 수동 작성 단계.
- ~~복식 세부 근거 미확보~~ → 2026-09-11 해소 (D-011 게이트 통과). 잔여: 짚신 출처가 언론 보도 → P3 에서 박물관 페이지로 교체 권장.

---

## 최근 변경 (최신순)

- **2026-09-14 오후 사용자** — **D-042** 배치 2: 3장 OK, M2 재생성 (위임 2 credits) · **D-043** M2 V02 OK → S08_SH001 LOOK_APPROVED. **EP01 현재 시점 실사 10샷 전부 파이프라인 A 로 확정.** EP01 94.12 credits.

- **2026-09-14 오후 사용자 + Claude Code** — **D-041** 사용자 캡처 21장 RED 판정 (권리 기록, gitignore). 남은 2샷 텍스트 전용 생성 (구도 수치만): S01_SH001 + S08_SH001 M1–M3, 8 credits, 4/4 SUCCESS, 봇 PASS 3 · PARTIAL 1. 사용자 OK/FIX 대기. EP01 92.12 credits.

- **2026-09-14 오후 사용자** — **D-040** 배치 1 8장 전부 OK → S01_SH002 · S02_SH001(3컷) · S03_SH001 · S06_SH007 · S06_SH011 · S08_SH003 · S09_SH003 · S09_SH004 LOOK_APPROVED. 파이프라인 A 9/9 승인.

- **2026-09-14 오후 사용자 + Claude Code** — **D-038** 현장 촬영 제외, 전부 자체 제작. **D-039** 파이프라인 A 배치 1: GREEN CC0 원본 5장 추가 (권리·proof), 8장 생성 (Nano Banana 2, 16 credits, 8/8 SUCCESS), 봇 PASS 7 · PARTIAL 1. D-026 완화. 사용자 OK/FIX 대기. EP01 84.12 credits.

- **2026-09-14 오후 사용자** — **D-036** Nano Banana 2 = 파이프라인 A 기본 모델 · **D-037** S02_SH001 V01 최종 OK → LOOK_APPROVED. 파이프라인 A 첫 시험 성공 (2 credits).

- **2026-09-14 오후 Claude Code** — 파이프라인 A 첫 유료 시험 (사용자 '보내'): S02_SH001 V01 생성 SUCCESS, 2 credits, Sent Prompt Rule 검증 (전송문 = V01 assembled_text). 봇 판정 PASS(minor). 모델 이름 불일치 (Nano Banana 2 ≠ Pro) 기록. EP01 소진 68.12 credits. 검증 339/339. **사용자 OK/FIX + 모델 결정 대기.**

- **2026-09-14 오후 사용자 + Claude Code** — **D-035.** 검수 §4 B 8건 전부 승인 → 반영: PRESENT lock 쌍 (`DDABONG_GLOBAL_PRESENT_V01` · `DDABONG_NEGATIVE_PRESENT_V01`) · present-day 라벨 · I2V_MOTION 확장 (MODEL_ROUTER) · approval 스키마 (`prompt_ids` required · `delegated`) · 검증기 규칙 +4 (AI ≤ 6초 · PAID 승인 gate 필수 · 위임 한도 · `rights:` 참조) · CAMERA 기본값 · 표준 3개 ACTIVE (OS_INDEX). S02_SH001 시험 준비: 라우터 OVERRIDDEN · 샷 AI_STILL + photo_ai · prompt V01 · approval PA_001 · Gagnon 원본 5018×3345 다운로드 (rights 실측 완료). 검증 338/338. **전송은 사용자 확인 뒤.**

- **2026-09-13 사용자** — **D-032.** 경주 짧은 촬영 (다음 주): 꼭 찍기 5컷 (거리 · 오프닝 드러남 · 엔딩 같은 자리 · 천마총 매치컷 · 몽타주), 나머지 5컷은 시간 남으면. TODO `08_REAL_FOOTAGE/SHOOT_TODO_EP01_20260913.md`.

- **2026-09-13 Claude Code (D-029 에이전트)** — 촬영 대신 인터넷 사진 조사 `15_QA/REAL_SHOT_ALTERNATIVES_20260913.md`: REAL 10샷 중 사진 그대로 2 · 사진+줌/이동 (손실 있음) 6 · **촬영 필요 2** (S01_SH001 거리, S08_SH001 걷기·차·카페 몽타주 — 사용 가능한 영상 못 찾음). H07 은 사진 먼저 고르고 AI 그림을 맞추는 순서 가능, 단 천마총 정면 최적 사진은 CC BY-SA (YELLOW). 경주시 관광 사진은 '개인적, 공익적 용도' 한정 → 수익 채널 사용 불가 (RED 제안). 사용자 결정 대기 (§5).

- **2026-09-13 Claude Code (D-029 에이전트)** — 현장 촬영 준비 점검 `15_QA/SHOOT_READINESS_20260913.md`: 샷 목록 10개·87초 계획과 일치. 막는 것 4가지 — 촬영 허가 미확인 (Q1–Q5), 촬영 날짜·잔디 색 (H07 'green mound'), 직접 촬영 권리 증빙 절차 없음, 상태 문서 옛 촬영 목록 (이번에 정리). 사용자 결정 D1–D7.

- **2026-09-13 Claude Code** — 권리 이미지 크기 실측: 유리잔 3000px (원본 최대 11605px) · 말다래 3000×1933 (원본 5454×3516) · 가슴걸이 2000×3000 · 금제 관모 3000×2000 → 4건 모두 1080p 전체 화면 가능. 가슴걸이·금제 관모 출처도 e뮤지엄으로.

- **2026-09-13 사용자** — **D-031.** H06 사진 V03 최종 OK → `EP01_S06_SH010` LOOK_APPROVED (approved_version V03). 추가 생성 없음, EP01 소진 66.12 credits 그대로.

- **2026-09-13 Claude Code (D-029)** — 권리 해상도: 유리잔 (경주2386)·말다래 (경주2309) 출처를 e뮤지엄 페이지로 교체 — 같은 유물번호, 공공누리 1유형, 사진 3000px급 → 1080p 전체 화면 가능. 페이지 원문 증빙 저장. 가슴걸이·금제 관모 e뮤지엄 1유형 확인 (크기 미측정).

- **2026-09-13 Claude Code (D-029)** — 권리 증빙: 기존 GREEN 4건 (금관·금허리띠·천마도·NRICH 1973) 페이지 원문 저장·라벨 확인 → 사용 중 GREEN 8건 proof 완비. 유리잔 613×816·말다래 800×515 표시 이미지 → 1080p 전체 화면에 부족, 고해상도 원본 조사 중.

- **2026-09-13 Claude Code** — H06 3차 (D-030, 2 credits): 비율 3.9:1·둥근 꼭대기·지평선·단계 통과, 사람 규모 크게 개선 (원근 감안 약 1/5–1/6, 목표 1/8) → SUCCESS, **사용자 최종 OK 대기**. 공용 계정 출처 불명 차감 5건 (-10) 제외. EP01 소진 66.12 credits.

- **2026-09-13 사용자** — **D-030.** H06 1회 추가 승인 · P-012 미정 유지 (영상 계속 미승인) · 사진 전용 위임 한도: 샷당 2 호출/4 credits, 누적 20 credits, 그림 최종 OK 는 사용자.

- **2026-09-13 Claude Code (D-029)** — 에이전트 배치 + Codex 역할 반박 검수 BLOCK 수정: YELLOW_ACTIVE 해소 (유리잔·금제 관모·가슴걸이·천마무늬 말다래 GREEN 1유형, 페이지 원문 proof 저장) · S02_SH003 말다래 정정 (금동 말다래) · 데이터 정리 (H05 라벨 2개 · S03_SH002 · 자갈/토기 사실 연결) · 영상 V02 6개 한 가지 동작 · 시작 사진 3개 (문장만, H03 금 제거). 커밋 8a3d798 은 스크립트 중단으로 일부만 반영된 상태였고 이어서 완결.

- **2026-09-13 Claude Code (D-029 에이전트)** — 권리 조사: 국립경주박물관 페이지 원문 확인 → 가슴걸이·금제 관모·유리잔 공공누리 1유형 → GREEN 3건 생성, S02_SH003·S05_SH001 연결 교체, OTHER_OBJECTS BACKUP_ONLY. **YELLOW_ACTIVE 해소.** 데이터 정리: H05 라벨 2개 · S03_SH002 권리 메모 · G04 자갈 사실 연결.

- **2026-09-13 사용자** — **D-029.** Codex 중계 종료 → 봇 자체 멀티 에이전트 (작업 에이전트 · Codex 역할 반박 검수 · 검증기 · push). 유료·그림·역사·main 관문 유지. H06 3번째 시도는 사용자 결정 대기.

- **2026-09-13 Claude Code** — H06 2차 (2 credits, 승인 2/2 소진): 비율·지평선·단계 통과, **사람 대비 규모 실패 (1/4, 목표 1/8)** · 평평한 꼭대기 · 무술복 같은 옷 → PARTIAL, **STOP**. 수정안 V04 + PATCH + 새 승인(PENDING, 1회/2 credits) 저장만. EP01 소진 64.12 credits.

- **2026-09-13 Claude Code** — H06 1차 (2 credits, 승인 1/2): 단계 OK · 규모 대체로 OK · **봉분 비율 약 2.3:1 (목표 3.7:1) · 지평선 전봇대·건물** → REJECTED. 실패 항목만 고친 V03 + PATCH 저장 후 마지막 2차 시도. EP01 소진 62.12 credits.

- **2026-09-13 사용자** — **D-028.** Higgsfield = provider, Kling 3.0 = model (영상), D-024 '0건' = EXTREME_CAMERA 파이프라인 0건으로 명확화. 샷에 logical_pipeline/provider/model 분리. D3 Blender 없이 먼저, 공간 오류 2회 STOP. D4 H06 사진 최대 2회/4 credits. P-012 는 실제 청구액 받으면 확정, **영상 미승인**.

- **2026-09-13 사용자** — **D-027.** 기준 그림 3장 최종 확정 (S04 V05 · S06 OPEN_CHAMBER V02 · S06 MOUND_BUILDING V01). 군중 참고 그림 규칙 추가. 기준 그림 16 credits (2 호출 버퍼 미사용), EP01 누적 60.12 credits. 다음: AI 샷 8개 생성 방법·비용 관리안.

- **2026-09-13 Claude Code** — 사용자 지적 (S04 노동자 얼굴 복제) → 참고 그림 없이 새로 생성 V05, S04 V05 PASS (2 credits, 승인 8/10). 사용자 최종 OK 대기 → OK 면 기준 그림 3장 확정. EP01 소진 60.12 credits.

- **2026-09-13 Claude Code** — S04 편집 V04 PASS (2 credits, 승인 7/10): 현대 지평선·줄자·쇠 삽날 제거. 사용자 최종 OK 대기 → OK 면 기준 그림 3장 확정. EP01 소진 58.12 credits.

- **2026-09-13 Claude Code** — 기준 그림 S06 OPEN_CHAMBER V02 APPROVED (S06 2장 확정). S04 새로 생성 V03 (2 credits, 승인 6/10): 검은 띠 해결, 새 문제 = 지평선 전봇대·현대 건물, 노란 줄자, 쇠 날 삽 일부 → 편집 V04 저장, 사용자 OK 대기. EP01 소진 56.12 credits.

- **2026-09-13 Claude Code** — 기준 그림 FIX 결과 (4 credits, 승인 5/10): S06 MOUND_BUILDING APPROVED · S06 OPEN_CHAMBER V02 PASS (관·허리띠) 최종 OK 대기 · S04 V02 PARTIAL (검은 띠·쇠 공구 일부 남음) → 새로 생성 V03 저장, 사용자 OK 대기. EP01 소진 54.12 credits.

- **2026-09-13 Claude Code** — 기준 그림 V01 3장 생성 (6 credits, 승인 3/10). S04: 쇠 공구·검은 띠 → FIX 제안 · S06 OPEN_CHAMBER: 서양식 관·쇠 경첩·민 허리띠 → FIX 제안 · S06 MOUND_BUILDING: 통과 제안. FIX 문장(V02)·PATCH 저장, **사용자 OK/FIX 대기**. `08_GENERATION_CACHE/EP01/MF/REVIEW_MF_V01.md`. EP01 소진 50.12 credits.

- **2026-09-13 사용자** — **D-026.** 1~7 추천안 전부 승인: Master Frame 3장 (S04 · S06 OPEN_CHAMBER · S06 MOUND_BUILDING) Money Gate 최대 10 호출/20 credits · H07 천마총 착지 · 자체 촬영 GREEN · 월성·사찰 선택 · G13 옆 단면+평면 inset · G13 hedge · G04 층 순서.

- **2026-09-13 Claude Code (D-025 자율 + 검수 에이전트)** — 무료 작업 2건: 촬영 계획 `08_REAL_FOOTAGE/SHOOT_PLAN_EP01_V01.md` (10컷 87초, 매치컷·시선·오프닝 반복, 초록 잔디 조건) · 그래픽 명세 v2 `14_EDIT/GRAPHICS_SPEC_EP01_V2.md` (G01–G12 이관 + G13, 사실 기록 범위만). 둘 다 검수 에이전트 PASS WITH FIXES → 수정 반영. Master Frame 계획 `15_QA/MASTER_FRAME_PLAN_EP01.md` (S06 층 순서 충돌 A/B). **사람 결정 대기 목록은 채팅으로 일괄 보고.**

- **2026-09-13 사용자** — **D-025.** 운영 방식: 무료 작업 자율 + 검수 에이전트 점검, **검증 통과 시 작업 브랜치 push 자동** (D-007 대체). 사람 관문 = 유료 승인 · 그림 OK/FIX · 역사 해석 · main 병합. Codex 교차 검수는 큰 단계 완료 시에만.

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
