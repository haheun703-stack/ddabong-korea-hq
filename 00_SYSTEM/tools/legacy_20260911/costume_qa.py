# -*- coding: utf-8 -*-
"""D-011 costume Historical QA: write sources/facts, resolve costume TBD with evidence grades."""
import json, sys
from pathlib import Path
ROOT = Path(sys.argv[1]); D = "2026-09-11"; BY = "Claude Code (Continuity Engine / Historical QA)"

def w(p, d):
    p = ROOT / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

SRC = {
 "SRC_NAHF_SILLA_CLOTHING_001": dict(title="신편 한국사 — 삼국의 문화 Ⅵ. 의식주 생활 1. 의생활 4) 신라의 의생활", inst="국사편찬위원회 (우리역사넷)", url="https://contents.history.go.kr/mobile/nh/view.do?levelId=nh_008_0070_0010_0040",
  ex="관을 유자례, 유(저고리)를 위해, 고(바지)를 가반, 화를 세라 함. 자·비·청·황 4색은 공복, 평인은 백색이나 흑색 옷이었을 것. 상류층 남자는 소매가 좁은 저고리와 넓은 바지, 서민 남자는 소매가 좁은 저고리와 좁은 바지. 근거 유물: 천마총 기마인물, 김유신묘 12지 호석상, 양직공도 신라 사신(소매 좁고 오른쪽 여밈, 넓은 바지).", conf="PROBABLE", unc="문헌·유물 종합 해석. '평인 백·흑'은 추정 표현.", typ="ACADEMIC"),
 "SRC_SAMGUKSAGI_SAEKBOK_001": dict(title="『삼국사기』 권33 잡지2 색복 — 신라 (사료로 본 한국사 '신라 귀족의 복식 문화')", inst="김부식 편 / 국사편찬위원회 번역·해설", url="https://contents.history.go.kr/front/hm/view.do?levelId=hm_036_0040",
  ex="법흥왕대 제도: 태대각간~대아찬 자주색 옷, 아찬~급찬 다홍색 옷(아홀), 대나마·나마 푸른색, 대사~선저지 누런색.", conf="FACT", unc="12세기 편찬 기록. 520년(법흥왕 7) 공복 제정으로 보는 것이 통설이나 일부 이견. 5세기 전반에도 같은 규정이 있었다는 근거는 아님.", typ="PRIMARY_RECORD"),
 "SRC_NMK_GEUMNYEONGCHONG_RIDER_001": dict(title="기마 인물형 토기 (금령총 출토, 국보, 본관9705)", inst="국립중앙박물관 소장품 검색", url="https://www.museum.go.kr/site/main/relic/search/view?relicId=3802",
  ex="신라, 경주 금령총. 주인상: 호화로운 관모를 쓰고 갑옷을 입음. 하인상: 상투 머리에 수건을 동여맸고 상체는 벗음. 당시 복식과 마구류 연구에 중요한 자료. 이미지 공공누리 1유형.", conf="FACT", unc="5~6세기 부장 명기. 하인 상체 노출은 명기 표현이라 실제 노동 복장 일반화에 주의.", typ="MUSEUM"),
 "SRC_AKS_ENCYKOREA_BOKSIK_001": dict(title="한국민족문화대백과사전 「복식」", inst="한국학중앙연구원 (집필 유송옥·김동욱)", url="https://encykorea.aks.ac.kr/Article/E0023690",
  ex="신라 초·중기 관모는 백화모 기본, 상부 귀족층 금관·금동관. 상의는 유 위에 표의, 귀족은 과대·서민은 포대. 하의는 바지. 발에 버선 + 운두 낮은 이, 관원·귀족은 발목 덮는 화. 고대 한국 복식은 좌임·우임 혼재.", conf="PROBABLE", unc="사전 서술('~한 것 같다') — 종합 추정.", typ="SECONDARY"),
 "SRC_KCULTURE_SILLA_TOU_001": dict(title="전통문화포털 — 시대별 한복 / 삼국시대·통일신라 (부상 토우)", inst="한국공예·디자인문화진흥원 (문화체육관광부)", url="https://www.kculture.or.kr/clothes/code/941/menu/921/idx/189/currentPage/3",
  ex="국립경주박물관 부상(夫像) 토우: 변형모를 쓰고, 주름을 선각으로 표현한 고 위에 둥근 깃의 유를 입고, 허리 앞에 요패를 늘인 과대 착용 — 신라 의례복의 일종으로 추측.", conf="PROBABLE", unc="토우 1점 기준. 의례복 추정.", typ="GOVERNMENT"),
 "SRC_KPEA_CHEONMACHONG_TEXTILE_001": dict(title="신라시대 섬유직물의 분석고찰 — 천마총 출토유물을 중심으로", inst="육영수·김상용, 『기술사』 1976.3", url="https://koreascience.kr/article/JAKO197652941873240.page",
  ex="천마총 출토 직물류 20여 편을 화학·물리 시험분석: 사용 섬유, 밀도, 섬도, 조직, 염색 상태 조사. 신라 당시 직물 명칭·품질·염색기술 추정.", conf="FACT", unc="초록만 확인. 섬유별 결론(견/마 비율)은 원문 PDF 확인 필요.", typ="ACADEMIC"),
 "SRC_KHAN_STRAW_SHOE_POTTERY_001": dict(title="죽은 자를 위한 신라·가야인들의 마지막 선물 — 온갖 모양의 토기·토우 (짚신 모양 토기)", inst="경향신문 2023-06-07 (국립중앙박물관 특별전 보도)", url="https://www.khan.co.kr/article/202306071601001",
  ex="신라 짚신 모양 이형토기에 나타난 짚신은 오늘날 짚신과 차이가 거의 없음.", conf="PROBABLE", unc="언론 보도. P3 에서 박물관 소장품 페이지로 교체 권장.", typ="SECONDARY"),
}
CLM = {
 "CLM_SILLA_COSTUME_001": dict(ko="신라 기본 복식은 상의 유(저고리)+하의 고(바지). 상류층 남자는 소매 좁은 저고리에 넓은 바지, 서민 남자는 소매 좁은 저고리에 좁은 바지.", en="Basic Silla dress = short jacket (yu) + trousers (go). Upper-class men: narrow sleeves with wide trousers; commoner men: narrow sleeves with narrow trousers.", conf="PROBABLE", src=["SRC_NAHF_SILLA_CLOTHING_001"], hedge=True),
 "CLM_SILLA_COSTUME_002": dict(ko="법흥왕대 관등별 공복색: 자(태대각간~대아찬)·비(아찬~급찬)·청(대나마·나마)·황(대사~선저지). 평인은 백·흑으로 추정.", en="Under King Beopheung, official robe colours by rank: purple, crimson, blue, yellow. Commoners probably white or black.", conf="FACT", src=["SRC_SAMGUKSAGI_SAEKBOK_001", "SRC_NAHF_SILLA_CLOTHING_001"], hedge=False, note="법령은 FACT. '평인 백·흑'은 PROBABLE. 5세기 전반 적용 여부는 불확실 → 5세기 장면에서는 색 위계만 참고."),
 "CLM_SILLA_COSTUME_003": dict(ko="관모: 초·중기 백화모(자작나무 껍질 모자) 기본, 상부 귀족층 금관·금동관. 금령총 주인상은 호화 관모, 하인상은 상투에 수건.", en="Headwear: birch-bark cap as base; gold/gilt-bronze crowns for top elite. Geumnyeongchong rider: master wears ornate cap, servant has topknot with cloth band.", conf="PROBABLE", src=["SRC_AKS_ENCYKOREA_BOKSIK_001", "SRC_NMK_GEUMNYEONGCHONG_RIDER_001"], hedge=True),
 "CLM_SILLA_COSTUME_004": dict(ko="허리띠: 귀족층은 과대(금속 장식 띠, 요패), 일반 서민은 포대(천 띠).", en="Belts: elite wore metal-plaque belts (gwadae) with pendants; commoners wore cloth belts.", conf="PROBABLE", src=["SRC_AKS_ENCYKOREA_BOKSIK_001", "SRC_KCULTURE_SILLA_TOU_001"], hedge=True),
 "CLM_SILLA_COSTUME_005": dict(ko="신발: 버선에 운두 낮은 이(履), 관원·귀족은 발목 덮는 화(靴). 짚신 모양 토기가 존재해 서민 짚신 사용 개연성.", en="Footwear: low shoes (ri) over socks; officials and elite wore ankle boots (hwa). Straw-sandal-shaped pottery suggests commoner straw sandals.", conf="PROBABLE", src=["SRC_AKS_ENCYKOREA_BOKSIK_001", "SRC_KHAN_STRAW_SHOE_POTTERY_001"], hedge=True),
 "CLM_SILLA_COSTUME_006": dict(ko="천마총에서 직물 20여 편이 출토되어 분석됨 (섬유·조직·염색). 말다래는 마직.", en="Some 20 textile fragments from Cheonmachong were analysed (fibre, weave, dye); the saddle flap used hemp cloth.", conf="FACT", src=["SRC_KPEA_CHEONMACHONG_TEXTILE_001"], hedge=False, note="서민 = 마직, 귀족 = 견직 일반화는 PROBABLE."),
 "CLM_SILLA_COSTUME_007": dict(ko="여밈: 양직공도 신라 사신·토용은 우임(오른쪽 여밈). 다만 고대 한국 복식은 좌임·우임 혼재.", en="Closure: the Silla envoy in Liang Zhigongtu and clay figures show right-over-left closure, though ancient Korean dress mixed both.", conf="PROBABLE", src=["SRC_NAHF_SILLA_CLOTHING_001", "SRC_AKS_ENCYKOREA_BOKSIK_001"], hedge=True),
 "CLM_SILLA_COSTUME_008": dict(ko="부상 토우(국립경주박물관): 변형모 + 둥근 깃 유 + 주름 잡은 고 + 요패 달린 과대 — 의례복으로 추정.", en="Husband figurine (Gyeongju NM): cap, round-collar jacket, pleated trousers, plaque belt with pendants — probably ceremonial dress.", conf="PROBABLE", src=["SRC_KCULTURE_SILLA_TOU_001"], hedge=True),
}
L, A, E = "COSTUME_SILLA_LABORER_A01", "COSTUME_SILLA_ATTENDANT_A01", "COSTUME_SILLA_ELITE_A01"
USED = {"CLM_SILLA_COSTUME_001": [L, A, E], "CLM_SILLA_COSTUME_002": [E, A], "CLM_SILLA_COSTUME_003": [L, E], "CLM_SILLA_COSTUME_004": [L, A, E],
        "CLM_SILLA_COSTUME_005": [L, A, E], "CLM_SILLA_COSTUME_006": [L, E], "CLM_SILLA_COSTUME_007": [L, A, E], "CLM_SILLA_COSTUME_008": [E]}
