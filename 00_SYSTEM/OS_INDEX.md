# OS INDEX — DDABONG STUDIO OS v0.1 문서·스키마 지도

> 봇은 `BOT_HANDOFF` → `BOT_BOOTSTRAP_PROMPT` → `CURRENT_STATUS` → 이 문서 → 활성 에피소드 매니페스트 순으로 읽는다.
> 상태 `ACTIVE` = 현재 적용. `DRAFT` = 정본 내용 이관본, 승인 전까지 정본 §N 우선 (DECISIONS P-004).
> Web HQ: <https://haheun703-stack.github.io/ddabong-korea-hq/00_SYSTEM/os-index.html>

---

## 1. 운영 문서 (`00_SYSTEM/`)

| 파일 | 성격 | 바뀌는 빈도 | 상태 |
|---|---|---|---|
| `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` | 운영 계약 (정본) | 거의 안 바뀜 (개정은 D-번호) | ACTIVE |
| `BOT_BOOTSTRAP_PROMPT.md` | 봇 시작 프롬프트 | 가끔 | ACTIVE |
| `CURRENT_STATUS.md` | 지금 어디까지 왔나 · 현재 게이트 · 승인 필요 | 매 작업마다 | ACTIVE |
| `AGENT_RULES.md` | 에이전트 공동 작업 규칙 · 엔진별 담당/금지 | 가끔 | ACTIVE |
| `DECISIONS.md` | D-번호 결정 / P-번호 승인 대기 | 결정할 때마다 | ACTIVE |
| `ACTIVE_TASK.md` | 작업 잠금 | 작업 시작/종료마다 | ACTIVE |
| `OS_INDEX.md` | 이 문서 — 문서·스키마 지도 | 문서 추가 시 | ACTIVE |
| `schemas/_README.md` | 스키마 계약 · ID 규칙 · 공통 규칙 | 스키마 변경 시 | ACTIVE |

## 2. 표준 문서 (`00_SYSTEM/standards/`) — 정본 §22

