# -*- coding: utf-8 -*-
"""D-026 reviewer fixes (PASS WITH FIXES): stale pointers, S04 camera, schema tightening, and master-frame prompt wording.
The PRM_MF_*_V01 prompts were never sent (no generation record), so their text is finalised in place before first send (D-016).
Usage:  python 00_SYSTEM/tools/d026_review_fixes.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def rep(path, pairs):
    p = Path(path); s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        if b in s and a not in s: continue
        assert s.count(a) >= 1, (path, a[:50]); s = s.replace(a, b)
    p.write_text(s, encoding="utf-8")

# 1-2 CURRENT_STATUS stale pointers
rep(R / "00_SYSTEM/CURRENT_STATUS.md", [
 ("`_S06_MASTER_V01` (path 없음, 승인 전)", "`_S06_MASTER_OPEN_CHAMBER_V01` · `_S06_MASTER_MOUND_BUILDING_V01` (D-026 분리, path 없음, 승인 전)"),
 ("LOC_GYEONGJU_DAEREUNGWON_V01.spatial_lock.match_cut_frame", "LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame (D-026)"),
])
# 3 Daereungwon 'uses'
f = R / "05_HISTORY_DATABASE/locations/LOC_GYEONGJU_DAEREUNGWON_V01.json"; d = rd(f)
d["uses"] = ["H07 매치컷 착지는 천마총 봉분 (LOC_CHEONMACHONG_V01, D-026)" if "H07" in u else u for u in d.get("uses", [])]
w(f, d)
# 4 plan table
rep(EP / "15_QA/MASTER_FRAME_PLAN_EP01.md", [
 ("| `EP01_S04_MASTER_V01` | H01 목재 준비 (FLOW_VEO) · H02 돌 운반 (BLENDER_FLOW) · H02b 작업 와이드 (BLENDER_FLOW) | 노동자 | SH004 35mm 1.4m tracking |",
  "| `EP01_S04_MASTER_V01` | H01 목재 준비 (FLOW_VEO) · H02 돌 운반 (BLENDER_FLOW) · H02b 작업 와이드 (BLENDER_FLOW) | 노동자 | SH005 28mm 1.6m (D-026 통일) |"),
 ("| `EP01_S06_MASTER_V01` | H04 장례 준비 (BLENDER_FLOW) · H05 관찰자 시점 (BLENDER_FLOW) · H06 거의 완성된 봉분 (AI_STILL) | 원로 · 시종 · 노동자 | SH002 28mm 1.5m static, 배치 좌표 있음 |",
  "| `EP01_S06_MASTER_OPEN_CHAMBER_V01` (D-026) | H04 장례 준비 (BLENDER_FLOW) | 원로 · 시종 · 노동자 | SH002 28mm 1.5m static, 배치 좌표 있음 |\n| `EP01_S06_MASTER_MOUND_BUILDING_V01` (D-026) | H05 관찰자 시점 (BLENDER_FLOW) · H06 거의 완성된 봉분 (AI_STILL) | 원로 · 시종 · 노동자 | SH005 35mm 1.5m |"),
])
# 5 legacy visual-assets BLUE meaning note (top of file, content untouched)
p = R / "episodes/ep01-visual-assets.md"; s = p.read_text(encoding="utf-8")
if "D-026" not in s:
    first, _, rest = s.partition("\n")
    s = first + "\n\n> **D-026 (2026-09-13) 안내**: 이 문서의 `BLUE = 직접 촬영` 표기는 옛 표기다. 현재 규칙(RIGHTS_STANDARD 규칙 5)에서 자체 촬영은 증빙(self-shot / original footage / source file retained)을 남기면 **GREEN**, BLUE 는 확인 중·게시 금지.\n" + rest
    p.write_text(s, encoding="utf-8")
# 6 S04 frame camera = prompt camera
f = EP / "07_SHOTS/master_frame_EP01_S04_MASTER_V01.json"; d = rd(f); d["camera_id"] = "CAMERA_EP01_S04_SH005_V01"; d["updated_at"] = D; w(f, d)
# 11 schema tightening
f = R / "00_SYSTEM/schemas/master_frame.schema.json"; d = rd(f)
d["properties"]["frame_id"]["pattern"] = r"^EP\d{2,3}_S\d{2}_MASTER(_(?!V\d{2}_|V\d{2}$)[A-Z0-9]+)*_V\d{2}$"; w(f, d)
f = R / "00_SYSTEM/schemas/scene.schema.json"; d = rd(f)
d["properties"]["master_frame"] = {"anyOf": [{"type": "string"}, {"type": "array", "items": {"type": "string"}, "minItems": 1, "uniqueItems": True}, {"type": "null"}],
                                   "description": "master_frame_id (승인 필요). 씬 안에서 역사 단계가 갈리면 여러 개 (D-026)"}
w(f, d)

# 7-9 + wording: final master-frame texts
STYLE = "Photorealistic historical documentary still, style B Documentary Reenactment, natural textures and skin, not glossy, earthy natural colours."
NO = "No tiled roofs, no buildings, no palace, no stone walls, no modern tools, no metal shovels or pick-axes, no rubber wheels, no cranes, no gold objects visible, no crown visible, no text, no watermark, no logo."
LAB = "labourers in undyed coarse hemp short jackets with cloth waist cords, shin-bound trousers, straw sandals or bare feet, topknots or cloth headbands"
ATT = "funeral attendants in undyed white, black and grey-brown hemp jackets wrapped right over left and closed only by plain cloth waist belts (no ribbon ties on the chest), one woman in a long plain grey skirt"
ELITE = ("Exactly ONE person in blue in the whole image: the senior elite observer, in a muted dusty blue silk robe with short outer sleeves over long ivory inner sleeves, "
         "pale birch-bark conical cap and restrained bronze plaque belt with small pendants. Nobody else wears blue, a birch-bark cap or a bronze belt.")
TOOLS = "Tools only: straw baskets, rope, wooden poles and wooden spades."
CROWD = "No one looks at the camera, no one poses."
TEXTS = {
 "PRM_MF_EP01_S04_MASTER_V01": " ".join([
   "One wide cinematic establishing frame, 16:9, a single still image.",
   "Early Silla, Gyeongju, 5th century: the Cheonmachong burial site at an early construction stage.",
   "In the centre, a rectangular wooden outer burial chamber of thick timber beams stands on levelled ground, about 6.6 by 4.2 metres, open-topped with no lid; a low course of river stones is only beginning to line its outer walls, and nothing covers the top.",
   "The earth mound has not been raised yet; the open work area around the chamber is wide.",
   f"Everyone in the image is a labourer: {LAB}.",
   "At the left edge, a timber yard where labourers measure and shape beams; in the middle ground other labourers carry river stones in straw baskets toward the chamber.",
   "Use the reference image for the labourers' clothing only; faces varied, no hero figure.",
   TOOLS, CROWD,
   "Camera about 1.6 metres high, 28mm lens feel, slightly elevated three-quarter view of the whole work area, overcast morning light, dust in the air.",
   STYLE, NO]),
 "PRM_MF_EP01_S06_MASTER_OPEN_CHAMBER_V01": " ".join([
   "One wide cinematic frame, 16:9, a single still image.",
   "Early Silla, Gyeongju, 5th century: the Cheonmachong burial site at the stage when the wooden outer chamber is complete and still open.",
   "In the centre, the rectangular timber chamber stands on levelled ground, open-topped with no lid and nothing on top; a low course of river stones may line its outer walls, but no stones or earth cover it.",
   "Inside the chamber, a plain wooden coffin with its lid visible from above, and a plain wooden chest at the head end of the coffin.",
   "Reference images: references 1 and 2 = the senior observer's face and costume only; reference 3 = the attendants' clothing only; reference 4 = the labourers' clothing only; do not copy faces between groups.",
   ELITE,
   "He stands still in the foreground at a respectful distance, seen three-quarter from behind, watching the chamber.",
   f"Near the open chamber, {ATT}, stand holding cloth-wrapped bundles.",
   f"Further back, {LAB}, wait beside straw baskets of river stones, not working.",
   "Hierarchy is shown only by spacing and behaviour.", CROWD,
   "Camera about 1.5 metres high, 28mm lens feel, static, late afternoon light, solemn and controlled.",
   STYLE, NO]),
 "PRM_MF_EP01_S06_MASTER_MOUND_BUILDING_V01": " ".join([
   "One wide cinematic frame, 16:9, a single still image.",
   "Early Silla, Gyeongju, 5th century: the same Cheonmachong site at a later stage.",
   "The wooden chamber is already fully buried under a heap of river stones and hidden; no timber, coffin or chamber walls are visible anywhere.",
   "A broad earth mound is rising over the stones, already far taller than people but not finished; the finished mound will be about 47 metres across and 12.7 metres high, about 3.7 times as wide as it is high, a wide low dome, not a steep hill; people at its base look tiny.",
   "Reference images: references 1 and 2 = the senior observer's face and costume only; reference 3 = the labourers' clothing only; reference 4 = the attendants' clothing only; do not copy faces between groups.",
   ELITE,
   "He stands still in the foreground at a respectful distance, seen three-quarter from behind, watching the mound grow.",
   f"{LAB[0].upper() + LAB[1:]} carry straw baskets of earth up the slope and pack the sides; a few {ATT} stand in small groups at the base.",
   TOOLS, CROWD,
   "Camera about 1.5 metres high behind the observer, 35mm lens feel, low warm late-afternoon sunlight, long shadows, calm and monumental, not celebratory.",
   STYLE, NO]),
}
REFS = {"PRM_MF_EP01_S04_MASTER_V01": ["laborer_full_body"],
        "PRM_MF_EP01_S06_MASTER_OPEN_CHAMBER_V01": ["elite_hero", "elite_back_view", "attendant_full_body", "laborer_full_body"],
        "PRM_MF_EP01_S06_MASTER_MOUND_BUILDING_V01": ["elite_hero", "elite_back_view", "laborer_full_body", "attendant_full_body"]}
gens = R / "08_GENERATION_CACHE/EP01"
for pid, text in TEXTS.items():
    assert not any(g.read_text(encoding="utf-8").count(pid) for g in gens.glob("generation_*.json")), f"{pid} already sent - needs a new version"
    f = EP / f"11_AI_STILLS/prompt_{pid}.json"; d = rd(f); d["assembled_text"] = text; w(f, d)
f = gens / "approval_APR_EP01_MF_001.json"; d = rd(f); m = d["money_gate_presented"]
m["image_references"] = {"laborer_full_body": "412a72bc-f3f1-4955-8d3a-36e1e6306d1f", "attendant_full_body": "84c0fdbc-1c5c-4edd-bb35-b1836ae14288",
                         "elite_hero": "5de27748-f100-47e0-af23-1bdb68466bb7", "elite_back_view": "fba70a58-ef3f-45b7-8f94-7c61d0284307"}
m["reference_order"] = REFS
w(f, d)
print("fixed; words:", {k: len(v.split()) for k, v in TEXTS.items()})
