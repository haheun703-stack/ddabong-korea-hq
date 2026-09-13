# -*- coding: utf-8 -*-
"""Record master-frame FIX edits (jobs da44103f S04 PARTIAL, de2b6a3e S06 OPEN_CHAMBER SUCCESS) and save S04 V03
(fresh generation with explicit full-frame + wood-only wording) + PATCH_MF_EP01_S04_002 BEFORE sending (D-016).
Usage:  python 00_SYSTEM/tools/mf_v02_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOBS = [
 ("EP01_S04_MASTER_V01", "da44103f-e79a-4bbb-8515-b4995e7069e5", ["4de7af1f-490d-4b33-94c7-8c0f8309e478"], "PARTIAL", "PATCH_MF_EP01_S04_001",
  "Bot check PARTIAL: black letterbox bars still present top and bottom; some tools became wooden (hoe/pole) but a metal-bladed spade, a metal spade at right and the saw remain. Edit loop stopped (same lesson as attendant full_body) -> fresh generation V03 proposed."),
 ("EP01_S06_MASTER_OPEN_CHAMBER_V01", "de2b6a3e-106b-41a1-81ac-8cee206fee6b", ["80d2d3db-44cd-4d01-8b50-76048154c458", "5681f1e0-fe07-4fc3-b36c-f512dc7a2992"], "SUCCESS", "PATCH_MF_EP01_S06_OPEN_CHAMBER_001",
  "Bot check PASS: coffin is now a plain straight-sided rectangular box with flat lid; observer belt now bronze plaques with small hanging pendants; everything else unchanged (chest position/hardware untouched per owner scope)."),
]
gids = []
for frame, job, inputs, status, patch, check in JOBS:
    pid = f"PRM_MF_{frame[:-4]}_V02"; sent = rd(EP / f"11_AI_STILLS/prompt_{pid}.json")["assembled_text"]
    jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{job}.json"
    w(R / jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
               "created_at": f"{D}T06:31:58Z",
               "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1,
                          "input_images": [{"id": i, "type": "image_job"} for i in inputs], "prompt": sent},
               "retrieved_at": D, "note": "generate_image_batch/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V02)."})
    gid = f"GEN_MF_{frame[:-4]}_HIGGSFIELD_V02"; gids.append(gid)
    out = f"08_GENERATION_CACHE/EP01/MF/MF_{frame[:-4]}_V02_{job[:8]}.png"
    prev = f"08_GENERATION_CACHE/EP01/MF/MF_{frame}_{inputs[0][:8]}.png"
    w(C / f"generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_FRAME:{frame}", "stage": "STILL", "provider": "Higgsfield",
        "model": f"Nano Banana Pro (job_set_type nano_banana_2, 2k, 16:9, edit of job {inputs[0][:8]})",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": "V02",
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MF_001",
        "input_paths": [prev], "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0,
                 "note": f"Higgsfield job {job}. Balance 1872.48 -> 1866.48 (-6) over this pair; transactions show an extra Nano Banana Pro -2 at 06:31:23Z not sent by this session (shared account, D-018) - not counted in EP01."},
        "result_status": status, "failure_id": None, "started_at": f"{D}T06:31:58Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"FIX edit ({patch}, owner OK 2026-09-13). {check}"})
    pt = rd(C / f"keep_change_patch_{patch}.json"); pt["resulting_generation_id"] = gid; w(C / f"keep_change_patch_{patch}.json", pt)
    if status == "SUCCESS":
        mf = EP / f"07_SHOTS/master_frame_{frame}.json"; d = rd(mf); d["path"] = out; d["generation_id"] = gid; d["status"] = "DRAFT"; d["updated_at"] = D; w(mf, d)

v1 = rd(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V01.json"); v2 = rd(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V02.json")
t = v1["assembled_text"]
a1 = "One wide cinematic establishing frame, 16:9, a single still image."
a2 = "Tools only: straw baskets, rope, wooden poles and wooden spades."
assert t.count(a1) == 1 and t.count(a2) == 1
t = t.replace(a1, "One wide establishing documentary photograph that fills the entire 16:9 frame edge to edge, a single still image; no black bars, no letterbox, no borders.")
t = t.replace(a2, "Tools only: straw baskets, rope, wooden poles, wooden mallets and all-wooden spades. Every tool is made entirely of wood: no metal blades, no metal heads, no saws, no pick-axes, no hoes.")
v3 = dict(v2)
v3.update(prompt_id="PRM_MF_EP01_S04_MASTER_V03", version="V03", parent_prompt_id="PRM_MF_EP01_S04_MASTER_V02", patch_id="PATCH_MF_EP01_S04_002",
          assembled_text=t, reference_images=["character_pack:CHAR_SILLA_LABORER_GROUP_01"],
          shot_delta="S04 master frame fresh generation: V01 text + full-frame (no letterbox) + wood-only tools",
          created_at=D, created_by="Image Generation Agent (Claude Code) - method change after PARTIAL edit, saved before sending (D-016), pending owner OK")
w(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V03.json", v3)
w(C / "keep_change_patch_PATCH_MF_EP01_S04_002.json", {
    "patch_id": "PATCH_MF_EP01_S04_002", "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "from_version": "V02", "to_version": "V03", "fix_reason": "AI_ARTIFACT",
    "keep": ["V01 scene description: open-topped chamber, low stone course, no mound, timber yard, labourers in hemp with baskets, overcast dust", "camera 1.6 m / 28mm feel", "laborer clothing reference 412a72bc"],
    "change": ["NOT an edit: fresh text+reference generation (crowd faces may change, LITE)", "explicit full-frame 16:9, no letterbox", "explicit all-wood tools, no metal heads/blades/saws"],
    "reason": "V02 edit PARTIAL: letterbox bars kept, some metal tools kept. Edits of many small details are unreliable (same as attendant full_body); explicit wording in a fresh generation worked before.",
    "requested_by": "Image Generation Agent (Claude Code) - pending owner OK", "created_at": D,
    "resulting_prompt_id": "PRM_MF_EP01_S04_MASTER_V03", "resulting_generation_id": None})

c = rd(C / "cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 54.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 54.12 credits (원로 24.12 · 군중 20 · 기준 그림 10). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "28 호출 = 54.12 credits (원로 13 · 군중 10 · 기준 그림 5). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## FIX 결과" not in s:
    s += ("\n## FIX 결과 (2026-09-13, 4 credits, 승인 5/10)\n\n"
          "- S06 OPEN_CHAMBER V02 `MF_EP01_S06_MASTER_OPEN_CHAMBER_V02_de2b6a3e.png`: **PASS** — 곧은 네모 관, 청동 과대+드리개. 사용자 최종 OK 대기.\n"
          "- S04 V02 `MF_EP01_S04_MASTER_V02_da44103f.png`: **PARTIAL** — 검은 띠 그대로, 쇠 삽·톱 일부 남음. 편집 반복 중단 → 새로 생성 V03 저장 (`PATCH_MF_EP01_S04_002`), 사용자 OK 대기.\n"
          "- 크레딧: 이번 쌍에서 잔액 -6, 거래 내역에 06:31:23Z 출처 불명 -2 (공용 계정, D-018) → EP01 비용 미포함.\n")
r.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 50.12 credits (26 호출: 원로 13 · 군중 10 · 기준 그림 3) — KRW 환산 P-012 |", "| 소진 | 54.12 credits (28 호출: 원로 13 · 군중 10 · 기준 그림 5) — KRW 환산 P-012 |"),
             ("소진 50.12 credits, KRW 환산 P-012)", "소진 54.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "기준 그림 FIX 결과" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — 기준 그림 FIX 결과 (4 credits, 승인 5/10): S06 MOUND_BUILDING APPROVED · S06 OPEN_CHAMBER V02 PASS (관·허리띠) 최종 OK 대기 · S04 V02 PARTIAL (검은 띠·쇠 공구 일부 남음) → 새로 생성 V03 저장, 사용자 OK 대기. EP01 소진 54.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", gids)
