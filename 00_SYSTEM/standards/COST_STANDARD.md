# COST_STANDARD — 비용·Money Gate 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §11
> **승인 전까지 정본 §11 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `cost`, `approval`, `generation`

---

## 예산
에피소드마다 생성 예산 (`episode.budget`). 미확인이면 `null` — 0 으로 쓰지 않는다.

## 경고 단계 (`cost.gate_state`)
| 소진 | 상태 |
|---|---|
| < 80% | `OPEN` |
| 80% | `WARNING_80` |
| 95% | `STRONG_WARNING_95` |
| 100% | `LOCKED_100` — 생성 잠금 |
| 예산 미확인 | `UNKNOWN_BUDGET` — 생성 잠금 |

## 유료 호출 전 제시 (Money Gate)
`shot ID` · `provider/model` · `expected attempts` · `estimated cost range` · `continuity risk` · **승인 버튼**
사람만 승인 → `approval.kind = PAID_GENERATION`. `generation.approval_id` 없는 유료 실행은 위반.

## 현재
EP01 예산 ₩40,000 확정 (D-015) → `OPEN`. 소진은 크레딧 단위 기록, KRW 환산율 미정 (P-012).

---

## 미결 (사용자 결정 필요)

- ~~P-001 EP01 예산 통화·금액~~ → D-015 ₩40,000 확정
