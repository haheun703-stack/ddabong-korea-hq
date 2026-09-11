# EP01 P4 Shot Router — 판정 리포트

> 생성 2026-09-11 · Visual Router (Claude Code) · 스크립트 출력 (재생성). 규칙: 정본 §6 §7 + 감독 기준 (D-014). `human_decision = PENDING` — 사용자 ACCEPT/OVERRIDE 대기.

## 요약

- 49 샷 라우팅: AI_STILL 1 · ARCHIVE 20 · BLENDER_FLOW 6 · HIGGSFIELD 1 · ORIGINAL_GRAPHIC 11 · REAL_SHOOT 10
- 파이프라인 변경 7건 (legacy Higgsfield 8 → HIGGSFIELD 1 · BLENDER_FLOW 6 · AI_STILL 1)
- 유료 생성 0 (라우팅은 판정만). Money Gate 여전히 UNKNOWN_BUDGET.

## 재판정 — 역사 재현 8컷 (왜 Higgsfield 가 아닌가)

| shot | 컷 | 이전 | 판정 | fallback | 규칙 | 이유 |
|---|---|---|---|---|---|---|
| `EP01_S04_SH004` | H01 | HIGGSFIELD | **BLENDER_FLOW** | HIGGSFIELD | Human motion + natural movement (carrying, ritual preparation, looking) → FLOW/VEO (Blender previz for scale) | H01 목재 준비: 노동 동작 중심(human_motion 70), 카메라는 느린 측면 트래킹. 공간 의존 중간(60). 자연스러운 손·몸 움직임이 핵심이라 Flow/Veo. Blender 는 작업장 스케일 previz 만. |
| `EP01_S04_SH005` | H02 | HIGGSFIELD | **BLENDER_FLOW** | HIGGSFIELD | High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO | H02 돌 운반: 봉분 일부 형성 상태의 공간 관계(70) + 와이드→손 푸시인(55) + 반복 운반 동작(75). 공간·카메라·동작 모두 → Blender 공간 lock 후 Flow/Veo. |
| `EP01_S04_SH006` | H02 wide | HIGGSFIELD | **BLENDER_FLOW** | AI_STILL | High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO | H02 조직된 작업 와이드: 공간 정확도 75, 정적 와이드. SH005 와 같은 Blender 씬에서 카메라만 바꿔 뽑는다 → 유료 호출 절감. 실패 시 Blender 키프레임 AI_STILL + 미세 모션. |
| `EP01_S05_SH005` | H03 | HIGGSFIELD | **BLENDER_FLOW** | AI_STILL | Human motion + natural movement (carrying, ritual preparation, looking) → FLOW/VEO (Blender previz for scale) | H03 부장품 준비: 손·천·금속 클로즈업, 얕은 심도. 공간 의존 낮음(50) 이라 Blender previz 생략 가능, 승인 키프레임 → Flow/Veo 직행. 4초라 AI_STILL + 켄번스로도 대체 가능. |
| `EP01_S06_SH002` | H04 | HIGGSFIELD | **BLENDER_FLOW** | HIGGSFIELD | High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO | H04 장례 준비 와이드: 역할별 배치(공간 80) + 반복 인물 원로 등장 → master_frame 필수, 인물 연속성 critical. 정적 와이드 + 전경 미세 움직임 → Blender 배치 lock → Flow/Veo reference-driven. |
| `EP01_S06_SH005` | H05 | HIGGSFIELD | **BLENDER_FLOW** | HIGGSFIELD | High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO | H05 관찰자 시점: 공간 85 + 카메라 60(관찰자 뒤 느린 전진) + 원로 뒷모습 연속성. 에피소드 핵심 컷(visual 100) 이라 공간·인물 lock 이 우선 → Blender → Flow/Veo. 극단 카메라가 아니므로 Higgsfield 는 fallback. |
| `EP01_S06_SH010` | H06 | HIGGSFIELD | **AI_STILL** | BLENDER_FLOW | Low motion + high factual density (historical reconstruction) → AI_STILL | H06 완성 봉분 와이드: 움직임 거의 없음(20), 정보량(스케일 47 m/12.7 m) 높음, 정적 와이드 → AI_STILL. Blender 로 봉분 스케일·소그룹 위치 lock 한 키프레임을 생성 기준으로. 미세 카메라 필요 시 BLENDER_FLOW. |
| `EP01_S08_SH002` | H07 | HIGGSFIELD | **HIGGSFIELD** | AI_STILL | Strong reveal / extreme camera / past-to-present match cut → HIGGSFIELD | H07 과거→현재 매치컷: 정본 §6 Higgsfield 용도(past-to-present match cut). 카메라 고정이지만 특수 전환 컷. 실사 착지 구도(SH003) 촬영 후 그 구도에 맞춰 생성. 정지 프레임이면 AI_STILL 로 충분. |

