# QA_STANDARD — QA 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §2 §13 §17
> **승인 전까지 정본 §2 §13 §17 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `evaluation`, `failure_memory`, `rights`

---

## 게이트 순서 (§2)
`HISTORY QA → VISUAL QA → RETENTION QA → RIGHTS QA → FINAL APPROVAL`. 공급자가 빠르다고 게이트를 건너뛰지 않는다.

## Historical QA
등급·출처 연결·hedge 표현·AI 라벨 확인. → `HISTORY_ACCURACY_STANDARD.md`
제목·썸네일 문구의 주장 → `fact_id` (FACT 등급) 또는 질문형인지 확인 (D-046, `TITLE_STANDARD.md`).

## Visual QA
Fix reason 분류 (§13). 실패는 `failure_memory` 로. 연속성 위반(얼굴 변경·복식 드리프트)은 KEEP/CHANGE.

## Retention QA (§17)
노출 위험 플래그: 시각 변화 없는 긴 설명 · 새 장소/오브젝트/리빌 없음 · 반복 내레이션 · 낮은 오디오 변화.
개입: archive insert · map/graphic · TIME-MATCH · question reset · audio change · object reveal.

## Rights QA
모든 외부 자산 GREEN/YELLOW. → `RIGHTS_STANDARD.md`

## 평가 기록
`evaluation.schema.json` — 항목별 점수·근거·중대 결함·채택.

---

## 미결 (사용자 결정 필요)

- 평가 배점 (아스트라 제안 30/25/20/15/10) 확정
