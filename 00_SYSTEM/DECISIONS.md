# DECISIONS — 결정 기록

> 확정된 결정은 `D-번호`, 승인 대기 제안은 `P-번호`. 승인되면 P → D 로 옮기고 날짜를 적는다.
> 큰 결정(정본 개정, 스타일 LOCK, 파이프라인 변경, 스키마 변경, 예산)은 반드시 여기에 남긴다. 결정은 삭제하지 않는다.
> 브랜드 결정 원본: `brand_decisions.json` (2026-08-14)

---

## 확정 (D)

### D-001 · 2026-08-14 · 영문 브랜드명 / 한글 표기 / 마스터 로고 (사용자)
**승인 내용** DDABONG KOREA · 따봉 코리아 · 태극 빨강/파랑 붓터치 엄지 + 대한민국 도장. Web HQ 밝은 테마.
**근거** `brand_decisions.json`

### D-002 · 2026-08-14 · 슬로건 (사용자)
**승인 내용** STORIES BEHIND KOREA. 브랜드 방향: 전통+현대 / 긍정+스토리텔링 / Why Korea? 관점.

### D-003 · 2026-08-14 · 핵심 채널 콘셉트 · 역사 해석 원칙 · 파일럿 3편 (사용자)
**승인 내용** "Not just what happened. Why it made sense to them." / FACT → CONTEXT → INTERPRETATION 분리 / Higgsfield 는 당시 사람의 생각·시선·갈등·선택 시각화 도구, `AI Visual Reconstruction` 표기 / 파일럿 순서 경주 왕릉 → 신라 금관 → 온돌.
**반영** `concept-bible.md`, 정본 §0 §9.

### D-004 · 2026-09-11 · 역사 인물 시각 스타일 = B Documentary Reenactment (사용자)
**승인 내용** 본편 역사 인물은 B. Hero/Thumbnail 만 A Cinematic Photoreal 수준 보조. C Semi-Realistic 3D 는 previz/참고. D Stylized 는 기본 아님.
**근거** CASE-DDABONG-CHAR-001 (정본 §20) → `schemas/examples/case_memory_TEMPLATE.json`
**주의** 마스코트·썸네일에 대한 전역 규칙이 아니다.

### D-005 · 2026-09-11 · DDABONG STUDIO OS v0.1 정본 채택 (사용자)
**승인 내용** `00_SYSTEM/BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` 를 봇 운영 계약으로. 멀티에이전트 6엔진, Continuity Engine, Learning Engine(4 memory + 회귀검사), KEEP/CHANGE, Money Gate 80/95/100, Source/Rights Ledger.
**반영** `BOT_BOOTSTRAP_PROMPT.md`, `bot-handoff.html`

### D-006 · 2026-09-11 · 활성 EP01 = 경주 왕릉/천마총, 황룡사 EP001 은 템플릿 예시 (사용자)
**승인 내용** OS 예시의 `EP001_HWANGNYONGSA` 는 템플릿. 활성 EP01 을 덮어쓰지 않는다.
**반영** `episode.json.template_note`, `schemas/examples/*_TEMPLATE.json` 은 EP001 ID 만 사용.

### D-007 · 2026-09-11 · P0 범위 · EP01 파일 처리 · Git 운영 (사용자)
**승인 내용**
- 리포 클론 위치: `H:\...\3. 따봉 코리아_유튜브 모음_260814\ddabong-korea-hq\`
- P0 범위 = 폴더 골격 전체 + 운영 문서 4종 + 스키마 전부 완성 + §22 나머지 표준 문서는 정본 내용을 옮긴 v0.1 DRAFT
- 기존 `episodes/ep01-*` 는 제자리 유지, `02_SEASONS/S01/EP01/episode.json` 매니페스트로 참조만
- 로컬 커밋까지 자율, **push 직전 변경 요약 후 사용자 확인**
**반영** `AGENT_RULES.md` §6, `.gitignore`, `episode.json.legacy_artifacts`

---

## 승인 대기 (P)

### P-001 · EP01 생성 예산 (Money Gate 기준값)
**제안** 통화·금액 확정 필요. 미확인 동안 `cost.gate_state = UNKNOWN_BUDGET` 으로 유료 생성 잠금.
**영향** `02_SEASONS/S01/EP01/episode.json.budget`, `COST_STANDARD.md`

### P-002 · 에피소드 ID 자릿수
**제안** 활성 EP01 은 `EP01` 유지 (기존 파일명 `ep01-*` 와 일치). 정본 예시는 `EP001`. 시즌 2 이후 3자리로 통일할지 결정.
**영향** `schemas/shot.schema.json` 등 ID 패턴은 두 자리·세 자리 모두 허용 중.

### P-003 · 표준 문서 언어
**제안** 한글 본문 + 영문 키/ID (형제 프로젝트 관례). 정본은 영문 유지.

### P-004 · 표준 문서 22개 v0.1 DRAFT → ACTIVE 승인
**제안** `00_SYSTEM/standards/*.md` 는 정본 내용 이관본. 검토 후 일괄 또는 개별 ACTIVE 승격. 승인 전에는 정본 §N 우선.
