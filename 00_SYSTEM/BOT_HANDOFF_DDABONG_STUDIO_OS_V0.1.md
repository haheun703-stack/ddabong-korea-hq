# DDABONG STUDIO OS v0.1 — BOT HANDOFF

Status: CANONICAL HANDOFF
Date: 2026-09-11
Project: DDABONG KOREA / 따봉 대한민국
Role of this document: A bot or agent starting work on DDABONG must read this first and treat it as the current operating contract unless a newer approved version exists.

---

## 0. FIRST PRINCIPLE

DDABONG KOREA is not a generic Korea-promotion channel and not an AI spectacle channel.

Core promise:

> Not just what happened. Why it made sense to them.

Korean operating interpretation:

> 무슨 일이 있었는지만 보여주지 않는다. 그 시대 사람들은 왜 그렇게 생각했고, 왜 그 선택이 당시에는 말이 되었는지를 보여준다.

Narrative grammar:

QUESTION → FACT → CONTEXT → MINDSET → CHOICE → LEGACY

Historical evidence rule:

FACT → PROBABLE → INTERPRETIVE → ARTISTIC

Never present unrecorded inner thoughts as fact.

---

# 1. OS TOP-LEVEL RULES

1. Generate Late
   - Paid image/video generation happens only after research, history QA, scene/shot/camera/composition decisions.

2. Reuse Everything
   - Reuse eras, locations, costumes, characters, camera setups, prompts, music presets and assets.

3. Change Only What Failed
   - Do not regenerate a full shot if only one element failed.
   - Use KEEP / CHANGE patches.

4. Human Approval Before Cost
   - Paid generation and meaningful historical interpretation require human approval.

5. Evidence Before Imagination
   - Real source material first, reconstruction second, cinematic invention last.

6. Never overwrite approved versions
   - Version every important artifact and allow rollback.

7. Production and system-improvement are separate
   - Daily production uses approved standards.
   - Rule changes are tested separately and promoted only after regression checks.

---

# 2. OFFICIAL PRODUCTION PIPELINE

IDEA
→ RESEARCH
→ SOURCE / FACT QA
→ STORY ANGLE
→ TITLE + THUMBNAIL CONCEPT
→ SCRIPT
→ NARRATION DESIGN
→ TEMP MUSIC MAP
→ SCENE BREAKDOWN
→ SHOTLIST
→ SHOT ROUTER
→ REAL SHOOT / ARCHIVE / AI STILL / BLENDER PREVIZ / FLOW-VEO / HIGGSFIELD
→ ROUGH CUT
→ FINAL MUSIC
→ SFX / AMBIENCE / FOLEY
→ AUDIO MIX
→ HISTORY QA
→ VISUAL QA
→ RETENTION QA
→ RIGHTS QA
→ FINAL APPROVAL
→ PUBLISH
→ SHORTS / CLIPS
→ ANALYTICS
→ SYSTEM LEARNING

Do not skip gates merely because a provider can generate quickly.

---

# 3. MULTI-AGENT ARCHITECTURE

The system appears as one studio but uses specialized agents under a MASTER ORCHESTRATOR.

## Story Engine
- Research Agent
- Fact Check Agent
- Strategy Agent
- Thumbnail Agent
- Script Agent
- Narration Director

## Continuity Engine
- Character Supervisor
- Costume Supervisor
- Location Continuity Agent
- Scene Continuity Agent
- Master Frame Manager

## Visual Engine
- Scene Planner
- Shot Director
- Visual Router
- Blender Agent
- Image Generation Agent
- Video Generation Agent

## Audio Engine
- Music Director
- Voice/Narration Director
- Sound Director

## Quality Engine
- Historical QA Agent
- Visual QA Agent
- Rights Agent
- Retention QA Agent
- Cost Gate Agent

## Publish & Learning Engine
- Publish Agent
- Shorts Agent
- Analytics Agent
- Experience Learning Agent

### Agent handoff rule
Agents do not pass free-form opinions as truth. They pass approved structured data with IDs, status and provenance.

### Provider abstraction
Agent ≠ provider.

