# AGENT RULES — DDABONG STUDIO OS 에이전트 공동 작업 규칙

> 모든 봇/에이전트는 서로 대화하지 않는다. **같은 리포와 같은 문서를 읽는다.** 이 문서가 그 계약이다.
> 사람(채널 운영자)이 감독·최종 승인, MASTER ORCHESTRATOR 아래 6개 엔진의 에이전트가 작업한다. 정본: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §1 §3 §23 §24.
> 문서 버전 v0.1 (2026-09-11)

---

## 0. 작업 시작 전 반드시 읽는 순서

1. `00_SYSTEM/BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` — 운영 계약 (정본)
2. `00_SYSTEM/BOT_BOOTSTRAP_PROMPT.md` — 봇 행동 규약
3. `00_SYSTEM/CURRENT_STATUS.md` — 지금 어디까지 왔나, 현재 게이트
4. `00_SYSTEM/OS_INDEX.md` — 문서·스키마 지도
5. `00_SYSTEM/ACTIVE_TASK.md` — 다른 에이전트의 잠금 확인
6. 활성 에피소드 매니페스트 `02_SEASONS/S01/EP01/episode.json` + 그 `legacy_artifacts`

읽지 않고 시작한 작업은 무효로 본다.

---

## 1. 공통 규칙 (정본 §1)

| # | 규칙 | 운영 의미 |
|---|---|---|
| 1 | Generate Late | 리서치·역사 QA·씬/샷/카메라 결정 이전에 유료 생성 금지 |
| 2 | Reuse Everything | ID(era/location/character/costume/prompt lock/camera) 가 있으면 새로 만들지 않는다 |
| 3 | Change Only What Failed | 한 요소 실패 → `keep_change_patch` 로 새 버전. 전체 재생성 금지 |
| 4 | Human Approval Before Cost | 유료 호출·의미 있는 역사 해석은 `approval` 기록 후 진행 |
| 5 | Evidence Before Imagination | 실제 자료 → 복원 → 영화적 창작 순서. 샷·주장에 FACT/PROBABLE/INTERPRETIVE/ARTISTIC 명시 |
| 6 | Never overwrite approved | 승인본은 `version_history` 누적 + 새 `V<NN>`. 롤백 가능 |
| 7 | 제작 ≠ 시스템 개선 | 일상 제작은 ACTIVE 표준만 사용. 규칙 변경은 `evaluation` + 회귀검사 후 승격 |
| 8 | Sent Prompt Rule (D-016) | 보낼 문장을 먼저 prompt 새 버전으로 저장 → 그 `assembled_text` 를 그대로 전송 → generation 에 `prompt_id` + `provider_job` 연결. 어기면 검증 FAIL |

**에이전트 인계 규칙**: 자유 의견을 진실처럼 넘기지 않는다. ID·status·provenance 가 있는 구조화 데이터(스키마 인스턴스)로 넘긴다.
**Provider 추상화**: Agent ≠ provider. Gemini/Claude/OpenAI/Flow/Veo/Higgsfield/Suno 는 교체 가능하며 OS 는 살아남아야 한다.

---

## 2. 엔진별 에이전트 — 담당 / 금지 / 산출 스키마 (정본 §3)

### Story Engine
**담당** Research Agent(리서치 원문·요약) · Fact Check Agent(`fact.json` `source.json`) · Strategy Agent(`01_CHANNEL/channel.json` 페르소나·핵심 질문 · `QUESTION_BANK` 분류 · 벤치마크 `BENCHMARK_STANDARD` · 스토리 앵글, 채널 기준서) · Thumbnail Agent(§14 컴포저·QA) · Script Agent(대본 버전) · Narration Director(§16 리듬)
**금지** 출처 없는 주장 작성 · 기록에 없는 내면 생각을 사실로 서술 · 승인된 대본 v2 를 다시 쓰기
**산출** `fact` `source` + `05_SCRIPT/` 버전 파일

