# -*- coding: utf-8 -*-
"""Apply D-015 (user decisions A-F on P2 pre-flight). No paid generation."""
import json, glob, re, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- A: locks -> APPROVED ; B: elite costume lock text ----
OLD_ELITE = rd("06_PROMPT_LIBRARY/locks/COSTUME_SILLA_ELITE_A01_LOCK.json")["text"]
NEW_ELITE = (OLD_ELITE
    .replace("(PROBABLE; colour and belt INTERPRETIVE)", "(PROBABLE; colour and belt fixed by D-015)")
    .replace("restrained silver or bronze", "restrained bronze")
    .replace("muted crimson or blue tones, never purple", "muted blue tones, never crimson, never purple")
    .replace("Forbidden: gold crown, Joseon royal or official robes, Ming/Qing imperial dress, fantasy king styling, purple.",
             "Forbidden: gold crown, silver or gold belt plaques, Joseon royal or official robes, Ming/Qing imperial dress, fantasy king styling, purple, crimson."))
assert NEW_ELITE != OLD_ELITE and "muted blue" in NEW_ELITE and "restrained bronze" in NEW_ELITE
for f in glob.glob(str(R / "06_PROMPT_LIBRARY/locks/CHAR_*_LOCK.json")) + glob.glob(str(R / "06_PROMPT_LIBRARY/locks/COSTUME_*_LOCK.json")):
    f = Path(f).relative_to(R); d = rd(f); d["status"] = "APPROVED"; d["updated_at"] = D
    if d["lock_id"] == "COSTUME_SILLA_ELITE_A01_LOCK": d["text"] = NEW_ELITE; d["source"] += " · D-015 colour/belt"
    w(f, d)
c = rd("05_HISTORY_DATABASE/costumes/COSTUME_SILLA_ELITE_A01.json"); e = c["elements"]
e["belt"] = "과대 — 금속 장식 띠 + 요패. 천마총 금제 허리띠 복제 금지(피장자 부장품) → 절제된 동(bronze) 계열로 확정 (D-015, 사용자) — PROBABLE (CLM_004, CLM_008). 은·금 판 금지"
e["color"] = "청(muted blue) 계열로 확정 (D-015, 사용자). 자색(최고위)·비(다홍) 회피. 관등 공복색 위계 참고 — PROBABLE 유지 (CLM_002; 5세기 적용 여부 불확실, hedge 유지)"
e["forbidden"] = "금관, 은·금 과대 판, 조선 곤룡포/관복, 명·청 황실 예복, 판타지 왕 연출, 자색, 다홍"
e["qa_note"] = "D-011 근거 확정 2026-09-11. D-015 (2026-09-11, 사용자): 옷 색 muted blue · 과대 bronze 확정, historical_basis 는 PROBABLE 유지 (P-009 종결)."
c["updated_at"] = D; w("05_HISTORY_DATABASE/costumes/COSTUME_SILLA_ELITE_A01.json", c)
n = 0
for f in glob.glob(str(R / "02_SEASONS/S01/EP01/1[12]_AI_*/prompt_*.json")):
    f = Path(f).relative_to(R); d = rd(f)
    if OLD_ELITE in d["assembled_text"]:
        d["assembled_text"] = d["assembled_text"].replace(OLD_ELITE, NEW_ELITE); w(f, d); n += 1
print("re-assembled prompts:", n)

# ---- C, D notes ----
ch = rd("05_HISTORY_DATABASE/characters/CHAR_SILLA_ELITE_OBSERVER_01.json")
ch["notes"] += " D-015: back_view 는 정식 슬롯이 아닌 FULL Pack 보조 레퍼런스 이미지 (스키마 미확장, P-005 종결). 생성 순서: 배치 1 = hero·front·three_quarter_left·full_body 4장 → 사람 검수 → 나머지 6 + back_view."
ch["updated_at"] = D; w("05_HISTORY_DATABASE/characters/CHAR_SILLA_ELITE_OBSERVER_01.json", ch)
for cid in ["CHAR_SILLA_LABORER_GROUP_01", "CHAR_SILLA_ATTENDANT_GROUP_01"]:
    ch = rd(f"05_HISTORY_DATABASE/characters/{cid}.json")
    ch["notes"] += " D-015: LITE_CROWD 유지 확인 (사용자). H02 푸시인이 특정 얼굴에 머물 때만 FULL 승격 검토."
    ch["updated_at"] = D; w(f"05_HISTORY_DATABASE/characters/{cid}.json", ch)

