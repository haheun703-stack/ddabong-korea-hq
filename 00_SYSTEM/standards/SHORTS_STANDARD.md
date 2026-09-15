# SHORTS_STANDARD — 쇼츠·클립 파생 기준

> 문서 버전 **v0.1 DRAFT** (2026-09-15, Claude Code) · 출처: `PUBLISH_STANDARD.md` §산출 (17_SHORTS) · `STORY_ENGINE_STANDARD.md` §미결 '쇼츠 축약형' · AGENT_RULES Audio Engine 금지 '내레이터 얼굴 노출' · 자료집 역할 3 릴스기획 · 5 UGC대본(대체)
> **승인 전까지 정본이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `asset`
> 근거: D-046 (2026-09-15, "AI 마케팅팀 7명" 자료집 적용 — `AI 비서/` 캡처 9장, 구조 연구용)

---

## 1. 원칙
- 쇼츠는 본편의 **한 질문 · 한 장면 · 한 숫자** 로 만든다. 본편 요약이 아니다.
- **얼굴 없음**: 내레이터 얼굴 0% 규칙 유지 → UGC/토킹헤드 대신 **텍스트 온 이미지 + 내레이션**. AI 인물 재현은 본편 승인 컷만, 전체의 10% 안팎 (D-033 #3).
- 첫 프레임 텍스트 ≤ 6 단어 (질문의 축약, `TITLE_STANDARD.md` §3). 첫 3초 = 리빌 또는 숫자.
- 길이 20–45초, 세로 9:16 (본편 16:9 승인 컷을 크롭 — 크롭 안전 영역은 `GRAPHICS_SPEC` safe area).
- 라벨: 본편과 같은 AI 라벨 (`AI Visual Reconstruction` / present-day, photo-based). 출처 1개 이상 설명란.
- CTA: 마지막 2초 "full story ↗" + 본편 링크. 쇼츠에서 구독 요청 금지 (본편에서만).

## 2. 파일
`<EP>/17_SHORTS/SHORTS_PLAN_<EP>.md` (컷 목록·텍스트·출처) → 제작 뒤 `asset` 인스턴스 (derivative_of = 본편 shot_id).

## 3. 담당
Shorts Agent (계획·컷 선택) · Script Agent (텍스트) · Rights Agent (라벨·출처) · 사용자 (게시).

---

## 미결 (사용자 결정 필요)

- 편당 쇼츠 개수 (제안 2–3) · 게시 시점 (본편 D-1 티저 1 · D+2 · D+5).
- 세로 크롭 vs 세로 전용 재생성 (유료) — 기본은 크롭.
