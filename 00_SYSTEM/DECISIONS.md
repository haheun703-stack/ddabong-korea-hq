# DECISIONS — 결정 기록

> 확정된 결정은 `D-번호`, 승인 대기 제안은 `P-번호`. 승인되면 P → D 로 옮기고 날짜를 적는다.
> 큰 결정(정본 개정, 스타일 LOCK, 파이프라인 변경, 스키마 변경, 예산)은 반드시 여기에 남긴다. 결정은 삭제하지 않는다.
> 브랜드 결정 원본: `brand_decisions.json` (2026-08-14)

---

## 확정 (D)

### D-001 · 2026-08-14 · 영문 브랜드명 / 한글 표기 / 마스터 로고 (사용자)
**승인 내용** DDABONG KOREA · 따봉 코리아 · 태극 빨강/파랑 붓터치 엄지 + 대한민국 도장. Web HQ 밝은 테마.
**근거** `brand_decisions.json`

### D-002 · 2026-08-14 · 슬로건 (사용자)
**승인 내용** STORIES BEHIND KOREA. 브랜드 방향: 전통+현대 / 긍정+스토리텔링 / Why Korea? 관점.

### D-003 · 2026-08-14 · 핵심 채널 콘셉트 · 역사 해석 원칙 · 파일럿 3편 (사용자)
**승인 내용** "Not just what happened. Why it made sense to them." / FACT → CONTEXT → INTERPRETATION 분리 / Higgsfield 는 당시 사람의 생각·시선·갈등·선택 시각화 도구, `AI Visual Reconstruction` 표기 / 파일럿 순서 경주 왕릉 → 신라 금관 → 온돌.
**반영** `concept-bible.md`, 정본 §0 §9.

### D-004 · 2026-09-11 · 역사 인물 시각 스타일 = B Documentary Reenactment (사용자)
**승인 내용** 본편 역사 인물은 B. Hero/Thumbnail 만 A Cinematic Photoreal 수준 보조. C Semi-Realistic 3D 는 previz/참고. D Stylized 는 기본 아님.
**근거** CASE-DDABONG-CHAR-001 (정본 §20) → `schemas/examples/case_memory_TEMPLATE.json`
**주의** 마스코트·썸네일에 대한 전역 규칙이 아니다.

### D-005 · 2026-09-11 · DDABONG STUDIO OS v0.1 정본 채택 (사용자)
**승인 내용** `00_SYSTEM/BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` 를 봇 운영 계약으로. 멀티에이전트 6엔진, Continuity Engine, Learning Engine(4 memory + 회귀검사), KEEP/CHANGE, Money Gate 80/95/100, Source/Rights Ledger.
**반영** `BOT_BOOTSTRAP_PROMPT.md`, `bot-handoff.html`

### D-006 · 2026-09-11 · 활성 EP01 = 경주 왕릉/천마총, 황룡사 EP001 은 템플릿 예시 (사용자)
**승인 내용** OS 예시의 `EP001_HWANGNYONGSA` 는 템플릿. 활성 EP01 을 덮어쓰지 않는다.
**반영** `episode.json.template_note`, `schemas/examples/*_TEMPLATE.json` 은 EP001 ID 만 사용.

