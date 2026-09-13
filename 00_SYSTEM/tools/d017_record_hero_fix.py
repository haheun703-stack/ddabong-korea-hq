# -*- coding: utf-8 -*-
"""D-017: record the hero background-fix generation (job 5de27748) sent verbatim from PRM_..._HERO_V04.
Usage:  python 00_SYSTEM/tools/d017_record_hero_fix.py SUCCESS|REJECTED "bot check note"
"""
import json, sys
from pathlib import Path

R = Path(__file__).resolve().parents[2]
STATUS, NOTE = sys.argv[1], sys.argv[2]
CHAR = "CHAR_SILLA_ELITE_OBSERVER_01"; CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
JOB = "5de27748-f100-47e0-af23-1bdb68466bb7"; GEN = "GEN_MP_ELITE_HERO_HIGGSFIELD_V03"; PID = f"PRM_MP_{CHAR}_HERO_V04"
OUT = f"{CACHE}/MP_ELITE/MP_ELITE_HERO_V03_5de27748.png"; REF = f"{CACHE}/MP_ELITE/MP_ELITE_HERO_V02_c7a5cc92.png"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

sent = rd(f"{STILLS}/prompt_{PID}.json")["assembled_text"]
jp = f"{CACHE}/provider_jobs/HF_{JOB}.json"
w(jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
       "created_at": "2026-09-13T04:11:25Z",
       "params": {"width": 1792, "height": 2400, "aspect_ratio": "3:4", "resolution": "2k", "batch_size": 1,
                  "input_images": [{"id": "c7a5cc92-3f36-4b40-8071-84da9f6c6441", "type": "image_job"}], "prompt": sent},
       "retrieved_at": "2026-09-13", "note": "Higgsfield job_status raw_data. Result/CDN URLs omitted. params.prompt is the text actually sent (identical to HERO_V04)."})

w(f"{CACHE}/generation_{GEN}.json", {
    "generation_id": GEN, "shot_id": f"MASTER_PACK:{CHAR}:hero", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:4, image_references=hero job c7a5cc92, edit)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V04",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MP_ELITE_BATCH1_001",
    "input_paths": [REF], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1914.48 -> 1912.48)"},
    "result_status": STATUS, "failure_id": None, "started_at": "2026-09-13T04:11:25Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": f"D-017 FIX (PATCH_MP_ELITE_HERO_002): edit of hero V02 image, background tiled-roof buildings only. Batch-1 approval call 6/8. {NOTE}"})

pt = rd(f"{CACHE}/keep_change_patch_PATCH_MP_ELITE_HERO_002.json"); pt["resulting_generation_id"] = GEN
w(f"{CACHE}/keep_change_patch_PATCH_MP_ELITE_HERO_002.json", pt)

c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
if GEN not in c["generation_ids"]: c["generation_ids"].append(GEN)
c["spent_by_provider"] = {"Higgsfield (credits)": 10.12}; c["as_of"] = "2026-09-13"
c["budget"]["note"] = "D-015 사용자 확정 ₩40,000. 소진 Higgsfield 10.12 credits (배치 1 8.12 + D-017 hero 배경 편집 2). 크레딧→KRW 환산율 미확정 (P-012) → spent_total/percent_used null."
c["note"] = "배치 1: 5 호출 (soul_2 0.12 + Nano Banana Pro [nano_banana_2] 2 x 4) = 8.12 · D-017 hero 배경 편집 1 호출 2 = 합계 10.12 credits (6 호출). P-012 환산율 확정 시 percent_used 계산. 80% WARNING · 95% STRONG · 100% LOCKED."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

if STATUS == "SUCCESS":
    ch = rd(f"05_HISTORY_DATABASE/characters/{CHAR}.json")
    ch["master_pack"]["hero"] = {"path": OUT, "generation_id": GEN, "status": "DRAFT"}
    if "hero V03" not in ch["notes"]:
        ch["notes"] += " hero V03 (배경 편집, job 5de27748) DRAFT → 사람 확인 대기. 얼굴 ID 참조는 c7a5cc92 유지."
    w(f"05_HISTORY_DATABASE/characters/{CHAR}.json", ch)
print("recorded", GEN, STATUS)
