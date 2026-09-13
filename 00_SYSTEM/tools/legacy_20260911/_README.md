# 2026-09-11 데이터 생성 스크립트 (보관용)

P1–P2 인스턴스를 만든 일회성 스크립트. 원래 세션 임시 폴더에만 있었다 (2026-09-13 전체 검수 지적 → 저장소로 이동).
모두 `python <script> <repo-root>` 형태. 이미 반영된 결과를 다시 쓰므로 **재실행 전 git diff 로 확인**한다.

| 스크립트 | 산출 |
|---|---|
| gen_ep01_shots.py | 씬 9 · 샷 (러프컷 타임라인 기준) |
| costume_qa.py | D-011 복식 출처·사실, 복식 TBD 해소 |
| delta_apply.py | SCRIPT_ROUGHCUT_DELTA X2/X3 반영 |
| gen_p3.py | P3 Source/Rights Ledger |
| gen_p4.py | P4 Shot Router 판정 49 |
| gen_p2prep.py | P2 lock · 프롬프트 · 카메라 · master_frame |
| apply_d015.py | D-015 반영 (복식 lock, 프롬프트 재조립, cost/approval) |
| record_batch1.py | 원로 Master Pack 배치 1 기록 |
