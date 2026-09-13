# -*- coding: utf-8 -*-
"""2026-09-13 full-review fixes 1-5 (no paid generation).
Usage:  python 00_SYSTEM/tools/fix_review_20260913.py
 1) store the prompts actually sent in batch 1 as new prompt versions (+ keep_change_patch for hero retry)
 2) record requested model name AND provider job type (provider_job + params file)
 4) negative arrays = DDABONG_NEGATIVE + era/location/costume lock 'Forbidden:' items (unsent prompts only)
 5) episode.json budget.spent aligned with cost file
 (3 = validator rules, edited in 00_SYSTEM/schemas/validate.py)
Prompt texts below are copied verbatim from Higgsfield job_status raw_data (retrieved 2026-09-13).
"""
import json, re
from datetime import datetime, timezone
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = "2026-09-13"; SENT = "2026-09-11"; BY = "Claude Code (review fix 2026-09-13)"
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"; LOCKS = R / "06_PROMPT_LIBRARY/locks"
CHAR = "CHAR_SILLA_ELITE_OBSERVER_01"

def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- lock-derived negative (same logic as validate.py required_negative) ----
def forbidden_items(lock_id):
    p = LOCKS / f"{lock_id}.json"
    if not lock_id or not p.exists(): return []
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("items"): return list(d["items"])
    m = re.search(r"Forbidden:\s*(.*?)\.?\s*$", d["text"])
    if not m: return []
    body = m.group(1)
    return [s.strip() for s in body.split(";" if ";" in body else ",") if s.strip()]

def required_negative(locks):
    ids = ["DDABONG_NEGATIVE_V01", locks.get("era"), locks.get("location")]
    for cc in locks.get("character_costume", []): ids += cc.split("+")
    out = []
    for i in ids:
        for it in forbidden_items(i):
            if it not in out: out.append(it)
    return out

def full_negative(prompt):
    neg = list(prompt.get("negative") or [])
    return neg + [i for i in required_negative(prompt["locks"]) if i not in neg]

