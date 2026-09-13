# -*- coding: utf-8 -*-
"""Resolve YELLOW_ACTIVE RTS_GNM_OTHER_OBJECTS_001 (D-014) using the 2026-09-13 page check (15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md):
split into GREEN KOGL Type 1 records for objects the shots actually use; OTHER_OBJECTS -> BACKUP_ONLY (earrings/pottery unchecked, stays YELLOW).
S02_SH003 '말다래' = the Cheonmado painting (already RTS_WIKI_CHEONMADO_001 on that shot) -> no separate mudguard record.
Usage:  python 00_SYSTEM/tools/rights_gnm_split_20260913.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; RT = R / "05_HISTORY_DATABASE/rights"; SH = R / "02_SEASONS/S01/EP01/07_SHOTS"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
BY = "Claude Code (Rights check agent, D-029)"
QUOTE = "국립경주박물관이 창작한 저작권 보호분야 {name} 저작물은 \"공공누리\" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)"
NEW = [
 ("RTS_GNM_CHEST_ORNAMENT_001", "ASSET_GNM_CHEONMACHONG_CHEST_ORNAMENT_V01", "https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=53&mode=V",
  "Source: Gyeongju National Museum, Chest ornament from Cheonmachong (Gyeongju 2379), KOGL Type 1.", "가슴걸이", "원본이미지 다운로드 있음."),
 ("RTS_GNM_GOLD_CAP_001", "ASSET_GNM_CHEONMACHONG_GOLD_CAP_V01", "https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=58&mode=V",
  "Source: Gyeongju National Museum, Gold cap from Cheonmachong (Gyeongju 2275), KOGL Type 1.", "금제 관모", "원본이미지 다운로드 있음 (2장)."),
 ("RTS_GNM_GLASS_CUP_001", "ASSET_GNM_CHEONMACHONG_GLASS_CUP_V01", "https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=172&mng_no=256&mode=V",
  "Source: Gyeongju National Museum, Glass cup from Cheonmachong (Treasure No. 620), KOGL Type 1.", "유리잔", "전시 해설 페이지: 원본 다운로드 버튼 없음, 표시 이미지만 → 편집 전 해상도 확인. 부족하면 소장품 DB/e뮤지엄 원본 페이지를 찾아 그 라벨을 다시 확인."),
]
for rid, aid, src, credit, name, extra in NEW:
    w(RT / f"{rid}.json", {"rights_id": rid, "asset_id": aid, "source": src, "creator": "국립경주박물관", "license": "KOGL Type 1",
        "commercial_use": "YES", "modification_allowed": "YES", "attribution_required": "YES", "attribution_text": credit,
        "expiration": None, "proof": None, "research_permission": "YES", "media_reuse_permission": "YES", "status": "GREEN",
        "checked_at": D, "checked_by": BY,
        "notes": f"RTS_GNM_OTHER_OBJECTS_001 에서 분리 (2026-09-13 페이지 원문 확인). 페이지 문구: '{QUOTE.format(name=name)}'. {extra} proof 캡처 미보관 (편집 전 저장). 15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md.",
        "usage_tier": "ACTIVE"})

SWAP = {"EP01_S02_SH003": ["RTS_GNM_GLASS_CUP_001"], "EP01_S05_SH001": ["RTS_GNM_GOLD_CAP_001", "RTS_GNM_CHEST_ORNAMENT_001"]}
for sid, new_ids in SWAP.items():
    f = SH / f"shot_{sid}.json"; d = rd(f)
    ids = [x for x in d["rights_ids"] if x != "RTS_GNM_OTHER_OBJECTS_001"]
    for x in new_ids:
        if x not in ids: ids.append(x)
    d["rights_ids"] = ids; d["updated_at"] = D
    if "RIGHTS_CHECK_GNM_OTHER_OBJECTS" not in d["notes"]:
        extra = ""  # superseded by fix_codex_review_20260913.py (mudguard = gilt-bronze, RTS_GNM_MUDGUARD_001)
        d["notes"] += f" 권리 해소 2026-09-13: RTS_GNM_OTHER_OBJECTS_001 (YELLOW) → {', '.join(new_ids)} (GREEN, 공공누리 1유형, 15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md).{extra}"
    w(f, d)

f = RT / "RTS_GNM_OTHER_OBJECTS_001.json"; d = rd(f)
for sid in SWAP:
    assert "RTS_GNM_OTHER_OBJECTS_001" not in rd(SH / f"shot_{sid}.json")["rights_ids"]
d["usage_tier"] = "BACKUP_ONLY"; d["checked_at"] = D
if "2026-09-13" not in d["notes"]:
    d["notes"] += " 2026-09-13: 가슴걸이·금제 관모·유리잔은 1유형 확인 → RTS_GNM_CHEST_ORNAMENT_001 · RTS_GNM_GOLD_CAP_001 · RTS_GNM_GLASS_CUP_001 로 분리, 두 샷 연결 교체. 천마무늬 말다래(경주2309)·유리구슬 목걸이(경주2381)도 1유형 확인했으나 미사용. 귀걸이·토기는 페이지 미확인 → YELLOW 유지, BACKUP_ONLY."
w(f, d)

p = R / "02_SEASONS/S01/EP01/15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md"; s = p.read_text(encoding="utf-8")
if "## 반영 (2026-09-13)" not in s:
    s += ("\n## 반영 (2026-09-13)\n\n- 확인 필요 A 해소: S02_SH003 몽타주의 '말다래'는 **천마도 그림** — 이 샷에 이미 `RTS_WIKI_CHEONMADO_001` 이 연결돼 있음 → 금동 말다래 기록 만들지 않음.\n"
          "- 생성: `RTS_GNM_CHEST_ORNAMENT_001` · `RTS_GNM_GOLD_CAP_001` · `RTS_GNM_GLASS_CUP_001` (GREEN, ACTIVE).\n"
          "- 샷 교체: S02_SH003 → GLASS_CUP · S05_SH001 → GOLD_CAP + CHEST_ORNAMENT. `RTS_GNM_OTHER_OBJECTS_001` → BACKUP_ONLY (YELLOW 유지).\n"
          "- 남은 일: 유리잔 표시 이미지 해상도 확인 (확인 필요 B), 모든 GREEN 기록 proof 캡처 보관.\n")
p.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
s = s.replace("- YELLOW_ACTIVE 1건 (`RTS_GNM_OTHER_OBJECTS_001`) — 편집 확정 전 필수 해소 (D-014).",
              "- ~~YELLOW_ACTIVE 1건~~ **해소 (2026-09-13)**: `RTS_GNM_OTHER_OBJECTS_001` → 유리잔·금제 관모·가슴걸이 GREEN 1유형 분리, 원본은 BACKUP_ONLY. 남은 일: 유리잔 해상도 확인, GREEN proof 캡처.")
s = s.replace("| DONE (P3) · YELLOW_ACTIVE 1건 편집 전 해소 |", "| DONE (P3) · YELLOW_ACTIVE 해소 (2026-09-13) |")
if "YELLOW_ACTIVE 해소" not in s.split("## 최근 변경")[1][:600]:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code (D-029 에이전트)** — 권리 조사: 국립경주박물관 페이지 원문 확인 → 가슴걸이·금제 관모·유리잔 공공누리 1유형 → GREEN 3건 생성, S02_SH003·S05_SH001 연결 교체, OTHER_OBJECTS BACKUP_ONLY. **YELLOW_ACTIVE 해소.** 데이터 정리: H05 라벨 2개 · S03_SH002 권리 메모 · G04 자갈 사실 연결.\n", 1)
p.write_text(s, encoding="utf-8")
print("rights split applied")
