# 노동자·시종 복식 근거 검증 (D-053, 2026-09-16)

> 계기: D-052 원로(elite) 복식 검증에서 기존 lock 의 "반소매·V자 깊은 여밈·청동 과대·원추형 관모"가 시대착오/무근거로 드러나 정정됨. 같은 방법을 하위 계층(노동자·시종)에 적용.
> 방법: 웹 리서치(유료 도구 미사용, WebSearch/WebFetch만) → 신규 출처 11건을 `05_HISTORY_DATABASE/sources/` 에, 신규 주장 11건을 `05_HISTORY_DATABASE/facts/CLM_SILLA_COSTUME_021~031` 에 기록.
> 검증 대상 파일: `05_HISTORY_DATABASE/costumes/COSTUME_SILLA_LABORER_A01.json` (V01, 2026-09-11), `05_HISTORY_DATABASE/costumes/COSTUME_SILLA_ATTENDANT_A01.json` (V01, 2026-09-11).
> **본 문서는 판정만 담는다. lock JSON 수정은 소유자 승인 후 별도 커밋.**

---

## §1 검증 대상 요약 (현재 lock 속성)

### 1-1. COSTUME_SILLA_LABORER_A01 (봉분 조성 노동자 — 목재·돌 운반) / V01 / historical_basis: PROBABLE
| 속성 | 현재 lock 값 | lock 이 단 근거 |
|---|---|---|
| 재질 | 마직(삼베류) 평직, 무염 생지 | CLM_006 + CLM_002 |
| 상의 | 소매 좁은 저고리(유), 엉덩이선, 직령, 우임 / 노동 중 상체 노출 가능 | CLM_001, CLM_007 / CLM_003 |
| 하의 | 통 좁은 바지(고), 정강이·발목 끈 묶음 가능 | CLM_001 (묶음은 INTERPRETIVE) |
| 허리띠 | 포대(천 허리끈), 금속 장식 없음 | CLM_004 |
| 신발 | 짚신 또는 맨발 | CLM_005 |
| 머리 | 상투 + 천 수건 동여맴, 또는 맨상투 | CLM_003 |
| 색 | 백·흑·생지색, 공복 4색(자·비·청·황) 금지 | CLM_002 |
| 마모 | 먼지·땀·해진 자국 | ARTISTIC |

### 1-2. COSTUME_SILLA_ATTENDANT_A01 (장례 시종·장인) / V01 / historical_basis: PROBABLE
| 속성 | 현재 lock 값 | lock 이 단 근거 |
|---|---|---|
| 재질 | 노동자보다 고운 마직 또는 저포 평직 / 견직은 귀족 전용 | CLM_006 유추 / INTERPRETIVE |
| 상의 | 소매 좁은 저고리, 엉덩이선, 직령 우임, 노동자보다 정돈됨 | CLM_001, CLM_007 |
| 하의 | 통 좁은~중간 바지 / **여성 시종은 저고리+치마** | CLM_001 |
| 허리띠 | 포대(천 띠), 장식 최소 | CLM_004 |
| 신발 | 운두 낮은 이(履) 또는 짚신 | CLM_005 |
| 머리 | 상투 + 수건 또는 단순 건 | CLM_003 |
| 색 | 백·흑·회갈 등 무염 계열, 공복 4색 금지 | CLM_002 |
| 계급 표지 | 관등 없는 서민으로 상정 (과대·요패 없음) | CLM_004 |

---

## §2 출처 목록 (신규 11건 + 재사용 6건)

