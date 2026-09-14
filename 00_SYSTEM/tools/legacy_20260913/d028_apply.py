# -*- coding: utf-8 -*-
"""D-028 (2026-09-13): D1 A (Higgsfield = provider, Kling 3.0 = model), D-024 meaning clarified, logical pipeline separated from provider/model,
D3 Blender-less BLENDER_I2V with STOP after 2 spatial failures, D4 H06 still approved (max 2 calls / 4 credits), P-012 still open.
Saves H06 sent-form prompt V02 BEFORE sending (D-016).  Usage: python 00_SYSTEM/tools/d028_apply.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; SH = EP / "07_SHOTS"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

LOGICAL = ["REAL_SHOOT", "ARCHIVE", "ORIGINAL_GRAPHIC", "AI_STILL", "I2V_MOTION", "BLENDER_I2V", "EXTREME_CAMERA"]
PROVIDERS = ["HIGGSFIELD", "GOOGLE_FLOW", "BLENDER_LOCAL", "MANUAL", "NONE"]
# ---- schemas: logical pipeline + provider + model (legacy pipeline kept for compatibility) ----
p = R / "00_SYSTEM/schemas/shot.schema.json"; s = rd(p)
s["properties"]["logical_pipeline"] = {"type": ["string", "null"], "enum": LOGICAL + [None],
    "description": "D-028 논리 분류 (공급자·모델과 무관). legacy pipeline 대응: AI_STILL→AI_STILL, FLOW_VEO→I2V_MOTION, BLENDER_FLOW→BLENDER_I2V, HIGGSFIELD→EXTREME_CAMERA"}
s["properties"]["provider"] = {"type": ["string", "null"], "enum": PROVIDERS + [None], "description": "D-028 공급 플랫폼 (예: HIGGSFIELD)"}
s["properties"]["model"] = {"type": ["string", "null"], "description": "D-028 실제 생성 모델 ID (예: KLING_3_0, NANO_BANANA_PRO)"}
w(p, s)
p = R / "00_SYSTEM/schemas/router_decision.schema.json"; s = rd(p)
s["properties"]["selected_provider"] = {"type": ["string", "null"], "description": "D-028 선택된 공급 플랫폼"}
s["properties"]["selected_model"] = {"type": ["string", "null"], "description": "D-028 선택된 모델"}
w(p, s)

# ---- 8 AI shots ----
MAP = {"AI_STILL": "AI_STILL", "FLOW_VEO": "I2V_MOTION", "BLENDER_FLOW": "BLENDER_I2V", "HIGGSFIELD": "EXTREME_CAMERA"}
count = 0
for f in sorted(SH.glob("shot_*.json")):
    d = rd(f)
    if d["pipeline"] not in MAP: continue
    d["logical_pipeline"] = MAP[d["pipeline"]]; d["provider"] = "HIGGSFIELD"
    d["model"] = "NANO_BANANA_PRO" if d["pipeline"] == "AI_STILL" else "KLING_3_0"
    if "D-028" not in d["notes"]:
        d["notes"] += f" D-028: logical_pipeline {d['logical_pipeline']} · provider HIGGSFIELD (공급 플랫폼) · model {d['model']}" + (" (시작 사진 필요 시 NANO_BANANA_PRO)" if d["model"] == "KLING_3_0" else "") + "."
    d["updated_at"] = D; w(f, d); count += 1
    r = SH / f"router_decision_RTR_{d['shot_id']}_V01.json"; rr = rd(r)
    rr["selected_provider"] = "HIGGSFIELD"; rr["selected_model"] = d["model"]
    cand = "Higgsfield (Kling 3.0)" if d["model"] == "KLING_3_0" else "Higgsfield (Nano Banana Pro)"
    if cand not in rr["provider_candidates"]: rr["provider_candidates"].append(cand)
    w(r, rr)
assert count == 8, count

# ---- D4 approval: H06 still only ----
w(C / "approval_APR_EP01_AI_B1_001.json", {
    "approval_id": "APR_EP01_AI_B1_001", "kind": "PAID_GENERATION", "target_id": "EP01_S06_SH010",
    "money_gate_presented": {"shot_id": "EP01_S06_SH010", "prompt_ids": ["PRM_EP01_S06_SH010_V01"],
        "provider_model": "HIGGSFIELD / NANO_BANANA_PRO (job type nano_banana_2), 2k, 16:9 still",
        "expected_attempts": 2, "estimated_cost_range": "2–4 credits (hard cap 4)",
        "continuity_risk": "MEDIUM - mound 47 m x 12.7 m proportion, human scale, modern intrusion, construction stage"},
    "decision": "APPROVE", "fix_reason": None, "decided_by": "사용자", "decided_at": f"{D}T08:00:00Z",
    "note": "D-028 D4: H06 사진만. 최대 2 호출 / 4 credits. 영상 미포함. 첫 결과 승인 가능하면 2번째 미사용. 실패 시 실패 항목만 새 prompt 버전 + PATCH 후 재시도."})

# ---- H06 sent-form prompt V02 ----
v1 = rd(EP / "11_AI_STILLS/prompt_PRM_EP01_S06_SH010_V01.json"); v2 = dict(v1)
TEXT = " ".join([
 "One wide documentary photograph that fills the entire 16:9 frame edge to edge, a single still image; no black bars, no letterbox, no borders.",
 "Early Silla, Gyeongju, 5th century: the Cheonmachong earth mound nearly completed, seen from a distance.",
 "Use the reference image only for the site, soil colour, light mood and clothing palette; do not copy its people, its camera position or its unfinished stage.",
 "The mound is a broad, low, smooth dome of freshly packed earth, about 47 metres across and 12.7 metres high - almost four times as wide as it is high - with the last bare patches being smoothed near the top; no stones, timber or chamber visible anywhere.",
 "Small groups of people stand far off near its base for scale; a person about 1.6 metres tall is only about one eighth of the mound's height and looks tiny against it.",
 "They are labourers in undyed coarse hemp and funeral attendants in belted white, black and grey-brown hemp jackets; all different faces, no one in blue, no one posing, no one looking at the camera.",
 "Camera about 1.7 metres high, 24mm lens feel, static wide view, low warm sunlight from the side, long shadows, calm and permanent, not celebratory.",
 "Surroundings: open early countryside with bare low hills and a few trees; no utility poles, no power lines, no buildings, no roads, no fences, no regular field grid, no modern objects.",
 "Photorealistic historical documentary still, style B Documentary Reenactment, natural textures, not glossy, earthy natural colours.",
 "No tiled roofs, no stone walls, no manicured grass lawn, no gold objects, no crown, no text, no watermark, no logo."])
v2.update(prompt_id="PRM_EP01_S06_SH010_V02", version="V02", parent_prompt_id="PRM_EP01_S06_SH010_V01", patch_id=None, assembled_text=TEXT,
          reference_images=["master_frame:EP01_S06_MASTER_MOUND_BUILDING_V01"],
          shot_delta="H06 sent form: nearly completed 47 m x 12.7 m mound, human scale 1:8, 24mm static 1.7 m, clean early horizon; crowd costume in text only; label strings removed",
          created_at=D, created_by="Image Generation Agent (Claude Code) - sent form, saved before sending (D-016), D-028 D4")
w(EP / "11_AI_STILLS/prompt_PRM_EP01_S06_SH010_V02.json", v2)

# ---- decisions / standards / plan / status ----
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8"); anchor = "\n---\n\n## 승인 대기 (P)"
old = "EP01 은 다큐 톤 우선 → **Higgsfield 사용 0건으로 잠금**."
if old in s:
    s = s.replace(old, old + " *(D-028 명확화: HIGGSFIELD CAMERA / EXTREME CAMERA 파이프라인 = 0 shots. 공급 플랫폼으로서 Higgsfield 는 허용.)*")
if "### D-028" not in s:
    s = s.replace(anchor, """
