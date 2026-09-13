# 전체 검수 수정 — 2026-09-13

> 대상: 2026-09-11 전체 검수 (HEAD `318fc24`) 에서 나온 우선 수정 1–5. **유료 생성 0.** Higgsfield 는 조회(job_status)만 사용.
> 스크립트 `00_SYSTEM/tools/fix_review_20260913.py` (재실행 시 변경 없음) · 검증 `00_SYSTEM/schemas/validate.py` 244/244, 상호참조 OK.

## 1. 실제 전송 프롬프트가 기록과 달랐음 → 버전으로 저장

Higgsfield job 5건의 `params.prompt` 를 복구했다. 5건 모두 V01 `assembled_text` 를 그대로 보내지 않았다 (hero 1차 soul_2 시도 포함).

| generation | 이전 기록 | 실제 전송 = 새 prompt | parent |
|---|---|---|---|
| `GEN_MP_ELITE_HERO_HIGGSFIELD_V01` (REJECTED) | HERO_V01 | `PRM_…_HERO_V02` | HERO_V01 |
| `GEN_MP_ELITE_HERO_HIGGSFIELD_V02` | HERO_V01 | `PRM_…_HERO_V03` + `PATCH_MP_ELITE_HERO_001` | HERO_V02 |
| `GEN_MP_ELITE_FRONT_HIGGSFIELD_V01` | FRONT_V01 | `PRM_…_FRONT_V02` | FRONT_V01 |
| `GEN_MP_ELITE_THREE_QUARTER_LEFT_HIGGSFIELD_V01` | …_V01 | `PRM_…_THREE_QUARTER_LEFT_V02` | …_V01 |
| `GEN_MP_ELITE_FULL_BODY_HIGGSFIELD_V01` | FULL_BODY_V01 | `PRM_…_FULL_BODY_V02` | FULL_BODY_V01 |

**솔직한 기록**: hero 재시도는 "실패 항목만 변경" 원칙을 지키지 못했다. 실패 3항목(두 번째 인물·다홍·워터마크) 외에 모델(soul_2 → Nano Banana Pro)과 프롬프트 전문을 바꿨다. patch 의 `change` 에 그대로 적었다.

## 2. 모델명

기록 오류라기보다 표기 누락이었다. Higgsfield 표시명은 **Nano Banana Pro**, 내부 job type 은 **`nano_banana_2`** (2 credits/장). `generation.provider_job` 필드(스키마 추가)에 `job_id · job_set_type · display_name · params_path` 를 남기고, 원문 params 는 `08_GENERATION_CACHE/EP01/provider_jobs/HF_<job>.json` (결과 URL 제외).

## 3. 검증기 Money Gate 규칙 (`money_rules`)

| 규칙 | 음성 테스트 |
|---|---|
| 유료·비용미상 생성에 approval_id 없음 | CAUGHT |
| approval 이 APPROVE 된 PAID_GENERATION 아님 | CAUGHT |
| prompt(부모 계보의 뿌리)가 approval prompt_ids 밖 | CAUGHT |
| 생성 호출 수 > expected_attempts | CAUGHT |
| prompt_id 없음 / prompt_version 불일치 | CAUGHT |
| Higgsfield 생성에 provider_job 없음 · 전송 프롬프트 ≠ assembled_text | CAUGHT |
| cost 크레딧 합계 ≠ generation 합계 · 폴더 generation 미등재 | CAUGHT |
| episode.budget ≠ 최신 cost.budget | CAUGHT (수정 전 실데이터) |
| Master Pack 슬롯 DRAFT/APPROVED 인데 path·generation 없음 / SUCCESS 출력 아님 | CAUGHT |
| patch ↔ prompt 역참조 · parent 없음 · prompt_id 접미사 ≠ version | CAUGHT |
| negative ⊉ (DDABONG_NEGATIVE + 시대·장소·복식 lock `Forbidden:`) — 대체된 버전은 동결 | CAUGHT |

"전송 프롬프트 = assembled_text" 규칙 덕분에, 이미 보낸 프롬프트의 본문을 V01 그대로 고치면 이제 FAIL 이 난다 (검수 지적 8 부분 해소). 앞으로는 **보낼 문장을 먼저 prompt 새 버전으로 저장하고 그대로 보낸다.**

## 4. negative 누락

원로 13개만이 아니었다. 프롬프트 25개 전부 negative 가 공통 목록 복사본(28개)이라 시대 lock(조선식 기와 궁궐·석조 능묘 등)과 복식 lock(다홍·자색·은/금 과대, 노동자 관복색 등) 금지 항목이 빠져 있었다. 아직 보내지 않은 21개는 제자리 보강, 이미 보낸 V01 4개는 기록으로 동결하고 새 버전에 반영했다. 재발 방지는 규칙 3의 마지막 줄.

## 5. 예산 소진 불일치

`episode.json` budget.spent `0` → `null` (cost 파일과 동일: 8.12 credits, KRW 환산 P-012 미정).

## 함께 처리

- 데이터 생성 스크립트 8개를 임시 폴더에서 `00_SYSTEM/tools/legacy_20260911/` 로 이동.
- CURRENT_STATUS 옛 문구 (샷 48 · P2 NEXT · 예산 미확인 · P3/P4 옛 할 일), `COST_STANDARD.md` · `EP01_MASTER_PACK_REQUIREMENTS.md` 의 UNKNOWN_BUDGET 문구 정리.

## 남은 것 (중요도 낮음 · 확인 필요)

- Web HQ 두 페이지 옛 상태 — main 병합 때 동기 반영 (기존 결정).
- H07 프롬프트 target IMAGE ↔ 샷 파이프라인 HIGGSFIELD — 정지 컷인지 영상 매치컷인지 사람 결정.
- hero V03 배경 기와지붕이 시대 lock 금지(조선식 기와 건물군)에 해당하는지 — Work 검수에서 함께 판정.
- 배치 1 사람 판정 (APPROVE/FIX) 대기.
