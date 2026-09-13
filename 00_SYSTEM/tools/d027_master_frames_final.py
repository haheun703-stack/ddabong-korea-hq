# -*- coding: utf-8 -*-
"""D-027 (2026-09-13): EP01 master frames final approved (S04 V05, S06 OPEN_CHAMBER V02, S06 MOUND_BUILDING V01);
crowd reference-image rule added to CHARACTER_CONTINUITY_STANDARD; approval APR_EP01_MF_001 closed at 8/10.
Usage:  python 00_SYSTEM/tools/d027_master_frames_final.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

f = EP / "07_SHOTS/master_frame_EP01_S04_MASTER_V01.json"; d = rd(f)
assert d["generation_id"] == "GEN_MF_EP01_S04_MASTER_HIGGSFIELD_V05"
d["status"] = "APPROVED"; d["approved_by"] = "사용자"; d["approved_at"] = D; d["updated_at"] = D; w(f, d)
for fr in ("EP01_S06_MASTER_OPEN_CHAMBER_V01", "EP01_S06_MASTER_MOUND_BUILDING_V01"):
    assert rd(EP / f"07_SHOTS/master_frame_{fr}.json")["status"] == "APPROVED", fr

f = C / "approval_APR_EP01_MF_001.json"; a = rd(f)
if "D-027" not in a["note"]:
    a["note"] += " D-027: 8 호출 / 16 credits 로 종료, 남은 2 호출은 버퍼로 미사용 (새 호출은 새 승인 필요)."
w(f, a)

r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## 최종 확정 (D-027)" not in s:
    s += ("\n## 최종 확정 (D-027, 2026-09-13)\n\n| 기준 그림 | 최종본 | 파생 AI 샷 |\n|---|---|---|\n"
          "| `EP01_S04_MASTER_V01` | V05 `MF_EP01_S04_MASTER_V05_c4ceb494.png` | H01 · H02 · H02b |\n"
          "| `EP01_S06_MASTER_OPEN_CHAMBER_V01` | V02 `MF_EP01_S06_MASTER_OPEN_CHAMBER_V02_de2b6a3e.png` | H04 |\n"
          "| `EP01_S06_MASTER_MOUND_BUILDING_V01` | V01 `MF_EP01_S06_MASTER_MOUND_BUILDING_V01_8e1007b7.png` | H05 · H06 |\n\n"
          "남은 메모 (허용): S04 뒤쪽 쇠처럼 보이는 삽 2자루 · 지평선 작은 흰 점; S06-A 궤 위치·경첩 (T자 배치는 G13). 8 호출 16 credits, 2 호출 미사용.\n")
r.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/standards/CHARACTER_CONTINUITY_STANDARD.md"; s = p.read_text(encoding="utf-8")
if "D-027" not in s:
    s = s.rstrip("\n") + ("\n\n## 군중 장면의 참고 그림 (D-027)\n"
        "군중(LITE_CROWD) 장면에 참고 이미지를 강하게 넣으면 그 얼굴이 군중 전체에 복제된다 (EP01 S04 V03·V04, 군중 2단계에서 확인).\n"
        "- 군중의 복식·분위기는 **문장 설명 중심**으로 지정한다 (얼굴 다양성: 나이·수염·체격·머리 형태를 명시, 'no cloned faces').\n"
        "- 참고 이미지는 **반복 인물 continuity 가 필요한 경우**(FULL Pack 인물, 예: 원로)에만 제한적으로 쓰고, 이미지마다 역할(얼굴/복식)을 문장에 지정한다.\n"
        "- 군중이 옷만 맞추면 되는 경우 참고 이미지는 쓰지 않거나, 쓰더라도 결과의 얼굴 반복을 검수 항목에 넣는다.\n")
    p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8"); anchor = "\n---\n\n## 승인 대기 (P)"
if "### D-027" not in s:
    s = s.replace(anchor, """
### D-027 · 2026-09-13 · EP01 Master Frames 최종 확정 · 군중 참고 그림 규칙 (사용자)
**확정** `EP01_S04_MASTER_V01` = V05 (참고 그림 없이 새로 생성, 군중 얼굴 복제 해소) · `EP01_S06_MASTER_OPEN_CHAMBER_V01` = V02 (관 형태·원로 허리띠 수정) · `EP01_S06_MASTER_MOUND_BUILDING_V01` = V01. 전부 APPROVED.
**근거** V05 는 복제 느낌·시대 위반(전봇대·건물·줄자·검은 띠)·공사 단계를 해결. 남은 미세 요소(뒤쪽 쇠처럼 보이는 삽 2자루, 지평선 흰 점)는 와이드 장면에서 영향 작음 → 추가 재생성은 새 문제 위험이 더 큼 (Change Only What Failed · Generate Late).
**비용** 기준 그림 8 호출 / 16 credits, `APR_EP01_MF_001` 한도 10 중 2 호출은 버퍼로 미사용하고 종료. EP01 누적 60.12 credits.
**운영 규칙** 군중 장면에 참고 이미지를 강하게 넣으면 얼굴 복제 위험 → 군중 복식·분위기는 문장 설명 중심, 참고 이미지는 반복 인물 continuity 가 필요한 경우에만 제한적으로 (CHARACTER_CONTINUITY_STANDARD §군중 장면의 참고 그림).
**다음** AI 샷 8개 생성 방법·비용 관리안 정리 (사용자 요청).
""" + anchor, 1)
p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
s = s.replace("`_S06_MASTER_OPEN_CHAMBER_V01` · `_S06_MASTER_MOUND_BUILDING_V01` (D-026 분리, path 없음, 승인 전)",
              "`_S06_MASTER_OPEN_CHAMBER_V01` · `_S06_MASTER_MOUND_BUILDING_V01` — **3장 APPROVED (D-027)**")
if "D-027." not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-027.** 기준 그림 3장 최종 확정 (S04 V05 · S06 OPEN_CHAMBER V02 · S06 MOUND_BUILDING V01). 군중 참고 그림 규칙 추가. 기준 그림 16 credits (2 호출 버퍼 미사용), EP01 누적 60.12 credits. 다음: AI 샷 8개 생성 방법·비용 관리안.\n", 1)
p.write_text(s, encoding="utf-8")
print("D-027 recorded")
