# EP01 P2 Character Master — 생성 전 사전 점검 (Pre-flight)

> 작성 2026-09-11 · Claude Code · 브랜치 `p1-continuity` · **유료 생성 0**
> 순서(사용자 고정): Character Lock 확인 → Master Pack 요구 확인 → 복식 TBD 검사 → Reference Set 구성 → FULL/LITE 분기 → Master Frame 후보 → **사람 승인** → 이후에만 유료 생성
> 검증: `validate.py` 231/231 PASS · cross-reference OK (reference_images 규칙 추가 후)

---

## 1. Character Lock 확인 — PASS

| lock | status | 원본 character | 영문 전용 | 복식 lock 연결 |
|---|---|---|---|---|
| `CHAR_SILLA_ELITE_OBSERVER_01_LOCK` | DRAFT | `CHAR_SILLA_ELITE_OBSERVER_01` (FULL) | ✔ | `COSTUME_SILLA_ELITE_A01_LOCK` |
| `CHAR_SILLA_LABORER_GROUP_01_LOCK` | DRAFT | `CHAR_SILLA_LABORER_GROUP_01` (LITE_CROWD) | ✔ | `COSTUME_SILLA_LABORER_A01_LOCK` |
| `CHAR_SILLA_ATTENDANT_GROUP_01_LOCK` | DRAFT | `CHAR_SILLA_ATTENDANT_GROUP_01` (LITE_CROWD) | ✔ | `COSTUME_SILLA_ATTENDANT_A01_LOCK` |

- lock 텍스트 = character `physical_lock` + `role` 영문화 (ba55720). 원로는 "not the deceased, not a king" 명시.
- 복식 lock 3종: 금관·금허리띠 복제 금지, 자색 금지, 조선 한복·명청 의복 금지 문구 포함.
- lock 은 전부 DRAFT → 사용자 승인 시 APPROVED 로 승격 (검수 항목 A).

## 2. Master Pack 요구사항 확인 — PASS (프롬프트 17 = 요구 17)

| character | tier | 필수 슬롯 | 프롬프트 파일 (`11_AI_STILLS/prompt_PRM_MP_*`) | 수 |
|---|---|---|---|---|
| ELITE_OBSERVER_01 | FULL | hero · front · 3/4 L · 3/4 R · profile · full_body · neutral_standing · walking · costume_detail · expression_sheet | 10 | 10 |
| ELITE_OBSERVER_01 | FULL +α | **back_view** (H05 뒷모습, 정본 슬롯 밖 · P-005) | 1 | 1 |
| LABORER_GROUP_01 | LITE_CROWD | full_body(체형 3인 병렬) · walking(짐 운반) · costume_detail | 3 | 3 |
| ATTENDANT_GROUP_01 | LITE_CROWD | full_body · walking · costume_detail(손·소매, H03) | 3 | 3 |

- 모든 MP 프롬프트: `target = IMAGE`, lock 5종 조립(`assembled_text`), `negative` 28항, `reference_images = []` (첫 생성이므로 정상).
- `master_pack.*.status`: 원로 10 MISSING · 군중 각 3 MISSING / 7 NOT_REQUIRED → 검증기 Lite 규칙 통과.

## 3. 복식 TBD 검사 — PASS (TBD 0)

- `costumes/` `characters/` `locks/` 에 문자열 `TBD` 없음.
- 복식 3종 `historical_basis = PROBABLE`, 사실 `CLM_SILLA_COSTUME_001–008` 연결 (D-011 게이트 통과 유지).
- 잔여 INTERPRETIVE 1건: **P-009** 원로 옷 색(비 vs 청)·과대 재질. lock 텍스트는 "muted crimson or blue tones, restrained silver or bronze" 로 양쪽을 허용하는 hedge 상태. **생성 전 사용자가 한쪽으로 확정하면 lock 1줄만 고치면 된다** (검수 항목 B). 미확정이어도 검증기는 차단하지 않는다.

## 4. Reference Set 구성 — DONE (생성 순서 = 참조 계보)

생성물은 3층 계보로 참조된다. 위층이 승인돼야 아래층 프롬프트의 `reference_images` 가 실체를 가진다.

```
층 1  Master Pack 17장          reference_images = []                 ← 첫 생성, 참조 없음
층 2  Master Frame 2장          ← character_pack (층 1 승인본)
        EP01_S04_MASTER_V01     laborer pack · CAMERA_EP01_S04_SH004_V01 · LOC_CHEONMACHONG
        EP01_S06_MASTER_V01     elite + attendant + laborer pack · CAMERA_EP01_S06_SH002_V01
층 3  AI 샷 프롬프트 8          ← master_frame (층 2) + character_pack (층 1)
        S04_SH004/5/6 ← S04_MASTER + laborer
        S06_SH002/5/10 ← S06_MASTER + (elite, attendant, laborer)
        S05_SH005 ← attendant pack 만 (손 클로즈업, master_frame 없음)   ← 이번에 수정
        S08_SH002 ← 참조 없음 (인물 없음, H07 매치컷은 실사 SH003 구도 후 생성)
```

