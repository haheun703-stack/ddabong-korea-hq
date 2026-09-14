# -*- coding: utf-8 -*-
"""D-026 (2026-09-13) data side: split S06 master frame by construction stage, move H07 landing to Cheonmachong,
save 3 master-frame prompts BEFORE sending (D-016) + APPROVED approval (max 10 calls / 20 credits).
Docs side (shoot plan, graphics spec, rights standard, script hedge, delta) is applied separately.
Usage:  python 00_SYSTEM/tools/d026_apply.py
"""
import json, re, sys
from pathlib import Path

R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / "00_SYSTEM/tools"))
D = "2026-09-13"; EP = R / "02_SEASONS/S01/EP01"; SH = EP / "07_SHOTS"; CACHE = R / "08_GENERATION_CACHE/EP01"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- schemas: frame_id with optional stage tag; scene.master_frame may list several frames ----
p = R / "00_SYSTEM/schemas/master_frame.schema.json"; s = rd(p)
s["properties"]["frame_id"]["pattern"] = r"^EP\d{2,3}_S\d{2}_MASTER(_[A-Z0-9]+(_[A-Z0-9]+)*)?_V\d{2}$"
s["properties"]["frame_id"]["description"] = "예: EP001_S04_MASTER_V03 · 같은 씬에 역사 단계가 다르면 EP01_S06_MASTER_OPEN_CHAMBER_V01 처럼 단계 태그 (D-026)"
w(p, s)
p = R / "00_SYSTEM/schemas/scene.schema.json"; s = rd(p)
s["properties"]["master_frame"] = {"type": ["string", "array", "null"], "items": {"type": "string"},
                                   "description": "master_frame_id (승인 필요). 씬 안에서 역사 단계가 갈리면 여러 개 (D-026)"}
w(p, s)

# ---- split S06 master frame ----
OPEN, MOUND, OLD = "EP01_S06_MASTER_OPEN_CHAMBER_V01", "EP01_S06_MASTER_MOUND_BUILDING_V01", "EP01_S06_MASTER_V01"
old = rd(SH / f"master_frame_{OLD}.json")
base = {k: old[k] for k in ("scene_id", "version", "path", "generation_id", "location", "status", "approved_by", "approved_at")}
w(SH / f"master_frame_{OPEN}.json", dict(base, frame_id=OPEN, characters=old["characters"], costumes=old["costumes"],
  camera_id="CAMERA_EP01_S06_SH002_V01", derived_shots=["EP01_S06_SH002"], updated_at=D))
w(SH / f"master_frame_{MOUND}.json", dict(base, frame_id=MOUND, characters=old["characters"], costumes=old["costumes"],
  camera_id="CAMERA_EP01_S06_SH005_V01", derived_shots=["EP01_S06_SH005", "EP01_S06_SH010"], updated_at=D))
(SH / f"master_frame_{OLD}.json").unlink()

sc = rd(SH / "scene_EP01_S06.json"); sc["master_frame"] = [OPEN, MOUND]; sc["updated_at"] = D; w(SH / "scene_EP01_S06.json", sc)
for sid, frame in (("EP01_S06_SH002", OPEN), ("EP01_S06_SH005", MOUND), ("EP01_S06_SH010", MOUND)):
    f = SH / f"shot_{sid}.json"; d = rd(f); d["master_frame"] = frame; d["updated_at"] = D
    if "D-026" not in d["notes"]: d["notes"] += f" D-026: master_frame {OLD} → {frame} (천마총 층 순서: 목곽 열린 단계 vs 봉분 상승 단계)."
    w(f, d)
for rel in ("12_AI_VIDEO/prompt_PRM_EP01_S06_SH002_V01.json", "12_AI_VIDEO/prompt_PRM_EP01_S06_SH005_V01.json", "11_AI_STILLS/prompt_PRM_EP01_S06_SH010_V01.json"):
    f = EP / rel; d = rd(f)   # never sent -> in-place reference update is allowed (no generation record references them)
    frame = OPEN if "SH002" in rel else MOUND
    d["reference_images"] = [f"master_frame:{frame}" if r == f"master_frame:{OLD}" else r for r in d["reference_images"]]
    w(f, d)

