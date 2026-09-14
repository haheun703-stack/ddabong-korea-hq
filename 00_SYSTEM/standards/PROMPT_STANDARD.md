# PROMPT_STANDARD — 프롬프트 조립 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §8
> **승인 전까지 정본 §8 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `prompt`

---

## 조립식
`GLOBAL LOCK + ERA LOCK + LOCATION LOCK + CHARACTER/COSTUME LOCK + STYLE LOCK + CAMERA DATA + SHOT DELTA`
매번 처음부터 쓰지 않는다. → `prompt.schema.json`

## LOCK ID 예
`DDABONG_GLOBAL_V01` · `SILLA_EARLY_V01` · `GYEONGJU_BURIAL_V01` · `SILLA_COSTUME_OFFICIAL_V01` · `DDABONG_DOC_REENACTMENT_V01` · `CAMERA_S004_V02` · `SHOT_ACTION_V01`

## 저장
LOCK 조각은 `06_PROMPT_LIBRARY/locks/`, 조립 결과는 `assembled/` 에 `assembled_text` 포함 저장 (재현 가능).

## 수정
한 요소 실패 → `keep_change_patch` → `parent_prompt_id` 를 가진 새 `V<NN>`.

## 기존 EP01 프롬프트
`episodes/ep01-higgsfield-prompts.html` 7컷 + 공통 금지요소는 APPROVED. P1 에서 LOCK 조각으로 분해하되 내용은 바꾸지 않는다. (완료: `locks/` 11개 APPROVED, D-015)

---

## 미결 (사용자 결정 필요)

- 없음
