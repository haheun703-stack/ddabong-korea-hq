# -*- coding: utf-8 -*-
"""Record master frames V01 (APR_EP01_MF_001 calls 1-3) and save FIX edit prompts V02 + patches BEFORE sending (D-016).
Usage:  python 00_SYSTEM/tools/mf_v01_record.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; CACHE = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
REFS = {"412a72bc": "412a72bc-f3f1-4955-8d3a-36e1e6306d1f", "84c0fdbc": "84c0fdbc-1c5c-4edd-bb35-b1836ae14288",
        "5de27748": "5de27748-f100-47e0-af23-1bdb68466bb7", "fba70a58": "fba70a58-ef3f-45b7-8f94-7c61d0284307"}
JOBS = [
 ("EP01_S04_MASTER_V01", "4de7af1f-490d-4b33-94c7-8c0f8309e478", "06:11:29", ["412a72bc"],
  "Bot check: layer stage correct (open-topped timber chamber on levelled ground, low course of river stones at its walls, no mound yet), timber yard left, labourers in hemp with baskets, dust, overcast. ISSUES: several metal tool heads (pick-axes, hoes, saw, one metal-bladed spade) despite 'wooden tools only'; black letterbox bars baked in at top and bottom. -> FIX edit proposed (PATCH_MF_EP01_S04_001).",
  ("PATCH_MF_EP01_S04_001", "AI_ARTIFACT", ["chamber, stones, stage", "labourers faces, clothing, poses", "timber yard", "dust and light", "camera angle"],
   ["metal tool heads -> wooden tools", "remove baked-in black letterbox bars, fill full 16:9 frame"],
   "Edit the reference image. Keep everything exactly as it is: the same scene, timber chamber, river stones, labourers, their faces, clothing and poses, the timber yard, the dust, the light and the camera angle. Change only two things: (1) every tool with a metal head or blade - pick-axes, hoes, saws and spades - becomes a plain wooden tool: wooden spades, wooden poles and wooden mallets with no metal parts; (2) remove the black letterbox bars at the top and bottom and extend the scene naturally so the image fills the whole 16:9 frame. No metal tools, no black bars, no text, no watermark, no logo.",
   ["4de7af1f-490d-4b33-94c7-8c0f8309e478"])),
 ("EP01_S06_MASTER_OPEN_CHAMBER_V01", "80d2d3db-44cd-4d01-8b50-76048154c458", "06:11:30", ["5de27748", "fba70a58", "84c0fdbc", "412a72bc"],
  "Bot check: stage correct (open-topped chamber, coffin and chest inside, low stone course outside, no stones or earth on top), attendants in belted hemp holding cloth bundles, two women in grey skirts, labourers waiting with stone baskets, exactly one person in blue (observer, three-quarter back, birch-bark cap), late light. ISSUES: coffin has a tapered hexagonal Western-coffin outline; chest has metal hinges and latch; observer's belt is a plain leather strap without bronze plaques or pendants. -> FIX edit proposed (PATCH_MF_EP01_S06_OPEN_CHAMBER_001).",
  ("PATCH_MF_EP01_S06_OPEN_CHAMBER_001", "HISTORICAL_ISSUE", ["chamber, stones, stage", "all faces, clothing, poses", "bundles and baskets", "light and camera angle", "exactly one person in blue"],
   ["coffin -> plain straight-sided rectangular box with flat lid", "chest -> no metal hinges or latch", "observer belt -> bronze plaque belt with small pendants"],
   "Edit the reference image. Keep everything exactly as it is: the same open timber chamber, river stones, attendants, labourers and senior observer, all faces, clothing and poses, the bundles and baskets, the light and the camera angle. Change only three things: (1) the coffin inside the chamber becomes a plain straight-sided rectangular wooden box with a flat lid, with no tapered or angled shoulders; (2) the wooden chest has no metal hinges, latches or handles, plain wood only; (3) the senior observer's belt becomes a restrained bronze plaque belt with small hanging bronze pendants, like the belt in the second reference image. No text, no watermark, no logo.",
   ["80d2d3db-44cd-4d01-8b50-76048154c458", "5681f1e0-fe07-4fc3-b36c-f512dc7a2992"])),
 ("EP01_S06_MASTER_MOUND_BUILDING_V01", "8e1007b7-fc47-4de0-9ba4-709d4a44efeb", "06:11:30", ["5de27748", "fba70a58", "412a72bc", "84c0fdbc"],
  "Bot check: stage acceptable (heap of river stones with earth mound rising over and around it, no timber/coffin/chamber visible), labourers carrying earth baskets on the slope with ropes, attendants in belted hemp at the base, exactly one person in blue (observer from behind, birch-bark cap). NOTES (not blocking): front of the stone heap is still exposed below the earth (plausible mid-construction); mound crop makes the 3.7:1 proportion hard to judge; observer belt shows plaques faintly but no pendants.",
  None),
]
gids = []
for frame, job, t, refs, check, fix in JOBS:
    pid = f"PRM_MF_{frame}"; sent = rd(EP / f"11_AI_STILLS/prompt_{pid}.json")["assembled_text"]
    jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{job}.json"
    w(R / jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
               "created_at": f"{D}T{t}Z",
               "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1,
                          "input_images": [{"id": REFS[r], "type": "image_job"} for r in refs], "prompt": sent},
               "retrieved_at": D, "note": "generate_image_batch/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V01)."})
    gid = f"GEN_MF_{frame[:-4]}_HIGGSFIELD_V01"; gids.append(gid)
    out = f"08_GENERATION_CACHE/EP01/MF/MF_{frame}_{job[:8]}.png"
    w(CACHE / f"generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_FRAME:{frame}", "stage": "STILL", "provider": "Higgsfield",
        "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 16:9, image_references=" + " + ".join(refs) + ")",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": "V01",
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MF_001",
        "input_paths": [], "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {job} (batch of 3: balance 1878.48 -> 1872.48)"},
        "result_status": "SUCCESS", "failure_id": None, "started_at": f"{D}T{t}Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"D-026 master frame. {check} Awaiting owner OK/FIX."})
    mf = EP / f"07_SHOTS/master_frame_{frame}.json"; d = rd(mf); d["path"] = out; d["generation_id"] = gid; d["status"] = "DRAFT"; d["updated_at"] = D; w(mf, d)
    if fix:
        patch, reason, keep, change, text, inputs = fix
        v1 = rd(EP / f"11_AI_STILLS/prompt_{pid}.json"); v2 = dict(v1)
        v2.update(prompt_id=pid[:-4] + "_V02", version="V02", parent_prompt_id=pid, patch_id=patch, assembled_text=text,
                  shot_delta=f"master frame FIX edit: {'; '.join(change)}", created_at=D,
                  created_by="Image Generation Agent (Claude Code) — FIX edit, saved before sending (D-016), pending owner OK")
        w(EP / f"11_AI_STILLS/prompt_{v2['prompt_id']}.json", v2)
        w(CACHE / f"keep_change_patch_{patch}.json", {
            "patch_id": patch, "shot_id": f"MASTER_FRAME:{frame}", "from_version": "V01", "to_version": "V02", "fix_reason": reason,
            "keep": keep, "change": change, "reason": check.split("ISSUES: ")[1].split(" -> ")[0] + f" Edit input: {', '.join(i[:8] for i in inputs)}.",
            "requested_by": "Image Generation Agent (Claude Code) — pending owner OK", "created_at": D,
            "resulting_prompt_id": v2["prompt_id"], "resulting_generation_id": None})

c = rd(CACHE / "cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 50.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 50.12 credits (원로 24.12 · 군중 20 · 기준 그림 6). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "26 호출 = 50.12 credits (원로 13 · 군중 10 · 기준 그림 3). P-012 환산율 확정 시 percent_used 계산."
w(CACHE / "cost_COST_EP01_20260911.json", c)

rows = "\n".join(f"| {f} | `MF_{f}_{j[:8]}.png` | {ck} | ☐ APPROVE ☐ FIX |" for f, j, _, _, ck, _ in JOBS)
(CACHE / "MF/REVIEW_MF_V01.md").write_text(f"""# EP01 기준 그림 V01 — 사람 검수 시트