# ---- H07 landing = Cheonmachong mound ----
for sid in ("EP01_S08_SH002", "EP01_S08_SH003", "EP01_S06_SH007"):
    f = SH / f"shot_{sid}.json"; d = rd(f)
    if d["location"] != "LOC_CHEONMACHONG_V01":
        d["location"] = "LOC_CHEONMACHONG_V01"; d["updated_at"] = D
        d["notes"] += " D-026: 장소 LOC_GYEONGJU_DAEREUNGWON_V01 → LOC_CHEONMACHONG_V01 (H07·H05 역사 재현과 같은 천마총 봉분에 착지)."
        d["notes"] = d["notes"].replace("LOC_GYEONGJU_DAEREUNGWON_V01.spatial_lock.match_cut_frame", "LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame")
    w(f, d)
LC = R / "05_HISTORY_DATABASE/locations/LOC_CHEONMACHONG_V01.json"; lc = rd(LC)
lc["spatial_lock"]["match_cut_frame"] = {
    "status": "TO_RECORD_AFTER_SHOOT", "shot_id": "EP01_S08_SH003", "pairs_with": "EP01_S08_SH002 (H07 AI_STILL)",
    "note": "D-026: 천마총 봉분 착지. SH003 삼각대 촬영 후 값을 채우고, 그 뒤 H07 생성 (D-018). 키 이름은 SHOOT_PLAN_EP01_V01 §3a.",
    "position_description": None, "gps": None, "mound_id": "천마총 (황남동 155호분)", "lens_mm": None, "lens_35mm_equiv": None,
    "camera_height_m": None, "tilt_deg": None, "heading_deg": None, "mound_offset": None, "horizon_height": None,
    "shot_datetime": None, "sun_direction": None, "weather": None, "grass_colour": None, "take_id": None}
lc["updated_at"] = D; w(LC, lc)
LD = R / "05_HISTORY_DATABASE/locations/LOC_GYEONGJU_DAEREUNGWON_V01.json"; ld = rd(LD)
ld["spatial_lock"]["match_cut_frame"] = "D-026: 매치컷 착지 구도는 천마총 봉분 기준 → LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame 에 기록."
ld["updated_at"] = D; w(LD, ld)

# ---- master-frame prompts (saved before sending) ----
from importlib import util
spec = util.spec_from_file_location("v", R / "00_SYSTEM/schemas/validate.py")  # reuse required_negative without running main
src = (R / "00_SYSTEM/schemas/validate.py").read_text(encoding="utf-8")
ns = {"__file__": str(R / "00_SYSTEM/schemas/validate.py")}
exec(src.split("def money_rules")[0].replace("import json, re, sys, warnings", "import json, re, sys, warnings"), ns)
required_negative = ns["required_negative"]

