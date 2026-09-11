# 원로 Master Pack 배치 1 — 사람 검수 시트

> 생성 2026-09-11 · 승인 `APR_EP01_MP_ELITE_BATCH1_001` · 5 호출 / 4 채택 · 8.12 credits (KRW 환산 P-012)
> 이미지 파일은 Git 미추적 (이 폴더). 검수 결과는 `character.master_pack.<slot>.status` 를 APPROVED / MISSING(재생성) 으로 갱신하고 D-번호를 남긴다.

| slot | 파일 | 모델 | 판정(봇) | 사람 검수 |
|---|---|---|---|---|
| hero (V01) | `MP_ELITE_HERO_V01_35407202.png` | soul_2 | **REJECTED** — 갑옷 두 번째 인물, 다홍 내의, 가짜 문자 워터마크 | 참고용만 |
| hero (V02) | `MP_ELITE_HERO_V02_c7a5cc92.png` | nano_banana_pro | PASS — 단독, muted blue + 상아 내의 + bronze 과대 + 자작나무 관모, 문자 없음 | ☐ APPROVE ☐ FIX |
| front | `MP_ELITE_FRONT_V01_ae0b4062.png` | nano_banana_pro + hero 참조 | PASS — 동일 얼굴, 균일광, 무배경 | ☐ APPROVE ☐ FIX |
| three_quarter_left | `MP_ELITE_THREE_QUARTER_LEFT_V01_8d82a4c5.png` | nano_banana_pro + hero 참조 | PASS — 동일 얼굴, 관모 실루엣 명확 | ☐ APPROVE ☐ FIX |
| full_body | `MP_ELITE_FULL_BODY_V01_5681f1e0.png` | nano_banana_pro + hero 참조 | PASS — 전신, 화(靴)+버선, 통 넓은 회색 바지, 자연 비율 | ☐ APPROVE ☐ FIX |

## 검수 포인트 (사람이 결정)

1. **표의 소매 길이** — 4장 모두 표의가 반소매, 내의 좁은 소매가 밖으로 나옴. lock 은 "좁은 소매 유 + 긴 표의" 라 위반은 아니지만 의도(긴 소매 표의)와 다르면 FIX(COSTUME) → KEEP face/cap/belt, CHANGE sleeve → 4장 재생성 (약 8 credits).
2. **관모** — 백화모 계열 원뿔형. 근거 CLM_003/008 과 맞는지 확인.
3. **연령** — 40대 후반 인상. 50대로 올릴지.
4. hero V02 배경의 기와지붕 — hero 는 대표 초상이라 허용 범위인지.
5. 동일 얼굴 판정 — 4장 나란히 놓고 확인.

## 승인 시 다음 단계 (G1 잔여)

three_quarter_right · profile · neutral_standing · walking · costume_detail · expression_sheet 6장 + back_view 1장 (보조) — 전부 hero V02 를 image_references 로. 별도 approval `APR_EP01_MP_ELITE_BATCH2_001`.
