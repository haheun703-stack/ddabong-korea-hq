# HISTORY_ACCURACY_STANDARD — 역사 정확성 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §0 §9
> **승인 전까지 정본 §0 §9 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `fact`, `source`, `shot`

---

## 등급 (모든 주장·시각 디테일에 필수)
| 등급 | 정의 | 예 |
|---|---|---|
| `FACT` | 강한 증거로 확인되는 존재·연대 | 천마총 발굴 1973 |
| `PROBABLE` | 비교 증거 기반 개연성 있는 재료·색 | 복식 재질·색 |
| `INTERPRETIVE` | 기록 없는 군중 규모·정확한 배치 | 의례 참석 인원 |
| `ARTISTIC` | 새벽 안개·극적 광선 등 연출 | 조명·날씨 |

## 규칙
1. 기록에 없는 내면 생각을 사실적 인용이나 확신으로 제시하지 않는다. `INTERPRETIVE` 이상은 "might have / may have / it is possible that" 로 표현 (`fact.hedge_required = true`).
2. 역사 AI 장면은 `AI Visual Reconstruction` 라벨. 강한 해석 장면은 `INTERPRETIVE RECONSTRUCTION` 고려. 현재 시점 사진 기반 재구성(파이프라인 A)은 `AI Visual Reconstruction (present-day, photo-based)` (D-035 #2).
3. 증거 순서: 실제 자료 → 복원 → 영화적 창작 (Evidence Before Imagination).
4. 근거 없는 건축을 사실로 제시하지 않는다. 모든 시대에 조선 양식을 쓰지 않는다.
5. 대본 블록·샷·인물·복식·장소 모두 등급 필드를 가진다.

## FACT → CONTEXT → INTERPRETATION (D-003)
사실 / 당시 조건 / 근거 기반 해석을 화면·내레이션에서 구분한다 (EP01 그래픽 명세의 FACT/CONTEXT/INTERPRETATION 카드가 선례).

---

## 미결 (사용자 결정 필요)

- Historical QA 통과 기준 점수(썸네일·리텐션과 별개) 확정
