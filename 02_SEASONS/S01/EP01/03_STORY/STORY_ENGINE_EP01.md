# EP01 스토리 엔진 대입 — 「경주 왕릉 / 천마총」 (샘플, 2026-09-14)

> 작성: Claude Code · `STORY_ENGINE_STANDARD.md` v0.1 을 `episodes/ep01-production-script-v2.md` (2026-08-16, APPROVED) 에 대입한 결과. **대본을 고치지 않았다.** 빈 칸·어긋남을 보고만 한다.
> 샷 ID 는 `07_SHOTS/shot_EP01_*.json` (49샷, 러프컷 v1 TC).

## 대본 머리 (제안)

```
one_line_thesis:   "They did not bury the dead to hide them. They buried them to keep the living in order."
                    (죽은 자를 숨기려 묻은 게 아니라, 산 자의 질서를 지키려 묻었다)
obvious_answers:   (현재 대본에 없음 — 아래 ② 참조)
numbers_on_screen: 지름 47 m · 높이 12.7 m · 목곽 6.6×4.2 m · 1973년 · 유물 11,000점+ · 155호분  (CLM_CHEONMACHONG_LAYOUT_001 · CLM_EP01_STRUCT_004 · S3)
people_moments:    S04 H01–H04 (노동자 4컷) · S06 H05 (원로) · S07 (시종)  — 현재 AI 8샷 45초 ≈ 11%
```

## 7단계 대입

| # | 단계 | 대본 v2 구간 | 샷 | 판정 |
|---|---|---|---|---|
| ① | QUESTION | 0:00–0:35 COLD OPEN "why would a society give this much…" | S01_SH001–SH004 (REAL 2 · GRAPHIC 2) | **있음.** 현재 시점·외국인 시선 OK |
| ② | REJECTED OBVIOUS ANSWER | **없음** | — | **빈 칸.** 후보: (a) "왕이 많아서?" → 신라 왕 56명 vs 경주 봉분 수백 기 (FACT 필요, 새 fact_id) (b) "땅이 남아서?" → 왕궁(월성) 바로 옆 도심 (S1) (c) "그냥 큰 무덤?" → 안에 목곽·강돌·유물 11,000점 (S3). 20–40초 추가 → 전체 7:05 → 약 7:35, 러프컷 재조정 필요 |
| ③ | FACT | 0:35–2:15 (WHAT IS HERE + CHEONMACHONG) | S02–S03, G03·G04·G06 | **있음.** 숫자는 내레이션에만 있고 화면 치수선 없음 → GT-03 적용 대상 (G04 단면에 47 m / 12.7 m 치수 추가 검토) |
| ④ | CONTEXT | 2:15–3:15 (HOW BUILT) + 3:15–4:20 (GOLD) | S04 G05 · S05 G07 | **있음.** 박물관 해석 인용 형태 유지 |
| ⑤ | MINDSET | 4:20–5:20 MINDSET RECONSTRUCTION | S06 H05 원로 + G08 방법 카드 | **있음.** 라벨·hedge 규칙 이미 적용 |
| ⑥ | CHOICE | 2:15–3:15 의 H01–H04 (노동) 가 사실상 CHOICE 화면 | S04 H01–H04 | **있으나 순서 역전.** 대본은 CHOICE(노동) 를 MINDSET 앞에 둠. 러프컷 v1 순서 유지 (D-010) 하되 내레이션으로 "그래서" 연결을 보강 |
| ⑦ | LEGACY | 5:20–7:05 (THEN/NOW 매치컷 · 오프닝 구도 재등장 · 엔드) | S08 G10 · S09_SH003 | **있음.** 마지막 문장을 `one_line_thesis` 로 맞추는지 확인 필요 |

## 결론

- 7단계 중 **6개 충족, ② 만 빈 칸.** ② 를 넣으면 약 30초 늘어난다. 넣을지, 넣으면 어디를 줄일지는 사용자 결정 (러프컷 v1 은 D-010 기준).
- ③ 의 숫자를 화면에 올리는 것(GT-03)은 대본 변경 없이 그래픽 스펙 v2 에서 처리 가능.
- 이 파일은 샘플이다. 대본 v3 로 갈지 여부는 별도 결정.
