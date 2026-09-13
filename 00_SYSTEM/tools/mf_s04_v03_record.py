# -*- coding: utf-8 -*-
"""Record S04 master frame V03 fresh generation (job 447da844, PARTIAL) and save V04 background/props edit + PATCH_MF_EP01_S04_003
BEFORE sending (D-016).  Usage: python 00_SYSTEM/tools/mf_s04_v03_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOB = "447da844-0c8f-4d3a-9d0f-ca6dae38eb7b"; GID = "GEN_MF_EP01_S04_MASTER_HIGGSFIELD_V03"; PID = "PRM_MF_EP01_S04_MASTER_V03"
OUT = "08_GENERATION_CACHE/EP01/MF/MF_EP01_S04_MASTER_V03_447da844.png"
jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{JOB}.json"
w(R / jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"{D}T06:38:33Z",
           "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1,
                      "input_images": [{"id": "412a72bc-f3f1-4955-8d3a-36e1e6306d1f", "type": "image_job"}],
                      "prompt": rd(EP / f"11_AI_STILLS/prompt_{PID}.json")["assembled_text"]},
           "retrieved_at": D, "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V03)."})
CHECK = ("Bot check PARTIAL: letterbox gone (full frame) and most tools wooden (mallets, carrying poles with baskets); open chamber with stone course, labourers in hemp. "
         "NEW ISSUES: modern background on the horizon (utility poles and power lines, modern buildings/greenhouses, regular field grid); "
         "a yellow modern tape measure held by the front-left labourer; a few spades still read as metal-bladed. -> edit V04 proposed (PATCH_MF_EP01_S04_003).")
w(C / f"generation_{GID}.json", {
    "generation_id": GID, "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 16:9, image_references=412a72bc)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V03",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MF_001",
    "input_paths": [], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1866.48 -> 1864.48)"},
    "result_status": "PARTIAL", "failure_id": None, "started_at": f"{D}T06:38:33Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)", "notes": f"Method change after V02 PARTIAL (PATCH_MF_EP01_S04_002, owner OK). {CHECK}"})
pt = rd(C / "keep_change_patch_PATCH_MF_EP01_S04_002.json"); pt["resulting_generation_id"] = GID; w(C / "keep_change_patch_PATCH_MF_EP01_S04_002.json", pt)

TEXT = ("Edit the reference image. Keep everything in the foreground and middle ground exactly as it is: the timber chamber, the river stones, all labourers, "
        "their faces, clothing and poses, the baskets, carrying poles, mallets, timber beams, the dust, the light and the camera angle. "
        "Change only three things: (1) the far background and horizon becomes empty 5th-century countryside - bare low hills and open untilled land with a few trees - "
        "with no utility poles, no power lines, no buildings, no greenhouses and no regular field grid; (2) the yellow tape measure in the front-left labourer's hands "
        "becomes a plain wooden measuring stick; (3) every spade blade becomes plain wood, with no metal. Full frame, no black bars, no text, no watermark, no logo.")
v3 = rd(EP / f"11_AI_STILLS/prompt_{PID}.json"); v4 = dict(v3)
v4.update(prompt_id="PRM_MF_EP01_S04_MASTER_V04", version="V04", parent_prompt_id=PID, patch_id="PATCH_MF_EP01_S04_003", assembled_text=TEXT,
          shot_delta="S04 master frame edit of V03: remove modern horizon (poles, wires, buildings), tape measure -> wooden stick, spade blades -> wood",
          created_at=D, created_by="Image Generation Agent (Claude Code) - edit, saved before sending (D-016), pending owner OK")
w(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V04.json", v4)
w(C / "keep_change_patch_PATCH_MF_EP01_S04_003.json", {
    "patch_id": "PATCH_MF_EP01_S04_003", "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "from_version": "V03", "to_version": "V04", "fix_reason": "HISTORICAL_ISSUE",
    "keep": ["full-frame composition (no letterbox)", "chamber, stones, labourers, faces, clothing, poses", "baskets, poles, mallets, beams", "dust, light, camera angle"],
    "change": ["modern horizon (utility poles, power lines, buildings, greenhouses, field grid) -> empty early countryside",
               "yellow tape measure -> wooden measuring stick", "spade blades -> plain wood"],
    "reason": "V03 fixed letterbox and most tools but introduced modern background objects and a tape measure (SILLA_EARLY_V01 forbids modern objects). Background replacement is a large-region edit, which worked before (hero tiled roofs, D-017).",
    "requested_by": "Image Generation Agent (Claude Code) - pending owner OK", "created_at": D,
    "resulting_prompt_id": "PRM_MF_EP01_S04_MASTER_V04", "resulting_generation_id": None})

c = rd(C / "cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 56.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 56.12 credits (원로 24.12 · 군중 20 · 기준 그림 12). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "29 호출 = 56.12 credits (원로 13 · 군중 10 · 기준 그림 6). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## S04 새로 생성 V03 결과" not in s:
    s += ("\n## S04 새로 생성 V03 결과 (2 credits, 승인 6/10)\n\n"
          "`MF_EP01_S04_MASTER_V03_447da844.png` **PARTIAL** — 검은 띠 없음·공구 대부분 나무. 새 문제: 지평선의 전봇대·전깃줄·현대 건물·반듯한 논밭, 노란 줄자, 쇠 날처럼 보이는 삽 일부.\n"
          "제안: V03 편집 V04 (배경을 빈 옛 들판으로 + 줄자 → 나무 자 + 삽날 → 나무), `PATCH_MF_EP01_S04_003` 저장, 사용자 OK 대기. 대안: V01 + 검은 띠 무료 크롭 (쇠 공구 남음).\n")
r.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 54.12 credits (28 호출: 원로 13 · 군중 10 · 기준 그림 5) — KRW 환산 P-012 |", "| 소진 | 56.12 credits (29 호출: 원로 13 · 군중 10 · 기준 그림 6) — KRW 환산 P-012 |"),
             ("소진 54.12 credits, KRW 환산 P-012)", "소진 56.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "S04 새로 생성 V03" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — 기준 그림 S06 OPEN_CHAMBER V02 APPROVED (S06 2장 확정). S04 새로 생성 V03 (2 credits, 승인 6/10): 검은 띠 해결, 새 문제 = 지평선 전봇대·현대 건물, 노란 줄자, 쇠 날 삽 일부 → 편집 V04 저장, 사용자 OK 대기. EP01 소진 56.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", GID)