Examples:
- Research Agent may use Gemini/OpenAI/other research provider.
- Script Agent may use Claude/OpenAI/other LLM provider.
- Video Generation Agent may route to Flow/Veo/Higgsfield.
- Music Director may route to Suno/licensed library/future provider.

The OS must survive provider changes.

---

# 4. DATA MODEL

Hierarchy:

PROJECT
└─ SEASON
   └─ EPISODE
      └─ SCENE
         └─ SHOT
            └─ VERSION

Shared entities:

ASSET
SOURCE
FACT
PROMPT
MODEL
GENERATION
COST
APPROVAL
LICENSE
MUSIC
VOICE
ANALYTICS
CHARACTER
COSTUME
ERA
LOCATION
MASTER_FRAME
CASE_MEMORY
FAILURE_MEMORY
PERFORMANCE_MEMORY

SHOT is the minimum operational unit.

Example:

```json
{
  "shot_id": "EP001_S04_SH003",
  "duration": 8,
  "purpose": "elite burial preparation",
  "era": "SILLA_EARLY",
  "location": "GYEONGJU_BURIAL_SITE",
  "historical_confidence": "PROBABLE",
  "camera_complexity": 55,
  "spatial_accuracy": 90,
  "human_motion": 45,
  "visual_importance": 85,
  "pipeline": "BLENDER_FLOW",
  "status": "PREVIZ_APPROVED",
  "characters": ["CHAR_SILLA_OFFICIAL_01"],
  "costumes": ["COSTUME_SILLA_OFFICIAL_A01"],
  "continuity_group": "EP001_S04",
  "master_frame": "EP001_S04_MASTER_V03",
  "must_keep": ["face_identity","body_proportion","hair","costume","height_ratio"]
}
```

---

# 5. CHARACTER / CONTINUITY STRATEGY

This is a core DDABONG system, not an optional visual preference.

## Approved main historical character style

PRIMARY STYLE:
B — Documentary Reenactment

Definition:
- realistic Korean facial proportions
- natural skin texture
- subtle imperfections and lived-in detail
- restrained expressions
- historically researched clothing
- natural documentary lighting
- not overly glamorous
- not glossy AI-model skin
- not fantasy-drama styling
- not generic Joseon hanbok for all Korean history

Hero-shot exception:
- Selected poster/thumbnail/opening hero frames may lean toward Cinematic Photoreal, but the episode body remains Documentary Reenactment.

Semi-realistic 3D is mainly for previz/reference.
Stylized/game-cinematic is not the default body style.

## Character Master Pack required before video generation
For each important recurring historical person:
- Hero portrait
- front
- 3/4 left
- 3/4 right
- profile
- full body
- neutral standing
- walking pose
- costume detail
- expression sheet

Status must reach CHARACTER_MASTER_APPROVED before paid video generation.

## Character IDs
Never prompt with only “a Silla official.”
Use persistent IDs:
- CHAR_SILLA_OFFICIAL_01
- COSTUME_SILLA_OFFICIAL_A01
- LOC_GYEONGJU_BURIAL_SITE_V01

## Scene Master Frame
Each scene with recurring people should have an approved master frame.
All child shots should derive from that visual lineage.

## KEEP / CHANGE patching
If only costume failed:

KEEP:
- face_identity
- body
- camera
- composition
- lighting
- actor_position

CHANGE:
- collar shape
- belt
- sleeve ornamentation

Do not rewrite the whole prompt.

---

# 6. BLENDER / FLOW-VEO / HIGGSFIELD DIRECTING STRATEGY

## Blender role
Blender is not primarily the final face generator.
It locks:
- space
- scale
- camera
- lens
- actor positions
- movement paths
- height ratios
- architecture relationships

Blender input should be structured data, not vague natural language.

Example:

```json
{
  "lens": 28,
  "camera_height": 1.6,
  "duration": 8,
  "fps": 24,
  "motion": {"type":"dolly_forward","distance":7},
  "tilt": {"start":0,"end":14},
  "target": "MAIN_OBJECT"
}
```

## Flow / Veo role
Primary motion path when continuity and natural movement matter:
- walking
- carrying
- looking
- ritual preparation
- subtle human interaction
- ordinary dolly/pan/tracking