### D-007 · 2026-09-11 · P0 범위 · EP01 파일 처리 · Git 운영 (사용자)
**승인 내용**
- 리포 클론 위치: `H:\...\3. 따봉 코리아_유튜브 모음_260814\ddabong-korea-hq\`
- P0 범위 = 폴더 골격 전체 + 운영 문서 4종 + 스키마 전부 완성 + §22 나머지 표준 문서는 정본 내용을 옮긴 v0.1 DRAFT
- 기존 `episodes/ep01-*` 는 제자리 유지, `02_SEASONS/S01/EP01/episode.json` 매니페스트로 참조만
- 로컬 커밋까지 자율, **push 직전 변경 요약 후 사용자 확인**
**반영** `AGENT_RULES.md` §6, `.gitignore`, `episode.json.legacy_artifacts`

### D-008 · 2026-09-11 · Master Pack 등급: BACKGROUND CROWD = Lite / RECURRING OR FOREGROUND = Full (사용자, P-005 승인)
**승인 내용** 반복 신원 유지가 필요 없는 군중(노동자·시종·장인)은 전신 / 걷기 / 복식 3종 Lite Crowd Pack. 카메라에 반복 등장하거나 얼굴이 식별되는 인물은 반드시 10종 Full Pack 으로 승격.
**반영** `character.schema.json` `master_pack_tier` (FULL / LITE_CROWD) + 슬롯 상태 `NOT_REQUIRED`, `validate.py` 등급 검사, 군중 2그룹 LITE_CROWD · 원로 FULL.

### D-009 · 2026-09-11 · AI 재현 컷은 5–6초 핵심 순간으로 분할 (사용자, P-006 승인)
**승인 내용** H04 16초·H05 15초를 AI 영상 한 번으로 밀지 않는다. AI 는 핵심 재현 순간만 5–6초, 나머지는 실사·발굴자료·유물·그래픽·편집 모션으로 채운다. Generate Late 와 "AI 는 실제 증거를 대신하지 않는다" 원칙에 따름.
**반영** EP01 S04·S06 샷 재분할. AI 합계 70초 → 45초. 모든 Higgsfield 샷 ≤ 6초.

### D-010 · 2026-09-11 · 러프컷 v1 = 샷 구조 임시 작업 기준, 차이는 SCRIPT_ROUGHCUT_DELTA 로 (사용자, P-007 승인)
**승인 내용** 샷/씬 분해는 러프컷 타임라인을 따르되 최종 정본은 아니다. 차이 4곳은 P3 Fact/Source 연결 전에 정리. 내용·사실·해석이 다르면 Script/Fact 우선, 단순 타이밍·컷 배치 차이면 Rough Cut 우선.
**반영** `02_SEASONS/S01/EP01/05_SCRIPT/SCRIPT_ROUGHCUT_DELTA.md`

### D-011 · 2026-09-11 · 복식 TBD → 근거 기반 확정 게이트 (사용자)
**승인 내용** 근거 없는 옷깃·여밈·모자·신발을 상상으로 채우지 않는다. Character Master Pack 생성 전에 복식 TBD 가 근거 자료로 확정돼야 한다.
**반영** `validate.py` — 복식에 TBD 가 남아 있는데 Master Pack 슬롯이 DRAFT/APPROVED 가 되면 FAIL.

### D-012 · 2026-09-11 · P1 APPROVED WITH CONDITIONS · Git (사용자)
**승인 내용** P1 승인 (조건: D-008~D-011). `6a60b1b` 를 `p1-continuity` 에 push. main 병합은 다음 검수 게이트 전까지 보류. Web HQ 표시는 merge 시점에 동기 (main 만 배포).

### D-013 · 2026-09-11 · P3 진입 승인 + Shot `evidence_role` (사용자)
**승인 내용** `b918b24` push. P3 Source/Rights Ledger 진입: S1–S6 → SOURCE, 주장 → FACT(등급), 49 샷 `fact_ids` + 외부 자산 `rights_id`, 출처 미연결 샷 / 권리 미확인 자산 / 과도한 해석 자동 FAIL, 검증 리포트. 각 샷에 `evidence_role = PRIMARY / SUPPORTING / CONTEXT / NONE` 추가 (G13 = PRIMARY, 현대 실사 = CONTEXT).
**반영** `shot.schema.json` `evidence_role`, `validate.py` `ledger_rules()`, `05_HISTORY_DATABASE/{sources,facts,rights}/`, `02_SEASONS/S01/EP01/15_QA/P3_LEDGER_REPORT.md`.

### D-014 · 2026-09-11 · P-010 권리 등급 · P4 진입 · 라우터 감독 기준 (사용자)
**승인 내용** `e5c4d39` push. 권리 등급: GREEN 사용 가능 / **YELLOW_ACTIVE** 실제 샷 연결 → 편집 전 해결 필수 / **YELLOW_BACKUP** 대체 가능 → 실제 사용 시에만 해결 / RED 금지. B5 박물관 기타 유물 1건은 YELLOW_ACTIVE 필수 해소 항목, 나머지 3건 BACKUP_ONLY. P4 진입: H01–H06 은 legacy Higgsfield 태그를 그대로 두지 않고 정본 라우터로 재판정. 감독 기준: 공간 정확도↑+카메라 복잡도↑ → BLENDER→FLOW/VEO · 사람 동작 중심 → FLOW/VEO · 강한 reveal/극단 카메라/특수 전환 → HIGGSFIELD · 정보량↑ 움직임↓ → AI STILL · 현재 장소 → REAL_SHOOT · 공식 자료 → ARCHIVE. 각 판정에 spatial_accuracy / camera_complexity / human_motion / continuity_importance / historical_importance / visual_importance / recommended / fallback / reason 기록.
**반영** `rights.schema.json` `usage_tier`, `router_decision.schema.json` `scores` `fallback_pipeline` `previous_pipeline`, `validate.py` (BACKUP_ONLY 참조 FAIL · AI 샷 라우터 필수 · 샷 파이프라인 ≠ 라우터 판정 FAIL), `07_SHOTS/router_decision_RTR_*` 49건, `15_QA/P4_ROUTER_REPORT.md`.
**결과** legacy Higgsfield 8 → HIGGSFIELD 1 (H07 매치컷) · BLENDER_FLOW 6 · AI_STILL 1 (H06). 라우터 `human_decision = PENDING` → 사용자 ACCEPT/OVERRIDE 대기 (P-011).

---

### D-015 · 2026-09-11 · P2 사전 점검 승인 A–F · Money Gate OPEN · Master Pack 소규모 배치 (사용자)
**승인 내용** `15_QA/P2_PREFLIGHT_REPORT.md` 항목 A–F. **A** Character lock 3 + Costume lock 3 → APPROVED. **B** (P-009 종결) 원로 옷 색 muted blue · 금속 포인트 restrained bronze, `historical_basis` 는 PROBABLE 유지. **C** 노동자·시종 2그룹 LITE_CROWD 유지, H02 푸시인이 특정 얼굴에 머물 때만 FULL 승격 검토. **D** (P-005 종결) back_view 는 정식 슬롯 추가 없이 FULL Pack 보조 레퍼런스 이미지로 취급, 스키마 미확장. **E** (P-011 보류) 라우터 49건 ACCEPT/OVERRIDE 는 AI 샷 생성 직전 최종 승인. **F** (P-001 종결) EP01 AI 생성 예산 **₩40,000**, Money Gate OPEN.
**생성 원칙** 17장 일괄 생성 금지. 배치 1 = 원로 hero · front · three_quarter_left · full_body 4장 → 사람 검수(얼굴·체형·복식 lock 확인) → 나머지 6 + back_view → 군중 6. Generate Late + Change Only What Failed.
**반영** locks 6 APPROVED · `COSTUME_SILLA_ELITE_A01` color/belt/forbidden · 프롬프트 13 재조립 (원로 MP 11 + S06_SH002 · SH005; 생성 전이라 V01 유지) · `episode.json.budget` · `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` OPEN · `approval_APR_EP01_MP_ELITE_BATCH1_001.json` APPROVE · validate.py 가 cost/approval/generation 인스턴스 검증.

### D-016 · 2026-09-13 · 전체 검수 수정 승인 · 전송 프롬프트 정본 규칙 · 우선순위 (사용자)
**승인 내용** `6c66f13` (검수 수정 1–5, `15_QA/REVIEW_FIX_20260913.md`) → `origin/p1-continuity` push. main 은 계속 보류 (D-012). 유료 생성은 배치 1 Work 판정 전까지 정지 유지.
**정본 규칙 (Sent Prompt Rule)** ① 보낼 문장을 먼저 prompt 새 버전으로 저장 → ② 저장된 `assembled_text` 를 **그대로** 전송 → ③ generation 기록에 실제 전송본 연결 (`prompt_id` + `provider_job.params_path`). 이 순서가 깨지면 FAIL — `validate.py money_rules` 가 강제한다.
**우선순위** 1 배치 1 Work 판정 → 2 hero 배경 기와지붕 시대 위반 여부 → 3 H07 정지/영상 매치컷 결정 → 4 Master Pack 확장 → 5 Web HQ 는 main 병합 시점 동기화.

### D-017 · 2026-09-13 · 원로 Master Pack 배치 1 사람 판정 (사용자)
**판정** 얼굴 동일성 OK. front · three_quarter_left · full_body **APPROVED**. hero 는 얼굴·복식 OK, 배경의 조선식 기와지붕 건물이 시대 lock(SILLA_EARLY_V01) 위반 → **그 항목만 FIX**. 소매(반소매 겉옷 + 긴 속옷 소매)는 유지.
**방법** 전체 재생성 대신 기존 hero 이미지(job c7a5cc92)를 입력으로 배경만 편집 1회 (`PRM_…_HERO_V04`, `PATCH_MP_ELITE_HERO_002`). 배치 1 승인 범위 8회 중 6번째. Sent Prompt Rule (D-016) 적용.
**다음** 편집본 사람 확인 → hero APPROVED 되면 4장 완료 → 나머지 6 + back_view 는 새 approval.
**결과** hero V03 (job 5de27748, 2 credits) 사용자 APPROVE (2026-09-13) → 배치 1 4장 APPROVED.

### D-018 · 2026-09-13 · Master Pack 배치 2 승인 · H07 정지 이미지 · 크레딧 공용 (사용자)
**승인** `APR_EP01_MP_ELITE_BATCH2_001` APPROVE — 원로 나머지 7장 (three_quarter_right · profile · neutral_standing · walking · costume_detail · expression_sheet · back_view), 최대 10 호출 (14–20 credits). 참조 = hero V03 + full_body V01. 전송은 저장된 V02 문장 그대로 (D-016).
**H07** `EP01_S08_SH002` HIGGSFIELD → **AI_STILL** (라우터 OVERRIDDEN, P-011 중 1건 확정). 현장 SH003 착지 구도 촬영 뒤 생성.
**크레딧** Higgsfield 계정은 다른 작업과 공용 → 잔액 차이는 EP01 소진이 아니다. EP01 소진은 generation 기록(job 단위) 합계만으로 계산.

### D-019 · 2026-09-13 · 원로 Master Pack 배치 2 사람 판정 · Character Master 승인 (사용자)
**판정** 배치 2 7장 (three_quarter_right · profile · neutral_standing · walking · costume_detail · expression_sheet · back_view) 전부 APPROVE. profile 방향(오른쪽)·back_view 비계·모자 높이 메모는 허용.
**결과** `CHAR_SILLA_ELITE_OBSERVER_01` Master Pack 10/10 APPROVED → **CHARACTER_MASTER_APPROVED**. 원로 유료 생성 누적 22 credits (배치 1 8.12 포함 EP01 전체 24.12).
**다음** 군중 LITE Pack (노동자 3 · 시종 3) — 별도 approval.

### D-020 · 2026-09-13 · 군중 LITE Master Pack 승인 (사용자)
**승인** `APR_EP01_MP_CROWD_001` APPROVE — 노동자 3 · 시종 3 (full_body · walking · costume_detail, 한 장에 3명, 3:2), 최대 9 호출 (12–18 credits). 1단계 full_body 2장 → 사람 확인 → 2단계 나머지 4장 (해당 무리 full_body 를 복식 참조). 전송은 저장된 V02 문장 그대로 (D-016).

### D-021 · 2026-09-13 · 군중 시종 full_body 재편집 · 승인 한도 확대 (사용자)
**결정** 시종 full_body 편집 PARTIAL(여자만 옷고름 제거) → 남자 2명만 위치 지정 재편집 1회 (`PRM_…ATTENDANT…_FULL_BODY_V04`, `PATCH_MP_ATTENDANT_FULL_BODY_002`). `APR_EP01_MP_CROWD_001` 한도 9 → **12 호출** (최대 24 credits). 재편집이 또 실패하면 편집 반복하지 않고 방법 전환을 사용자에게 제안.

### D-022 · 2026-09-13 · 군중 full_body 승인 (사용자)
**판정** 노동자 `MP_LABORER_FULL_BODY_V02_412a72bc.png` (공구 제거 편집) · 시종 `MP_ATTENDANT_FULL_BODY_V04_84c0fdbc.png` (방법 A 새로 생성, 옷고름 없음) **APPROVED**. 시종 V03 (가운데 남자 옷고름 남음) 탈락.
**다음** 2단계 4장 — 노동자 walking/costume_detail V02 (참조 job 412a72bc) · 시종 walking/costume_detail V03 (참조 job 84c0fdbc). 승인 한도 12 중 6 사용.

### D-023 · 2026-09-13 · 군중 LITE Pack 승인 · P2 Character Master 완료 (사용자)
**판정** 노동자·시종 walking · costume_detail 4장 APPROVE → 두 무리 LITE Pack 3/3 → **CHARACTER_MASTER_APPROVED**. 원로(D-019) 포함 **캐릭터 3/3 승인 = P2 완료**.
**메모** walking/costume_detail 에 참조 full_body 얼굴이 반복됨 → 영상에서 같은 3인조를 알아볼 정도로 반복하지 않는다. 시종 옷감 새것 느낌은 허용.
**비용** EP01 누적 44.12 credits (23 호출: 원로 13 · 군중 10). 군중 승인 12 중 10 사용, 남은 2 호출은 사용하지 않고 종료.

### D-024 · 2026-09-13 · P-011 라우터 49건 최종 잠금 · FLOW_VEO 분류 추가 · EP01 Higgsfield 0건 (사용자)
**확정** 46건 ACCEPTED · `EP01_S04_SH004` H01 · `EP01_S05_SH005` H03 → **FLOW_VEO** (OVERRIDDEN) · `EP01_S08_SH002` H07 AI_STILL 유지 (D-018). 최종 구성 REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 (H02 · H02b · H04 · H05) · FLOW_VEO 2 · AI_STILL 2 (H06 · H07) · **HIGGSFIELD 0**. AI 8컷 45초 (≈11%, 모두 ≤6초).
**EP01 재현 원칙** 공간 위계·규모 → BLENDER_FLOW · 행동 중심·공간 중간 → FLOW_VEO · 저동작 정보 컷 → AI_STILL · 증거 → ARCHIVE · 현재 장소 → REAL_SHOOT · 설명 도식 → ORIGINAL_GRAPHIC. EP01 은 다큐 톤 우선 → **Higgsfield 사용 0건으로 잠금**.
**스키마** shot.pipeline · router_decision.recommended/fallback 에 `FLOW_VEO` 정식 추가 (BLENDER_FLOW 와 독립). 검증기: FLOW_VEO 를 AI 파이프라인으로 취급, 라우터 PENDING 인 샷의 generation 은 FAIL.
**유지 주의** YELLOW_ACTIVE 권리 1건 (`RTS_GNM_OTHER_OBJECTS_001` → S02_SH003 · S05_SH001) 편집 확정 전 해소 필수 (판정과 별개). Flow/Veo 자동 연결 도구 없음 → 라우터만 확정, 실제 생성은 별도 승인 + 별도 Money Gate. Blender 자동화(P7) 전 → 카메라 초안 기준 수작업 허용.
**근거** `02_SEASONS/S01/EP01/15_QA/P011_ROUTER_FINAL.md`

---

## 승인 대기 (P)

### P-012 · Higgsfield 크레딧 → KRW 환산율 (Money Gate 계산용)
**현황** 예산은 KRW ₩40,000 (D-015), 소진은 Higgsfield 크레딧 (배치 1 = 8.12 credits, plus 플랜). 환산율이 없어 `cost.percent_used` 를 계산할 수 없다.
**제안** 플랜 월 요금 ÷ 월 크레딧으로 1 credit 당 KRW 를 정해 `COST_STANDARD.md` 에 기록.
**영향** `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` spent_total / percent_used.


### ~~P-001~~ · (종결 D-015) EP01 생성 예산 (Money Gate 기준값)
**제안** 통화·금액 확정 필요. 미확인 동안 `cost.gate_state = UNKNOWN_BUDGET` 으로 유료 생성 잠금.
**영향** `02_SEASONS/S01/EP01/episode.json.budget`, `COST_STANDARD.md`

### P-002 · 에피소드 ID 자릿수
**제안** 활성 EP01 은 `EP01` 유지 (기존 파일명 `ep01-*` 와 일치). 정본 예시는 `EP001`. 시즌 2 이후 3자리로 통일할지 결정.
**영향** `schemas/shot.schema.json` 등 ID 패턴은 두 자리·세 자리 모두 허용 중.

### P-003 · 표준 문서 언어
**제안** 한글 본문 + 영문 키/ID (형제 프로젝트 관례). 정본은 영문 유지.

### P-004 · 표준 문서 22개 v0.1 DRAFT → ACTIVE 승인
**제안** `00_SYSTEM/standards/*.md` 는 정본 내용 이관본. 검토 후 일괄 또는 개별 ACTIVE 승격. 승인 전에는 정본 §N 우선.

*(P-005 → D-008, P-006 → D-009, P-007 → D-010 으로 승인됨, 2026-09-11)*

### ~~P-009~~ · (종결 D-015) 원로 인물 옷 색·허리띠 재질 (복식 QA, 2026-09-11)
**현황** `COSTUME_SILLA_ELITE_A01` 의 다른 항목은 PROBABLE 로 확정됐으나, 옷 색과 과대(허리띠) 재질은 인물의 관등을 정하지 않으면 근거로 못 정한다. 삼국사기 색복지(법흥왕대) 기준 자=최고위, 비=아찬~급찬, 청=대나마·나마.
**제안** 원로는 "왕 아님·피장자 아님"이므로 **비(다홍) 계열 + 은·동 과대** 권장. 자색·금제 과대는 피장자/왕급이라 제외. 5세기 전반에 이 색 규정이 있었는지는 불확실하므로 INTERPRETIVE 로 유지.
**영향** Master Pack 생성 프롬프트의 COSTUME LOCK.

### ~~P-011~~ · **종결 D-024 (2026-09-13)** · 라우터 판정 49건 ACCEPT / OVERRIDE (P4, 2026-09-11)
**현황** 전 샷 `human_decision = PENDING`. 실질 판단 대상은 재현 8컷 — 특히 **H05** (`EP01_S06_SH005`, 에피소드 핵심 컷): 판정 BLENDER_FLOW (공간 85 + 인물 연속성), fallback HIGGSFIELD. 나머지 41건은 규칙 그대로 (REAL/ARCHIVE/GRAPHIC).
**제안** 일괄 ACCEPT. OVERRIDE 시 `router_decision.human_decision = OVERRIDDEN` + `override_note`, 샷 `pipeline` 변경.
**근거** `02_SEASONS/S01/EP01/15_QA/P4_ROUTER_REPORT.md`

### P-008 · Shot 스키마에 인물 가시성 필드 추가 (P2 백로그, 사용자 제안 2026-09-11)
**제안** `shot.schema.json` 에 `foreground_role` 또는 `character_visibility` (예: BACKGROUND / MIDGROUND / FOREGROUND_IDENTIFIABLE) 를 추가해, 군중 인물이 전경·식별 가능하게 쓰이면 `validate.py` 가 FULL Pack 승격을 자동 요구하게 한다 (D-008 규칙 자동화). 지금은 사람 검수.
**시점** P2 또는 P3. P1 에는 넣지 않는다.
**영향** 스키마 변경 + 48개 샷 인스턴스 필드 추가 + 검증기 규칙.
