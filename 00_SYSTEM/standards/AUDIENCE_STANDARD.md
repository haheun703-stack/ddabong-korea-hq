# AUDIENCE_STANDARD — 시청자 기준 (페르소나 · 니즈맵 · 질문수집)

> 문서 버전 **v0.1 DRAFT** (2026-09-15, Claude Code) · 출처: `MASTER_CHANNEL_BIBLE.md` §1 §6 · `STORY_ENGINE_STANDARD.md` ①② · 자료집 역할 1 시장조사
> **승인 전까지 정본이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `channel`, `analytics`
> 근거: D-046 (2026-09-15, "AI 마케팅팀 7명" 자료집 적용 — `AI 비서/` 캡처 9장, 구조 연구용)

---

## 1. 인스턴스
`01_CHANNEL/channel.json` (`channel.schema.json`). 페르소나·핵심 질문·니즈맵·채널 약속은 여기 한 곳에만 둔다. 제목·설명란·쇼츠·커뮤니티 문구는 전부 이 파일을 기준으로 쓴다.

## 2. 페르소나 (자료집: 페르소나)
- PRIMARY 1 · SECONDARY 1 이상. 필드: 나이대 · 지역 · 한국 지식 수준 · 진입 경로 · 원하는 것 · 오해 · 불편 · 보는 채널.
- 주 타깃 = `PERSONA_KOREA_CURIOUS_EN_01` (영어권 25–44, 한국사 지식 0, K-드라마·여행 경로) — 사용자 결정 2026-09-15.
- 규칙: 대본·제목이 PRIMARY 의 `misconceptions` 중 하나를 건드리면 ② REJECTED OBVIOUS ANSWER 후보로 기록한다 (EP02 부터, D-034 #1).

## 3. 고객문제 = 핵심 질문 (자료집: 고객문제)
`audience.core_questions[]` = 외국인이 실제로 묻는 질문. 각 에피소드의 ① QUESTION 은 이 목록의 한 항목이거나 새 항목을 추가한다. 목록에 없는 질문으로 에피소드를 시작하면 WARN (Strategy Agent).

## 4. 니즈맵 (자료집: 니즈맵)
`audience.needs_map[]` = 욕구 → 우리가 답하는 장치 → 적용 에피소드. 새 표준·파이프라인이 생기면 어느 니즈에 답하는지 한 줄 추가한다.

## 5. 질문수집 (자료집: 질문수집 · 태그분류 · 고객관리)
- 저장소: `01_CHANNEL/QUESTION_BANK.md` (채널 단위) · `02_SEASONS/<S>/<EP>/18_ANALYTICS/COMMENTS_<EP>_<YYYYMMDD>.md` (에피소드 수확본).
- 수확 시점: 게시 D+1 · D+7 · D+28 (= `cadence.measure_days`). 담당 Analytics Agent (수확) → Strategy Agent (분류·로드맵 반영).
- 태그 5종: `QUESTION` · `CORRECTION` · `PRAISE` · `REQUEST` · `SPAM`. `QUESTION`·`REQUEST` 는 `CONTENT_ROADMAP.md` 후보 입력, `CORRECTION` 은 Fact Check Agent 로.
- 기록 범위: 공개 핸들 · 댓글 원문 · 날짜만. 개인정보·DM 내용 기록 금지. 게시 전에는 Reddit / Quora / YouTube 댓글(타 채널) 검색으로 씨앗 10개.
- 봇은 답글 **초안**만 쓴다. 게시는 사용자 (`cta_policy.bot_may_post = false`).

## 6. 경쟁사분석
→ `BENCHMARK_STANDARD.md`.

---

## 미결 (사용자 결정 필요)

- 페르소나 (b) 를 SECONDARY 로 유지할지 삭제할지 (3편 뒤 `top_countries`·댓글로 판단).
- `question.schema.json` 신설 여부 (3편 넘어 QUESTION_BANK 가 md 로 관리하기 어려워지면).
