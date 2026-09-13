# -*- coding: utf-8 -*-
"""Generate EP01 scene_*.json / shot_*.json from the approved roughcut timeline (episodes/ep01-premiere-roughcut.html)."""
import json, sys
from pathlib import Path

OUT = Path(sys.argv[1])
TODAY, BY = "2026-09-11", "Claude Code (Continuity Engine)"
DT, CH, MU, DW = "LOC_GYEONGJU_DAEREUNGWON_V01", "LOC_CHEONMACHONG_V01", "LOC_GYEONGJU_NATIONAL_MUSEUM_V01", "LOC_GYEONGJU_DOWNTOWN_V01"
OBS, LAB, ATT = "CHAR_SILLA_ELITE_OBSERVER_01", "CHAR_SILLA_LABORER_GROUP_01", "CHAR_SILLA_ATTENDANT_GROUP_01"
COSTUME = {OBS: "COSTUME_SILLA_ELITE_A01", LAB: "COSTUME_SILLA_LABORER_A01", ATT: "COSTUME_SILLA_ATTENDANT_A01"}
KEEP_PERSON = ["face_identity", "body_proportion", "hair", "costume", "height_ratio"]
KEEP_GROUP = ["costume", "era_lock", "location_lock", "height_ratio"]
KEEP_MATCH = ["mound_silhouette", "frame_position", "horizon_height"]
AIVR, IR = "AI Visual Reconstruction", "INTERPRETIVE RECONSTRUCTION"
R, A, G, H = "REAL_SHOOT", "ARCHIVE", "ORIGINAL_GRAPHIC", "HIGGSFIELD"
SE, EX, PD, NO = "SILLA_EARLY", "EXCAVATION_1973", "PRESENT_DAY", "NONE"
ROUTE_NOTE = "파이프라인은 legacy 팩 태그 그대로 (잠정). P4 Visual Router 에서 재판정."
FLOW_NOTE = "운반·작업·의례 준비 동작은 정본 §6 상 Flow/Veo 영역 → P4 에서 BLENDER_FLOW 재검토."

