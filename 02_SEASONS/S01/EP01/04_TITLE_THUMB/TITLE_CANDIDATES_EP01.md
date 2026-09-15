# EP01 제목 후보 5안 (TITLE_STANDARD v0.1, 2026-09-15)

> 작성: Script Agent (Claude Code) · 근거 `channel.json.core_questions[0]` · 확정은 사용자 (2안 = 실험 A/B). `episode.json.working_title_en` = "Why Are Giant Tombs Everywhere in This Korean City?" (작업명 유지).
> 규칙: 질문형 또는 FACT 근거 · ≤ 60자 · 낚시어 금지 · 왕 이름 단정 금지 (`CLM_EP01_OCCUPANT_006`).

| # | 제목 (EN) | 형식 | 주장 → 근거 | 글자 | 메모 |
|---|---|---|---|---|---|
| T1 | Why Are Giant Tombs Everywhere in This Korean City? | 질문형 | 봉분이 도심에 있음 → `CLM_EP01_TOMBS_001` (FACT) | 51 | 작업명. 안전한 기본안 |
| T2 | Why Did Ancient Korea Bury Its Kings in the Middle of Town? | 질문형 | 왕릉군 = 도시 경관 → `CLM_EP01_TOMBS_001` · `CLM_EP01_MODERN_012` | 58 | "kings" 는 왕급 추정 → 피장자 단정 아님 (S4). 그래도 `OCCUPANT_006` 주의 |
| T3 | The Grass Hills of Gyeongju Are 1,500-Year-Old Tombs | FACT 단정 | 봉분 = 신라 고분 → `CLM_EP01_TUMULI_002` · 연대 → `SRC_UNESCO_GYEONGJU_001` | 49 | 숫자 "1,500" 은 화면 숫자에 없음 → `numbers_on_screen` 추가 필요, 아니면 금지 |
| T4 | Inside a 47-Meter Tomb: What Korea Buried With Its Dead | FACT 단정 | 47 m → `CLM_EP01_STRUCT_004` · 부장품 → `CLM_EP01_GOODS_005` | 55 | 각도 MYSTERY. 숫자 화면 일치 (47 m) |
| T5 | This Korean City Built Mountains for the Dead. Here's Why. | 질문형(변형) | 봉분 규모 → `CLM_EP01_STRUCT_004`; "why" = ⑤ INTERPRETIVE 는 hedge 로 답함 | 57 | "Mountains" 는 비유 → 자막에서 12.7 m 로 보정. 낚시 경계선, 권장 순위 낮음 |

**봇 권장**: 실험 A = T1 (질문형·안전), B = T4 (숫자·MYSTERY 각도). T3 은 화면 숫자 추가 시에만.

근거 문장:
- `CLM_EP01_TOMBS_001` (FACT): Gyeongju holds concentrated Silla royal tomb groups that form part of the city landscape.
- `CLM_EP01_TUMULI_002` (FACT): Tumuli Park Belt has three tomb groups, mostly domed; wooden chambers covered with gravel; gold, glass and ceramics excavated.
- `CLM_EP01_STRUCT_004` (FACT): Cheonmachong: wooden chamber 6.6×4.2 m with coffin 2.15×0.8 m, stones piled above, earth mound 47 m across and 12.7 m high.
- `CLM_EP01_GOODS_005` (FACT): Gold crown, earrings, ornaments, weapons, vessels, lacquerware, glass and horse gear were placed with the dead and in the chest; the birch-bark saddle flap bears a heavenly horse.
- `CLM_EP01_OCCUPANT_006` (FACT): The occupant was probably a king or of comparable rank, but the identity is not certain.
