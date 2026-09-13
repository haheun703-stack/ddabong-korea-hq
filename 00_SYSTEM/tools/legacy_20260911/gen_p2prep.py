# -*- coding: utf-8 -*-
"""P2 prep (no paid generation): lock library, master-pack prompts, AI shot prompts, camera drafts, master_frame stubs."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"; BY = "Image/Video Generation Agent (Claude Code)"
EP = "02_SEASONS/S01/EP01"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): p = R / p; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

era = rd("05_HISTORY_DATABASE/era/SILLA_EARLY.json"); loc = rd("05_HISTORY_DATABASE/locations/LOC_CHEONMACHONG_V01.json")
COS = {c: rd(f"05_HISTORY_DATABASE/costumes/{c}.json") for c in ("COSTUME_SILLA_LABORER_A01", "COSTUME_SILLA_ATTENDANT_A01", "COSTUME_SILLA_ELITE_A01")}
CH = {c: rd(f"05_HISTORY_DATABASE/characters/{c}.json") for c in ("CHAR_SILLA_ELITE_OBSERVER_01", "CHAR_SILLA_LABORER_GROUP_01", "CHAR_SILLA_ATTENDANT_GROUP_01")}

# ---------- 1. lock library (정본 §8) ----------
GLOBAL = "Photorealistic cinematic historical documentary. Natural physical proportions. Historically plausible reconstruction. Realistic materials. Natural lighting. No fantasy. No modern objects. No text. No logos. No excessive saturation. No glossy AI look. No malformed anatomy. No arbitrary architecture changes."
ERA = ("Early Silla, Gyeongju royal capital, 5th to early 6th century. Elite burial construction context. Modest timber work spaces, no palace spectacle. Forbidden: " + "; ".join(era["forbidden_anachronisms"]) + ".")
LOCT = (f"Cheonmachong under construction, Gyeongju: stone-mound wooden-chamber tomb. Wooden outer chamber {loc['spatial_lock']['wooden_outer_chamber_m']['length']} x {loc['spatial_lock']['wooden_outer_chamber_m']['width']} m, coffin inside, river stones piled above and around the chamber, earth mound finishing at about {loc['spatial_lock']['mound_diameter_m']} m diameter and {loc['spatial_lock']['mound_height_m']} m height. Layer order: coffin and grave-goods chest, wooden chamber, stones, earth. Do not invent stone-pile thickness, work duration, headcount or ritual order.")
COS_EN = {
 "COSTUME_SILLA_LABORER_A01": "Silla labourer (PROBABLE, CLM_SILLA_COSTUME_001-007): undyed coarse hemp plain-weave; short narrow-sleeved jacket to hip length, straight collar closing right over left; narrow trousers, possibly bound at shin or ankle; plain cloth waist cord, no metal; straw sandals or bare feet; topknot with a cloth band or bare topknot, may be bare-chested while working; colours natural white, black or raw fibre, no bright dye. Dust, sweat, worn cloth. Forbidden: Joseon hanbok silhouette, gat hat, Ming/Qing dress, samurai elements, modern fabric, purple/crimson/blue/yellow official colours.",
 "COSTUME_SILLA_ATTENDANT_A01": "Silla funeral attendant/artisan (PROBABLE): finer hemp or ramie plain-weave; narrow-sleeved hip-length jacket, straight collar closing right over left, tidier than labourers; narrow to medium trousers (women: jacket and skirt); plain cloth belt, minimal ornament; low shoes or straw sandals; topknot with cloth or simple cap; undyed white, black or grey-brown tones, no official colours. Sleeve ends and wrists must read clearly in hand close-ups. Forbidden: Joseon hanbok silhouette, court robes, fantasy priest robes, Chinese imperial dress, official four colours.",
 "COSTUME_SILLA_ELITE_A01": "Silla senior elite observer (PROBABLE; colour and belt INTERPRETIVE): silk outer robe over hemp/ramie inner jacket; narrow-sleeved jacket under a longer outer robe, straight collar closing right over left, rounded collar acceptable; wide trousers, pleats acceptable; plaque belt with hanging pendants in restrained silver or bronze - never a copy of the Cheonmachong gold belt; ankle boots over socks; birch-bark style cap or simple formal cap - never a gold or gilt-bronze crown; muted crimson or blue tones, never purple. Back view, shoulder line and cap silhouette must be consistent. Forbidden: gold crown, Joseon royal or official robes, Ming/Qing imperial dress, fantasy king styling, purple.",
}
def cos_text(cid): return f"{cid}: {COS_EN[cid]}"
STYLE = "DDABONG Documentary Reenactment (style B): realistic Korean facial proportions, natural skin texture with subtle imperfections, restrained expressions, historically researched clothing, natural documentary lighting, not glamorous, not glossy, not fantasy-drama, not generic Joseon hanbok."
NEG = ["Joseon dynasty hanbok", "gat hats", "Ming or Qing court robes", "samurai armor", "European medieval armor", "fantasy armor", "giant stone palace", "Chinese imperial palace", "pagoda skyline", "torii gates", "modern tools", "excavators", "cranes", "concrete", "electric lights", "plastic", "modern roads", "supernatural ghosts", "glowing magic", "fantasy crown", "exaggerated crying", "battle scene", "cinematic war spectacle", "modern museum display cases", "text", "watermark", "glossy skin", "malformed anatomy"]
LOCKS = {
 "DDABONG_GLOBAL_V01": {"lock_id": "DDABONG_GLOBAL_V01", "kind": "GLOBAL", "text": GLOBAL, "source": "정본 §8 Global base", "status": "APPROVED", "updated_at": D},
 "SILLA_EARLY_V01": {"lock_id": "SILLA_EARLY_V01", "kind": "ERA", "text": ERA, "source": "05_HISTORY_DATABASE/era/SILLA_EARLY.json", "status": "DRAFT", "updated_at": D},
 "LOC_CHEONMACHONG_V01": {"lock_id": "LOC_CHEONMACHONG_V01", "kind": "LOCATION", "text": LOCT, "source": "05_HISTORY_DATABASE/locations/LOC_CHEONMACHONG_V01.json (S3/S4)", "status": "DRAFT", "updated_at": D},
 "DDABONG_DOC_REENACTMENT_V01": {"lock_id": "DDABONG_DOC_REENACTMENT_V01", "kind": "STYLE", "text": STYLE, "source": "정본 §5 · D-004", "status": "APPROVED", "updated_at": D},
 "DDABONG_NEGATIVE_V01": {"lock_id": "DDABONG_NEGATIVE_V01", "kind": "NEGATIVE", "text": ", ".join(NEG), "items": NEG, "source": "legacy higgsfield 팩 공통 금지요소 + §8", "status": "APPROVED", "updated_at": D},
}
for cid in COS:
    LOCKS[cid + "_LOCK"] = {"lock_id": cid + "_LOCK", "kind": "COSTUME", "text": cos_text(cid), "source": f"05_HISTORY_DATABASE/costumes/{cid}.json (D-011)", "status": "DRAFT", "updated_at": D}
ROLE_EN = {"CHAR_SILLA_ELITE_OBSERVER_01": "senior member of the elite watching mound construction and funeral preparation from a distance; not the deceased, not a king",
           "CHAR_SILLA_LABORER_GROUP_01": "crowd of labourers preparing timber, carrying stones and building the mound; no recurring individual face",
           "CHAR_SILLA_ATTENDANT_GROUP_01": "crowd of attendants and artisans selecting and arranging grave goods and preparing the rite; faces often out of frame, hands first"}
for cid, c in CH.items():
    pl = c["physical_lock"]
    LOCKS[cid + "_LOCK"] = {"lock_id": cid + "_LOCK", "kind": "CHARACTER", "text": f"{cid} ({c['name_en']}): {ROLE_EN[cid]}. Face: {pl['face_identity']}. Body: {pl['body_proportion']}. Hair: {pl['hair'].split(' - ')[0].split(' — ')[0]}. Age: {pl['age_range']}. Skin: {pl['skin']}. Costume lock: {c['default_costume_id']}_LOCK.", "source": f"05_HISTORY_DATABASE/characters/{cid}.json", "status": "DRAFT", "updated_at": D}
for lid, l in LOCKS.items(): w(f"06_PROMPT_LIBRARY/locks/{lid}.json", l)
(R / "06_PROMPT_LIBRARY/locks/_README.md").write_text("# 06_PROMPT_LIBRARY/locks — 프롬프트 lock 조각 (정본 §8)\n\n> 프롬프트는 여기 조각을 조립한다. 매번 처음부터 쓰지 않는다. 조각이 바뀌면 새 V번호.\n> 조립 순서: GLOBAL + ERA + LOCATION + CHARACTER/COSTUME + STYLE + CAMERA + SHOT DELTA. NEGATIVE 는 별도 전달.\n\n| lock_id | kind | 원천 |\n|---|---|---|\n" + "\n".join(f"| `{k}` | {v['kind']} | {v['source']} |" for k, v in LOCKS.items()) + "\n", encoding="utf-8")

def assemble(locks, delta, cam=None):
    parts = [GLOBAL, f"[{locks['era']}] {LOCKS[locks['era']]['text']}", f"[{locks['location']}] {LOCKS[locks['location']]['text']}"]
    for cc in locks["character_costume"]:
        for piece in cc.split("+"): parts.append(f"[{piece}] {LOCKS[piece]['text']}")
    parts.append(f"[{locks['style']}] {STYLE}")
    if cam: parts.append(f"[{cam['camera_id']}] lens {cam['lens']}mm, camera height {cam['camera_height']} m, {cam['motion']['type']}" + (f" {cam['motion']['distance']} m" if cam['motion'].get('distance') else "") + f", {cam['duration']} s.")
    parts.append(f"SHOT: {delta}")
    return " ".join(parts)

# ---------- 2. master pack prompts (IMAGE) ----------
SLOT = {"hero": "hero portrait, chest-up, three-quarter light, calm direct gaze", "front": "front view, neutral expression, full head and shoulders, flat even daylight",
        "three_quarter_left": "three-quarter view from the left, neutral", "three_quarter_right": "three-quarter view from the right, neutral", "profile": "true profile view, showing headwear silhouette",
        "full_body": "full body head to toe, standing, arms relaxed, plain earth background, whole costume visible", "neutral_standing": "neutral standing pose, weight even, hands at sides, facing camera",
        "walking": "mid-stride walking pose, side-front angle, natural gait", "costume_detail": "close detail of collar, closure, belt and sleeve end; fabric weave visible; hands in frame", "expression_sheet": "sheet of five restrained expressions: neutral, attentive, concerned, resolved, quiet grief; no exaggeration"}
LITE = {"full_body", "walking", "costume_detail"}
extra = {"CHAR_SILLA_ELITE_OBSERVER_01": {"back_view": "view from directly behind, shoulders and headwear silhouette, standing still looking away toward distant work (H05 reference)"}}
n = 0
for cid, c in CH.items():
    slots = list(SLOT) if c["master_pack_tier"] == "FULL" else [s for s in SLOT if s in LITE]
    for slot in slots + list(extra.get(cid, {})):
        delta = extra.get(cid, {}).get(slot) or SLOT[slot]
        if "GROUP" in cid: delta += "; three different individuals side by side, varied faces and builds, no recurring hero face"
        pid = f"PRM_MP_{cid}_{slot.upper()}_V01"
        locks = {"global": "DDABONG_GLOBAL_V01", "era": "SILLA_EARLY_V01", "location": "LOC_CHEONMACHONG_V01", "character_costume": [f"{cid}_LOCK+{c['default_costume_id']}_LOCK"], "style": "DDABONG_DOC_REENACTMENT_V01", "camera": None}
        w(f"{EP}/11_AI_STILLS/prompt_{pid}.json", {"prompt_id": pid, "shot_id": f"MASTER_PACK:{cid}:{slot}", "target": "IMAGE", "locks": locks, "shot_delta": delta, "negative": NEG, "assembled_text": assemble(locks, delta), "reference_images": [], "version": "V01", "parent_prompt_id": None, "patch_id": None, "created_at": D, "created_by": BY}); n += 1
mp_count = n

# ---------- 3. camera drafts for AI shots ----------
CAM = {
 "EP01_S04_SH004": dict(lens=35, h=1.4, motion={"type": "tracking", "distance": 3, "degrees": None, "speed_curve": "linear"}, target="CHAR_SILLA_LABORER_GROUP_01", note="H01 slow lateral tracking past timber work"),
 "EP01_S04_SH005": dict(lens=28, h=1.6, motion={"type": "push_in", "distance": 6, "degrees": None, "speed_curve": "ease_in"}, target="MAIN_OBJECT", note="H02 wide to hands and stones"),
 "EP01_S04_SH006": dict(lens=24, h=2.2, motion={"type": "static", "distance": None, "degrees": None, "speed_curve": None}, target="MAIN_OBJECT", note="H02 wide, same Blender scene as SH005"),
 "EP01_S05_SH005": dict(lens=50, h=1.0, motion={"type": "dolly_forward", "distance": 0.4, "degrees": None, "speed_curve": "ease_in_out"}, target="CHAR_SILLA_ATTENDANT_GROUP_01", note="H03 hands and objects, shallow depth"),
 "EP01_S06_SH002": dict(lens=28, h=1.5, motion={"type": "static", "distance": None, "degrees": None, "speed_curve": None}, target="CHAR_SILLA_ELITE_OBSERVER_01", note="H04 static wide, foreground micro movement"),
 "EP01_S06_SH005": dict(lens=35, h=1.5, motion={"type": "dolly_forward", "distance": 2, "degrees": None, "speed_curve": "linear"}, target="CHAR_SILLA_ELITE_OBSERVER_01", note="H05 behind observer, slow forward"),
 "EP01_S06_SH010": dict(lens=24, h=1.7, motion={"type": "static", "distance": None, "degrees": None, "speed_curve": None}, target="MAIN_OBJECT", note="H06 nearly complete mound, low warm sun (AI_STILL key frame)"),
 "EP01_S08_SH002": dict(lens=35, h=1.6, motion={"type": "static", "distance": None, "degrees": None, "speed_curve": None}, target="MAIN_OBJECT", note="H07 match-cut: copy lens/height/position from EP01_S08_SH003 real plate once shot"),
}
POS = {"EP01_S06_SH002": [{"character_id": "CHAR_SILLA_ELITE_OBSERVER_01", "x": 0.0, "y": -6.0, "z": 0.0, "facing_deg": 0}, {"character_id": "CHAR_SILLA_ATTENDANT_GROUP_01", "x": 2.0, "y": 2.0, "z": 0.0, "facing_deg": 200}, {"character_id": "CHAR_SILLA_LABORER_GROUP_01", "x": -4.0, "y": 8.0, "z": 0.0, "facing_deg": 160}],
       "EP01_S06_SH005": [{"character_id": "CHAR_SILLA_ELITE_OBSERVER_01", "x": 0.0, "y": 2.5, "z": 0.0, "facing_deg": 0}]}
for sid, c in CAM.items():
    sh = rd(f"{EP}/07_SHOTS/shot_{sid}.json")
    cam_id = f"CAMERA_{sid}_V01"
    w(f"{EP}/10_BLENDER/camera_{cam_id}.json", {"camera_id": cam_id, "shot_id": sid, "lens": c["lens"], "camera_height": c["h"], "duration": sh["duration"], "fps": 24, "motion": c["motion"], "tilt": {"start": 0, "end": 0}, "target": c["target"], "actor_positions": POS.get(sid, []), "height_ratios": {"CHAR_SILLA_ELITE_OBSERVER_01": 1.0, "CHAR_SILLA_LABORER_GROUP_01": 0.97, "CHAR_SILLA_ATTENDANT_GROUP_01": 0.98} if sh["characters"] else None, "blender_file": None, "version": "V01", "status": "DRAFT", "updated_at": D})

# ---------- 4. master_frame stubs ----------
for sc, shots in {"EP01_S04": ["EP01_S04_SH004", "EP01_S04_SH005", "EP01_S04_SH006"], "EP01_S06": ["EP01_S06_SH002", "EP01_S06_SH005", "EP01_S06_SH010"]}.items():
    scene = rd(f"{EP}/07_SHOTS/scene_{sc}.json"); fid = f"{sc}_MASTER_V01"
    w(f"{EP}/07_SHOTS/master_frame_{fid}.json", {"frame_id": fid, "scene_id": sc, "version": "V01", "path": None, "generation_id": None, "characters": scene["characters"], "costumes": sorted({CH[c]["default_costume_id"] for c in scene["characters"]}), "location": "LOC_CHEONMACHONG_V01", "camera_id": f"CAMERA_{shots[0]}_V01" if sc == "EP01_S04" else "CAMERA_EP01_S06_SH002_V01", "status": "DRAFT", "approved_by": None, "approved_at": None, "derived_shots": shots, "updated_at": D})
    scene["master_frame"] = fid; scene["updated_at"] = D; w(f"{EP}/07_SHOTS/scene_{sc}.json", scene)

# ---------- 5. AI shot prompts (from legacy APPROVED H-pack, condensed as shot_delta) ----------
H = {
 "EP01_S04_SH004": ("VIDEO", "H01: skilled workers prepare thick timber beams for the burial chamber, measuring, carrying and fitting wood with simple period tools; coordinated labour, physical effort, no dramatic emotion; earthy colours, cool morning light, dust in air; medium-wide."),
 "EP01_S04_SH005": ("VIDEO", "H02: groups of workers carry large river stones toward the wooden chamber with baskets and wooden supports; repetition, weight, organisation; mound only partly formed; overcast daylight; wide to hands and stones."),
 "EP01_S04_SH006": ("VIDEO", "H02 wide: organised work around the partly built mound seen from a static wide position; many small figures, no hero posing."),
 "EP01_S05_SH005": ("VIDEO", "H03: attendants carefully arrange burial goods before placement - gold ornaments in verified Silla forms, glass vessels, pottery, horse gear; hands, cloth, metal and glass in close shots; deliberate selection; soft interior daylight; not a museum display."),
 "EP01_S06_SH002": ("VIDEO", "H04: elite funeral preparation, several groups in different roles - attendants near the chamber, workers with materials, a senior figure observing; hierarchy shown by spacing and behaviour only; static wide, late afternoon light, solemn controlled atmosphere."),
 "EP01_S06_SH005": ("VIDEO", "H05: camera behind a senior observer standing at a respectful distance watching the mound being built while workers, attendants and objects move through an organised space; slow forward movement; no lips moving, no visions; composition suggests the social problem of visible authority. Interpretation, not a recorded event."),
 "EP01_S06_SH010": ("IMAGE", "H06: nearly completed monumental mound, earth newly packed over the stone-covered chamber, small groups at a distance for scale; permanence and visibility, not celebration; low warm sunlight, long shadows, static wide."),
 "EP01_S08_SH002": ("IMAGE", "H07: newly finished earthen mound fills the frame in a simple wide composition, camera completely stable, mound centred slightly off-axis, sparse ancient surroundings, no people near camera, neutral daylight; designed to hard-cut to the same-shaped green mound in modern Gyeongju."),
}
for sid, (tgt, delta) in H.items():
    sh = rd(f"{EP}/07_SHOTS/shot_{sid}.json"); cam = rd(f"{EP}/10_BLENDER/camera_CAMERA_{sid}_V01.json")
    cc = [f"{c}_LOCK+{CH[c]['default_costume_id']}_LOCK" for c in sh["characters"]]
    locks = {"global": "DDABONG_GLOBAL_V01", "era": "SILLA_EARLY_V01", "location": "LOC_CHEONMACHONG_V01", "character_costume": cc, "style": "DDABONG_DOC_REENACTMENT_V01", "camera": cam["camera_id"]}
    pid = f"PRM_{sid}_V01"; folder = "12_AI_VIDEO" if tgt == "VIDEO" else "11_AI_STILLS"
    refs = ([f"master_frame:{sh['master_frame'] or sid[:8] + '_MASTER_V01'}"] if sh["characters"] else []) + [f"character_pack:{c}" for c in sh["characters"]]
    w(f"{EP}/{folder}/prompt_{pid}.json", {"prompt_id": pid, "shot_id": sid, "target": tgt, "locks": locks, "shot_delta": delta + " " + (sh["ai_label"] or ""), "negative": NEG, "assembled_text": assemble(locks, delta, cam), "reference_images": refs, "version": "V01", "parent_prompt_id": None, "patch_id": None, "created_at": D, "created_by": BY})
    sh["prompt_id"] = pid; sh["camera_id"] = cam["camera_id"]
    if sid.startswith("EP01_S04") or sid.startswith("EP01_S06"): sh["master_frame"] = sid[:8] + "_MASTER_V01"
    sh["updated_at"] = D; sh["updated_by"] = BY; w(f"{EP}/07_SHOTS/shot_{sid}.json", sh)
print("locks", len(LOCKS), "master-pack prompts", mp_count, "cameras", len(CAM), "shot prompts", len(H), "master frames 2")
