# -*- coding: utf-8 -*-
"""Record Master Pack batch 1 (elite: hero x2 attempts, front, 3/4 left, full body)."""
import json, sys
from pathlib import Path
R = Path(sys.argv[1]); D = "2026-09-11"; CACHE = "08_GENERATION_CACHE/EP01"
def rd(p): return json.loads((R / p).read_text(encoding="utf-8"))
def w(p, d):
    p = R / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

STD = {"CHARACTER_CONTINUITY_STANDARD.md": "v0.1", "COST_STANDARD.md": "v0.1"}
def gen(slot, ver, job, model, cost, started, finished, out, status, notes, inputs=(), attempts=1):
    return {"generation_id": f"GEN_MP_ELITE_{slot}_HIGGSFIELD_{ver}", "shot_id": f"MASTER_PACK:CHAR_SILLA_ELITE_OBSERVER_01:{slot.lower()}",
            "stage": "STILL", "provider": "Higgsfield", "model": model, "prompt_id": f"PRM_MP_CHAR_SILLA_ELITE_OBSERVER_01_{slot}_V01", "prompt_version": "V01",
            "standard_versions": STD, "case_ids_used": ["CASE_DDABONG_CHAR_001"], "approval_id": "APR_EP01_MP_ELITE_BATCH1_001",
            "input_paths": list(inputs), "output_paths": [f"{CACHE}/MP_ELITE/{out}"], "attempts": attempts, "duration_sec": None,
            "cost": {"currency": "CREDITS", "amount": cost, "spent": cost, "note": f"Higgsfield job {job}"},
            "result_status": status, "failure_id": None, "started_at": started, "finished_at": finished,
            "run_by": "Image Generation Agent (Claude Code)", "notes": notes}

HERO_REF = f"{CACHE}/MP_ELITE/MP_ELITE_HERO_V02_c7a5cc92.png"
recs = [
 gen("HERO", "V02", "c7a5cc92-3f36-4b40-8071-84da9f6c6441", "nano_banana_pro (2k, 3:4)", 2.0, "2026-09-11T13:37:41Z", "2026-09-11T13:38:20Z",
     "MP_ELITE_HERO_V02_c7a5cc92.png", "SUCCESS", "Attempt 2 after V01 REJECTED. Changed only failed items: single subject, ivory inner (no crimson), no text, timber yard background. PASS on lock: Korean 40s-50s restrained face, birch-bark conical cap, muted blue outer robe, bronze plaque belt with pendants, no crown. Human-review flags: outer robe is short-sleeved over long inner sleeves (lock says narrow-sleeved inner + longer outer; acceptable but confirm); tiled roofs visible in background. This image is the identity reference (job id) for the other views.", attempts=2),
 gen("FRONT", "V01", "ae0b4062-481f-46e0-919e-28289aaba8e0", "nano_banana_pro (2k, 3:4, image_references=hero V02)", 2.0, "2026-09-11T13:39:01Z", "2026-09-11T13:39:40Z",
     "MP_ELITE_FRONT_V01_ae0b4062.png", "SUCCESS", "Same face identity as hero V02. Flat daylight, plain grey-brown background. Costume identical. No forbidden elements, no text.", inputs=[HERO_REF]),
 gen("THREE_QUARTER_LEFT", "V01", "8d82a4c5-cd4f-4605-83b7-d5ab5fb3e350", "nano_banana_pro (2k, 3:4, image_references=hero V02)", 2.0, "2026-09-11T13:39:05Z", "2026-09-11T13:39:45Z",
     "MP_ELITE_THREE_QUARTER_LEFT_V01_8d82a4c5.png", "SUCCESS", "Same face identity, ~45 deg left turn, cap silhouette clear (useful for profile later). Plain earth background. No forbidden elements, no text.", inputs=[HERO_REF]),
 gen("FULL_BODY", "V01", "5681f1e0-fe07-4fc3-b36c-f512dc7a2992", "nano_banana_pro (2k, 2:3, image_references=hero V02)", 2.0, "2026-09-11T13:39:09Z", "2026-09-11T13:39:50Z",
     "MP_ELITE_FULL_BODY_V01_5681f1e0.png", "SUCCESS", "Head to toe, plain earth ground. Below-knee muted blue outer robe, ivory inner narrow sleeves, wide grey trousers, bronze belt with pendants, ankle boots over socks. Natural proportions -> use for height_ratio. Same face. No forbidden elements, no text.", inputs=[HERO_REF]),
]
for r in recs: w(f"{CACHE}/generation_{r['generation_id']}.json", r)

