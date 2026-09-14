# CHARACTER_CONTINUITY_STANDARD — 캐릭터·연속성 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §5 §20
> **승인 전까지 정본 §5 §20 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `character`, `costume`, `location`, `master_frame`, `keep_change_patch`

---

## Character Master Pack (유료 비디오 생성 전 필수)
반복 등장 인물마다 10종: `hero` `front` `three_quarter_left` `three_quarter_right` `profile` `full_body` `neutral_standing` `walking` `costume_detail` `expression_sheet`
→ 모두 APPROVED 이어야 `character.status = CHARACTER_MASTER_APPROVED`.

## 영구 ID
"a Silla official" 처럼 서술로 프롬프트하지 않는다. `CHAR_SILLA_OFFICIAL_01` · `COSTUME_SILLA_OFFICIAL_A01` · `LOC_GYEONGJU_BURIAL_SITE_V01`.

## Scene Master Frame
반복 인물이 있는 씬은 승인된 `master_frame` 을 가진다. 자식 샷은 그 시각 계보에서 파생 (`shot.master_frame`).

## KEEP / CHANGE
복식만 실패한 경우:
- KEEP `face_identity` `body` `camera` `composition` `lighting` `actor_position`
- CHANGE `collar shape` `belt` `sleeve ornamentation`
전체 프롬프트를 다시 쓰지 않는다. → `keep_change_patch.schema.json`

## 샷 기본 `must_keep`
`face_identity` `body_proportion` `hair` `costume` `height_ratio`

## 결정 사례
CASE-DDABONG-CHAR-001 (D-004): 본편 B, Hero 는 A 보조. 마스코트·썸네일 전역 규칙 아님.

---

## 미결 (사용자 결정 필요)

- ~~EP01 반복 인물 후보 목록 (Higgsfield 7컷 기준) 확정 → P1~~ → P2 완료 (D-023, 원로 FULL · 군중 LITE 2)

## 군중 장면의 참고 그림 (D-027)
군중(LITE_CROWD) 장면에 참고 이미지를 강하게 넣으면 그 얼굴이 군중 전체에 복제된다 (EP01 S04 V03·V04, 군중 2단계에서 확인).
- 군중의 복식·분위기는 **문장 설명 중심**으로 지정한다 (얼굴 다양성: 나이·수염·체격·머리 형태를 명시, 'no cloned faces').
- 참고 이미지는 **반복 인물 continuity 가 필요한 경우**(FULL Pack 인물, 예: 원로)에만 제한적으로 쓰고, 이미지마다 역할(얼굴/복식)을 문장에 지정한다.
- 군중이 옷만 맞추면 되는 경우 참고 이미지는 쓰지 않거나, 쓰더라도 결과의 얼굴 반복을 검수 항목에 넣는다.