for sid, s in SRC.items():
    w(f"05_HISTORY_DATABASE/sources/{sid}.json", {"source_id": sid, "claim_ids": [c for c, v in CLM.items() if sid in v["src"]], "title": s["title"], "institution_or_author": s["inst"], "url_or_path": s["url"], "verified_at": D, "verified_by": BY, "excerpt_or_summary": s["ex"], "confidence": s["conf"], "uncertainty": s["unc"], "source_type": s["typ"], "rights_id": None, "notes": "복식 Historical QA (D-011) 용. 미디어 재사용 권리는 별개(P3 rights)."})
for cid, c in CLM.items():
    w(f"05_HISTORY_DATABASE/facts/{cid}.json", {"claim_id": cid, "text_ko": c["ko"], "text_en": c["en"], "confidence": c["conf"], "source_ids": c["src"], "used_in": USED[cid], "hedge_required": c["hedge"], "verified_at": D, "verified_by": BY, "notes": c.get("note")})

def upd(cid, elements, note):
    p = ROOT / f"05_HISTORY_DATABASE/costumes/{cid}.json"; d = json.loads(p.read_text(encoding="utf-8"))
    elements["qa_note"] = note
    d["elements"] = elements; d["historical_basis"] = "PROBABLE"
    d["fact_ids"] = sorted(c for c, u in USED.items() if cid in u); d["updated_at"] = D
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