# ---- F: Money Gate OPEN ----
ep = rd("02_SEASONS/S01/EP01/episode.json")
ep["budget"] = {"currency": "KRW", "amount": 40000, "spent": 0, "note": "D-015 (2026-09-11, 사용자): EP01 AI 생성 예산 ₩40,000. Money Gate OPEN."}
w("02_SEASONS/S01/EP01/episode.json", ep)
w("08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json", {
    "cost_id": "COST_EP01_20260911", "episode_id": "EP01",
    "budget": {"currency": "KRW", "amount": 40000, "spent": 0, "note": "D-015 사용자 확정"},
    "spent_total": 0, "spent_by_provider": {}, "percent_used": 0, "gate_state": "OPEN", "generation_ids": [], "as_of": D,
    "note": "P-001 종결. 유료 호출마다 generation.json 추가 후 spent_total/percent_used 갱신. 80% WARNING · 95% STRONG · 100% LOCKED."})
w("08_GENERATION_CACHE/EP01/approval_APR_EP01_MP_ELITE_BATCH1_001.json", {
    "approval_id": "APR_EP01_MP_ELITE_BATCH1_001", "kind": "PAID_GENERATION", "target_id": "CHAR_SILLA_ELITE_OBSERVER_01",
    "money_gate_presented": {
        "shot_id": "MASTER_PACK:CHAR_SILLA_ELITE_OBSERVER_01:batch1",
        "prompt_ids": ["PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_HERO_V01", "PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_FRONT_V01",
                       "PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_THREE_QUARTER_LEFT_V01", "PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_FULL_BODY_V01"],
        "provider_model": "Higgsfield / image model TBD at run", "expected_attempts": "4 images x up to 2 attempts",
        "estimated_cost_range": "미확인 (첫 파일럿, 실제 비용 데이터 수집)", "continuity_risk": "HIGH - 첫 얼굴·체형·복식 lock"},
    "decision": "APPROVE", "fix_reason": None, "decided_by": "사용자", "decided_at": D + "T00:00:00Z",
    "note": "D-015. 소규모 배치 1 (4장) 승인. 사람 검수 통과 후 나머지 6 + back_view 는 별도 approval."})

# ---- validator: register cache instances ----
v = R / "00_SYSTEM/schemas/validate.py"; s = v.read_text(encoding="utf-8")
old = '            sorted(ROOT.glob("02_SEASONS/*/*/1[12]_AI_*/prompt_*.json"))\n'
new = ('            sorted(ROOT.glob("02_SEASONS/*/*/1[12]_AI_*/prompt_*.json")) + \\\n'
       '            sorted(ROOT.glob("08_GENERATION_CACHE/*/cost_*.json")) + sorted(ROOT.glob("08_GENERATION_CACHE/*/approval_*.json")) + \\\n'
       '            sorted(ROOT.glob("08_GENERATION_CACHE/*/generation_*.json"))\n')
assert old in s; v.write_text(s.replace(old, new, 1), encoding="utf-8")

