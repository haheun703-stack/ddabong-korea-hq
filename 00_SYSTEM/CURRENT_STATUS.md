# CURRENT STATUS — 지금 어디까지 왔나

> **매 작업마다 갱신한다.** 이 파일 하나만 읽으면 어느 봇/AI 창을 열어도 바로 이어갈 수 있어야 한다.
> 갱신: 2026-09-11 (Claude Code) · 마지막 사용자 승인: 2026-09-11 (P0 범위·EP01 파일 유지·push 전 확인 → D-007)
> 읽는 순서: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` → `BOT_BOOTSTRAP_PROMPT.md` → **이 문서** → `OS_INDEX.md` → `02_SEASONS/S01/EP01/episode.json`

---

## 지금 우선 작업

**사용자 손에 있는 것 3개**
- P-001 EP01 생성 예산 금액 (Money Gate 기준값) — 미확인이면 유료 생성 게이트는 `UNKNOWN_BUDGET` 으로 잠김.
- P-002 에피소드 ID 자릿수 (`EP01` 유지 vs `EP001` 통일).
- P-003 표준 문서 언어 (P0 초안은 한글 본문 + 영문 키/ID).

**봇이 바로 갈 수 있는 것: P1 — Continuity Engine**
- `05_HISTORY_DATABASE/` 에 EP01 실제 인스턴스 생성: `era/SILLA_EARLY.json`, `locations/LOC_GYEONGJU_DAEREUNGWON_V01.json`, `LOC_CHEONMACHONG_V01.json`.
- `episodes/ep01-higgsfield-prompts.html` 의 역사 재현 7컷 → `character.json` 후보 추출 → Character Master Pack 요구 목록 작성 (생성은 Money Gate 이후).
- EP01 씬/샷 분해: `episodes/ep01-premiere-roughcut.html` 타임라인 → `02_SEASONS/S01/EP01/07_SHOTS/scene_*.json`, `shot_*.json` (승인된 대본 v2 기준, 새로 쓰지 않음).

---

## P0 — OS 정본 문서·스키마 (2026-09-11 · DONE, push 대기)

| 항목 | 상태 |
|---|---|
| §21 폴더 골격 `01_CHANNEL` ~ `10_EXPORTS` + 에피소드 템플릿 18폴더 | DONE |
| `00_SYSTEM/schemas/` 29개 JSON Schema + TEMPLATE 예시 + `validate.py` (30/30 PASS) | DONE |
| `02_SEASONS/S01/EP01/episode.json` 매니페스트 (기존 `episodes/ep01-*` 참조, 이동 없음) | DONE |
| 운영 문서 `CURRENT_STATUS` `AGENT_RULES` `DECISIONS` `ACTIVE_TASK` | DONE |
| §22 표준 문서 22개 v0.1 DRAFT (`00_SYSTEM/standards/`) | DONE (DRAFT — 승인 전까지 정본 §N 우선) |
| `OS_INDEX.md` + Web HQ `os-index.html`, `index.html`/`bot-handoff.html` 링크 | DONE |
| GitHub push → Web HQ 반영 | **대기 — 사용자 확인 후** |

---

## EP01 「경주 왕릉 / 천마총」 — Why Are Giant Tombs Everywhere in This Korean City? (ACTIVE)

**현재 게이트: `REAL_SHOOT`** (프리프로덕션 ≈91%) · 매니페스트 `02_SEASONS/S01/EP01/episode.json` · Web HQ `episodes/ep01-gyeongju-tombs.html`

| 단계 | 산출물 | 상태 |
|---|---|---|
| RESEARCH | `episodes/ep01-research-verified-v2.md` | APPROVED |
| SCRIPT | `episodes/ep01-production-script-v2.md` (v1은 PREVIOUS) | APPROVED |
| SHOTLIST | `ep01-visual-assets`, `ep01-graphics-spec` (G01–G12) | APPROVED |
| REAL_SHOOT | `ep01-field-shoot-plan` 체크리스트 | 계획 APPROVED · **촬영 미실행** |
| ARCHIVE | `ep01-archive-photos` (1973 NRICH), `ep01-artifact-library` | 선별 APPROVED · 파일 다운로드 미실행 |
| HIGGSFIELD | `ep01-higgsfield-prompts` 7컷 | 프롬프트 APPROVED · **생성 금지 (Money Gate 미승인, 예산 미확인)** |
| ROUGH_CUT | `ep01-premiere-roughcut` 0:00–7:05 | 설계 APPROVED |

**다음 실제 작업 (순서)**
1. 경주 현장 촬영 (좁은 주제 + 넓은 클러스터 촬영: 불국사·다보탑/석가탑·석굴암·첨성대·박물관·월정교/동궁).
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

- `00_SYSTEM/standards/*.md` 22개 v0.1 DRAFT — 정본 내용 이관본. 사용자 승인 시 `standard_version` 을 ACTIVE 로 올린다. 승인 전에는 정본 §N 이 우선.

---

## 차단 / 미결

- 예산 미확인 → 유료 생성 전면 잠금 (규칙 위반 아님, 정상 상태).
- Blender 로컬 브리지(P7) 없음 → `camera.json` 은 수동 작성 단계.

---

## 최근 변경 (최신순)

- **2026-09-11 Claude Code** — P0 완료: 폴더 골격, 29 스키마, EP01 매니페스트, 운영 문서 4종, 표준 22개 DRAFT, OS_INDEX + Web HQ 페이지. 로컬 브랜치 `p0-os-schemas` 커밋. push 대기.
- **2026-09-11 사용자** — **D-007.** P0 범위 = 핵심 완성 + 나머지 골격 / EP01 파일 제자리 유지 + 매니페스트 / 커밋 후 push 전 확인.
- **2026-09-11 (이전 세션)** — **D-004~D-006.** 정본 v0.1 채택, 캐릭터 스타일 B Documentary Reenactment, EP01 = 경주 왕릉/천마총, 황룡사는 예시. Bootstrap Prompt + Web HQ bot-handoff 페이지.
- **2026-08-16** — EP01 프리프로덕션 페이지 9종 완료 (research v2 · script v2 · visual · field shoot · archive · artifacts · higgsfield · graphics · roughcut).
- **2026-08-14 사용자** — **D-001~D-003.** 브랜드명 DDABONG KOREA · 슬로건 STORIES BEHIND KOREA · 핵심 콘셉트 · 파일럿 3편 (경주 왕릉 → 신라 금관 → 온돌).
