# 원로 Master Pack 배치 2 — 사람 검수 시트

> 생성 2026-09-13 · 승인 `APR_EP01_MP_ELITE_BATCH2_001` (D-018) · 7 호출 / 7 성공 · 14 credits (승인 한도 10 호출 중 7)
> 모델 Nano Banana Pro (nano_banana_2), 참조 = hero V03 + full_body V01 (둘 다 APPROVED). 전송 = 각 `PRM_…_V02` 문장 그대로 (D-016).
> 결과는 `character.master_pack.<slot>.status` 를 APPROVED / FIX 로 갱신한다. back_view 는 보조 이미지 (슬롯 아님).

| slot | 파일 | 판정(봇) | 사람 검수 |
|---|---|---|---|
| three_quarter_right | `MP_ELITE_THREE_QUARTER_RIGHT_V01_73a0605d.png` | PASS - same face, turned ~45 deg showing his right side, plain earth-toned background, costume identical. Cap reads slightly taller/rounder than hero. | ☑ APPROVE (D-019) |
| profile | `MP_ELITE_PROFILE_V01_008de825.png` | PASS with note - true profile and clear cap silhouette, same face. Faces screen RIGHT (prompt asked screen left); mirror in edit if direction matters. Cap slightly taller. | ☑ APPROVE (D-019) |
| neutral_standing | `MP_ELITE_NEUTRAL_STANDING_V01_87b625c8.png` | PASS - front full body, even stance, hands at sides, costume identical. Nearly the same framing as full_body V01 (acceptable for this slot). | ☑ APPROVE (D-019) |
| walking | `MP_ELITE_WALKING_V01_200b0388.png` | PASS - natural mid-stride from side-front, same face, boots/trousers/belt consistent, plain earth ground. | ☑ APPROVE (D-019) |
| costume_detail | `MP_ELITE_COSTUME_DETAIL_V01_2d1fbdfc.png` | PASS with note - collar right over left, silk/hemp weave, bronze plaque belt + pendants, sleeve ends and both hands clear. Crop shows mouth/chin (prompt said crop above chin) - harmless. | ☑ APPROVE (D-019) |
| expression_sheet | `MP_ELITE_EXPRESSION_SHEET_V01_f7d6da72.png` | PASS - five head-and-shoulders panels, same face, restrained neutral/attentive/concerned/resolved/quiet grief, no labels or text. | ☑ APPROVE (D-019) |
| back_view | `MP_ELITE_BACK_VIEW_V01_fba70a58.png` | PASS with note - directly behind, cap and shoulder silhouette clear, facing a mound under construction. Human check: a few thin grey scaffold poles at the top may read as modern metal pipes. | ☑ APPROVE (D-019) |

## 사람이 볼 점

1. 7장 모두 배치 1 얼굴과 같은 사람인지.
2. profile 이 오른쪽을 본다 (요청은 왼쪽). 편집에서 좌우 반전으로 해결 가능 → FIX 불필요 판단.
3. back_view 상단 비계 기둥 몇 개가 가는 회색 금속관처럼 보이는지 (시대 lock: 현대 재료 금지).
4. 모자가 몇 장에서 hero 보다 약간 높고 둥글다 — 허용 범위인지.

FIX 는 남은 3 호출 안에서 실패 항목만 (PATCH + 새 prompt 버전 먼저).

## 사람 판정 (D-019, 2026-09-13)

7장 모두 APPROVE. 원로 Master Pack 10/10 APPROVED → `CHARACTER_MASTER_APPROVED`. 배치 2 승인 호출 7/10 사용 (FIX 없음).
