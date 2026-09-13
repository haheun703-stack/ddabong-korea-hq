# -*- coding: utf-8 -*-
"""Attendant full_body method change (user chose A, 2026-09-13): fresh text-only generation with explicit no-chest-ties fastening.
Saves V05 + PATCH_MP_ATTENDANT_FULL_BODY_003 BEFORE sending (D-016).  Usage: python 00_SYSTEM/tools/crowd_attendant_v05_prepare.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"; CID = "CHAR_SILLA_ATTENDANT_GROUP_01"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
TEXT = ("Exactly THREE different people, two men and one woman, nobody else. Early Silla Korea, 5th century, funeral attendants and artisans. "
        "FULL BODY: head to toe, standing side by side, arms relaxed, plain flat earth background, whole costume visible. "
        "Varied realistic Korean faces, ages 20s to 50s, calm focused expressions, natural builds, hair neatly tied in a topknot with cloth or a simple cloth cap for the men, neatly tied hair for the woman; no single hero face. "
        "Costume: finer undyed hemp or ramie plain-weave, narrow-sleeved hip-length jackets with straight collar wrapping right over left. "
        "Jacket fastening: NO ribbon ties and NO bows on the chest; every jacket on all three people is closed only by a plain cloth belt tied at the waist, and the chest front is completely plain. "
        "The men in narrow to medium trousers, the woman in the same belted jacket over a long plain skirt; low cloth shoes or straw sandals; colours only undyed white, black and grey-brown. "
        "Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy, natural proportions. "
        "No Joseon hanbok silhouette, no goreum ribbon ties, no court robes, no fantasy priest robes, no Chinese imperial dress, no official colours (no purple, crimson, blue or yellow garments). "
        "No tiled roofs, no buildings. No text, no watermark, no logo.")
v4 = rd(f"{STILLS}/prompt_PRM_MP_{CID}_FULL_BODY_V04.json"); v5 = dict(v4)
v5.update(prompt_id=f"PRM_MP_{CID}_FULL_BODY_V05", version="V05", parent_prompt_id=v4["prompt_id"], patch_id="PATCH_MP_ATTENDANT_FULL_BODY_003",
          shot_delta="full_body fresh generation: jackets closed only by waist belt, no chest ribbon ties", assembled_text=TEXT, reference_images=[],
          created_at="2026-09-13", created_by="Image Generation Agent (Claude Code) — method change A, saved before sending (D-016)")
w(f"{STILLS}/prompt_{v5['prompt_id']}.json", v5)
w(f"{CACHE}/keep_change_patch_PATCH_MP_ATTENDANT_FULL_BODY_003.json", {
    "patch_id": "PATCH_MP_ATTENDANT_FULL_BODY_003", "shot_id": f"MASTER_PACK:{CID}:full_body", "from_version": "V04", "to_version": "V05",
    "fix_reason": "HISTORICAL_ISSUE",
    "keep": ["group of two men and one woman", "finer undyed hemp/ramie", "white/black/grey-brown palette", "cloth headwear", "long skirt for the woman", "plain earth background", "style B"],
    "change": ["NOT an edit: fresh text-only generation (faces may change, LITE crowd)", "explicit fastening: no chest ribbon ties, jackets closed only by waist belt"],
    "reason": "Two edits (V03, V04) left chest ribbon ties on at least one man. D-021: stop edit loop; user chose method A (fresh generation with explicit fastening wording).",
    "requested_by": "사용자 (2026-09-13, 방법 A)", "created_at": "2026-09-13",
    "resulting_prompt_id": v5["prompt_id"], "resulting_generation_id": None})
print(TEXT)
