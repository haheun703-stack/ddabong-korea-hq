# RIGHTS CHECK — `RTS_GNM_OTHER_OBJECTS_001` (B5 박물관 기타 유물) 개별 라벨 확인

- 확인일: 2026-09-13 · 확인자: Claude Code (조사 시점에는 데이터 변경 없음 → 2026-09-13 반영됨, 아래 '반영' 절)
- 대상 권리: `RTS_GNM_OTHER_OBJECTS_001` (YELLOW / ACTIVE, D-014 YELLOW_ACTIVE, 편집 확정 전 해소 필수)
- 연결 샷: `EP01_S02_SH003` (금관 → 유리잔 → 말다래), `EP01_S05_SH001` (금관·관모·금허리띠·가슴걸이)
- 대상 유물·URL 출처: `episodes/ep01-artifact-library.html` 카드 3, 4, 5, 7, 8 (금관 B1 = `RTS_GNM_GOLD_CROWN_001`, 금허리띠 B3 = `RTS_GNM_GOLD_GIRDLE_001`, 천마도 = `RTS_WIKI_CHEONMADO_001` 은 이미 기록이 있어 제외)
- 방법: 국립경주박물관 각 페이지를 직접 받아서(curl, 2026-09-13) HTML 원문에서 공공누리 문구와 다운로드 링크를 확인. WebFetch 요약과도 대조함. 대조군으로 금관 페이지(mng_no=59)도 확인했고, 같은 형식의 "(1유형)" 문구와 "원본이미지 다운로드" 버튼이 있었음.
- 주의 (조사 시점 기준, 이후 '반영' 절로 대체됨): 이 파일은 조사 기록일 뿐이며 권리 JSON, 샷 JSON은 수정하지 않았음. 게시 직전에 페이지 라벨을 한 번 더 확인하고 캡처를 `proof` 로 남겨야 함 (현재 `proof` 없음).

## 1. 유물별 확인 결과