STYLE = "Photorealistic historical documentary still, style B Documentary Reenactment, natural textures and skin, not glossy, earthy natural colours."
ELITE = "the senior elite observer in a muted dusty blue silk robe with short outer sleeves over long ivory inner sleeves, pale birch-bark conical cap and restrained bronze plaque belt with small pendants"
ATT = "funeral attendants in undyed white, black and grey-brown hemp jackets wrapped right over left and closed only by plain cloth waist belts (no ribbon ties on the chest), one woman in a long plain grey skirt"
LAB = "labourers in undyed coarse hemp short jackets with cloth waist cords, shin-bound trousers, straw sandals or bare feet, topknots or cloth headbands"
NO = "No tiled roofs, no buildings, no palace, no stone walls, no modern tools, no metal shovels or pick-axes, no rubber wheels, no cranes, no gold objects visible, no crown visible, no text, no watermark, no logo."
PROMPTS = {
 "EP01_S04_MASTER_V01": (["CHAR_SILLA_LABORER_GROUP_01_LOCK+COSTUME_SILLA_LABORER_A01_LOCK"], "CAMERA_EP01_S04_SH005_V01",
   "S04 master frame: early construction stage - open timber chamber, stones just beginning, labourers at work",
   " ".join(["One wide cinematic establishing frame, 16:9, a single still image.",
     "Early Silla, Gyeongju, 5th century: the Cheonmachong burial site at an early construction stage.",
     "In the centre, a rectangular wooden outer burial chamber of thick timber beams stands in a shallow pit, about 6.6 by 4.2 metres; river stones are only beginning to be piled around its sides.",
     "The earth mound has not been raised yet; the open work area around the chamber is wide.",
     f"At the left edge, a timber yard where {LAB} measure and shape beams; in the middle ground other labourers carry river stones in baskets toward the chamber.",
     "Use the reference image for the labourers' clothing only; faces varied, nobody posing, no hero figure.",
     "Camera about 1.6 metres high, 28mm lens feel, slightly elevated three-quarter view of the whole work area, overcast morning light, dust in the air.",
     STYLE, NO])),
 OPEN: (["CHAR_SILLA_ELITE_OBSERVER_01_LOCK+COSTUME_SILLA_ELITE_A01_LOCK", "CHAR_SILLA_ATTENDANT_GROUP_01_LOCK+COSTUME_SILLA_ATTENDANT_A01_LOCK", "CHAR_SILLA_LABORER_GROUP_01_LOCK+COSTUME_SILLA_LABORER_A01_LOCK"],
   "CAMERA_EP01_S06_SH002_V01", "S06 master frame A (H04): wooden chamber complete and still open, before stones - funeral preparation by role",
   " ".join(["One wide cinematic frame, 16:9, a single still image.",
     "Early Silla, Gyeongju, 5th century: the Cheonmachong burial site at the stage when the wooden outer chamber is complete and still open, before any stones are piled over it.",
     "In the centre, the open rectangular timber chamber in its pit, with a plain wooden coffin inside and a plain wooden chest at the head end of the coffin.",
     f"Close to the open chamber, {ATT}, carefully carry small objects wrapped in plain cloth; hands and gestures matter, faces calm.",
     f"Further back, {LAB}, wait beside baskets of river stones, not yet working.",
     f"In the foreground at a respectful distance, {ELITE}, stands still, seen three-quarter from behind, watching the chamber.",
     "Hierarchy is shown only by spacing and behaviour.",
     "Use the reference images for each group's clothing and for the senior observer's face and costume.",
     "Camera about 1.5 metres high, 28mm lens feel, static, late afternoon light, solemn and controlled.",
     STYLE, NO])),
 MOUND: (["CHAR_SILLA_ELITE_OBSERVER_01_LOCK+COSTUME_SILLA_ELITE_A01_LOCK", "CHAR_SILLA_LABORER_GROUP_01_LOCK+COSTUME_SILLA_LABORER_A01_LOCK", "CHAR_SILLA_ATTENDANT_GROUP_01_LOCK+COSTUME_SILLA_ATTENDANT_A01_LOCK"],
   "CAMERA_EP01_S06_SH005_V01", "S06 master frame B (H05, H06): chamber covered by stones, earth mound rising",
   " ".join(["One wide cinematic frame, 16:9, a single still image.",
     "Early Silla, Gyeongju, 5th century: the same Cheonmachong site at a later stage; the wooden chamber is already buried under a heap of river stones, and a broad earth mound is rising over it.",
     "The mound is already far taller than people but not finished; its final size will be about 47 metres across and 12.7 metres high, a wide low dome, not a steep hill.",
     f"{LAB} carry baskets of earth up the slope and pack the sides; a few {ATT} stand in small groups at the base.",
     f"In the foreground, {ELITE}, stands still at a respectful distance, seen three-quarter from behind, watching the mound grow.",
     "Use the reference images for each group's clothing and for the senior observer's face and costume.",
     "Camera about 1.5 metres high behind the observer, 35mm lens feel, low warm late-afternoon sunlight, long shadows, calm and monumental, not celebratory.",
     STYLE, NO])),
}
pids = []
for frame, (cc, cam, delta, text) in PROMPTS.items():
    pid = f"PRM_MF_{frame}"  # ends with _V01
    locks = {"global": "DDABONG_GLOBAL_V01", "era": "SILLA_EARLY_V01", "location": "LOC_CHEONMACHONG_V01", "character_costume": cc,
             "style": "DDABONG_DOC_REENACTMENT_V01", "camera": cam}
    chars = [c.split("_LOCK")[0] for c in cc]
    w(EP / f"11_AI_STILLS/prompt_{pid}.json", {
        "prompt_id": pid, "shot_id": f"MASTER_FRAME:{frame}", "target": "IMAGE", "locks": locks, "shot_delta": delta,
        "negative": required_negative(locks), "assembled_text": text,
        "reference_images": [f"character_pack:{c}" for c in chars], "version": "V01", "parent_prompt_id": None, "patch_id": None,
        "created_at": D, "created_by": "Image Generation Agent (Claude Code) — master frame, saved before sending (D-016, D-026)"})
    pids.append(pid)

