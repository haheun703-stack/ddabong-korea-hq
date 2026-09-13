# -*- coding: utf-8 -*-
"""Apply Codex-role reviewer BLOCK fixes (2026-09-13) to the uncommitted batch:
mudguard rights (S02_SH003 = gilt-bronze mudguard per script v2 0:35-1:25 + artifact library card 7), proof pages, stale reports/status/spec/plan,
video V02 texts (no build-order/ritual sentences, one main action), H01/H03 start stills, S05_SH005 GOODS_005 link.
Proof paths are filled only for pages whose KOGL Type 1 label was verified in the saved HTML (pass verified ids as argv).
Usage:  python 00_SYSTEM/tools/fix_codex_review_20260913.py RTS_GNM_CHEST_ORNAMENT_001 RTS_GNM_GOLD_CAP_001 ...
"""
import json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; SH = EP / "07_SHOTS"; RT = R / "05_HISTORY_DATABASE/rights"; D = "2026-09-13"
VERIFIED = set(sys.argv[1:])
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def rep(path, pairs):
    p = Path(path); s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        if a in s: s = s.replace(a, b)
        elif b not in s: raise SystemExit(f"anchor not found in {path}: {a[:60]}")
    p.write_text(s, encoding="utf-8")

# 1) mudguard record + proof paths
w(RT / "RTS_GNM_MUDGUARD_001.json", {"rights_id": "RTS_GNM_MUDGUARD_001", "asset_id": "ASSET_GNM_CHEONMACHONG_MUDGUARD_V01",
    "source": "https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=193&mng_no=295&mode=V", "creator": "국립경주박물관", "license": "KOGL Type 1",
    "commercial_use": "YES", "modification_allowed": "YES", "attribution_required": "YES",
    "attribution_text": "Source: Gyeongju National Museum, Mudguard with winged-horse design from Cheonmachong (Gyeongju 2309), KOGL Type 1.",
    "expiration": None, "proof": None, "research_permission": "YES", "media_reuse_permission": "YES", "status": "GREEN",
    "checked_at": D, "checked_by": "Claude Code (Rights check agent, D-029)",
    "notes": "RTS_GNM_OTHER_OBJECTS_001 에서 분리. 천마무늬 말다래 (경주2309, 금동판). 페이지 문구 '국립경주박물관이 창작한 저작권 보호분야 천마무늬 말다래 저작물은 \"공공누리\" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)'. 원본 다운로드 버튼 없음, 표시 이미지만 → 편집 전 해상도 확인. 천마도(RTS_WIKI_CHEONMADO_001)와 다른 유물. S02_SH003 (대본 v2 0:35–1:25 'horse equipment', 유물 라이브러리 카드 7).",
    "usage_tier": "ACTIVE"})
for rid in ("RTS_GNM_CHEST_ORNAMENT_001", "RTS_GNM_GOLD_CAP_001", "RTS_GNM_GLASS_CUP_001", "RTS_GNM_MUDGUARD_001"):
    f = RT / f"{rid}.json"; d = rd(f)
    if rid in VERIFIED:
        d["proof"] = f"05_HISTORY_DATABASE/rights/proof/{rid}_20260913.html"
    if rid == "RTS_GNM_GLASS_CUP_001":
        d["attribution_text"] = "Source: Gyeongju National Museum, Glass cup from Cheonmachong (Treasure), KOGL Type 1."
    w(f, d)

# 2) shots
f = SH / "shot_EP01_S02_SH003.json"; d = rd(f)
if "RTS_GNM_MUDGUARD_001" not in d["rights_ids"]: d["rights_ids"].append("RTS_GNM_MUDGUARD_001")
d["notes"] = d["notes"].replace(" 말다래 = 천마도 그림 (RTS_WIKI_CHEONMADO_001), 별도 금동 말다래 기록 불필요.",
    " 정정 (반박 검수): 이 샷의 '말다래'는 금동 천마무늬 말다래 (대본 v2 0:35–1:25 'horse equipment', 유물 라이브러리 카드 7) → RTS_GNM_MUDGUARD_001 연결. 천마도(RTS_WIKI_CHEONMADO_001)는 1:25–2:15 구간 유물로 기존 연결 유지.")
