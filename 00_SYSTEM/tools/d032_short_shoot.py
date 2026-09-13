# -*- coding: utf-8 -*-
"""D-032: owner chose the short shoot next week (REAL_SHOT_ALTERNATIVES option B). Records the decision and points status to the TODO list.
No generation. Idempotent.  Usage: python 00_SYSTEM/tools/d032_short_shoot.py
"""
from pathlib import Path
R = Path(__file__).resolve().parents[2]
TODO = "02_SEASONS/S01/EP01/08_REAL_FOOTAGE/SHOOT_TODO_EP01_20260913.md"
assert (R / TODO).exists()

p = R / "00_SYSTEM/DECISIONS.md"; t = p.read_text(encoding="utf-8")
if "### D-032" not in t:
    anchor = "H06 총 3 호출 / 6 credits, 추가 호출 없음.\n"
    assert t.count(anchor) == 1
    t = t.replace(anchor, anchor + "\n### D-032 · 2026-09-13 · 경주 짧은 촬영 (사용자 \"1번 경주 방문 관련 2번으로 다음주에 가서 찍어서 올테니\")\n"
        "**결정** `15_QA/REAL_SHOT_ALTERNATIVES_20260913.md` §5 안 B — 다음 주 짧은 촬영. **꼭 찍기 5컷**: S01_SH001 · S01_SH002 · S09_SH003 · S08_SH003 (매치컷 착지) · S08_SH001. "
        "**시간 남으면 5컷**: S02_SH001 · S03_SH001 · S06_SH007 · S06_SH011 · S09_SH004 (못 찍으면 인터넷 사진 후보로 대체).\n"
        "**유지** H07 은 촬영 뒤 생성 (D-018 순서 그대로). CC BY-SA 사용 여부 · 포토코리아 확인은 대체가 필요할 때만 결정.\n"
        f"**TODO** `{TODO}` (촬영 허가 문의 Q1–Q5 · 날짜·예비일 · 촬영자 · 원본 보관은 사용자).\n", 1)
    p.write_text(t, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; t = p.read_text(encoding="utf-8")
old = "준비 점검 `15_QA/SHOOT_READINESS_20260913.md` (촬영 허가 Q1–Q5 · 사용자 결정 D1–D7 대기). "
if old in t:
    t = t.replace(old, f"준비 점검 `15_QA/SHOOT_READINESS_20260913.md`. **D-032: 다음 주 짧은 촬영 (꼭 찍기 5컷), TODO `{TODO}`.** ")
if "D-032" not in t.split("## 최근 변경")[1][:600]:
    t = t.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-032.** 경주 짧은 촬영 (다음 주): 꼭 찍기 5컷 (거리 · 오프닝 드러남 · 엔딩 같은 자리 · 천마총 매치컷 · 몽타주), 나머지 5컷은 시간 남으면. TODO `08_REAL_FOOTAGE/SHOOT_TODO_EP01_20260913.md`.\n", 1)
p.write_text(t, encoding="utf-8")
print("D-032 recorded")
