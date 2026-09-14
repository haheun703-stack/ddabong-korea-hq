# -*- coding: utf-8 -*-
"""Crowd LITE Master Packs (laborer + attendant): save exact texts to send as V02 prompts + PENDING approval. Nothing is sent.
Step 1 = full_body (text only). Step 2 = walking + costume_detail with that group's APPROVED full_body as costume reference.
Usage:  python 00_SYSTEM/tools/crowd_prepare.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = "2026-09-13"; CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

STYLE = "Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy, natural proportions."
TAIL = "No tiled roofs, no buildings. No text, no watermark, no logo."
REF = "Use the reference image for the costume only: keep the clothing identical in cut, fabric and colour; the faces must be different people."
GROUPS = {
 "CHAR_SILLA_LABORER_GROUP_01": dict(
   who="Exactly THREE different men, nobody else. Early Silla Korea, 5th century, burial-mound construction labourers.",
   people="Varied realistic Korean faces, ages 20s to 40s, lean working builds, mixed heights, sun-weathered dusty skin, hair in a topknot with a cloth band or a bare topknot; no single hero face, no close-up acting.",
   costume="Costume on all three: undyed coarse hemp plain-weave short jacket to hip length with narrow sleeves and straight collar closing right over left, narrow trousers bound at the shin, plain cloth waist cord with no metal, straw sandals or bare feet; colours only natural white, raw fibre and black; worn, dusty cloth.",
   neg="No Joseon hanbok silhouette, no gat hat, no Ming or Qing dress, no samurai elements, no modern fabric, no purple, crimson, blue or yellow garments.",
   walk="WALKING: full body, the three labourers walking mid-stride from a side-front angle with natural gait, one carrying a river stone against his chest, plain flat earth ground.",
   detail="COSTUME DETAIL: close-up from chest to waist of the three labourers standing side by side, showing the straight collars closing right over left, the plain cloth waist cords, the narrow sleeve ends and their rough working hands; coarse hemp weave visible; faces cropped out above the chin; soft daylight, plain earth background."),
 "CHAR_SILLA_ATTENDANT_GROUP_01": dict(
   who="Exactly THREE different people, two men and one woman, nobody else. Early Silla Korea, 5th century, funeral attendants and artisans.",
   people="Varied realistic Korean faces, ages 20s to 50s, calm focused expressions, natural builds, hair neatly tied in a topknot with cloth or a simple cloth cap for the men, neatly tied hair for the woman; no single hero face.",
   costume="Costume: finer undyed hemp or ramie plain-weave, narrow-sleeved hip-length jackets with straight collar closing right over left, tidier than labourers; the men in narrow to medium trousers, the woman in the same jacket over a long plain skirt; plain cloth belts with minimal ornament; low cloth shoes or straw sandals; colours only undyed white, black and grey-brown.",
   neg="No Joseon hanbok silhouette, no court robes, no fantasy priest robes, no Chinese imperial dress, no official colours (no purple, crimson, blue or yellow garments).",
   walk="WALKING: full body, the three attendants walking mid-stride from a side-front angle with calm natural gait, one man holding a small plain wooden box with both hands, plain flat earth ground.",
   detail="COSTUME DETAIL: close-up from chest to waist of the three attendants standing side by side, showing the straight collars closing right over left, the plain cloth belts, the narrow sleeve ends and wrists, and their hands clearly; ramie and hemp weave visible; faces cropped out above the chin; soft daylight, plain earth background."),
}
FULL = "FULL BODY: head to toe, standing side by side, arms relaxed, plain flat earth background, whole costume visible."

prompts = []
for cid, g in GROUPS.items():
    texts = {
        "FULL_BODY": " ".join([g["who"], FULL, g["people"], g["costume"], STYLE, g["neg"], TAIL]),
        "WALKING": " ".join([REF, g["who"], g["walk"], g["people"], g["costume"], STYLE, g["neg"], TAIL]),
        "COSTUME_DETAIL": " ".join([REF, g["who"], g["detail"], g["costume"], STYLE, g["neg"], TAIL]),
    }
    for slot, text in texts.items():
        v1 = rd(f"{STILLS}/prompt_PRM_MP_{cid}_{slot}_V01.json")
        v2 = dict(v1)
        v2.update(prompt_id=f"PRM_MP_{cid}_{slot}_V02", assembled_text=text, version="V02", parent_prompt_id=v1["prompt_id"], patch_id=None,
                  reference_images=[] if slot == "FULL_BODY" else [f"character_pack:{cid}"], created_at=D,
                  created_by="Image Generation Agent (Claude Code) — crowd LITE pack, saved before sending (D-016)")
        w(f"{STILLS}/prompt_{v2['prompt_id']}.json", v2)
        prompts.append(v2["prompt_id"])

w(f"{CACHE}/approval_APR_EP01_MP_CROWD_001.json", {
    "approval_id": "APR_EP01_MP_CROWD_001", "kind": "PAID_GENERATION", "target_id": "CHAR_SILLA_LABORER_GROUP_01 + CHAR_SILLA_ATTENDANT_GROUP_01",
    "money_gate_presented": {
        "shot_id": "MASTER_PACK:CROWD_LITE:EP01",
        "prompt_ids": prompts,
        "aspect_ratios": {p: "3:2" for p in prompts},
        "steps": "1) FULL_BODY x2 (text only) -> human check -> 2) WALKING + COSTUME_DETAIL x2 each, image_references = that group's APPROVED full_body",
        "provider_model": "Higgsfield / Nano Banana Pro (job type nano_banana_2), 2k, 3:2",
        "expected_attempts": 9,
        "estimated_cost_range": "12–18 credits (2 credits x 6 images, + up to 3 FIX retries)",
        "continuity_risk": "LOW-MEDIUM - LITE_CROWD (no recurring face); costume consistency anchored by step-1 full_body"},
    "decision": "PENDING", "fix_reason": None, "decided_by": "사용자", "decided_at": f"{D}T00:00:00Z",
    "note": "준비만 됨 (decided_at = 준비 시각, 결정 시 갱신). 사용자 APPROVE 전 전송 금지. 전송은 각 prompt 의 assembled_text 그대로."})
print("saved", len(prompts), "crowd prompts + PENDING approval")