d["updated_by"] = "Rights check + Codex-role review (Claude Code, D-029)"; d["updated_at"] = D; w(f, d)
f = SH / "shot_EP01_S05_SH001.json"; d = rd(f)
d["notes"] = d["notes"].replace("B1/B3 GREEN, 나머지는 개별 확인.", "B1/B3 GREEN, 나머지는 개별 확인 (2026-09-13 해소: 관모·가슴걸이 GREEN).")
d["updated_by"] = "Rights check + Codex-role review (Claude Code, D-029)"; d["updated_at"] = D; w(f, d)
f = SH / "shot_EP01_S05_SH005.json"; d = rd(f)
if "CLM_EP01_GOODS_005" not in d["fact_ids"]: d["fact_ids"].append("CLM_EP01_GOODS_005")
d["notes"] = d["notes"].replace("손·천·금속·유리 클로즈업. 금 유물 형태는 실제 B1/B3 참조, 판타지 보석 금지.",
    "손·천·금속·유리 클로즈업. 금 유물 형태는 실제 B1/B3 참조, 판타지 보석 금지. (2026-09-13 반박 검수: 금 허리띠는 피장자 착장 FACT 이므로 탁자 위 부장품으로 그리지 않음 — 시작 사진은 무늬 없는 회색 토기·천만.)")
d["updated_at"] = D; w(f, d)
f = R / "05_HISTORY_DATABASE/facts/CLM_EP01_GOODS_005.json"; d = rd(f)
if "EP01_S05_SH005" not in d.get("used_in", []): d.setdefault("used_in", []).append("EP01_S05_SH005")
w(f, d)

# 3) keep the split script from reintroducing the wrong claim on rerun
rep(R / "00_SYSTEM/tools/rights_gnm_split_20260913.py", [
 ('extra = " 말다래 = 천마도 그림 (RTS_WIKI_CHEONMADO_001), 별도 금동 말다래 기록 불필요." if sid == "EP01_S02_SH003" else ""', 'extra = ""  # superseded by fix_codex_review_20260913.py (mudguard = gilt-bronze, RTS_GNM_MUDGUARD_001)'),
])