# ---- DECISIONS.md ----
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8")
d15 = """### D-015 · 2026-09-11 · P2 사전 점검 승인 A–F · Money Gate OPEN · Master Pack 소규모 배치 (사용자)
**승인 내용** `15_QA/P2_PREFLIGHT_REPORT.md` 항목 A–F. **A** Character lock 3 + Costume lock 3 → APPROVED. **B** (P-009 종결) 원로 옷 색 muted blue · 금속 포인트 restrained bronze, `historical_basis` 는 PROBABLE 유지. **C** 노동자·시종 2그룹 LITE_CROWD 유지, H02 푸시인이 특정 얼굴에 머물 때만 FULL 승격 검토. **D** (P-005 종결) back_view 는 정식 슬롯 추가 없이 FULL Pack 보조 레퍼런스 이미지로 취급, 스키마 미확장. **E** (P-011 보류) 라우터 49건 ACCEPT/OVERRIDE 는 AI 샷 생성 직전 최종 승인. **F** (P-001 종결) EP01 AI 생성 예산 **₩40,000**, Money Gate OPEN.
**생성 원칙** 17장 일괄 생성 금지. 배치 1 = 원로 hero · front · three_quarter_left · full_body 4장 → 사람 검수(얼굴·체형·복식 lock 확인) → 나머지 6 + back_view → 군중 6. Generate Late + Change Only What Failed.
**반영** locks 6 APPROVED · `COSTUME_SILLA_ELITE_A01` color/belt/forbidden · 프롬프트 13 재조립 (원로 MP 11 + S06_SH002 · SH005; 생성 전이라 V01 유지) · `episode.json.budget` · `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` OPEN · `approval_APR_EP01_MP_ELITE_BATCH1_001.json` APPROVE · validate.py 가 cost/approval/generation 인스턴스 검증.

---

## 승인 대기 (P)
"""
marker = "\n---\n\n## 승인 대기 (P)\n"
assert marker in s; s = s.replace(marker, "\n---\n\n" + d15, 1)
for pid in ["P-001", "P-005", "P-009"]:
    s = re.sub(rf"^### {pid} · ", f"### ~~{pid}~~ · (종결 D-015) ", s, count=1, flags=re.M)
s = re.sub(r"^### P-011 · ", "### P-011 · (보류 D-015: AI 샷 직전 승인) ", s, count=1, flags=re.M)
p.write_text(s, encoding="utf-8")

