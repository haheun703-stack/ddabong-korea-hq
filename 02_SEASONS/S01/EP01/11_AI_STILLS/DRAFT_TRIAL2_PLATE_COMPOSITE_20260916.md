# 시험 ② 실제 플레이트 합성 — 프롬프트 초안 (2026-09-16, 승인 전 · 생성 0)

광원 근거: `02_SEASONS/S01/EP01/01_RESEARCH/PLATE_LIGHT_ANALYSIS_DAEREUNGWON_20260916.md`
플레이트: `02_SEASONS/S01/EP01/02_SOURCES/RTS_COMMONS_DAEREUNGWON_GAGNON_001_5018x3345.jpg` (CC0, `RTS_COMMONS_DAEREUNGWON_GAGNON_001`)

**작업 방식 (두 안 공통)**: 오려붙이기 아님. **이미지 편집(인페인트)** 이다. 원본 사진 픽셀을 그대로 두고 인물과 접지 그림자만 그려 넣는다. 전면 재생성(리디자인) 금지 — 그러면 "사진 우선" 증명이 안 된다.
검수 기준: 200% 줌에서 ① 인물 경계 ② 발 접지 ③ 광질 일치 ④ 심도 일치 ⑤ 잔디 텍스처 연속성. 배경 픽셀이 바뀌었으면 FAIL.

---

## 안 A — 신라 원로 뒷모습 (어젯밤 원안)

- 목적: 순수 기술 시험. 통과해도 EP01 샷은 못 채운다 (분석 §6).
- 비용: 2~4 credits (1~2회).

```
Edit this photograph. Preserve every existing pixel of the photograph unchanged: the grass mounds, their exact silhouettes and proportions, the trees, the sky, the grass texture, the gravel path, the grain and the colour. Do not relight, do not recolour, do not re-render the background.

Add one standing human figure, and nothing else.

Figure: a senior Korean man in his 40s-50s seen from directly behind, standing still, looking away toward the mound. Early Silla elite dress (5th to early 6th century): muted grey-blue silk outer robe to about knee length, long narrow sleeves, straight collar crossed right over left with a shallow closing, plain leather plaque belt with silver plaques and no more than three short hanging pendants, ankle-tied trousers, socks and low leather boots, low soft blunt cap, hair tied up under the cap. No gold crown, no crimson, no purple, no short sleeves, no deep V opening, no tall conical hat, no bronze belt, no rank-colour trim.

Placement: feet at approximately x=0.30, y=0.63 of the frame. Figure height approximately 13.6% of the frame height. He must stand on the flat grass, not on the mound slope.

Lighting - match the photograph exactly: fully overcast diffuse skylight, no sun, no key light, no rim light, no backlight. Illumination comes from the whole sky dome above. Left and right sides of the figure must be within a third of a stop of each other. Neutral to very slightly cool white balance. Low contrast, matching the photograph's narrow range. Skin low in saturation and contrast, no glow, no sheen.

Shadow: no cast shadow. Only a soft ambient contact shadow directly under the feet, about 25-35% darker than the surrounding grass, soft-edged, fading out within 40 cm of the feet. Do not draw a long directional shadow.

Depth of field: everything sharp. The photograph was shot at f/8 on a 28.8mm-equivalent lens. The figure must be as sharp as the grass around him. No background blur, no subject blur, no bokeh.

Lens and grain: match the photograph's slight wide-angle perspective and its existing digital grain across the figure so he sits in the same image, not on top of it.

No text, no watermark, no logo, no lens flare, no HDR look, no oversaturation, no glossy AI look, no malformed anatomy, no extra people, no modern objects on the figure, no altered landform.
```

## 안 B — 현대 관람객 (봇 권장)

- 목적: `EP01_S06_SH011` ("현재 봉분과 관람객") 과 `EP01_S01_SH002` ("사람으로 크기 비교") 가 실제로 요구하는 그림. 통과 시 두 샷이 AI 리디자인 → **진짜 사진 + AI 인물** 로 승격.
- 비용: 2~4 credits (1~2회). 안 A와 동일.
- 난이도는 안 A보다 낮다 (현대 복장이라 고증 변수 없음, 인물이 더 작음).

```
Edit this photograph. Preserve every existing pixel of the photograph unchanged: the grass mounds, their exact silhouettes and proportions, the trees, the sky, the grass texture, the gravel path, the grain and the colour. Do not relight, do not recolour, do not re-render the background.

Add three present-day visitors walking together, seen from behind, and nothing else.

Figures: ordinary present-day visitors in plain casual clothing - muted jackets, trousers, one with a small backpack. Faces not visible, no recognisable individuals. Walking away from the camera along the flat grass toward the mound. Natural relaxed posture, mid-stride, slightly staggered spacing.

Placement: the group centred at approximately x=0.72, y=0.62 of the frame. Each figure approximately 11-14% of the frame height. They must stand on the flat grass, not on the mound slope. They exist to give the mound its scale.

Lighting - match the photograph exactly: fully overcast diffuse skylight, no sun, no key light, no rim light, no backlight. Illumination comes from the whole sky dome above. Left and right sides of each figure must be within a third of a stop of each other. Neutral to very slightly cool white balance. Low contrast, matching the photograph's narrow range. No glow, no sheen.

Shadow: no cast shadows. Only a soft ambient contact shadow directly under each pair of feet, about 25-35% darker than the surrounding grass, soft-edged, fading out within 40 cm. Do not draw long directional shadows.

Depth of field: everything sharp. The photograph was shot at f/8 on a 28.8mm-equivalent lens. The figures must be as sharp as the grass around them. No background blur, no subject blur, no bokeh.

Lens and grain: match the photograph's slight wide-angle perspective and its existing digital grain across the figures so they sit in the same image, not on top of it.

No text, no watermark, no logo, no lens flare, no HDR look, no oversaturation, no glossy AI look, no malformed anatomy, no crowds, no vehicles, no signage, no historical costume, no altered landform.
```

---

**상태**: DRAFT. 사용자가 A/B 선택 + Money Gate 승인 후에야 정식 prompt JSON 으로 저장하고 (Sent Prompt Rule) 전송한다. 현재 Higgsfield 커넥터 미인증이라 전송 불가.
작성: Claude Code, 2026-09-16 오전. 유료 도구 미사용.
