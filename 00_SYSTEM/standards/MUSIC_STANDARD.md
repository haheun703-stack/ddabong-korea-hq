# MUSIC_STANDARD — 음악 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-11, Claude Code) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §16
> **승인 전까지 정본 §16 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `music`, `rights`

---

- 정체성: **Korean Cinematic Hybrid** — 현대 시네마틱 스코어 안에 한국 전통 음색을 통합. 전통 음악 연속 재생 아님.
- 공급자 추상화: Suno 등 단일 벤더에 종속되지 않는다 (`music.provider`).
- 흐름: TEMP MUSIC MAP(대본 후) → FINAL MUSIC(러프컷 후).
- 모든 음악은 `rights_id` 필수.

---

## 미결 (사용자 결정 필요)

- 음악 공급자·라이선스 정책
