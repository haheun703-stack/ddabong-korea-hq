# -*- coding: utf-8 -*-
"""P3 Source/Rights Ledger: sources S1/S2/S5/S6, EP01 facts, rights, shot evidence links, QA report."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"; BY = "Claude Code (Story Engine Fact Check / Quality Engine Rights)"
SH = R / "02_SEASONS/S01/EP01/07_SHOTS"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): p = R / p; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# 1. shot schema: evidence_role
p = R / "00_SYSTEM/schemas/shot.schema.json"; s = rd(p)
if "evidence_role" not in s["properties"]:
    new = {}
    for k, v in s["properties"].items():
        new[k] = v
        if k == "fact_ids":
            new["evidence_role"] = {"type": "string", "enum": ["PRIMARY", "SUPPORTING", "CONTEXT", "NONE"],
              "description": "D-013. 이 샷이 fact_ids 에 대해 하는 역할: PRIMARY = 그 사실을 직접 보여주는 증거 화면 / SUPPORTING = 사실을 뒷받침·보완(재현 포함) / CONTEXT = 분위기·현재 맥락 / NONE = 역사 주장 없음(브랜드·방법론 카드). NONE 이 아니면 fact_ids 필수. ARCHIVE·AI 파이프라인은 NONE 불가."}
    s["properties"] = new
    w("00_SYSTEM/schemas/shot.schema.json", s)

# 2. sources (S3/S4 already exist)
SRC = {
 "SRC_UNESCO_GYEONGJU_001": dict(t="UNESCO World Heritage — Gyeongju Historic Areas (research-v2 S1)", i="UNESCO World Heritage Centre", u="https://whc.unesco.org/en/list/976/",
   ex="경주역사유적지구: 신라 도읍의 궁궐·사찰·성곽·왕릉군 유산 경관. 대릉원지구(Tumuli Park Belt)는 왕릉 3개 그룹, 대부분 돔형 봉분, 이중 목관을 자갈로 덮은 구조, 금·유리·토기 등 부장품. 5개 지구가 신라 도시 구조·사회 구조·생활상 증거.", c="FACT", unc="영상·사진은 All Rights Reserved (권리 RED).", ty="GOVERNMENT"),
 "SRC_GNM_SILLA_GOLD_001": dict(t="국립경주박물관 「신라, 황금의 나라」 (research-v2 S2)", i="국립경주박물관", u="https://gyeongju.museum.go.kr/kor/html/sub04/0403.html?mode=V&no=5053",
   ex="5세기~6세기 초 신라 황금문화 전성기: 지배층은 왕경에 거대 무덤을 만들고 피장자를 정교한 금제품으로 치장, 금으로 신성함·정통성·영원한 권위를 표현.", c="FACT", unc="박물관 공식 해석 (해석의 출처가 공식기관이라는 점이 FACT). 개별 유물 이미지 권리는 페이지별 확인.", ty="MUSEUM"),
 "SRC_NRICH_CONFERENCE_2023_001": dict(t="『천마총과 동아시아 고분문화』 학술대회 자료집 (research-v2 S5)", i="국립문화유산연구원 2023", u="https://portal.nrich.go.kr/kor/originalUsrView.do?info_idx=9001&menuIdx=1046",
   ex="수록 논문: 천마총을 통한 적석목곽분 구조 재검토 / 천마총 부장품 구성과 특징 / 천마총 장례 절차와 재현 전략. 장례 과정·표상 전략이 정식 연구 주제임을 확인.", c="FACT", unc="전문 미열람. 특정 결론을 이 논문에 귀속시키지 않는다.", ty="ACADEMIC"),
 "SRC_KOREA_KR_CHEONMADO_001": dict(t="천마총 천마도 정부 설명 (research-v2 S6)", i="korea.kr 정책브리핑", u="https://www.korea.kr/news/policyNewsView.do?newsId=148957403",
   ex="1973년 155호분 출토. 자작나무 껍질을 여러 겹 댄 말다래에 그림. 5~6세기 신라.", c="FACT", unc=None, ty="GOVERNMENT"),
}
# 3. facts
F = {
 "CLM_EP01_TOMBS_001": ("경주에는 신라 왕릉군이 집중되어 있고, 왕릉은 도시 경관의 일부다.", "Gyeongju holds concentrated Silla royal tomb groups that form part of the city landscape.", "FACT", ["SRC_UNESCO_GYEONGJU_001"], False, None),
 "CLM_EP01_TUMULI_002": ("대릉원지구는 왕릉 3개 그룹으로 구성, 대부분 돔형 봉분. 목곽을 자갈로 덮은 구조이며 금·유리·토기 등이 출토됐다.", "Tumuli Park Belt has three tomb groups, mostly domed; wooden chambers covered with gravel; gold, glass and ceramics excavated.", "FACT", ["SRC_UNESCO_GYEONGJU_001"], False, None),
 "CLM_EP01_EXCAV_003": ("천마총은 1973년 황남동 155호분으로 발굴됐다(황남대총 발굴 전 시험 발굴). 11,526점 수습. 1974년 천마도 말다래에서 따 명명.", "Cheonmachong was excavated in 1973 as Tomb No. 155 (test dig before Hwangnamdaechong); 11,526 objects; named in 1974 after the heavenly-horse saddle flap.", "FACT", ["SRC_GNM_CHEONMA_EXHIBITION_001"], False, "대본 v2 'more than eleven thousand' 과 일치."),
 "CLM_EP01_STRUCT_004": ("천마총은 목곽(6.6×4.2 m)에 관(2.15×0.8 m)을 넣고 위에 돌을 쌓은 뒤 흙 봉분(지름 47 m·높이 12.7 m)을 올린 구조다.", "Cheonmachong: wooden chamber 6.6×4.2 m with coffin 2.15×0.8 m, stones piled above, earth mound 47 m across and 12.7 m high.", "FACT", ["SRC_GNM_CHEONMA_EXHIBITION_001", "SRC_NRICH_CHEONMACHONG_DICT_001"], False, None),
 "CLM_EP01_GOODS_005": ("금관·귀걸이·장신구·무기·용기·칠기·유리·말갖춤이 피장자와 부장궤에 부장됐다. 자작나무 껍질 말다래에 천마가 그려져 있다.", "Gold crown, earrings, ornaments, weapons, vessels, lacquerware, glass and horse gear were placed with the dead and in the chest; the birch-bark saddle flap bears a heavenly horse.", "FACT", ["SRC_GNM_CHEONMA_EXHIBITION_001", "SRC_KOREA_KR_CHEONMADO_001"], False, None),
 "CLM_EP01_OCCUPANT_006": ("피장자는 규모·유물로 보아 왕 또는 왕에 준하는 인물로 추정되나, 신원은 확정되지 않았다.", "The occupant was probably a king or of comparable rank, but the identity is not certain.", "FACT", ["SRC_NRICH_CHEONMACHONG_DICT_001"], False, "불확실성 자체가 사실. 특정 왕 이름을 대지 않는다."),
 "CLM_EP01_GOLD_007": ("국립경주박물관은 5세기~6세기 초 신라 지배층이 왕경에 거대 무덤을 만들고 금으로 신성함·정통성·영원한 권위를 표현했다고 설명한다.", "Gyeongju National Museum states that in the 5th–early 6th c. the Silla elite built huge tombs in the capital and used gold to express sacredness, legitimacy and enduring authority.", "FACT", ["SRC_GNM_SILLA_GOLD_001"], False, "박물관 공식 해석을 인용하는 형태로만 FACT. 내레이션은 'The museum describes…' 를 유지."),
 "CLM_EP01_FUNERAL_008": ("이 규모의 장례는 단순한 사적 이별이 아니라 조직된 사회적 행사였을 수 있다.", "A funeral on this scale may have been an organised social event rather than a private farewell.", "INTERPRETIVE", ["SRC_GNM_CHEONMA_EXHIBITION_001", "SRC_NRICH_CONFERENCE_2023_001"], True, None),
 "CLM_EP01_DISPLAY_009": ("매장의 과시는 산 자들에게 위계와 권위를 전달했을 수 있다.", "Burial display may have communicated hierarchy and authority to the living.", "INTERPRETIVE", ["SRC_GNM_SILLA_GOLD_001"], True, None),
 "CLM_EP01_ORDER_010": ("지배자의 죽음은 사회·정치 질서를 재확인할 필요를 만들었을 수 있다.", "The death of a ruler may have created a need to reaffirm social and political order.", "INTERPRETIVE", ["SRC_GNM_SILLA_GOLD_001", "SRC_NRICH_CONFERENCE_2023_001"], True, "금지: '질서 유지를 위해 지었다'를 단정. 'allows us to ask whether' 형태만."),
 "CLM_EP01_MOUND_011": ("봉분은 지위와 기억을 눈에 보이게 하는 진술로 기능했을 수 있다.", "The mound may have operated as a visible statement of rank and memory.", "INTERPRETIVE", ["SRC_UNESCO_GYEONGJU_001", "SRC_GNM_SILLA_GOLD_001"], True, None),
 "CLM_EP01_MODERN_012": ("현재 경주 도심에서는 도로·주택·상점 사이로 왕릉 봉분이 솟아 있고, 사람들이 그 사이를 걷는다.", "In present-day Gyeongju the mounds rise among roads, houses and shops, and people walk between them.", "FACT", ["SRC_UNESCO_GYEONGJU_001"], False, "현장 촬영이 직접 증거. UNESCO 는 '도시 안의 유산 경관' 맥락 출처."),
 "CLM_EP01_RITES_013": ("천마총의 장례 절차와 재현(표상) 전략은 국립문화유산연구원 학술대회의 정식 연구 주제다.", "Cheonmachong funeral procedure and representational strategy are formal research topics at an NRICH conference.", "FACT", ["SRC_NRICH_CONFERENCE_2023_001"], False, "특정 결론을 인용하지 않는다."),
}
# 4. rights (external assets only)
RT = {
 "RTS_NRICH_1973_PHOTOS_001": ("ASSET_NRICH_1973_EXCAVATION_SET_V01", "https://portal.nrich.go.kr/kor/textbookUseCulturalUsrView.do?idx=2&menuIdx=1229", "국립문화유산연구원 기록관", "KOGL Type 1", "YES", "YES", "YES", "Source: National Research Institute of Cultural Heritage (NRICH), Cheonmachong excavation photographs, 1973, KOGL Type 1.", "GREEN", "archive-photos 페이지에서 항목별 제1유형 확인. 다운로드 시 파일마다 라벨 재확인 후 proof 캡처 저장. 2019 간행물 PDF 캡처는 금지 (별도 RED)."),
 "RTS_GNM_GOLD_CROWN_001": ("ASSET_GNM_CHEONMACHONG_GOLD_CROWN_V01", "https://gyeongju.museum.go.kr/kor/html/sub04/0406.html?GotoPage=32&dvs_code=&mng_no=59&mode=V", "국립경주박물관", "KOGL Type 1", "YES", "YES", "YES", "Source: Gyeongju National Museum, Gold crown from Cheonmachong, KOGL Type 1.", "GREEN", "visual-assets B1 공식 1순위."),
 "RTS_WIKI_GOLD_CROWN_002": ("ASSET_WIKI_CHEONMACHONG_GOLD_CROWN_V01", "https://commons.wikimedia.org/wiki/File:Gold_crown_from_Cheonmachong.jpg", "Wikimedia Commons 업로더 (페이지 확인)", "CC BY 2.0", "YES", "YES", "YES", "Gold crown from Cheonmachong — [author], CC BY 2.0, via Wikimedia Commons.", "GREEN", "B2 백업. 저작자명 페이지에서 확정 후 attribution_text 채움."),
 "RTS_GNM_GOLD_GIRDLE_001": ("ASSET_GNM_CHEONMACHONG_GOLD_GIRDLE_V01", "https://commons.wikimedia.org/wiki/File:%ED%97%88%EB%A6%AC%EB%9D%A0.jpg", "국립경주박물관 (Commons 경유)", "KOGL Type 1", "YES", "YES", "YES", "Source: Gyeongju National Museum, Gold girdle from Cheonmachong, KOGL Type 1.", "GREEN", "B3."),
 "RTS_WIKI_CHEONMADO_001": ("ASSET_WIKI_CHEONMADO_V01", "https://commons.wikimedia.org/wiki/File:Korea-Silla-Cheonmado-01.jpg", "Public Domain (원작 5–6세기)", "Public Domain Mark", "YES", "YES", "NO", "Cheonmado (Heavenly Horse painting), Public Domain, via Wikimedia Commons.", "GREEN", "B4. 라이선스 페이지 캡처를 proof 로 보관."),
 "RTS_GNM_OTHER_OBJECTS_001": ("ASSET_GNM_CHEONMACHONG_OTHER_OBJECTS_V01", "https://gyeongju.museum.go.kr/", "국립경주박물관", "페이지별 확인 필요 (KOGL 1 또는 4)", "UNKNOWN", "UNKNOWN", "YES", None, "YELLOW", "B5 귀걸이·유리·토기·말갖춤. 소장품 페이지마다 라벨 확인 → 1유형이면 개별 GREEN 인스턴스로 분리. 4유형이면 사용 금지."),
 "RTS_GYEONGJU_CITY_IMAGE_001": ("ASSET_GYEONGJU_CITY_TOURISM_IMAGE_V01", "https://www.gyeongju.go.kr/gyeongjuimage/page.do?mnu_uid=2409", "경주시", "출처표시 조건, 상업 범위 불명확", "UNKNOWN", "UNKNOWN", "YES", None, "YELLOW", "A1 백업. 수익화 영상 사용은 서면 확인 후. 기본은 자체 촬영(BLUE)."),
 "RTS_WIKI_DAEREUNGWON_001": ("ASSET_WIKI_DAEREUNGWON_2006_V01", "https://commons.wikimedia.org/wiki/File:Royal_Silla_burial_mounds_2006c.jpg", "Wikimedia Commons 업로더", "CC BY-SA 2.0", "YES", "YES", "YES", None, "YELLOW", "A2 백업. Share-Alike 의무 수용 여부 결정 필요."),
 "RTS_WIKI_CHEONMACHONG_ENTRANCE_001": ("ASSET_WIKI_CHEONMACHONG_ENTRANCE_V01", "https://commons.wikimedia.org/wiki/File:Cheonmachong_%EC%B2%9C%EB%A7%88%EC%B4%9D_%E5%A4%A9%E9%A6%AC%E5%A1%9A_(5329004409).jpg", "Wikimedia Commons 업로더", "CC BY-SA 2.0", "YES", "YES", "YES", None, "YELLOW", "A3 백업. 동일 SA 이슈."),
 "RTS_NRICH_2019_PUBLICATION_001": ("ASSET_NRICH_CHEONMACHONG_2019_BOOK_V01", "https://portal.nrich.go.kr/", "국립문화유산연구원", "KOGL Type 4", "NO", "NO", "YES", None, "RED", "C2 「천마총, 발굴조사의 기록」. 연구 참고만. 캡처·재사용 금지."),
 "RTS_UNESCO_NHK_VIDEO_001": ("ASSET_UNESCO_NHK_GYEONGJU_VIDEO_V01", "https://whc.unesco.org/en/list/976/", "UNESCO / NHK", "All rights reserved", "NO", "NO", "YES", None, "RED", "C3. 참고만. 리핑 금지."),
}
for sid, s in SRC.items():
    w(f"05_HISTORY_DATABASE/sources/{sid}.json", {"source_id": sid, "claim_ids": [c for c, v in F.items() if sid in v[3]], "title": s["t"], "institution_or_author": s["i"], "url_or_path": s["u"], "verified_at": D, "verified_by": BY, "excerpt_or_summary": s["ex"], "confidence": s["c"], "uncertainty": s["unc"], "source_type": s["ty"], "rights_id": None, "notes": "research-v2 source map 정규화 (P3)."})
for sid in ("SRC_GNM_CHEONMA_EXHIBITION_001", "SRC_NRICH_CHEONMACHONG_DICT_001"):
    p = R / f"05_HISTORY_DATABASE/sources/{sid}.json"; d = rd(p)
    d["claim_ids"] = sorted(set(d["claim_ids"]) | {c for c, v in F.items() if sid in v[3]}); w(f"05_HISTORY_DATABASE/sources/{sid}.json", d)
for rid, (a, src, cr, lic, com, mod, att, txt, st, note) in RT.items():
    w(f"05_HISTORY_DATABASE/rights/{rid}.json", {"rights_id": rid, "asset_id": a, "source": src, "creator": cr, "license": lic, "commercial_use": com, "modification_allowed": mod, "attribution_required": att, "attribution_text": txt, "expiration": None, "proof": None, "research_permission": "YES", "media_reuse_permission": "YES" if st == "GREEN" else ("NO" if st == "RED" else "UNKNOWN"), "status": st, "checked_at": D, "checked_by": BY, "notes": note})

# 5. shot evidence map: shot -> (role, facts, rights)
NR, CR, CR2, GD, CM, OT = "RTS_NRICH_1973_PHOTOS_001", "RTS_GNM_GOLD_CROWN_001", "RTS_WIKI_GOLD_CROWN_002", "RTS_GNM_GOLD_GIRDLE_001", "RTS_WIKI_CHEONMADO_001", "RTS_GNM_OTHER_OBJECTS_001"
T, TU, EX, ST, GO, OC, GL, FU, DI, OR, MO, MD, RI, LY = ["CLM_EP01_TOMBS_001"], ["CLM_EP01_TUMULI_002"], ["CLM_EP01_EXCAV_003"], ["CLM_EP01_STRUCT_004"], ["CLM_EP01_GOODS_005"], ["CLM_EP01_OCCUPANT_006"], ["CLM_EP01_GOLD_007"], ["CLM_EP01_FUNERAL_008"], ["CLM_EP01_DISPLAY_009"], ["CLM_EP01_ORDER_010"], ["CLM_EP01_MOUND_011"], ["CLM_EP01_MODERN_012"], ["CLM_EP01_RITES_013"], ["CLM_CHEONMACHONG_LAYOUT_001"]
M = {
 "EP01_S01_SH001": ("CONTEXT", MD, []), "EP01_S01_SH002": ("CONTEXT", T+MD, []), "EP01_S01_SH003": ("SUPPORTING", T, []), "EP01_S01_SH004": ("SUPPORTING", T, []),
 "EP01_S02_SH001": ("SUPPORTING", T+TU, []), "EP01_S02_SH002": ("PRIMARY", TU, []), "EP01_S02_SH003": ("PRIMARY", GO+TU, [CR, CM, OT]),
 "EP01_S03_SH001": ("CONTEXT", EX, []), "EP01_S03_SH002": ("PRIMARY", EX, [NR]), "EP01_S03_SH003": ("PRIMARY", EX+GO, [NR]), "EP01_S03_SH004": ("PRIMARY", GO, [CR, CM]), "EP01_S03_SH005": ("PRIMARY", OC, []),
 "EP01_S04_SH001": ("PRIMARY", ST, [NR]), "EP01_S04_SH002": ("PRIMARY", ST+LY, []), "EP01_S04_SH003": ("PRIMARY", ST, []), "EP01_S04_SH004": ("SUPPORTING", ST+FU, []), "EP01_S04_SH005": ("SUPPORTING", ST+FU, []), "EP01_S04_SH006": ("SUPPORTING", ST+FU, []), "EP01_S04_SH007": ("SUPPORTING", ST, [NR]),
 "EP01_S05_SH001": ("PRIMARY", GL+GO, [CR, GD, OT]), "EP01_S05_SH002": ("PRIMARY", GL, []), "EP01_S05_SH003": ("PRIMARY", GO+LY, [NR]), "EP01_S05_SH004": ("PRIMARY", GO, [GD]), "EP01_S05_SH005": ("SUPPORTING", GL+DI, []), "EP01_S05_SH006": ("PRIMARY", GL, [CR]),
 "EP01_S06_SH001": ("NONE", [], []), "EP01_S06_SH002": ("SUPPORTING", FU+OR, []), "EP01_S06_SH003": ("SUPPORTING", ST, [NR]), "EP01_S06_SH004": ("SUPPORTING", GL, [CR]), "EP01_S06_SH005": ("SUPPORTING", OR+DI, []), "EP01_S06_SH006": ("SUPPORTING", GL, [CR]), "EP01_S06_SH007": ("CONTEXT", MD+MO, []), "EP01_S06_SH008": ("NONE", [], []), "EP01_S06_SH009": ("SUPPORTING", EX, [NR]), "EP01_S06_SH010": ("SUPPORTING", ST+MO+DI, []), "EP01_S06_SH011": ("CONTEXT", MD, []),
 "EP01_S07_SH001": ("PRIMARY", GO, [CR]), "EP01_S07_SH002": ("SUPPORTING", LY, [NR]), "EP01_S07_SH003": ("SUPPORTING", GL, [CR]), "EP01_S07_SH004": ("SUPPORTING", GL+DI, [CR]), "EP01_S07_SH005": ("PRIMARY", LY, []),
 "EP01_S08_SH001": ("CONTEXT", MD, []), "EP01_S08_SH002": ("SUPPORTING", ST+MO, []), "EP01_S08_SH003": ("CONTEXT", MD+T, []),
 "EP01_S09_SH001": ("SUPPORTING", EX, [NR]), "EP01_S09_SH002": ("SUPPORTING", GL, [CR]), "EP01_S09_SH003": ("CONTEXT", MD, []), "EP01_S09_SH004": ("CONTEXT", MD, []), "EP01_S09_SH005": ("NONE", [], []),
}
CONF = {c: v[2] for c, v in F.items()}; CONF["CLM_CHEONMACHONG_LAYOUT_001"] = "FACT"
RANK = {"FACT": 3, "PROBABLE": 2, "INTERPRETIVE": 1, "ARTISTIC": 0}
used = {c: [] for c in CONF}
changed_conf = []
for sid, (role, facts, rights) in M.items():
    p = SH / f"shot_{sid}.json"; d = rd(p)
    d["evidence_role"] = role; d["fact_ids"] = facts; d["rights_ids"] = rights
    if facts:
        best = max(RANK[CONF[c]] for c in facts)
        if RANK[d["historical_confidence"]] > best:
            changed_conf.append((sid, d["historical_confidence"], [k for k, v in RANK.items() if v == best][0]))
            d["historical_confidence"] = [k for k, v in RANK.items() if v == best][0]
    for c in facts: used[c].append(sid)
    d["updated_at"] = D; d["updated_by"] = BY
    w(f"02_SEASONS/S01/EP01/07_SHOTS/shot_{sid}.json", d)
for cid, (ko, en, conf, src, hedge, note) in F.items():
    w(f"05_HISTORY_DATABASE/facts/{cid}.json", {"claim_id": cid, "text_ko": ko, "text_en": en, "confidence": conf, "source_ids": src, "used_in": used[cid], "hedge_required": hedge, "verified_at": D, "verified_by": BY, "notes": note})
p = R / "05_HISTORY_DATABASE/facts/CLM_CHEONMACHONG_LAYOUT_001.json"; d = rd(p); d["used_in"] = sorted(set(used["CLM_CHEONMACHONG_LAYOUT_001"]) | {"LOC_CHEONMACHONG_V01"}); w("05_HISTORY_DATABASE/facts/CLM_CHEONMACHONG_LAYOUT_001.json", d)

# 6. report
shots = [rd(SH / f"shot_{s}.json") for s in M]
roles = {r: sum(1 for s in shots if s["evidence_role"] == r) for r in ("PRIMARY", "SUPPORTING", "CONTEXT", "NONE")}
yellow = [(s["shot_id"], r) for s in shots for r in s["rights_ids"] if RT[r][8] == "YELLOW"]
lines = ["# EP01 P3 Source/Rights Ledger — 검증 리포트", "", f"> 생성 {D} · {BY} · 생성 스크립트 출력, 손으로 고치지 않는다 (재생성).", "> 규칙: D-010 (Script/Fact 우선) · D-013 (evidence_role) · 정본 §9 §10.", "",
 "## 요약", "", f"- 출처 SOURCE: {len(SRC) + 2} (research-v2 S1–S6 전부 정규화) + 복식 7 = {len(SRC) + 9}", f"- 사실 FACT/CLAIM: EP01 {len(F)} + 천마총 배치 1 + 복식 8 = {len(F) + 9}", f"- 권리 RIGHTS: {len(RT)} — GREEN {sum(1 for v in RT.values() if v[8]=='GREEN')} · YELLOW {sum(1 for v in RT.values() if v[8]=='YELLOW')} · RED {sum(1 for v in RT.values() if v[8]=='RED')}",
 f"- 샷 {len(shots)}: evidence_role PRIMARY {roles['PRIMARY']} · SUPPORTING {roles['SUPPORTING']} · CONTEXT {roles['CONTEXT']} · NONE {roles['NONE']}", f"- fact 미연결 샷: {sum(1 for s in shots if s['evidence_role']!='NONE' and not s['fact_ids'])} · ARCHIVE 권리 미연결: {sum(1 for s in shots if s['pipeline']=='ARCHIVE' and not s['rights_ids'])} · RED 권리 사용: {sum(1 for s in shots for r in s['rights_ids'] if RT[r][8]=='RED')}", ""]
if changed_conf:
    lines += ["## 과도한 해석 자동 하향 (샷 등급 > 근거 등급)", ""] + [f"- `{s}`: {a} → {b}" for s, a, b in changed_conf] + [""]
lines += ["## YELLOW 권리 — 사용 전 확인 필요", ""] + [f"- `{s}` ← `{r}`: {RT[r][9]}" for s, r in yellow] + ["", "## 샷별 연결", "", "| shot | pipeline | conf | role | facts | rights |", "|---|---|---|---|---|---|"]
lines += [f"| {s['shot_id']} | {s['pipeline']} | {s['historical_confidence']} | {s['evidence_role']} | {' '.join(c.replace('CLM_EP01_','').replace('CLM_CHEONMACHONG_','') for c in s['fact_ids']) or '—'} | {' '.join(r.replace('RTS_','') for r in s['rights_ids']) or '—'} |" for s in shots]
lines += ["", "## 내레이션 금지 문장 (research-v2 DO NOT STATE)", "", "- “Silla people believed the king remained politically powerful after death.”", "- “The tomb was built specifically to prevent political instability.”", "- “A Silla official ordered the tomb to demonstrate continuity of government.”", "- 사료에 없는 인용문을 역사적 발언처럼 제시.", "", "INTERPRETIVE 사실(008–011)은 `hedge_required = true` → 내레이션에 may / allows us to ask whether / one way to understand 필수.", "", "## 남은 일", "", "- YELLOW 권리 확인 후 GREEN/RED 로 확정 (B5 는 페이지별 분리).", "- 다운로드한 파일마다 `proof` (라이선스 페이지 캡처 경로) 기입.", "- 짚신 출처 `SRC_KHAN_STRAW_SHOE_POTTERY_001` 을 박물관 페이지로 교체.", "- Wikimedia CC BY 자산은 저작자명 확정 후 `attribution_text` 완성."]
(R / "02_SEASONS/S01/EP01/15_QA/P3_LEDGER_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("sources", len(SRC), "facts", len(F), "rights", len(RT), "shots", len(M), "roles", roles, "conf-lowered", changed_conf, "yellow", len(yellow))
