# EXPERIMENT_STANDARD — 제목·썸네일 실험 기준 (A/B · 소재변형)

> 문서 버전 **v0.1 DRAFT** (2026-09-15, Claude Code) · 출처: `ANALYTICS_STANDARD.md` §스냅샷 '실험 변수' · `THUMBNAIL_STANDARD.md` §미결 · `EXPERIENCE_LEARNING_STANDARD.md` 규칙 · 자료집 역할 5 광고소재 (A/B테스트 · 소재변형)
> **승인 전까지 정본이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `analytics` (`experiment`)
> 근거: D-046 (2026-09-15, "AI 마케팅팀 7명" 자료집 적용 — `AI 비서/` 캡처 9장, 구조 연구용)

---

## 1. 무엇을 실험하나
- **썸네일**: YouTube "Test & compare" 최대 **3종**. 차이는 **문구·크롭·각도(SCALE/MYSTERY/CONTRAST)** 만. 히어로샷은 1장 재사용 — 추가 유료 생성은 승인·Money Gate·P-012 뒤.
- **제목**: 2안. 게시 시 A, **72시간** 뒤 CTR 이 채널 기준(첫 3편은 기준 없음 → 4% 미만) 이면 B 로 교체 1회. 24시간 안 교체 금지 (노출 초기 편향).

## 2. 기록 (`analytics.experiment`)
```json
"experiment": {
  "method": "YT_TEST_COMPARE",          // YT_TEST_COMPARE | MANUAL_SWAP | NONE
  "variants": [ {"id": "A", "angle": "MYSTERY", "thumb_text": "WHAT'S INSIDE?", "title": "..."} ],
  "winner": null,                       // 변형 id 또는 null
  "decided_at": null,                   // YYYY-MM-DD
  "note": null
}
```
게시 시점에 `variants` 를 먼저 기록하고, `measure_days` (1/7/28) 스냅샷마다 `winner` 를 갱신한다.

## 3. 승격 금지
- 결과는 `performance_memory` 에만 적재한다. **3편 누적 전에는 `TITLE_STANDARD.md`·`THUMBNAIL_STANDARD.md` 를 개정하지 않는다** (EXPERIENCE_LEARNING "사례 1개로 전역 규칙 승격 금지").
- 실험 변형도 TITLE_STANDARD 의 금지어·FACT 근거 규칙을 지킨다. 낚시 변형 금지.

## 4. 담당
Thumbnail Agent (변형 제작) · Analytics Agent (기록·판정) · 사용자 (교체 승인 — 제목 교체는 게시 조작이므로 사용자 손).

---

## 미결 (사용자 결정 필요)

- CTR 기준선 (첫 3편 뒤 채널 평균으로 대체).
- Test & compare 사용 가능 여부 (채널 자격 요건) — PUBLISH_STANDARD 미결 "채널 계정" 과 같이.
