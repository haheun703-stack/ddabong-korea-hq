# ANALYTICS_STANDARD — 성과 분석 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §2 §18 · 아스트라 §5 성과 기록
> **승인 전까지 정본 §2 §18 · 아스트라 §5 성과 기록 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `analytics`, `performance_memory`

---

## 스냅샷 (`analytics.schema.json`)
게시일 · 측정일 · **게시 후 경과일** · 플랫폼별 지표 · 상위 국가 · 실험 변수 · 데이터 출처. 없는 값은 `null`.

## KPI (기존 로드맵)
CTR · 30초 유지율 · 시청 시간 · 국가 분포.

## Performance Memory
스냅샷을 `performance_memory` 로 요약 → Learning Engine 입력. 제작 지표(시간·시도·비용·승인율·재작업)와 시청 지표를 함께 기록.

---

## 미결 (사용자 결정 필요)

- 측정 주기 (예: 게시 후 1/7/28일)
