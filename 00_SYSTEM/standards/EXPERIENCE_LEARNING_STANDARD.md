# EXPERIENCE_LEARNING_STANDARD — 경험 학습 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §1-7 §18 · 아스트라 인수인계 §5–§7
> **승인 전까지 정본 §1-7 §18 · 아스트라 인수인계 §5–§7 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `case_memory`, `failure_memory`, `performance_memory`, `standard_version`, `evaluation`

---

## 원칙
프롬프트를 길게 쌓지 않는다. **사용자 판단을 구조화된 사례로 저장**한다. 제작과 시스템 개선은 분리한다.

## 4 메모리
| 메모리 | 내용 | 스키마 |
|---|---|---|
| STANDARD | 현재 승인된 채널/시스템 규칙 | `standards/*.md` + `standard_version` |
| CASE | AI 초안 + 사용자 수정/선택 + 이유 + 범위 | `case_memory` |
| FAILURE | 구체적 실패와 해결 | `failure_memory` |
| PERFORMANCE | 시간·시도·비용·승인율·CTR·유지율 | `performance_memory` |

## 학습 루프
`USER REVIEW → AI RESULT vs USER APPROVED RESULT → DIFF ANALYZER → FAILURE CLASSIFIER → CASE MEMORY → RULE CHANGE CANDIDATE → REGRESSION TEST → HUMAN APPROVAL → NEW STANDARD VERSION`

## 규칙
1. 사례 1개로 규칙을 승격하지 않는다. 이전 좋은 사례 + 미사용 사례로 검사.
2. 실행 기록은 당시 사용한 표준 버전을 가리킨다 (`generation.standard_versions`).
3. 파인튜닝은 시작점이 아니다. 승인 표준 + 관련 사례 검색 + 평가 + 회귀검사부터. 반복·측정된 사례가 충분히 쌓인 뒤 학습 고려.
4. ACTIVE 표준을 개선 실험이 덮어쓰지 않는다 (DRAFT → 평가 → ACTIVE, 이전은 PREVIOUS).

---

## 미결 (사용자 결정 필요)

- 없음