### 신규
| # | 출처 | 기관/저자 | 연도 | 등급 | URL |
|---|---|---|---|---|---|
| S1 | 신라 왕경인의 복식에 대한 고고학적 자료와 그 특성, 『영남고고학』 103, 229-254 | 김재열 | 2025 | **A** (학술논문/KCI) | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003246376 |
| S2 | 월간 국가유산사랑 「1500년 전 신라인의 생생한 몸짓과 표정 — 토우에 담긴 희로애락」 | 국가유산청 | n.d. | **A** (국가유산청) | https://www.cha.go.kr/cop/bbs/selectBoardArticle.do?nttId=92241&bbsId=BBSMSTR_1008&mn=NS_01_09_01 |
| S3 | 신편 한국사 8권 「4) 신라의 의생활」 | 국사편찬위원회 (우리역사넷) | n.d. | **A** (국가 편찬 통사) | https://contents.history.go.kr/mobile/nh/view.do?levelId=nh_008_0070_0010_0040 |
| S4 | 한국문화사 「경주 황남대총」 | 국사편찬위원회 (우리역사넷) | n.d. | **A** | https://contents.history.go.kr/mobile/kc/view.do?levelId=kc_r100044&code=kc_age_10 |
| S5 | 한국민족문화대백과사전 「백의민족」 (『수서』 신라전 인용) | 서봉하 / 한국학중앙연구원 | 2023 수정 | **B** (백과, 1차는 『수서』) | https://encykorea.aks.ac.kr/Article/E0022280 |
| S6 | 신라의 衣生活과 織物 생산 | 박남수 | 2011 | **A** (학술논문/KCI) | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001618129 |
| S7 | 황성동 출토 여성토우의 복식 고증과 돌 코스튬 응용디자인 연구, 『복식』 61(7) 67-79 | 최정 | 2011 | **A** (학술논문) | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201131242951202 |
| S8 | 한국 전통복식 여밈의 변화와 미적 특성, 『한국의류학회지』 42(6), DOI 10.5850/JKSCT.2018.42.6.924 | 김소희 (숙명여대) | 2018 | **A** (학술논문) | https://koreascience.kr/article/JAKO201811459665537.pdf |
| S9 | 국보 「도기 기마인물형 명기」 (신라 5세기, 금령총) | 국가유산청 국가유산포털 | 1962 지정 | **A** (국가유산청) | https://www.heritage.go.kr/heri/cul/culSelectDetail.do?pageNo=1_1_1_1&ccbaCpno=1111100910000 |
| S10 | 사료로 본 한국사 「흥덕왕의 사치 금령 조치」 (834) | 국사편찬위원회 | n.d. | **A** | https://contents.history.go.kr/front/hm/view.do?levelId=hm_036_0020&tabId=01&treeId=010303 |
| S11 | 『삼국사기』 권33 잡지2 색복 — 평인·평인녀 조 | 김부식(1145) / 국사편찬위 한국사DB | 1145 | **A** (1차 사료) | https://db.history.go.kr/ancient/level.do?levelId=sg_033r_0020_0130 |

### 재사용 (D-011·D-052 등록분)
| # | 출처 | 등급 |
|---|---|---|
| R1 | SRC_NMK_GEUMNYEONGCHONG_RIDER_001 — 기마 인물형 토기, 국립중앙박물관 소장품 (주인/하인상 기술) | A |
| R2 | SRC_KCULTURE_SILLA_TOU_001 — 전통문화포털 부상 토우 (국립경주박물관) | B |
| R3 | SRC_KHAN_STRAW_SHOE_POTTERY_001 — 짚신 모양 토기 (경향신문 2023) | C (1차는 박물관 유물) |
| R4 | SRC_NAHF_SILLA_CLOTHING_001 — 우리역사넷 신라 복식 | A |
| R5 | SRC_KPEA_CHEONMACHONG_TEXTILE_001 — 천마총 출토 직물 | A |
| R6 | SRC_NAHF_GOGURYEO_MURAL_DRESS_001 — 우리역사넷 고구려 복식 (**유추 전용**) | A |

> 위키피디아는 어느 판정에도 단독 근거로 쓰지 않았다. 「백의민족」 관련 위키 항목은 『수서』 원문 → 한국민족문화대백과(S5) → 신편 한국사(S3)로 추적해 대체했다.

---

## §3 주장 표 (속성별 판정)

### 3-1. 노동자 (COSTUME_SILLA_LABORER_A01)

