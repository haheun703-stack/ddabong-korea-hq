# -*- coding: utf-8 -*-
"""Record attendant full_body method A (job 84c0fdbc, sent verbatim from V05) and save attendant step-2 prompts V03
with the same explicit fastening clause BEFORE sending (D-016).  Usage: python 00_SYSTEM/tools/crowd_attendant_v05_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"; CID = "CHAR_SILLA_ATTENDANT_GROUP_01"
JOB = "84c0fdbc-1c5c-4edd-bb35-b1836ae14288"; GID = "GEN_MP_ATTENDANT_FULL_BODY_HIGGSFIELD_V04"; PID = f"PRM_MP_{CID}_FULL_BODY_V05"
OUT = f"{CACHE}/MP_CROWD/MP_ATTENDANT_FULL_BODY_V04_84c0fdbc.png"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
jp = f"{CACHE}/provider_jobs/HF_{JOB}.json"
w(jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
       "created_at": "2026-09-13T04:50:48Z",
       "params": {"width": 2528, "height": 1696, "aspect_ratio": "3:2", "resolution": "2k", "batch_size": 1, "input_images": [],
                  "prompt": rd(f"{STILLS}/prompt_{PID}.json")["assembled_text"]},
       "retrieved_at": "2026-09-13", "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V05)."})
w(f"{CACHE}/generation_{GID}.json", {
    "generation_id": GID, "shot_id": f"MASTER_PACK:{CID}:full_body", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:2, text only)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V05",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MP_CROWD_001",
    "input_paths": [], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1888.48 -> 1886.48)"},
    "result_status": "SUCCESS", "failure_id": None, "started_at": "2026-09-13T04:50:48Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": "Method A (PATCH_MP_ATTENDANT_FULL_BODY_003). Bot check PASS: two men + one woman, all jackets wrap right over left and are closed only by plain cloth waist belts, chest fronts plain (no long ribbon ties; only a tiny inner tie knot beside the belt on two people), grey/white/black hemp, long grey skirt, straw sandals and cloth shoes, cloth cap, plain earth background. Faces differ from V01-V03 (LITE crowd, allowed)."})
pt = rd(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_003.json"); pt["resulting_generation_id"] = GID
w(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_003.json", pt)
ch = rd(f"05_HISTORY_DATABASE/characters/{CID}.json")
ch["master_pack"]["full_body"] = {"path": OUT, "generation_id": GID, "status": "DRAFT"}; ch["updated_at"] = "2026-09-13"
w(f"05_HISTORY_DATABASE/characters/{CID}.json", ch)

# attendant step-2 prompts V03: same fastening clause as V05 (saved, not sent)
FASTEN_OLD = "narrow-sleeved hip-length jackets with straight collar closing right over left, tidier than labourers; the men in narrow to medium trousers, the woman in the same jacket over a long plain skirt; plain cloth belts with minimal ornament;"
FASTEN_NEW = ("narrow-sleeved hip-length jackets with straight collar wrapping right over left; jacket fastening: NO ribbon ties and NO bows on the chest, "
              "every jacket is closed only by a plain cloth belt tied at the waist and the chest front is completely plain; the men in narrow to medium trousers, "
              "the woman in the same belted jacket over a long plain skirt;")
for slot in ("WALKING", "COSTUME_DETAIL"):
    v2 = rd(f"{STILLS}/prompt_PRM_MP_{CID}_{slot}_V02.json"); t = v2["assembled_text"]
    assert t.count(FASTEN_OLD) == 1, slot
    t = t.replace(FASTEN_OLD, FASTEN_NEW).replace("No Joseon hanbok silhouette,", "No Joseon hanbok silhouette, no goreum ribbon ties,")
    if slot == "COSTUME_DETAIL":
        t = t.replace("showing the straight collars closing right over left, the plain cloth belts,", "showing the plain chest fronts with collars wrapping right over left and no ribbon ties, the plain cloth waist belts,")
    v3 = dict(v2); v3.update(prompt_id=f"PRM_MP_{CID}_{slot}_V03", version="V03", parent_prompt_id=v2["prompt_id"], patch_id=None, assembled_text=t,
                             created_at="2026-09-13", created_by="Image Generation Agent (Claude Code) — fastening clause from V05, saved before sending (D-016)")
    w(f"{STILLS}/prompt_{v3['prompt_id']}.json", v3)

c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 36.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 36.12 credits (원로 24.12 · 군중 12 = full_body 2 + 편집 3 + 시종 재생성 1). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "19 호출 = 36.12 credits (원로 13 · 군중 6). P-012 환산율 확정 시 percent_used 계산."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)
p = R / f"{CACHE}/MP_CROWD/REVIEW_CROWD_STEP1.md"; s = p.read_text(encoding="utf-8")
if "## 방법 A 결과" not in s:
    s += ("\n## 방법 A 결과 (새로 생성, 2 credits, 승인 6/12)\n\n`MP_ATTENDANT_FULL_BODY_V04_84c0fdbc.png` **PASS** — 세 명 모두 가슴 옷고름 없음, 허리 천띠로만 여밈. "
          "얼굴은 새 인물 (LITE 군중이라 허용). 시종 2단계 문장도 같은 여밈 문구로 V03 저장.\n\n"
          "**1단계 사람 확인 대기**: 노동자 `MP_LABORER_FULL_BODY_V02_412a72bc.png` · 시종 `MP_ATTENDANT_FULL_BODY_V04_84c0fdbc.png` → OK 면 2단계 4장 (남은 6 호출).\n")
p.write_text(s, encoding="utf-8")
print("recorded", GID)
