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

## HERITAGE_INSERT — 유적 3D 구조 인서트 (D-058, 2026-09-19)

- **정의**: 사람 0 의 3D 테크니컬 컷어웨이로 유적·지정문화재의 구조를 설명하는 인서트. `pipeline = HERITAGE_INSERT`.
- **길이**: 인서트 1개 15–25초 = 6–10초 컷 2–3개. **AI 영상 컷당 ≤10초** (BIBLE §74 예외, 사람 없는 구조물에 한함). 편당 2–3개, 러닝타임 10–15%.
- **위치**: 7단계 중 ③ FACT · ④ CONTEXT. ⑤⑥ (인물 재현) 에는 쓰지 않는다.
- **룩**: `DDABONG_TECH_INFOGRAPHIC_V01` (두 번째 룩 락). 사극 실사 룩과 한 편 안에서 공존하되 인서트 경계에서 전환한다.
- **제작**: Blender `--passes tech` (Freestyle 구조선 + 무채색 오버라이드) → `gemini_omni_flash_1_1` i2v (또는 `seedance_2_5` omni_reference) → 편집 오버레이 라벨 (영문 + 한자/국문 1줄). 입력 플레이트에 **비례 단서 필수** (1.7 m 인물 실루엣 또는 치수 바). 지면·단면 평면은 Freestyle 제외.
- **형상 출처**: 국가유산청·국립중앙박물관 공공누리 1유형 3D 스캔 우선 (FACT). 스캔 없는 소실 건물은 `INTERPRETIVE` + "추정 복원" 자막.
- **고지**: 업로드 시 변형·합성 자기 공개. 편마다 카메라 경로·강조 대상을 바꾼다 (유튜브 2026-07-16 비진정성 기준).
- **검수**: 12프레임 시트 + 층 순서 FACT 대조 + 비례 대조 (치수선 기준). 글자 0 · 사람 0 확인.
- 근거: `09_ANALYTICS/benchmarks/HERITAGE_INSERT_SURVEY_AND_PLAN_20260919.md` · 시험 `08_GENERATION_CACHE/EP01/HERITAGE_INSERT/REVIEW_INSERT_G04_OMNI_V01_20260919.md`.

## 미결 (사용자 결정 필요)

- 리뷰 UI 구현 방식 (P5): Web HQ 정적 페이지 + JSON vs 별도 앱
