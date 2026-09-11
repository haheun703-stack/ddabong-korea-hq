# RIGHTS_STANDARD — 권리 기록 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §10
> **승인 전까지 정본 §10 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `rights`, `license`, `asset`

---

## 최소 항목 (`rights.schema.json`)
`rights_id` · `asset_id` · `source` · `creator` · `license` · `commercial_use` · `modification_allowed` · `attribution_required` · `expiration` · `proof` · `status`

## 상태
| 상태 | 뜻 | 게시 |
|---|---|---|
| `GREEN` | 상업 사용·수정 가능 확인 | 가능 |
| `YELLOW` | 조건부 (출처표시 등) — 조건을 `attribution_text` 에 | 조건 충족 시 |
| `RED` | 불가 | **금지** |
| `BLUE` | 확인 중 | **금지** |

## 규칙
1. 모든 외부 시각/음향 자산은 `rights_id` 필수.
2. `research_permission` 과 `media_reuse_permission` 은 별개 필드.
3. 미해결 권리(RED/BLUE)로 게시 금지 (정본 §23).
4. 자주 쓰는 라이선스는 `license.schema.json` 프리셋 (예: `LIC_KOGL_TYPE1`).

---

## 미결 (사용자 결정 필요)

- NRICH·국립박물관 자료의 기본 라이선스 프리셋 확정
