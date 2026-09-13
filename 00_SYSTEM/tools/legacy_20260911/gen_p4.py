# -*- coding: utf-8 -*-
"""P4 Shot Router: rights usage_tier (D-014), router schema extension, 49 router decisions, report."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"; BY = "Visual Router (Claude Code)"
SH = R / "02_SEASONS/S01/EP01/07_SHOTS"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): p = R / p; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def insert_after(props, after, key, val):
    out = {}
    for k, v in props.items():
        out[k] = v
        if k == after: out[key] = val
    return out

# 1. rights schema: usage_tier
p = "00_SYSTEM/schemas/rights.schema.json"; s = rd(R / p)
if "usage_tier" not in s["properties"]:
    s["properties"] = insert_after(s["properties"], "status", "usage_tier", {"type": "string", "enum": ["ACTIVE", "BACKUP_ONLY"],
      "description": "D-014. ACTIVE = 실제 샷에 연결됨 (YELLOW 이면 편집 전 해결 필수 = YELLOW_ACTIVE). BACKUP_ONLY = 대체 가능, 실제 사용 시에만 해결 (YELLOW_BACKUP). BACKUP_ONLY 자산을 샷이 참조하면 FAIL."})
    w(p, s)
for rid, tier in {"RTS_GNM_OTHER_OBJECTS_001": "ACTIVE", "RTS_GYEONGJU_CITY_IMAGE_001": "BACKUP_ONLY", "RTS_WIKI_DAEREUNGWON_001": "BACKUP_ONLY", "RTS_WIKI_CHEONMACHONG_ENTRANCE_001": "BACKUP_ONLY",
                  "RTS_WIKI_GOLD_CROWN_002": "BACKUP_ONLY", "RTS_NRICH_1973_PHOTOS_001": "ACTIVE", "RTS_GNM_GOLD_CROWN_001": "ACTIVE", "RTS_GNM_GOLD_GIRDLE_001": "ACTIVE", "RTS_WIKI_CHEONMADO_001": "ACTIVE"}.items():
    pp = f"05_HISTORY_DATABASE/rights/{rid}.json"; d = rd(R / pp); d["usage_tier"] = tier
    if rid == "RTS_GNM_OTHER_OBJECTS_001": d["notes"] += " D-014: YELLOW_ACTIVE — 편집 확정 전 필수 해소."
    w(pp, d)

# 2. router schema: scores / fallback / previous
p = "00_SYSTEM/schemas/router_decision.schema.json"; s = rd(R / p)
if "scores" not in s["properties"]:
    s["properties"] = insert_after(s["properties"], "recommended_pipeline", "fallback_pipeline", {"type": ["string", "null"], "enum": ["REAL_SHOOT", "ARCHIVE", "AI_STILL", "ORIGINAL_GRAPHIC", "BLENDER_FLOW", "HIGGSFIELD", None], "description": "1순위 실패 시 대체 파이프라인 (D-014)"})
    s["properties"] = insert_after(s["properties"], "fallback_pipeline", "previous_pipeline", {"type": ["string", "null"], "description": "라우팅 전 샷에 적혀 있던 파이프라인 (legacy 태그 추적)"})
    s["properties"] = insert_after(s["properties"], "rule_applied", "scores", {"type": "object", "additionalProperties": False,
      "properties": {k: {"type": "integer", "minimum": 0, "maximum": 100} for k in ("spatial_accuracy", "camera_complexity", "human_motion", "visual_importance")} |
                    {k: {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]} for k in ("continuity_importance", "historical_importance")},
      "required": ["spatial_accuracy", "camera_complexity", "human_motion", "continuity_importance", "historical_importance", "visual_importance"]})
    w(p, s)

# 3. routing
OBS = "CHAR_SILLA_ELITE_OBSERVER_01"
RULES = {
 "REAL": "Present-day location → REAL_SHOOT",
 "ARCH": "Historical photo/document/artifact → ARCHIVE",
 "GRAPH": "Low motion + high factual density → ORIGINAL_GRAPHIC",
 "STILL": "Low motion + high factual density (historical reconstruction) → AI_STILL",
 "BF_SPATIAL": "High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO",
 "BF_MOTION": "Human motion + natural movement (carrying, ritual preparation, looking) → FLOW/VEO (Blender previz for scale)",
 "HIGGS": "Strong reveal / extreme camera / past-to-present match cut → HIGGSFIELD",
}
# manual judgement for the 8 legacy Higgsfield shots (supervisor criteria, D-014)
AI = {
 "EP01_S04_SH004": ("BLENDER_FLOW", "HIGGSFIELD", "BF_MOTION", "H01 목재 준비: 노동 동작 중심(human_motion 70), 카메라는 느린 측면 트래킹. 공간 의존 중간(60). 자연스러운 손·몸 움직임이 핵심이라 Flow/Veo. Blender 는 작업장 스케일 previz 만."),
 "EP01_S04_SH005": ("BLENDER_FLOW", "HIGGSFIELD", "BF_SPATIAL", "H02 돌 운반: 봉분 일부 형성 상태의 공간 관계(70) + 와이드→손 푸시인(55) + 반복 운반 동작(75). 공간·카메라·동작 모두 → Blender 공간 lock 후 Flow/Veo."),
 "EP01_S04_SH006": ("BLENDER_FLOW", "AI_STILL", "BF_SPATIAL", "H02 조직된 작업 와이드: 공간 정확도 75, 정적 와이드. SH005 와 같은 Blender 씬에서 카메라만 바꿔 뽑는다 → 유료 호출 절감. 실패 시 Blender 키프레임 AI_STILL + 미세 모션."),
 "EP01_S05_SH005": ("BLENDER_FLOW", "AI_STILL", "BF_MOTION", "H03 부장품 준비: 손·천·금속 클로즈업, 얕은 심도. 공간 의존 낮음(50) 이라 Blender previz 생략 가능, 승인 키프레임 → Flow/Veo 직행. 4초라 AI_STILL + 켄번스로도 대체 가능."),
 "EP01_S06_SH002": ("BLENDER_FLOW", "HIGGSFIELD", "BF_SPATIAL", "H04 장례 준비 와이드: 역할별 배치(공간 80) + 반복 인물 원로 등장 → master_frame 필수, 인물 연속성 critical. 정적 와이드 + 전경 미세 움직임 → Blender 배치 lock → Flow/Veo reference-driven."),
 "EP01_S06_SH005": ("BLENDER_FLOW", "HIGGSFIELD", "BF_SPATIAL", "H05 관찰자 시점: 공간 85 + 카메라 60(관찰자 뒤 느린 전진) + 원로 뒷모습 연속성. 에피소드 핵심 컷(visual 100) 이라 공간·인물 lock 이 우선 → Blender → Flow/Veo. 극단 카메라가 아니므로 Higgsfield 는 fallback."),
 "EP01_S06_SH010": ("AI_STILL", "BLENDER_FLOW", "STILL", "H06 완성 봉분 와이드: 움직임 거의 없음(20), 정보량(스케일 47 m/12.7 m) 높음, 정적 와이드 → AI_STILL. Blender 로 봉분 스케일·소그룹 위치 lock 한 키프레임을 생성 기준으로. 미세 카메라 필요 시 BLENDER_FLOW."),
 "EP01_S08_SH002": ("HIGGSFIELD", "AI_STILL", "HIGGS", "H07 과거→현재 매치컷: 정본 §6 Higgsfield 용도(past-to-present match cut). 카메라 고정이지만 특수 전환 컷. 실사 착지 구도(SH003) 촬영 후 그 구도에 맞춰 생성. 정지 프레임이면 AI_STILL 로 충분."),
}
def route(d):
    sid = d["shot_id"]
    if sid in AI: return AI[sid]
    if d["pipeline"] == "REAL_SHOOT": return ("REAL_SHOOT", None, "REAL", "현재 장소 실사 (era PRESENT_DAY).")
    if d["pipeline"] == "ARCHIVE": return ("ARCHIVE", None, "ARCH", "공식 발굴사진·유물 이미지 (rights 연결 완료).")
    if d["pipeline"] == "ORIGINAL_GRAPHIC": return ("ORIGINAL_GRAPHIC", None, "GRAPH", "정보 밀도 높고 움직임 적음 → 자체 그래픽 (권리 BLUE).")
    raise RuntimeError(sid)
ATT = {"REAL_SHOOT": 1, "ARCHIVE": 1, "ORIGINAL_GRAPHIC": 2, "AI_STILL": 3, "BLENDER_FLOW": 3, "HIGGSFIELD": 3}
PROV = {"BLENDER_FLOW": ["Blender", "Flow", "Veo"], "HIGGSFIELD": ["Higgsfield"], "AI_STILL": ["Flow (image)", "Higgsfield (image)"]}
rows, changes = [], []
for p in sorted(SH.glob("shot_*.json")):
    d = rd(p); sid = d["shot_id"]
    rec, fb, rk, why = route(d)
    cont = "HIGH" if OBS in d["characters"] or sid in ("EP01_S08_SH002", "EP01_S08_SH003") else ("MEDIUM" if d["characters"] else "LOW")
    hist = {"PRIMARY": "HIGH", "SUPPORTING": "MEDIUM"}.get(d["evidence_role"], "LOW")
    risk = "HIGH" if cont == "HIGH" and rec in PROV else ("MEDIUM" if rec in PROV else "LOW")
    did = f"RTR_{sid}_V01"
    w(f"02_SEASONS/S01/EP01/07_SHOTS/router_decision_{did}.json", {
        "decision_id": did, "shot_id": sid, "recommended_pipeline": rec, "fallback_pipeline": fb, "previous_pipeline": d["pipeline"],
        "reason": why, "rule_applied": RULES[rk],
        "scores": {"spatial_accuracy": d["spatial_accuracy"], "camera_complexity": d["camera_complexity"], "human_motion": d["human_motion"],
                   "continuity_importance": cont, "historical_importance": hist, "visual_importance": d["visual_importance"]},
        "historical_confidence": d["historical_confidence"], "continuity_risk": risk,
        "expected_cost_range": {"currency": "CREDITS", "min": None, "max": None}, "expected_attempts": ATT[rec],
        "provider_candidates": PROV.get(rec, []), "human_decision": "PENDING", "override_note": None, "decided_at": D, "decided_by": BY})
    if d["pipeline"] != rec: changes.append((sid, d["pipeline"], rec))
    d["router_decision_id"] = did; d["pipeline"] = rec; d["status"] = "ROUTED"; d["updated_at"] = D; d["updated_by"] = BY
    w(f"02_SEASONS/S01/EP01/07_SHOTS/{p.name}", d)
    rows.append((sid, d["previous_pipeline"] if "previous_pipeline" in d else None, rec, fb, cont, hist, d["historical_confidence"], risk))

# 4. report
from collections import Counter
cnt = Counter(r[2] for r in rows)
L = ["# EP01 P4 Shot Router — 판정 리포트", "", f"> 생성 {D} · {BY} · 스크립트 출력 (재생성). 규칙: 정본 §6 §7 + 감독 기준 (D-014). `human_decision = PENDING` — 사용자 ACCEPT/OVERRIDE 대기.", "",
     "## 요약", "", f"- 49 샷 라우팅: " + " · ".join(f"{k} {v}" for k, v in sorted(cnt.items())),
     f"- 파이프라인 변경 {len(changes)}건 (legacy Higgsfield 8 → HIGGSFIELD 1 · BLENDER_FLOW 6 · AI_STILL 1)", "- 유료 생성 0 (라우팅은 판정만). Money Gate 여전히 UNKNOWN_BUDGET.", "",
     "## 재판정 — 역사 재현 8컷 (왜 Higgsfield 가 아닌가)", "", "| shot | 컷 | 이전 | 판정 | fallback | 규칙 | 이유 |", "|---|---|---|---|---|---|---|"]
NAMES = {"EP01_S04_SH004": "H01", "EP01_S04_SH005": "H02", "EP01_S04_SH006": "H02 wide", "EP01_S05_SH005": "H03", "EP01_S06_SH002": "H04", "EP01_S06_SH005": "H05", "EP01_S06_SH010": "H06", "EP01_S08_SH002": "H07"}
for sid, (rec, fb, rk, why) in AI.items():
    L.append(f"| `{sid}` | {NAMES[sid]} | HIGGSFIELD | **{rec}** | {fb} | {RULES[rk]} | {why} |")
L += ["", "## 전체 판정", "", "| shot | pipeline | fallback | continuity | historical | confidence | risk |", "|---|---|---|---|---|---|---|"]
L += [f"| {s} | {rec} | {fb or '—'} | {c} | {h} | {conf} | {risk} |" for s, _, rec, fb, c, h, conf, risk in rows]
L += ["", "## 권리 등급 (D-014)", "", "- GREEN → 사용 가능 · YELLOW_ACTIVE → 실제 샷 연결, 편집 전 해결 필수 · YELLOW_BACKUP → 대체 가능, 실제 사용 시에만 해결 · RED → 금지",
      "- **YELLOW_ACTIVE 1건**: `RTS_GNM_OTHER_OBJECTS_001` (EP01_S02_SH003, EP01_S05_SH001) — 박물관 소장품 페이지별 KOGL 유형 확인 후 GREEN 분리 또는 컷 제외.",
      "- YELLOW_BACKUP 3건: 경주시 이미지 · Wikimedia 대릉원 · Wikimedia 천마총 입구 (자체 촬영 확보 시 미사용).", "",
      "## 다음", "", "- 사용자: 라우터 판정 ACCEPT / OVERRIDE (특히 H05 — Higgsfield 유지 여부).", "- P2 Character Master (원로 FULL + 군중 LITE) → master_frame S04·S06 → 그 뒤에만 유료 생성.", "- Blender 브리지(P7) 전까지 `camera.json` 은 수동."]
(R / "02_SEASONS/S01/EP01/15_QA/P4_ROUTER_REPORT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(dict(cnt), "changes", changes)
