# 군중 LITE 1단계 (full_body) — 사람 검수 시트

> 2026-09-13 · 승인 `APR_EP01_MP_CROWD_001` (D-020) · 2 호출 / 2 성공 · 4 credits (한도 9 중 2)

| 무리 | 파일 | 봇 판정 | 제안 |
|---|---|---|---|
| 노동자 | `MP_LABORER_FULL_BODY_V01_f5514f0f.png` | 사람·복식 OK. **삽·곡괭이가 현대 쇠 공구처럼 보임** (시대 lock 위반 소지) | 공구만 지우는 편집 1회 (`PRM_…_V03` + `PATCH_MP_LABORER_FULL_BODY_001` 저장됨) |
| 시종 | `MP_ATTENDANT_FULL_BODY_V01_30791f45.png` | 사람·색 OK. **가슴 긴 옷고름 매듭이 조선 한복처럼 보임** (복식 lock 위반) | 옷고름만 지우고 허리 천띠로 여미는 편집 1회 (`PRM_…_V03` + `PATCH_MP_ATTENDANT_FULL_BODY_001` 저장됨) |

편집은 사용자 OK 후 전송. 편집본 확인 뒤 2단계 (walking · costume_detail) 는 편집본을 복식 참조로.

## 편집 결과 (사용자 '둘다 수정', 4 credits, 승인 4/9)

| 무리 | 파일 | 결과 |
|---|---|---|
| 노동자 | `MP_LABORER_FULL_BODY_V02_412a72bc.png` | **PASS** — 공구 제거, 나머지 동일 |
| 시종 | `MP_ATTENDANT_FULL_BODY_V02_77078e12.png` | **PARTIAL** — 여자만 옷고름 제거·허리띠. 남자 2명 옷고름 남음 → 재편집 `PRM_…_V04` + `PATCH_MP_ATTENDANT_FULL_BODY_002` 저장, 사용자 OK 대기 |

남은 승인: 5 호출. 재편집 1 + 2단계 4 = 5 → 한도 딱 맞음 (추가 FIX 는 새 승인).

## 재편집 결과 (D-021, 2 credits, 승인 5/12)

`MP_ATTENDANT_FULL_BODY_V03_dc7f38ed.png` **PARTIAL** — 왼쪽 남자 옷고름 제거 성공, 여자 유지. **가운데 젊은 남자 옷고름 남음·허리띠 없음.** D-021 에 따라 편집 반복 중단 → 방법 전환 사용자 결정 대기.
