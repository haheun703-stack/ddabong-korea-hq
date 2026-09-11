# CURRENT STATUS — 지금 어디까지 왔나

> **매 작업마다 갱신한다.** 이 파일 하나만 읽으면 어느 봇/AI 창을 열어도 바로 이어갈 수 있어야 한다.
> 갱신: 2026-09-11 (Claude Code, P1) · 마지막 사용자 승인: 2026-09-11 (P0 범위·EP01 파일 유지·push 전 확인 → D-007)
> 읽는 순서: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` → `BOT_BOOTSTRAP_PROMPT.md` → **이 문서** → `OS_INDEX.md` → `02_SEASONS/S01/EP01/episode.json`

---

## 지금 우선 작업

**사용자 손에 있는 것**
- P-001 EP01 생성 예산 금액 (Money Gate 기준값) — 미확인이면 유료 생성 게이트는 `UNKNOWN_BUDGET` 으로 잠김.
- P-002 에피소드 ID 자릿수 (`EP01` 유지 vs `EP001` 통일).
- P-003 표준 문서 언어 (P0 초안은 한글 본문 + 영문 키/ID).
- `p1-continuity` → main 병합 시점 (D-012: 다음 검수 게이트 전까지 보류).

- **P-009** 원로(`CHAR_SILLA_ELITE_OBSERVER_01`) 옷 색 비(다홍) vs 청 · 과대 재질 — 관등 미설정이라 INTERPRETIVE (NEW).

- **P-011** 라우터 판정 49건 ACCEPT / OVERRIDE (핵심: H05 BLENDER_FLOW vs Higgsfield).
- YELLOW_ACTIVE 1건 (`RTS_GNM_OTHER_OBJECTS_001`) — 편집 확정 전 필수 해소 (D-014).

**봇이 바로 갈 수 있는 것**
- P2 Character Master 준비 문서: 원로 FULL 10종 + 군중 LITE 3종 프롬프트 조립(§8 lock 조각) — 생성은 예산(P-001) 후.
- `camera.json` 수동 작성: BLENDER_FLOW 6컷 (Blender 브리지 P7 전).
- graphics-spec v2 (G13 추가) — legacy HTML 은 수정하지 않고 새 문서로.

## P4 — Shot Router (2026-09-11 · DONE, 사용자 ACCEPT 대기 P-011)

| 항목 | 산출 | 상태 |
|---|---|---|
| 라우터 판정 | `07_SHOTS/router_decision_RTR_EP01_*_V01.json` 49건 — 점수 6종 + recommended/fallback/reason/rule | `PENDING` |
| 재판정 결과 | legacy Higgsfield 8 → **HIGGSFIELD 1** (H07 매치컷) · **BLENDER_FLOW 6** (H01–H05) · **AI_STILL 1** (H06) | 샷 `pipeline` 갱신, `status = ROUTED` |
| 최종 구성 | REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 6 · AI_STILL 1 · HIGGSFIELD 1 | — |
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
- P3 Source/Rights Ledger: research-v2 S1–S6 → `05_HISTORY_DATABASE/sources/`, claim safety table → `facts/`, 그다음 샷 `fact_ids` 연결.
- P4 Shot Router: 43개 샷 `router_decision.json` (특히 H01–H06 → BLENDER_FLOW 재검토).

---

## P1 — Continuity Engine (2026-09-11 · **COMPLETE — APPROVED WITH CONDITIONS** D-008~D-012)

브랜치 `p1-continuity` (`6a60b1b` `a89734b` origin push 완료, main 병합 보류). **Web HQ 는 main 만 배포하므로 P1 COMPLETE 표시는 병합 시점에 동기 반영** (사용자 결정, 2026-09-11). P2 백로그: P-008 인물 가시성 필드. 조건: Lite Crowd Pack (D-008) · AI 컷 5–6초 (D-009) · 러프컷 임시 기준 + DELTA 정리 (D-010) · 복식 TBD 게이트 (D-011).
**P2 NEXT — Character Master** (선행: D-011 복식 확정 + P-001 예산).

| 항목 | 산출 | 상태 |
|---|---|---|
| ERA | `05_HISTORY_DATABASE/era/` `SILLA_EARLY` · `EXCAVATION_1973` · `PRESENT_DAY` | DONE |
| LOCATION | `locations/` 대릉원 · 천마총(치수 47 m/12.7 m, 목곽 6.6×4.2 m) · 경주 도심 · 국립경주박물관 | DRAFT |
| COSTUME | `costumes/` 노동자 · 시종 · 원로 `_A01` — **D-011 근거 확정 완료** (PROBABLE, fact_ids 연결) | DRAFT |
| FACT / SOURCE (복식) | `facts/CLM_SILLA_COSTUME_001–008` · `sources/SRC_*` 7건 (국사편찬위·삼국사기 색복·국립중앙박물관·민족문화대백과·전통문화포털·1976 직물 논문·짚신 토기 보도) | DONE |
| CHARACTER | `characters/` 원로 1인 (FULL) + 군중 2그룹 (LITE_CROWD) | DRAFT |
| Master Pack 요구 목록 | `characters/EP01_MASTER_PACK_REQUIREMENTS.md` | DONE |
| 씬·샷 분해 | `02_SEASONS/S01/EP01/07_SHOTS/` 씬 9 · 샷 48 (러프컷 v1 기준 + D-009 분할, 합계 425초 = 7:05) | `BROKEN_DOWN` / `PLANNED` |
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
| SHOT_ROUTER | `07_SHOTS/router_decision_*` 49 + `15_QA/P4_ROUTER_REPORT.md` | DONE (P4) · ACCEPT 대기 P-011 |
| REAL_SHOOT | `ep01-field-shoot-plan` 체크리스트 | 계획 APPROVED · **촬영 미실행** |
| ARCHIVE | `ep01-archive-photos` (1973 NRICH), `ep01-artifact-library` | 선별 APPROVED · 파일 다운로드 미실행 |
| HIGGSFIELD | `ep01-higgsfield-prompts` 7컷 | 프롬프트 APPROVED · **생성 금지 (Money Gate 미승인, 예산 미확인)** |
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
| EP01 예산 | **미확인** (P-001) |
| 소진 | 미확인 |
| 게이트 상태 | `UNKNOWN_BUDGET` → 유료 생성 잠금 |

---

## 검수 요청 (needs_review)

- `00_SYSTEM/standards/*.md` 22개 v0.1 DRAFT — 사용자 승인 시 ACTIVE (P-004).
- P1 인스턴스 전체 DRAFT — 특히 `CHAR_SILLA_ELITE_OBSERVER_01` 인물 설정(피장자·왕 아님)과 복식 방향.

---

## 차단 / 미결

- 예산 미확인 → 유료 생성 전면 잠금 (규칙 위반 아님, 정상 상태).
- Blender 로컬 브리지(P7) 없음 → `camera.json` 은 수동 작성 단계.
- ~~복식 세부 근거 미확보~~ → 2026-09-11 해소 (D-011 게이트 통과). 잔여: 짚신 출처가 언론 보도 → P3 에서 박물관 페이지로 교체 권장.

---

## 최근 변경 (최신순)

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