upd(L, {
 "material": "마직(삼베류) 평직, 무염 생지 — PROBABLE (CLM_006 천마총 마직 확인 + CLM_002 평인 백·흑 추정)",
 "upper": "소매 좁은 저고리(유), 엉덩이선 길이, 직령, 우임 — PROBABLE (CLM_001, CLM_007). 노동 중 상체 노출 가능 — PROBABLE (CLM_003 금령총 하인상)",
 "lower": "통 좁은 바지(고), 정강이·발목 끈 묶음 가능 — PROBABLE (CLM_001; 묶음은 INTERPRETIVE)",
 "belt": "포대 — 천 허리끈, 금속 장식 없음 — PROBABLE (CLM_004)",
 "footwear": "짚신 또는 맨발 — PROBABLE (CLM_005 짚신 모양 토기)",
 "headwear": "상투 + 천 수건 동여맴, 또는 맨상투 — PROBABLE (CLM_003 금령총 하인상)",
 "color": "백·흑·생지색 — PROBABLE (CLM_002). 채도 높은 염색 없음. 자·비·청·황은 관등 공복색이므로 금지",
 "wear": "먼지·땀·해진 자국 (lived-in) — ARTISTIC",
 "forbidden": "조선 한복 실루엣, 갓, 명·청 복식, 사무라이 요소, 현대 원단, 공복 4색"},
 "D-011 근거 확정 2026-09-11. TBD 없음. 잔여 불확실: 바지 묶음 방식, 소매 선(襈) 유무.")
