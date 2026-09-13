# -*- coding: utf-8 -*-
"""Record S04 master frame V04 edit (job cbd3f3df, sent verbatim from PRM_MF_EP01_S04_MASTER_V04) as SUCCESS; frame path -> V04 (DRAFT, owner OK pending).
Usage:  python 00_SYSTEM/tools/mf_s04_v04_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOB = "cbd3f3df-6bf2-41c2-9ca7-7d824eb898f2"; SRC = "447da844-0c8f-4d3a-9d0f-ca6dae38eb7b"
GID = "GEN_MF_EP01_S04_MASTER_HIGGSFIELD_V04"; PID = "PRM_MF_EP01_S04_MASTER_V04"
OUT = "08_GENERATION_CACHE/EP01/MF/MF_EP01_S04_MASTER_V04_cbd3f3df.png"
jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{JOB}.json"
w(R / jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"{D}T06:43:03Z",
           "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1,
                      "input_images": [{"id": SRC, "type": "image_job"}], "prompt": rd(EP / f"11_AI_STILLS/prompt_{PID}.json")["assembled_text"]},
           "retrieved_at": D, "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V04)."})
w(C / f"generation_{GID}.json", {
    "generation_id": GID, "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 16:9, edit of job 447da844)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V04",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MF_001",
    "input_paths": ["08_GENERATION_CACHE/EP01/MF/MF_EP01_S04_MASTER_V03_447da844.png"], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1864.48 -> 1862.48)"},
    "result_status": "SUCCESS", "failure_id": None, "started_at": f"{D}T06:43:03Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": "Edit (PATCH_MF_EP01_S04_003, owner 'A'). Bot check PASS: horizon now low hills, a few trees and open land - no poles, wires or buildings; tape measure became a wooden stick; front spade blades now read as wood; chamber, stones, labourers, dust and framing unchanged; full frame, no letterbox."})
pt = rd(C / "keep_change_patch_PATCH_MF_EP01_S04_003.json"); pt["resulting_generation_id"] = GID; w(C / "keep_change_patch_PATCH_MF_EP01_S04_003.json", pt)
mf = EP / "07_SHOTS/master_frame_EP01_S04_MASTER_V01.json"; d = rd(mf); d["path"] = OUT; d["generation_id"] = GID; d["status"] = "DRAFT"; d["updated_at"] = D; w(mf, d)
c = rd(C / "cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 58.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 58.12 credits (원로 24.12 · 군중 20 · 기준 그림 14). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "30 호출 = 58.12 credits (원로 13 · 군중 10 · 기준 그림 7). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## S04 편집 V04 결과" not in s:
    s += ("\n## S04 편집 V04 결과 (2 credits, 승인 7/10)\n\n`MF_EP01_S04_MASTER_V04_cbd3f3df.png` **PASS** — 지평선 전봇대·건물 제거 (낮은 산·나무·들판), 줄자 → 나무 자, 앞쪽 삽날 → 나무. 나머지 동일. 사용자 최종 OK 대기.\n")
r.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 56.12 credits (29 호출: 원로 13 · 군중 10 · 기준 그림 6) — KRW 환산 P-012 |", "| 소진 | 58.12 credits (30 호출: 원로 13 · 군중 10 · 기준 그림 7) — KRW 환산 P-012 |"),
             ("소진 56.12 credits, KRW 환산 P-012)", "소진 58.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "S04 편집 V04 PASS" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — S04 편집 V04 PASS (2 credits, 승인 7/10): 현대 지평선·줄자·쇠 삽날 제거. 사용자 최종 OK 대기 → OK 면 기준 그림 3장 확정. EP01 소진 58.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", GID)