# ---- batch 1 jobs, verbatim ----
REF = [{"id": "c7a5cc92-3f36-4b40-8071-84da9f6c6441", "type": "image_job"}]
NB = lambda wd, ht, ar, refs: {"width": wd, "height": ht, "aspect_ratio": ar, "resolution": "2k", "batch_size": 1, "input_images": refs}
JOBS = [
 dict(gen="GEN_MP_ELITE_HERO_HIGGSFIELD_V01", slot="HERO", ver="V02", parent="V01", job="35407202-2db4-46ef-b52f-6fef00e29bac",
      type="text2image_soul_v2", name="Higgsfield Soul 2.0", ts=1789133763.355848,
      model="Higgsfield Soul 2.0 (job_set_type text2image_soul_v2, 2k, 3:4, seed 238493, style General)",
      params={"width": 1536, "height": 2048, "batch_size": 1, "seed": 238493, "enhance_prompt": False, "quality": "1080p",
              "style_id": "3db34ab5-3439-4317-9e03-08dc30852e69", "style_name": "General"},
      prompt="hero portrait, chest-up, three-quarter light, calm direct gaze. Photorealistic cinematic historical documentary. Natural physical proportions. Historically plausible reconstruction. Realistic materials. Natural lighting. No fantasy. No modern objects. No text. No logos. No excessive saturation. No glossy AI look. No malformed anatomy. Early Silla, Gyeongju royal capital, 5th to early 6th century. Elite burial construction context. Modest timber work spaces, no palace spectacle. CHAR_SILLA_ELITE_OBSERVER_01 (Senior elite observer): senior member of the elite watching mound construction and funeral preparation from a distance; not the deceased, not a king. Face: realistic Korean facial proportions, restrained expression, not a portrait of any named historical person. Body: natural, medium build, upright still posture. Hair: tied up, period-appropriate. Age: 40s-50s. Skin: natural texture, weathered, no gloss. Costume: Silla senior elite observer: silk outer robe over hemp/ramie inner jacket; narrow-sleeved jacket under a longer outer robe, straight collar closing right over left; plaque belt with hanging pendants in restrained bronze - never a copy of the Cheonmachong gold belt; birch-bark style cap or simple formal cap - never a gold or gilt-bronze crown; muted blue tones, never crimson, never purple. DDABONG Documentary Reenactment (style B): realistic Korean facial proportions, natural skin texture with subtle imperfections, restrained expressions, historically researched clothing, natural documentary lighting, not glamorous, not glossy, not fantasy-drama, not generic Joseon hanbok. Negative: Joseon dynasty hanbok, gat hats, Ming or Qing court robes, samurai armor, fantasy armor, fantasy crown, gold crown, silver or gold belt plaques, purple, crimson, text, watermark, glossy skin, malformed anatomy.",
      why="V01 assembled_text was not sent verbatim: condensed (location lock dropped, costume lock shortened, inline negative) to fit a single-still prompt."),
 dict(gen="GEN_MP_ELITE_HERO_HIGGSFIELD_V02", slot="HERO", ver="V03", parent="V02", job="c7a5cc92-3f36-4b40-8071-84da9f6c6441",
      type="nano_banana_2", name="Nano Banana Pro", ts=1789133861.763083,
      model="Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:4)", params=NB(1792, 2400, "3:4", []),
      prompt="Exactly ONE person, alone in frame, nobody else. Hero portrait, chest-up, three-quarter light, calm direct gaze. Photorealistic cinematic historical documentary still, style B Documentary Reenactment: realistic Korean facial proportions, natural skin texture with subtle imperfections, restrained expression, natural documentary lighting, not glamorous, not glossy, not fantasy-drama. Setting: Early Silla, Gyeongju, 5th century, modest timber work yard, soft out-of-focus wooden scaffolding and earth behind him, no palace, no red walls. Subject: CHAR_SILLA_ELITE_OBSERVER_01, a senior elite man in his late 40s to 50s, medium build, upright still posture, weathered skin, hair tied up under a pale birch-bark style cap (simple formal cap, no crown, no gold). Costume: muted dusty blue silk outer robe with straight collar closing right over left, over an undyed ivory hemp inner jacket with narrow sleeves; a restrained bronze plaque belt with small hanging bronze pendants; entire palette muted blue, ivory, grey-brown and bronze only. Absolutely no red, no crimson, no purple garments. No text, no letters, no watermark, no signature, no logo anywhere in the image. No second person, no guard, no soldier, no armour, no gat hat, no Joseon hanbok, no Ming or Qing robes, no gold crown.",
      why="Retry after V02 REJECTED; see PATCH_MP_ELITE_HERO_001. Prompt was rewritten, not minimally patched, and the model was switched."),
 dict(gen="GEN_MP_ELITE_FRONT_HIGGSFIELD_V01", slot="FRONT", ver="V02", parent="V01", job="ae0b4062-481f-46e0-919e-28289aaba8e0",
      type="nano_banana_2", name="Nano Banana Pro", ts=1789133941.384887,
      model="Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:4, input_images=hero job c7a5cc92)", params=NB(1792, 2400, "3:4", REF),
      prompt="Use the reference image as the exact same person: keep his face identity, age, skin, hair, cap, and costume identical. Exactly ONE person, alone. FRONT VIEW: straight-on front view, neutral expression, full head and shoulders, flat even daylight, plain muted earth-toned background, no scaffolding, no buildings. Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy. Same costume: pale birch-bark style conical cap, muted dusty blue silk outer robe with straight collar closing right over left over an undyed ivory hemp inner jacket, restrained bronze plaque belt with small bronze pendants. Palette only muted blue, ivory, grey-brown, bronze. No red, no crimson, no purple. No text, no watermark, no logo. No second person.",
      why="V01 assembled_text was not sent verbatim: reference-image identity form, condensed costume, inline negative."),
 dict(gen="GEN_MP_ELITE_THREE_QUARTER_LEFT_HIGGSFIELD_V01", slot="THREE_QUARTER_LEFT", ver="V02", parent="V01", job="8d82a4c5-cd4f-4605-83b7-d5ab5fb3e350",
      type="nano_banana_2", name="Nano Banana Pro", ts=1789133945.926826,
      model="Nano Banana Pro (job_set_type nano_banana_2, 2k, 3:4, input_images=hero job c7a5cc92)", params=NB(1792, 2400, "3:4", REF),
      prompt="Use the reference image as the exact same person: keep his face identity, age, skin, hair, cap, and costume identical. Exactly ONE person, alone. THREE-QUARTER VIEW FROM THE LEFT: his head and body turned about 45 degrees so the camera sees his left side, neutral restrained expression, head and shoulders, soft even daylight, plain muted earth-toned background, no scaffolding, no buildings. Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy. Same costume: pale birch-bark style conical cap, muted dusty blue silk outer robe with straight collar closing right over left over an undyed ivory hemp inner jacket, restrained bronze plaque belt with small bronze pendants. Palette only muted blue, ivory, grey-brown, bronze. No red, no crimson, no purple. No text, no watermark, no logo. No second person.",
      why="V01 assembled_text was not sent verbatim: reference-image identity form, condensed costume, inline negative."),
 dict(gen="GEN_MP_ELITE_FULL_BODY_HIGGSFIELD_V01", slot="FULL_BODY", ver="V02", parent="V01", job="5681f1e0-fe07-4fc3-b36c-f512dc7a2992",
      type="nano_banana_2", name="Nano Banana Pro", ts=1789133949.753476,
      model="Nano Banana Pro (job_set_type nano_banana_2, 2k, 2:3, input_images=hero job c7a5cc92)", params=NB(1696, 2528, "2:3", REF),
      prompt="Use the reference image as the exact same person: keep his face identity, age, skin, hair, cap, and costume identical. Exactly ONE person, alone. FULL BODY: head to toe, standing upright and still, arms relaxed at his sides, feet visible, plain flat earth background, no scaffolding, no buildings, whole costume visible. Photorealistic historical documentary still, style B Documentary Reenactment, natural skin texture, not glossy, natural proportions. Same costume: pale birch-bark style conical cap, muted dusty blue silk outer robe reaching below the knee with straight collar closing right over left, over an undyed ivory hemp inner jacket with narrow sleeves, wide grey-brown trousers, restrained bronze plaque belt with small bronze pendants at the waist, ankle-high leather boots over socks. Palette only muted blue, ivory, grey-brown, bronze. No red, no crimson, no purple. No gold crown, no gold belt. No text, no watermark, no logo. No second person.",
      why="V01 assembled_text was not sent verbatim: reference-image identity form, condensed costume, inline negative."),
]
PATCH = "PATCH_MP_ELITE_HERO_001"