# (scene_no, title, beat, era, location, tc_range, script_section, [shots])
# shot: (in, out, pipeline, era, location, confidence, purpose, chars, (cc, sa, hm, vi), must_keep, ai_label, notes)
SCENES = [
 (1, "Cold Open — 도시 한가운데 거대한 봉분", "QUESTION", PD, DT, "0:00–0:42", "script v2 0:00–0:35 COLD OPEN", [
  ("0:00", "0:08", R, PD, DW, "FACT", "현대 경주 거리 — 봉분은 아직 안 보이거나 일부만", [], (20, 30, 30, 60), [], None, "field-shoot A1. 현장음 1초 먼저."),
  ("0:08", "0:18", R, PD, DT, "FACT", "카페/도로에서 봉분 리빌, 사람으로 크기 비교", [], (35, 50, 30, 90), ["mound_silhouette"], None, "REAL 우선순위 1–3. 이 구도는 EP01_S09_SH003 에서 다시 쓴다 → 렌즈·위치 기록 필수."),
  ("0:18", "0:25", G, PD, DT, "FACT", "G01 질문 카드 — 봉분 와이드 위 타이틀", [], (5, 10, 0, 80), [], None, "G01. 배경 V1 = 봉분 와이드 실사 (SH002 연장)."),
  ("0:25", "0:42", G, PD, NO, "FACT", "G02 Korea → Gyeongju → SILLA CAPITAL 지도", [], (10, 70, 0, 60), [], None, "G02. research-v2 S1."),
 ]),
 (2, "FACT — 여기엔 실제로 무엇이 있나", "FACT", PD, DT, "0:42–1:25", "script v2 0:35–1:25", [
  ("0:42", "0:53", R, PD, DT, "FACT", "왕릉군·월성·사찰 등 역사경관 3–4컷", [], (25, 40, 10, 60), [], None, "넓은 클러스터 촬영분 활용 (정본 §19). S1."),
  ("0:53", "1:05", G, PD, DT, "FACT", "G03 왕릉군 개념도 (자체 단순화 도식)", [], (10, 60, 0, 55), [], None, "G03. UNESCO '왕릉군 3개 그룹' (S1). GIS 복제 금지."),
  ("1:05", "1:25", A, SE, MU, "FACT", "유물 몽타주 금관 → 유리잔 → 말다래 (컷당 1–1.5초)", [], (5, 20, 0, 75), [], None, "visual-assets B1/B4 GREEN, B5 YELLOW (개별 라이선스 확인 전 사용 금지). S1/S3. [불일치 X1] 대본 v2 는 이 구간에 G04 단면 그래픽도 있으나 러프컷에는 없음."),
 ]),
 (3, "천마총 — 1973년 발굴과 이름의 유래", "FACT", EX, CH, "1:25–2:15", "script v2 1:25–2:15 CASE STUDY", [
  ("1:25", "1:38", R, PD, CH, "FACT", "천마총 외관·표지·입구", [], (20, 50, 10, 70), [], None, "촬영 허가 확인. 백업 A3 (CC BY-SA, YELLOW)."),
  ("1:38", "1:53", A, EX, CH, "FACT", "1973 조사단·발굴현장 흑백사진", [], (5, 30, 0, 85), [], None, "archive-photos (NRICH). 사진마다 라이선스 확인 (C1 YELLOW). S3."),
  ("1:53", "1:58", A, EX, CH, "FACT", "유물 수습 현장 사진", [], (5, 20, 0, 70), [], None, "S3: 11,526점 수습."),
  ("1:58", "2:04", A, SE, MU, "FACT", "금관 → 천마도", [], (5, 10, 0, 90), [], None, "B1 금관 KOGL 1유형, B4 천마도 PD. S3/S6."),
  ("2:04", "2:15", G, NO, NO, "FACT", "G06 WHO WAS BURIED HERE? / UNKNOWN WITH CERTAINTY", [], (5, 0, 0, 80), [], None, "G06. S4 피장자 불확실. 미스터리 연출 과하게 하지 않기. [불일치 X2] 대본 v2 문구는 'OCCUPANT: UNCERTAIN'."),
 ]),
 (4, "무덤은 공사였다 — 조성 과정", "CONTEXT", SE, CH, "2:15–3:15", "script v2 2:15–3:15", [
  ("2:15", "2:24", A, EX, CH, "FACT", "구조가 드러난 발굴현장 사진", [], (5, 40, 0, 70), [], None, "실제 자료 → AI 순서 (팩 편집 원칙)."),
  ("2:24", "2:32", G, SE, CH, "FACT", "G04 적석목곽 단면 — 관 → 목곽 → 돌무지 → 흙 봉분", [], (15, 90, 0, 85), [], None, "G04. 치수·층 순서는 LOC_CHEONMACHONG_V01.spatial_lock (S3). 박물관 도면 트레이싱 금지."),
  ("2:32", "2:48", G, SE, CH, "FACT", "G05 무덤 조성 4단계", [], (15, 85, 0, 75), [], None, "G05. H01/H02/H03 과 연결."),
  ("2:48", "2:54", H, SE, CH, "PROBABLE", "H01 목재 준비 — 무덤이 '공사'였다는 감각", [LAB], (45, 60, 70, 70), KEEP_GROUP, AIVR, "H01 프롬프트 APPROVED (legacy 팩). 6초 (D-009). " + FLOW_NOTE),
  ("2:54", "3:00", H, SE, CH, "PROBABLE", "H02 돌 운반 — 규모와 노동력", [LAB], (55, 70, 75, 75), KEEP_GROUP, AIVR, "H02. 6초 (D-009). 봉분은 일부만 형성된 상태. " + FLOW_NOTE),
  ("3:00", "3:06", H, SE, CH, "PROBABLE", "H02 조직된 작업 와이드", [LAB], (40, 75, 60, 70), KEEP_GROUP, AIVR, "H02 프롬프트 재사용, 6초 (D-009). SH005 와 같은 생성본에서 잘라 쓸 수 있으면 유료 호출 1회 절약 → 라우터 판단."),
  ("3:06", "3:15", A, EX, CH, "FACT", "실제 발굴사진으로 복귀", [], (5, 30, 0, 60), [], None, "AI 끝나면 실제 자료로 복귀, 음악 안정."),
 ]),
 (5, "금이 말해주는 것 — 신성함·정통성·권위", "CONTEXT", SE, MU, "3:15–4:20", "script v2 3:15–4:20", [
  ("3:15", "3:36", A, SE, MU, "FACT", "금관·관모·금허리띠·가슴걸이 몽타주", [], (5, 10, 0, 85), [], None, "B1/B3 GREEN, 나머지는 개별 확인. S2."),
  ("3:36", "3:52", G, NO, NO, "FACT", "G07 SACREDNESS · LEGITIMACY · AUTHORITY", [], (5, 0, 0, 90), [], None, "G07. 출처 라벨 Gyeongju National Museum (S2). 에피소드 핵심 문장."),
  ("3:52", "4:00", A, EX, CH, "FACT", "허리띠 출토현장", [], (5, 30, 0, 65), [], None, "사실 → 현재 연결."),
  ("4:00", "4:08", A, SE, MU, "FACT", "현재 유물 (허리띠)", [], (5, 10, 0, 65), [], None, "B3 KOGL 1유형."),
  ("4:08", "4:12", H, SE, CH, "PROBABLE", "H03 부장품 준비 — '무엇을 넣을지 골랐다'", [ATT], (35, 50, 40, 75), KEEP_GROUP, AIVR, "H03. 손·천·금속·유리 클로즈업. 금 유물 형태는 실제 B1/B3 참조, 판타지 보석 금지. 4초."),
  ("4:12", "4:20", A, SE, MU, "FACT", "실제 금관으로 하드컷", [], (5, 10, 0, 80), [], None, "실제 유물이 문장 끝을 받는다."),
 ]),
 (6, "사고방식 재구성 — 대화가 아니라 문제를 재구성한다", "MINDSET", SE, CH, "4:20–5:20", "script v2 4:20–5:20", [
  ("4:20", "4:27", G, NO, NO, "FACT", "G08 FACT / CONTEXT / INTERPRETATION", [], (5, 0, 0, 80), [], None, "G08. DDABONG 방법론 카드."),
  ("4:27", "4:33", H, SE, CH, "INTERPRETIVE", "H04 장례 준비 — 역할별 배치로 위계를 보여줌 (핵심 순간)", [OBS, ATT, LAB], (40, 80, 50, 85), KEEP_PERSON, AIVR, "H04. 6초 핵심 컷 (D-009, 원래 16초). 반복 인물 등장 → master_frame EP01_S06_MASTER 필요 (P2). " + FLOW_NOTE),
  ("4:33", "4:38", A, EX, CH, "FACT", "1973 목곽·매장 공간 발굴사진 — 재현 뒤 실제 증거", [], (5, 40, 0, 65), [], None, "D-009 채움 컷 (H04 분할분). 편집 시 다른 실제 자료로 교체 가능."),
  ("4:38", "4:43", A, SE, MU, "FACT", "금제 장신구 디테일 — 사람은 가도 지위의 표시는 남는다", [], (5, 10, 0, 65), [], None, "D-009 채움 컷 (H04 분할분). 권리 GREEN 파일만."),
  ("4:43", "4:49", H, SE, CH, "INTERPRETIVE", "H05 관찰자 시점 — 사람 머릿속이 아니라 '문제 상황' (핵심 순간)", [OBS, LAB, ATT], (60, 85, 50, 100), KEEP_PERSON, IR, "H05 채널 차별점 핵심 컷. 6초 (D-009, 원래 15초). 카메라는 관찰자 뒤 → 뒷모습·어깨 실루엣 연속성이 핵심. AI Visual Reconstruction + INTERPRETIVE RECONSTRUCTION 둘 다 표시."),
  ("4:49", "4:54", A, SE, MU, "FACT", "금관 디테일 — rank · legitimacy · authority", [], (5, 10, 0, 75), [], None, "D-009 채움 컷 (H05 분할분). S2."),
  ("4:54", "4:58", R, PD, DT, "FACT", "현재 봉분을 멀리서 바라보는 시점 — H05 시선을 실사로 이어받기", [], (20, 50, 10, 70), [], None, "D-009 채움 컷 (H05 분할분). 현장 촬영 시 H05 와 비슷한 '뒤에서 바라보는' 구도로."),
  ("4:58", "5:03", G, NO, NO, "FACT", "NO DIRECT QUOTATION 카드", [], (5, 0, 0, 70), [], None, "G08 계열 신뢰 카드 (대본 v2 그래픽 목록 #8)."),
  ("5:03", "5:10", A, EX, CH, "FACT", "실제 발굴사진", [], (5, 30, 0, 60), [], None, "추측의 한계를 보여준 뒤 증거로 복귀."),
  ("5:10", "5:16", H, SE, CH, "PROBABLE", "H06 거의 완성된 봉분 와이드 — 권위가 '보이는 형태'가 됨", [ATT], (30, 90, 20, 85), KEEP_GROUP, AIVR, "H06. 6초 (D-009, 원래 10초). 봉분 스케일 47 m / 12.7 m 준수. 멀리 선 소그룹 → 얼굴 안 보임."),
  ("5:16", "5:20", R, PD, DT, "FACT", "현재 봉분과 관람객 — 지금도 산 사람들에게 보이는 봉분", [], (15, 40, 20, 65), [], None, "D-009 채움 컷 (H06 분할분). 관람객 얼굴 식별 불필요."),
 ]),
 (7, "금관의 의미가 바뀐다", "CHOICE", SE, MU, "5:20–6:05", "script v2 5:20–6:05", [
  ("5:20", "5:38", A, SE, MU, "FACT", "박물관 조명 아래 금관", [], (5, 10, 0, 90), [], None, "전시실 맥락 촬영은 권리 허용 시에만."),
  ("5:38", "5:45", A, EX, CH, "FACT", "출토 현장", [], (5, 30, 0, 65), [], None, "과거/현재 대비."),
  ("5:45", "5:52", A, SE, MU, "FACT", "금관", [], (5, 10, 0, 75), [], None, None),
  ("5:52", "6:05", A, SE, MU, "FACT", "금관 디테일 홀드 (+ 질문 자막 1줄 선택)", [], (5, 10, 0, 85), [], None, "문장 뒤 0.5초 여백. [불일치 X3] 대본 v2 에는 관람객 REAL 컷과 금관 위치 단면 그래픽도 있으나 러프컷에는 없음."),
 ]),
 (8, "현대 경주 — 도시가 무덤 곁에 산다", "LEGACY", PD, DT, "6:05–6:30", "script v2 6:05–6:40", [
  ("6:05", "6:20", R, PD, DT, "FACT", "산책·사진·차량·카페 몽타주", [], (25, 30, 40, 70), [], None, "현장음 다시 앞으로."),
  ("6:20", "6:25", H, SE, DT, "PROBABLE", "H07 과거 봉분 — 매치컷 셋업", [], (10, 95, 0, 90), KEEP_MATCH, AIVR, "H07 + G10. 정본 §6 상 Higgsfield 에 맞는 컷 (과거→현재 매치컷). SH003 실사 구도를 먼저 찍고 그 구도에 맞춰 생성 (Generate Late)."),
  ("6:25", "6:30", R, PD, DT, "FACT", "현재 봉분 — 매치컷 착지 (G10)", [], (10, 95, 0, 90), KEEP_MATCH, None, "G10. 삼각대 고정, 봉분은 약간 오프축. 구도를 LOC_GYEONGJU_DAEREUNGWON_V01.spatial_lock.match_cut_frame 에 기록."),
 ]),
 (9, "클로징 — 왜 이렇게 지은 것이 그들에게 말이 됐나", "LEGACY", PD, DT, "6:30–7:05", "script v2 6:40–7:05", [
  ("6:30", "6:36", A, EX, CH, "FACT", "발굴 (3단 교차 ①)", [], (5, 20, 0, 60), [], None, "[불일치 X4] 대본 v2 는 이 구간에 HIGGSFIELD 공사 플래시 2–3초, 러프컷은 아카이브/유물/실사 3단 교차."),
  ("6:36", "6:42", A, SE, MU, "FACT", "금관 (3단 교차 ②)", [], (5, 10, 0, 70), [], None, None),
  ("6:42", "6:48", R, PD, DT, "FACT", "현재 봉분 — 오프닝 구도 회수 (3단 교차 ③)", [], (15, 40, 0, 75), ["mound_silhouette"], None, "EP01_S01_SH002 구도 회수."),
  ("6:48", "6:59", R, PD, DT, "FACT", "석양·골든아워 왕릉 히어로 와이드", [], (20, 40, 0, 95), [], None, "엔딩 여운."),
  ("6:59", "7:05", G, NO, NO, "FACT", "G11 엔드카드 → G12 출처 슬레이트", [], (5, 0, 0, 60), [], None, "G11/G12. 실제 사용한 파일만 크레딧."),
 ]),
]

