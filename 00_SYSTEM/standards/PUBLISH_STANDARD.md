# PUBLISH_STANDARD — 게시 기준

> 문서 버전 **v0.2 DRAFT** (2026-09-15, Claude Code · v0.1 2026-09-11) · 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §2 §23 · D-046 (설명란 템플릿·CTA·고정 댓글·엔드스크린 추가)
> **승인 전까지 정본 §2 §23 이 우선한다.** 승인되면 `standard_version` 을 ACTIVE 로 올리고 `DECISIONS.md` 에 D-번호를 남긴다 (P-004).
> 관련 스키마: `approval`, `asset`, `channel`

---

## 게시 전 필수
- FINAL APPROVAL (`approval.kind = PUBLISH`)
- 출처 링크 목록 (설명란) — 출처 없이 게시 금지
- 모든 외부 자산 권리 GREEN/YELLOW
- 역사 AI 장면 `AI Visual Reconstruction` 라벨 · 현재 시점 사진 기반은 `(present-day, photo-based)` (D-035 #2)
- 브랜드 인트로 3–5초 — 위치는 콜드오픈 뒤 (`BRAND_INTRO_STANDARD.md` v0.2, D-046)
- 제목·썸네일 문구가 `TITLE_STANDARD.md` 통과 · 실험 변형은 `EXPERIMENT_STANDARD.md` 로 기록

## 설명란 템플릿 (순서 고정, D-046)
1. **훅 1줄** — ① QUESTION 의 질문 한 문장 (접히기 전 영역. CTA 금지)
2. **AI 라벨 고지** — "Historical scenes are AI visual reconstructions, labeled on screen. Present-day landscapes are AI reconstructions from licensed photographs."
3. **Sources** — 본편이 인용한 `source.json` 전부 (기관 · 제목 · URL). 이미지 권리 표기 (CC0/KOGL/CC BY 출처 문구는 `rights.attribution_text`)
4. **Chapters** — 7단계 타임코드 (①…⑦)
5. **CTA 1개** — 구독 (`channel.json.cta_policy.description_cta`). 여기 한 곳만
6. **Credits** — 제작 · 내레이션 · 음악 · 도구(공급자·모델 명시)

## 고정 댓글
질문 1개 + 출처 1줄 (`COMMUNITY_STANDARD.md`). 봇은 초안만.

## 엔드스크린 · 카드 (업셀의 채널 등가물)
마지막 20초: 다음 에피소드 1 + 재생목록 1. 구독 버튼 1. 외부 링크 없음 (P-013 전).

## 산출
`16_PUBLISH/PUBLISH_META_<EP>.md` (title_final · 실험 변형 · 설명란 · 태그 · 고정 댓글 · 엔드스크린 · 체크리스트), `10_EXPORTS/` 매니페스트. 파생: `SHORTS / CLIPS` → `17_SHORTS/` (`SHORTS_STANDARD.md`).

## 해외 시청자
영어 제목/자막 기본. 한국어 로고 표기 병행 (D-001). 언어 정책은 `channel.json.language`.

## 업로드 주기
`channel.json.cadence` (D-046: 격주 토 14:00 UTC) · 측정 D+1/7/28 (`ANALYTICS_STANDARD` 미결 해소).

---

## 미결 (사용자 결정 필요)

- 게시 채널 계정·핸들·Studio 접근·자막 언어 범위 · 채널 트레일러 유무
- EP01 게시일 (P-012 · 편집 뒤)