# cost.json — credits spent 8.12 (balance 1964.60 -> 1956.48); KRW conversion pending (P-012)
c = rd(f"{CACHE}/cost_COST_EP01_20260911.json")
c["spent_by_provider"] = {"Higgsfield (credits)": 8.12}
c["spent_total"] = None; c["percent_used"] = None
c["budget"]["spent"] = None
c["budget"]["note"] = "D-015 사용자 확정 ₩40,000. 소진은 Higgsfield 크레딧 8.12 (잔액 1964.60→1956.48). 크레딧→KRW 환산율 미확정 (P-012) → spent_total/percent_used null."
c["generation_ids"] = ["GEN_MP_ELITE_HERO_HIGGSFIELD_V01", "GEN_MP_ELITE_HERO_HIGGSFIELD_V02", "GEN_MP_ELITE_FRONT_HIGGSFIELD_V01", "GEN_MP_ELITE_THREE_QUARTER_LEFT_HIGGSFIELD_V01", "GEN_MP_ELITE_FULL_BODY_HIGGSFIELD_V01"]
c["note"] = "배치 1 완료: 5 호출 (soul_2 0.12 + nano_banana_pro 2 x 4) = 8.12 credits. P-012 환산율 확정 시 percent_used 계산. 80% WARNING · 95% STRONG · 100% LOCKED."
w(f"{CACHE}/cost_COST_EP01_20260911.json", c)

# character master_pack slots -> DRAFT (await human APPROVED)
ch = rd("05_HISTORY_DATABASE/characters/CHAR_SILLA_ELITE_OBSERVER_01.json")
for slot, gid, path in [("hero", "GEN_MP_ELITE_HERO_HIGGSFIELD_V02", "MP_ELITE_HERO_V02_c7a5cc92.png"),
                        ("front", "GEN_MP_ELITE_FRONT_HIGGSFIELD_V01", "MP_ELITE_FRONT_V01_ae0b4062.png"),
                        ("three_quarter_left", "GEN_MP_ELITE_THREE_QUARTER_LEFT_HIGGSFIELD_V01", "MP_ELITE_THREE_QUARTER_LEFT_V01_8d82a4c5.png"),
                        ("full_body", "GEN_MP_ELITE_FULL_BODY_HIGGSFIELD_V01", "MP_ELITE_FULL_BODY_V01_5681f1e0.png")]:
    ch["master_pack"][slot] = {"path": f"{CACHE}/MP_ELITE/{path}", "generation_id": gid, "status": "DRAFT"}
ch["status"] = "MASTER_IN_PROGRESS"; ch["updated_at"] = D
ch["notes"] += " 배치 1 생성 완료 (hero V02 · front · three_quarter_left · full_body, DRAFT) → 사람 검수 대기. 얼굴 ID 참조 = Higgsfield job c7a5cc92."
w("05_HISTORY_DATABASE/characters/CHAR_SILLA_ELITE_OBSERVER_01.json", ch)

# review sheet
(R / f"{CACHE}/MP_ELITE/REVIEW_BATCH1.md").write_text(f"""# 원로 Master Pack 배치 1 — 사람 검수 시트

> 생성 {D} · 승인 `APR_EP01_MP_ELITE_BATCH1_001` · 5 호출 / 4 채택 · 8.12 credits (KRW 환산 P-012)
> 이미지 파일은 Git 미추적 (이 폴더). 검수 결과는 `character.master_pack.<slot>.status` 를 APPROVED / MISSING(재생성) 으로 갱신하고 D-번호를 남긴다.

| slot | 파일 | 모델 | 판정(봇) | 사람 검수 |
|---|---|---|---|---|
| hero (V01) | `MP_ELITE_HERO_V01_35407202.png` | soul_2 | **REJECTED** — 갑옷 두 번째 인물, 다홍 내의, 가짜 문자 워터마크 | 참고용만 |
| hero (V02) | `MP_ELITE_HERO_V02_c7a5cc92.png` | nano_banana_pro | PASS — 단독, muted blue + 상아 내의 + bronze 과대 + 자작나무 관모, 문자 없음 | ☐ APPROVE ☐ FIX |
| front | `MP_ELITE_FRONT_V01_ae0b4062.png` | nano_banana_pro + hero 참조 | PASS — 동일 얼굴, 균일광, 무배경 | ☐ APPROVE ☐ FIX |
| three_quarter_left | `MP_ELITE_THREE_QUARTER_LEFT_V01_8d82a4c5.png` | nano_banana_pro + hero 참조 | PASS — 동일 얼굴, 관모 실루엣 명확 | ☐ APPROVE ☐ FIX |
| full_body | `MP_ELITE_FULL_BODY_V01_5681f1e0.png` | nano_banana_pro + hero 참조 | PASS — 전신, 화(靴)+버선, 통 넓은 회색 바지, 자연 비율 | ☐ APPROVE ☐ FIX |

## 검수 포인트 (사람이 결정)

1. **표의 소매 길이** — 4장 모두 표의가 반소매, 내의 좁은 소매가 밖으로 나옴. lock 은 "좁은 소매 유 + 긴 표의" 라 위반은 아니지만 의도(긴 소매 표의)와 다르면 FIX(COSTUME) → KEEP face/cap/belt, CHANGE sleeve → 4장 재생성 (약 8 credits).
2. **관모** — 백화모 계열 원뿔형. 근거 CLM_003/008 과 맞는지 확인.
3. **연령** — 40대 후반 인상. 50대로 올릴지.
4. hero V02 배경의 기와지붕 — hero 는 대표 초상이라 허용 범위인지.
5. 동일 얼굴 판정 — 4장 나란히 놓고 확인.

## 승인 시 다음 단계 (G1 잔여)

three_quarter_right · profile · neutral_standing · walking · costume_detail · expression_sheet 6장 + back_view 1장 (보조) — 전부 hero V02 를 image_references 로. 별도 approval `APR_EP01_MP_ELITE_BATCH2_001`.
""", encoding="utf-8")

