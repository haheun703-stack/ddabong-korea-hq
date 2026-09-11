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

### P-011 · (보류 D-015: AI 샷 직전 승인) 라우터 판정 49건 ACCEPT / OVERRIDE (P4, 2026-09-11)
**현황** 전 샷 `human_decision = PENDING`. 실질 판단 대상은 재현 8컷 — 특히 **H05** (`EP01_S06_SH005`, 에피소드 핵심 컷): 판정 BLENDER_FLOW (공간 85 + 인물 연속성), fallback HIGGSFIELD. 나머지 41건은 규칙 그대로 (REAL/ARCHIVE/GRAPHIC).
**제안** 일괄 ACCEPT. OVERRIDE 시 `router_decision.human_decision = OVERRIDDEN` + `override_note`, 샷 `pipeline` 변경.
**근거** `02_SEASONS/S01/EP01/15_QA/P4_ROUTER_REPORT.md`

### P-008 · Shot 스키마에 인물 가시성 필드 추가 (P2 백로그, 사용자 제안 2026-09-11)
**제안** `shot.schema.json` 에 `foreground_role` 또는 `character_visibility` (예: BACKGROUND / MIDGROUND / FOREGROUND_IDENTIFIABLE) 를 추가해, 군중 인물이 전경·식별 가능하게 쓰이면 `validate.py` 가 FULL Pack 승격을 자동 요구하게 한다 (D-008 규칙 자동화). 지금은 사람 검수.
**시점** P2 또는 P3. P1 에는 넣지 않는다.
**영향** 스키마 변경 + 48개 샷 인스턴스 필드 추가 + 검증기 규칙.
