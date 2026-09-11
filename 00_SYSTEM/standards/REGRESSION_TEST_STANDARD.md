# REGRESSION_TEST_STANDARD — 회귀 검사 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §1-7 §18
> **승인 전까지 정본 §1-7 §18 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `evaluation`, `standard_version`

---

## 언제
규칙 변경 후보(`case_memory.rule_change_candidate_id`)를 표준에 반영하기 전 반드시.

## 방법
1. 변경안을 DRAFT `standard_version` 으로 만든다.
2. 검사 세트: **이전 좋은 사례** (ACTIVE 표준으로 승인된 결과) + **미사용 사례** (변경안 도출에 쓰이지 않은 것).
3. 변경안 적용 결과를 `evaluation` 으로 기록: 항목별 점수·근거, 중대 결함, `regression_passed`.
4. 이전 좋은 사례가 나빠지면 실패. 사례 1개만 좋아진 것은 승격 근거가 아니다.
5. 통과 + 사람 승인 → ACTIVE, 이전 ACTIVE → PREVIOUS. `DECISIONS.md` D-번호.

## 산출 위치
`09_ANALYTICS/regression/` 또는 해당 에피소드 `15_QA/`.

---

## 미결 (사용자 결정 필요)

- 최소 검사 세트 크기