**수정 1건**: `prompt_PRM_EP01_S05_SH005_V01` 이 존재하지 않는 `master_frame:EP01_S05_MASTER_V01` 을 참조하고 있었다 (샷 `master_frame = null` 과 불일치). 참조 제거. S05 는 반복 개인 인물이 없는 손 클로즈업이라 정본 규칙상 master_frame 불필요.
**검증기 규칙 추가**: prompt `reference_images` 의 `master_frame:<id>` / `character_pack:<id>` 가 실존해야 한다 (음성 테스트: 수정 전 1 broken 검출 → 수정 후 OK).

## 5. FULL / LITE 분기 — 유지 (승격 대상 없음, 사람 확인 필요)

| character | 등장 샷 | 전경·얼굴 식별? | 판단 |
|---|---|---|---|
| ELITE_OBSERVER_01 | S06_SH002 (H04 원경) · S06_SH005 (H05 뒷모습) | 반복 개인 | **FULL** 유지 |
| LABORER_GROUP_01 | S04_SH004/5/6 (H01·H02 작업) · S06_SH002/5 배경 | 작업 동작 중심, 반복 얼굴 없음 · H02 는 "와이드→손 푸시인" | LITE_CROWD 유지 · **주의**: H02 푸시인이 특정 얼굴에 머물면 승격 검토 |
| ATTENDANT_GROUP_01 | S05_SH005 (H03 손 클로즈업) · S06_SH002/5/10 | 손·소매 전경, 얼굴 프레임 밖 | LITE_CROWD 유지 · costume_detail 이 손·소매 중심이어야 함 |

규칙(D-008): BACKGROUND CROWD = Lite / RECURRING OR FOREGROUND = Full. 자동화(P-008 `character_visibility` 필드)는 P2 백로그, 지금은 사람 검수 (검수 항목 C).

## 6. Master Frame 후보 — DRAFT 2 (path 없음)

| frame | 씬 | 인물 | 카메라 | 파생 샷 | 생성 기준 |
|---|---|---|---|---|---|
| `EP01_S04_MASTER_V01` | S04 봉분 조성 | laborer | `CAMERA_EP01_S04_SH004_V01` | SH004 · SH005 · SH006 | 라우터: Blender 공간 lock → 키프레임 1장. SH005/6 은 같은 씬에서 카메라만 변경 |
| `EP01_S06_MASTER_V01` | S06 장례 준비 | elite + attendant + laborer | `CAMERA_EP01_S06_SH002_V01` | SH002 · SH005 · SH010 | 역할별 배치(공간 80) lock. H05 는 같은 배치를 관찰자 뒤에서 |

Master Frame 은 Master Pack 승인(`CHARACTER_MASTER_APPROVED`) 뒤에 생성한다 (정본 §5).

## 7. 사람 승인 — 대기 항목

| # | 항목 | 결정 ID | 차단 여부 |
|---|---|---|---|
| A | Character lock 3 + Costume lock 3 → APPROVED | (신규) | 생성 전 필요 |
| B | 원로 옷 색 비 vs 청 · 과대 은 vs 동 | P-009 | 권장 확정, 미확정 시 hedge 유지 |
| C | 군중 2그룹 LITE_CROWD 유지 확인 (승격 없음) | D-008 | 확인만 |
| D | back_view 슬롯 추가 (스키마 변경) 또는 슬롯 밖 보조 이미지로 취급 | P-005 | 생성 자체는 차단 안 함 |
| E | 라우터 49건 ACCEPT / OVERRIDE | P-011 | **AI 샷(층 3) 차단** · Master Pack(층 1) 은 무관 |
| F | **EP01 생성 예산** → Money Gate OPEN | P-001 | **모든 유료 생성 차단** |

## 8. 승인 후 생성 계획 (참고 · 실행은 승인 뒤)

| 단계 | 대상 | 장수 | 선행 |
|---|---|---|---|
| G1 | 원로 FULL 10 + back_view 1 | 11 | A · F (B 권장) |
| G2 | 노동자 3 · 시종 3 | 6 | A · F |
| G3 | 원로 `CHARACTER_MASTER_APPROVED` 판정 · KEEP/CHANGE 패치 | — | G1 검수 |
| G4 | Master Frame S04 · S06 | 2 | G3 · E |
| G5 | AI 샷 8 (BLENDER_FLOW 6 · AI_STILL 1 · HIGGSFIELD 1) | 8 | G4 · E · SH003 실사 |

합계 이미지 19장 후 비디오. 비용 산정은 P6 Money Gate 어댑터.