| # | 속성 | 현재 lock 값 | 판정 | 근거 | 정정 제안값 |
|---|---|---|---|---|---|
| L1 | 재질 (마직 평직) | 마직(삼베류) 평직, 무염 생지 | **PROBABLE** | S6, R5 (CLM_030) | "거칠고 표백되지 않은 평직" 으로 기술. **섬유 종류(마/저) 단정은 삭제** — 신라 직물 위계는 섬유가 아니라 직조법·표백도·염색 차수로 정해짐(S6) |
| L2 | 상의 기본형 (유+고) | 소매 좁은 저고리, 엉덩이선 | **CONFIRMED** | R4, S3 (CLM_001) | 유지 |
| L3 | 소매 길이 | (좁은 소매, 길이 명시 없음) | **PROBABLE** | S3 (삼국 공통 유=긴소매), 원로 V02 정정과 동일 | "긴소매" 를 명시 — 원로 lock V02 와 동일 규칙. 반소매 금지 |
| L4 | 여밈 방향 (직령 **우임**) | 직령, 우임 고정 | **INTERPRETIVE** | S8, R4 (CLM_028) | "직령교임(얕은 교차). 우임 우세, 좌임 허용" 으로 완화. **우임 '고정'은 조선기 현상이라 5~6세기에 강제 불가**. 옷고름 표현 금지 |
| L5 | 상체 노출 | "노동 중 상체 노출 가능 — PROBABLE" | **INTERPRETIVE** (강등) | S9, R1, S1 (CLM_022) | 금령총 하인상은 **부장 명기(明器)의 신분 표현 관습**. 실제 노동복 증거 아님 → PROBABLE → INTERPRETIVE, 상시 노출 금지·1~2컷 한정 + hedge |
| L6 | 하의 (통 좁은 바지) | 통 좁은 바지(고) | **PROBABLE** | R4, S3 (CLM_001) | 유지 |
| L7 | 바지 정강이·발목 끈 묶음 | "가능" | **UNSUPPORTED** | 신라 자료 없음. 고구려 벽화 유추 시 R6 근거로 INTERPRETIVE 표기 필수 | 근거 없음 명시. 사용 시 "고구려 벽화 유추(INTERPRETIVE)" 라벨 |
| L8 | 허리띠 (포대, 금속 없음) | 천 허리끈, 금속 장식 없음 | **PROBABLE** | CLM_004, S8 (대가 주된 여밈 수단), S1 | 유지. 단 『삼국사기』 평인 "동·철 허리띠"(S11)는 **834년 규정이므로 인용 금지** |
| L9 | 신발 — 짚신 | 짚신 | **PROBABLE** | R3 (CLM_031) | 유지하되 "**서민 전용**" 함의 제거 — 짚신 모양 토기는 의례용 이형토기라 착용 계층 특정 불가 |
| L10 | 신발 — 맨발 | "또는 맨발" | **UNSUPPORTED** | 직접 증거 없음 | 삭제하거나 INTERPRETIVE 로 강등 |
| L11 | 머리 — 상투 | 상투 | **CONFIRMED** | S2 ("상투 튼 남자" 토우), R1 (CLM_023) | 유지 |
| L12 | 머리 — 천 수건 동여맴 | "천 수건, PROBABLE" | **INTERPRETIVE** (강등) | S3 (黑巾은 6세기 이후 기록), R1 (명기) (CLM_027) | 유지 가능하나 등급 강등. "5세기 직접 증거 없음" 주석 |
| L13 | 색 (백·흑·생지) | 백·흑·생지색 | **PROBABLE** | S5, S3 (CLM_025) | 유지하되 **근거를 CLM_002(법흥왕 공복색)에서 CLM_025(『수서』 백색 숭상)로 교체**. 내레이션에서 "백의민족" 용어 금지 |
| L14 | 공복 4색 금지 | 자·비·청·황 금지 | **CONFIRMED** | CLM_002, CLM_019 | 유지 (520년 이후 제도라 5세기 장면에서는 언급 자체 금지) |
| L15 | 계급 구분 표지 | (색·재질 차이로만 표현) | **정정 필요 / PROBABLE** | S1 (CLM_021) | **"갖춤의 양(요소 수)"이 1차 위계 표지** — 노동자는 관모 없음·허리띠 단순·신발 생략 등 요소를 빼는 방식으로 구분. 색/재질 차이보다 이쪽을 우선 |
| L16 | 마모·때 (lived-in) | ARTISTIC | **ARTISTIC** (유지) | — | 유지 |
| L17 | 장면 규모(부수 정보) | (lock 에 없음) | **PROBABLE** | S4 (CLM_024) | 황남대총 남분급 = 하루 300명×121일. 군중 컷 인원 밀도·공정(나무틀→돌무지 4m→봉토) 설계에 사용 |

### 3-2. 시종 (COSTUME_SILLA_ATTENDANT_A01)

