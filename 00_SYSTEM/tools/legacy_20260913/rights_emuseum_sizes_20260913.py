# -*- coding: utf-8 -*-
"""Record measured e-Museum image sizes (live page fetch with session cookie, 2026-09-13) for the 4 GNM GREEN records;
switch chest ornament / gold cap source to e-Museum (Type 1, same number). Idempotent.
Usage: python 00_SYSTEM/tools/rights_emuseum_sizes_20260913.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; RT = R / "05_HISTORY_DATABASE/rights"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
REP = "15_QA/ARCHIVE_IMAGE_RESOLUTION_20260913.md"; MARK = "크기 실측 (2026-09-13"

SIZES = {
 "RTS_GNM_GLASS_CUP_001": "표시 이미지 5장 3000×2243~2475 재측정 일치. 페이지에 적힌 원본 크기 8662×7148 · 8698×6651 · 8704×6876 · 11605×8680 · 11605×8706 (다운로드 버튼 파일은 미확인).",
 "RTS_GNM_MUDGUARD_001": "표시 이미지 3000×1933 재측정 일치. 페이지에 적힌 원본 크기 5454×3516 (다운로드 버튼 파일은 미확인).",
 "RTS_GNM_CHEST_ORNAMENT_001": "e뮤지엄 표시 이미지 2000×3000 (세로 사진) → 1080p 전체 화면 가능 (세로로 긴 사진이라 가로 화면에서는 위아래 이동/부분 확대). 페이지에 적힌 원본 크기 2000×3000.",
 "RTS_GNM_GOLD_CAP_001": "e뮤지엄 표시 이미지 3000×2000 → 1080p 전체 화면 가능. 페이지에 적힌 원본 크기 3000×2000.",
}
SRC = {"RTS_GNM_CHEST_ORNAMENT_001": ("https://www.emuseum.go.kr/detail?relicId=PS0100100200100237900000",
          "Source: Gyeongju National Museum (e-Museum), Chest ornament from Cheonmachong (Gyeongju 2379), KOGL Type 1."),
       "RTS_GNM_GOLD_CAP_001": ("https://www.emuseum.go.kr/detail?relicId=PS0100100200100227500000",
          "Source: Gyeongju National Museum (e-Museum), Gold cap from Cheonmachong (Gyeongju 2275), KOGL Type 1.")}
for rid, txt in SIZES.items():
    f = RT / f"{rid}.json"; d = rd(f); n = d["notes"]
    n = n.replace("(조사 에이전트 측정)", "(조사 에이전트 측정, 봇 재측정 일치)")
    n = n.replace("→ 전체 화면에 쓰려면 편집 전 e뮤지엄 이미지 크기 측정 필요 (미확인).", "→ e뮤지엄 이미지로 해결 (아래 실측).")
    if MARK not in n:
        n += f" {MARK}, 세션 쿠키로 페이지가 직접 내주는 이미지): {txt}"
    if rid in SRC:
        if d["source"] != SRC[rid][0]:
            n += f" 출처를 e뮤지엄으로 교체 (2026-09-13). 기존 GNM 소장품 DB 페이지 {d['source']} 는 천마총 출토 교차 확인용, 그 증빙 {d['proof']} 계속 보관."
        d["source"], d["attribution_text"] = SRC[rid]
        newp = f"05_HISTORY_DATABASE/rights/proof/{rid}_emuseum_20260913.html"
        if not (R / newp).exists():
            import os, tempfile
            live = Path(os.environ.get("TMP", tempfile.gettempdir())) / "emu" / f"{rid}_live.html"
            (R / newp).write_bytes(live.read_bytes())
        h = (R / newp).read_text(encoding="utf-8", errors="replace")
        assert "공공누리" in h and "제 1유형" in h.replace("제1유형", "제 1유형"), rid
        d["proof"] = newp
    d["notes"] = n; d["checked_at"] = D; w(f, d)

p = R / "02_SEASONS/S01/EP01" / REP; s = p.read_text(encoding="utf-8")
if "## 8. 크기 실측" not in s:
    s += ("\n## 8. 크기 실측 (2026-09-13, 봇 직접)\n\n"
          "e뮤지엄 상세 페이지를 쿠키와 함께 받아 페이지가 내주는 이미지를 직접 재고, 페이지 스크립트 `fnChangeMainImg(번호, 가로, 세로)` 에 적힌 원본 크기도 읽었다.\n\n"
          "| 기록 | 표시 이미지 (실측) | 페이지에 적힌 원본 크기 | 1080p 전체 화면 |\n|---|---|---|---|\n"
          "| 유리잔 경주2386 | 3000×2243~2475 (5장) | 8662×7148 ~ 11605×8706 | 가능 |\n"
          "| 말다래 경주2309 | 3000×1933 | 5454×3516 | 가능 |\n"
          "| 가슴걸이 경주2379 | 2000×3000 (세로) | 2000×3000 | 가능 (세로 사진 → 이동/부분 확대) |\n"
          "| 금제 관모 경주2275 | 3000×2000 | 3000×2000 | 가능 |\n\n"
          "- 가슴걸이·금제 관모도 출처를 e뮤지엄으로 교체 (1유형·번호 일치는 7절에서 확인). 기존 GNM 페이지 증빙은 천마총 출토 교차 확인용으로 보관.\n"
          "- 남은 일: 편집 전 브라우저 '이미지 다운로드' 로 받은 실제 파일 크기 기록 (원본 크기 파일이 나오는지).\n")
    p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
s = s.replace("가슴걸이·금제 관모 e뮤지엄 이미지 크기는 편집 전 확인.", "가슴걸이 2000×3000·금제 관모 3000×2000 실측 → 4건 모두 1080p 가능.")
if "크기 실측" not in s.split("## 최근 변경")[1][:900]:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — 권리 이미지 크기 실측: 유리잔 3000px (원본 최대 11605px) · 말다래 3000×1933 (원본 5454×3516) · 가슴걸이 2000×3000 · 금제 관모 3000×2000 → 4건 모두 1080p 전체 화면 가능. 가슴걸이·금제 관모 출처도 e뮤지엄으로.\n", 1)
p.write_text(s, encoding="utf-8")
print("sizes recorded")