# 4) reports / status / spec / plan
rep(EP / "15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md", [
 ("확인자: Claude Code (조사 전용, 데이터 변경 없음)", "확인자: Claude Code (조사 시점에는 데이터 변경 없음 → 2026-09-13 반영됨, 아래 '반영' 절)"),
 ("- 주의: 이 파일은 조사 기록일 뿐이며 권리 JSON, 샷 JSON은 수정하지 않았음.", "- 주의 (조사 시점 기준, 이후 '반영' 절로 대체됨): 이 파일은 조사 기록일 뿐이며 권리 JSON, 샷 JSON은 수정하지 않았음."),
 ("## 2. 제안 데이터 변경 (미적용. 승인 후 별도 커밋)", "## 2. 제안 데이터 변경 (조사 시점 미적용 → 2026-09-13 반영, '반영' 절)"),
 ("- 확인 필요 A 해소: S02_SH003 몽타주의 '말다래'는 **천마도 그림** — 이 샷에 이미 `RTS_WIKI_CHEONMADO_001` 이 연결돼 있음 → 금동 말다래 기록 만들지 않음.",
  "- 확인 필요 A 해소 (반박 검수 정정): S02_SH003 몽타주의 '말다래'는 **금동 천마무늬 말다래 (경주2309)** — 대본 v2 0:35–1:25 VO 'horse equipment', 유물 라이브러리 카드 7 배정. 천마도는 1:25–2:15 구간. → `RTS_GNM_MUDGUARD_001` 생성·연결 (천마도 기록은 유지). 앞선 '천마도' 판단은 근거 없이 내린 오류였음."),
 ("- 생성: `RTS_GNM_CHEST_ORNAMENT_001` · `RTS_GNM_GOLD_CAP_001` · `RTS_GNM_GLASS_CUP_001` (GREEN, ACTIVE).",
  "- 생성: `RTS_GNM_CHEST_ORNAMENT_001` · `RTS_GNM_GOLD_CAP_001` · `RTS_GNM_GLASS_CUP_001` · `RTS_GNM_MUDGUARD_001` (GREEN, ACTIVE). 증빙: 페이지 HTML 원문 `05_HISTORY_DATABASE/rights/proof/<rights_id>_20260913.html` (라벨 확인된 것만 proof 기재)."),
 ("- 샷 교체: S02_SH003 → GLASS_CUP · S05_SH001 → GOLD_CAP + CHEST_ORNAMENT.", "- 샷 교체: S02_SH003 → GLASS_CUP + MUDGUARD · S05_SH001 → GOLD_CAP + CHEST_ORNAMENT."),
 ("- 남은 일: 유리잔 표시 이미지 해상도 확인 (확인 필요 B), 모든 GREEN 기록 proof 캡처 보관.", "- 남은 일: 유리잔·말다래 표시 이미지 해상도 확인 (확인 필요 B), 기존 GREEN 기록(금관·금허리띠·천마도·NRICH) proof 보관."),
])
rep(EP / "15_QA/DATA_HYGIENE_20260913.md", [
 ("Prompts, DECISIONS, CURRENT_STATUS and the generation cache were not touched.", "This agent did not touch prompts, DECISIONS, CURRENT_STATUS or the generation cache (the orchestrator edited CURRENT_STATUS separately in the same batch)."),
 ("Result: `321/321 passed`, `cross-reference: OK`.", "Result at the time of these edits: `321/321 passed`, `cross-reference: OK` (the combined batch was re-validated before commit)."),
])
rep(R / "00_SYSTEM/CURRENT_STATUS.md", [
 ("- ~~YELLOW_ACTIVE 1건~~ **해소 (2026-09-13)**: `RTS_GNM_OTHER_OBJECTS_001` → 유리잔·금제 관모·가슴걸이 GREEN 1유형 분리, 원본은 BACKUP_ONLY. 남은 일: 유리잔 해상도 확인, GREEN proof 캡처.",
  "- ~~YELLOW_ACTIVE 1건~~ **해소 (2026-09-13)**: `RTS_GNM_OTHER_OBJECTS_001` → 유리잔·금제 관모·가슴걸이·천마무늬 말다래 GREEN 1유형 분리 (페이지 원문 proof 저장), 원본은 BACKUP_ONLY. 남은 일: 유리잔·말다래 표시 이미지 해상도 확인 (편집 전)."),
 ("YELLOW_ACTIVE 1 · YELLOW_BACKUP 3", "YELLOW_ACTIVE 0 · YELLOW_BACKUP 4 (2026-09-13)"),
 ("유리잔·금제 관모·가슴걸이 GREEN 3건 생성, S02_SH003·S05_SH001 연결 교체", "유리잔·금제 관모·가슴걸이·천마무늬 말다래 GREEN 4건 생성, S02_SH003·S05_SH001 연결 교체"),
])
rep(EP / "14_EDIT/GRAPHICS_SPEC_EP01_V2.md", [
 ("| `RTS_GNM_OTHER_OBJECTS_001` | 귀걸이·유리·토기·말갖춤 | 페이지별 확인 (KOGL 1 또는 4) | **YELLOW** (편집 확정 전 필수 해소, D-014) | S02_SH003, S05_SH001 | attribution_text 없음 → 해소 전 기재 불가. 4유형이면 사용 금지 |",
  "| `RTS_GNM_GLASS_CUP_001` | 천마총 유리잔 | KOGL Type 1 | GREEN · ACTIVE | S02_SH003 | Source: Gyeongju National Museum, Glass cup from Cheonmachong (Treasure), KOGL Type 1. |\n"
  "| `RTS_GNM_MUDGUARD_001` | 천마무늬 말다래 (경주2309) | KOGL Type 1 | GREEN · ACTIVE | S02_SH003 | Source: Gyeongju National Museum, Mudguard with winged-horse design from Cheonmachong (Gyeongju 2309), KOGL Type 1. |\n"
  "| `RTS_GNM_GOLD_CAP_001` | 천마총 금제 관모 | KOGL Type 1 | GREEN · ACTIVE | S05_SH001 | Source: Gyeongju National Museum, Gold cap from Cheonmachong (Gyeongju 2275), KOGL Type 1. |\n"
  "| `RTS_GNM_CHEST_ORNAMENT_001` | 천마총 가슴걸이 | KOGL Type 1 | GREEN · ACTIVE | S05_SH001 | Source: Gyeongju National Museum, Chest ornament from Cheonmachong (Gyeongju 2379), KOGL Type 1. |\n"
  "| `RTS_GNM_OTHER_OBJECTS_001` | 귀걸이·토기 (미확인분) | 페이지별 확인 | YELLOW · **BACKUP_ONLY** (2026-09-13) | 없음 | 사용 금지 (확인 전) |"),
 ("- **GREEN 레코드 4건 모두 `proof: null`** — 파일별 라이선스 캡처 저장 필요.", "- 2026-09-13 신규 GREEN 4건은 페이지 HTML 원문을 proof 로 저장. 기존 GREEN 4건 (금관·금허리띠·천마도·NRICH) 은 `proof: null` — 캡처 저장 필요."),
 ("금관·금허리띠(GREEN)는 해당, `RTS_GNM_OTHER_OBJECTS_001` (YELLOW) 은 해소 전 포함 불가.", "금관·금허리띠·유리잔·말다래·관모·가슴걸이 (GREEN) 해당. `RTS_GNM_OTHER_OBJECTS_001` 은 BACKUP_ONLY (미확인분, 포함 불가)."),
 ("- `RTS_GNM_OTHER_OBJECTS_001` YELLOW 해소 — 최종 편집 전", "- ~~`RTS_GNM_OTHER_OBJECTS_001` YELLOW 해소~~ 2026-09-13 해소 — 유리잔·말다래 표시 이미지 해상도 확인만 남음"),
])
rep(EP / "15_QA/AI_SHOT_PLAN_EP01.md", [
 ("| **새 시작 사진** (S04 기준 그림 참조) → 영상 |", "| **새 시작 사진** (문장만, 참고 그림 없음 — D-027 군중 규칙) → 영상 |"),
 ("| **새 시작 사진** (S04 참조) → 영상. 대안:", "| **새 시작 사진** (문장만, 참고 그림 없음 — D-027) → 영상. 대안:"),
 ("| FLOW_VEO | 35mm 초안 | **새 시작 사진** (시종 옷은 문장으로만) → 영상 |", "| FLOW_VEO | 50mm · 1.0m (카메라 초안) | **새 시작 사진** (시종 옷은 문장으로만, 금 유물 없음) → 영상 |"),
 ("- **G09 라벨**: H05 는 두 라벨 모두 필요한데 `ai_label` 칸에 하나뿐 (GRAPHICS_SPEC_EP01_V2 참고). 화면 최소 2초.", "- **G09 라벨**: H05 `ai_label` 에 두 라벨 반영됨 (2026-09-13 데이터 정리). 화면 최소 2초."),
])