| # | 속성 | 현재 lock 값 | 판정 | 근거 | 정정 제안값 |
|---|---|---|---|---|---|
| A1 | 재질 (고운 마직/저포) | 노동자보다 고운 마직 또는 저포 | **PROBABLE** | S6 (CLM_030) | "더 고르게 짠 평직, 표백도가 높음" 으로 기술 변경. 섬유 종류 단정 삭제 |
| A2 | "견직은 귀족 전용" | INTERPRETIVE | **INTERPRETIVE** (유지) | S6 — 왕실 공방 기술이 귀족 공방으로 전파, 이분법 아님 | 등급 유지, 단 "귀족 전용" → "상위 계층에 집중" 으로 완화 |
| A3 | 상의 기본형 | 소매 좁은 저고리, 직령 우임 | **CONFIRMED**(기본형) / **INTERPRETIVE**(우임 고정) | R4, S3 / S8 (CLM_028) | L4 와 동일 — 직령교임, 좌임 허용 |
| A4 | 소매 길이 | (명시 없음) | **PROBABLE** | S3 | "긴소매" 명시, 반소매 금지 (반비는 834년 최초 기록 — CLM_015) |
| A5 | 하의 (남성) | 통 좁은~중간 바지 | **PROBABLE** | R4 (CLM_001) | 유지 |
| A6 | **여성 시종 = 저고리+치마** | PROBABLE | **INTERPRETIVE** (강등) | S2("저고리를 입은 여자" 토우)는 세부 판별 불가(CLM_023); S7 황성동 여성토우는 **7세기 후반** | 기본형(유+상)은 유지하되 등급 강등. **높은 허리선·이중치마·쪽머리는 금지** |
| A7 | 여성 머리모양 | (lock 미기재) | **ANACHRONISTIC** (사용 시) | S7 (CLM_029) | 황성동식 "가르마 있는 쪽머리" 금지. S3 의 "辮髮하여 머리를 두름"이 그나마 근접하나 6세기 이후 기록 → INTERPRETIVE |
| A8 | 허리띠 (포대, 장식 최소) | 천 띠 | **PROBABLE** | CLM_004, S1, S8 | 유지. 금속 과판·요패 금지 (무관등) |
| A9 | 신발 (운두 낮은 이/짚신) | 이(履) 또는 짚신 | **PROBABLE** | CLM_005, R3 (CLM_031) | 유지. 발목 덮는 화(靴)는 관원·귀족 표지이므로 시종 금지 |
| A10 | 머리 — 상투+수건/건 | PROBABLE | **INTERPRETIVE** (강등) | S3, R1 (CLM_027) | L12 와 동일 |
| A11 | 색 (백·흑·회갈) | 무염 계열 | **PROBABLE** | S5, S3 (CLM_025) | 유지, 근거 교체 |
| A12 | 계급 표지 (무관등 서민 상정) | 과대·요패 없음 | **PROBABLE** | S1 (CLM_021), CLM_004 | 유지 + "요소 생략의 정도"로 노동자와 차등(시종 = 갖춤 제한, 노동자 = 갖춤 최소) |
| A13 | 복두(幞頭)·동철 대구 | (lock 에 없음 — 확인용) | **ANACHRONISTIC** | S10, S11 (CLM_026) | 금지 목록에 명시 추가. 『삼국사기』 평인 규정은 834년 것 |
| A14 | 손·소매 끝 디테일 (H03) | KEEP 대상 | 판정 대상 아님 | — | 소매 끝 선(襈) 없음 유지 (원로 V02 와 동일) |

**판정 집계**: CONFIRMED 4 · PROBABLE 14 · INTERPRETIVE 9 · UNSUPPORTED 2 · ANACHRONISTIC 2 · ARTISTIC 1 (총 32항)

---

## §4 정정 권고 요약

- **소매 길이를 "긴소매"로 명시** — 노동자·시종 모두. 반소매(반비)는 834년 최초 기록이라 원로와 같은 기준으로 금지.
- **"직령 우임" → "직령교임, 우임 우세·좌임 허용"** — 고대에는 좌·우임이 공존했고 우임 고정은 조선기 현상(S8). 옷고름 표현 금지.
- **노동자 상체 노출을 PROBABLE → INTERPRETIVE 로 강등** — 금령총 하인상은 부장 명기의 신분 표현 관습이지 노동복 기록이 아님(S9, R1, S1).
- **계급 구분의 1차 표지를 "색·재질"에서 "갖춤의 양(요소 수)"으로 변경** — 원로=일습, 시종=갖춤 제한, 노동자=갖춤 최소(S1).
- **섬유 종류 단정(마직/저포) 삭제** — 신라 직물 위계는 재료보다 직조법·표백도·염색 차수로 정해짐(S6). "거친 무표백 평직 / 고른 표백 평직"으로 기술.
- **여성 시종 복식을 PROBABLE → INTERPRETIVE 로 강등하고 황성동식 요소 금지** — 황성동 여성토우는 7세기 후반 자료(S7).
- **머리 수건(두건)을 PROBABLE → INTERPRETIVE 로 강등** — 黑巾 기록은 6세기 이후(S3). 상투 자체는 토우로 뒷받침되어 CONFIRMED 유지.
- **"맨발" 옵션 삭제 또는 INTERPRETIVE 강등**, 짚신에서 "서민 전용" 함의 제거(R3).
- **바지 발목 끈 묶음은 UNSUPPORTED** — 사용 시 "고구려 벽화 유추(INTERPRETIVE)" 라벨 필수(R6).
- **금지 목록에 복두(幞頭)·동철제 대구 추가** — 『삼국사기』 평인 규정은 834년(S10, S11).
- **색 근거를 CLM_002 → CLM_025 로 교체**하고, 내레이션에서 "백의민족"·"관등색" 용어 금지.
- **부수**: 봉분 축조 군중 컷 규모는 하루 300명×121일(황남대총 남분급)을 기준으로 설계(S4).

