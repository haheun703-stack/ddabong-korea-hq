# -*- coding: utf-8 -*-
"""D-031: owner final image OK for H06 (EP01_S06_SH010) attempt 3 (GEN_EP01_S06_SH010_HIGGSFIELD_V03, job 4cc87427).
Shot -> LOOK_APPROVED, approved_version V03, version_history V01..V03; generation/approval notes; DECISIONS + CURRENT_STATUS.
No generation. Idempotent.  Usage: python 00_SYSTEM/tools/d031_h06_ok.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
BY = "사용자"; MARK = "D-031"
AS = "08_GENERATION_CACHE/EP01/AI_STILL/"

f = EP / "07_SHOTS/shot_EP01_S06_SH010.json"; s = rd(f)
for p in ("H06_V01_0f250ab3.png", "H06_V02_d6326541.png", "H06_V03_4cc87427.png"):
    assert (R / AS / p).exists(), p
s["status"] = "LOOK_APPROVED"; s["approved_version"] = "V03"; s["updated_at"] = D; s["updated_by"] = "Claude Code (D-031 기록, 판정 사용자)"
s["version_history"] = [
    {"version": "V01", "stage": "STILL", "status": "REJECTED", "created_at": D, "created_by": "Image Generation Agent (Claude Code)", "path": AS + "H06_V01_0f250ab3.png",
     "note": "GEN_EP01_S06_SH010_HIGGSFIELD_V01 · prompt V02 · 봉분 비율 2.3:1, 지평선 전봇대·건물"},
    {"version": "V02", "stage": "STILL", "status": "PREVIOUS", "created_at": D, "created_by": "Image Generation Agent (Claude Code)", "path": AS + "H06_V02_d6326541.png",
     "note": "GEN_EP01_S06_SH010_HIGGSFIELD_V02 · prompt V03 · PARTIAL: 사람 규모 1/4, 평평한 꼭대기"},
    {"version": "V03", "stage": "STILL", "status": "APPROVED", "created_at": D, "created_by": BY, "path": AS + "H06_V03_4cc87427.png",
     "note": "GEN_EP01_S06_SH010_HIGGSFIELD_V03 · prompt V04 · D-031 사용자 최종 OK ('H06 OK'). 남은 작은 점: 사람 규모 약 1/5–1/6 (목표 1/8), 먼 인물 옷 일부 현대적 → 수용."},
]
if MARK not in s["notes"]:
    s["notes"] += " D-031: 사진 V03 (H06_V03_4cc87427.png) 사용자 최종 OK → LOOK_APPROVED. 편집에서 느린 줌 가능 (AI_SHOT_PLAN)."
w(f, s)

g = C / "generation_GEN_EP01_S06_SH010_HIGGSFIELD_V03.json"; d = rd(g)
d["notes"] = d["notes"].replace("Approval cap reached; owner final OK pending.", "Approval cap reached.")
if MARK not in d["notes"]:
    d["notes"] += " D-031 (2026-09-13): owner final OK ('H06 OK') -> shot LOOK_APPROVED, approved_version V03; remaining minor scale/costume points accepted."
w(g, d)
a = C / "approval_APR_EP01_AI_B1_002.json"; d = rd(a)
d["note"] = d["note"].replace("1/1 사용 (SUCCESS, 사용자 최종 OK 대기).", "1/1 사용 (SUCCESS, D-031 사용자 최종 OK).")
w(a, d)

p = R / "00_SYSTEM/DECISIONS.md"; t = p.read_text(encoding="utf-8")
if "### D-031" not in t:
    anchor = "위임 호출도 approval 기록을 남기고 `decided_by = 봇 (D-030 위임)` 으로 표기.\n"
    assert t.count(anchor) == 1
    t = t.replace(anchor, anchor + "\n### D-031 · 2026-09-13 · H06 사진 최종 OK (사용자 \"H06 OK\")\n"
        "**결정** `EP01_S06_SH010` (H06) 사진 **V03** (`08_GENERATION_CACHE/EP01/AI_STILL/H06_V03_4cc87427.png`, `GEN_EP01_S06_SH010_HIGGSFIELD_V03`) 승인 → 샷 `LOOK_APPROVED`, `approved_version = V03`.\n"
        "**수용한 작은 점** 사람 규모 약 1/5–1/6 (목표 1/8), 먼 인물 옷 일부 현대적. H06 총 3 호출 / 6 credits, 추가 호출 없음.\n", 1)
    p.write_text(t, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; t = p.read_text(encoding="utf-8")
if "D-031" not in t:
    t = t.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-031.** H06 사진 V03 최종 OK → `EP01_S06_SH010` LOOK_APPROVED (approved_version V03). 추가 생성 없음, EP01 소진 66.12 credits 그대로.\n", 1)
    p.write_text(t, encoding="utf-8")

p = EP / "15_QA/AI_SHOT_PLAN_EP01.md"; t = p.read_text(encoding="utf-8")
if "D-031" not in t:
    t += "\n## 진행 기록\n\n- 2026-09-13 **D-031**: 배치 1 H06 사진 완료 — V03 사용자 최종 OK (3 호출 / 6 credits). 다음 AI 샷은 영상 승인 (P-012 실제 청구액) 뒤.\n"
    p.write_text(t, encoding="utf-8")
print("D-031 recorded")
