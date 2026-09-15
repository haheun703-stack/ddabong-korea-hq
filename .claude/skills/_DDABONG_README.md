# 설치된 외부 스킬 (D-051, 2026-09-15)
출처: AI ASTRA (@aiastra0) 「프롬프트 자료집」 — 자유 사용, 출처 표기. 원본 zip 은 `프롬프트 자료집/스토리보드 및 스킬/`, 참고 시트 PNG 는 용량 때문에 제외.

| 스킬 | 우리 용도 | 치환 규칙 |
|---|---|---|
| storyboard-v1 | 섹션별 프리비즈 12컷 시트 | `gpt_image_2` → Higgsfield `nano_banana_pro` 3:2. 셀 텍스트는 영문만 (한글 헤더 깨짐 시험 전까지). 캐릭터·배경 = 승인 정지 컷을 reference 로 |
| storyboard-v2 | D형 인서트·H07 매치컷 START/END | 인물 모션 금지 (D-050) — 사람 없는 컷에만 |
| master-sheet-v2 | 마스터팩 재캐스팅 시트 (정면·3/4·측면·전신·표정) | 스타일 lock = `DDABONG_SAGEUK_CINEMATIC_V02`, 참조 주입은 정면 1컷 우선 |
| seedance-continuity-builder | 연속성 바이블·카메라 4요소 표기 | Seedance 2.0 전용 기능(첫 프레임 고정·15초 연장)은 무시. 인물 움직임 프롬프트 생성 금지 |

공통: Sent Prompt Rule 적용 — 스킬이 만든 프롬프트도 `prompt_*.json` 저장 → 전송 → 기록.