### Continuity Engine
**담당** Character Supervisor(`character.json`, Master Pack 상태) · Costume Supervisor(`costume.json`) · Location Continuity(`location.json`) · Scene Continuity(`scene.continuity_group`) · Master Frame Manager(`master_frame.json`)
**금지** "a Silla official" 식 자유 서술 프롬프트 · `CHARACTER_MASTER_APPROVED` 이전 유료 비디오 생성 · 모든 시대에 조선 한복
**산출** `character` `costume` `location` `era` `master_frame`

### Visual Engine
**담당** Scene Planner(`scene.json`) · Shot Director(`shot.json`) · Visual Router(`router_decision.json`, §7) · Blender Agent(`camera.json`, §6) · Image/Video Generation Agent(`prompt.json` 조립 §8, `generation.json`)
**금지** 라우터 출력 없이 파이프라인 선택 · Blender 입력을 자연어로 · 모든 컷 Higgsfield · 승인 없는 유료 호출
**산출** `scene` `shot` `router_decision` `camera` `prompt` `generation` `keep_change_patch`

### Audio Engine
**담당** Music Director(`music.json`, Korean Cinematic Hybrid) · Voice/Narration Director(`voice.json`, 고정 내레이터) · Sound Director(VOICE/MUSIC/AMBIENCE/SFX/FOLEY 레이어)
**금지** 전통 음악 연속 재생 · 단일 공급자 종속 · 내레이터 얼굴 노출(기본 0%)
**산출** `music` `voice` + `13_AUDIO/` 인덱스

### Quality Engine
**담당** Historical QA(등급·출처 검증) · Visual QA(§13 fix reason 분류, `failure_memory`) · Rights Agent(`rights.json`, GREEN/YELLOW/RED/BLUE) · Retention QA(§17 노출 위험) · Cost Gate Agent(`cost.json`, 80/95/100%)
**금지** RED/BLUE 권리 상태로 게시 통과 · 예산 미확인 상태에서 유료 생성 허용 · QA 없이 FINAL 승격
**산출** `rights` `cost` `evaluation` `failure_memory`

### Publish & Learning Engine
**담당** Publish Agent(출처 링크 포함 게시 메타 · 설명란 템플릿 · 엔드스크린) · Shorts Agent(파생물, `SHORTS_STANDARD`) · Analytics Agent(`analytics.json` `performance_memory.json` · 실험 기록 `EXPERIMENT_STANDARD` · 댓글 수확) · Experience Learning Agent(`case_memory` → `evaluation` → `standard_version`) · **Community Agent**(고정 댓글·커뮤니티 포스트·답글 **초안**, `COMMUNITY_STANDARD`, D-046)
**금지** 출처 없이 게시 · 사례 1개로 전역 규칙 승격 · ACTIVE 표준을 실험으로 덮어쓰기 · **봇의 댓글·포스트 자동 게시** (초안만, 게시는 사용자) · 출처 없는 답글
**산출** `analytics` `performance_memory` `case_memory` `standard_version` `evaluation`

### 보고 형식 (모든 에이전트, 작업 종료 시)
```
변경한 것: (파일/ID 목록)
남은 것: (다음 할 일)
다음 게이트: (§2 파이프라인 단계명)
승인 필요: (있으면 approval 종류와 대상 ID)
```

---

## 3. 사람 — 최종 승인

- 유료 생성(Money Gate), 역사 해석 수위, 버전 승인(⭐ APPROVE / 🔄 FIX / ❌ REJECT), 규칙 승격, 게시 — 모두 사람만.
- 사람의 수정/선택은 반드시 `case_memory` 로 남긴다 (초안 + 결과 + 이유 + 범위).

---

## 4. 충돌 시 우선순위

1. 사람의 최신 승인(`DECISIONS.md` D-번호)
2. `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` (정본)
3. `standards/*.md` 중 `status: ACTIVE` 인 버전
4. `CURRENT_STATUS.md`
5. DRAFT 표준, 에이전트 판단

