# 군중 LITE 2단계 (walking · costume_detail) — 사람 검수 시트

> 2026-09-13 · 승인 `APR_EP01_MP_CROWD_001` (D-022) · 4 호출 / 4 성공 · 8 credits (한도 12 중 10 사용)
> 참조 = 승인된 full_body (노동자 412a72bc · 시종 84c0fdbc). 전송 = 저장 문장 그대로 (D-016).

| 무리·슬롯 | 파일 | 봇 판정 | 사람 검수 |
|---|---|---|---|
| laborer walking | `MP_LABORER_WALKING_V01_2740544f.png` | PASS - three labourers walking toward camera (more frontal than side-front), middle man carries a river stone, cloth headbands, shin wraps, straw sandals/bare feet, same hemp jackets and cords, finished mounds behind. | ☐ APPROVE ☐ FIX |
| laborer costume_detail | `MP_LABORER_COSTUME_DETAIL_V01_06b95492.png` | PASS - chest-to-waist, collars right over left, cloth waist cords, sleeve ends and rough hands, coarse weave and dust; lower faces (mouth/beard) in frame. | ☐ APPROVE ☐ FIX |
| attendant walking | `MP_ATTENDANT_WALKING_V01_083c45d4.png` | PASS - side-front walking, man carries a plain wooden box, belted jackets with plain chest fronts (no ribbon ties), woman in long grey skirt and cloth shoes, straw sandals. | ☐ APPROVE ☐ FIX |
| attendant costume_detail | `MP_ATTENDANT_COSTUME_DETAIL_V01_d2a6b5ce.png` | PASS - plain chest fronts wrapping right over left, cloth waist belts, sleeve ends, wrists and hands clear; small inner tie knot beside each belt (not a chest ribbon). Fabric reads clean and new rather than hand-woven - minor. | ☐ APPROVE ☐ FIX |

## 사람이 볼 점

1. 참조 그림의 **얼굴이 그대로 따라옴** (문장은 '다른 사람'). 군중 LITE 는 복식 기준이라 허용 판단, 단 영상에서 이 3인조를 여러 컷에 알아볼 정도로 반복하지 않기.
2. 노동자 걷기는 옆-앞보다 정면에 가깝다.
3. 시종 옷감이 손으로 짠 삼베보다 깨끗한 새 리넨처럼 보인다 — 허용 범위인지.

모두 APPROVE 면 노동자·시종 LITE Pack 3/3 → 두 무리 CHARACTER_MASTER_APPROVED → **P2 Character Master 완료**.