upd(A, {
 "material": "노동자보다 고운 마직 또는 저포 평직 — PROBABLE (CLM_006 유추). 견직은 귀족 전용으로 상정 — INTERPRETIVE",
 "upper": "소매 좁은 저고리(유), 엉덩이선 길이, 직령 우임, 노동자보다 정돈됨 — PROBABLE (CLM_001, CLM_007)",
 "lower": "통 좁은~중간 바지(고) — PROBABLE (CLM_001 서민형). 여성 시종은 저고리+치마 — PROBABLE (CLM_001 서민 여자)",
 "belt": "포대 (천 띠), 장식 최소 — PROBABLE (CLM_004)",
 "footwear": "운두 낮은 이(履) 또는 짚신 — PROBABLE (CLM_005)",
 "headwear": "상투 + 수건 또는 단순 건 — PROBABLE (CLM_003)",
 "color": "백·흑·회갈 등 무염 계열 — PROBABLE (CLM_002 평인). 공복 4색 금지 (관등 없는 인원)",
 "hands": "H03 은 손 클로즈업 중심 — 소매 끝·손목 디테일이 KEEP 대상",
 "forbidden": "조선 한복 실루엣, 궁중 예복, 판타지 사제복, 중국 황실 복식, 공복 4색"},
 "D-011 근거 확정 2026-09-11. TBD 없음. 잔여 불확실: 시종의 관등·계층(무관등 서민으로 상정).")
upd(E, {
 "material": "견직 표의 + 마/저 내의 — PROBABLE (CLM_006 천마총 직물 + CLM_004 귀족/서민 구분 유추)",
 "upper": "소매 좁은 유 위에 표의(포), 직령 우임, 둥근 깃 가능 — PROBABLE (CLM_001, CLM_007, CLM_008 부상 토우)",
 "lower": "통 넓은 바지(고), 주름 표현 가능 — PROBABLE (CLM_001 상류층, CLM_008)",
 "belt": "과대 — 금속 장식 띠 + 요패. 천마총 금제 허리띠 복제 금지(피장자 부장품) → 은·동 계열 절제형 — PROBABLE (CLM_004, CLM_008). 재질 선택은 INTERPRETIVE",
 "footwear": "발목 덮는 화(靴) + 버선 — PROBABLE (CLM_005 관원·귀족)",
 "headwear": "백화모(자작나무 껍질) 계열 또는 변형모 — PROBABLE (CLM_003, CLM_008). 금관·금동관 착용 금지 (왕·피장자 아님)",
 "color": "관등 공복색 위계 참고 — 최고위 자색은 피하고 비(다홍)·청 계열 — INTERPRETIVE (CLM_002; 5세기 적용 여부 불확실, 인물 관등 미설정)",
 "silhouette_priority": "H05 는 뒤에서 찍는다 → 뒷모습·어깨선·관모 실루엣이 연속성 핵심",
 "forbidden": "금관, 조선 곤룡포/관복, 명·청 황실 예복, 판타지 왕 연출, 자색(최고위 공복색)"},
 "D-011 근거 확정 2026-09-11. TBD 없음. 잔여 불확실 (사용자 결정 가능): 인물 관등 → 옷 색(비 vs 청), 과대 재질. 현재 INTERPRETIVE 로 표기.")
p = ROOT / "05_HISTORY_DATABASE/era/SILLA_EARLY.json"; d = json.loads(p.read_text(encoding="utf-8")); d["fact_ids"] = sorted(CLM)
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("written", len(SRC), "sources,", len(CLM), "facts, 3 costumes")
