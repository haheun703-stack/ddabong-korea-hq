# -*- coding: utf-8 -*-
"""S04 master frame V05 (owner '진행' 2026-09-13): cloned-looking labourer faces -> fresh text-only generation (no image reference),
explicit face diversity + all earlier bans. Saves prompt + PATCH_MF_EP01_S04_004 BEFORE sending (D-016).
Usage:  python 00_SYSTEM/tools/mf_s04_v05_prepare.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
TEXT = " ".join([
 "One wide establishing documentary photograph that fills the entire 16:9 frame edge to edge, a single still image; no black bars, no letterbox, no borders.",
 "Early Silla, Gyeongju, 5th century: the Cheonmachong burial site at an early construction stage.",
 "In the centre, a rectangular wooden outer burial chamber of thick timber beams stands on levelled ground, about 6.6 by 4.2 metres, open-topped with no lid; a low course of river stones is only beginning to line its outer walls, and nothing covers the top.",
 "The earth mound has not been raised yet; the open work area around the chamber is wide.",
 "At the left edge, a timber yard where labourers measure and shape beams; in the middle ground other labourers carry river stones in straw baskets, some on shoulder poles, toward the chamber.",
 "Everyone in the image is a labourer in undyed coarse hemp: short jackets to hip length wrapped right over left with cloth waist cords, narrow trousers bound at the shin, straw sandals or bare feet; colours only natural off-white, raw fibre and a few black jackets.",
 "Every labourer is a clearly different individual: mixed ages from about 20 to 45, different face shapes and skin tones from sun, some clean-shaven, some with short stubble, only a few with beards; different heights and builds from thin to stocky; some with a cloth headband, some with a bare topknot; no two people look alike, no repeated or cloned faces, no hero figure.",
 "Tools only: straw baskets, rope, shoulder poles, wooden mallets and all-wooden spades. Every tool is made entirely of wood: no metal blades, no metal heads, no saws, no pick-axes, no hoes, no measuring tapes, nothing yellow or modern in anyone's hands.",
 "In the far background only bare low hills, open untilled land and a few trees: no utility poles, no power lines, no buildings, no greenhouses, no roads, no regular field grid.",
 "No one looks at the camera, no one poses.",
 "Camera about 1.6 metres high, 28mm lens feel, slightly elevated three-quarter view of the whole work area, overcast morning light, dust in the air.",
 "Photorealistic historical documentary still, style B Documentary Reenactment, natural textures and skin, not glossy, earthy natural colours.",
 "No tiled roofs, no stone walls, no modern objects, no rubber wheels, no cranes, no gold objects visible, no crown visible, no text, no watermark, no logo."])
v4 = rd(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V04.json"); v5 = dict(v4)
v5.update(prompt_id="PRM_MF_EP01_S04_MASTER_V05", version="V05", parent_prompt_id="PRM_MF_EP01_S04_MASTER_V04", patch_id="PATCH_MF_EP01_S04_004",
          assembled_text=TEXT, reference_images=[],
          shot_delta="S04 master frame fresh text-only generation: varied labourer faces (no image reference) + all earlier bans (letterbox, modern horizon, tape, metal tools)",
          created_at=D, created_by="Image Generation Agent (Claude Code) - fresh generation, saved before sending (D-016), owner OK")
w(EP / "11_AI_STILLS/prompt_PRM_MF_EP01_S04_MASTER_V05.json", v5)
w(C / "keep_change_patch_PATCH_MF_EP01_S04_004.json", {
    "patch_id": "PATCH_MF_EP01_S04_004", "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "from_version": "V04", "to_version": "V05", "fix_reason": "CHARACTER_IDENTITY",
    "keep": ["early construction stage: open-topped chamber, low stone course, no mound", "timber yard left, stone carrying middle ground", "hemp labourer costume (LITE crowd lock)", "camera 1.6 m / 28mm feel, overcast dust", "full frame, clean early horizon, wooden tools only"],
    "change": ["NOT an edit: fresh text-only generation without the laborer full_body image reference (its three bearded headbanded faces were cloned across the crowd)",
               "explicit face/age/height/beard/headband diversity, no cloned faces",
               "earlier fixes stated as bans from the start: letterbox, utility poles/buildings/field grid, tape measure, metal tools"],
    "reason": "Owner review of V03/V04: labourers look copy-pasted (same beard, headband, age). Crowd lock requires varied faces and mixed heights. The single reference image likely anchored all faces.",
    "requested_by": "사용자 (2026-09-13 '진행')", "created_at": D,
    "resulting_prompt_id": "PRM_MF_EP01_S04_MASTER_V05", "resulting_generation_id": None})
r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## S04 얼굴 복제 문제" not in s:
    s += ("\n## S04 얼굴 복제 문제 (사용자 지적 2026-09-13)\n\nV03·V04 노동자 얼굴이 거의 같음 (같은 수염·머리띠·나이) — 참고 그림 412a72bc 의 얼굴이 따라온 것으로 추정. "
          "→ 참고 그림 없이 문장만으로 새로 생성 V05 (`PATCH_MF_EP01_S04_004`), 얼굴 다양성 + 이전 금지 항목 명시. 승인 8/10 번째.\n")
r.write_text(s, encoding="utf-8")
print(TEXT)
