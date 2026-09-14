# -*- coding: utf-8 -*-
"""Elite Master Pack batch 2 (remaining 6 + back_view): save exact texts to send as V02 prompts + PENDING approval.
Nothing is sent. Sent Prompt Rule (D-016): these assembled_text values are sent verbatim after the user approves.
Usage:  python 00_SYSTEM/tools/batch2_prepare.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = "2026-09-13"; CHAR = "CHAR_SILLA_ELITE_OBSERVER_01"
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

REFS = {"hero_V03": "5de27748-f100-47e0-af23-1bdb68466bb7", "full_body_V01": "5681f1e0-fe07-4fc3-b36c-f512dc7a2992"}
ID1 = "Use the reference images as the exact same person: keep his face identity, age, skin, hair, cap, and costume identical. Exactly ONE person, alone."
STYLE = "Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy, natural proportions."
COSTUME = ("Same costume: pale birch-bark style conical cap, muted dusty blue silk outer robe reaching below the knee with straight collar "
           "closing right over left, short outer sleeves over an undyed ivory hemp inner jacket with long narrow sleeves, wide grey-brown "
           "trousers, restrained bronze plaque belt with small bronze pendants, ankle-high leather boots over socks.")
TAIL = "Palette only muted blue, ivory, grey-brown, bronze. No red, no crimson, no purple. No gold crown, no gold belt. No text, no watermark, no logo."
SLOTS = [
 ("THREE_QUARTER_RIGHT", "3:4", ID1, "THREE-QUARTER VIEW FROM THE RIGHT: his head and body turned about 45 degrees so the camera sees his right side, neutral restrained expression, head and shoulders, soft even daylight, plain muted earth-toned background, no scaffolding, no buildings.", " No second person."),
 ("PROFILE", "3:4", ID1, "TRUE SIDE PROFILE: head and body turned 90 degrees to face screen left, the full silhouette of the conical cap clearly visible, neutral expression, head and shoulders, soft even daylight, plain muted earth-toned background, no buildings.", " No second person."),
 ("NEUTRAL_STANDING", "2:3", ID1, "NEUTRAL STANDING: full body head to toe facing the camera, weight even on both feet, hands relaxed at his sides, calm neutral expression, feet visible, plain flat earth background, no buildings.", " No second person."),
 ("WALKING", "2:3", ID1, "WALKING: full body head to toe, mid-stride natural walking gait seen from a side-front angle, arms swinging slightly, calm expression, feet visible, plain flat earth ground, no buildings.", " No second person."),
 ("COSTUME_DETAIL", "3:4", ID1, "COSTUME DETAIL: close-up from chest to waist showing the straight collar closing right over left, the robe closure, the bronze plaque belt with pendants, and the sleeve ends with both hands in frame; silk and hemp weave visible; face cropped out above the chin; soft even daylight, plain background.", " No second person."),
 ("EXPRESSION_SHEET", "3:2", "Use the reference images as the exact same man: keep his face identity, age, skin, hair, cap, and costume identical. Show only this one man, repeated.",
  "EXPRESSION SHEET: one image with five head-and-shoulders portraits of this same man side by side in a single row on a plain light grey background, identical lighting and framing, restrained expressions only, left to right: neutral, attentive, concerned, resolved, quiet grief; no exaggeration.", " No other people, no labels."),
 ("BACK_VIEW", "2:3", ID1, "BACK VIEW: full body seen from directly behind, standing still and looking away toward a distant earth mound under construction, shoulders and the conical cap silhouette clear, face not visible, soft daylight, plain earth ground, no buildings.", " No second person."),
]

pids = []
for slot, ar, ident, delta, extra in SLOTS:
    v1 = rd(f"{STILLS}/prompt_PRM_MP_{CHAR}_{slot}_V01.json")
    text = " ".join([ident, delta, STYLE, COSTUME, TAIL]) + extra
    v2 = dict(v1)
    v2.update(prompt_id=f"PRM_MP_{CHAR}_{slot}_V02", assembled_text=text, reference_images=[f"character_pack:{CHAR}"], version="V02",
              parent_prompt_id=v1["prompt_id"], patch_id=None, created_at=D,
              created_by="Image Generation Agent (Claude Code) — batch 2, saved before sending (D-016); condensed reference-image form proven in batch 1")
    w(f"{STILLS}/prompt_{v2['prompt_id']}.json", v2)
    pids.append((v2["prompt_id"], ar))

w(f"{CACHE}/approval_APR_EP01_MP_ELITE_BATCH2_001.json", {
    "approval_id": "APR_EP01_MP_ELITE_BATCH2_001", "kind": "PAID_GENERATION", "target_id": CHAR,
    "money_gate_presented": {
        "shot_id": f"MASTER_PACK:{CHAR}:batch2",
        "prompt_ids": [p for p, _ in pids],
        "aspect_ratios": {p: ar for p, ar in pids},
        "image_references": REFS,
        "provider_model": "Higgsfield / Nano Banana Pro (job type nano_banana_2), 2k, image_references = hero V03 + full_body V01 (both APPROVED)",
        "expected_attempts": 10,
        "estimated_cost_range": "14–20 credits (2 credits x 7 images, + up to 3 FIX retries)",
        "continuity_risk": "MEDIUM - face and costume anchored by 4 APPROVED images; expression_sheet (5 faces in one image) and walking are the riskiest"},
    "decision": "PENDING", "fix_reason": None, "decided_by": "사용자", "decided_at": f"{D}T00:00:00Z",
    "note": "준비만 됨 (decided_at = 준비 시각, 결정 시 갱신). 사용자 APPROVE 전 전송 금지. 전송은 각 prompt 의 assembled_text 그대로."})
print("saved", len(pids), "prompts + PENDING approval")