w(CACHE / "approval_APR_EP01_MF_001.json", {
    "approval_id": "APR_EP01_MF_001", "kind": "PAID_GENERATION", "target_id": "EP01_S04_MASTER_V01 + " + OPEN + " + " + MOUND,
    "money_gate_presented": {
        "shot_id": "MASTER_FRAME:EP01", "prompt_ids": pids, "aspect_ratios": {p: "16:9" for p in pids},
        "image_references": {"laborer_full_body": "412a72bc-f3f1-4955-8d3a-36e1e6306d1f", "attendant_full_body": "84c0fdbc-1c5c-4edd-bb35-b1836ae14288",
                             "elite_hero": "5de27748-f100-47e0-af23-1bdb68466bb7"},
        "provider_model": "Higgsfield / Nano Banana Pro (job type nano_banana_2), 2k, 16:9 (still image tool; EP01 Higgsfield-video 0 unaffected)",
        "expected_attempts": 10, "estimated_cost_range": "6–20 credits (2 credits x 3 frames + FIX retries, hard cap 20)",
        "continuity_risk": "HIGH - first multi-character frames; layer order and 47 m / 12.7 m proportion must hold"},
    "decision": "APPROVE", "fix_reason": None, "decided_by": "사용자", "decided_at": f"{D}T07:00:00Z",
    "note": "D-026: 기준 그림 3장, 최대 10 호출 / 20 credits. 실패 시 실패 항목만 FIX (PATCH + 새 prompt 버전), 승인 범위 밖 호출 금지."})

# ---- decisions / status / plan ----
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8"); anchor = "\n---\n\n## 승인 대기 (P)"
if "### D-026" not in s:
    s = s.replace(anchor, f"""
### D-026 · 2026-09-13 · Master Frame 3장 승인 · H07 천마총 착지 · 자체 촬영 GREEN · 월성·사찰 선택 · G13·G04 확정 (사용자)
**1** S06 기준 그림을 역사 단계로 분리 (A안): `EP01_S04_MASTER_V01` · `{OPEN}` (H04, 목곽 열린 단계) · `{MOUND}` (H05·H06, 봉분 상승 단계). **Money Gate** `APR_EP01_MF_001` 최대 10 호출 / 20 credits. 실패 시 실패 항목만 FIX, 승인 범위 밖 호출 금지. 스키마: frame_id 단계 태그 허용, scene.master_frame 복수 허용.
**2** H07 매치컷 착지 = **천마총 봉분**. S08_SH002 · S08_SH003 · S06_SH007 장소 → LOC_CHEONMACHONG_V01, 착지 구도 기록 `LOC_CHEONMACHONG_V01.spatial_lock.match_cut_frame`.
**3** 자체 촬영 = **GREEN** (증빙: self-shot / original footage / source file retained). BLUE 는 확인 중·게시 금지 유지 (RIGHTS_STANDARD).
**4** 월성·사찰 = 선택 촬영. EP01 필수 영상은 대릉원·천마총 중심, 선택 촬영이 일정을 흔들면 안 됨.
**5** G13 = 동서 옆 단면 (머리 동쪽 · 금관 · 머리맡 궤) + 작은 평면 inset (T자 배치만).
**6** 해석 문장 hedge: "It may have belonged to a burial system of status, ceremony, and identity." (대본 v2 · SCRIPT_ROUGHCUT_DELTA)
**7** G04 층 순서 = 관 → 목곽 → 돌·자갈 → 흙 봉분. 별도 부장품 층 없음, 부장품은 관·목곽 주변 배치.
""" + anchor, 1)
p.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
if "D-026." not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-026.** 1~7 추천안 전부 승인: Master Frame 3장 (S04 · S06 OPEN_CHAMBER · S06 MOUND_BUILDING) Money Gate 최대 10 호출/20 credits · H07 천마총 착지 · 자체 촬영 GREEN · 월성·사찰 선택 · G13 옆 단면+평면 inset · G13 hedge · G04 층 순서.\n", 1)
p.write_text(s, encoding="utf-8")
p = EP / "15_QA/MASTER_FRAME_PLAN_EP01.md"; s = p.read_text(encoding="utf-8")
if "## 결정 (D-026)" not in s:
    s = s.replace("# EP01 Master Frame 계획 (초안) — 사람 결정 대기", "# EP01 Master Frame 계획 — **결정 D-026: A안**")
    s += f"\n## 결정 (D-026)\n\nA안 승인. 기준 그림 3장: `EP01_S04_MASTER_V01` · `{OPEN}` · `{MOUND}`. 프롬프트 `11_AI_STILLS/prompt_PRM_MF_*_V01.json` 저장 (전송 전), 승인 `APR_EP01_MF_001` (최대 10 호출 / 20 credits). 기존 `EP01_S06_MASTER_V01` 초안은 두 장으로 대체되어 삭제.\n"
p.write_text(s, encoding="utf-8")
print("D-026 data applied:", pids)
