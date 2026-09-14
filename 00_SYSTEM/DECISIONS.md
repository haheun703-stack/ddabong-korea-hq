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
**EP01 재현 원칙** 공간 위계·규모 → BLENDER_FLOW · 행동 중심·공간 중간 → FLOW_VEO · 저동작 정보 컷 → AI_STILL · 증거 → ARCHIVE · 현재 장소 → REAL_SHOOT · 설명 도식 → ORIGINAL_GRAPHIC. EP01 은 다큐 톤 우선 → **Higgsfield 사용 0건으로 잠금**. *(D-028 명확화: HIGGSFIELD CAMERA / EXTREME CAMERA 파이프라인 = 0 shots. 공급 플랫폼으로서 Higgsfield 는 허용.)*
**스키마** shot.pipeline · router_decision.recommended/fallback 에 `FLOW_VEO` 정식 추가 (BLENDER_FLOW 와 독립). 검증기: FLOW_VEO 를 AI 파이프라인으로 취급, 라우터 PENDING 인 샷의 generation 은 FAIL.
**유지 주의** YELLOW_ACTIVE 권리 1건 (`RTS_GNM_OTHER_OBJECTS_001` → S02_SH003 · S05_SH001) 편집 확정 전 해소 필수 (판정과 별개). Flow/Veo 자동 연결 도구 없음 → 라우터만 확정, 실제 생성은 별도 승인 + 별도 Money Gate. Blender 자동화(P7) 전 → 카메라 초안 기준 수작업 허용.
**근거** `02_SEASONS/S01/EP01/15_QA/P011_ROUTER_FINAL.md`

### D-025 · 2026-09-13 · 운영 방식: 자율 실행 + 검수 에이전트 · 검증 통과 시 push 자동 (사용자)
**배경** 사용자가 Codex ↔ Claude Code 사이에서 결과를 복붙으로 중계하던 방식은 LLM 2개를 사람이 연결하는 셈이라 비효율.
**결정** ① 무료 작업은 봇이 계획 → 실행 → 검수 에이전트(별도 컨텍스트)로 OS 규칙 점검 → `validate.py` → 커밋 → push 까지 자율. ② **검증 전체 PASS + 상호참조 OK 이면 작업 브랜치 push 자동** (D-007 의 "push 전 확인" 대체). 검증 실패 시 push 금지. ③ 사람 관문 유지: 유료 생성 승인(Money Gate) · 그림 최종 OK/FIX · 역사 해석 결정 · `main` 병합/push · force push·히스토리 재작성. ④ Codex 교차 검수는 큰 단계 완료 시에만 (같은 계열 모델 착각 보완).
**영향** AGENT_RULES §Git · 단축 명령, BOT_BOOTSTRAP_PROMPT. Web HQ(GitHub Pages)는 main 배포라 작업 브랜치 자동 push 로 공개 페이지는 바뀌지 않음.

