# MODEL_ROUTER — 모델·파이프라인 라우터

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §3 provider abstraction · §7
> **승인 전까지 정본 §3 provider abstraction · §7 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `router_decision`, `generation`

---

## Agent ≠ Provider
| 에이전트 | 후보 공급자 |
|---|---|
| Research Agent | Gemini / OpenAI / 기타 |
| Script Agent | Claude / OpenAI / 기타 |
| Image/Video Generation | Flow / Veo / Higgsfield |
| Music Director | Suno / 라이선스 라이브러리 / 기타 |
OS 는 공급자 교체에도 살아남아야 한다.

## Visual Router 기본 규칙 (§7)
| 조건 | 파이프라인 |
|---|---|
| 현재 장소 | `REAL_SHOOT` |
| 역사 사진·문서·유물 | `ARCHIVE` |
| 저모션 + 고사실밀도 | `AI_STILL` / `ORIGINAL_GRAPHIC` |
| 고공간정확도 + 고카메라복잡도 | `BLENDER_FLOW` |
| 초고카메라복잡도 + 중간 공간 의존 | `HIGGSFIELD` |
| 인물 연속성 critical | MASTER FRAME + reference-driven video |

## 출력 필수 (`router_decision.schema.json`)
`recommended_pipeline` · `reason` · `historical_confidence` · `continuity_risk` · `expected_cost_range` · `expected_attempts`

---

## 미결 (사용자 결정 필요)

- 각 공급자별 어댑터(P6) 우선순위와 계정/크레딧 현황