# DECISIONS P-012 + CURRENT_STATUS
p = R / "00_SYSTEM/DECISIONS.md"; s = p.read_text(encoding="utf-8")
if "### P-012" not in s:
    s = s.replace("## 승인 대기 (P)\n", "## 승인 대기 (P)\n\n### P-012 · Higgsfield 크레딧 → KRW 환산율 (Money Gate 계산용)\n**현황** 예산은 KRW ₩40,000 (D-015), 소진은 Higgsfield 크레딧 (배치 1 = 8.12 credits, plus 플랜). 환산율이 없어 `cost.percent_used` 를 계산할 수 없다.\n**제안** 플랜 월 요금 ÷ 월 크레딧으로 1 credit 당 KRW 를 정해 `COST_STANDARD.md` 에 기록.\n**영향** `08_GENERATION_CACHE/EP01/cost_COST_EP01_20260911.json` spent_total / percent_used.\n\n", 1)
p.write_text(s, encoding="utf-8")

p = R / "00_SYSTEM/CURRENT_STATUS.md"; s = p.read_text(encoding="utf-8")
s = s.replace("**유료 생성 현황 (D-015)**: Money Gate OPEN (₩40,000 / 소진 0). **지금 가능**: 원로 Master Pack 배치 1 (hero · front · three_quarter_left · full_body 4장, `approval_APR_EP01_MP_ELITE_BATCH1_001` APPROVE) → 사람 검수 → 나머지 6 + back_view → 군중 6.",
              "**유료 생성 현황 (D-015)**: Money Gate OPEN (₩40,000 / 소진 8.12 credits, KRW 환산 P-012). **배치 1 생성 완료 → 사람 검수 대기** `08_GENERATION_CACHE/EP01/MP_ELITE/REVIEW_BATCH1.md` (hero V02 · front · three_quarter_left · full_body, DRAFT). 승인되면 나머지 6 + back_view → 군중 6.", 1)
s = s.replace("| 소진 | ₩0 (0%) |", "| 소진 | 8.12 credits (5 호출, 4 채택) — KRW 환산 P-012 |", 1)
s = s.replace("- **P-011** 라우터 판정 49건", "- **P-012** Higgsfield 크레딧→KRW 환산율 (NEW).\n- **배치 1 검수** `08_GENERATION_CACHE/EP01/MP_ELITE/REVIEW_BATCH1.md` — 4장 APPROVE/FIX, 특히 표의 소매 길이.\n- **P-011** 라우터 판정 49건", 1)
s = s.replace("## 최근 변경 (최신순)\n", "## 최근 변경 (최신순)\n\n- **2026-09-11 Claude Code** — **첫 유료 생성.** 원로 Master Pack 배치 1: hero V01 REJECTED(갑옷 인물·다홍·워터마크) → V02 PASS, front · three_quarter_left · full_body (hero 참조) PASS. 5 호출 8.12 credits. generation.json 5, cost 갱신, character MASTER_IN_PROGRESS, 검수 시트. P-012 등록.\n", 1)
p.write_text(s, encoding="utf-8")
print("recorded")
