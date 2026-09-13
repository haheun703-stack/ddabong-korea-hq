# -*- coding: utf-8 -*-
"""Crowd step 2 (D-022): record 4 jobs sent verbatim (laborer V02, attendant V03).  Usage: python 00_SYSTEM/tools/crowd_step2_record.py"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"; APR = "APR_EP01_MP_CROWD_001"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
REF = {"LABORER": ("412a72bc-f3f1-4955-8d3a-36e1e6306d1f", f"{CACHE}/MP_CROWD/MP_LABORER_FULL_BODY_V02_412a72bc.png", "V02"),
       "ATTENDANT": ("84c0fdbc-1c5c-4edd-bb35-b1836ae14288", f"{CACHE}/MP_CROWD/MP_ATTENDANT_FULL_BODY_V04_84c0fdbc.png", "V03")}
FACES = " Note: the same three faces as the full_body reference carried over despite 'faces must be different people' - acceptable for a LITE crowd pack, but avoid featuring this trio as recognisable individuals across many shots."
JOBS = [
 ("LABORER", "WALKING", "2740544f-2e9c-4c32-9a5f-af20fcc4bf3b", "PASS - three labourers walking toward camera (more frontal than side-front), middle man carries a river stone, cloth headbands, shin wraps, straw sandals/bare feet, same hemp jackets and cords, finished mounds behind."),
 ("LABORER", "COSTUME_DETAIL", "06b95492-ba48-4fcd-af09-985b9045a579", "PASS - chest-to-waist, collars right over left, cloth waist cords, sleeve ends and rough hands, coarse weave and dust; lower faces (mouth/beard) in frame."),
 ("ATTENDANT", "WALKING", "083c45d4-7308-426d-8c61-4ecdabf905e3", "PASS - side-front walking, man carries a plain wooden box, belted jackets with plain chest fronts (no ribbon ties), woman in long grey skirt and cloth shoes, straw sandals."),
 ("ATTENDANT", "COSTUME_DETAIL", "d2a6b5ce-d52e-46c5-8cb3-1ef5a0c1a40e", "PASS - plain chest fronts wrapping right over left, cloth waist belts, sleeve ends, wrists and hands clear; small inner tie knot beside each belt (not a chest ribbon). Fabric reads clean and new rather than hand-woven - minor."),
]
gids = []
for grp, slot, job, check in JOBS:
    cid = f"CHAR_SILLA_{grp}_GROUP_01"; ref_job, ref_path, ver = REF[grp]; pid = f"PRM_MP_{cid}_{slot}_{ver}"
    jp = f"{CACHE}/provider_jobs/HF_{job}.json"
    w(jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": "2026-09-13T04:56:20Z",
           "params": {"width": 2528, "height": 1696, "aspect_ratio": "3:2", "resolution": "2k", "batch_size": 1,
                      "input_images": [{"id": ref_job, "type": "image_job"}], "prompt": rd(f"{STILLS}/prompt_{pid}.json")["assembled_text"]},
           "retrieved_at": "2026-09-13", "note": f"generate_image_batch/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt {ver})."})
    gid = f"GEN_MP_{grp}_{slot}_HIGGSFIELD_V01"; gids.append(gid)
    out = f"{CACHE}/MP_CROWD/MP_{grp}_{slot}_V01_{job[:8]}.png"
    w(f"{CACHE}/generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_PACK:{cid}:{slot.lower()}", "stage": "STILL", "provider": "Higgsfield",
        "model": f"Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:2, image_references=full_body job {ref_job[:8]})",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": ver,
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": APR,
        "input_paths": [ref_path], "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {job} (step-2 batch of 4: balance 1886.48 -> 1878.48)"},
        "result_status": "SUCCESS", "failure_id": None, "started_at": "2026-09-13T04:56:20Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"D-022 crowd step 2. Bot check: {check}{FACES}"})
    ch = rd(f"05_HISTORY_DATABASE/characters/{cid}.json")
    ch["master_pack"][slot.lower()] = {"path": out, "generation_id": gid, "status": "DRAFT"}; ch["updated_at"] = "2026-09-13"
    w(f"05_HISTORY_DATABASE/characters/{cid}.json", ch)
c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 44.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 44.12 credits (원로 24.12 · 군중 20 = full_body 2 + 편집 3 + 시종 재생성 1 + 2단계 4). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산."
c["note"] = "23 호출 = 44.12 credits (원로 13 · 군중 10). P-012 환산율 확정 시 percent_used 계산."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)
rows = "\n".join(f"| {g.lower()} {s.lower()} | `MP_{g}_{s}_V01_{j[:8]}.png` | {k} | ☐ APPROVE ☐ FIX |" for g, s, j, k in JOBS)
(R / f"{CACHE}/MP_CROWD/REVIEW_CROWD_STEP2.md").write_text(f"""# 군중 LITE 2단계 (walking · costume_detail) — 사람 검수 시트

> 2026-09-13 · 승인 `{APR}` (D-022) · 4 호출 / 4 성공 · 8 credits (한도 12 중 10 사용)
> 참조 = 승인된 full_body (노동자 412a72bc · 시종 84c0fdbc). 전송 = 저장 문장 그대로 (D-016).

| 무리·슬롯 | 파일 | 봇 판정 | 사람 검수 |
|---|---|---|---|
{rows}

## 사람이 볼 점

1. 참조 그림의 **얼굴이 그대로 따라옴** (문장은 '다른 사람'). 군중 LITE 는 복식 기준이라 허용 판단, 단 영상에서 이 3인조를 여러 컷에 알아볼 정도로 반복하지 않기.
2. 노동자 걷기는 옆-앞보다 정면에 가깝다.
3. 시종 옷감이 손으로 짠 삼베보다 깨끗한 새 리넨처럼 보인다 — 허용 범위인지.

모두 APPROVE 면 노동자·시종 LITE Pack 3/3 → 두 무리 CHARACTER_MASTER_APPROVED → **P2 Character Master 완료**.
""", encoding="utf-8")
print("recorded", gids)
