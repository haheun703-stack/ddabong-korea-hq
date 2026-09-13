# -*- coding: utf-8 -*-
"""Switch RTS_GNM_GLASS_CUP_001 / RTS_GNM_MUDGUARD_001 to their e-Museum pages (3000 px images, KOGL Type 1, same museum number)
per 15_QA/ARCHIVE_IMAGE_RESOLUTION_20260913.md; note e-Museum Type 1 pages for chest ornament / gold cap (image size unverified).
Idempotent.  Usage: python 00_SYSTEM/tools/rights_emuseum_hires_20260913.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; RT = R / "05_HISTORY_DATABASE/rights"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
REP = "15_QA/ARCHIVE_IMAGE_RESOLUTION_20260913.md"
MARK = "e뮤지엄 원본 확인 (2026-09-13)"

UPD = {
 "RTS_GNM_GLASS_CUP_001": dict(
  source="https://www.emuseum.go.kr/detail?relicId=PS0100100200100238600000",
  attribution_text="Source: Gyeongju National Museum (e-Museum), Glass cup from Cheonmachong (Treasure, Gyeongju 2386), KOGL Type 1.",
  old_proof="05_HISTORY_DATABASE/rights/proof/RTS_GNM_GLASS_CUP_001_20260913.html",
  note=f"{MARK}: 명칭 琉璃製杯, 소장품번호 경주2386, 보물, 문구 '저작권 보호분야 \"琉璃製杯\" 저작물은 공공누리 출처표시 조건에 따라 이용할 수 있습니다.' / '제 1유형 : 출처표시'. "
       "표시 이미지 5장 3000px급 (3000×2243~2475, 조사 에이전트 측정) → 1080p 전체 화면 해상도 문제 해결. "
       "천마총 출토는 GNM 소장품 DB sub04/0402 mng_no=46 (출토지 천마총, 경주2386, 1유형, 원본 668×515)으로 교차 확인. "
       "기존 전시 해설 페이지 (613×816) 는 보조 출처, 그 증빙은 proof/RTS_GNM_GLASS_CUP_001_20260913.html 에 계속 보관. "
       "남은 일: 편집 전 브라우저 '이미지 다운로드' 파일 크기 기록. " + REP + "."),
 "RTS_GNM_MUDGUARD_001": dict(
  source="https://www.emuseum.go.kr/detail?relicId=PS0100100200100230900000",
  attribution_text="Source: Gyeongju National Museum (e-Museum), Mudguard with winged-horse design from Cheonmachong (Gyeongju 2309), KOGL Type 1.",
  old_proof="05_HISTORY_DATABASE/rights/proof/RTS_GNM_MUDGUARD_001_20260913.html",
  note=f"{MARK}: 명칭 透彫金銅板竹心被障泥, 소장품번호 경주2309, 재질 금동, 문구 '저작권 보호분야 \"透彫金銅板竹心被障泥\" 저작물은 공공누리 출처표시 조건에 따라 이용할 수 있습니다.' / '제 1유형 : 출처표시'. "
       "표시 이미지 3000×1933 (조사 에이전트 측정) = 기존 전시 해설 800×515 와 같은 사진 → 해상도 문제 해결 (확대 약 1.8배 한계). "
       "천마총 출토는 GNM 전시 해설 mng_no=295 (경주2309, 키워드 천마총)로 교차 확인, 그 증빙은 proof/RTS_GNM_MUDGUARD_001_20260913.html 에 계속 보관. "
       "국립중앙박물관 2014 보도자료 사진은 공공누리 3유형 (변경금지) → 사용 금지. "
       "남은 일: 편집 전 브라우저 '이미지 다운로드' 파일 크기 기록. " + REP + "."),
}
for rid, u in UPD.items():
    f = RT / f"{rid}.json"; d = rd(f)
    newp = f"05_HISTORY_DATABASE/rights/proof/{rid}_emuseum_20260913.html"
    assert (R / newp).exists(), newp
    assert (R / u["old_proof"]).exists(), u["old_proof"]
    html = (R / newp).read_text(encoding="utf-8", errors="replace")
    assert "공공누리" in html and "제 1유형" in html.replace("제1유형", "제 1유형"), rid
    d["source"] = u["source"]; d["attribution_text"] = u["attribution_text"]; d["proof"] = newp; d["checked_at"] = D
    n = d["notes"]
    n = n.replace("원본 다운로드 버튼 없음, 표시 이미지만 → 편집 전 해상도 확인.", "원본 다운로드 버튼 없음, 표시 이미지만 (해상도 부족 → 아래 e뮤지엄으로 해결).")
    n = n.replace(" 부족하면 소장품 DB/e뮤지엄 원본 페이지를 찾아 그 라벨을 다시 확인.", "")
    n = n.replace(" proof 캡처 미보관 (편집 전 저장).", "")
    if MARK not in n: n += " " + u["note"]
    d["notes"] = n; w(f, d)

SIDE = {"RTS_GNM_CHEST_ORNAMENT_001": ("PS0100100200100237900000", "頸飾", "600×959"),
        "RTS_GNM_GOLD_CAP_001": ("PS0100100200100227500000", "金製冠帽", "600×757")}
for rid, (relic, name, size) in SIDE.items():
    f = RT / f"{rid}.json"; d = rd(f)
    if "e뮤지엄 페이지 (2026-09-13)" not in d["notes"]:
        d["notes"] += (f" e뮤지엄 페이지 (2026-09-13): https://www.emuseum.go.kr/detail?relicId={relic} — '{name}', 같은 소장품번호, '제 1유형' 확인. "
                       f"GNM 원본 다운로드는 {size} 로 작음 → 전체 화면에 쓰려면 편집 전 e뮤지엄 이미지 크기 측정 필요 (미확인). {REP}.")
    w(f, d)

p = R / "02_SEASONS/S01/EP01/15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md"; s = p.read_text(encoding="utf-8")
if "## 해상도 해결 (2026-09-13)" not in s:
    s += ("\n## 해상도 해결 (2026-09-13)\n\n- 유리잔·말다래 → e뮤지엄 페이지로 출처 교체 (같은 소장품번호, 제 1유형, 3000px급). 증빙 `proof/<rights_id>_emuseum_20260913.html`, 기존 GNM 페이지 증빙도 보관.\n"
          "- 가슴걸이·금제 관모: e뮤지엄 1유형 페이지 확인, 이미지 크기 미측정 (전체 화면 사용 시 편집 전 확인).\n"
          f"- 상세: `{REP}`.\n")
    p.write_text(s, encoding="utf-8")

p = R / "02_SEASONS/S01/EP01/15_QA/ARCHIVE_IMAGE_RESOLUTION_20260913.md"; s = p.read_text(encoding="utf-8")
if "## 7. 반영 (2026-09-13)" not in s:
    s += ("\n## 7. 반영 (2026-09-13)\n\n- 5절 제안대로 `RTS_GNM_GLASS_CUP_001`·`RTS_GNM_MUDGUARD_001` 의 source·attribution_text·proof·notes 갱신 (`00_SYSTEM/tools/rights_emuseum_hires_20260913.py`).\n"
          "- e뮤지엄 페이지 원문 저장: `05_HISTORY_DATABASE/rights/proof/RTS_GNM_GLASS_CUP_001_emuseum_20260913.html`, `…MUDGUARD_001_emuseum_20260913.html` (라벨 '공공누리'·'제 1유형', 소장품번호 일치 재확인).\n"
          "- 가슴걸이 (`PS0100100200100237900000` 頸飾)·금제 관모 (`PS0100100200100227500000` 金製冠帽) e뮤지엄 페이지도 제 1유형·번호 일치. 이미지는 페이지 JS로 불러와 저장 HTML에서 크기 측정 못 함 → 미확인, 해당 기록 notes 에 기재.\n"
          "- 남은 일 (편집 전): 브라우저 '이미지 다운로드' 실제 파일 크기 기록.\n")
    p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
s = s.replace("남은 일: 유리잔·말다래 표시 이미지 해상도 확인 (편집 전).",
              "유리잔·말다래 해상도 **해결** — e뮤지엄 1유형 3000px급 페이지로 출처 교체 (2026-09-13). 가슴걸이·금제 관모 e뮤지엄 이미지 크기는 편집 전 확인.")
if "e뮤지엄" not in s.split("## 최근 변경")[1][:800]:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code (D-029)** — 권리 해상도: 유리잔 (경주2386)·말다래 (경주2309) 출처를 e뮤지엄 페이지로 교체 — 같은 유물번호, 공공누리 1유형, 사진 3000px급 → 1080p 전체 화면 가능. 페이지 원문 증빙 저장. 가슴걸이·금제 관모 e뮤지엄 1유형 확인 (크기 미측정).\n", 1)
p.write_text(s, encoding="utf-8")
print("emuseum hires applied")