| 파일 | 출처 § | 상태 |
|---|---|---|
| `ANALYTICS_STANDARD.md` | §2 §18 · 아스트라 §5 성과 기록 | DRAFT v0.1 |
| `BLENDER_STANDARD.md` | §6 | DRAFT v0.1 |
| `BRAND_INTRO_STANDARD.md` | §15 | DRAFT v0.1 |
| `CAMERA_GRAMMAR.md` | §6 §7 | DRAFT v0.1 |
| `CASE_MEMORY_SCHEMA.md` | §18 · 아스트라 §5 수정 사례 | DRAFT v0.1 |
| `CHARACTER_CONTINUITY_STANDARD.md` | §5 §20 | DRAFT v0.1 |
| `CONTENT_ROADMAP.md` | §19 · brand_decisions.json 파일럿 3편 | DRAFT v0.1 |
| `COST_STANDARD.md` | §11 | DRAFT v0.1 |
| `EXPERIENCE_LEARNING_STANDARD.md` | §1-7 §18 · 아스트라 인수인계 §5–§7 | DRAFT v0.1 |
| `HISTORY_ACCURACY_STANDARD.md` | §0 §9 | DRAFT v0.1 |
| `MASTER_CHANNEL_BIBLE.md` | §0 §19 · concept-bible.md · brand_decisions.json | DRAFT v0.1 |
| `MODEL_ROUTER.md` | §3 provider abstraction · §7 | DRAFT v0.1 |
| `MUSIC_STANDARD.md` | §16 | DRAFT v0.1 |
| `NARRATION_STANDARD.md` | §16 | DRAFT v0.1 |
| `PROMPT_STANDARD.md` | §8 | DRAFT v0.1 |
| `PUBLISH_STANDARD.md` | §2 §23 · D-046 설명란 템플릿·CTA·고정댓글·엔드스크린 | DRAFT v0.2 (2026-09-15) |
| `QA_STANDARD.md` | §2 §13 §17 | DRAFT v0.1 |
| `REGRESSION_TEST_STANDARD.md` | §1-7 §18 | DRAFT v0.1 |
| `RIGHTS_STANDARD.md` | §10 | DRAFT v0.1 |
| `SHOT_STANDARD.md` | §4 §12 §13 | DRAFT v0.1 |
| `SOUND_STANDARD.md` | §16 §17 | DRAFT v0.1 |
| `SOURCE_STANDARD.md` | §10 · 아스트라 §5 근거 묶음 | DRAFT v0.1 |
| `THUMBNAIL_STANDARD.md` | §14 | DRAFT v0.1 |
| `VISUAL_STYLE_BIBLE.md` | §5 §8 §20 · D-051 | DRAFT v0.2 |
| `STORY_ENGINE_STANDARD.md` | concept-bible 6단계 + D-033 (② 추가) | **ACTIVE v0.1** (D-035 #8, 2026-09-14) |
| `PHOTO_AI_STANDARD.md` | D-033 파이프라인 A · `tools/photo_search.py` · `06_PROMPT_LIBRARY/templates/PHOTO_AI_REDESIGN_V01.md` | **ACTIVE v0.1** (D-035 #8, 2026-09-14) |
| `DIAGRAM_TEMPLATES.md` | D-033 파이프라인 B (GT-01~04) | **ACTIVE v0.1** (D-035 #8, 2026-09-14) |
| `AUDIENCE_STANDARD.md` | D-046 자료집 역할 1 (페르소나·니즈맵·질문수집) · `01_CHANNEL/channel.json` | DRAFT v0.1 (2026-09-15) |
| `TITLE_STANDARD.md` | D-046 역할 4·5 (제목·썸네일 문구·훅 3곳) | DRAFT v0.1 (2026-09-15) |
| `EXPERIMENT_STANDARD.md` | D-046 역할 5 (A/B · 소재변형) · `analytics.experiment` | DRAFT v0.1 (2026-09-15) |
| `BENCHMARK_STANDARD.md` | D-046 역할 1 (경쟁사분석) · `09_ANALYTICS/benchmarks/` | DRAFT v0.1 (2026-09-15) |
| `SHORTS_STANDARD.md` | D-046 역할 3 (릴스) · 5 (UGC 대체) | DRAFT v0.1 (2026-09-15) |
| `COMMUNITY_STANDARD.md` | D-046 역할 6·7 (댓글유도·후속·재참여, 채널 등가물) · Community Agent | DRAFT v0.1 (2026-09-15) |

## 3. 스키마 (`00_SYSTEM/schemas/`) — 30개, JSON Schema draft-07

| 그룹 | 스키마 |
|---|---|
| 제작 계층 | `season` `episode` `scene` `shot` |
| Continuity | `era` `location` `character` `costume` `master_frame` |
| Source / Rights | `source` `fact` `rights` `license` `asset` |
| 시각 실행 | `prompt` `camera` `router_decision` `generation` `keep_change_patch` |
| 비용 / 승인 | `cost` `approval` |
| Learning | `case_memory` `failure_memory` `performance_memory` `standard_version` `evaluation` |
| 오디오 / 성과 | `music` `voice` `analytics` (`experiment` 구조화, D-046) |
| 채널 | `channel` (D-046, `01_CHANNEL/channel.json`) |

검증: `python 00_SYSTEM/schemas/validate.py` · 예시: `schemas/examples/*_TEMPLATE.json` (EP001_HWANGNYONGSA 템플릿 ID만).

## 4. 폴더 (`정본 §21`)

| 폴더 | 용도 | 상태 |
|---|---|---|
| `01_CHANNEL/` | 채널 기준서 `channel.json` · 캘린더 · 질문 은행 | DRAFT (D-046) |
| `02_SEASONS/S01/EP01/` | 활성 EP01 매니페스트 `episode.json` + 템플릿 18폴더 | **ACTIVE** |
| `03_SHARED_ASSETS/` `04_BLENDER_LIBRARY/` `05_HISTORY_DATABASE/` `06_PROMPT_LIBRARY/` `07_AUDIO_LIBRARY/` | 공유 라이브러리 | 골격 (P1~) |
| `08_GENERATION_CACHE/` `10_EXPORTS/` | 생성물·출력 (바이너리 미추적) | 골격 |
| `09_ANALYTICS/` | 성과·회귀검사 | 골격 |
| `episodes/` | EP01 프리프로덕션 산출물 (OS 이전, 이동 금지) | APPROVED · LEGACY 위치 |
| `assets/` | 로고 | ACTIVE |
| `NEXT_SESSION.md` `concept-bible.md` `brand_decisions.json` | 2026-08-14 원본 기록 | 보존 (SUPERSEDED / 참조) |

## 5. 빌드 순서 (정본 §25)

P0 OS 문서·스키마 ✅ (2026-09-11) → P1 Continuity ✅ → P2 Character Master ✅ (D-023) → P3 Source/Rights Ledger ✅ → P4 Shot Router ✅ (D-024) → **현재: D-033 파이프라인 A/B 세팅 · 시험 1장 대기** → P5 Review UI → P6 Money Gate + provider adapters → P7 Blender bridge → P8 Learning/regression → P9 Publish/analytics 자동화.
첫 실전 검증은 활성 EP01 (경주 왕릉 / 천마총).
