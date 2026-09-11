# EP01 SCRIPT_ROUGHCUT_DELTA — 대본 v2 ↔ 러프컷 v1 차이 정리

> D-010 (2026-09-11, 사용자) · 샷/씬 분해는 러프컷 v1 타임라인을 **임시 작업 기준**으로 쓴다. 최종 정본은 아니다.
> **P3 Fact/Source 연결 전에 모든 항목이 `RESOLVED` 여야 한다.**
> 판정 규칙: **내용·사실·해석이 다르면 Script/Fact 우선 · 단순 타이밍·컷 배치 차이면 Rough Cut 우선.**
> 원본: `episodes/ep01-production-script-v2.md` · `episodes/ep01-premiere-roughcut.html`

| ID | 위치 | 대본 v2 | 러프컷 v1 | 차이 종류 | 판정 | 상태 |
|---|---|---|---|---|---|---|
| X1 | `EP01_S02` (0:35–1:25) | "Beneath many of these mounds were wooden burial spaces…" 문장 + G04 단면 그래픽 + 금관 매크로 | 해당 문장·G04·매크로가 이 구간에 없음 (G04 는 S04 에만) | **확인 필요** — 문장이 빠진 것이면 내용, 그래픽 위치만 다르면 배치 | 문장 누락이면 Script 우선 (S02 에 복원). 그래픽 위치만이면 Rough Cut 유지 | OPEN — 러프컷 전체 VO 대조 필요 |
| X2 | `EP01_S03_SH005` | 카드 `OCCUPANT: UNCERTAIN` | 카드 `WHO WAS BURIED HERE? / UNKNOWN WITH CERTAINTY` | 내용 (화면 문구 = 사실 진술) | Script 우선 → `OCCUPANT: UNCERTAIN`. P3 에서 S4 문구와 대조 | RESOLVED (규칙 적용) · P3 확인 |
| X3 | `EP01_S07` (5:20–6:05) | 관람객 실사 컷 + 금관 위치 단면 그래픽 ("고고학적으로 뒷받침될 때만") | 둘 다 없음 | 관람객 컷 = 배치 / 금관 위치 그래픽 = **사실 주장** | 관람객 컷: Rough Cut 유지(생략). 금관 위치 그래픽: S3 로 뒷받침되면 복원, 아니면 제외 | OPEN — P3 에서 S3 확인 |
| X4 | `EP01_S09_SH001` | 클로징에 Higgsfield 공사 플래시 2–3초 | 아카이브·유물·실사 3단 교차 | 배치 (같은 내용을 어떤 자료로 보여줄지) | Rough Cut 우선 → AI 플래시 없음 | RESOLVED |

## 샷 반영 상태

- X2 판정은 아직 샷 JSON 에 반영하지 않았다 (`EP01_S03_SH005.purpose` 는 러프컷 문구). P3 확인 후 한 번에 반영한다.
- X1·X3 가 Script 쪽으로 판정되면 해당 씬에 샷을 추가한다. 샷 ID 는 새 번호로 붙이고 기존 샷은 덮어쓰지 않는다.
