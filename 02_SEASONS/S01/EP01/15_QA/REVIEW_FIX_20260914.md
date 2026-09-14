# 전체 검수 + 수정 — 2026-09-14 (D-029 멀티 에이전트 + 반박 검수)

> 대상: HEAD `bb27a98` (D-034 직후). **유료 생성 0.** 검수 에이전트 5 (코드 · 로직 누락 · 슬러지 · 데이터 정합성 · 신규 표준) → 반박 검수 1 (VERDICT + file:line) → 확정된 A 항목만 적용 → `validate.py` **336/336 PASS, 상호참조 OK** (rights +1). 수정 스크립트는 세션 임시 폴더에서 실행 (저장소에 일회성 스크립트를 더 두지 않음, A-24).

## 1. 검수가 찾은 것 (반박 검수 후 확정)

| 등급 | 무엇 | 어디 | 조치 |
|---|---|---|---|
| **치명** | 오늘 넣은 `photo_ai` 규칙이 `modification_allowed is not True` 로 검사 — rights 스키마 enum 은 `"YES"/"NO"/"UNKNOWN"` 문자열이라 실제 GREEN 원본이 **전부 FAIL** (어제 "부정 테스트 통과"는 이 때문에 잡히지 않음) | `validate.py` photo_ai_rules | `!= "YES"` 로 수정, `usage_tier != "ACTIVE"` 로 강화. 양성 테스트 통과 확인 (아래 §3) |
| 높음 | 현재 시점(present-day) 프롬프트가 `DDABONG_NEGATIVE_V01`(modern roads · concrete · electric lights …) 전 항목을 강제당함 → 파이프라인 A 프롬프트 조립 불가 | `validate.py` required_negative · 템플릿 §lock | 검증기는 `locks.global` 이름으로 negative 세트 선택 (GLOBAL_V01 → NEGATIVE_V01 기존과 동일, 회귀 0). PRESENT lock 신설은 **B-1 사용자 결정** |
| 높음 | 돈 관문: `cost.amount==0, spent>0` 이면 approval 없이 통과 · Sent Prompt Rule 이 `provider=="Higgsfield"` 정확 일치만 | `validate.py` money_rules | spent>0 도 approval 필수 · provider 비교 대소문자 무시 |
| 높음 | INTERPRETIVE AI 샷 라벨에 `INTERPRETIVE RECONSTRUCTION` 없음 (S06_SH002) · EP01 HIGGSFIELD 0 잠금(D-024) 미강제 · OVERRIDDEN 라우터에 note 없어도 통과 · GREEN ACTIVE 권리 attribution_text 미검사 | `validate.py` ledger_rules | 규칙 4개 추가 + S06_SH002 라벨 수정. 음성 테스트 CAUGHT (§3) |
| 중간 | 스키마 FAIL 문서가 상호참조 단계에 들어가 KeyError 로 전체 중단 · cp949 콘솔에서 `–` 포함 메시지 크래시 | `validate.py` | FAIL 문서 제외 · stdout utf-8 재구성 |
| 중간 | 상태 문서 옛 문구 17곳 (D-016 다음 순서 완료, MF DRAFT, 라우터 PENDING, "HIGGSFIELD 8", rights 11/GREEN 5 → 실제 15/GREEN 9, 표준 22 → 27, `02_SOURCES/` 경로 …) | `CURRENT_STATUS.md` `P3_LEDGER_REPORT.md` `OS_INDEX.md` 표준 4개 `BOT_BOOTSTRAP_PROMPT.md` | 갱신 (역사 표기 또는 취소선) |
| 중간 | 데이터: 캐릭터 3건 `approved_by/at` null · `episode.json` note 소진 8.12 (실제 66.12) · DECISIONS D-032/33/34 역순 | 해당 파일 | 기입 · note 정리 · 재정렬 |
| 중간 | 신규 표준 오류: EP01 인물 컷 매핑 (H04=S06_SH002, S07 AI 0) · "11,000점+" 근거 오인 (실제 `CLM_EP01_EXCAV_003` 11,526점) · "56 kings" UNSOURCED · ⑤ 에 BLENDER_FLOW 누락 · ② 필수 vs D-034 EP01 면제 미기재 · G13 치수·색 예외 · 벤치마크 EP01 비율 이중 계산 (53≠49) | STORY_ENGINE_* · DIAGRAM_TEMPLATES · BENCHMARK | 전부 수정 |
| 중간 | `photo_search.py`: `CC-BY-SA-3.0` 하이픈형 → RED 오분류 · PD-US → GREEN 위험 · API error 미처리 · limit>50 무시 | tools | 패턴 확장 · PD-US → YELLOW · 오류 처리 · limit ≤ 50 (16 케이스 회귀 테이블 통과) |
| 낮음 | 일회성 스크립트 30개가 현역 도구와 섞임, `*_record.py` 재실행 시 장부 롤백 위험 | `00_SYSTEM/tools/` | `tools/legacy_20260913/` 로 이동 + 재실행 금지 README (parents[2] 경로가 깨져 실행 자체 불가) |
| 데이터 | D-034 #3 시험 원본 rights 인스턴스 없음 | `rights/` | `RTS_COMMONS_DAEREUNGWON_GAGNON_001` 신설 (GREEN · ACTIVE · CC0, 페이지 원문 proof 저장). **실측 미완** (Commons 원본 서버 429) |

