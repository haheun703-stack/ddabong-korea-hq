# SCHEMAS — DDABONG STUDIO OS v0.1 데이터 스키마

> JSON Schema draft-07. 출처: `BOT_HANDOFF_DDABONG_STUDIO_OS_V0.1.md` §4 데이터 모델 · §5 · §6 · §7 · §8 · §10 · §11 · §18 + `아스트라_인수인계_AI유튜브운영.md` §5 7-record.
> 검증: `python 00_SYSTEM/schemas/validate.py` (examples/ 전부 + `02_SEASONS/*/*/episode.json`). 새 인스턴스는 `$schema` 필드로 스키마를 가리키거나 파일명을 `<schema>_…json` 으로 짓는다.
> `examples/*_TEMPLATE.json` 은 **EP001_HWANGNYONGSA 템플릿 ID만** 사용한다. 활성 EP01 데이터가 아니다.

---

## 계층 · 공유 엔티티 (정본 §4)

```
PROJECT → SEASON → EPISODE → SCENE → SHOT → VERSION
```

| 스키마 | 역할 | 정본 § |
|---|---|---|
| `season` `episode` `scene` `shot` | 제작 계층. SHOT = 최소 운영 단위 | §4 §12 §19 |
| `character` `costume` `location` `era` `master_frame` | Continuity Engine 엔티티 | §5 §6 |
| `source` `fact` `rights` `license` `asset` | Source / Rights Ledger | §9 §10 |
| `prompt` `camera` `router_decision` | 프롬프트 조립 · Blender 입력 · 라우터 출력 | §6 §7 §8 |
| `generation` `cost` `approval` `keep_change_patch` | 실행 · Money Gate · 승인 · 부분 수정 | §5 §11 §13 |
| `case_memory` `failure_memory` `performance_memory` `standard_version` `evaluation` | Experience Learning Engine | §18 |
| `music` `voice` `analytics` | 오디오 · 성과 | §16 §2 |

## ID 명명 규칙 (정본 §5 · §8)

| 엔티티 | 패턴 | 예 |
|---|---|---|
| Episode / Scene / Shot | `EP<NN|NNN>` / `EP…_S<NN>` / `EP…_S<NN>_SH<NNN>` | `EP01`, `EP001_S04`, `EP001_S04_SH003` |
| Master frame | `EP…_S<NN>_MASTER_V<NN>` | `EP001_S04_MASTER_V03` |
| Character / Costume / Location | `CHAR_<ERA>_<ROLE>_<NN>` / `COSTUME_<ERA>_<ROLE>_<A><NN>` / `LOC_<PLACE>_V<NN>` | `CHAR_SILLA_OFFICIAL_01`, `COSTUME_SILLA_OFFICIAL_A01`, `LOC_GYEONGJU_BURIAL_SITE_V01` |
| Era | 대문자 스네이크 | `SILLA_EARLY` |
| Prompt lock | `<NAME>_V<NN>` | `DDABONG_GLOBAL_V01`, `DDABONG_DOC_REENACTMENT_V01`, `CAMERA_S004_V02` |
| Source / Claim / Rights | `SRC_…_NNN` / `CLM_…_NNN` / `RTS_…_NNN` | `SRC_NRICH_CHEONMACHONG_001` |
| Generation / Approval / Patch / Case / Failure | `GEN_…_VNN` / `APR_…_NNN` / `PATCH_…_NNN` / `CASE_…_NNN` / `FAIL_…_NNN` | `CASE_DDABONG_CHAR_001` |
| 버전 태그 | `V<NN>` (자산) · `v<major>.<minor>` (표준 문서) | `V03`, `v0.1` |

**활성 EP01 은 두 자리 `EP01`** 을 쓴다 (기존 `episodes/ep01-*` 파일명과 일치). 세 자리 통일 여부는 `DECISIONS.md` P-002.

## 공통 규칙

1. **덮어쓰기 금지** — 승인된 인스턴스는 `version_history` 에 누적하고 새 `V<NN>` 을 만든다. 롤백 가능해야 한다.
2. **미확인은 `null`** — 비용·성과·예산을 모르면 `null`. `0` 은 실제 0일 때만. (아스트라 §5)
3. **실행은 당시 기준을 가리킨다** — `generation.standard_versions`, `case_memory.standard_versions` 에 그때 쓴 표준 문서 버전을 적는다.
4. **사례 1개 ≠ 전역 규칙** — `case_memory` 는 `scope` 와 `exceptions` 를 반드시 채운다. 규칙 승격은 `evaluation` + `standard_version` 을 거친다.
5. **유료 생성 = `approval` 필수** — `generation.approval_id` 가 없는 유료 실행은 규칙 위반.
6. **외부 자산 = `rights_id` 필수** — `status` 가 GREEN/YELLOW 가 아니면 게시 금지.
7. **역사 등급 필수** — 사실·인물·복식·장소·샷 모두 `FACT / PROBABLE / INTERPRETIVE / ARTISTIC` 중 하나.