# 5) video V02 texts: one main action, no build-order/ritual sentences (kept in negative)
BANS = ("Keep everything in the start image unchanged: the same era, clothing, colours, faces, layout, horizon and light; nothing new is added to the scene. "
        "No text, no captions, no subtitles, no watermark, no logo. No modern objects, no metal tools. Every person keeps their own face for the whole shot. "
        "Nobody looks at the camera, nobody poses, nobody speaks.")
VID = {
 "PRM_EP01_S04_SH004_V02": "Slow sideways tracking shot: the camera moves steadily from left to right at a slow walking pace, about three metres over six seconds, at the same height, no zoom, no tilt, no cut. One main action: the labourer in front strikes a wooden wedge with slow, steady wooden-mallet strokes while the two men beside him shift their grip on the long beam; everyone else stays almost still at their work. Dust drifts slowly in the air.",
 "PRM_EP01_S04_SH005_V02": "Slow push-in: the camera moves straight forward about six metres over six seconds at the same height, easing in from almost still, no pan, no tilt, no cut, ending closer on the open wooden chamber and the stone carriers in the middle ground. One main action: the stone carriers walk toward the chamber with a heavy, steady pace, their straw baskets swaying slightly on the shoulder poles; the timber workers at the left only breathe and shift slightly. Stones appear only against the outside of the chamber walls; no earth is added. The camera does not settle on any one face.",
 "PRM_EP01_S04_SH006_V02": "Locked-off static camera for the whole six seconds: no pan, no tilt, no zoom, no shake, no cut. One main action: a single line of small figures carries straw baskets of river stones on shoulder poles toward the wooden chamber at a natural steady pace; everyone else stays almost still; dust drifts slowly. Stones appear only against the outside of the chamber walls; no earth is added; no single person becomes a focus.",
 "PRM_EP01_S05_SH005_V02": "Very slow gentle push forward: the camera moves straight ahead about forty centimetres over four seconds, easing in and out, at table height, no pan, no tilt, no cut. One small action: one hand gently sets a plain grey stoneware vessel down beside a folded cloth; all other hands stay still. No object changes shape and nothing new appears.",
 "PRM_EP01_S06_SH002_V02": "Locked-off static camera for the whole six seconds: no pan, no tilt, no zoom, no cut. Quiet natural stillness only: everyone stays exactly where they are, with slight breathing and one small shift of weight; a light breeze moves the cloth and a little dust. The senior observer in blue in the foreground stays still, seen from behind, and does not turn. The open chamber and everything in it stay unchanged. No lip movement.",
 "PRM_EP01_S06_SH005_V02": "Slow steady forward dolly: the camera glides straight ahead about two metres over six seconds at a constant slow speed, staying at the same height directly behind the senior observer in blue; it does not pass him, circle or tilt, no cut. The observer stays completely still, seen only from behind: no head turn, no gesture. One main action in the distance: a few labourers walk slowly up the slope of the mound carrying straw baskets of earth; everyone else stays still; dust drifts in the low sunlight. The mound keeps its shape and size. No visions, no glow.",
}
for pid, motion in VID.items():
    f = EP / f"12_AI_VIDEO/prompt_{pid}.json"; d = rd(f)
    d["assembled_text"] = motion + " " + BANS
    d["created_by"] = d["created_by"].split(" | ")[0] + " | revised after Codex-role review: one main action, build-order/ritual sentences moved to negative only"
    w(f, d)