| # | 유물 (페이지 표기) | 페이지 URL | 공공누리 표시 (원문 인용) | 다운로드 | 권장 상태 | 사용 샷 |
|---|---|---|---|---|---|---|
| 1 | 가슴걸이 (소장품번호 경주2379, 출토지 "경상북도>경주시>천마총") | https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=53&mode=V | "국립경주박물관이 창작한 저작권 보호분야 가슴걸이 저작물은 "공공누리" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)" | 있음. "원본이미지 다운로드" 링크 (`/_prog/download/?...func_gbn_cd=relic_data&mng_no=53&atch=atch_img1` 등) | **GREEN 분리** | EP01_S05_SH001 |
| 2 | 금제 관모 (소장품번호 경주2275, 출토지 "경상북도>경주시>황남동 천마총") | https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=58&mode=V | "국립경주박물관이 창작한 저작권 보호분야 금제 관모 저작물은 "공공누리" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)" | 있음. "원본이미지 다운로드" 링크 (atch_img1, atch_img2 확인) | **GREEN 분리** | EP01_S05_SH001 |
| 3 | 유리잔 (상세정보 "경주 천마총, 보물 제620호", 신라 6세기, 7.4cm, 유물번호 칸은 비어 있음) | https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=172&mng_no=256&mode=V | "국립경주박물관이 창작한 저작권 보호분야 유리잔 저작물은 "공공누리" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)" | "원본이미지 다운로드" 버튼 **없음**. 전시 해설 페이지(sub02)라서 표시 이미지만 있음 (`/_prog/download/image.php?src=kor/relic_mgr/20201215104442_00fvma9ti62uiix9qciyp4fnbxr6f3.jpg`) | **GREEN 분리** (라벨은 1유형). 단, 원본 해상도 파일이 없으므로 표시 이미지 품질을 확인하거나 소장품 DB 페이지를 따로 찾아야 함 | EP01_S02_SH003 |
| 4 | 천마무늬 말다래 (유물번호 경주2309, 길이 81.0cm, 대나무·금동판, 키워드 "천마총, 말갖춤") | https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=193&mng_no=295&mode=V | "국립경주박물관이 창작한 저작권 보호분야 천마무늬 말다래 저작물은 "공공누리" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)" | "원본이미지 다운로드" 버튼 **없음**. 표시 이미지만 있음 (`/_prog/download/image.php?src=kor/relic_mgr/20230428175025_001n0nx0j2lhyn9h2wztv85qf2inrj.jpg`) | **GREEN 분리** (라벨은 1유형). 단, 아래 "확인 필요 A"를 먼저 결정해야 함 | EP01_S02_SH003 (해당하는 경우) |
| 5 | 유리구슬 목걸이 (유물번호 경주2381, 천마총 출토) | https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?GotoPage=1&d_mng_no=193&mng_no=306&mode=V | "국립경주박물관이 창작한 저작권 보호분야 유리구슬 목걸이 저작물은 "공공누리" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)" | "원본이미지 다운로드" 버튼 **없음**. 표시 이미지만 있음 (`/_prog/download/image.php?src=kor/relic_mgr/20230428185735_001fjg2h1z47q4zk9xwza7175ikkjy.jpg`) | GREEN 가능. 다만 두 샷 모두 이 유물을 쓰지 않으므로 선택 사항 (BACKUP_ONLY) | 없음 (라이브러리 조합 B 전용) |
| 6 | 귀걸이 | 저장소에 URL 없음 | **확인 안 함.** 페이지를 특정하지 못해 라벨을 볼 수 없었음 | - | YELLOW 유지 (BACKUP_ONLY로 전환 권장) | 없음 |
| 7 | 토기 | 저장소에 URL 없음 | **확인 안 함.** 페이지를 특정하지 못해 라벨을 볼 수 없었음 | - | YELLOW 유지 (BACKUP_ONLY로 전환 권장) | 없음 |

4유형(RED)으로 표시된 페이지는 없었음. 확인한 5개 페이지 모두 1유형이었음.

### 확인 필요
- **A. S02_SH003 의 "말다래"가 어느 유물인지.** 샷의 `rights_ids` 에는 이미 `RTS_WIKI_CHEONMADO_001` 이 들어 있음. 몽타주 "말다래"가 천마도(천마그림 말다래, mng_no=298)라면 이 샷에는 #4 기록이 필요 없음. 금동판이 붙은 천마무늬 말다래(경주2309, 라이브러리 카드 7)라면 #4 기록을 연결해야 함. 편집/연출 결정이 필요함.
- **B. 유리잔·말다래 원본 파일.** 두 페이지는 원본 다운로드를 제공하지 않음. 1유형이므로 표시 이미지 사용 자체는 가능하지만, 해상도가 부족하면 국립경주박물관 소장품 DB(sub04) 또는 e뮤지엄에서 같은 유물의 원본 페이지를 찾고, **그 페이지 라벨을 다시 확인**해야 함 (라벨은 페이지마다 따로 확인. 추정 금지).
- **C. 증빙.** 모든 신규 기록의 `proof` 는 페이지 캡처 파일 경로로 채워야 함. 이번 조사에서는 캡처를 저장하지 않았음.

## 2. 제안 데이터 변경 (조사 시점 미적용 → 2026-09-13 반영, '반영' 절)

형식은 `RTS_GNM_GOLD_CROWN_001` 을 따름. `checked_by` 는 실제 반영하는 주체로 기입.

### 2-1. 신규 권리 기록 (`05_HISTORY_DATABASE/rights/`)

