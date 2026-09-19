# CAMERA_GRAMMAR — 카메라 문법

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §6 §7
> **승인 전까지 정본 §6 §7 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `camera`, `router_decision`

---

## 기본 모션 어휘
`static` `dolly_forward` `dolly_back` `pan` `tilt` `tracking` `orbit` `crane` `push_in` `reveal`

## 파이프라인별 카메라
- **Flow/Veo**: 걷기·운반·바라보기·의례 준비·미세 상호작용·일반 dolly/pan/tracking.
- **Higgsfield**: 극단적 push-in/reveal · 시간 전환 · 과거↔현재 매치컷 · 고임팩트 카메라 · hero moment. 모든 역사 컷을 보내지 않는다.
- **Blender**: 공간·렌즈·높이 고정 후 키프레임.

## AI 순서 규칙
`REAL EVIDENCE → SPATIAL RECONSTRUCTION → CHARACTER LOCK → KEY FRAME → MOTION → CINEMATIC CAMERA`
연속성이나 공간 정확도가 중요하면 랜덤 text-to-video 로 시작하지 않는다.

### 마지막 프레임 → 첫 프레임 체이닝 (제한 채택, DRAFT 2026-09-19 · P-014-E · 근거 `09_ANALYTICS/benchmarks/WORKFLOW_MASTERPROMPT_FLOW_20260919.md` §3-E)
- 허용: **D형 컷 (사람 없는 모션 ≤3초, `VISUAL_STYLE_BIBLE` §39~42)** 두 개를 한 호흡으로 이어야 할 때만. 앞 컷의 마지막 프레임을 뒤 컷의 `start_image` 로 넣는다 (`gemini_omni_flash_1_1` i2v · `seedance_2_5` omni_reference 모두 지원).
- 금지: 사람이 있는 컷의 체이닝. 얼굴·의상 드리프트가 컷마다 누적된다 (09-18 도구 재검토 §6, 8초가 정체성 유지 실질 한계).
- 체인은 최대 2단. 3단부터는 정지 컷 + 패럴랙스로 돌아간다.
- 체인 결과는 두 컷 이음새 12프레임 시트 (`QA_STANDARD` 영상 검수) 로 검수한다.

## 기본값 (D-035 #7)
`camera_*.json` 이 없는 샷은 **35 mm · 높이 1.6 m · tilt 0°** 를 쓴다 (사람 눈높이 정지 기준). 프롬프트 템플릿(`PHOTO_AI_REDESIGN_V01` 등)의 `{lens_mm}` `{cam_h}` `{tilt}` 빈 자리는 이 값으로 채운다. 다른 값을 쓰면 camera 인스턴스를 만든다.

## 카메라 LOCK ID
`CAMERA_S<NNN>_V<NN>` (예: `CAMERA_S004_V02`) — 프롬프트 조립의 CAMERA DATA 조각.

---

## 미결 (사용자 결정 필요)

- 없음
