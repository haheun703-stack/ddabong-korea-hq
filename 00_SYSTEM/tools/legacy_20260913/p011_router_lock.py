# -*- coding: utf-8 -*-
"""D-024 (2026-09-13): P-011 router lock. 46 ACCEPTED, H01/H03 OVERRIDDEN -> FLOW_VEO, H07 stays OVERRIDDEN (AI_STILL).
Adds FLOW_VEO to shot/router schemas, closes P-011, writes 15_QA/P011_ROUTER_FINAL.md.
Usage:  python 00_SYSTEM/tools/p011_router_lock.py
"""
import json
from collections import Counter
from pathlib import Path

R = Path(__file__).resolve().parents[2]
SH = R / "02_SEASONS/S01/EP01/07_SHOTS"; D = "2026-09-13"; BY = "사용자 (D-024)"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# 1) schemas
for name, keys in (("shot", ["pipeline"]), ("router_decision", ["recommended_pipeline", "fallback_pipeline"])):
    p = R / f"00_SYSTEM/schemas/{name}.schema.json"; s = rd(p)
    for k in keys:
        enum = s["properties"][k]["enum"]
        if "FLOW_VEO" not in enum: enum.insert(enum.index("BLENDER_FLOW") + 1, "FLOW_VEO")
    w(p, s)

# 2) router decisions + shots
OVR = {
 "EP01_S04_SH004": "D-024: H01 목재 준비 — 사람 움직임 중심(70), 공간 정밀도 중간(60), 단일 행동 → Blender 사전 고정 불필요. FLOW_VEO 단독 (S04 master frame 에서 시작).",
 "EP01_S05_SH005": "D-024: H03 부장품 준비 — 손 동작·소품 제스처 중심, 카메라 단순(35), 공간 50 → FLOW_VEO 단독 (시종 Character Pack 참조, master frame 없음).",
}
counts = Counter()
rows = []
for f in sorted(SH.glob("shot_*.json")):
    shot = rd(f); sid = shot["shot_id"]; rp = SH / f"router_decision_RTR_{sid}_V01.json"; r = rd(rp)
    if sid in OVR:
        r["human_decision"] = "OVERRIDDEN"; r["override_note"] = OVR[sid]
        if shot["pipeline"] != "FLOW_VEO":
            shot["pipeline"] = "FLOW_VEO"; shot["notes"] += " D-024: 파이프라인 BLENDER_FLOW → FLOW_VEO (사용자 OVERRIDE)."
            shot["updated_at"] = D; w(f, shot)
    elif sid == "EP01_S08_SH002":
        assert r["human_decision"] == "OVERRIDDEN" and shot["pipeline"] == "AI_STILL"
    else:
        r["human_decision"] = "ACCEPTED"
        assert r["recommended_pipeline"] == shot["pipeline"], sid
    if sid != "EP01_S08_SH002": r["decided_at"] = D; r["decided_by"] = BY
    w(rp, r)
    counts[shot["pipeline"]] += 1
    ai = shot["pipeline"] in ("AI_STILL", "FLOW_VEO", "BLENDER_FLOW", "HIGGSFIELD")
    rows.append(f"| {sid} | {shot['duration']} | {shot['purpose']} | {r['recommended_pipeline']} | **{shot['pipeline']}** | {r['human_decision']} | {'있음' if ai else '없음'} |")
assert counts == Counter({"ARCHIVE": 20, "ORIGINAL_GRAPHIC": 11, "REAL_SHOOT": 10, "BLENDER_FLOW": 4, "FLOW_VEO": 2, "AI_STILL": 2}), counts

