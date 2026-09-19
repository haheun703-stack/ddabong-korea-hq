# NARRATION_STANDARD — 내레이션 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §16
> **승인 전까지 정본 §16 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `voice`

---

- 리듬: `QUESTION → DISCOVERY → EVIDENCE → MEANING`
- 내레이터 얼굴: 기본 0%. 고정 내레이터 보이스 필수 (`VOICE_NARRATOR_MAIN_V01`).
- 역사 인물 대사: 정당하고 유용할 때만.
- 해석 표현: "might have / may have" (HISTORY_ACCURACY §1).
- EP01 선례: `episodes/ep01-production-script-v2.md` 문장 단위 + 화면 태그 `[REAL] [MUSEUM] [ARCHIVE] [GRAPHIC] [HIGGSFIELD]`.

## 속도 (DRAFT, 2026-09-19 · P-014-A · 근거 `09_ANALYTICS/benchmarks/WORKFLOW_MASTERPROMPT_FLOW_20260919.md` §3-A)

- 영어 내레이션 **120–140 wpm**, 10초당 **20–23 단어**. 대본 단계에서 섹션마다 `[XX 단어 / 예상 XX초]` 를 표기하고, 녹음 뒤 실측 초와 대조한다.
- 검증: EP01 Grady 9섹션 wav 실측 평균 129 wpm (섹션별 108–150), 총 6:02. 규칙은 이 실측에서 나왔다.
- 한국어판을 만들 경우 **7자/초 (10초당 공백 제외 70자)** — 벤치마크 워크플로의 한글 규칙, 미검증.
- 150 wpm 을 넘는 섹션은 정보 밀도 과다 신호 → 문장을 자르거나 화면에 숫자를 넘긴다 (③ FACT 단계는 화면 숫자로 덜어낼 수 있다).

## 대본 형식 (DRAFT, 2026-09-19 · P-014-C)

- 한 줄 = 한 호흡. 줄 머리에 **`[m:ss]` 타임스탬프** + 화면 태그 + 문장. 예: `[0:14] [GRAPHIC] Forty-seven metres across.`
- 타임스탬프는 누적 초 (섹션 경계에서 리셋하지 않는다). 러프컷 조립 스크립트가 이 줄을 그대로 타임라인 입력으로 읽는다 — 대본이 곧 편집 큐시트.
- 타임스탬프는 wpm 규칙으로 예측해 쓰고, 녹음 뒤 실측으로 갱신한다 (예측 → 실측 두 벌을 남긴다).
- EP01 은 이미 녹음이 끝났으므로 소급 적용하지 않는다. EP02 부터.

---

## 미결 (사용자 결정 필요)

- 내레이터 보이스 공급자/샘플 확정