정본과 DRAFT 표준이 다르면 정본. 정본과 D-결정이 다르면 D-결정 (정본 개정 대상으로 P-번호 등록).

---

## 5. 작업 잠금 — `ACTIVE_TASK.md`

- 시작 시 `agent / task / started / files` 를 채운다. 끝나면 `agent: none`.
- 다른 에이전트의 잠금이 살아 있으면 그 `files` 는 읽기만.
- 24시간 넘게 남아 있으면 사람에게 확인 후 비운다.

---

## 6. Git

- 브랜치: 시스템 작업 `p<N>-<topic>`, 에피소드 작업 `ep01-<topic>`.
- 커밋 메시지 한 줄 요약 + 본문에 변경 ID 목록.
- ~~로컬 커밋까지는 자율. push 는 변경 요약을 사람에게 보여주고 확인 후. (D-007)~~ → **D-025 (2026-09-13)**: `validate.py` 전체 PASS + 상호참조 OK 이면 작업 브랜치(`p1-continuity` 등) **push 자동**, 끝나고 쉬운 한국어 요약 보고. 검증 실패 시 push 금지. `main` 병합·push, force push, 히스토리 재작성은 계속 사람 OK 후.
- **운영 방식 (D-025)**: 무료 작업은 계획 → 실행 → 검수 에이전트(별도 컨텍스트) OS 규칙 점검 → 검증기 → 커밋 → push 까지 자율. 사람 관문은 ① 유료 생성 승인(Money Gate) ② 그림 최종 OK/FIX (봇이 먼저 거름) ③ 역사 해석 결정 ④ main 병합. 다른 회사 모델(Codex) 교차 검수는 큰 단계 완료 시에만. → **D-029 (2026-09-13)**: Codex 중계 종료. 큰 단계 교차 검수도 봇의 'Codex 역할 반박 검수 에이전트'가 맡는다. 유료·그림·역사·main 관문은 그대로.
- `episodes/` 기존 파일은 이동·삭제 금지. 참조는 `episode.json` 매니페스트.
- 바이너리 생성물은 `.gitignore` (08_GENERATION_CACHE, 10_EXPORTS, .blend, 촬영 원본).
- 상태가 바뀌면 **리포 파일과 Web HQ HTML 을 같이** 갱신한다 (정본 §24-10).

---

## 7. 상태 어휘 (공통)

| 어휘 | 뜻 |
|---|---|
| `DRAFT` | 작성 중, 승인 전 |
| `APPROVED` | 사람 승인. 덮어쓰기 금지 |
| `PREVIOUS` | 새 버전으로 대체됨. 보존 |
| `FINAL` | 게시용 최종 |
| `REJECTED` | 사람 거부. 이유는 `failure_memory` |
| `ACTIVE` / `PREVIOUS` (표준 문서) | 현재 적용 / 이전 적용 |
| `GREEN / YELLOW / RED / BLUE` (권리) | 사용 가능 / 조건부 / 불가 / 확인 중 |
| `OPEN / WARNING_80 / STRONG_WARNING_95 / LOCKED_100 / UNKNOWN_BUDGET` (비용) | Money Gate 상태 |
| `FACT / PROBABLE / INTERPRETIVE / ARTISTIC` | 역사 등급 |

---

## 8. 사람이 붙여넣는 짧은 명령

**봇에게**
- `상태` → `CURRENT_STATUS.md` 요약 + 현재 게이트 + 승인 필요 목록
- `EP01 계속` → 현재 게이트부터 이어서, 승인된 작업 재시작 금지
- `P1 시작` → Continuity Engine 인스턴스 생성 (유료 생성 없음)
- `머니게이트 <shot_id>` → §11 형식으로 제시하고 대기
- `KEEP/CHANGE <shot_id> <이유>` → 패치 작성, 새 버전, 전체 재생성 금지
- `사례 저장` → 직전 사용자 수정을 `case_memory` 로
- `push 해` → 즉시 검증 후 push (D-025 이후 검증 통과 시 자동이므로 보통 불필요)
