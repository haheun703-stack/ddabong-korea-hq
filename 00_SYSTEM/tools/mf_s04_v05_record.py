# -*- coding: utf-8 -*-
"""Record S04 master frame V05 fresh text-only generation (job c4ceb494, sent verbatim) as SUCCESS; frame path -> V05 (DRAFT, owner OK pending).
Usage:  python 00_SYSTEM/tools/mf_s04_v05_record.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[2]; EP = R / "02_SEASONS/S01/EP01"; C = R / "08_GENERATION_CACHE/EP01"; D = "2026-09-13"
def rd(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def w(p, d): Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
JOB = "c4ceb494-cc0b-43d4-96bc-58d5d3830ff5"; GID = "GEN_MF_EP01_S04_MASTER_HIGGSFIELD_V05"; PID = "PRM_MF_EP01_S04_MASTER_V05"
OUT = "08_GENERATION_CACHE/EP01/MF/MF_EP01_S04_MASTER_V05_c4ceb494.png"
jp = f"08_GENERATION_CACHE/EP01/provider_jobs/HF_{JOB}.json"
w(R / jp, {"provider": "Higgsfield", "job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "status": "completed",
           "created_at": f"{D}T06:51:52Z",
           "params": {"width": 2752, "height": 1536, "aspect_ratio": "16:9", "resolution": "2k", "batch_size": 1, "input_images": [],
                      "prompt": rd(EP / f"11_AI_STILLS/prompt_{PID}.json")["assembled_text"]},
           "retrieved_at": D, "note": "job_status result. Result/CDN URLs omitted. params.prompt = text actually sent (identical to prompt V05)."})
w(C / f"generation_{GID}.json", {
    "generation_id": GID, "shot_id": "MASTER_FRAME:EP01_S04_MASTER_V01", "stage": "STILL", "provider": "Higgsfield",
    "model": "Nano Banana Pro (job_set_type nano_banana_2, 2k, 16:9, text only - no image reference)",
    "provider_job": {"job_id": JOB, "job_set_type": "nano_banana_2", "display_name": "Nano Banana Pro", "params_path": jp},
    "prompt_id": PID, "prompt_version": "V05",
    "standard_versions": {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"},
    "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MF_001",
    "input_paths": [], "output_paths": [OUT], "attempts": 1, "duration_sec": None,
    "cost": {"currency": "CREDITS", "amount": 2.0, "spent": 2.0, "note": f"Higgsfield job {JOB} (balance 1862.48 -> 1860.48)"},
    "result_status": "SUCCESS", "failure_id": None, "started_at": f"{D}T06:51:52Z", "finished_at": None,
    "run_by": "Image Generation Agent (Claude Code)",
    "notes": ("Fresh text-only generation (PATCH_MF_EP01_S04_004, owner '진행'). Bot check PASS: labourer faces clearly varied (ages, grey hair, clean-shaven and bearded, "
              "black and off-white jackets, headband or bare topknot) - no cloned look; full frame; horizon low hills and trees; open-topped chamber with river-stone course, "
              "no mound; wooden mallets, shoulder-pole baskets, log yard. Minor notes: two spades in the middle background still read as metal-bladed; a tiny white speck "
              "on the far right horizon. Crowd lesson: a single crowd reference image clones faces - describe crowd costume in text instead.")})
pt = rd(C / "keep_change_patch_PATCH_MF_EP01_S04_004.json"); pt["resulting_generation_id"] = GID; w(C / "keep_change_patch_PATCH_MF_EP01_S04_004.json", pt)
mf = EP / "07_SHOTS/master_frame_EP01_S04_MASTER_V01.json"; d = rd(mf); d["path"] = OUT; d["generation_id"] = GID; d["status"] = "DRAFT"; d["updated_at"] = D; w(mf, d)
c = rd(C / "cost_COST_EP01_20260911.json")
if GID not in c["generation_ids"]: c["generation_ids"].append(GID)
c["spent_by_provider"] = {"Higgsfield (credits)": 60.12}
c["budget"]["note"] = c["budget"]["note"].split(" 소진")[0] + " 소진 Higgsfield 60.12 credits (원로 24.12 · 군중 20 · 기준 그림 16). 크레딧→KRW 환산율 미확정 (P-012). 계정 크레딧은 다른 작업과 공용 (D-018) → job 기록 합계로 계산 (06:31:23Z 출처 불명 -2 는 미포함)."
c["note"] = "31 호출 = 60.12 credits (원로 13 · 군중 10 · 기준 그림 8). P-012 환산율 확정 시 percent_used 계산."
w(C / "cost_COST_EP01_20260911.json", c)
r = C / "MF/REVIEW_MF_V01.md"; s = r.read_text(encoding="utf-8")
if "## S04 새로 생성 V05 결과" not in s:
    s += ("\n## S04 새로 생성 V05 결과 (참고 그림 없음, 2 credits, 승인 8/10)\n\n`MF_EP01_S04_MASTER_V05_c4ceb494.png` **PASS** — 얼굴·나이·수염·옷색 제각각 (복제 느낌 해소), 꽉 찬 화면, 깨끗한 지평선, 공사 초기 단계. "
          "메모: 가운데 뒤 삽 2자루 쇠 날처럼 보임, 오른쪽 끝 지평선 작은 흰 점. 사용자 최종 OK 대기.\n")
r.write_text(s, encoding="utf-8")
p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
for a, b in [("| 소진 | 58.12 credits (30 호출: 원로 13 · 군중 10 · 기준 그림 7) — KRW 환산 P-012 |", "| 소진 | 60.12 credits (31 호출: 원로 13 · 군중 10 · 기준 그림 8) — KRW 환산 P-012 |"),
             ("소진 58.12 credits, KRW 환산 P-012)", "소진 60.12 credits, KRW 환산 P-012)")]:
    s = s.replace(a, b)
if "S04 V05 PASS" not in s:
    s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-13 Claude Code** — 사용자 지적 (S04 노동자 얼굴 복제) → 참고 그림 없이 새로 생성 V05, S04 V05 PASS (2 credits, 승인 8/10). 사용자 최종 OK 대기 → OK 면 기준 그림 3장 확정. EP01 소진 60.12 credits.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded", GID)