Preferred path:
BLENDER PREVIZ → APPROVED KEY FRAME → IMAGE/REFERENCE CONDITIONING → FLOW/VEO

## Higgsfield role
Use selectively for:
- extreme push-in/reveal
- time transition
- past-to-present match cut
- high-impact camera choreography
- hero moment

Do not route every historical shot to Higgsfield.

## AI ordering rule
REAL EVIDENCE → SPATIAL RECONSTRUCTION → CHARACTER LOCK → KEY FRAME → MOTION → CINEMATIC CAMERA

Never start with random text-to-video when continuity or historical spatial accuracy matters.

---

# 7. VISUAL ROUTER

Default rules:

Present-day location → REAL_SHOOT
Historical photo/document/artifact → ARCHIVE
Low motion + high factual density → AI_STILL or ORIGINAL_GRAPHIC
High spatial accuracy + high camera complexity → BLENDER → FLOW/VEO
Very high camera complexity + medium spatial dependency → HIGGSFIELD
Human continuity critical → MASTER FRAME + REFERENCE-DRIVEN VIDEO

Router output must include:
- recommended pipeline
- reason
- historical confidence
- continuity risk
- expected cost range
- number of expected attempts

---

# 8. PROMPT SYSTEM

Prompt assembly:

GLOBAL LOCK
+ ERA LOCK
+ LOCATION LOCK
+ CHARACTER / COSTUME LOCK
+ STYLE LOCK
+ CAMERA DATA
+ SHOT DELTA

Do not write every prompt from scratch.

Example lock IDs:
- DDABONG_GLOBAL_V01
- SILLA_EARLY_V01
- GYEONGJU_BURIAL_V01
- SILLA_COSTUME_OFFICIAL_V01
- DDABONG_DOC_REENACTMENT_V01
- CAMERA_S004_V02
- SHOT_ACTION_V01

Global base:

Photorealistic cinematic historical documentary. Natural physical proportions. Historically plausible reconstruction. Realistic materials. Natural lighting. No fantasy. No modern objects. No text. No logos. No excessive saturation. No glossy AI look. No malformed anatomy. No arbitrary architecture changes.

---

# 9. HISTORICAL ACCURACY SYSTEM

Every historical claim or visual detail must carry one of:

FACT
PROBABLE
INTERPRETIVE
ARTISTIC

Examples:
- known existence/date from strong evidence → FACT
- plausible material/color based on comparative evidence → PROBABLE
- crowd size / exact arrangement not recorded → INTERPRETIVE
- dawn fog / dramatic sunbeam → ARTISTIC

Unrecorded inner thoughts must never be presented as factual quotation or certainty.

Historical AI scenes must display:
AI Visual Reconstruction

For stronger interpretation scenes also consider:
INTERPRETIVE RECONSTRUCTION

---

# 10. SOURCE LEDGER + RIGHTS LEDGER

Every factual claim must connect to source IDs.
Every external visual/audio asset must connect to rights records.

Source record minimum:
- source_id
- claim_id
- title
- institution/author
- URL/file path
- access/verification date
- excerpt/summary
- confidence

Rights record minimum:
- asset_id
- source
- creator
- license
- commercial_use
- modification_allowed
- attribution_required
- expiration
- proof
- status GREEN/YELLOW/RED/BLUE

Research permission and media reuse permission are separate.

---

# 11. COST / MONEY GATE

Each episode has a generation budget.

Warnings:
- 80%: warning
- 95%: strong warning
- 100%: generation locked

Before any paid generation show:
- shot ID
- provider/model
- expected attempts
- estimated cost range
- continuity risk
- approval button

Only a human may approve the paid call.

---

# 12. VERSIONING

Overwrite prohibited.

Example:

SHOT_014
- PREVIZ_V01
- PREVIZ_V02
- PREVIZ_V03 ★ APPROVED
- LOOK_V01
- LOOK_V02 ★ APPROVED
- VIDEO_V01
- VIDEO_V02
- VIDEO_V03 ★ FINAL

Rollback must always be possible.

---

# 13. REVIEW UI / MOBILE UI

Desktop Shot Review:
[V01] [V02] [V03] [V04]