## 전체 판정

| shot | pipeline | fallback | continuity | historical | confidence | risk |
|---|---|---|---|---|---|---|
| EP01_S01_SH001 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S01_SH002 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S01_SH003 | ORIGINAL_GRAPHIC | — | LOW | MEDIUM | FACT | LOW |
| EP01_S01_SH004 | ORIGINAL_GRAPHIC | — | LOW | MEDIUM | FACT | LOW |
| EP01_S02_SH001 | REAL_SHOOT | — | LOW | MEDIUM | FACT | LOW |
| EP01_S02_SH002 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S02_SH003 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S03_SH001 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S03_SH002 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S03_SH003 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S03_SH004 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S03_SH005 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S04_SH001 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S04_SH002 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S04_SH003 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S04_SH004 | BLENDER_FLOW | HIGGSFIELD | MEDIUM | MEDIUM | PROBABLE | MEDIUM |
| EP01_S04_SH005 | BLENDER_FLOW | HIGGSFIELD | MEDIUM | MEDIUM | PROBABLE | MEDIUM |
| EP01_S04_SH006 | BLENDER_FLOW | AI_STILL | MEDIUM | MEDIUM | PROBABLE | MEDIUM |
| EP01_S04_SH007 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S05_SH001 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S05_SH002 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S05_SH003 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S05_SH004 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S05_SH005 | BLENDER_FLOW | AI_STILL | MEDIUM | MEDIUM | PROBABLE | MEDIUM |
| EP01_S05_SH006 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S06_SH001 | ORIGINAL_GRAPHIC | — | LOW | LOW | FACT | LOW |
| EP01_S06_SH002 | BLENDER_FLOW | HIGGSFIELD | HIGH | MEDIUM | INTERPRETIVE | HIGH |
| EP01_S06_SH003 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S06_SH004 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S06_SH005 | BLENDER_FLOW | HIGGSFIELD | HIGH | MEDIUM | INTERPRETIVE | HIGH |
| EP01_S06_SH006 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S06_SH007 | REAL_SHOOT | — | LOW | LOW | INTERPRETIVE | LOW |
| EP01_S06_SH008 | ORIGINAL_GRAPHIC | — | LOW | LOW | FACT | LOW |
| EP01_S06_SH009 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S06_SH010 | AI_STILL | BLENDER_FLOW | MEDIUM | MEDIUM | PROBABLE | MEDIUM |
| EP01_S06_SH011 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S07_SH001 | ARCHIVE | — | LOW | HIGH | FACT | LOW |
| EP01_S07_SH002 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S07_SH003 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S07_SH004 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S07_SH005 | ORIGINAL_GRAPHIC | — | LOW | HIGH | FACT | LOW |
| EP01_S08_SH001 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S08_SH002 | HIGGSFIELD | AI_STILL | HIGH | MEDIUM | PROBABLE | HIGH |
| EP01_S08_SH003 | REAL_SHOOT | — | HIGH | LOW | FACT | LOW |
| EP01_S09_SH001 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S09_SH002 | ARCHIVE | — | LOW | MEDIUM | FACT | LOW |
| EP01_S09_SH003 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S09_SH004 | REAL_SHOOT | — | LOW | LOW | FACT | LOW |
| EP01_S09_SH005 | ORIGINAL_GRAPHIC | — | LOW | LOW | FACT | LOW |

## 권리 등급 (D-014)

- GREEN → 사용 가능 · YELLOW_ACTIVE → 실제 샷 연결, 편집 전 해결 필수 · YELLOW_BACKUP → 대체 가능, 실제 사용 시에만 해결 · RED → 금지
- **YELLOW_ACTIVE 1건**: `RTS_GNM_OTHER_OBJECTS_001` (EP01_S02_SH003, EP01_S05_SH001) — 박물관 소장품 페이지별 KOGL 유형 확인 후 GREEN 분리 또는 컷 제외.
- YELLOW_BACKUP 3건: 경주시 이미지 · Wikimedia 대릉원 · Wikimedia 천마총 입구 (자체 촬영 확보 시 미사용).

## 다음

- 사용자: 라우터 판정 ACCEPT / OVERRIDE (특히 H05 — Higgsfield 유지 여부).
- P2 Character Master (원로 FULL + 군중 LITE) → master_frame S04·S06 → 그 뒤에만 유료 생성.
- Blender 브리지(P7) 전까지 `camera.json` 은 수동.
