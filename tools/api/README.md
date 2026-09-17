# tools/api — 외부 API 키 현황과 활용 방식 (2026-09-17)

> 키는 repo 루트 `.env` 에만 (git 제외). 이 문서와 코드에는 값이 없다. 호출은 `tools/api/apis.py` 로 통일 (`python tools/api/apis.py selftest`).

## 1. 작동 확인 (09-17 14:00 실측)

| 키 | 상태 | 확인 방법 |
|---|---|---|
| `NAVER_CLIENT_ID/SECRET` | **OK** | 백과사전 검색 "천마총" 336건, 1위 = 한국민족문화대백과(terms.naver.com cid 46620). 뉴스 검색 OK |
| `ELEVENLABS_API_KEY` | **OK** (TTS·보이스 목록). `user_read` 권한 없음 → 잔여 글자 수 조회는 불가 | George 보이스 60자 TTS → mp3 56 KB. 모델: eleven_v3, multilingual_v2, flash_v2_5 등 |
| `WEBSHARE_USERNAME/PASSWORD` (+`_DEFAULT`) | **OK** | `p.webshare.io:80` 경유 출구 IP = 영국(Sky UK). 국내 전용 IP 여부는 미확인 |
| `KOREA_DATA_API_KEY` (64자, 공공데이터포털) | **대기** | e뮤지엄 서버 "SERVICE KEY IS NOT REGISTERED". 승인 뒤 제공기관 동기화(수 시간~1일) 전이거나, 다른 데이터셋용. 내일 재시험 |
| `EMUSEUM_API_KEY` (36자) | **미등록** | 동일 오류. 어느 포털에서 받은 키인지 확인 필요 |
| 국가유산청 | 키 불필요 | https 호출로 실데이터 확인 |
| `YOUTUBE_*`, `HIGGSFIELD_API_KEY`, `KHERITAGE_API_KEY` | 비어 있음 (필요 없음) | Higgsfield 는 claude.ai 커넥터 사용 |

## 2. 우리 OS 에서의 용도

| API | 쓰는 곳 | 규칙 |
|---|---|---|
| **네이버 백과사전** (`encyc`) | Historical QA 출처 탐색 1차 필터. 한국민족문화대백과·두산백과·문화원형 항목을 한 번에 검색 → `05_HISTORY_DATABASE/sources/` 후보 (등급 SECONDARY, 원문 URL 은 terms.naver.com 이 아니라 원 출처로 교체) | 백과 본문은 인용만, 이미지는 RED |
| **네이버 뉴스·블로그·웹** | 벤치마크·트렌드 모니터(예: "AI 역사 다큐" 반응), 다음 에피소드 소재(신규 발굴 뉴스), 커뮤니티 질문 수집 씨앗 | 봇은 수집만, 게시 없음 (Community Agent) |
| **네이버 이미지** | 구도 참고 검색만 | 권리 RED, 플레이트로 사용 금지 |
| **ElevenLabs** | 내레이션 **최종본** (D-047 초안 = Higgsfield TTS Grady). 영어 본편: George/Roger 급 남성 다큐 톤, `eleven_v3` 또는 `multilingual_v2`. 한국어판·쇼츠 더빙에도 사용 | 글자 수 = 비용. `COST_EP01` 에 provider "ElevenLabs (chars)" 로 기록. 샘플 3보이스 → 사용자 선택 → 전체 (Higgsfield 때와 동일 절차). EP01 대본 ≈ 5,500자 |
| **Webshare 프록시** | 리서치 스크립트가 막힌 사이트(e뮤지엄 500, Playboard 429, SocialBlade 403) 재시도. `proxy_session()` 으로 requests 세션 | 사람 검수 없이 대량 수집 금지. 출구 IP 가 해외라 국내 전용 사이트는 오히려 막힐 수 있음 |
| **공공데이터포털 e뮤지엄** | 등록 완료 시: 유물 검색 → 국립경주박물관 소장품(천마총 백화수피 관모·금관·과대) 실물 사진·치수·공공누리 등급 → `sources/` FACT 등급 + 플레이트 후보 | 공공누리 1유형만 플레이트 사용 |
| **국가유산청** | 국보·보물·사적 목록·좌표·지정일 → 다음 에피소드(다보탑·첨성대·불국사) FACT 기록 | 키 없음 |

## 3. 지금 바로 이득이 되는 순서
1. 네이버 백과로 노동자·시종·원로 복식 출처 재검색 → `sources/` 보강 (무료).
2. ElevenLabs 내레이션 샘플 3보이스 (콜드오픈 6문장 ≈ 400자 × 3) → 사용자 선택 → 최종 내레이션 교체 후보.
3. e뮤지엄 키 재시험(내일) → 관모 실물 사진 확보 → 복식 lock V03 근거.

## 4. 보안
`.env` 는 대화·캡처에 붙이지 않는다. 키를 새로 추가하면 `.env.example` 에 이름만 추가. 노출 시 발급처에서 폐기 후 재발급.
