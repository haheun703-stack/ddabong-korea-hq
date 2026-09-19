# HERITAGE_INSERT_STANDARD — 유적 3D 구조 인서트 제작 레시피

> 문서 버전 **v0.1 ACTIVE** (2026-09-19, Claude Code · D-058 컷 종류 신설 · D-059 팔레트 태극 파랑 · P-015 #7 종결)
> 근거: 조사 `09_ANALYTICS/benchmarks/HERITAGE_INSERT_SURVEY_AND_PLAN_20260919.md` · 시험 4회 `08_GENERATION_CACHE/EP01/HERITAGE_INSERT/REVIEW_INSERT_G04_OMNI_V0[1-4]_*.md` (96 credits) · 룩 락 `06_PROMPT_LIBRARY/locks/DDABONG_TECH_INFOGRAPHIC_V01.json`
> 상위: `SHOT_STANDARD.md` §HERITAGE_INSERT (길이·위치·빈도) · `VISUAL_STYLE_BIBLE.md` §74 예외 (사람 없는 구조물 ≤10초)

---

## 1. 한 줄

**형상은 Blender 가, 재질은 영상 모델이, 글자는 편집이 맡는다.** 셋을 섞으면 시험 4회에서 본 실패가 그대로 재현된다.

## 2. 순서 (컷 1개 기준, 약 반나절 + 24 credits)

| # | 단계 | 도구 | 비용 | 산출 |
|---|---|---|---|---|
| 1 | 형상 확보 — 국가유산청 포털 3D (공공누리 1유형) 또는 실측 치수 (FACT fact_id). 소실 건물은 INTERPRETIVE | `tools/api/apis.py khs` · 포털 3D 목록 | 0 | 씬 스펙에 치수 + fact_id |
| 2 | Blender 씬 (또는 기존 씬에 카메라 추가) + **비례 단서** (1.7 m 인물 실루엣, `SCALE_CUES` 컬렉션) + 무한 평면은 `FS_EXCLUDE` | `tools/blender/build_cheonmachong.py` 패턴 | 0 | .blend / bpy 스크립트 |
| 3 | `--passes tech` 렌더 (Freestyle 구조선 태극 파랑 + 무채색 오버라이드 + 다크 월드 + 글로우) | Blender 4.2 headless | 0 | `<CAM>_tech.png` |
| 4 | 영상화 — `gemini_omni_flash_1_1` image-to-video, `start_image` = tech 플레이트, 8초 720p 16:9 | Higgsfield CLI | **24** | mp4 + provider job JSON |
| 5 | 검수 — 12프레임 시트 (1.5 fps) + §5 체크리스트 | `ffmpeg` + PIL | 0 | `QC_*_12FRAMES.jpg` + REVIEW md |
| 6 | 편집 — 오버레이 라벨 (영문 + 한자/국문 1줄, 밑줄형 치수), 강조 1요소만 브랜드 빨강, 모델이 그린 숫자는 덮기 | 편집 툴 | 0 | 컷 |
| 7 | 기록 — prompt / approval / generation / cost (Sent Prompt Rule) | 검증기 게이트 | 0 | `validate.py` cross-reference OK |

## 3. 프롬프트 템플릿 (V02/V04 검증본)

```
Technical architectural cutaway animation of <대상, 한 문장>, true scale: <봉분/건물 폭·높이 m>, the tiny human silhouette standing at the <위치> base is 1.7 metres, and <핵심 내부 요소> is only <m> long, so <비례를 말로: a small box deep inside a vast hill>. The camera performs one slow, smooth orbital move of about 15 degrees around the cross-section, revealing the layered interior: <층 1>, <층 2>, <층 3>. The glowing cobalt-blue structure lines stay crisp and continuous throughout as an overlay. Dark neutral grey background, no sky. Subtle floating dust motes only. No people other than the static scale silhouette, no text, no labels, no logos, no flicker. Steady, deliberate, museum-exhibit pacing.
```

**지켜야 할 것 (시험에서 돈 주고 확인)**
- 미터 값이 프롬프트에 있으면 **금지 문구와 무관하게 라벨로 렌더된다** (V02·V03). 그래서 라벨은 편집에서 덮는 것을 전제로 하고, 대신 비례가 정확해지는 이득을 취한다. 숫자를 빼면 비례가 무너진다 (V01 = 1/4).
- **프롬프트를 길게 하지 말 것.** 금지·지시를 더 얹은 V03 은 모델이 없는 옆방을 지어냈다. 구조는 플레이트가 정한 것만, 프롬프트는 재질·카메라·색만.
- 부정 프롬프트 필드는 쓰지 않는다 (real CFG 필요, D-057 fal 교훈). 배제는 본문 마지막 한 문장으로.
- `negative` 기록 필드는 글로벌 락 금지 목록을 상속한다 (검증기 규칙).

## 4. 플레이트 규격

- Freestyle: silhouette + crease(120°) + border + contour + external contour, 두께 2.6 px, 색 `--tech_rgb 0.20,0.58,1.00`.
- 오버라이드: 전 메시 → `tech_base` (0.11/0.12/0.14, roughness 0.95). 4.2 EEVEE Next 는 뷰레이어 material_override 를 무시하므로 슬롯 교체 방식 (`_swap_materials`).
- 월드: 노드 끄고 단색 (0.030/0.034/0.045). 하늘 노드가 켜져 있으면 상하 띠가 생기고 모델이 그걸 애니메이션한다 (V01).
- 컴포지터: Freestyle 패스 → Fog Glow (threshold 0.05, size 8) → 색 곱 → 베이스에 Add.
- **비례 단서 필수**: 1.7 m 실루엣 (실린더 + 구), 카메라 쪽 x 오프셋 0.6 m, 프레임 안·지면 위. 없으면 크기가 무너진다 (V01).
- **무한 평면 제외**: Ground 등은 `FS_EXCLUDE` 컬렉션 → lineset `collection_negation = EXCLUSIVE`.
- 작은 오브젝트 다수(돌무지)는 선이 뭉친다 → 인서트 대상이 돌무지 자체가 아니면 그 컬렉션도 `FS_EXCLUDE` 에.

## 5. 검수 체크리스트 (12프레임 시트)

1. 구조선이 8초 내내 끊기지 않고 색이 유지되는가
2. 층 순서·요소 수가 FACT 와 같은가 (지어낸 방·문·통로 없음)
3. 비례 — 핵심 내부 요소 / 전체 폭이 FACT 비율 ±20 % 안인가
4. 비례 인물이 정지해 있는가 (움직이면 인물 컷이 됨 → 금지)
5. 모델이 그린 숫자·글자의 **위치**를 적어 편집 오버레이로 전부 덮이는지 확인. 덮이지 않는 위치면 재생성
6. 카메라 — 느린 궤도/푸시인 하나뿐인가 (컷 전환·급회전 없음)
7. 배경 — 하늘·지형·건물이 생기지 않았는가

## 6. 권리·고지

- 형상 출처가 공공누리 1유형 3D 면 설명란·화면 하단에: `본 저작물은 <기관>에서 <연도>년 작성하여 공공누리 제1유형으로 개방한 '<자료명>'을 이용하였습니다.`
- 실측 없는 복원은 화면에 `추정 복원 / Reconstruction (interpretive)` 라벨.
- 업로드 시 유튜브 '변형·합성 콘텐츠' 자기 공개 체크. 편마다 카메라 경로·강조 대상을 바꾼다 (2026-07-16 비진정성 기준 회피).
- 라벨은 `AI Visual Reconstruction` 표기 규칙(D-003)을 따른다.

## 7. 비용 기준

컷당 24 credits (8초 720p) × 편당 2–3 = 48–72. 재생성은 §5 실패 시 1회만. 시험 단계(4회 96)는 EP01 에 계상.

---

## 미결 (사용자 결정 필요)

- 두 번째 인서트(황남대총 크기 비교) 착수 시점 — EP01 러프컷 전/후.
- 세로 9:16 인서트 (쇼츠) 는 같은 씬에 세로 카메라 추가로 파생 (PRODUCTION_PLAN Phase 5) — 별도 시험 필요 여부.
