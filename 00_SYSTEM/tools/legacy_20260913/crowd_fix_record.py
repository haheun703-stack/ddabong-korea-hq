# -*- coding: utf-8 -*-
"""Crowd full_body FIX edits (user OK "둘다 수정"): record jobs 412a72bc (laborer) / 77078e12 (attendant),
and save attendant retry V04 + PATCH_MP_ATTENDANT_FULL_BODY_002 BEFORE any sending (D-016).
Usage:  python 00_SYSTEM/tools/crowd_fix_record.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"; APR = "APR_EP01_MP_CROWD_001"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

JOBS = [
 ("LABORER", "412a72bc-f3f1-4955-8d3a-36e1e6306d1f", "f5514f0f-e657-4b85-b868-72256da35304", "SUCCESS",
  "Bot check PASS: spade and pick-axes removed, empty relaxed hands; faces, clothing, footwear, mounds and light unchanged."),
 ("ATTENDANT", "77078e12-15a1-480e-b67e-5f8044921940", "30791f45-502b-4d21-9add-028bb4a7c5b1", "PARTIAL",
  "Bot check PARTIAL: woman (right) fixed - chest ties gone, cloth belt at waist. Man left and young man middle STILL have long chest ribbon ties (middle man also no belt). Faces, colours, bundles unchanged. -> retry V04 saved (PATCH_MP_ATTENDANT_FULL_BODY_002), awaiting user OK."),
]
gids = []
for grp, job, src, status, check in JOBS:
    cid = f"CHAR_SILLA_{grp}_GROUP_01"; pid = f"PRM_MP_{cid}_FULL_BODY_V03"
    sent = rd(f"{STILLS}/prompt_{pid}.json")["assembled_text"]
    jp = f"{CACHE}/provider_jobs/HF_{job}.json"
    w(jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": "2026-09-13T04:42:20Z",
           "params": {"width": 2528, "height": 1696, "aspect_ratio": "3:2", "resolution": "2k", "batch_size": 1,
                      "input_images": [{"id": src, "type": "image_job"}], "prompt": sent},
           "retrieved_at": "2026-09-13", "note": "generate_image_batch/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V03)."})
    gid = f"GEN_MP_{grp}_FULL_BODY_HIGGSFIELD_V02"; gids.append(gid)
    out = f"{CACHE}/MP_CROWD/MP_{grp}_FULL_BODY_V02_{job[:8]}.png"
    src_path = f"{CACHE}/MP_CROWD/MP_{grp}_FULL_BODY_V01_{src[:8]}.png"
    w(f"{CACHE}/generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_PACK:{cid}:full_body", "stage": "STILL", "provider": "Higgsfield",
        "model": f"Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:2, edit of job {src[:8]})",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": "V03",
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": APR,
        "input_paths": [src_path], "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {job} (fix pair: balance 1894.48 -> 1890.48)"},
        "result_status": status, "failure_id": None, "started_at": "2026-09-13T04:42:20Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"FIX edit (PATCH_MP_{grp}_FULL_BODY_001, user OK 2026-09-13). {check}"})
    pt = rd(f"{CACHE}/keep_change_patch_PATCH_MP_{grp}_FULL_BODY_001.json")
    pt["resulting_generation_id"] = gid; pt["requested_by"] = "사용자 (2026-09-13 '둘다 수정')"
    w(f"{CACHE}/keep_change_patch_PATCH_MP_{grp}_FULL_BODY_001.json", pt)
    if status == "SUCCESS":
        ch = rd(f"05_HISTORY_DATABASE/characters/{cid}.json")
        ch["master_pack"]["full_body"] = {"path": out, "generation_id": gid, "status": "DRAFT"}
        w(f"05_HISTORY_DATABASE/characters/{cid}.json", ch)

# attendant retry V04 (input = partial edit 77078e12, woman already fixed)
cid = "CHAR_SILLA_ATTENDANT_GROUP_01"; v3 = rd(f"{STILLS}/prompt_PRM_MP_{cid}_FULL_BODY_V03.json"); v4 = dict(v3)
v4.update(prompt_id=f"PRM_MP_{cid}_FULL_BODY_V04", version="V04", parent_prompt_id=v3["prompt_id"], patch_id="PATCH_MP_ATTENDANT_FULL_BODY_002",
          shot_delta="full_body edit retry: remove remaining chest ribbon ties on the two men only",
          assembled_text=("Edit the reference image. Keep all three people exactly as they are: same faces, bodies, poses, hair, headwear, trousers, "
                          "skirt, footwear, fabric colours, bundles, lighting and background. Change only the two men's jackets (the man on the left "
                          "in dark grey and the young man in the middle in beige): remove the long fabric ribbon ties and bows hanging on their chests "
                          "completely, so the front of each jacket is plain and closed right over left with no strings. The man on the left keeps his "
                          "waist belt; give the young man in the middle a plain beige cloth belt tied at the waist like the others. Keep the woman on "
                          "the right exactly as she is. No ribbons or bows on any chest. No text, no watermark, no logo."),
          created_at="2026-09-13", created_by="Image Generation Agent (Claude Code) — FIX retry, saved before sending (D-016)")
w(f"{STILLS}/prompt_{v4['prompt_id']}.json", v4)
w(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_002.json", {
    "patch_id": "PATCH_MP_ATTENDANT_FULL_BODY_002", "shot_id": f"MASTER_PACK:{cid}:full_body", "from_version": "V03", "to_version": "V04",
    "fix_reason": "HISTORICAL_ISSUE",
    "keep": ["three faces and bodies", "poses", "hair and headwear", "trousers and skirt", "fabric colours", "bundles", "woman's corrected jacket", "background", "lighting"],
    "change": ["remove remaining chest ribbon ties on the two men", "add plain cloth waist belt to the middle man"],
    "reason": "V03 edit (GEN_MP_ATTENDANT_FULL_BODY_HIGGSFIELD_V02) PARTIAL: only the woman's ties were removed. Retry targets the two men by position, input = the partial edit.",
    "requested_by": "Image Generation Agent (Claude Code) — pending user OK", "created_at": "2026-09-13",
    "resulting_prompt_id": v4["prompt_id"], "resulting_generation_id": None})

c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 32.12}; c["as_of"] = "2026-09-13"
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 32.12 credits (원로 24.12 · 군중 8 = full_body 2 + 편집 2). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "17 호출 = 32.12 credits (원로 13 · 군중 4). P-012 환산율 확정 시 percent_used 계산."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

p = R / f"{CACHE}/MP_CROWD/REVIEW_CROWD_STEP1.md"; s = p.read_text(encoding="utf-8")
if "## 편집 결과" not in s:
    s += ("\n## 편집 결과 (사용자 '둘다 수정', 4 credits, 승인 4/9)\n\n| 무리 | 파일 | 결과 |\n|---|---|---|\n"
          "| 노동자 | `MP_LABORER_FULL_BODY_V02_412a72bc.png` | **PASS** — 공구 제거, 나머지 동일 |\n"
          "| 시종 | `MP_ATTENDANT_FULL_BODY_V02_77078e12.png` | **PARTIAL** — 여자만 옷고름 제거·허리띠. 남자 2명 옷고름 남음 → 재편집 `PRM_…_V04` + `PATCH_MP_ATTENDANT_FULL_BODY_002` 저장, 사용자 OK 대기 |\n\n"
          "남은 승인: 5 호출. 재편집 1 + 2단계 4 = 5 → 한도 딱 맞음 (추가 FIX 는 새 승인).\n")
p.write_text(s, encoding="utf-8")
print("recorded", gids)