> {D} · 승인 `APR_EP01_MF_001` (D-026) · 3 호출 / 3 성공 · 6 credits (한도 10 호출 / 20 credits 중 3 호출)
> 전송 = 각 `PRM_MF_*_V01` 문장 그대로. FIX 문장(V02)과 PATCH 는 저장만, 사용자 OK 후 전송.

| frame | 파일 | 봇 판정 | 사람 검수 |
|---|---|---|---|
{rows}

## FIX 제안 (저장됨, 미전송)

- S04 → `PRM_MF_EP01_S04_MASTER_V02` + `PATCH_MF_EP01_S04_001`: 쇠 공구 → 나무 공구, 위아래 검은 띠 제거. 입력 = V01 이미지. 1 호출.
- S06 OPEN_CHAMBER → `PRM_MF_EP01_S06_MASTER_OPEN_CHAMBER_V02` + `PATCH_MF_EP01_S06_OPEN_CHAMBER_001`: 관 → 곧은 네모 나무 상자, 궤 쇠 경첩 제거, 원로 허리띠 → 청동 과대. 입력 = V01 이미지 + 원로 전신. 1 호출.
- S06 MOUND_BUILDING: 수정 없음 제안 (메모만).

FIX 2건 전송 시 누적 5 / 10 호출, 10 / 20 credits.
""", encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 44.12 credits (23 호출: 원로 13 · 군중 10) — KRW 환산 P-012 |", "| 소진 | 50.12 credits (26 호출: 원로 13 · 군중 10 · 기준 그림 3) — KRW 환산 P-012 |"),
             ("소진 44.12 credits, KRW 환산 P-012)", "소진 50.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "기준 그림 V01 3장 생성" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — 기준 그림 V01 3장 생성 (6 credits, 승인 3/10). S04: 쇠 공구·검은 띠 → FIX 제안 · S06 OPEN_CHAMBER: 서양식 관·쇠 경첩·민 허리띠 → FIX 제안 · S06 MOUND_BUILDING: 통과 제안. FIX 문장(V02)·PATCH 저장, **사용자 OK/FIX 대기**. `08_GENERATION_CACHE/EP01/MF/REVIEW_MF_V01.md`. EP01 소진 50.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", gids)