# 6) start stills
f = EP / "11_AI_STILLS/prompt_PRM_EP01_S04_SH004_START_V01.json"; d = rd(f)
d["shot_delta"] = d["shot_delta"].replace("S04 master frame as layout-only reference", "text-only, no reference image (D-027)")
if "text-only" not in d["shot_delta"]: d["shot_delta"] += " (text-only, no reference image, D-027)"
w(f, d)
f = EP / "11_AI_STILLS/prompt_PRM_EP01_S04_SH006_START_V01.json"; d = rd(f)
if "text-only" not in d["shot_delta"]: d["shot_delta"] += " (text-only, no reference image, D-027)"
w(f, d)
f = EP / "11_AI_STILLS/prompt_PRM_EP01_S05_SH005_START_V01.json"; d = rd(f)
d["assembled_text"] = " ".join([
 "One documentary photograph that fills the entire 16:9 frame edge to edge, a single still image; no black bars, no letterbox, no borders.",
 "Early Silla, Gyeongju, 5th century: close view of the hands of funeral attendants preparing grave goods on a low plain wooden plank table before burial.",
 "Hands come first: one pair of hands sets a plain grey stoneware vessel beside folded undyed hemp cloths; another pair rests on a folded cloth; a third pair holds a small plain grey stoneware vessel still.",
 "On the table: only several plain grey stoneware vessels and folded undyed hemp cloths.",
 "The attendants wear finer undyed hemp or ramie jackets with narrow sleeves, wrapped right over left and closed only by plain cloth belts, no ribbon ties; colours only undyed white, black and grey-brown; the narrow sleeve ends and wrists read clearly.",
 "The hands belong to different people: different ages from about 20 to 50, men and one woman, different skin tones and hand shapes; faces are mostly out of frame above the chin, and any partly visible face is a different person, calm and focused, not looking at the camera.",
 "Background soft and out of focus: plain earth floor and timber posts of a simple work shelter, no tiled roof.",
 "Camera about 1.0 metre high, at table height, close 50mm lens feel, shallow depth of field, soft indirect daylight.",
 "Photorealistic historical documentary still, style B Documentary Reenactment, natural skin and fabric textures, not glossy, earthy natural colours.",
 "Not a museum display: no glass cases, no labels, no stands, no spotlights.",
 "No gold objects, no fantasy jewels, no gemstones, no crown, no modern objects, no metal tools, no text, no watermark, no logo."])
d["shot_delta"] = "H03 start still: attendants' hands with plain grey stoneware vessels and folded hemp cloths only (no gold - the girdle is worn by the occupant, FACT), 50mm table height, text-only"
d["created_by"] = d["created_by"].split(" | ")[0] + " | revised after Codex-role review: gold removed, generic stoneware, 50mm per camera lock"
w(f, d)
print("codex review fixes applied; proof filled for:", sorted(VERIFIED))
