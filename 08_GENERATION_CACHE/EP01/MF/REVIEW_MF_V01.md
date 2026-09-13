# EP01 기준 그림 V01 — 사람 검수 시트

> 2026-09-13 · 승인 `APR_EP01_MF_001` (D-026) · 3 호출 / 3 성공 · 6 credits (한도 10 호출 / 20 credits 중 3 호출)
> 전송 = 각 `PRM_MF_*_V01` 문장 그대로. FIX 문장(V02)과 PATCH 는 저장만, 사용자 OK 후 전송.

| frame | 파일 | 봇 판정 | 사람 검수 |
|---|---|---|---|
| EP01_S04_MASTER_V01 | `MF_EP01_S04_MASTER_V01_4de7af1f.png` | Bot check: layer stage correct (open-topped timber chamber on levelled ground, low course of river stones at its walls, no mound yet), timber yard left, labourers in hemp with baskets, dust, overcast. ISSUES: several metal tool heads (pick-axes, hoes, saw, one metal-bladed spade) despite 'wooden tools only'; black letterbox bars baked in at top and bottom. -> FIX edit proposed (PATCH_MF_EP01_S04_001). | ☐ APPROVE ☐ FIX |
| EP01_S06_MASTER_OPEN_CHAMBER_V01 | `MF_EP01_S06_MASTER_OPEN_CHAMBER_V01_80d2d3db.png` | Bot check: stage correct (open-topped chamber, coffin and chest inside, low stone course outside, no stones or earth on top), attendants in belted hemp holding cloth bundles, two women in grey skirts, labourers waiting with stone baskets, exactly one person in blue (observer, three-quarter back, birch-bark cap), late light. ISSUES: coffin has a tapered hexagonal Western-coffin outline; chest has metal hinges and latch; observer's belt is a plain leather strap without bronze plaques or pendants. -> FIX edit proposed (PATCH_MF_EP01_S06_OPEN_CHAMBER_001). | ☐ APPROVE ☐ FIX |
| EP01_S06_MASTER_MOUND_BUILDING_V01 | `MF_EP01_S06_MASTER_MOUND_BUILDING_V01_8e1007b7.png` | Bot check: stage acceptable (heap of river stones with earth mound rising over and around it, no timber/coffin/chamber visible), labourers carrying earth baskets on the slope with ropes, attendants in belted hemp at the base, exactly one person in blue (observer from behind, birch-bark cap). NOTES (not blocking): front of the stone heap is still exposed below the earth (plausible mid-construction); mound crop makes the 3.7:1 proportion hard to judge; observer belt shows plaques faintly but no pendants. | ☐ APPROVE ☐ FIX |

## FIX 제안 (저장됨, 미전송)

- S04 → `PRM_MF_EP01_S04_MASTER_V02` + `PATCH_MF_EP01_S04_001`: 쇠 공구 → 나무 공구, 위아래 검은 띠 제거. 입력 = V01 이미지. 1 호출.
- S06 OPEN_CHAMBER → `PRM_MF_EP01_S06_MASTER_OPEN_CHAMBER_V02` + `PATCH_MF_EP01_S06_OPEN_CHAMBER_001`: 관 → 곧은 네모 나무 상자, 궤 쇠 경첩 제거, 원로 허리띠 → 청동 과대. 입력 = V01 이미지 + 원로 전신. 1 호출.
- S06 MOUND_BUILDING: 수정 없음 제안 (메모만).

FIX 2건 전송 시 누적 5 / 10 호출, 10 / 20 credits.

## 사용자 판정 (2026-09-13)

- S04: **FIX** — 쇠 공구 → 나무, 검은 띠 제거.
- S06 OPEN_CHAMBER: **FIX** — 관 형태 + 원로 허리띠만. 궤 위치·경첩은 이번 수정 범위 밖 (T자 배치는 G13 이 전달).
- S06 MOUND_BUILDING: **APPROVED**.

## FIX 결과 (2026-09-13, 4 credits, 승인 5/10)

- S06 OPEN_CHAMBER V02 `MF_EP01_S06_MASTER_OPEN_CHAMBER_V02_de2b6a3e.png`: **PASS** — 곧은 네모 관, 청동 과대+드리개. 사용자 최종 OK 대기.
- S04 V02 `MF_EP01_S04_MASTER_V02_da44103f.png`: **PARTIAL** — 검은 띠 그대로, 쇠 삽·톱 일부 남음. 편집 반복 중단 → 새로 생성 V03 저장 (`PATCH_MF_EP01_S04_002`), 사용자 OK 대기.
- 크레딧: 이번 쌍에서 잔액 -6, 거래 내역에 06:31:23Z 출처 불명 -2 (공용 계정, D-018) → EP01 비용 미포함.

**사용자 OK (2026-09-13)**: S06 OPEN_CHAMBER V02 최종 APPROVED · S04 새로 생성 V03 진행.
