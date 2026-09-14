# PHOTO_AI_STANDARD — 파이프라인 A: 사진 탐색 → AI 리디자인 → 영상화

> 문서 버전 **v0.1 DRAFT** (2026-09-14, Claude Code) · 근거: D-033 #1 #2 (사용자 승인 2026-09-14) · `RIGHTS_STANDARD.md` · `PROMPT_STANDARD.md` (Sent Prompt Rule) · `MODEL_ROUTER.md` (D-028 logical pipeline)
> 벤치마크: `09_ANALYTICS/benchmarks/BENCHMARK_ARCHDICT_GYEONGHOERU_20260914.md` (현장 촬영 0, 실사풍 30% 는 전부 사진→AI 재구성)
> 도구: `00_SYSTEM/tools/photo_search.py` (A2) · 프롬프트 템플릿 `06_PROMPT_LIBRARY/templates/PHOTO_AI_REDESIGN_V01.md` (A4)

---

## 1. 무엇을 위한 파이프라인인가

현재 시점의 장소·풍경·건물을 **현장 촬영 없이** 실사풍으로 만든다. 공개 라이선스 사진을 참고 이미지로 넣고, 계절·빛·구도를 샷 요구에 맞춰 AI 로 다시 그린다. 움직임이 필요하면 그 정지 이미지를 5–6초 영상으로 만든다.
쓰지 않는 곳: 유물 (ARCHIVE 그대로) · 역사 인물 장면 (Character Master 파이프라인) · 도해 (파이프라인 B).

## 2. 단계

| 단계 | 내용 | 산출 | 비용 |
|---|---|---|---|
| A1 | 샷 요구 읽기 — `shot.purpose` · `location` · 계절·빛·사람·움직임 (`human_motion`) | — | 0 |
| A2 | 후보 탐색 — `photo_search.py` 로 Commons 후보를 등급·크기와 함께 표로. e뮤지엄·공유마당·KTV 는 수동 (스크립트 확장 예정) | `15_QA/PHOTO_AI_CANDIDATES_<date>.md/.json` | 0 |
| A3 | 권리 기록 — 고른 원본마다 `rights/RTS_*.json` (페이지 원문 proof 저장, 실측 크기) | rights 인스턴스 | 0 |
| A4 | AI 리디자인 — 템플릿으로 프롬프트 조립 → **Sent Prompt Rule** (저장 → 그대로 전송 → generation 기록 연결) | prompt + generation 인스턴스, 정지 이미지 | 유료 (이미지 1–2 크레딧) |
| A5 | 영상화 (선택) — `human_motion ≥ 30` 또는 카메라 이동 필요 시 I2V 5–6초. 현장음은 CC0 음원 별도 | generation 인스턴스, 클립 | 유료 (5–10 크레딧) |
| A6 | 라벨·계보·검증 — `ai_label` · `photo_ai.source_rights_ids` · `validate.py` 통과 | 샷 JSON 갱신 | 0 |

A4·A5 는 Money Gate (COST_STANDARD) 와 사용자 승인 뒤에만. A1–A3·A6 은 봇이 바로 간다.

## 3. 권리 규칙 (핵심)

1. **AI 참고 이미지로 넣는 원본은 GREEN 만** — CC0 · Public Domain · 공공누리 1유형. `rights.status = GREEN`, `usage_tier = ACTIVE`, `modification_allowed = "YES"` (rights 스키마 enum 은 문자열). 자체 촬영 원본도 GREEN (D-026, rights 인스턴스 + proof 필수).
2. **YELLOW (CC BY · CC BY-SA)** 는 참고 이미지로 넣지 않는다. "봉분 위치 · 지평선 높이 · 렌즈 추정" 같은 **수치만** 옮겨 적는다 (프롬프트 텍스트에 반영, 이미지 미첨부). 이 경우 `photo_ai.source_rights_ids` 에 넣지 않고 `photo_ai.composition_ref_note` 에 적는다.
3. **RED** (NC · ND · 사용범위 불명 · 경주시 관광사진 등) 는 어떤 방식으로도 쓰지 않는다.
4. **AI 재구성 결과물은 원본 권리를 승계한다.** 원본이 GREEN 이어야 결과물이 GREEN. 결과물 rights 는 따로 만들지 않고 샷의 `photo_ai.source_rights_ids` 로 계보를 남긴다.
5. **AI 라벨 필수.** 실사처럼 보여도 `ai_label` 을 비우지 않는다. 현재 시점 장소 재구성은 `AI Visual Reconstruction (present-day, photo-based)`. 유튜브 합성 콘텐츠 공개 표시 대상.
6. 실제 인물 얼굴이 식별되는 원본은 쓰지 않는다 (관람객은 뒷모습·원경만).

## 4. 샷 JSON 필드 (`shot.schema.json` `photo_ai`, 선택)

```json
"photo_ai": {
  "source_rights_ids": ["RTS_COMMONS_DAEREUNGWON_GAGNON_001"],
  "composition_ref_note": "YELLOW 慶州-大陵苑-天馬塚 에서 봉분 중심 x=0.55, 지평선 y=0.62 만 옮김 (이미지 미첨부)",
  "redesign_prompt_id": "PRM_PA_EP01_S02_SH001_V01",
  "i2v_generation_id": null
}
```

검증기 규칙 (`validate.py photo_ai_rules`, D-033):
- `photo_ai` 가 있으면 `pipeline` ∈ {`AI_STILL`, `FLOW_VEO`} 이어야 한다.
- `source_rights_ids` 각각 실존 · `status = GREEN` · `usage_tier = ACTIVE` · `modification_allowed = "YES"`. 아니면 **FAIL**. YELLOW 수치 전용이면 `source_rights_ids: []` + `composition_ref_note` 필수.
- `ai_label` 비어 있으면 **FAIL** (기존 규칙과 중복이지만 photo_ai 는 별도 메시지).
- `redesign_prompt_id` 가 있으면 prompt 인스턴스 실존.

## 5. 목표 배합 안에서의 자리

EP02 부터 화면의 25–30% (D-033 #4). ① QUESTION · ④ CONTEXT · ⑦ LEGACY 단계에서 주로 쓴다 (STORY_ENGINE_STANDARD §2).

## 미결 (사용자 결정 필요)

- e뮤지엄·공유마당·KTV 자동 탐색 추가 여부 (API 유무 확인 필요).
- 원본 GREEN 사진이 없을 때의 대안 순서: (a) YELLOW 수치만 → 텍스트 전용 생성, (b) 현장 촬영, (c) 샷 삭제. 기본값 제안 = (a).
- 현재 시점 재구성의 라벨 문구 확정 (`AI Visual Reconstruction (present-day, photo-based)`).
