# -*- coding: utf-8 -*-
"""Crowd step 1 (D-020): record the two full_body jobs + save FIX edit prompts (V03) and patches BEFORE sending (D-016).
Usage:  python 00_SYSTEM/tools/crowd_step1_record.py
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
 ("LABORER", "f5514f0f-e657-4b85-b868-72256da35304",
  "Bot check: three different men, undyed hemp/black jackets, cloth waist cords, shin-bound trousers, straw sandals/bare feet, topknots, finished mounds behind. ISSUE (era lock: no modern tools): they hold a flat steel spade and pick-axes that read as modern metal tools -> FIX edit proposed (PATCH_MP_LABORER_FULL_BODY_001).",
  "HISTORICAL_ISSUE", ["three faces and bodies", "poses", "hemp jackets and colours", "waist cords", "trousers and footwear", "hair", "mound background", "lighting"],
  ["remove the steel spade and pick-axes; hands empty and relaxed"],
  "Hand tools read as modern steel tools (SILLA_EARLY_V01 forbids modern tools). Edit the existing image so the costume reference stays identical.",
  "Edit the reference image. Keep the three men exactly as they are: same faces, bodies, poses, clothing, hair, footwear, lighting, background mounds and sky. Change only the hand tools: remove the metal spade and the metal pick-axes completely, so all three men stand with empty relaxed hands at their sides. No modern tools, no metal tools. No text, no watermark, no logo."),
 ("ATTENDANT", "30791f45-502b-4d21-9add-028bb4a7c5b1",
  "Bot check: two men and one woman, undyed grey/black/ivory hemp, cloth headband and cloth cap, woman in long skirt, cloth bundles, plain earth. ISSUE (costume lock: no Joseon hanbok silhouette): all three jackets fasten with long chest ribbon ties (goreum-like bows) that read as Joseon hanbok -> FIX edit proposed (PATCH_MP_ATTENDANT_FULL_BODY_001).",
  "HISTORICAL_ISSUE", ["three faces and bodies", "poses", "hair and headwear", "trousers and skirt", "fabric colours", "footwear", "bundles", "background", "lighting"],
  ["remove chest ribbon ties on all three jackets; jackets held only by a plain cloth belt at the waist"],
  "Chest ribbon ties read as Joseon hanbok (COSTUME_SILLA_ATTENDANT_A01_LOCK forbids Joseon hanbok silhouette). Edit the existing image so faces and costume otherwise stay identical.",
  "Edit the reference image. Keep the three people exactly as they are: same faces, bodies, poses, hair, headwear, trousers, skirt, footwear, fabric colours, bundles, lighting and background. Change only the jacket fastening: remove the long ribbon ties on the chest of all three jackets; each jacket closes right over left with a straight collar and is held only by a plain cloth belt tied at the waist, like simple ancient work jackets. No ribbon bows on the chest, no Joseon hanbok look. No text, no watermark, no logo."),
]
gids = []
for grp, job, check, reason_code, keep, change, reason, fix_text in JOBS:
    cid = f"CHAR_SILLA_{grp}_GROUP_01"; pid = f"PRM_MP_{cid}_FULL_BODY_V02"
    sent = rd(f"{STILLS}/prompt_{pid}.json")["assembled_text"]
    jp = f"{CACHE}/provider_jobs/HF_{job}.json"
    w(jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": "2026-09-13T04:37:09Z",
           "params": {"width": 2528, "height": 1696, "aspect_ratio": "3:2", "resolution": "2k", "batch_size": 1, "input_images": [], "prompt": sent},
           "retrieved_at": "2026-09-13", "note": "generate_image_batch/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V02)."})
    gid = f"GEN_MP_{grp}_FULL_BODY_HIGGSFIELD_V01"; gids.append(gid)
    out = f"{CACHE}/MP_CROWD/MP_{grp}_FULL_BODY_V01_{job[:8]}.png"
    w(f"{CACHE}/generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_PACK:{cid}:full_body", "stage": "STILL", "provider": "Higgsfield",
        "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:2, text only)",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": "V02",
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": APR,
        "input_paths": [], "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {job} (step 1 pair: balance 1898.48 -> 1894.48)"},
        "result_status": "SUCCESS", "failure_id": None, "started_at": "2026-09-13T04:37:09Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"D-020 crowd step 1. {check}"})
    ch = rd(f"05_HISTORY_DATABASE/characters/{cid}.json")
    ch["master_pack"]["full_body"] = {"path": out, "generation_id": gid, "status": "DRAFT"}
    ch["status"] = "MASTER_IN_PROGRESS"; ch["updated_at"] = "2026-09-13"
    w(f"05_HISTORY_DATABASE/characters/{cid}.json", ch)
    # FIX prompt V03 + patch, saved before any sending
    patch = f"PATCH_MP_{grp}_FULL_BODY_001"
    v2 = rd(f"{STILLS}/prompt_{pid}.json"); v3 = dict(v2)
    v3.update(prompt_id=f"PRM_MP_{cid}_FULL_BODY_V03", shot_delta=f"full_body edit: {change[0]}", assembled_text=fix_text,
              reference_images=[f"character_pack:{cid}"], version="V03", parent_prompt_id=pid, patch_id=patch, created_at="2026-09-13",
              created_by="Image Generation Agent (Claude Code) — FIX edit, saved before sending (D-016)")
    w(f"{STILLS}/prompt_{v3['prompt_id']}.json", v3)
    w(f"{CACHE}/keep_change_patch_{patch}.json", {
        "patch_id": patch, "shot_id": f"MASTER_PACK:{cid}:full_body", "from_version": "V02", "to_version": "V03", "fix_reason": reason_code,
        "keep": keep, "change": change, "reason": reason, "requested_by": "Image Generation Agent (Claude Code) — pending user OK",
        "created_at": "2026-09-13", "resulting_prompt_id": v3["prompt_id"], "resulting_generation_id": None})

c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 28.12}; c["as_of"] = "2026-09-13"
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 28.12 credits (원로 24.12 = 배치1 8.12 + hero 편집 2 + 배치2 14 · 군중 1단계 4). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "15 호출 = 28.12 credits (원로 배치1 5 · hero 편집 1 · 배치2 7 · 군중 1단계 2). P-012 환산율 확정 시 percent_used 계산."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

(R / f"{CACHE}/MP_CROWD/REVIEW_CROWD_STEP1.md").write_text("""# 군중 LITE 1단계 (full_body) — 사람 검수 시트

> 2026-09-13 · 승인 `APR_EP01_MP_CROWD_001` (D-020) · 2 호출 / 2 성공 · 4 credits (한도 9 중 2)

| 무리 | 파일 | 봇 판정 | 제안 |
|---|---|---|---|
| 노동자 | `MP_LABORER_FULL_BODY_V01_f5514f0f.png` | 사람·복식 OK. **삽·곡괭이가 현대 쇠 공구처럼 보임** (시대 lock 위반 소지) | 공구만 지우는 편집 1회 (`PRM_…_V03` + `PATCH_MP_LABORER_FULL_BODY_001` 저장됨) |
| 시종 | `MP_ATTENDANT_FULL_BODY_V01_30791f45.png` | 사람·색 OK. **가슴 긴 옷고름 매듭이 조선 한복처럼 보임** (복식 lock 위반) | 옷고름만 지우고 허리 천띠로 여미는 편집 1회 (`PRM_…_V03` + `PATCH_MP_ATTENDANT_FULL_BODY_001` 저장됨) |

편집은 사용자 OK 후 전송. 편집본 확인 뒤 2단계 (walking · costume_detail) 는 편집본을 복식 참조로.
""", encoding="utf-8")
print("recorded", gids)
