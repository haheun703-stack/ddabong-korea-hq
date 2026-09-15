# TITLE_STANDARD — 제목 · 썸네일 문구 · 훅 3곳 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-15, Claude Code) · 출처: `THUMBNAIL_STANDARD.md` §QA · `HISTORY_ACCURACY_STANDARD.md` 규칙 · 자료집 역할 4 카피라이팅 · 5 광고소재(썸네일문구)
> **승인 전까지 정본이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `episode`, `analytics`
> 근거: D-046 (2026-09-15, "AI 마케팅팀 7명" 자료집 적용 — `AI 비서/` 캡처 9장, 구조 연구용)

---

## 1. 제목 (자료집: 헤드라인)
- 후보 **5안** 을 `<EP>/04_TITLE_THUMB/TITLE_CANDIDATES_<EP>.md` 에 쓰고, 각 안에 **주장 → fact_id** 를 붙인다.
- 허용 형식: (a) **질문형** (`channel.json.core_questions` 의 질문 그대로 또는 축약) (b) **FACT 등급 주장** (`fact.confidence = FACT` 인 `fact_id` 근거).
- 금지: INTERPRETIVE 근거로 단정하는 제목 · 낚시어 (SHOCKING · SECRET · "historians hate" · "you won't believe") · 화면 숫자(`numbers_on_screen`)와 다른 숫자 · 특정 왕 이름으로 피장자 단정 (`CLM_EP01_OCCUPANT_006`).
- 길이: 영어 **≤ 60자** (모바일 2줄). 고유명사는 1개까지, 첫 등장 고유명사는 설명어와 함께 ("Silla" → "ancient Korea's Silla").
- 확정 제목 = `16_PUBLISH/PUBLISH_META_<EP>.md` 의 `title_final`. `episode.json.working_title_en` 은 작업명으로 유지.
- 실험: 2안까지 `EXPERIMENT_STANDARD.md` 규칙으로 교체 가능.

## 2. 썸네일 문구 (자료집: 썸네일문구 · 소재각도)
- **≤ 3 단어**, 대문자, 제목과 같은 정보 반복 금지 (THUMBNAIL_STANDARD QA).
- 소재각도 = 컴포저 5재료 중 앞세울 것 1개: `SCALE` (크기) · `MYSTERY` (안에 뭐가) · `CONTRAST` (과거/현재). 문구는 그 각도 하나만 말한다.
- 후보 3안 → `THUMB_TEXT_<EP>.md`. 문구 없음도 하나의 안.

## 3. 훅 3곳 (자료집: 후킹문구 · 반전훅)
| 곳 | 규칙 |
|---|---|
| 콜드오픈 0:00–3초 | ① QUESTION 의 첫 컷 (질문 카드 또는 현재 장소 리빌). 브랜드 인트로는 그 **뒤** (D-046, `BRAND_INTRO_STANDARD.md`) |
| 설명란 첫 줄 | 접히기 전 1줄 = ① 의 질문 한 문장. CTA 금지 |
| 고정 댓글 첫 줄 | 시청자에게 되묻는 질문 1개 (`cta_policy.pinned_comment_cta`) |
| 쇼츠 첫 프레임 | 텍스트 온 이미지 ≤ 6 단어, 본편 질문의 축약 (`SHORTS_STANDARD.md`) |

## 4. 랜딩카피 (자료집: 랜딩카피)
채널 About = `channel.json.promise` 1줄 + `differentiators` 3줄 + 업로드 주기. `01_CHANNEL/CHANNEL_ABOUT.md` (게시 전 작성).

## 5. QA
`QA_STANDARD.md` HISTORY QA 에 "제목 주장 → fact_id" 검사 1줄 (D-046). 낚시어 목록은 이 문서 §1 이 정본.

---

## 미결 (사용자 결정 필요)

- EP01 제목 5안 중 실험용 2안 선택 · 썸네일 문구 3안 중 선택 (없음 / ≤3단어 / 숫자형).
- 광고카피·세일즈카피는 판매 결정(P-013) 뒤.