Actions:
⭐ APPROVE
🔄 FIX
❌ REJECT

Fix reasons:
- Camera
- Architecture
- Costume
- Lighting
- Motion
- Character identity
- Historical issue
- AI artifact
- Other

Mobile should be intentionally simple:
PLAY
👍 APPROVE
🔄 FIX
❌ REJECT

---

# 14. THUMBNAIL SYSTEM

Composer ingredients:
MAIN HISTORICAL OBJECT
+ KEY FIGURES
+ PAST/PRESENT CONTRAST
+ STRONG SCALE
+ ONE VISUAL MYSTERY

QA:
- central object clear?
- too many faces?
- faces legible on mobile?
- title and thumbnail repeating same information?
- past/present contrast immediate?
- one mystery, not ten?

---

# 15. BRAND INTRO

3–5 seconds maximum.
Role: TIME GUIDE / signature transition into Korean past and present.
Tone: grandeur 80 / friendliness 20.
Avoid over-comedy.

---

# 16. NARRATION / AUDIO

Narration rhythm:
QUESTION → DISCOVERY → EVIDENCE → MEANING

Narrator face: 0% by default.
Fixed narrator voice: required.
Historical characters speak only when justified and useful.

Audio layers:
VOICE
MUSIC
AMBIENCE
SFX
FOLEY

Music identity:
Korean Cinematic Hybrid
Traditional Korean timbres integrated inside modern cinematic scoring, not traditional music playing continuously.

Music provider must remain abstracted from Suno or any single vendor.

---

# 17. RETENTION QA

Flag exposition risk when:
- long explanation without visual change
- no new location/object/reveal
- repetitive narration
- low audio variation

Suggested interventions:
- archive insert
- map/graphic
- TIME-MATCH
- question reset
- audio change
- object reveal

---

# 18. EXPERIENCE LEARNING ENGINE

This was strengthened using the attached 2026-09-11 AI YouTube operations analysis report.

Do not merely accumulate longer prompts.
Store user judgment as structured examples.

Four memories:

1. STANDARD MEMORY
   - current approved channel/system rules

2. CASE MEMORY
   - AI draft + user-edited/selected result + reason + scope

3. FAILURE MEMORY
   - concrete failure and what fixed it

4. PERFORMANCE MEMORY
   - time, attempts, cost, approval rate, CTR, retention, etc.

Learning loop:

USER REVIEW
→ AI RESULT vs USER APPROVED RESULT
→ DIFF ANALYZER
→ FAILURE CLASSIFIER
→ CASE MEMORY
→ RULE CHANGE CANDIDATE
→ REGRESSION TEST
→ HUMAN APPROVAL
→ NEW STANDARD VERSION

Never promote a rule from one successful example alone.
Test against earlier good cases and unused cases.

Fine-tuning is NOT the starting point.
Start with approved standards + retrieval of relevant cases + evaluation + regression testing.
Consider model training only after enough repeated, measured cases exist.

---

# 19. CURRENT DDABONG PROJECT STATE

Active channel:
DDABONG KOREA
Slogan: STORIES BEHIND KOREA

Current active episode:
EP01 — Gyeongju Royal Tombs / Cheonmachong
English working title:
Why Are Giant Tombs Everywhere in This Korean City?

Important: OS examples that mention EP001 Hwangnyongsa are TEMPLATE EXAMPLES ONLY. Do not overwrite the current active EP01.

Prepared EP01 assets already in repository include:
- verified research v2
- production script v2
- visual asset acquisition plan
- Gyeongju field shoot plan
- 1973 Cheonmachong excavation archive gallery
- artifact source library
- Higgsfield prompt pack
- graphics specification
- Premiere rough-cut timeline

Current strategic expansion:
Gyeongju should be treated as a reusable content cluster. When filming, capture not only royal tombs but reusable footage for Bulguksa, Dabotap/Seokgatap, Seokguram, Cheomseongdae, museum, Woljeonggyo/Donggung where practical.

Rule:
VIDEO TOPIC = NARROW
FIELD SHOOT = BROAD

---

# 20. DDABONG CHARACTER DECISION LOG

CASE-DDABONG-CHAR-001

Task:
Choose historical human visual style.

