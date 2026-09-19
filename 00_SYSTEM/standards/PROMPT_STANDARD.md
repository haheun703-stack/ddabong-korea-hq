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

## 부록 A — 화면 내 한글·숫자 (조건부, DRAFT 2026-09-19 · P-014-D · 근거 `09_ANALYTICS/benchmarks/WORKFLOW_MASTERPROMPT_FLOW_20260919.md` §3-D)

기본은 **금지** (`VISUAL_STYLE_BIBLE` §74 화면 내 글자 · 도해 라벨은 편집 오버레이). 유일한 예외는 **썸네일** (`THUMBNAIL_STANDARD`, 예: "47 M") 처럼 글자가 이미지의 일부여야 할 때. 그 경우 프롬프트에 아래 문구를 그대로 결합한다 (벤치마크 워크플로의 "Strict 1-to-1 Mapping", 스토리보드에서 한글 3단어가 깨지지 않고 렌더된 것을 확인):

`Text (Strict 1-to-1 Mapping): displays only the following exact text, once each: 1. "[문구 1]" 2. "[문구 2, optional]". Strictly single occurrence, no duplicate boxes, no extra UI, no letter repetition, no character stuttering. Typography: clean bold sans-serif, perfectly legible.`

부정 조각 (real-CFG 를 지원하는 모델에서만): `malformed Hangul, gibberish text, stuttered characters, repeating syllables, duplicate words`.
검수는 200% 줌 글자 항목 (`QA_STANDARD` 3단 #1) 에서 한 글자씩 대조. 한 글자라도 틀리면 재생성이 아니라 편집 오버레이로 전환한다.

---

## 미결 (사용자 결정 필요)

- 부록 A 를 썸네일 외로 넓힐지 (현재 답: 넓히지 않는다).
