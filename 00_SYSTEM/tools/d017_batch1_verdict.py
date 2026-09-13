# -*- coding: utf-8 -*-
"""D-017 (2026-09-13): batch-1 human verdict + hero background FIX prompt saved BEFORE sending (Sent Prompt Rule, D-016).
Usage:  python 00_SYSTEM/tools/d017_batch1_verdict.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = "2026-09-13"; CHAR = "CHAR_SILLA_ELITE_OBSERVER_01"
CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d): (R / p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# 1) verdict: front / three_quarter_left / full_body APPROVED, hero stays DRAFT (FIX background)
ch = rd(f"05_HISTORY_DATABASE/characters/{CHAR}.json")
for slot in ("front", "three_quarter_left", "full_body"):
    ch["master_pack"][slot]["status"] = "APPROVED"
ch["updated_at"] = D
if "D-017" not in ch["notes"]:
    ch["notes"] += " D-017: front · three_quarter_left · full_body APPROVED. hero = FIX (배경 조선식 기와지붕만 제거, 얼굴 유지)."
w(f"05_HISTORY_DATABASE/characters/{CHAR}.json", ch)

# 2) HERO_V04 = exact text to send (edit of hero job c7a5cc92)
SEND = ("Edit the reference image. Keep the same man exactly as he is: same face, age, skin, hair, cap, costume, belt, pose, "
        "framing, lighting, and the wooden scaffolding and earth mound behind him. Change only the background buildings: remove "
        "every tiled roof and every roofed building. Where they were, show more earth mound, wooden scaffolding and overcast sky. "
        "No tiled roofs, no curved eaves, no palace, no temple, no houses. Exactly ONE person. No text, no watermark, no logo.")
PATCH = "PATCH_MP_ELITE_HERO_002"
v3 = rd(f"{STILLS}/prompt_PRM_MP_{CHAR}_HERO_V03.json")
v4 = dict(v3)
v4.update(prompt_id=f"PRM_MP_{CHAR}_HERO_V04", shot_delta="hero portrait edit: remove background tiled-roof buildings only (D-017)",
          assembled_text=SEND, reference_images=[f"character_pack:{CHAR}"], version="V04",
          parent_prompt_id=f"PRM_MP_{CHAR}_HERO_V03", patch_id=PATCH, created_at=D,
          created_by="Image Generation Agent (Claude Code) — saved before sending (D-016)")
w(f"{STILLS}/prompt_PRM_MP_{CHAR}_HERO_V04.json", v4)
w(f"{CACHE}/keep_change_patch_{PATCH}.json", {
    "patch_id": PATCH, "shot_id": f"MASTER_PACK:{CHAR}:hero", "from_version": "V03", "to_version": "V04", "fix_reason": "ARCHITECTURE",
    "keep": ["face identity", "age", "birch-bark cap", "muted blue robe + ivory inner", "bronze pendant belt", "pose and framing", "lighting", "scaffolding and earth mound"],
    "change": ["background tiled-roof buildings removed (Joseon-style tiled buildings forbidden by SILLA_EARLY_V01)"],
    "reason": "D-017 human review: hero V02 image background shows curved-eave tiled-roof buildings. Edit the existing image (input = hero job c7a5cc92) so the face used as identity reference does not drift.",
    "requested_by": "사용자 (D-017)", "created_at": D, "resulting_prompt_id": f"PRM_MP_{CHAR}_HERO_V04", "resulting_generation_id": None})

# 3) review sheet
p = R / f"{CACHE}/MP_ELITE/REVIEW_BATCH1.md"; s = p.read_text(encoding="utf-8")
for f in ("MP_ELITE_FRONT_V01", "MP_ELITE_THREE_QUARTER_LEFT_V01", "MP_ELITE_FULL_BODY_V01"):
    i = s.find(f); j = s.find("☐ APPROVE ☐ FIX", i)
    if i >= 0 and j >= 0: s = s[:j] + "☑ APPROVE (D-017)" + s[j + len("☐ APPROVE ☐ FIX"):]
i = s.find("MP_ELITE_HERO_V02"); j = s.find("☐ APPROVE ☐ FIX", i)
if i >= 0 and j >= 0: s = s[:j] + "☑ FIX 배경 기와지붕만 (D-017, PATCH_MP_ELITE_HERO_002)" + s[j + len("☐ APPROVE ☐ FIX"):]
if "## 사람 판정 (D-017)" not in s:
    s += ("\n## 사람 판정 (D-017, 2026-09-13)\n\n- 얼굴 동일성 OK (hero V01 은 실패작, 검수 제외).\n- front · three_quarter_left · full_body **APPROVED**.\n"
          "- hero: 얼굴·복식 OK, **배경 조선식 기와지붕만 FIX** → 기존 이미지 편집 1회 (배치 1 승인 6/8 번째 호출).\n"
          "- 소매(반소매 겉옷 + 긴 속옷 소매): 규칙 위반 아님, 4장 일관 → 유지.\n")
p.write_text(s, encoding="utf-8")

# 4) decision log
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8")
anchor = "\n---\n\n## 승인 대기 (P)"
if "### D-017" not in s:
    s = s.replace(anchor, """
### D-017 · 2026-09-13 · 원로 Master Pack 배치 1 사람 판정 (사용자)
**판정** 얼굴 동일성 OK. front · three_quarter_left · full_body **APPROVED**. hero 는 얼굴·복식 OK, 배경의 조선식 기와지붕 건물이 시대 lock(SILLA_EARLY_V01) 위반 → **그 항목만 FIX**. 소매(반소매 겉옷 + 긴 속옷 소매)는 유지.
**방법** 전체 재생성 대신 기존 hero 이미지(job c7a5cc92)를 입력으로 배경만 편집 1회 (`PRM_…_HERO_V04`, `PATCH_MP_ELITE_HERO_002`). 배치 1 승인 범위 8회 중 6번째. Sent Prompt Rule (D-016) 적용.
**다음** 편집본 사람 확인 → hero APPROVED 되면 4장 완료 → 나머지 6 + back_view 는 새 approval.
""" + anchor, 1)
p.write_text(s, encoding="utf-8")
print("D-017 recorded; HERO_V04 saved (not sent)")
