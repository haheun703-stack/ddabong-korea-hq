# -*- coding: utf-8 -*-
"""Record H06 still attempt 2 (job d6326541, sent verbatim from PRM_EP01_S06_SH010_V03) as PARTIAL; approval call cap reached (2/2) -> STOP.
Save V04 + PATCH_EP01_S06_SH010_002 and a PENDING approval for owner decision (nothing sent).  Usage: python 00_SYSTEM/tools/h06_v02_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOB = "d6326541-2bc3-476a-9837-cc48cbddeee7"; GID = "GEN_EP01_S06_SH010_HIGGSFIELD_V02"; PID = "PRM_EP01_S06_SH010_V03"
OUT = "08_GENERATION_CACHE/EP01/AI_STILL/H06_V02_d6326541.png"
v3 = rd(EP / f"11_AI_STILLS/prompt_{PID}.json")
jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{JOB}.json"
w(R / jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"{D}T11:50:35Z",
           "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1, "input_images": [], "prompt": v3["assembled_text"]},
           "retrieved_at": D, "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V03)."})
CHECK = ("Owner criteria check: (1) proportion PASS - base width ~4x height (target ~3.7x), but the top is flat with a terrace ledge instead of a rounded crown; "
         "(2) modern intrusion PASS - only hills, trees and low neighbouring mounds; (3) stage PASS - nearly finished earth mound, workers smoothing the top; "
         "(4) human scale FAIL - people at the base reach ~1/4 of the mound height (target ~1/8), so the mound reads ~6 m tall instead of 12.7 m; "
         "extra issue: central attendants in white jackets with dark belts read like modern martial-arts uniforms.")
w(C / f"generation_{GID}.json", {
    "generation_id": GID, "shot_id": "EP01_S06_SH010", "stage": "STILL", "provider": "Higgsfield",
    "model": "NANO_BANANA_PRO (job_set_type nano_banana_2, 2k, 16:9, text only)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V03",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_AI_B1_001",
    "input_paths": [], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1858.48 -> 1856.48)"},
    "result_status": "PARTIAL", "failure_id": None, "started_at": f"{D}T11:50:35Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": f"D-028 D4 call 2/2 (retry, PATCH_EP01_S06_SH010_001). {CHECK} Approval cap reached -> STOP, owner decision required (no automatic 3rd call)."})
pt = rd(C / "keep_change_patch_PATCH_EP01_S06_SH010_001.json"); pt["resulting_generation_id"] = GID; w(C / "keep_change_patch_PATCH_EP01_S06_SH010_001.json", pt)
a = rd(C / "approval_APR_EP01_AI_B1_001.json")
if "2/2 사용" not in a["note"]: a["note"] += " 2/2 사용 후 종료 (1차 REJECTED, 2차 PARTIAL)."
w(C / "approval_APR_EP01_AI_B1_001.json", a)

t = v3["assembled_text"]
reps = [
 ("and the top is a wide rounded crown, not a peak;", "and the top is a smoothly rounded crown - no flat top, no terrace ledge, not a peak;"),
 ("Small groups of people stand near its base for scale; a person about 1.6 metres tall is only about one eighth of the mound's height and looks tiny against it.",
  "Small groups of people stand right at the foot of the mound and must look tiny: each person reaches only about one eighth of the mound's height, so about eight people standing on each other's shoulders would be needed to reach the top; nobody stands in the foreground near the camera."),
 ("funeral attendants in belted white, black and grey-brown hemp jackets;",
  "funeral attendants in plain white, black and grey-brown hemp jackets closed with cloth cords - not martial-arts uniforms, no white robes with dark belts;"),
 ("about 60 metres from the mound", "about 80 metres from the mound"),
]
for x, y in reps:
    assert t.count(x) == 1, x[:40]; t = t.replace(x, y)
v4 = dict(v3)
v4.update(prompt_id="PRM_EP01_S06_SH010_V04", version="V04", parent_prompt_id=PID, patch_id="PATCH_EP01_S06_SH010_002", assembled_text=t,
          shot_delta="H06 proposal: human scale 1:8 (tiny figures at the foot, none in foreground), rounded crown (no flat top/ledge), attendants not martial-arts-uniform-like, camera ~80 m",
          created_at=D, created_by="Image Generation Agent (Claude Code) - proposal saved before any sending (D-016), pending new owner approval")
w(EP / "11_AI_STILLS/prompt_PRM_EP01_S06_SH010_V04.json", v4)
w(C / "keep_change_patch_PATCH_EP01_S06_SH010_002.json", {
    "patch_id": "PATCH_EP01_S06_SH010_002", "shot_id": "EP01_S06_SH010", "from_version": "V03", "to_version": "V04", "fix_reason": "ARCHITECTURE",
    "keep": ["~4:1 width-to-height proportion", "clean early horizon (no man-made objects)", "nearly finished stage with workers on top", "low warm side light, far camera, 35mm"],
    "change": ["human scale: figures ~1/8 of mound height, none in foreground", "rounded crown instead of flat top with ledge", "attendant jackets not martial-arts-uniform-like", "camera 60 m -> 80 m"],
    "reason": "Attempt 2 (GEN_EP01_S06_SH010_HIGGSFIELD_V02) fixed proportion and horizon but people read ~1/4 of mound height (mound looks ~6 m) and the top is flat with a ledge.",
    "requested_by": "Image Generation Agent (Claude Code) - pending owner approval", "created_at": D,
    "resulting_prompt_id": "PRM_EP01_S06_SH010_V04", "resulting_generation_id": None})
w(C / "approval_APR_EP01_AI_B1_002.json", {
    "approval_id": "APR_EP01_AI_B1_002", "kind": "PAID_GENERATION", "target_id": "EP01_S06_SH010",
    "money_gate_presented": {"shot_id": "EP01_S06_SH010", "prompt_ids": ["PRM_EP01_S06_SH010_V04"],
        "provider_model": "HIGGSFIELD / NANO_BANANA_PRO, 2k, 16:9 still", "expected_attempts": 1, "estimated_cost_range": "2 credits (hard cap 2)",
        "continuity_risk": "MEDIUM - human scale 1:8 is the failed item"},
    "decision": "PENDING", "fix_reason": "ARCHITECTURE", "decided_by": "사용자", "decided_at": f"{D}T00:00:00Z",
    "note": "준비만 됨 (decided_at = 준비 시각). H06 3번째 호출은 이 새 승인 없이는 금지 (D-028 D3/D4)."})

c = rd(C / "cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 64.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 64.12 credits (원로 24.12 · 군중 20 · 기준 그림 16 · AI 샷 4). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "33 호출 = 64.12 credits (원로 13 · 군중 10 · 기준 그림 8 · AI 샷 2). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for x, y in [("| 소진 | 62.12 credits (32 호출: 원로 13 · 군중 10 · 기준 그림 8 · AI 샷 1) — KRW 환산 P-012 |", "| 소진 | 64.12 credits (33 호출: 원로 13 · 군중 10 · 기준 그림 8 · AI 샷 2) — KRW 환산 P-012 |"),
             ("소진 62.12 credits, KRW 환산 P-012)", "소진 64.12 credits, KRW 환산 P-012)")]:
    s = s.replace(x, y)
if "H06 2차" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — H06 2차 (2 credits, 승인 2/2 소진): 비율·지평선·단계 통과, **사람 대비 규모 실패 (1/4, 목표 1/8)** · 평평한 꼭대기 · 무술복 같은 옷 → PARTIAL, **STOP**. 수정안 V04 + PATCH + 새 승인(PENDING, 1회/2 credits) 저장만. EP01 소진 64.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", GID)