**`RTS_GNM_CHEST_ORNAMENT_001.json`**
```json
{
  "rights_id": "RTS_GNM_CHEST_ORNAMENT_001",
  "asset_id": "ASSET_GNM_CHEONMACHONG_CHEST_ORNAMENT_V01",
  "source": "https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=53&mode=V",
  "creator": "국립경주박물관",
  "license": "KOGL Type 1",
  "commercial_use": "YES",
  "modification_allowed": "YES",
  "attribution_required": "YES",
  "attribution_text": "Source: Gyeongju National Museum, Chest ornament from Cheonmachong (Gyeongju 2379), KOGL Type 1.",
  "expiration": null,
  "proof": null,
  "research_permission": "YES",
  "media_reuse_permission": "YES",
  "status": "GREEN",
  "checked_at": "2026-09-13",
  "checked_by": "<반영 주체>",
  "notes": "RTS_GNM_OTHER_OBJECTS_001 에서 분리. 페이지 문구 '...가슴걸이 저작물은 \"공공누리\" 출처표시 조건에 따라 이용할 수 있습니다. (1유형)'. 원본이미지 다운로드 있음. 15_QA/RIGHTS_CHECK_GNM_OTHER_OBJECTS_20260913.md.",
  "usage_tier": "ACTIVE"
}
```

**`RTS_GNM_GOLD_CAP_001.json`**: 위와 같은 구조에 아래 값을 넣음.
- `asset_id`: `ASSET_GNM_CHEONMACHONG_GOLD_CAP_V01`
- `source`: `https://gyeongju.museum.go.kr/kor/html/sub04/0402.html?GotoPage=1&dvs_code=&mng_no=58&mode=V`
- `license` `KOGL Type 1` · `commercial_use`/`modification_allowed`/`media_reuse_permission` `YES` · `status` `GREEN` · `usage_tier` `ACTIVE`
- `attribution_text`: `Source: Gyeongju National Museum, Gold cap from Cheonmachong (Gyeongju 2275), KOGL Type 1.`
- `notes`: 분리 출처, "(1유형)" 인용, 원본이미지 다운로드 있음 (2장)

**`RTS_GNM_GLASS_CUP_001.json`**
- `asset_id`: `ASSET_GNM_CHEONMACHONG_GLASS_CUP_V01`
- `source`: `https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=172&mng_no=256&mode=V`
- `license` `KOGL Type 1` · `YES` ×3 · `status` `GREEN` · `usage_tier` `ACTIVE`
- `attribution_text`: `Source: Gyeongju National Museum, Glass cup from Cheonmachong (Treasure No. 620), KOGL Type 1.`
- `notes`: "(1유형)" 인용. 전시 해설 페이지이며 원본 다운로드 버튼 없음. 표시 이미지만 있어 해상도 확인 필요 (확인 필요 B)

**`RTS_GNM_MUDGUARD_001.json`** (확인 필요 A 결정 후, 경주2309 사용 시에만)
- `asset_id`: `ASSET_GNM_CHEONMACHONG_MUDGUARD_V01`
- `source`: `https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?d_mng_no=193&mng_no=295&mode=V`
- `license` `KOGL Type 1` · `YES` ×3 · `status` `GREEN` · `usage_tier` `ACTIVE`
- `attribution_text`: `Source: Gyeongju National Museum, Mudguard with winged-horse design from Cheonmachong (Gyeongju 2309), KOGL Type 1.`
- `notes`: "(1유형)" 인용. 원본 다운로드 버튼 없음. 천마도(RTS_WIKI_CHEONMADO_001)와는 다른 유물

**(선택) `RTS_GNM_GLASS_BEADS_001.json`**
- `asset_id`: `ASSET_GNM_CHEONMACHONG_GLASS_BEADS_V01`
- `source`: `https://gyeongju.museum.go.kr/kor/html/sub02/0202.html?GotoPage=1&d_mng_no=193&mng_no=306&mode=V`
- `license` `KOGL Type 1` · `status` `GREEN` · **`usage_tier` `BACKUP_ONLY`** (연결 샷 없음)
- `attribution_text`: `Source: Gyeongju National Museum, Glass bead necklace from Cheonmachong (Gyeongju 2381), KOGL Type 1.`