def sec(tc):
    m, s = tc.split(":"); return int(m) * 60 + int(s)

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

OUT.mkdir(parents=True, exist_ok=True)
scene_ids, n_shots = [], 0
for no, title, beat, era, loc, tc, section, shots in SCENES:
    sid = f"EP01_S{no:02d}"; scene_ids.append(sid)
    shot_ids, scene_chars = [], []
    for i, (tin, tout, pipe, sera, sloc, conf, purpose, chars, (cc, sa, hm, vi), keep, label, note) in enumerate(shots, 1):
        shid = f"{sid}_SH{i:03d}"; shot_ids.append(shid)
        scene_chars += [c for c in chars if c not in scene_chars]
        notes = [f"TC {tin}–{tout} (러프컷 v1 기준, 내레이션 녹음 후 조정)."]
        if note: notes.append(note)
        if pipe == H and ROUTE_NOTE not in (note or ""): notes.append(ROUTE_NOTE)
        notes.append("점수(camera_complexity 등)는 Continuity Engine 추정치 — P4 라우터에서 확정.")
        dump(OUT / f"shot_{shid}.json", {
            "shot_id": shid, "scene_id": sid, "episode_id": "EP01",
            "duration": sec(tout) - sec(tin), "purpose": purpose, "era": sera, "location": sloc,
            "historical_confidence": conf,
            "camera_complexity": cc, "spatial_accuracy": sa, "human_motion": hm, "visual_importance": vi,
            "pipeline": pipe, "status": "PLANNED",
            "characters": chars, "costumes": [COSTUME[c] for c in chars],
            "continuity_group": sid, "master_frame": None, "must_keep": keep,
            "camera_id": None, "prompt_id": None, "router_decision_id": None,
            "fact_ids": [], "rights_ids": [], "ai_label": label,
            "version_history": [], "approved_version": None,
            "created_at": TODAY, "updated_at": TODAY, "updated_by": BY,
            "notes": " ".join(notes),
        })
        n_shots += 1
    mf_note = " 반복 인물 등장 → 유료 생성 전 승인된 master_frame 필요 (정본 §5, P2)." if scene_chars else ""
    dump(OUT / f"scene_{sid}.json", {
        "scene_id": sid, "episode_id": "EP01", "title": title, "story_beat": beat,
        "era": era, "location": loc, "characters": scene_chars, "master_frame": None,
        "shot_ids": shot_ids, "status": "BROKEN_DOWN", "updated_at": TODAY, "updated_by": BY,
        "notes": f"TC {tc} · 원본 {section} + episodes/ep01-premiere-roughcut.html. 대본은 새로 쓰지 않음.{mf_note}",
    })
print(f"{len(scene_ids)} scenes, {n_shots} shots ->", OUT)
print(json.dumps(scene_ids))