# 3) decisions: D-024 + close P-011
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8"); anchor = "\n---\n\n## 승인 대기 (P)"
if "### D-024" not in s:
    s = s.replace(anchor, """
### D-024 · 2026-09-13 · P-011 라우터 49건 최종 잠금 · FLOW_VEO 분류 추가 · EP01 Higgsfield 0건 (사용자)
**확정** 46건 ACCEPTED · `EP01_S04_SH004` H01 · `EP01_S05_SH005` H03 → **FLOW_VEO** (OVERRIDDEN) · `EP01_S08_SH002` H07 AI_STILL 유지 (D-018). 최종 구성 REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 (H02 · H02b · H04 · H05) · FLOW_VEO 2 · AI_STILL 2 (H06 · H07) · **HIGGSFIELD 0**. AI 8컷 45초 (≈11%, 모두 ≤6초).
**EP01 재현 원칙** 공간 위계·규모 → BLENDER_FLOW · 행동 중심·공간 중간 → FLOW_VEO · 저동작 정보 컷 → AI_STILL · 증거 → ARCHIVE · 현재 장소 → REAL_SHOOT · 설명 도식 → ORIGINAL_GRAPHIC. EP01 은 다큐 톤 우선 → **Higgsfield 사용 0건으로 잠금**.
**스키마** shot.pipeline · router_decision.recommended/fallback 에 `FLOW_VEO` 정식 추가 (BLENDER_FLOW 와 독립). 검증기: FLOW_VEO 를 AI 파이프라인으로 취급, 라우터 PENDING 인 샷의 generation 은 FAIL.
**유지 주의** YELLOW_ACTIVE 권리 1건 (`RTS_GNM_OTHER_OBJECTS_001` → S02_SH003 · S05_SH001) 편집 확정 전 해소 필수 (판정과 별개). Flow/Veo 자동 연결 도구 없음 → 라우터만 확정, 실제 생성은 별도 승인 + 별도 Money Gate. Blender 자동화(P7) 전 → 카메라 초안 기준 수작업 허용.
**근거** `02_SEASONS/S01/EP01/15_QA/P011_ROUTER_FINAL.md`
""" + anchor, 1)
s = s.replace("### P-011 · (보류 D-015: AI 샷 직전 승인) 라우터 판정 49건 ACCEPT / OVERRIDE (P4, 2026-09-11)",
              "### ~~P-011~~ · **종결 D-024 (2026-09-13)** · 라우터 판정 49건 ACCEPT / OVERRIDE (P4, 2026-09-11)")
p.write_text(s, encoding="utf-8")

# 4) router standard
p = R / "00_SYSTEM/standards/MODEL_ROUTER.md"; s = p.read_text(encoding="utf-8")
row = "| 고공간정확도 + 고카메라복잡도 | `BLENDER_FLOW` |"
if "`FLOW_VEO`" not in s:
    assert s.count(row) == 1
    s = s.replace(row, row + "\n| 사람 움직임 중심 + 중간 공간 의존 (단일 행동·손 동작) | `FLOW_VEO` (D-024) |")
p.write_text(s, encoding="utf-8")

# 5) status
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [
 ("- **P-011** 라우터 판정 49건 ACCEPT / OVERRIDE — **AI 샷 생성 직전 최종 승인으로 보류 (D-015)**.",
  "- ~~P-011~~ **라우터 49건 잠금 (D-024)**: 46 ACCEPTED · H01·H03 → FLOW_VEO · H07 AI_STILL · **EP01 Higgsfield 0건**. 실제 AI 생성은 별도 승인 + Money Gate."),
 ("다음 유료는 AI 샷 (P-011 ACCEPT + master_frame 승인 뒤). AI 샷은 P-011 ACCEPT + `CHARACTER_MASTER_APPROVED` + master_frame APPROVED 뒤.",
  "라우터 잠금 (D-024). 다음 유료는 Master Frame S04 · S06 → AI 샷 (Flow/Veo 는 별도 비용 게이트)."),
 ("## P4 — Shot Router (2026-09-11 · DONE, 사용자 ACCEPT 대기 P-011)", "## P4 — Shot Router (2026-09-11 · DONE · **최종 잠금 D-024 2026-09-13**)"),
 ("| 최종 구성 | REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 6 · AI_STILL 1 · HIGGSFIELD 1 | — |",
  "| 최종 구성 (D-024) | REAL 10 · ARCHIVE 20 · GRAPHIC 11 · BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · **HIGGSFIELD 0** | 46 ACCEPTED · 3 OVERRIDDEN (H01 · H03 · H07) · `15_QA/P011_ROUTER_FINAL.md` |"),
 ("| DONE (P4) · ACCEPT 대기 P-011 |", "| DONE (P4) · **잠금 D-024** |"),
 ("| HIGGSFIELD | `ep01-higgsfield-prompts` 7컷 | 프롬프트 APPROVED · Money Gate OPEN (D-015) · 원로 Master Pack 배치 1만 생성, **AI 샷 생성은 P-011 ACCEPT + Character Master 승인 뒤** |",
  "| AI 재현 | legacy `ep01-higgsfield-prompts` 7컷 → 라우터 D-024: BLENDER_FLOW 4 · FLOW_VEO 2 · AI_STILL 2 · Higgsfield 0 | Character Master 승인 완료 (D-023) · 다음 Master Frame S04 · S06 → AI 샷 (별도 승인) |"),
]:
    s = s.replace(a, b)
