# STORY_ENGINE_STANDARD — 스토리 엔진 7단계

> 문서 버전 **v0.1 ACTIVE** (2026-09-14, Claude Code · **ACTIVE 승격 D-035 #8**, 전체 검수 D-029 통과) · 근거: `concept-bible.md` §Story engine (6단계) + D-033 (벤치마크 반영, 사용자 승인 2026-09-14)
> 이 문서가 `concept-bible.md` 6단계보다 우선한다 (D-035). ② 는 EP02 부터 (D-034 #1).
> 관련 표준: `NARRATION_STANDARD.md` (리듬 QUESTION → DISCOVERY → EVIDENCE → MEANING 은 이 7단계의 축약형) · `HISTORY_ACCURACY_STANDARD.md` (FACT / INTERPRETATION) · `SHOT_STANDARD.md`
> 샘플 대입: `02_SEASONS/S01/EP01/03_STORY/STORY_ENGINE_EP01.md`

---

## 1. 원칙

- 채널 질문은 하나다: **Why is Korea like this?** 매 에피소드는 "무슨 일이 있었나"가 아니라 "왜 그들에게 그 선택이 말이 됐나"에 답한다.
- 7단계는 순서가 정보다. 단계 번호를 대본에 표기한다 (`[STEP 2]`). 주제에 안 맞는 단계는 **생략 가능하되 생략 사유를 적는다** (② 와 ⑤ 는 생략 불가). **적용 범위: EP02 부터 (D-034 #1). EP01 은 대본 v2 · 러프컷 v1 유지, ② 면제.**
- 한 줄 주제 (`one_line_thesis`) 를 대본 머리에 먼저 쓴다. ⑦ 은 반드시 그 한 줄로 닫는다.

## 2. 7단계

| # | 단계 | 역할 | 주로 쓰는 화면 (SHOT pipeline) | 근거 표시 | 길이 가이드 (7분 기준) |
|---|---|---|---|---|---|
| ① | **QUESTION** | 외국인이 처음 떠올릴 질문. 현재 시점에서 시작. **콜드오픈: 첫 컷 3–8초가 0:00, 브랜드 인트로는 그 뒤 (D-046)** | `AI_STILL`(사진→AI 재구성) · `REAL_SHOOT` · `ORIGINAL_GRAPHIC`(질문 카드) | 없음 | 15–35초 |
| ② | **REJECTED OBVIOUS ANSWER** (상식 처방 기각) | 시청자가 떠올릴 뻔한 답 1–3개를 FACT 로 먼저 기각. 질문을 더 세게 남긴다 | `ORIGINAL_GRAPHIC`(도해 GT-04 "틀린 답 X") · `ARCHIVE` | 기각 근거 = FACT 등급 fact_id 필수 | 20–45초 |
| ③ | **FACT** | 기록·유물·발굴로 확인되는 사실. 숫자·치수를 화면에 | `ORIGINAL_GRAPHIC`(GT-01 단면 · GT-03 치수) · `ARCHIVE` · `BLENDER_FLOW` | 출처 라벨 필수 (SOURCE_STANDARD) | 60–90초 |
| ④ | **CONTEXT** | 당시 사회·종교·환경·기술·권력 | `ORIGINAL_GRAPHIC`(GT-02 오버헤드) · `AI_STILL` | FACT / PROBABLE 구분 | 45–75초 |
| ⑤ | **MINDSET** | 그 조건에서 사람들이 세상을 봤을 법한 방식 | **AI 인물 재현** (`BLENDER_FLOW` · `FLOW_VEO` · `AI_STILL` · `HIGGSFIELD` — EP01 은 HIGGSFIELD 0, D-024) 5–6초 컷 | `ai_label` = `AI Visual Reconstruction` + `INTERPRETIVE RECONSTRUCTION`, hedge 화법 (might / may have) | 45–75초 |
| ⑥ | **CHOICE** | 그래서 어떤 선택·행동으로 이어졌나 | AI 인물 재현 + `ORIGINAL_GRAPHIC`(과정 도해) | 해석 라벨 유지 | 45–75초 |
| ⑦ | **LEGACY** | 오늘의 한국과 연결. ① 의 구도가 다시 나온다 | `REAL_SHOOT` · `AI_STILL`(사진→AI) · 매치컷 | 한 줄 주제로 닫기 | 30–60초 |

AI 인물 재현은 전체 길이의 **10% 안팎** (D-033 #3). ②③④ 가 벤치마크에서 배운 부분이고, ⑤⑥ 이 우리만 있는 부분이다.

## 3. 대본 머리 필수 항목

```
one_line_thesis:   한 줄 주제 (⑦ 에서 그대로 되풀이)
obvious_answers:   ② 에서 기각할 상식 답 1–3개 + 각 기각 근거 fact_id
numbers_on_screen: ③ 에서 화면에 올릴 숫자·치수 (fact_id 와 함께)
people_moments:    ⑤⑥ 인물 컷 목록 (shot_id, 5–6초, ai_label)
```

## 4. 검수 (QA_STANDARD 연동)

- ② 가 없으면 **FAIL** (대본 검수, EP02 부터). ⑤ 가 없으면 FAIL.
- ② 의 기각 근거가 FACT 등급이 아니면 FAIL (INTERPRETIVE 로 상식을 기각하지 않는다).
- ⑦ 마지막 문장이 `one_line_thesis` 와 다르면 WARN.
- 외국인 시청자 전제: 고유명사(삼국사기·실록·적석목곽) 첫 등장 시 한 구절 설명 없으면 WARN.

## 5. 벤치마크에서 가져온 것 · 버린 것 (D-033 #5)

가져옴: 상식 처방 기각(②) · 한 줄 주제로 긴 시간 꿰기 · 숫자·치수 화면 표시(③).
버림: 공학 설명서 톤(도해는 ③④ 에만) · 사람 없는 화면(⑤⑥ 필수) · 국내 시청자 전제 · 근거와 해석을 같은 톤으로 말하기.

## 미결 (사용자 결정 필요)

- ② 의 영문 단계명 확정 (`REJECTED OBVIOUS ANSWER` vs `NOT THAT SIMPLE`).
- 길이 가이드가 7분 기준인데 쇼츠(17_SHORTS)용 축약형 필요 여부.
