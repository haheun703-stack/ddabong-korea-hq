# SOURCE_STANDARD — 출처 기록 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §10 · 아스트라 §5 근거 묶음
> **승인 전까지 정본 §10 · 아스트라 §5 근거 묶음 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `source`, `fact`

---

## 최소 항목 (`source.schema.json`)
`source_id` · `claim_ids[]` · `title` · `institution_or_author` · `url_or_path` · `verified_at` · `excerpt_or_summary` · `confidence` · `uncertainty` · `source_type`

## 규칙
1. 모든 사실 주장(`fact.claim_id`)은 최소 1개 `source_id` 에 연결된다.
2. 출처 확인일과 확인자를 남긴다. 링크가 죽으면 `uncertainty` 에 기록.
3. 연구 열람 허가 ≠ 미디어 재사용 허가. 미디어를 쓰면 `rights_id` 를 별도로 만든다.
4. 출처 없이 게시 금지 (정본 §23).
5. EP01 선례: `episodes/ep01-research-verified-v2.md` 의 출처 목록을 `02_SEASONS/S01/EP01/02_SOURCES/` 인스턴스로 옮기는 것이 P1 작업.

## 출처 유형
`PRIMARY_RECORD` `EXCAVATION_REPORT` `ACADEMIC` `MUSEUM` `GOVERNMENT` `SECONDARY` `OTHER`

---

## 미결 (사용자 결정 필요)

- 없음
