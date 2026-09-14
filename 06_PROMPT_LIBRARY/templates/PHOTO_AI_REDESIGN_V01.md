# PHOTO_AI_REDESIGN_V01 — 사진→AI 리디자인 프롬프트 템플릿 (파이프라인 A4)

> v0.1 DRAFT (2026-09-14) · `PHOTO_AI_STANDARD.md` §2 A4 · 조립 결과는 `prompt` 인스턴스 `assembled_text` 로 저장하고 **그대로** 전송한다 (Sent Prompt Rule).
> lock 조립: prompt 인스턴스의 `locks` 필수 키는 유지한다 — `era: "NONE"`, `location`: 해당 LOC lock 또는 `"NONE"`, `character_costume: []`, `style: DDABONG_DOC_REENACTMENT_V01`. `global` 은 현재 시점용 `DDABONG_GLOBAL_PRESENT_V01` (+ 짝 `DDABONG_NEGATIVE_PRESENT_V01`) — **D-035 #1 로 신설 (APPROVED)**. 검증기는 `global` 이름으로 negative 세트를 고르므로 `negative` 배열은 `DDABONG_NEGATIVE_PRESENT_V01.items` 를 전부 포함해야 한다. 참고 원본은 `reference_images: ["rights:<rights_id>"]` 로 계보 기록 (검증기가 실존 확인).

## 템플릿

```
[REFERENCE IMAGE: {source_rights_id} — GREEN, attached]        ← GREEN 일 때만. YELLOW 면 이 줄 삭제
Present-day {location_name}, {country}. Photorealistic documentary still, {aspect} , {resolution_hint}.
Keep from the reference: the exact landform and silhouette of {subject} (shape, proportion, position in frame at x≈{cx}, horizon at y≈{hy}), the surrounding trees and paths.
Change: season → {season}; light → {light} ({time_of_day}); weather → {weather}; remove all people, signage, vehicles, and modern clutter unless listed here: {keep_list}.
Camera: {lens_mm} mm, height {cam_h} m, tilt {tilt}°, {motion_note_for_still}.
Grass color {grass}; sky {sky}. No text, no watermark, no lens flare, no HDR look, no oversaturation.
Documentary tone, neutral grade, slight film grain acceptable.
```

## 자리표 채우는 규칙

| 자리표 | 출처 |
|---|---|
| `{location_name}` `{country}` | `location.json` (`name_en`) |
| `{subject}` `{cx}` `{hy}` | GREEN 참고 이미지에서 읽거나, YELLOW 면 `photo_ai.composition_ref_note` 의 수치 |
| `{season}` `{light}` `{time_of_day}` `{weather}` | 샷 `notes` · 계절 통일 규칙 (EP 단위로 한 계절) |
| `{lens_mm}` `{cam_h}` `{tilt}` | `camera_*.json` 있으면 그 값, 없으면 CAMERA_GRAMMAR 기본 (35 mm · 1.6 m · 0°) |
| `{keep_list}` | 샷 목적상 남겨야 할 요소 (예: "one distant visitor, back view, ≤3% of frame") |
| `{aspect}` `{resolution_hint}` | 16:9 · "4K master" |

## 샘플 (EP01_S02_SH001 · 대릉원 봉분 무리 경관)

```
[REFERENCE IMAGE: RTS_COMMONS_DAEREUNGWON_GAGNON_001 — GREEN, attached]
Present-day Daereungwon Tomb Complex, Gyeongju, South Korea. Photorealistic documentary still, 16:9, 4K master.
Keep from the reference: the exact landform and silhouette of the three overlapping grass-covered burial mounds (shape, proportion, position in frame at x≈0.50, horizon at y≈0.60), the pine trees at left and the gravel path.
Change: season → early summer; light → soft overcast daylight (mid-morning); weather → thin high cloud; remove all people, signage, vehicles, and modern clutter unless listed here: none.
Camera: 35 mm, height 1.6 m, tilt 0°, static tripod frame for slow 3% push-in in edit.
Grass color fresh green; sky pale grey-blue. No text, no watermark, no lens flare, no HDR look, no oversaturation.
Documentary tone, neutral grade, slight film grain acceptable.
```

이 샘플은 2026-09-14 prompt 인스턴스 `11_AI_STILLS/prompt_PRM_PA_EP01_S02_SH001_V01.json` 으로 저장됐다 (assembled_text = GLOBAL_PRESENT 문장 + 위 본문). 승인 `APR_EP01_PA_001` (D-034 #3, 1 호출 / 2 credits). 전송 여부는 generation 인스턴스로 확인.