Options tested:
A Cinematic Photoreal
B Documentary Reenactment
C Semi-Realistic 3D
D Stylized Cinematic

User approved:
B Documentary Reenactment

Operational meaning:
- body historical reenactment scenes use B
- hero/thumbnail may selectively borrow A-level cinematic polish
- C mainly previz/reference
- D not default

This is a reusable approved case, not a universal rule for mascots or thumbnails.

---

# 21. FILE SYSTEM TARGET

DDABONG_STUDIO/

00_SYSTEM/
01_CHANNEL/
02_SEASONS/
03_SHARED_ASSETS/
04_BLENDER_LIBRARY/
05_HISTORY_DATABASE/
06_PROMPT_LIBRARY/
07_AUDIO_LIBRARY/
08_GENERATION_CACHE/
09_ANALYTICS/
10_EXPORTS/

Episode template:

00_BRIEF/
01_RESEARCH/
02_SOURCES/
03_STORY/
04_TITLE_THUMB/
05_SCRIPT/
06_NARRATION/
07_SHOTS/
08_REAL_FOOTAGE/
09_ARCHIVE/
10_BLENDER/
11_AI_STILLS/
12_AI_VIDEO/
13_AUDIO/
14_EDIT/
15_QA/
16_PUBLISH/
17_SHORTS/
18_ANALYTICS/

---

# 22. SYSTEM CANONICAL DOCUMENTS TO MAINTAIN

MASTER_CHANNEL_BIBLE.md
AGENT_RULES.md
CURRENT_STATUS.md
CONTENT_ROADMAP.md
HISTORY_ACCURACY_STANDARD.md
SOURCE_STANDARD.md
RIGHTS_STANDARD.md
VISUAL_STYLE_BIBLE.md
CHARACTER_CONTINUITY_STANDARD.md
THUMBNAIL_STANDARD.md
BRAND_INTRO_STANDARD.md
BLENDER_STANDARD.md
CAMERA_GRAMMAR.md
SHOT_STANDARD.md
PROMPT_STANDARD.md
MODEL_ROUTER.md
NARRATION_STANDARD.md
MUSIC_STANDARD.md
SOUND_STANDARD.md
COST_STANDARD.md
QA_STANDARD.md
PUBLISH_STANDARD.md
ANALYTICS_STANDARD.md
EXPERIENCE_LEARNING_STANDARD.md
CASE_MEMORY_SCHEMA.md
REGRESSION_TEST_STANDARD.md

---

# 23. ABSOLUTE DO-NOT RULES

❌ all scenes text-to-video
❌ new style for every shot
❌ unsupported architecture presented as fact
❌ random face changes across shots
❌ generic Joseon styling across Korean eras
❌ paid generation without approval
❌ full prompt rewrite when one detail failed
❌ publish without sources
❌ publish with unresolved rights
❌ 10-minute continuous AI footage
❌ nonstop traditional music
❌ thumbnail with too many ideas
❌ AI-generated inner thoughts presented as historical fact
❌ one successful example immediately becoming a global rule

---

# 24. BOT STARTUP PROCEDURE

When a bot receives this project:

1. Read this document first.
2. Read the latest CURRENT_STATUS and active episode files.
3. Identify the exact current gate.
4. Do not restart already-approved work.
5. Reuse approved IDs, prompts, characters, sources and assets.
6. If a change is requested, record KEEP / CHANGE and create a new version.
7. Before paid generation, present Money Gate and wait for human approval.
8. Before historical interpretation, verify source/confidence status.
9. After human correction, create a Case Memory entry.
10. Update both repository records and viewable Web HQ HTML.

---

# 25. NEXT BUILD PRIORITY

System build order:

P0 — Canonical OS docs and schemas
P1 — Episode / Scene / Shot data model
P2 — Character + Continuity Engine
P3 — Source + Rights Ledger
P4 — Shot Router
P5 — Review UI + mobile approval
P6 — Money Gate + provider adapters
P7 — Blender local agent bridge
P8 — Learning / regression system
P9 — Publish / analytics automation

The first real proving ground remains the active Gyeongju Royal Tombs episode.

END OF CANONICAL HANDOFF.
