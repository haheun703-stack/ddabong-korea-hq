# -*- coding: utf-8 -*-
"""Record elite Master Pack batch 2 (D-018): 7 jobs sent verbatim from V02 prompts.
Usage:  python 00_SYSTEM/tools/batch2_record.py
"""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[2]
CHAR = "CHAR_SILLA_ELITE_OBSERVER_01"; CACHE = "08_GENERATION_CACHE/EP01"; STILLS = "02_SEASONS/S01/EP01/11_AI_STILLS"
APR = "APR_EP01_MP_ELITE_BATCH2_001"
REF_JOBS = [{"id": "5de27748-f100-47e0-af23-1bdb68466bb7", "type": "image_job"}, {"id": "5681f1e0-fe07-4fc3-b36c-f512dc7a2992", "type": "image_job"}]
REF_PATHS = [f"{CACHE}/MP_ELITE/MP_ELITE_HERO_V03_5de27748.png", f"{CACHE}/MP_ELITE/MP_ELITE_FULL_BODY_V01_5681f1e0.png"]
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# slot, job, created (from result file name), size, aspect, bot check
JOBS = [
 ("THREE_QUARTER_RIGHT", "73a0605d-ef41-47dd-8cca-2f3c1c7bb7b6", "04:21:11", (1792, 2400), "3:4",
  "PASS - same face, turned ~45 deg showing his right side, plain earth-toned background, costume identical. Cap reads slightly taller/rounder than hero."),
 ("PROFILE", "008de825-bc0c-465d-a68a-a1853aa22103", "04:21:11", (1792, 2400), "3:4",
  "PASS with note - true profile and clear cap silhouette, same face. Faces screen RIGHT (prompt asked screen left); mirror in edit if direction matters. Cap slightly taller."),
 ("NEUTRAL_STANDING", "87b625c8-a537-4ca2-add6-fbb9049a7913", "04:21:10", (1696, 2528), "2:3",
  "PASS - front full body, even stance, hands at sides, costume identical. Nearly the same framing as full_body V01 (acceptable for this slot)."),
 ("WALKING", "200b0388-1ad1-4299-b9c7-20bf3318d74e", "04:21:11", (1696, 2528), "2:3",
  "PASS - natural mid-stride from side-front, same face, boots/trousers/belt consistent, plain earth ground."),
 ("COSTUME_DETAIL", "2d1fbdfc-cf28-444d-80ce-9945bf72c40c", "04:21:11", (1792, 2400), "3:4",
  "PASS with note - collar right over left, silk/hemp weave, bronze plaque belt + pendants, sleeve ends and both hands clear. Crop shows mouth/chin (prompt said crop above chin) - harmless."),
 ("EXPRESSION_SHEET", "f7d6da72-89b6-44e4-8a84-73373070970d", "04:21:11", (2528, 1696), "3:2",
  "PASS - five head-and-shoulders panels, same face, restrained neutral/attentive/concerned/resolved/quiet grief, no labels or text."),
 ("BACK_VIEW", "fba70a58-ef3f-45b7-8f94-7c61d0284307", "04:21:11", (1696, 2528), "2:3",
  "PASS with note - directly behind, cap and shoulder silhouette clear, facing a mound under construction. Human check: a few thin grey scaffold poles at the top may read as modern metal pipes."),
]
gids = []
for slot, job, t, (wd, ht), ar, check in JOBS:
    pid = f"PRM_MP_{CHAR}_{slot}_V02"; sent = rd(f"{STILLS}/prompt_{pid}.json")["assembled_text"]
    jp = f"{CACHE}/provider_jobs/HF_{job}.json"
    w(jp, {"provider": "Higgsfield", "job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"2026-09-13T{t}Z",
           "params": {"width": wd, "height": ht, "aspect_ratio": ar, "resolution": "2k", "batch_size": 1, "input_images": REF_JOBS, "prompt": sent},
           "retrieved_at": "2026-09-13", "note": "generate_image_batch index/jobs_wait result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V02)."})
    gid = f"GEN_MP_ELITE_{slot}_HIGGSFIELD_V01"; gids.append(gid)
    out = f"{CACHE}/MP_ELITE/MP_ELITE_{slot}_V01_{job[:8]}.png"
    w(f"{CACHE}/generation_{gid}.json", {
        "generation_id": gid, "shot_id": f"MASTER_PACK:{CHAR}:{slot.lower()}", "stage": "STILL", "provider": "Higgsfield",
        "model": f"Nano Banana Pro (job_set_type nano_banana_2, 2k, {ar}, image_references=hero V03 + full_body V01)",
        "provider_job": {"job_id": job, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
        "prompt_id": pid, "prompt_version": "V02",
        "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
        "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": APR,
        "input_paths": REF_PATHS, "output_paths": [out], "attempts": 1, "duration_sec": None,
        "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {job} (batch of 7: balance 1912.48 -> 1898.48)"},
        "result_status": "SUCCESS", "failure_id": None, "started_at": f"2026-09-13T{t}Z", "finished_at": None,
        "run_by": "Image Generation Agent (Claude Code)", "notes": f"D-018 batch 2. Bot check: {check} Awaiting human review."})
    if slot != "BACK_VIEW":  # back_view is an auxiliary reference image, not a schema slot (D-015 D)
        ch = rd(f"05_HISTORY_DATABASE/characters/{CHAR}.json")
        ch["master_pack"][slot.lower()] = {"path": out, "generation_id": gid, "status": "DRAFT"}
        w(f"05_HISTORY_DATABASE/characters/{CHAR}.json", ch)

