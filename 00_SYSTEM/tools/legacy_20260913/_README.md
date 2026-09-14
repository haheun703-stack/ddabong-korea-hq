# 2026-09-11 ~ 2026-09-13 일회성 데이터 갱신 스크립트 (보관용)

2026-09-14 전체 검수(D-029 반박 검수 A-24)로 `00_SYSTEM/tools/` 에서 이동. 각 스크립트는 특정 결정(D-017 ~ D-032)이나 검수 수정을 **한 번** 반영한 것이며 결과는 이미 저장소에 들어 있다.

**재실행 금지.** 이유:
- 모두 `Path(__file__).resolve().parents[2]` 로 저장소 루트를 잡는다 → 이 폴더(한 단계 깊음)에서는 루트가 `00_SYSTEM/` 이 되어 경로가 깨진다 (의도된 안전장치).
- `*_record.py` 는 generation/approval/prompt JSON 을 무조건 다시 쓰고 `spent_by_provider` 를 당시 절대값(예: 24.12)으로 덮어쓴다 → 현재 66.12 장부가 과거로 롤백된다.
- `fix_review_20260913.py` 는 소진액을 8.12 기준으로 덮어쓴다.
- `d026_apply.py` 는 스키마 패턴을 옛 값으로 되돌린다.

현역 도구는 `00_SYSTEM/tools/photo_search.py` 하나 (조회 전용). 새 일회성 스크립트는 세션 임시 폴더에서 실행하고, 결과 요약만 `15_QA/REVIEW_FIX_*.md` 에 남긴다.

| 스크립트 | 반영한 결정 |
|---|---|
| batch2_prepare/record · d017_* · mf_* · h06_* · crowd_* | P2 Character Master · Master Frame · H06 (D-017 ~ D-031) |
| p011_router_lock.py · d026_apply.py · d027_master_frames_final.py · d028_apply.py · d031_h06_ok.py · d032_short_shoot.py | D-024 ~ D-032 |
| fix_review_20260913.py · fix_codex_review_20260913.py · d026_review_fixes.py | 2026-09-13 전체 검수 수정 |
| rights_gnm_split_20260913.py · rights_emuseum_*_20260913.py | 권리 GNM 분리 · e뮤지엄 실측 |
