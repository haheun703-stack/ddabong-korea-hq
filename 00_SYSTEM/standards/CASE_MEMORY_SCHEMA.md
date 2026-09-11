# CASE_MEMORY_SCHEMA — 사례 메모리 스키마 설명

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §18 · 아스트라 §5 수정 사례
> **승인 전까지 정본 §18 · 아스트라 §5 수정 사례 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `case_memory`

---

## 필드 (`case_memory.schema.json`)
| 필드 | 뜻 |
|---|---|
| `case_id` | `CASE_<TOPIC>_<NNN>` (예: `CASE_DDABONG_CHAR_001`) |
| `channel_id` | 채널 |
| `task_context` | 작업 상황 (단계·대상) |
| `ai_draft` / `user_result` | AI 초안 / 사용자 수정·선택 결과 (요약 또는 경로) |
| `options_tested[]` | 제시된 선택지 |
| `reason` | 사용자가 밝힌 이유·가설 |
| `scope` / `exceptions[]` | **적용 범위와 예외** — 전역 규칙화 방지 |
| `edit_time_min` | 수정 소요 시간 (미확인 null) |
| `standard_versions` | 당시 표준 버전 |
| `status` | ACTIVE / SUPERSEDED / RETIRED |

## 저장 시점
사람이 AI 결과를 수정·선택할 때마다 (정본 §24-9). 짧은 명령 `사례 저장`.

## 첫 사례
`schemas/examples/case_memory_TEMPLATE.json` = CASE-DDABONG-CHAR-001 (실제 결정 D-004).

---

## 미결 (사용자 결정 필요)

- 없음
