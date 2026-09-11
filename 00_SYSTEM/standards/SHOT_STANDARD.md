# SHOT_STANDARD — 샷 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §4 §12 §13
> **승인 전까지 정본 §4 §12 §13 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `shot`, `scene`, `approval`, `keep_change_patch`

---

## SHOT = 최소 운영 단위
ID `EP<NN|NNN>_S<NN>_SH<NNN>`. 필수 메타: 등급, 인물/복식 ID, 카메라 데이터(JSON), 파이프라인, 상태, 버전 이력. → `shot.schema.json`

## 점수 (0–100)
`camera_complexity` · `spatial_accuracy` · `human_motion` · `visual_importance` — 라우터 입력.

## 버전 (덮어쓰기 금지)
```
SHOT_014: PREVIZ_V01 → V02 → V03 ★APPROVED / LOOK_V01 → V02 ★APPROVED / VIDEO_V01 → V02 → V03 ★FINAL
```
롤백 항상 가능. `version_history[]` 누적.

## 리뷰 UI (§13)
Desktop: `[V01][V02][V03][V04]` · ⭐ APPROVE / 🔄 FIX / ❌ REJECT
Fix reason: `CAMERA` `ARCHITECTURE` `COSTUME` `LIGHTING` `MOTION` `CHARACTER_IDENTITY` `HISTORICAL_ISSUE` `AI_ARTIFACT` `OTHER`
Mobile: PLAY · 👍 · 🔄 · ❌ (의도적으로 단순).

---

## 미결 (사용자 결정 필요)

- 리뷰 UI 구현 방식 (P5): Web HQ 정적 페이지 + JSON vs 별도 앱
