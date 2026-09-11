# 08_GENERATION_CACHE

> DDABONG STUDIO OS v0.1 · 폴더 계약 · 출처: `00_SYSTEM/BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §21
> 이 폴더의 파일은 `00_SYSTEM/schemas/` 스키마를 따른다. 승인된 버전은 덮어쓰지 않고 새 버전을 만든다.

- **용도**: 유료 생성 결과 원본과 실행 기록(generation.json). 바이너리는 Git 미추적
- **소유 에이전트**: Cost Gate Agent
- **들어갈 파일**: generation.json / cost.json / approval.json (추적) + 생성물 파일(미추적)
- **ID 규칙 예시**: `GEN_<SHOT_ID>_<PROVIDER>_VNN`