### D-026 · 2026-09-13 · Master Frame 3장 승인 · H07 천마총 착지 · 자체 촬영 GREEN · 월성·사찰 선택 · G13·G04 확정 (사용자)
**1** S06 기준 그림을 역사 단계로 분리 (A안): `EP01_S04_MASTER_V01` · `EP01_S06_MASTER_OPEN_CHAMBER_V01` (H04, 목곽 열린 단계) · `EP01_S06_MASTER_MOUND_BUILDING_V01` (H05·H06, 봉분 상승 단계). **Money Gate** `APR_EP01_MF_001` 최대 10 호출 / 20 credits. 실패 시 실패 항목만 FIX, 승인 범위 밖 호출 금지. 스키마: frame_id 단계 태그 허용, scene.master_frame 복수 허용.
**2** H07 매치컷 착지 = **천마총 봉분**. S08_SH002 · S08_SH003 · S06_SH007 장소 → LOC_CHEONMACHONG_V01, 착지 구도 기록 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame`.
**3** 자체 촬영 = **GREEN** (증빙: self-shot / original footage / source file retained). BLUE 는 확인 중·게시 금지 유지 (RIGHTS_STANDARD).
**4** 월성·사찰 = 선택 촬영. EP01 필수 영상은 대릉원·천마총 중심, 선택 촬영이 일정을 흔들면 안 됨.
**5** G13 = 동서 옆 단면 (머리 동쪽 · 금관 · 머리맡 궤) + 작은 평면 inset (T자 배치만).
**6** 해석 문장 hedge: "It may have belonged to a burial system of status, ceremony, and identity." (대본 v2 · SCRIPT_ROUGHCUT_DELTA)
**7** G04 층 순서 = 관 → 목곽 → 돌·자갈 → 흙 봉분. 별도 부장품 층 없음, 부장품은 관·목곽 주변 배치.

### D-027 · 2026-09-13 · EP01 Master Frames 최종 확정 · 군중 참고 그림 규칙 (사용자)
**확정** `EP01_S04_MASTER_V01` = V05 (참고 그림 없이 새로 생성, 군중 얼굴 복제 해소) · `EP01_S06_MASTER_OPEN_CHAMBER_V01` = V02 (관 형태·원로 허리띠 수정) · `EP01_S06_MASTER_MOUND_BUILDING_V01` = V01. 전부 APPROVED.
**근거** V05 는 복제 느낌·시대 위반(전봇대·건물·줄자·검은 띠)·공사 단계를 해결. 남은 미세 요소(뒤쪽 쇠처럼 보이는 삽 2자루, 지평선 흰 점)는 와이드 장면에서 영향 작음 → 추가 재생성은 새 문제 위험이 더 큼 (Change Only What Failed · Generate Late).
**비용** 기준 그림 8 호출 / 16 credits, `APR_EP01_MF_001` 한도 10 중 2 호출은 버퍼로 미사용하고 종료. EP01 누적 60.12 credits.
**운영 규칙** 군중 장면에 참고 이미지를 강하게 넣으면 얼굴 복제 위험 → 군중 복식·분위기는 문장 설명 중심, 참고 이미지는 반복 인물 continuity 가 필요한 경우에만 제한적으로 (CHARACTER_CONTINUITY_STANDARD §군중 장면의 참고 그림).
**다음** AI 샷 8개 생성 방법·비용 관리안 정리 (사용자 요청).

### D-028 · 2026-09-13 · 영상 공급자 · D-024 의미 명확화 · 논리 분류와 공급자/모델 분리 · H06 사진 승인 (사용자)
**D1 (A)** 영상 생성은 **Higgsfield 를 공급 플랫폼(provider)** 으로 쓰고 **실제 모델은 Kling 3.0 (model)**. "Higgsfield 방식" 승인이 아니다.
**D-024 명확화 (폐기 아님)** `HIGGSFIELD CAMERA / EXTREME CAMERA PIPELINE = 0 shots` · `Higgsfield as model provider = allowed` · `Selected model for current I2V test = Kling 3.0`.
**분류 분리** 모델·서비스 이름을 샷 판정에 박지 않는다. 샷에 `logical_pipeline` · `provider` · `model` 을 별도로 남긴다: 사람 동작 사진→영상 = `I2V_MOTION / HIGGSFIELD / KLING_3_0`, Blender 필요 = `BLENDER_I2V / HIGGSFIELD / KLING_3_0`, 정지 = `AI_STILL / HIGGSFIELD / NANO_BANANA_PRO`, 극단 카메라 = `EXTREME_CAMERA` (EP01 0). 기존 `pipeline` 값(FLOW_VEO · BLENDER_FLOW)은 호환 때문에 유지. 라우터에 `selected_provider/selected_model`, 영상 6개 `provider_candidates` 에 Higgsfield (Kling 3.0) 추가. 검증기: AI 샷은 세 필드 필수 + 대응 일치.
**D3** Blender 없이 기준 그림/시작 사진 + 카메라 초안 → I2V 로 먼저 시도. **같은 샷 공간 오류 2회 연속 → STOP → Blender 전환 여부 재승인. 자동 3번째 생성 금지.**
**D4** `APR_EP01_AI_B1_001` H06 (`EP01_S06_SH010`) 사진만, 최대 2 호출 / 4 credits, 영상 미포함. 첫 결과가 승인 가능하면 2번째 미사용. 실패 시 실패 항목만 새 prompt 버전 + PATCH.
**D2 (P-012 미정 유지)** 원화 환산은 실제 계정 월 결제 금액(원화 청구액) + 월 지급 크레딧으로 확정. 봇은 공개 요금표 숫자를 임의로 기록하지 않는다. **영상 생성은 아직 승인하지 않음.**

### D-029 · 2026-09-13 · Codex 중계 종료 · 봇 자체 멀티 에이전트 운영 (사용자)
**배경** 사용자가 Codex ↔ Claude Code 결과를 옮기던 흐름이 Codex 토큰 소진으로 끊김. 사용자: "코덱스의 사고를 받아서 자체적으로 멀티 에이전트로 진행하고 OS 로 검수·검증하면서 진행".
**운영** ① 작업 에이전트(분리된 파일 범위) → ② **Codex 역할 반박 검수 에이전트** (독립 컨텍스트, OS 규칙·데이터 대조, VERDICT + 파일:줄 근거) → ③ `validate.py` 종료 코드 0 → ④ 커밋 → ⑤ 작업 브랜치 push (D-025) → ⑥ 사용자에게 쉬운 한국어 요약. 큰 단계 끝의 교차 검수는 Codex 대신 반박 검수 에이전트가 맡는다 (같은 계열 모델 한계는 기록에 명시).
**유지되는 사람 관문** 유료 생성 승인(Money Gate), 그림 최종 OK/FIX, 역사 해석 결정, main 병합. 사용자가 크레딧 한도를 명시적으로 위임하기 전까지 봇은 유료 호출을 스스로 승인하지 않는다.

### D-030 · 2026-09-13 · H06 1회 추가 · P-012 유지 · 사진 크레딧 위임 한도 (사용자 "1,2,3 너의 추론대로")
**1** H06 (`EP01_S06_SH010`) 1회 추가 승인 — `APR_EP01_AI_B1_002` 최대 1 호출 / 2 credits, 문장 `PRM_EP01_S06_SH010_V04` (사람 규모 1:8 · 둥근 꼭대기 · 무술복 아닌 옷).
**2** P-012 는 **미정 유지**. 사용자가 앞서 "임의 숫자 금지, 실제 청구액이 정본"이라고 했으므로 봇은 공개 요금표로 확정하지 않는다. **영상 생성은 계속 미승인.**
**3 위임 한도 (사진 전용)** 봇이 스스로 승인할 수 있는 범위: AI 사진(AI_STILL · 기준 그림/사진 수정 편집)만, **샷당 최대 2 호출 / 4 credits**, 위임분 **누적 최대 20 credits** (초과 시 사용자 재승인). 실패 시 실패 항목만 새 버전 + PATCH, 2회 실패 시 STOP. **그림 최종 OK/FIX 는 사용자**. 영상(I2V_MOTION · BLENDER_I2V)과 영상용 시작 사진은 위임 제외 (Generate Late — 영상 승인 뒤). 위임 호출도 approval 기록을 남기고 `decided_by = 봇 (D-030 위임)` 으로 표기.

### D-031 · 2026-09-13 · H06 사진 최종 OK (사용자 "H06 OK")
**결정** `EP01_S06_SH010` (H06) 사진 **V03** (`08_GENERATION_CACHE/EP01/AI_STILL/H06_V03_4cc87427.png`, `GEN_EP01_S06_SH010_HIGGSFIELD_V03`) 승인 → 샷 `LOOK_APPROVED`, `approved_version = V03`.
**수용한 작은 점** 사람 규모 약 1/5–1/6 (목표 1/8), 먼 인물 옷 일부 현대적. H06 총 3 호출 / 6 credits, 추가 호출 없음.

### D-032 · 2026-09-13 · 경주 짧은 촬영 (사용자 "1번 경주 방문 관련 2번으로 다음주에 가서 찍어서 올테니")
**결정** `15_QA/REAL_SHOT_ALTERNATIVES_20260913.md` §5 안 B — 다음 주 짧은 촬영. **꼭 찍기 5컷**: S01_SH001 · S01_SH002 · S09_SH003 · S08_SH003 (매치컷 착지) · S08_SH001. **시간 남으면 5컷**: S02_SH001 · S03_SH001 · S06_SH007 · S06_SH011 · S09_SH004 (못 찍으면 인터넷 사진 후보로 대체).
**유지** H07 은 촬영 뒤 생성 (D-018 순서 그대로). CC BY-SA 사용 여부 · 포토코리아 확인은 대체가 필요할 때만 결정.
**TODO** `02_SEASONS/S01/EP01/08_REAL_FOOTAGE/SHOOT_TODO_EP01_20260913.md` (촬영 허가 문의 Q1–Q5 · 날짜·예비일 · 촬영자 · 원본 보관은 사용자).

### D-033 · 2026-09-14 · 제작 방식 전환 — 벤치마크 반영 (사용자 "그래")
**근거** `09_ANALYTICS/benchmarks/BENCHMARK_ARCHDICT_GYEONGHOERU_20260914.md` (신비한 건축사전 경회루 영상, 사용자 판정: 현장 촬영 0, 실사풍은 전부 가져온 사진의 AI 재구성).
**결정**
1. 기본 제작 파이프라인 2개를 OS 표준으로 세팅: **A. 사진 탐색 → AI 리디자인(실사풍 재구성) → 필요 시 영상화** · **B. 3D 단면·도해 애니메이션**. 현장 촬영은 필수가 아닌 선택지로 내림 (D-032 경주 촬영은 유지, 비교용 실사 앵커).
2. 파이프라인 A 원본은 **GREEN 만** (CC0 · PD · 공공누리 1유형). YELLOW 는 구도 수치만 옮겨 적음, RED 금지. AI 재구성 결과물은 원본 권리를 승계하며 AI 라벨 필수.
3. **사람은 유지한다.** 벤치마크 채널과 달리 우리는 MINDSET·CHOICE 를 보여주는 AI 재현 인물 컷(5–6초, 전체 10% 안팎)을 반드시 둔다. Character Master 자산은 차별점.
4. 목표 배합 (EP02 부터 기본, EP01 은 참고): 3D 도해 30–35% · 사진→AI 재구성 25–30% · 유물 아카이브 20–25% · AI 인물 10% 안팎 · 현대 실사 5–10%.
5. **스토리 엔진 템플릿** 을 도구와 같은 무게로 세팅. 벤치마크에서 가져올 것: 상식 처방 기각 칸(QUESTION 과 FACT 사이) · 한 줄 주제로 긴 시간 꿰기 · 숫자·치수를 화면에 보여주기. 버릴 것: 공학 설명서 톤 · 사람 없는 화면 · 국내 시청자 전제.
6. 차별점은 화면 품질이 아니라 질문의 각도("왜 그들에게 말이 됐나")와 근거 표시(FACT / INTERPRETATION 을 화면에서도 구분).

### D-034 · 2026-09-14 · 샘플 1–3 검토 뒤 4건 (사용자 "너의 추론대로")
**1** ② REJECTED OBVIOUS ANSWER 는 **EP02 부터** 적용. EP01 대본은 러프컷 v1 기준 유지 (D-010), ③ 치수선(GT-03) 만 GRAPHICS_SPEC 에서 추가.
**2** GREEN 원본 없는 샷: YELLOW 수치만 옮긴 텍스트 전용 생성 → 안 되면 현장 촬영 (D-032 유지).
**3** 파이프라인 A 첫 유료 시험 = `EP01_S02_SH001` 1장 (GREEN Gagnon CC0 원본, 최대 1 호출 / 2 credits, D-030 사진 위임 한도 안). **실행은 Higgsfield 커넥터 재인증 뒤**, prompt 인스턴스 저장 + approval 기록 후 Sent Prompt Rule.
**4** `STORY_ENGINE_STANDARD` · `PHOTO_AI_STANDARD` · `DIAGRAM_TEMPLATES` 는 2026-09-14 전체 검수(D-029 반박 검수) 통과 뒤 ACTIVE.

### D-035 · 2026-09-14 · 전체 검수 보고서 §4 B 8건 (사용자 "8건 전부 권고대로 승인")
**근거** `02_SEASONS/S01/EP01/15_QA/REVIEW_FIX_20260914.md` §4. Higgsfield claude.ai 커넥터 잔액 재조회 1,676.58 credits (plus) 확인 뒤.
**1** PRESENT lock 쌍 신설 `06_PROMPT_LIBRARY/locks/DDABONG_GLOBAL_PRESENT_V01` + `DDABONG_NEGATIVE_PRESENT_V01` (APPROVED). 역사 GLOBAL/NEGATIVE 는 그대로.
**2** 현재 시점 사진 기반 재구성 라벨 = `AI Visual Reconstruction (present-day, photo-based)`. `shot.schema.ai_label` description · HISTORY_ACCURACY 규칙 2 · G09 갱신.
**3** D-028 `I2V_MOTION` 정의를 "사진→영상 (인물 동작 · 풍경/장소 카메라 이동)" 으로 확장. 분류·공급자·모델 분리 원칙은 그대로.
**4** 파이프라인 A 시험 절차 확정: `EP01_S02_SH001` 라우터 OVERRIDDEN (REAL_SHOOT → AI_STILL, note) · pipeline/logical/provider/model · ai_label · photo_ai → prompt `PRM_PA_EP01_S02_SH001_V01` 저장 → approval `APR_EP01_PA_001` (D-034 #3, 1 호출 / 2 credits) → 전송. D-032 촬영 병행. 11초 샷은 경관 3–4컷 중 1컷을 이 정지 이미지로 채운다.
**5** `approval.money_gate_presented` 의 `expected_attempts` · `prompt_ids` required 승격 (기존 6건 전부 충족). AI 샷 `duration ≤ 6` 검증 규칙 — **현재 시점 사진 기반(photo_ai) 정지 컷은 예외** (D-009 5–6초 제한은 인물 재현 컷 대상; 봇 판단, 사용자 이견 시 S02_SH001 분할).
**6** `approval.delegated: true` 필드 (D-030 위임 승인). 검증기: decided_by 에 '봇' · 시도 ≤ 2 · 샷당 ≤ 4 credits · 누적 ≤ 20 credits.
**7** `CAMERA_GRAMMAR.md` 기본값 35 mm · 1.6 m · tilt 0° 명시.
**8** `STORY_ENGINE_STANDARD` · `PHOTO_AI_STANDARD` · `DIAGRAM_TEMPLATES` v0.1 **ACTIVE**. PHOTO_AI 의 'A4 보류' 조건은 #1 과 함께 해소되어 A4 포함 전부 ACTIVE.

### D-036 · 2026-09-14 · 파이프라인 A 기본 모델 = Nano Banana 2 (사용자 "Nano Banana 2를 파이프라인 A 기본으로 인정")
**경위** S02_SH001 시험 (`GEN_PA_EP01_S02_SH001_HIGGSFIELD_V01`, 2 credits) 이 Higgsfield 카탈로그 id `nano_banana_2` 로 나갔는데 실제 job_set_type 은 `nano_banana_flash` ('Nano Banana 2'). 승인 문구의 NANO_BANANA_PRO (H06 이 쓴 job `nano_banana_2`) 와 다름. 결과가 기준 통과.
**결정** 파이프라인 A (사진 기반 현재 시점 재구성) 기본 모델 = `NANO_BANANA_2` (HIGGSFIELD). 역사 인물·기준 그림은 기존 NANO_BANANA_PRO 유지. `MODEL_ROUTER.md` 모델 표 갱신, S02_SH001 샷·라우터·승인 model 값 정정. 재생성 없음 (추가 비용 0). **운영 규칙 추가**: 전송 전 preflight 결과의 job_set_type 을 승인 문구와 대조, 다르면 전송 전 보고.

### D-037 · 2026-09-14 · 파이프라인 A 시험 1장 최종 OK (사용자 "ok")
**결정** `EP01_S02_SH001` V01 (`GEN_PA_EP01_S02_SH001_HIGGSFIELD_V01`, `08_GENERATION_CACHE/EP01/AI_STILL/PA_S02_SH001_V01_9cbd059e.png`) **APPROVED** → 샷 LOOK_APPROVED, approved_version V01. 작은 점 (오른쪽 말뚝·줄·포장길 잔존, 왼쪽 소나무) 수용, 추가 호출 없음. **파이프라인 A 첫 시험 성공** — 사진→AI 재구성 2 credits 로 기준 통과. EP01 누적 68.12 credits.
**의미** PHOTO_AI_STANDARD A1–A6 전 단계가 실제로 한 번 돌았다 (탐색 → 권리 → 프롬프트 → 승인 → 전송 → 라벨·계보·검증). EP02 부터 25–30% 배합 (D-033 #4) 적용 가능.

### D-038 · 2026-09-14 · 현장 촬영 제외 — EP01 전부 자체 제작 (사용자 "직접 촬영 말고, 우리가 자체적으로 해보자고")
**결정** D-032 경주 촬영은 **하지 않는다.** REAL_SHOOT 9샷 전부 파이프라인 A (GREEN 사진 → AI 재구성) 로 전환. GREEN 없는 샷은 D-034 #2 (YELLOW 수치만 옮긴 텍스트 전용). 움직임 중심 2샷 (S01_SH001 거리 · S08_SH001 몽타주) 은 정지 이미지 뒤 I2V (P-012 뒤).
**GREEN 추가 5** `RTS_COMMONS_DAEREUNGWON_MIETCHEN_PINE_001` · `_MOUND_001` · `_VALLEY_001` · `RTS_COMMONS_CHEONMACHONG_SIGN_MIETCHEN_001` · `RTS_COMMONS_HWANGNAMDAECHONG_GAGNON_001` (전부 CC0, 원본 `02_SEASONS/S01/EP01/02_SOURCES/`, 페이지 proof 저장).
**봇 규칙** 앞으로 "현장 촬영" 을 다음 단계로 제안하지 않는다.

### D-039 · 2026-09-14 · 파이프라인 A 배치 1 (8장, 16 credits) + D-026 완화 (사용자)
**승인** `APR_EP01_PA_002` — S01_SH002 (→ S09_SH003 재사용) · S02_SH001 추가 2컷 · S03_SH001 표지 · S06_SH007 · S06_SH011 (뒷모습 관람객 소수 추가) · S08_SH003 · S09_SH004 (골든아워). 각 1회, 2 credits, 실패 시 STOP. 최종 OK/FIX 는 8장 일괄.
**D-026 완화** 매치컷 착지 = "대릉원 봉분 (천마총형, 47 m·12.7 m 비율)". 원본 MOUND_001 은 어느 고분인지 미확인이나 AI 재구성이라 화면에 드러나지 않음. H07 은 같은 비율로 생성.

### D-040 · 2026-09-14 · 파이프라인 A 배치 1 8장 전부 OK (사용자 "8장 전부 OK")
**결정** `APR_EP01_PA_002` 8/8 SUCCESS → 전부 APPROVED. 샷 LOOK_APPROVED: S01_SH002 · S02_SH001 (V01 + 컷2 V02 + 컷3 V03) · S03_SH001 · S06_SH007 · S06_SH011 · S08_SH003 · S09_SH003 (S01_SH002 이미지 재사용) · S09_SH004 (지형 이탈 수용 — 엔딩 여운 컷). 추가 호출 0. EP01 누적 84.12 credits.
**결과** EP01 현재 시점 실사 컷 중 7샷이 정지 이미지로 확보됨 (원래 REAL 10 중 S02 + 7 = 8 완료). 남은 2: S01_SH001 거리 · S08_SH001 몽타주 (I2V 필요, P-012 뒤). 파이프라인 A 누적: 9장 생성 · 9장 승인 · 실패 0 · 18 credits.

### D-041 · 2026-09-14 · 사용자 캡처 21장 = RED, 구도만 옮겨 텍스트 전용 4장 (사용자 "구도만 옮겨 텍스트 전용 4장 (8 credits)")
**판정** `경주 사진 모음/` 캡처 21장은 유튜브 방송·채널 화면 (MBN · YTN · MeyGold · MBC 나혼자산다/픽잇) → **RED** (`RTS_YOUTUBE_CAPTURES_GYEONGJU_001`). 자막·로고를 지워도 저작권 그대로 → 화면 사용·AI 참고 첨부 금지 (D-033 #2). 폴더는 `.gitignore` (커밋 안 함), 구도 연구용으로만 보관.
**결정** D-034 #2 방식으로 남은 2샷 생성: S01_SH001 황리단길 거리 1장 · S08_SH001 몽타주 3장 (산책로 · 한옥 카페 · 봉분 옆 도로). 이미지 미첨부, 구도 수치만 `photo_ai.composition_ref_note`. `APR_EP01_PA_003` 4 호출 / 8 credits. S08_SH001 15초 = 정지 3 × 5초 (원래 8–12클립 축소), 움직임은 I2V (P-012 뒤).
**규칙 메모** 거리·몽타주 샷은 차·사람이 목적이라 NEGATIVE_PRESENT 의 'vehicles'·'crowds' 를 해당 샷에 한해 유보 (prompt shot_delta 에 명시). 판독 가능한 간판·식별 가능한 얼굴 금지는 유지.

### D-042 · 2026-09-14 · 배치 2 판정: 3장 OK + M2 카페 재생성 (사용자 "3장 OK + M2 카페 재생성 (2 credits)")
**결정** S01_SH001 V01 LOOK_APPROVED · S08_SH001 M1 (V01) · M3 (V03) APPROVED · M2 (V02) REJECTED — 손님 얼굴 AI 블러 흔적 · 칠판 낙서 · 차 엠블럼. FIX = `PATCH_EP01_S08_SH001_M2_001` → `PRM_PA_EP01_S08_SH001_M2_V02` (손님 2명 뒷모습·멀리, 칠판 없음, 엠블럼 없음). 승인 `APR_EP01_PA_004` **위임 (D-030)**, 1회 / 2 credits, 실패 시 STOP.
**결과** REAL 10샷 중 9샷 정지 이미지 확보 (S08_SH001 은 3컷 중 2컷 확정). EP01 누적 92.12 credits (재생성 전).

### D-043 · 2026-09-14 · M2 카페 V02 OK — EP01 현재 시점 실사 10샷 전부 정지 이미지 확정 (사용자 "OK")
**결정** `GEN_PA_EP01_S08_SH001_M2_HIGGSFIELD_V02` APPROVED (위임 1회, 2 credits) → S08_SH001 LOOK_APPROVED (M1 · M2 V02 · M3). 차 엠블럼은 편집에서 흐림.
**결과** 원래 REAL_SHOOT 10샷 → 전부 파이프라인 A 정지 이미지로 LOOK_APPROVED (S01_SH001 · S01_SH002 · S02_SH001×3 · S03_SH001 · S06_SH007 · S06_SH011 · S08_SH001×3 · S08_SH003 · S09_SH003 · S09_SH004). 파이프라인 A 누적: 14 생성 · 13 승인 · 1 REJECTED(M2 V01) · 28 credits. EP01 누적 94.12 credits, 잔액 1648.58. 위임 누적 2/20.
**다음** 움직임 필요 컷 (S01_SH001 · S08_SH001 M1–M3 · S01_SH002 리빌) 은 I2V Kling 3.0 — P-012 뒤 승인. H07 (S08_SH002) 은 S08_SH003 플레이트에 맞춰 생성 가능. GT-0x 도해.

### D-044 · 2026-09-14 · H07 (S08_SH002) 생성 승인 — S08_SH003 플레이트에 맞춤 (사용자 "승인 — 최대 2회 / 4 credits")
**전제** 착지 플레이트 = `GEN_PA_EP01_S08_SH003_HIGGSFIELD_V01` (D-040). 실측값 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame` 기록 (꼭대기 x0.44/y0.31, 지평선 y0.62, 밑변 0.00–0.95, 35 mm·1.6 m·0°). D-018 의 "현장 SH003 촬영 뒤" 조건은 D-038 로 AI 플레이트로 대체.
**승인** `APR_EP01_AI_B1_003`: `PRM_EP01_S08_SH002_V02` (V01 + 매치컷 수치 + 맨흙 봉분), Nano Banana Pro (카탈로그 `nano_banana_pro` 확인), 참고 이미지 = S08_SH003 플레이트 (job id). 최대 2회 / 4 credits.

