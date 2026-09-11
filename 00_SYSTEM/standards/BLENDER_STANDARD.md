# BLENDER_STANDARD — Blender 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §6
> **승인 전까지 정본 §6 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `camera`, `location`

---

## 역할
Blender 는 최종 얼굴 생성기가 아니다. **잠그는 것**: 공간 · 스케일 · 카메라 · 렌즈 · 인물 위치 · 이동 경로 · 높이 비율 · 건축 관계.

## 입력은 구조화 데이터 (`camera.schema.json`)
```json
{"lens":28,"camera_height":1.6,"duration":8,"fps":24,"motion":{"type":"dolly_forward","distance":7},"tilt":{"start":0,"end":14},"target":"MAIN_OBJECT"}
```
자연어 지시 금지.

## 경로
`BLENDER PREVIZ → APPROVED KEY FRAME → IMAGE/REFERENCE CONDITIONING → FLOW/VEO`

## 라이브러리
`04_BLENDER_LIBRARY/` 에 카메라 프리셋·장소 공간 데이터. `.blend` 는 Git 미추적, 경로만 `location.blender_scene_path`.

---

## 미결 (사용자 결정 필요)

- Blender 로컬 에이전트 브리지(P7) 방식