# ---- CURRENT_STATUS.md ----
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
reps = [
 ("- P-001 EP01 생성 예산 금액 (Money Gate 기준값) — 미확인이면 유료 생성 게이트는 `UNKNOWN_BUDGET` 으로 잠김.\n", "- ~~P-001~~ EP01 예산 **₩40,000 확정 (D-015)** → Money Gate OPEN.\n"),
 ("- **P-009** 원로(`CHAR_SILLA_ELITE_OBSERVER_01`) 옷 색 비(다홍) vs 청 · 과대 재질 — 관등 미설정이라 INTERPRETIVE (NEW).\n", "- ~~P-009~~ 원로 옷 색 muted blue · 과대 bronze 확정 (D-015), PROBABLE 유지.\n"),
 ("- **P-011** 라우터 판정 49건 ACCEPT / OVERRIDE (핵심: H05 BLENDER_FLOW vs Higgsfield).\n", "- **P-011** 라우터 판정 49건 ACCEPT / OVERRIDE — **AI 샷 생성 직전 최종 승인으로 보류 (D-015)**.\n"),
 ("**유료 생성 시작 조건 (모두 충족해야)**: P-001 예산 확정 → `cost.json` OPEN · P-011 라우터 ACCEPT · Master Pack 생성 → `CHARACTER_MASTER_APPROVED` · master_frame APPROVED.",
  "**유료 생성 현황 (D-015)**: Money Gate OPEN (₩40,000 / 소진 0). **지금 가능**: 원로 Master Pack 배치 1 (hero · front · three_quarter_left · full_body 4장, `approval_APR_EP01_MP_ELITE_BATCH1_001` APPROVE) → 사람 검수 → 나머지 6 + back_view → 군중 6. AI 샷은 P-011 ACCEPT + `CHARACTER_MASTER_APPROVED` + master_frame APPROVED 뒤."),
 ("| 승인 대기 | A lock 승인 · B P-009 · C 군중 등급 확인 · D P-005 back_view · E P-011 · **F P-001 예산 (전면 차단)** |", "| 승인 | **D-015**: A✔ lock 6 APPROVED · B✔ muted blue + bronze · C✔ LITE 유지 · D✔ back_view 보조 · E 보류(AI 샷 직전) · F✔ ₩40,000 OPEN |"),
 ("| EP01 예산 | **미확인** (P-001) |\n| 소진 | 미확인 |\n| 게이트 상태 | `UNKNOWN_BUDGET` → 유료 생성 잠금 |", "| EP01 예산 | **₩40,000** (D-015) — `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` |\n| 소진 | ₩0 (0%) |\n| 게이트 상태 | `OPEN` — 배치 1 승인 `APR_EP01_MP_ELITE_BATCH1_001` |"),
 ("- 예산 미확인 → 유료 생성 전면 잠금 (규칙 위반 아님, 정상 상태).\n", "- ~~예산 미확인~~ → D-015 ₩40,000 OPEN. 배치 1 생성은 Higgsfield 연결(MCP 인증) 필요.\n"),
 ("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-11 사용자** — **D-015.** P2 사전 점검 A–F 승인: lock 6 APPROVED, 원로 muted blue + bronze (PROBABLE 유지), LITE_CROWD 유지, back_view 보조 이미지, P-011 은 AI 샷 직전, **예산 ₩40,000 Money Gate OPEN**. Master Pack 은 원로 4장 배치부터.\n- **2026-09-11 Claude Code** — D-015 반영: 복식 lock·인스턴스 갱신, 프롬프트 13 재조립, cost/approval 인스턴스, 검증기 캐시 등록, 배치 1 브리프 `11_AI_STILLS/MP_BATCH1_BRIEF.md`.\n"),
 ("(Claude Code, P2 pre-flight)", "(Claude Code, D-015 반영)"),
]
for a, b in reps:
    if a not in s: print("WARN status marker missing:", a[:50])
    s = s.replace(a, b, 1)
p.write_text(s, encoding="utf-8")

# ---- Batch 1 brief ----
rows = []
for slot in ["HERO", "FRONT", "THREE_QUARTER_LEFT", "FULL_BODY"]:
    d = rd(f"02_SEASONS/S01/EP01/11_AI_STILLS/prompt_PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_{slot}_V01.json")
    rows.append(f"## {slot.lower()} — `{d['prompt_id']}`\n\n**shot_delta**: {d['shot_delta']}\n\n**assembled_text**\n\n```\n{d['assembled_text']}\n```\n\n**negative**\n\n```\n{', '.join(d['negative'])}\n```\n")
(R / "02_SEASONS/S01/EP01/11_AI_STILLS/MP_BATCH1_BRIEF.md").write_text(
    "# Master Pack 배치 1 — 원로 4장 (D-015)\n\n"
    "> 승인 `APR_EP01_MP_ELITE_BATCH1_001` · Money Gate OPEN (₩40,000, 소진 0) · 대상 `CHAR_SILLA_ELITE_OBSERVER_01` (FULL)\n"
    "> 실행 규칙: 1장씩 생성 → `08_GENERATION_CACHE/EP01/generation_GEN_MP_ELITE_<slot>_HIGGSFIELD_V01.json` 기록 → `cost.json` spent 갱신. 실패 시 전체 재작성 금지, `keep_change_patch` 로 실패 항목만 변경.\n"
    "> 검수 기준: 얼굴 ID 고정(4장 동일 인물) · 체형/키 비율 · 복식 = muted blue 표의 + bronze 과대 + 자작나무 계열 관모 · 금관/은·금 과대/자색/다홍 없음 · 스타일 B (광택 없음, 절제된 표정).\n"
    "> **아직 생성 0.** Higgsfield MCP 인증 후 실행.\n\n" + "\n".join(rows), encoding="utf-8")
print("done")
