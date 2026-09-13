# -*- coding: utf-8 -*-
"""Apply SCRIPT_ROUGHCUT_DELTA resolutions X2/X3 to shot instances; add Cheonmachong layout fact/sources."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"; BY = "Claude Code (Continuity Engine / Historical QA)"
SH = R / "02_SEASONS/S01/EP01/07_SHOTS"
def rd(p): return json.loads(p.read_text(encoding="utf-8"))
def w(p, d): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# sources S3 / S4 (research-v2) as ledger instances
w(R/"05_HISTORY_DATABASE/sources/SRC_GNM_CHEONMA_EXHIBITION_001.json", {
 "source_id": "SRC_GNM_CHEONMA_EXHIBITION_001", "claim_ids": ["CLM_CHEONMACHONG_LAYOUT_001"],
 "title": "특별전 「천마, 다시 날다」 — 천마총 구조·부장품 (research-v2 S3)", "institution_or_author": "국립경주박물관",
 "url_or_path": "https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=110&mode=VD", "verified_at": D, "verified_by": BY,
 "excerpt_or_summary": "봉분 지름 47 m, 높이 12.7 m. 덧널 6.6×4.2 m, 널 2.15×0.8 m. 덧널 위 돌무지, 흙 봉분. 금관·금드리개·금귀걸이·고리자루칼은 무덤 주인을 안치한 널에. 부장품 궤(1.8×1.0 m)는 무덤 주인의 머리맡.",
 "confidence": "FACT", "uncertainty": "널 안 착장품의 신체 부위별 위치는 이 페이지에 명시 없음 (S4 로 보완).", "source_type": "MUSEUM", "rights_id": None,
 "notes": "전시 자료 일부는 공공누리 4유형 — 이미지 재사용은 rights 별도 확인 (research-v2 경고)."})
w(R/"05_HISTORY_DATABASE/sources/SRC_NRICH_CHEONMACHONG_DICT_001.json", {
 "source_id": "SRC_NRICH_CHEONMACHONG_DICT_001", "claim_ids": ["CLM_CHEONMACHONG_LAYOUT_001"],
 "title": "한국고고학사전 「천마총」 (research-v2 S4)", "institution_or_author": "국립문화유산연구원",
 "url_or_path": "https://portal.nrich.go.kr/kor/archeologyUsrView.do?idx=5195&menuIdx=797", "verified_at": D, "verified_by": BY,
 "excerpt_or_summary": "목관 안의 피장자는 동쪽으로 머리를 두고 금관·금제 세환이식·경흉식·금팔찌와 반지·금제 과대와 요패 등의 장신구를 착용. 목관 동쪽에 석단에 붙여 남북 장축의 부장품 수장궤 → 목관과 T자형 배치. 피장자 왼쪽 허리 아래 단봉환두대도 1점. 목관 밖 석단 동남쪽 모서리에 투조문 금제관모와 백화수피제 관모.",
 "confidence": "FACT", "uncertainty": "피장자 신원 불확실 (왕 또는 왕급). 연대 이견 있음.", "source_type": "EXCAVATION_REPORT", "rights_id": None, "notes": None})
w(R/"05_HISTORY_DATABASE/facts/CLM_CHEONMACHONG_LAYOUT_001.json", {
 "claim_id": "CLM_CHEONMACHONG_LAYOUT_001",
 "text_ko": "천마총 피장자는 목관 안에 머리를 동쪽으로 두고 금관·귀걸이·경흉식·과대 등을 착용한 상태였다. 부장품 궤는 머리맡(동쪽)에 목관과 T자로 놓였고, 금제관모·백화수피 관모는 목관 밖 석단 동남쪽 모서리에 있었다.",
 "text_en": "The Cheonmachong occupant lay in the coffin head to the east, wearing the gold crown, earrings, chest ornament and belt. The grave-goods chest sat at the head end in a T-layout; the gold and birch-bark caps lay outside the coffin at the SE corner of the stone platform.",
 "confidence": "FACT", "source_ids": ["SRC_NRICH_CHEONMACHONG_DICT_001", "SRC_GNM_CHEONMA_EXHIBITION_001"],
 "used_in": ["EP01_S07_SH005", "LOC_CHEONMACHONG_V01"], "hedge_required": False, "verified_at": D, "verified_by": BY,
 "notes": "X3 판정 근거. G13 단면 그래픽은 이 배치(머리 동쪽·금관 착용·머리맡 부장궤)만 그린다. 그 밖의 세부는 그리지 않는다."})

# location spatial lock update
p = R/"05_HISTORY_DATABASE/locations/LOC_CHEONMACHONG_V01.json"; d = rd(p)
d["spatial_lock"]["grave_goods_placement"] = "피장자 머리 동쪽, 금관·귀걸이·경흉식·과대 착장. 부장품 궤(1.8×1.0 m)는 머리맡에 T자 배치. 금제관모·백화수피 관모는 목관 밖 석단 동남 모서리. 환두대도는 왼쪽 허리 아래. (CLM_CHEONMACHONG_LAYOUT_001)"
d["spatial_lock"]["unverified_do_not_invent"] = "돌무지 높이·두께, 조성 기간, 작업 인원 수, 의례 순서."
d["fact_ids"] = ["CLM_CHEONMACHONG_LAYOUT_001"]; d["spatial_lock"]["source_refs"] = ["research-v2 S3", "research-v2 S4", "SRC_GNM_CHEONMA_EXHIBITION_001", "SRC_NRICH_CHEONMACHONG_DICT_001"]
w(p, d)

# X2: card wording -> script
p = SH/"shot_EP01_S03_SH005.json"; d = rd(p)
d["purpose"] = "G06 OCCUPANT: UNCERTAIN 카드"
d["notes"] = d["notes"].replace("[불일치 X2] 대본 v2 문구는 'OCCUPANT: UNCERTAIN'.", "X2 RESOLVED (D-010, 내용 → Script 우선): 문구 'OCCUPANT: UNCERTAIN'. 러프컷의 'WHO WAS BURIED HERE?' 는 보조 문구로만 (S4).")
d["updated_at"] = D; d["updated_by"] = BY; w(p, d)

# X3: insert G13 crown-position cross-section into S07 (5:42–5:46), shorten SH002
p = SH/"shot_EP01_S07_SH002.json"; d = rd(p)
d["duration"] = 4; d["notes"] = d["notes"].replace("TC 5:38–5:45", "TC 5:38–5:42") + " X3: 뒤에 SH005 G13 삽입으로 3초 단축."
d["updated_at"] = D; d["updated_by"] = BY; w(p, d)
base = rd(SH/"shot_EP01_S07_SH003.json")
new = dict(base); new.update({
 "shot_id": "EP01_S07_SH005", "duration": 4, "purpose": "G13 금관 위치 단면 — 피장자 머리 동쪽, 금관 착용, 머리맡 부장궤 (단순화 도식)",
 "era": "SILLA_EARLY", "location": "LOC_CHEONMACHONG_V01", "historical_confidence": "FACT",
 "camera_complexity": 10, "spatial_accuracy": 90, "human_motion": 0, "visual_importance": 80,
 "pipeline": "ORIGINAL_GRAPHIC", "characters": [], "costumes": [], "must_keep": [], "ai_label": None,
 "fact_ids": ["CLM_CHEONMACHONG_LAYOUT_001"], "version_history": [], "approved_version": None,
 "created_at": D, "updated_at": D, "updated_by": BY,
 "notes": "TC 5:42–5:46 (러프컷 v1 기준, 내레이션 녹음 후 조정). X3 RESOLVED (D-010, 사실 → Script 우선): 대본 v2 '금관 위치 단면, 고고학적으로 뒷받침될 때만' → S4 로 뒷받침됨. G13 은 legacy graphics-spec(G01–G12) 에 없는 신규 그래픽 → graphics-spec v2 필요 (legacy HTML 은 수정하지 않음). 그리는 것: 목관 안 피장자 머리 동쪽 + 머리 위 금관 + 머리맡 부장궤 T자. 그 외 세부 금지. 점수는 Continuity Engine 추정치 — P4 라우터에서 확정."})
w(SH/"shot_EP01_S07_SH005.json", new)
p = SH/"scene_EP01_S07.json"; d = rd(p)
if "EP01_S07_SH005" not in d["shot_ids"]: d["shot_ids"].append("EP01_S07_SH005")
d["updated_at"] = D; d["notes"] += " X3 반영: SH005 G13 추가 (2026-09-11)."; w(p, d)

# X1: narration = script v2 (content); G04 placement = roughcut (S04 only) -> note on S02 scene
p = SH/"scene_EP01_S02.json"; d = rd(p)
d["notes"] += " X1 RESOLVED (D-010): 내레이션은 대본 v2 전문 그대로 (러프컷 행은 첫 문장만 표기한 것). 'wooden burial spaces' 문장은 SH001 REAL + SH002 G03 위에 얹는다. G04 단면은 러프컷대로 S04 에서만 (배치 → Rough Cut 우선). 금관 매크로는 SH003 몽타주 첫 컷이 담당."
d["updated_at"] = D; w(p, d)
p = SH/"shot_EP01_S02_SH003.json"; d = rd(p)
d["notes"] = d["notes"].replace("[불일치 X1] 대본 v2 는 이 구간에 G04 단면 그래픽도 있으나 러프컷에는 없음.", "X1 RESOLVED: G04 는 S04 에서만. 몽타주 첫 컷 = 금관 매크로 (대본 v2 '슬로우 매크로').")
d["updated_at"] = D; w(p, d)
print("ok")
