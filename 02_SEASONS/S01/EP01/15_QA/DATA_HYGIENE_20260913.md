# EP01 Data Hygiene — 2026-09-13

Scope: 5 items that reviewers flagged. Only small data fixes with evidence behind them. Not committed and not pushed. This agent did not touch prompts, DECISIONS, CURRENT_STATUS or the generation cache (the orchestrator edited CURRENT_STATUS separately in the same batch). No paid tools were used.

Validator: `python 00_SYSTEM/schemas/validate.py` gave exit 0 both before and after the edits. Result at the time of these edits: `321/321 passed`, `cross-reference: OK` (the combined batch was re-validated before commit).

Changed files:
- `02_SEASONS/S01/EP01/07_SHOTS/shot_EP01_S06_SH005.json` (item 1)
- `02_SEASONS/S01/EP01/07_SHOTS/shot_EP01_S03_SH002.json` (item 2)
- `02_SEASONS/S01/EP01/07_SHOTS/shot_EP01_S04_SH002.json` (item 3)
- `05_HISTORY_DATABASE/facts/CLM_EP01_TUMULI_002.json` (item 3, reverse link in `used_in`)

`updated_at` was set to 2026-09-13 and `updated_by` to `Data Hygiene (Claude Code)` in the 3 edited shots. Existing notes were only appended to, never deleted.

---

## 1. H05 double AI label — FIXED

Evidence:
- `00_SYSTEM/schemas/shot.schema.json:167-172`: `ai_label` type is `["string","null"]`. It is not an enum.
- `shot_EP01_S06_SH005.json:43` (before): `"INTERPRETIVE RECONSTRUCTION"` only.
- `shot_EP01_S06_SH005.json:49` notes: "AI Visual Reconstruction + INTERPRETIVE RECONSTRUCTION 둘 다 표시".
- `14_EDIT/GRAPHICS_SPEC_EP01_V2.md:184`, `:188` ("H05 는 두 줄 모두"), `:387` (§5 #4b: the field and the notes disagree).
- `validate.py:103-104` only checks that `ai_label` is non-empty for AI pipelines. It does not check the value.

Change: `ai_label` is now `"AI Visual Reconstruction · INTERPRETIVE RECONSTRUCTION"`. A pointer note to §2 G09 / §5 #4b was appended to the notes.

Validator: exit 0.

## 2. S03_SH002 stale rights wording — FIXED (note appended)

Evidence:
- `shot_EP01_S03_SH002.json:36` notes: "사진마다 라이선스 확인 (C1 YELLOW)".
- `05_HISTORY_DATABASE/rights/RTS_NRICH_1973_PHOTOS_001.json:6` `KOGL Type 1`, `:15` `"status": "GREEN"`, `:19` `"usage_tier": "ACTIVE"`, `:18` notes (check the label on each file when downloading).

Change: appended "권리 표기 갱신 2026-09-13: RTS_NRICH_1973_PHOTOS_001 = GREEN / ACTIVE (KOGL Type 1, 파일별 공공누리 라벨 확인 필요). 위 'C1 YELLOW' 는 이전 기록." The original text is kept.

Validator: exit 0.

## 3. G04 gravel fact — FIXED (link + reverse link)

Evidence:
- `14_EDIT/GRAPHICS_SPEC_EP01_V2.md:101`: the locked layer order includes "stone/gravel". `:103` says "자갈(gravel)" is supported only by `CLM_EP01_TUMULI_002`. `:392` (§5 #7a) says it must be linked to `EP01_S04_SH002.fact_ids`.
- `05_HISTORY_DATABASE/facts/CLM_EP01_TUMULI_002.json:4` "wooden chambers covered with gravel", `:5` `"confidence": "FACT"`.
- `CLM_EP01_STRUCT_004.json:4` only says "stones piled above". It does not mention gravel.
- Over-interpretation rule `validate.py:69,100-102`: the shot's `historical_confidence` is `FACT` (`shot_EP01_S04_SH002.json:9`), and the strongest linked fact is still FACT, so the rule stays satisfied.

Change:
- `shot_EP01_S04_SH002.json` `fact_ids` now contains `CLM_EP01_STRUCT_004`, `CLM_CHEONMACHONG_LAYOUT_001` and `CLM_EP01_TUMULI_002` (line 27). A note was appended.
- `CLM_EP01_TUMULI_002.json` `used_in` now also lists `EP01_S04_SH002` (line 13).

Validator: exit 0.

## 4. G13 unlinked dimensions fact — NO CHANGE (no link needed now)

Evidence:
- `shot_EP01_S07_SH005.json:24-26`: `fact_ids` = `CLM_CHEONMACHONG_LAYOUT_001` only.
- `14_EDIT/GRAPHICS_SPEC_EP01_V2.md:258` (coffin shown with "치수 라벨 없음"), `:277` (no chest dimension label), `:321` (§3.10 #5: all dimension labels forbidden, because SH005 links only `LAYOUT_001`).
- `:263`: the optional wooden-chamber outline would need `STRUCT_004` linked first, but whether to include it is still undecided.

Why no change: G13 now shows no dimensions or stone layers, so `CLM_EP01_STRUCT_004` is not needed. If an editor later adds the wooden-chamber outline or the stone/earth layers (`:263`, `:278`), the link must be added at that point.

Validator: n/a (no edit). Exit 0 overall.

## 5. G13 narration hedge — NO CHANGE (old sentence not quoted in shot)

Evidence:
- `00_SYSTEM/DECISIONS.md:132` (D-026 #6): "It may have belonged to a burial system of status, ceremony, and identity."
- `shot_EP01_S07_SH005.json:34` notes: they do not contain "It belonged…" or any narration quote. They cover only X3/D-010, the G13 drawing scope and the scores.
- The old sentence appears only in resolved history rows: `05_SCRIPT/SCRIPT_ROUGHCUT_DELTA.md:14` (X5 RESOLVED) and `14_EDIT/GRAPHICS_SPEC_EP01_V2.md:401` (§5 #15 RESOLVED). The current text is at `:241` and `:308`.

Why no change: the shot notes don't quote the old sentence, so there is nothing to point to D-026.

Validator: n/a (no edit). Exit 0 overall.
