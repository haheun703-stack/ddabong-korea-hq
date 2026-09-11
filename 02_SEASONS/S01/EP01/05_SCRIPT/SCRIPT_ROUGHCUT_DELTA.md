# EP01 SCRIPT_ROUGHCUT_DELTA — 대본 v2 ↔ 러프컷 v1 차이 정리

> D-010 (2026-09-11, 사용자) · 샷/씬 분해는 러프컷 v1 타임라인을 **임시 작업 기준**으로 쓴다. 최종 정본은 아니다.
> 판정 규칙: **내용·사실·해석이 다르면 Script/Fact 우선 · 단순 타이밍·컷 배치 차이면 Rough Cut 우선.**
> 원본: `episodes/ep01-production-script-v2.md` · `episodes/ep01-premiere-roughcut.html`
> **상태: 4/4 RESOLVED (2026-09-11) → P3 진입 가능.**

| ID | 위치 | 대본 v2 | 러프컷 v1 | 차이 종류 | 판정 | 반영 |
|---|---|---|---|---|---|---|
| X1 | `EP01_S02` (0:35–1:25) | "Beneath many of these mounds…" 문장 + G04 단면 + 금관 매크로 | 행마다 첫 문장만 표기, G04 는 2:15 에만 | 내레이션 = 표기 생략(내용 아님) / G04 위치 = 배치 | 내레이션은 대본 v2 전문 그대로. G04 는 S04 에서만 (Rough Cut). 금관 매크로 = S02_SH003 몽타주 첫 컷 | `scene_EP01_S02` · `shot_EP01_S02_SH003` notes |
| X2 | `EP01_S03_SH005` | 카드 `OCCUPANT: UNCERTAIN` | `WHO WAS BURIED HERE? / UNKNOWN WITH CERTAINTY` | 내용 (화면 문구 = 사실 진술) | Script 우선 → `OCCUPANT: UNCERTAIN`, 러프컷 문구는 보조 | `shot_EP01_S03_SH005.purpose` |
| X3 | `EP01_S07` (5:20–6:05) | 관람객 실사 컷 + 금관 위치 단면 ("고고학적으로 뒷받침될 때만") | 둘 다 없음 | 관람객 컷 = 배치 / 금관 위치 = **사실 주장** | 관람객 컷: 생략 유지 (S08 에 있음). 금관 위치: **S4 로 뒷받침됨** (피장자 머리 동쪽, 금관 착용, 머리맡 부장궤 T자) → 복원 | 신규 `shot_EP01_S07_SH005` G13 (3초, 5:42–5:45), `SH002` 7→4초. `CLM_CHEONMACHONG_LAYOUT_001` + 출처 2건 |
| X4 | `EP01_S09_SH001` | 클로징 Higgsfield 공사 플래시 2–3초 | 아카이브·유물·실사 3단 교차 | 배치 | Rough Cut 우선 → AI 플래시 없음 | 변경 없음 |

## 후속

- **G13** 은 legacy `ep01-graphics-spec.html` (G01–G12) 에 없다. legacy 문서는 수정하지 않으므로 graphics-spec **v2** 를 만들 때 G13 을 추가한다 (백로그).
- 러프컷 v1 의 시간 배분은 내레이션 녹음 후 어차피 재조정된다. 총 길이 425초는 유지.