---

## §5 불확실 항목과 그 이유

| 항목 | 불확실 사유 | 보완 경로 |
|---|---|---|
| 노동자 상의의 실제 길이·품 | 토우 크기 2~10cm — 세부 판별 불가(S2). 명기는 이상화된 표현 | 권준희 2001 「고신라기 토우에 나타난 복식 연구」(『복식』 51-4, DBpia 유료) 본문 |
| 신라 하위 계층의 여밈 방향 실측 | S8 은 통사 관점이며 5~6세기 신라 개체 표본 미제시 | 김재열 2025 본문(KCI 유료) 도판 — 초록만 열람함 |
| 5세기 노동자·시종의 두건 유무 | 黑巾 기록은 『양서』·『남사』·『수서』 계열로 6세기 이후 편찬(S3). 금령총 하인상 수건은 명기 관습 | 쪽샘지구·월성로 토우 개별 소장품 레코드(e뮤지엄) |
| 실제 착용 섬유·염료 | 천마총·황남대총 직물 분석은 귀족 부장품 중심. 서민 복식 잔존물 없음 | 1974 『천마총 발굴조사보고서』 PDF, 2019 『천마총, 발굴조사의 기록』 |
| 여성 시종의 존재 여부·역할 | 장례 시종에 여성이 포함됐는지 5~6세기 직접 기록 없음 | 김재열 2025 본문, 신라 상장례 연구 |
| 짚신 착용 계층 | 짚신 모양 토기는 의례용 이형토기라 계층 특정 불가(R3) | 국립경주박물관 이형토기 소장품 해설 |
| 맨발 표현 | 토우·명기에서 맨발 여부를 계층 지표로 다룬 연구 미확인 | 김재열 2025, 권준희 2001 |
| 『삼국사기』 색복 평인 조 원문 | 한국사DB 해당 세부 항목 직접 열람 실패(6두품녀 조만 노출) — 검색 요약 기준으로 기록(S11) | db.history.go.kr 색복조 평인 항목 levelId 재탐색 |

---

## 산출 파일
- 본 문서: `02_SEASONS/S01/EP01/01_RESEARCH/COSTUME_LABOURER_ATTENDANT_VERIFY_20260916.md`
- 신규 주장 11건: `05_HISTORY_DATABASE/facts/CLM_SILLA_COSTUME_021.json` ~ `CLM_SILLA_COSTUME_031.json`
- 신규 출처 11건: `05_HISTORY_DATABASE/sources/` (SRC_KIM_JAEYEOL_WANGGYEONG_001, SRC_CHA_TOU_HEARTFELT_001, SRC_NAHF_SILLA_LIFE_DRESS_001, SRC_NAHF_HWANGNAMDAECHONG_001, SRC_AKS_ENCYKOREA_BAEKUI_001, SRC_PARK_NAMSU_TEXTILE_001, SRC_CHOI_JUNG_HWANGSEONG_FIGURINE_001, SRC_KIM_SOHEE_YEOMIM_001, SRC_KHERITAGE_RIDER_NT91_001, SRC_NAHF_HEUNGDEOK_SUMPTUARY_001, SRC_SAMGUKSAGI_SAEKBOK_PYEONGIN_001)
- 검증: `python 00_SYSTEM/schemas/validate.py` → 498/498 passed, cross-reference OK
- 미수행(승인 대기): `05_HISTORY_DATABASE/costumes/COSTUME_SILLA_LABORER_A01.json` / `COSTUME_SILLA_ATTENDANT_A01.json` 의 V02 패치, lock 발행, 커밋
