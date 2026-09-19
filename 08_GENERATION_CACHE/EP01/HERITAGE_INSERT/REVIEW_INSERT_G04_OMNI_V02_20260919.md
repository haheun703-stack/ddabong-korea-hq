# 검수 — 유적 인서트 V02 (D-058 보정 재생성, 2026-09-19)

입력: `CAM_G04_SECTION_tech.png` (비례 단서 1.7 m 인물 + 6.6 m 바, 지면 평면 Freestyle 제외). 모델 `gemini_omni_flash_1_1` 8초 720p, **24 credits** (누적 48). 출력 `INSERT_G04_SECTION_OMNI_V02_96b1a461.mp4`, 시트 `QC_INSERT_G04_OMNI_V02_12FRAMES.jpg`.

## 판정: 기하 PASS · 규칙 FAIL 1건 (V03 필요)

| 항목 | V01 | V02 |
|---|---|---|
| 목곽/봉분 비례 | ~1/4 ✗ | **~1/7 ✅ (FACT 6.6/47)** |
| 층 순서 목곽→돌→흙 | ✅ | ✅ |
| 구조선 연속 | ✅ | ✅ 8초, 4.7s 부터 반투명 3D 컷어웨이 궤도 — 레퍼런스 문법 그대로 |
| 지면 프레임 선 | ✗ | ✅ 없음 |
| 비례 인물 | 없음 | ✅ 왼쪽 밑동 정지 |
| **화면 내 글자** | 없음 ✅ | **✗ 모델이 치수 라벨을 직접 그림** (47 m · 12.7 m · 6.6 m · 1.7 m, 밑동에 1.8 m 로 보이는 것 1). 숫자는 프롬프트 값과 일치·판독 가능하지만 `HERITAGE_INSERT` 규칙 = 라벨은 편집 오버레이만 |

## 원인
프롬프트에 치수를 숫자로 적자(비례를 가르치려고) 모델이 그 숫자를 라벨로 렌더했다. 뒤의 no text, no labels 보다 앞의 수치 서술이 더 강하게 작용.

## V03 처방 (승인 필요, 24 credits)
- 수치 유지 + 본문 지시로 **Do not render any numbers, measurement labels, dimension lines or arrows; convey scale only through the silhouette.** 명시.
- 대안: 숫자를 빼고 비례를 말로만 (the chamber is about one seventh of the mound width).
- V03 통과 시 레시피 확정 (P-015 #7). 라벨은 편집에서 얹는다.
