# 08_GENERATION_CACHE/EP01/BLENDER — 천마총 마스터 씬 렌더 (D-053 Phase 1)

생성: `blender -b --python tools/blender/build_cheonmachong.py -- --out 08_GENERATION_CACHE/EP01/BLENDER --save 04_BLENDER_LIBRARY/scenes/EP01_CHEONMACHONG_MASTER_V01.blend`
사양: `02_SEASONS/S01/EP01/10_BLENDER/SCENE_SPEC_CHEONMACHONG_V01.md`. PNG 는 git 제외(재생성 가능), 이 README 와 컨택트 시트 jpg 만 기록.

| 파일 패턴 | 내용 |
|---|---|
| `CAM_S0x_SHxxx_*_clay.png` | 샷 카메라 8개 클레이 (Higgsfield 실사화 참조) |
| `*_depth.png` | 깊이 정규화 (DepthFlow 패럴랙스) |
| `*_line.png` | 아웃라인 (도해 베이스) |
| `CAM_G04_SECTION_*` | 단면 컷어웨이 (X=0 절단) |
| `CAM_G05_BUILD_S1~S5_*` | 축조 단계 5 (아이소, 동일 프레임 = 시각 시계) |
| `CAM_G14_ELEVATION_clay.png` | 치수선 47 m / 12.7 m / 10 m 자 |
| `CAM_SHORTS_01~03_*` | 9:16 쇼츠 카메라 |
| `CONTACT_SHOTS_CLAY_V01.jpg` · `CONTACT_DIAGRAMS_V01.jpg` | 검수용 시트 |