superseded = set()
for j in JOBS:
    pid_new = f"PRM_MP_{CHAR}_{j['slot']}_{j['ver']}"
    pid_parent = f"PRM_MP_{CHAR}_{j['slot']}_{j['parent']}"
    superseded.add(pid_parent)
    # (2) provider job params (result URLs omitted)
    jp = f"{CACHE}/provider_jobs/HF_{j['job']}.json"
    w(jp, {"provider": "Higgsfield", "job_id": j["job"], "job_set_type": j["type"], "display_name": j["name"], "status": "completed",
           "created_at": datetime.fromtimestamp(j["ts"], timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "params": dict(j["params"], prompt=j["prompt"]), "retrieved_at": D,
           "note": "Higgsfield job_status raw_data. Result/CDN URLs omitted. params.prompt is the text actually sent."})
    # (1) prompt version = text actually sent
    base = rd(f"{STILLS}/prompt_{pid_parent}.json")  # HERO_V02 is written earlier in this loop
    new = dict(base)
    new.update(prompt_id=pid_new, assembled_text=j["prompt"], version=j["ver"], parent_prompt_id=pid_parent,
               patch_id=PATCH if pid_new.endswith("HERO_V03") else None, created_at=SENT,
               reference_images=[f"character_pack:{CHAR}"] if j["params"].get("input_images") else [],
               created_by=f"Image Generation Agent (Claude Code) — sent {SENT}, recorded {D}")
    new["negative"] = full_negative(base)
    w(f"{STILLS}/prompt_{pid_new}.json", new)
    # generation record
    gp = f"{CACHE}/generation_{j['gen']}.json"; g = rd(gp)
    g["model"] = j["model"]; g["prompt_id"] = pid_new; g["prompt_version"] = j["ver"]
    job = {"job_id": j["job"], "job_set_type": j["type"], "display_name": j["name"], "params_path": jp}
    g = {k2: v2 for k, v in g.items() if k != "provider_job"
         for k2, v2 in ([(k, v), ("provider_job", job)] if k == "model" else [(k, v)])}  # provider_job right after model
    if "[review fix 2026-09-13]" not in (g["notes"] or ""):
        g["notes"] = (g["notes"] or "") + f" [review fix 2026-09-13] Sent prompt stored as {pid_new} (parent {pid_parent}). {j['why']}"
    w(gp, g)

# keep_change_patch for the hero retry
w(f"{CACHE}/keep_change_patch_{PATCH}.json", {
    "patch_id": PATCH, "shot_id": f"MASTER_PACK:{CHAR}:hero", "from_version": "V02", "to_version": "V03", "fix_reason": "AI_ARTIFACT",
    "keep": ["face identity (Korean, 40s-50s, restrained)", "birch-bark style cap", "bronze plaque belt with pendants", "muted blue outer robe", "timber work-yard background"],
    "change": ["single subject only (second armoured figure removed)", "inner garment ivory, no red/crimson/purple", "no text / watermark",
               "NOT a failed item: model switched soul_2 -> Nano Banana Pro", "NOT minimal: prompt rewritten in full (see PRM_..._HERO_V03)"],
    "reason": "hero V02 attempt (GEN_MP_ELITE_HERO_HIGGSFIELD_V01) REJECTED: second figure in armour, crimson inner garment, hallucinated watermark. Recorded retroactively on 2026-09-13; the retry changed more than the failed items (model + full rewrite).",
    "requested_by": "Image Generation Agent (Claude Code)", "created_at": SENT,
    "resulting_prompt_id": f"PRM_MP_{CHAR}_HERO_V03", "resulting_generation_id": "GEN_MP_ELITE_HERO_HIGGSFIELD_V02"})

# (4) negative for prompts never sent (superseded V01s stay frozen as records)
touched = []
for f in sorted((R / "02_SEASONS/S01/EP01").glob("1[12]_AI_*/prompt_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    if d["prompt_id"] in superseded: continue
    neg = full_negative(d)
    if neg != d.get("negative"):
        d["negative"] = neg; w(f.relative_to(R), d); touched.append(d["prompt_id"])

# cost note wording
c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["note"] = c["note"].replace("nano_banana_pro 2 x 4", "Nano Banana Pro [job_set_type nano_banana_2] 2 x 4")
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

# (5) episode budget aligned with cost file
ep = rd("02_SEASONS/S01/EP01/episode.json")
ep["budget"]["spent"] = c["budget"]["spent"]
if "P-012" not in ep["budget"]["note"]:
    ep["budget"]["note"] += f" 소진 Higgsfield 8.12 credits (배치 1) — KRW 환산율 미정 (P-012) → spent null. 정본: {CACHE}/cost_COST_EP01_20260911.json"
w("02_SEASONS/S01/EP01/episode.json", ep)

# review sheet model column
p = R / f"{CACHE}/MP_ELITE/REVIEW_BATCH1.md"; s = p.read_text(encoding="utf-8")
s = s.replace("| nano_banana_pro", "| Nano Banana Pro (nano_banana_2)")
if "실제 전송 프롬프트" not in s:
    s = s.replace("## 검수 포인트", "> 실제 전송 프롬프트 (2026-09-13 기록): hero V01 시도 → `PRM_…_HERO_V02`, hero V02 → `PRM_…_HERO_V03` (+ `PATCH_MP_ELITE_HERO_001`), front · three_quarter_left · full_body → 각 `_V02`. 원문 = `provider_jobs/HF_<job>.json`.\n\n## 검수 포인트", 1)
p.write_text(s, encoding="utf-8")

print("prompts negative updated:", len(touched))
print("\n".join(touched))
