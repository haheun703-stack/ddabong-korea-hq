# -*- coding: utf-8 -*-
"""D-021 attendant full_body retry (job dc7f38ed, sent verbatim from V04): record as PARTIAL.
Usage:  python 00_SYSTEM/tools/crowd_retry_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
CID = "CHAR_SILLA_ATTENDANT_GROUP_01"; PID = f"PRM_MP_{CID}_FULL_BODY_V04"
JOB = "dc7f38ed-f345-4dbc-aebb-17d155986a2e"; SRC = "77078e12-15a1-480e-b67e-5f8044921940"; GID = "GEN_MP_ATTENDANT_FULL_BODY_HIGGSFIELD_V03"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
jp = f"{CACHE}/provider_jobs/HF_{JOB}.json"
w(jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
       "created_at": "2026-09-13T04:47:24Z",
       "params": {"width": 2528, "height": 1696, "aspect_ratio": "3:2", "resolution": "2k", "batch_size": 1,
                  "input_images": [{"id": SRC, "type": "image_job"}], "prompt": rd(f"{STILLS}/prompt_{PID}.json")["assembled_text"]},
       "retrieved_at": "2026-09-13", "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V04)."})
w(f"{CACHE}/generation_{GID}.json", {
    "generation_id": GID, "shot_id": f"MASTER_PACK:{CID}:full_body", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:2, edit of job 77078e12)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V04",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MP_CROWD_001",
    "input_paths": [f"{CACHE}/MP_CROWD/MP_ATTENDANT_FULL_BODY_V02_77078e12.png"],
    "output_paths": [f"{CACHE}/MP_CROWD/MP_ATTENDANT_FULL_BODY_V03_dc7f38ed.png"], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1890.48 -> 1888.48)"},
    "result_status": "PARTIAL", "failure_id": None, "started_at": "2026-09-13T04:47:24Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": "D-021 retry (PATCH_MP_ATTENDANT_FULL_BODY_002). Bot check PARTIAL: left man fixed (chest ties removed, belt kept); woman unchanged and compliant; young man in the middle STILL has the long chest ribbon tie and no belt. Per D-021, no further edit loop - method change proposed to user."})
pt = rd(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_002.json"); pt["resulting_generation_id"] = GID
w(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_002.json", pt)
c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 34.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 34.12 credits (원로 24.12 · 군중 10 = full_body 2 + 편집 3). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "18 호출 = 34.12 credits (원로 13 · 군중 5). P-012 환산율 확정 시 percent_used 계산."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)
p = R / f"{CACHE}/MP_CROWD/REVIEW_CROWD_STEP1.md"; s = p.read_text(encoding="utf-8")
if "## 재편집 결과" not in s:
    s += ("\n## 재편집 결과 (D-021, 2 credits, 승인 5/12)\n\n`MP_ATTENDANT_FULL_BODY_V03_dc7f38ed.png` **PARTIAL** — 왼쪽 남자 옷고름 제거 성공, 여자 유지. "
          "**가운데 젊은 남자 옷고름 남음·허리띠 없음.** D-021 에 따라 편집 반복 중단 → 방법 전환 사용자 결정 대기.\n")
p.write_text(s, encoding="utf-8")
print("recorded", GID)
