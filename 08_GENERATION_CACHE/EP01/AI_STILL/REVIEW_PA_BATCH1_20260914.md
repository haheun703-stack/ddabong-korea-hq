# REVIEW — 파이프라인 A 배치 1 (8장, 2026-09-14, D-039)

폴더: `08_GENERATION_CACHE/EP01/AI_STILL/` · 원본: `02_SEASONS/S01/EP01/02_SOURCES/` · 승인 `APR_EP01_PA_002` 8/8 사용 · 16 credits (잔액 1674.58 → 1658.58) · 모델 Nano Banana 2 (D-036) · 전부 2752×1536.

| # | 샷 | 파일 | 원본 (CC0) | 봇 판정 | 메모 |
|---|---|---|---|---|---|
| 0 | S01_SH002 소나무 리빌 (→ S09_SH003 재사용) | `PA_S01_SH002_V01_0d7214c7.png` | MIETCHEN_PINE_001 | **PASS** | 소나무 줄기·봉분·낮은 울타리 유지, 흐린 낮, 사람 0 |
| 1 | S02_SH001 컷2 골짜기 | `PA_S02_SH001_CUT2_V01_56483502.png` | MIETCHEN_VALLEY_001 | **PASS** (note) | 배경에 기와지붕 공원 건물 1 — 현재 시점이라 허용 |
| 2 | S02_SH001 컷3 황남대총 | `PA_S02_SH001_CUT3_V01_d5c835b5.png` | HWANGNAMDAECHONG_GAGNON_001 | **PASS** | 쌍봉·연못·반영 유지 |
| 3 | S03_SH001 천마총 표지 | `PA_S03_SH001_V01_8af35906.png` | CHEONMACHONG_SIGN_MIETCHEN_001 | **PASS** | 天馬塚 세 글자 온전·판독 가능, 램프 유지 |
| 4 | S06_SH007 뒤에서 보는 봉분 | `PA_S06_SH007_V01_3f311e90.png` | MIETCHEN_MOUND_001 | **PASS** | 배롱나무·비석·벤치·광장 제거 성공, 은행나무 유지 |
| 5 | S06_SH011 봉분 + 관람객 | `PA_S06_SH011_V01_df608dab.png` | DAEREUNGWON_GAGNON_001 | **PASS** (minor) | 관람객 5명 뒷모습·작게 (요청 3–4명) |
| 6 | S08_SH003 매치컷 착지 | `PA_S08_SH003_V01_0f2174d1.png` | MIETCHEN_MOUND_001 | **PASS** (note) | 깨끗한 플레이트. 꼭대기 x≈0.42 (요청 0.58 — 오프축 방향 반대, "약간 오프축" 조건은 충족). `match_cut_frame` 은 이 이미지에서 잰다 |
| 7 | S09_SH004 석양 히어로 | `PA_S09_SH004_V01_f4dd6947.png` | DAEREUNGWON_GAGNON_001 | **PARTIAL** | 골든아워 빛은 성공. **지형 이탈**: 봉분 3기 → 4기, 앞에 넓은 자갈길 생김 ("exact landform" 실패). 엔딩 여운 컷이라 그대로 써도 무방 — 사용자 판단 |

**결과 요약**: PASS 7 · PARTIAL 1 (S09_SH004). 실패 0. 추가 호출 0.

**FIX 후보 (사용자 결정)**
- S09_SH004: 참고 이미지 유지 + "exactly three mounds as in the reference, no gravel foreground" 강조해 1회 재생성 (2 credits, D-030 위임 한도 안).
- S08_SH003: 오프축 방향을 오른쪽으로 바꾸고 싶으면 1회 재생성 (2 credits). 그대로 써도 됨.

**다음 (보류 2샷)**: S01_SH001 거리 · S08_SH001 몽타주 — 정지 이미지 + I2V (Kling 3.0, P-012 뒤).