### D-045 · 2026-09-14 · H07 2차 OK (사용자 "OK")
**경과** 1차 (`GEN_EP01_S08_SH002_HIGGSFIELD_V01`) PARTIAL — 봉분 중앙·좁음, 산 지평선, 겨울 들판, 지평선 끝 인공물. `PATCH_EP01_S08_SH002_001` → V03 (참고 이미지 구도 그대로, 표면만 맨흙, 초여름, 인공물 0). 2차 (`_V02`) PASS.
**결정** H07 V02 **APPROVED** → `EP01_S08_SH002` LOOK_APPROVED. G10 매치컷 양쪽 플레이트 확보 (과거 H07 ↔ 현재 S08_SH003). 꼭대기 5–10% 우측 편차는 편집 정렬. 4 credits, EP01 누적 98.12. 승인 한도 소진, 추가 생성 없음.
**결과** EP01 AI 정지 컷 전부 확보: H06 · H07 · 파이프라인 A 13. 남은 AI = 영상 H01–H05 + I2V (P-012 뒤).

---

## 승인 대기 (P)

### P-012 · Higgsfield 크레딧 → KRW 환산율 (Money Gate 계산용)
**현황** 예산은 KRW ₩40,000 (D-015), 소진은 Higgsfield 크레딧 (배치 1 = 8.12 credits, plus 플랜). 환산율이 없어 `cost.percent_used` 를 계산할 수 없다.
**제안** 플랜 월 요금 ÷ 월 크레딧으로 1 credit 당 KRW 를 정해 `COST_STANDARD.md` 에 기록. **D-028: 실제 계정 청구 원화 금액 + 월 지급 크레딧(Manage Account → Subscription 캡처 또는 수치)으로만 확정. 영상 배치 전 필수.**
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
