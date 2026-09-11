# EP01 Character Master Pack 요구 목록

> P1 Continuity Engine 산출 · 2026-09-11 · Claude Code
> 근거: 정본 §5 (Master Pack 10종, `CHARACTER_MASTER_APPROVED` 전 유료 비디오 생성 금지), D-004 (스타일 B Documentary Reenactment)
> **이 문서는 요구 목록일 뿐이다. 생성은 Money Gate(P-001 예산) 승인 후 P2 에서 진행한다.**

---

## 1. 누가 어느 샷에 나오나

| character_id | 역할 | 등장 샷 (Higgsfield 팩) | 얼굴 노출 |
|---|---|---|---|
| `CHAR_SILLA_ELITE_OBSERVER_01` | 장례를 지켜보는 원로 (피장자·왕 아님) | `EP01_S06_SH002` (H04), `EP01_S06_SH003` (H05) | H04 원경 / H05 **뒷모습** |
| `CHAR_SILLA_LABORER_GROUP_01` | 봉분 조성 노동자 무리 | `EP01_S04_SH004`–`SH006` (H01·H02), `EP01_S06_SH002`–`SH003` 배경 | 군중, 개별 얼굴 반복 없음 |
| `CHAR_SILLA_ATTENDANT_GROUP_01` | 시종·장인 무리 | `EP01_S05_SH005` (H03), `EP01_S06_SH002`·`SH003`·`SH006` | H03 손 위주 / H06 원경 |

H07 (`EP01_S08_SH002`) 은 인물이 없다.

## 2. 인물별 Master Pack

### CHAR_SILLA_ELITE_OBSERVER_01 — 10종 전부 필수 (정본 §5)

| 슬롯 | 요구 사항 | EP01 에서 특히 중요한 이유 |
|---|---|---|
| hero | 스타일 B 기준 대표 초상. A 수준 연출은 썸네일용일 때만 | 기준 얼굴 |
| front | 정면, 무표정, 자연광 | 얼굴 ID 고정 |
| three_quarter_left / right | 3/4 좌·우 | H04 원경 각도 |
| profile | 측면 | 관모 실루엣 |
| full_body | 전신, 복식 전체 | 키·비율 고정 (`height_ratio`) |
| neutral_standing | 가만히 선 자세 | H04·H05 모두 서서 지켜봄 |
| walking | 걷는 자세 | H05 는 카메라가 뒤에서 전진 — 인물은 거의 정지, 우선순위 낮음 |
| costume_detail | 허리띠·깃·관모 디테일 | 금관·금허리띠 복제 금지 확인용 |
| expression_sheet | 절제된 표정 3–5종 | 감정 연기 클로즈업 금지 규칙 준수 확인 |

**추가 요구 (정본 슬롯 밖, P-005 와 함께 결정)**: H05 는 관찰자 뒤에서 찍는다. 그래서 **뒷모습 / 어깨 너머 시점** 레퍼런스가 사실상 가장 중요하다. 슬롯 추가 여부는 스키마 변경이라 사용자 승인이 필요하다.

### CHAR_SILLA_LABORER_GROUP_01 · CHAR_SILLA_ATTENDANT_GROUP_01 — 축소 제안 (P-005)

군중은 얼굴이 반복되지 않고, 연속성은 **복식·체형·도구**로 유지된다. 제안:

| 슬롯 | 노동자 | 시종·장인 |
|---|---|---|
| full_body | 필수 (체형 3–4종) | 필수 |
| walking | 필수 (짐 운반 동작) | 선택 |
| costume_detail | 필수 | 필수 (손·소매 — H03) |
| 나머지 7종 | 생략 (`MISSING` 유지, 군중 예외로 기록) | 생략 |

결정 전까지 스키마상 10종 모두 `MISSING` 이며 `CHARACTER_MASTER_APPROVED` 는 불가하다.

## 3. 선행 조건 (생성 전에 끝나야 함)

1. **복식 Historical QA** — `COSTUME_SILLA_*_A01` 의 TBD 항목 (여밈·깃·관모·신발) 을 근거 자료로 채운다. 근거 없이 Master Pack 을 만들면 전부 다시 만들게 된다 (Rule 3).
2. **P-001 예산** — Money Gate 가 `UNKNOWN_BUDGET` 인 동안 유료 생성 잠금.
3. **P-005 군중 예외** 결정.
4. S04·S06 **master_frame** 은 Master Pack 승인 뒤 (P2).

## 4. 예상 생성 규모 (참고, 비용 산정은 P6)

- 원로 10종 (+ 뒷모습 1–2종 제안)
- 군중 축소안 채택 시: 노동자 3종 × 체형 변형 + 시종 2종 ≈ 8–10장
- 채택하지 않으면: 3명 × 10종 = 30장