### D-028 · 2026-09-13 · 영상 공급자 · D-024 의미 명확화 · 논리 분류와 공급자/모델 분리 · H06 사진 승인 (사용자)
**D1 (A)** 영상 생성은 **Higgsfield 를 공급 플랫폼(provider)** 으로 쓰고 **실제 모델은 Kling 3.0 (model)**. "Higgsfield 방식" 승인이 아니다.
**D-024 명확화 (폐기 아님)** `HIGGSFIELD CAMERA / EXTREME CAMERA PIPELINE = 0 shots` · `Higgsfield as model provider = allowed` · `Selected model for current I2V test = Kling 3.0`.
**분류 분리** 모델·서비스 이름을 샷 판정에 박지 않는다. 샷에 `logical_pipeline` · `provider` · `model` 을 별도로 남긴다: 사람 동작 사진→영상 = `I2V_MOTION / HIGGSFIELD / KLING_3_0`, Blender 필요 = `BLENDER_I2V / HIGGSFIELD / KLING_3_0`, 정지 = `AI_STILL / HIGGSFIELD / NANO_BANANA_PRO`, 극단 카메라 = `EXTREME_CAMERA` (EP01 0). 기존 `pipeline` 값(FLOW_VEO · BLENDER_FLOW)은 호환 때문에 유지. 라우터에 `selected_provider/selected_model`, 영상 6개 `provider_candidates` 에 Higgsfield (Kling 3.0) 추가. 검증기: AI 샷은 세 필드 필수 + 대응 일치.
**D3** Blender 없이 기준 그림/시작 사진 + 카메라 초안 → I2V 로 먼저 시도. **같은 샷 공간 오류 2회 연속 → STOP → Blender 전환 여부 재승인. 자동 3번째 생성 금지.**
**D4** `APR_EP01_AI_B1_001` H06 (`EP01_S06_SH010`) 사진만, 최대 2 호출 / 4 credits, 영상 미포함. 첫 결과가 승인 가능하면 2번째 미사용. 실패 시 실패 항목만 새 prompt 버전 + PATCH.
**D2 (P-012 미정 유지)** 원화 환산은 실제 계정 월 결제 금액(원화 청구액) + 월 지급 크레딧으로 확정. 봇은 공개 요금표 숫자를 임의로 기록하지 않는다. **영상 생성은 아직 승인하지 않음.**
""" + anchor, 1)
s = s.replace("**제안** 플랜 월 요금 ÷ 월 크레딧으로 1 credit 당 KRW 를 정해 `COST_STANDARD.md` 에 기록.",
              "**제안** 플랜 월 요금 ÷ 월 크레딧으로 1 credit 당 KRW 를 정해 `COST_STANDARD.md` 에 기록. **D-028: 실제 계정 청구 원화 금액 + 월 지급 크레딧(Manage Account → Subscription 캡처 또는 수치)으로만 확정. 영상 배치 전 필수.**")
p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/standards/MODEL_ROUTER.md"; s = p.read_text(encoding="utf-8")
if "D-028" not in s:
    s = s.rstrip("\n") + ("\n\n## 논리 분류 · 공급자 · 모델 분리 (D-028)\n"
        "샷 판정(논리 분류)은 공급자·모델이 바뀌어도 그대로 둔다. 모델 교체(Kling → Veo → Seedance 등)는 `provider` / `model` 필드만 바꾸고 새 승인을 받는다.\n\n"
        "| 논리 분류 (`logical_pipeline`) | legacy `pipeline` | 예: provider / model |\n|---|---|---|\n"
        "| `AI_STILL` | AI_STILL | HIGGSFIELD / NANO_BANANA_PRO |\n| `I2V_MOTION` (사람 동작 사진→영상) | FLOW_VEO | HIGGSFIELD / KLING_3_0 |\n"
        "| `BLENDER_I2V` (공간·카메라 사전 작업 필요) | BLENDER_FLOW | HIGGSFIELD / KLING_3_0 (+ BLENDER_LOCAL 사전 작업) |\n"
        "| `EXTREME_CAMERA` (극단 카메라·강한 임팩트) | HIGGSFIELD | EP01 = 0 shots |\n")
    p.write_text(s, encoding="utf-8")

p = EP / "15_QA/AI_SHOT_PLAN_EP01.md"; s = p.read_text(encoding="utf-8")
if "## 결정 (D-028)" not in s:
    s += ("\n## 결정 (D-028, 2026-09-13)\n\n- D1 A: provider = HIGGSFIELD, model = KLING_3_0 (영상) · NANO_BANANA_PRO (사진). D-024 의 0건 = EXTREME_CAMERA 파이프라인 0건.\n"
          "- 샷 기록에 `logical_pipeline` (I2V_MOTION · BLENDER_I2V · AI_STILL) + provider + model 분리 기록.\n"
          "- D3 OK: 공간 오류 2회 연속 → STOP → Blender 전환 재승인, 자동 3번째 금지.\n"
          "- D4: `APR_EP01_AI_B1_001` H06 사진만 최대 2 호출 / 4 credits. 문장 `PRM_EP01_S06_SH010_V02` 저장.\n"
          "- D2: 실제 계정 청구액 + 월 크레딧 받으면 P-012 확정. **영상 생성 미승인.**\n")
    p.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
if "D-028." not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 사용자** — **D-028.** Higgsfield = provider, Kling 3.0 = model (영상), D-024 '0건' = EXTREME_CAMERA 파이프라인 0건으로 명확화. 샷에 logical_pipeline/provider/model 분리. D3 Blender 없이 먼저, 공간 오류 2회 STOP. D4 H06 사진 최대 2회/4 credits. P-012 는 실제 청구액 받으면 확정, **영상 미승인**.\n", 1)
p.write_text(s, encoding="utf-8")
print("D-028 applied")