if "D-024." not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-024.** P-011 종결: 라우터 49건 잠금 (46 ACCEPTED · H01 · H03 → FLOW_VEO · H07 AI_STILL), `FLOW_VEO` 스키마 추가, **EP01 Higgsfield 0건**. 검증기: 라우터 PENDING 샷 generation FAIL.\n", 1)
p.write_text(s, encoding="utf-8")

# 6) report
(R / "02_SEASONS/S01/EP01/15_QA/P011_ROUTER_FINAL.md").write_text(f"""# P-011 라우터 최종 잠금 — D-024

> 2026-09-13 · 사용자 승인 · 스크립트 `00_SYSTEM/tools/p011_router_lock.py`

## 결과

| 파이프라인 | P4 판정 | 최종 (D-024) |
|---|---|---|
| REAL_SHOOT | 10 | 10 |
| ARCHIVE | 20 | 20 |
| ORIGINAL_GRAPHIC | 11 | 11 |
| BLENDER_FLOW | 6 | **4** (H02 · H02b · H04 · H05) |
| FLOW_VEO | — | **2** (H01 · H03) |
| AI_STILL | 1 | **2** (H06 · H07) |
| HIGGSFIELD | 1 | **0 (EP01 잠금)** |

46 ACCEPTED · 3 OVERRIDDEN. AI 8컷 45초 (≈11%, 모두 ≤6초).

## EP01 재현 원칙

- 공간 위계·규모 중요 → **BLENDER_FLOW**
- 행동 중심, 공간 중간 → **FLOW_VEO**
- 움직임 적은 정보 컷 → **AI_STILL**
- 증거 중심 → **ARCHIVE**
- 현재 장소 → **REAL_SHOOT**
- 설명 도식 → **ORIGINAL_GRAPHIC**
- 극단 카메라·과장된 reveal 이 핵심이 아닌 다큐 톤 → **Higgsfield 0건**

## 변경 2건

- `EP01_S04_SH004` H01 목재 준비: BLENDER_FLOW → **FLOW_VEO** — 사람 움직임 중심, 공간 정밀도 중간, 단일 행동.
- `EP01_S05_SH005` H03 부장품 준비: BLENDER_FLOW → **FLOW_VEO** — 손 동작·소품 제스처 중심, 카메라 단순.

## 주의 (판정과 별개)

1. YELLOW_ACTIVE 권리 `RTS_GNM_OTHER_OBJECTS_001` (S02_SH003 · S05_SH001) — 편집 확정 전 해소 필수.
2. Flow/Veo 자동 연결 도구 없음 — 실제 생성은 별도 승인 + 별도 Money Gate (크레딧 체계 다름).
3. Blender 자동화(P7) 전 — BLENDER_FLOW 4건은 `10_BLENDER/camera_*` 초안 기준 수작업 허용.
4. 의존성: Master Frame S04 (H01 · H02 · H02b) · S06 (H04 · H05 · H06), H07 은 SH003 실사 구도 뒤.

## 49건

| Shot | 초 | 목적 | 라우터 권고 | 최종 | 사람 판정 | AI 비용 |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n", encoding="utf-8")
print(dict(counts))