**반박 검수가 기각한 것 (고치지 않음)**: 구 proof HTML 4개 "미참조" (실제 notes 에서 참조) · LOCATION/COSTUME "DRAFT 오도" (실제 DRAFT) · `RTS_GNM_OTHER_OBJECTS_001` YELLOW_ACTIVE (해소됨) · `character_costume` 빈 배열 (무인물 샷 정상) · budget 0 검사 · HTML 스냅샷 (D-012 의도) · concept-bible 중복 (보존 원본).

## 2. 데이터 정합성 (R4, 전부 계산)

파이프라인 분포 49 / 425초 · 라우터 46/3 · 크레딧 66.12 = cost = generation 34건 · approval 초과 0 · D-030 위임 사용 0/20 · 마스터팩 16슬롯 파일 존재 · 사실·hedge 위반 0 · 경로 80/80 존재 → **MATCH**. 불일치는 위 표의 "데이터" 3건뿐.

## 3. 검증기 테스트

| 테스트 | 결과 |
|---|---|
| 양성: S02_SH001 을 AI_STILL + `photo_ai`(Gagnon GREEN) + 라벨로 바꾼 임시 샷 | photo_ai 오류 **0** (남은 오류는 라우터 미OVERRIDE 뿐 — 시험 직전 절차) |
| 음성: INTERPRETIVE 샷 라벨 축소 + HIGGSFIELD 파이프라인 | "INTERPRETIVE RECONSTRUCTION 필수" · "EP01 HIGGSFIELD 잠금" **CAUGHT** |
| 어제 음성 (YELLOW 원본 · 미존재 rights · 라벨 없음 · 미존재 prompt) | 여전히 CAUGHT |
| 회귀 | 336/336 PASS, 상호참조 OK |

## 4. 사용자 결정 필요 (B, 반박 검수 권고 포함)

1. **PRESENT lock 쌍 신설** (`DDABONG_GLOBAL_PRESENT_V01` + `DDABONG_NEGATIVE_PRESENT_V01`) — 없으면 파이프라인 A 프롬프트를 저장할 수 없다. 권고: 승인.
2. present-day 라벨 문구 `AI Visual Reconstruction (present-day, photo-based)` 확정 + `shot.schema` description · G09 갱신. 권고: 채택.
3. D-028 `I2V_MOTION` 정의를 "사진→영상 (인물·풍경)" 으로 확장 (풍경 I2V 도 FLOW_VEO 로 가려면 필요). 권고: 확장.
4. D-034 #3 시험 절차 확인: S02_SH001 라우터 OVERRIDDEN (note) + pipeline AI_STILL + logical/provider/model + ai_label + photo_ai → 그 뒤 prompt 저장 → approval → 전송. D-032 의 S02_SH001 "시간 남으면 촬영" 은 병행 유지. 권고: 이대로.
5. `approval.money_gate_presented.expected_attempts/prompt_ids` required 승격 + AI 샷 `duration ≤ 6` 규칙 (스키마 변경). 권고: 승인.
6. D-030 위임 누적 추적을 위해 approval 에 `delegated: true` 필드 (스키마 변경). 권고: 승인.
7. `CAMERA_GRAMMAR.md` 에 기본값 (35 mm · 1.6 m · tilt 0°) 명시. 권고: 승인.
8. 표준 3개 (STORY_ENGINE · PHOTO_AI · DIAGRAM_TEMPLATES) DRAFT → ACTIVE (D-034 #4 조건 = 이 검수 통과). PHOTO_AI 는 B-1 전까지 "ACTIVE (A4 보류)". 권고: 승인.

## 5. 남은 것 (오늘 범위 밖)
Gagnon 원본 실측 (429 재시도) · KOGL `LicenseShortName` 실값 1건 확인 · e뮤지엄·공유마당 탐색 자동화 · GT-0x Blender 템플릿 · NARRATION 4단계 ↔ 7단계 대응표 · ep01-visual-assets md/html 갈라짐 확인.