ch = rd(f"05_HISTORY_DATABASE/characters/{CHAR}.json"); ch["updated_at"] = "2026-09-13"
if "배치 2 생성" not in ch["notes"]:
    ch["notes"] += f" 배치 2 생성 (D-018): 나머지 6 슬롯 DRAFT + back_view 보조 이미지 `{CACHE}/MP_ELITE/MP_ELITE_BACK_VIEW_V01_fba70a58.png` → 사람 검수 대기."
w(f"05_HISTORY_DATABASE/characters/{CHAR}.json", ch)

c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["generation_ids"] += [g for g in gids if g not in c["generation_ids"]]
c["spent_by_provider"] = {"Higgsfield (credits)": 24.12}; c["as_of"] = "2026-09-13"
c["budget"]["note"] = "D-015 사용자 확정 ₩40,000. 소진 Higgsfield 24.12 credits (배치 1 8.12 + D-017 hero 편집 2 + D-018 배치 2 14). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → 잔액 차이가 아니라 job 기록 합계로 계산."
c["note"] = "13 호출 = 24.12 credits (배치 1 5 · hero 편집 1 · 배치 2 7). P-012 환산율 확정 시 percent_used 계산. 80% WARNING · 95% STRONG · 100% LOCKED."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

rows = "\n".join(f"| {s.lower()} | `MP_ELITE_{s}_V01_{j[:8]}.png` | {chk} | ☐ APPROVE ☐ FIX |" for s, j, _, _, _, chk in JOBS)
(R / f"{CACHE}/MP_ELITE/REVIEW_BATCH2.md").write_text(f"""# 원로 Master Pack 배치 2 — 사람 검수 시트

> 생성 2026-09-13 · 승인 `{APR}` (D-018) · 7 호출 / 7 성공 · 14 credits (승인 한도 10 호출 중 7)
> 모델 Nano Banana Pro (nano_banana_2), 참조 = hero V03 + full_body V01 (둘 다 APPROVED). 전송 = 각 `PRM_…_V02` 문장 그대로 (D-016).
> 결과는 `character.master_pack.<slot>.status` 를 APPROVED / FIX 로 갱신한다. back_view 는 보조 이미지 (슬롯 아님).

| slot | 파일 | 판정(봇) | 사람 검수 |
|---|---|---|---|
{rows}

## 사람이 볼 점

1. 7장 모두 배치 1 얼굴과 같은 사람인지.
2. profile 이 오른쪽을 본다 (요청은 왼쪽). 편집에서 좌우 반전으로 해결 가능 → FIX 불필요 판단.
3. back_view 상단 비계 기둥 몇 개가 가는 회색 금속관처럼 보이는지 (시대 lock: 현대 재료 금지).
4. 모자가 몇 장에서 hero 보다 약간 높고 둥글다 — 허용 범위인지.

FIX 는 남은 3 호출 안에서 실패 항목만 (PATCH + 새 prompt 버전 먼저).
""", encoding="utf-8")
print("recorded", len(gids))
