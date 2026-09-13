# -*- coding: utf-8 -*-
"""Record H06 still attempt 1 (job 0f250ab3, sent verbatim from PRM_EP01_S06_SH010_V02) as REJECTED, save V03 + PATCH_EP01_S06_SH010_001
BEFORE the 2nd (last) approved call.  Usage: python 00_SYSTEM/tools/h06_v01_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOB = "0f250ab3-5927-4c80-8a01-2dcae8e5f74f"; GID = "GEN_EP01_S06_SH010_HIGGSFIELD_V01"; PID = "PRM_EP01_S06_SH010_V02"
OUT = "08_GENERATION_CACHE/EP01/AI_STILL/H06_V01_0f250ab3.png"
v2 = rd(EP / f"11_AI_STILLS/prompt_{PID}.json")
jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{JOB}.json"
w(R / jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"{D}T11:47:26Z",
           "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1,
                      "input_images": [{"id": "8e1007b7-fc47-4de0-9ba4-709d4a44efeb", "type": "image_job"}], "prompt": v2["assembled_text"]},
           "retrieved_at": D, "note": "job_status raw_data. Result/CDN URLs omitted. params.prompt verified identical to prompt V02 (1605 chars)."})
CHECK = ("Owner criteria check: (1) construction stage PASS - smooth nearly finished earth dome, people smoothing the top, no stones/timber; "
         "(2) human scale roughly OK - base figures read about 1/6 of mound height (target ~1/8), partly close wide-angle perspective; "
         "(3) proportion FAIL - visible width ~2.3x height vs target ~3.7x (too steep/peaked), likely inherited from the steep mound in reference frame MOUND_BUILDING and 24mm close camera; "
         "(4) modern intrusion FAIL - utility poles and white buildings on the left horizon, white structure on the right horizon.")
w(C / f"generation_{GID}.json", {
    "generation_id": GID, "shot_id": "EP01_S06_SH010", "stage": "STILL", "provider": "Higgsfield",
    "model": "NANO_BANANA_PRO (job_set_type nano_banana_2, 2k, 16:9, image_references=MOUND_BUILDING frame 8e1007b7)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V02",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_AI_B1_001",
    "input_paths": ["08_GENERATION_CACHE/EP01/MF/MF_EP01_S06_MASTER_MOUND_BUILDING_V01_8e1007b7.png"], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1860.48 -> 1858.48)"},
    "result_status": "REJECTED", "failure_id": None, "started_at": f"{D}T11:47:26Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)", "notes": f"D-028 D4 call 1/2. {CHECK} -> retry V03 (PATCH_EP01_S06_SH010_001), pre-approved in D4."})

TEXT = " ".join([
 "One wide documentary photograph that fills the entire 16:9 frame edge to edge, a single still image; no black bars, no letterbox, no borders.",
 "Early Silla, Gyeongju, 5th century: the Cheonmachong earth mound nearly completed, seen from far away.",
 "The mound is a very broad, low, gently sloping dome of freshly packed earth, about 47 metres across and only 12.7 metres high: its height is barely a quarter of its width, the slopes are gentle, about 25 to 30 degrees, and the top is a wide rounded crown, not a peak; the last bare patches are being smoothed near the top; no stones, timber or chamber visible anywhere.",
 "Small groups of people stand near its base for scale; a person about 1.6 metres tall is only about one eighth of the mound's height and looks tiny against it.",
 "They are labourers in undyed coarse hemp and funeral attendants in belted white, black and grey-brown hemp jackets; all different faces, no one in blue, no one posing, no one looking at the camera.",
 "Camera about 1.7 metres high, standing far back, about 60 metres from the mound, 35mm lens feel, so the whole mound sits in the middle of the frame with open ground on both sides; static wide view, low warm sunlight from the side, long shadows, calm and permanent, not celebratory.",
 "The horizon is empty early countryside - only bare low hills and a few trees, nothing man-made anywhere: no utility poles, no power lines, no buildings, no sheds, no roads, no fences, no regular field grid, no modern objects.",
 "Photorealistic historical documentary still, style B Documentary Reenactment, natural textures, not glossy, earthy natural colours.",
 "No tiled roofs, no stone walls, no manicured grass lawn, no gold objects, no crown, no text, no watermark, no logo."])
v3 = dict(v2)
v3.update(prompt_id="PRM_EP01_S06_SH010_V03", version="V03", parent_prompt_id=PID, patch_id="PATCH_EP01_S06_SH010_001", assembled_text=TEXT,
          reference_images=[], shot_delta="H06 retry: gentle low dome (height ~1/4 width), camera far back 35mm, empty man-made-free horizon, no reference image",
          created_at=D, created_by="Image Generation Agent (Claude Code) - retry, saved before sending (D-016), D-028 D4 call 2/2")
w(EP / "11_AI_STILLS/prompt_PRM_EP01_S06_SH010_V03.json", v3)
w(C / "keep_change_patch_PATCH_EP01_S06_SH010_001.json", {
    "patch_id": "PATCH_EP01_S06_SH010_001", "shot_id": "EP01_S06_SH010", "from_version": "V02", "to_version": "V03", "fix_reason": "HISTORICAL_ISSUE",
    "keep": ["nearly completed smooth earth dome stage", "people at base for scale, text-described costumes, no blue", "low warm side light, calm", "full frame, documentary style"],
    "change": ["modern horizon (poles, buildings) -> explicit 'nothing man-made anywhere'",
               "mound proportion too steep -> explicit height ~1/4 width, gentle 25-30 degree slopes, rounded crown",
               "camera 24mm close -> far back ~60 m, 35mm (reduces wide-angle height exaggeration; camera draft is 24mm static)",
               "reference image MOUND_BUILDING removed (its steep rising mound was likely copied)"],
    "reason": "Attempt 1 (GEN_EP01_S06_SH010_HIGGSFIELD_V01) failed owner criteria: modern intrusion and mound proportion ~2.3:1 instead of ~3.7:1.",
    "requested_by": "사용자 (D-028 D4 사전 승인: 실패 시 실패 항목만 수정 후 재시도)", "created_at": D,
    "resulting_prompt_id": "PRM_EP01_S06_SH010_V03", "resulting_generation_id": None})

c = rd(C / "cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 62.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 62.12 credits (원로 24.12 · 군중 20 · 기준 그림 16 · AI 샷 2). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "32 호출 = 62.12 credits (원로 13 · 군중 10 · 기준 그림 8 · AI 샷 1). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 60.12 credits (31 호출: 원로 13 · 군중 10 · 기준 그림 8) — KRW 환산 P-012 |", "| 소진 | 62.12 credits (32 호출: 원로 13 · 군중 10 · 기준 그림 8 · AI 샷 1) — KRW 환산 P-012 |"),
             ("소진 60.12 credits, KRW 환산 P-012)", "소진 62.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "H06 1차" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — H06 1차 (2 credits, 승인 1/2): 단계 OK · 규모 대체로 OK · **봉분 비율 약 2.3:1 (목표 3.7:1) · 지평선 전봇대·건물** → REJECTED. 실패 항목만 고친 V03 + PATCH 저장 후 마지막 2차 시도. EP01 소진 62.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", GID)