### 2-2. 기존 기록 수정

1. `07_SHOTS/shot_EP01_S02_SH003.json` `rights_ids`: `RTS_GNM_OTHER_OBJECTS_001` 을 빼고 `RTS_GNM_GLASS_CUP_001` 을 넣음 (A가 경주2309로 정해지면 `RTS_GNM_MUDGUARD_001` 도 추가). `notes` 의 "B5 YELLOW (개별 라이선스 확인 전 사용 금지)"도 함께 갱신.
2. `07_SHOTS/shot_EP01_S05_SH001.json` `rights_ids`: `RTS_GNM_OTHER_OBJECTS_001` 을 빼고 `RTS_GNM_GOLD_CAP_001`, `RTS_GNM_CHEST_ORNAMENT_001` 을 넣음. `notes` "나머지는 개별 확인"도 갱신.
3. `RTS_GNM_OTHER_OBJECTS_001.json`: 두 샷에서 참조를 모두 제거한 **다음에** `usage_tier` 를 `ACTIVE` 에서 `BACKUP_ONLY` 로 바꿈 (순서를 지키지 않으면 validate.py 의 BACKUP_ONLY 참조 FAIL). `status` 는 YELLOW 유지 (귀걸이·토기 미확인). `notes` 에 분리된 기록 id와 이 보고서 경로를 추가.
4. 필요하면 해당 `router_decision_RTR_EP01_S02_SH003_V01.json` / `..._S05_SH001_V01.json` 에 rights 참조가 있는지 확인하고 함께 맞춤 (이번에는 확인하지 않음).
5. 반영 후 `validate.py` 를 실행하고, `CURRENT_STATUS.md` 의 YELLOW_ACTIVE 1건 해소 여부를 갱신함.

## 반영 (2026-09-13)

- 확인 필요 A 해소 (반박 검수 정정): S02_SH003 몽타주의 '말다래'는 **금동 천마무늬 말다래 (경주2309)** — 대본 v2 0:35–1:25 VO 'horse equipment', 유물 라이브러리 카드 7 배정. 천마도는 1:25–2:15 구간. → `RTS_GNM_MUDGUARD_001` 생성·연결 (천마도 기록은 유지). 앞선 '천마도' 판단은 근거 없이 내린 오류였음.
- 생성: `RTS_GNM_CHEST_ORNAMENT_001` · `RTS_GNM_GOLD_CAP_001` · `RTS_GNM_GLASS_CUP_001` · `RTS_GNM_MUDGUARD_001` (GREEN, ACTIVE). 증빙: 페이지 HTML 원문 `05_HISTORY_DATABASE/rights/proof/<rights_id>_20260913.html` (라벨 확인된 것만 proof 기재).
- 샷 교체: S02_SH003 → GLASS_CUP + MUDGUARD · S05_SH001 → GOLD_CAP + CHEST_ORNAMENT. `RTS_GNM_OTHER_OBJECTS_001` → BACKUP_ONLY (YELLOW 유지).
- 남은 일: 유리잔·말다래 표시 이미지 해상도 확인 (확인 필요 B), 기존 GREEN 기록(금관·금허리띠·천마도·NRICH) proof 보관 — 2026-09-13 완료.

## 해상도 해결 (2026-09-13)

- 유리잔·말다래 → e뮤지엄 페이지로 출처 교체 (같은 소장품번호, 제 1유형, 3000px급). 증빙 `proof/<rights_id>_emuseum_20260913.html`, 기존 GNM 페이지 증빙도 보관.
- 가슴걸이·금제 관모: e뮤지엄 1유형 페이지 확인, 이미지 크기 미측정 (전체 화면 사용 시 편집 전 확인).
- 상세: `15_QA/ARCHIVE_IMAGE_RESOLUTION_20260913.md`.
