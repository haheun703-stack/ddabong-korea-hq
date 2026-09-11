#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DDABONG STUDIO OS — schema validator.
Usage:  python 00_SYSTEM/schemas/validate.py            (validate examples/ + known instances)
        python 00_SYSTEM/schemas/validate.py FILE.json  (validate one instance; schema picked by "$schema" or filename prefix)
"""
import json, sys, warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from pathlib import Path
try:
    from jsonschema import Draft7Validator, RefResolver
except ImportError:
    print("jsonschema not installed. Run:  pip install jsonschema"); sys.exit(2)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMAS = {p.stem.replace(".schema", ""): json.loads(p.read_text(encoding="utf-8")) for p in HERE.glob("*.schema.json")}
STORE = {v["$id"]: v for v in SCHEMAS.values()}

DIR_SCHEMA = {"era": "era", "locations": "location", "characters": "character", "costumes": "costume",
              "facts": "fact", "sources": "source", "rights": "rights"}

def pick(path, data):
    ref = data.get("$schema", "")
    for name in SCHEMAS:
        if ref.endswith(f"{name}.schema.json"): return name
    if path.parent.name in DIR_SCHEMA: return DIR_SCHEMA[path.parent.name]
    stem = path.stem.lower()
    for name in sorted(SCHEMAS, key=len, reverse=True):
        if stem.startswith(name): return name
    return None

def check(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    name = pick(path, data)
    if not name: return (path, "NO_SCHEMA", [])
    schema = SCHEMAS[name]
    v = Draft7Validator(schema, resolver=RefResolver(schema["$id"], schema, store=STORE))
    errs = [f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in v.iter_errors(data)]
    return (path, name, errs)

INSTANCES = sorted(ROOT.glob("02_SEASONS/*/*/episode.json")) + \
            sorted(p for p in ROOT.glob("05_HISTORY_DATABASE/*/*.json")) + \
            sorted(ROOT.glob("02_SEASONS/*/*/07_SHOTS/*.json")) + \
            sorted(ROOT.glob("02_SEASONS/*/*/10_BLENDER/camera_*.json")) + \
            sorted(ROOT.glob("02_SEASONS/*/*/1[12]_AI_*/prompt_*.json")) + \
            sorted(ROOT.glob("08_GENERATION_CACHE/*/cost_*.json")) + sorted(ROOT.glob("08_GENERATION_CACHE/*/approval_*.json")) + \
            sorted(ROOT.glob("08_GENERATION_CACHE/*/generation_*.json"))

LITE_SLOTS = {"full_body", "walking", "costume_detail"}

def pack_rules(p, d, costumes):
    """D-008 master pack tier + D-011 costume TBD gate."""
    errs, rel = [], p.relative_to(ROOT)
    tier, pack = d.get("master_pack_tier", "FULL"), d.get("master_pack", {})
    required = LITE_SLOTS if tier == "LITE_CROWD" else set(pack)
    for slot, v in pack.items():
        if v["status"] == "NOT_REQUIRED" and slot in required:
            errs.append(f"{rel}: master_pack.{slot} is required for tier {tier} (D-008)")
    if d.get("status") == "CHARACTER_MASTER_APPROVED":
        missing = [s for s in required if pack.get(s, {}).get("status") != "APPROVED"]
        if missing: errs.append(f"{rel}: CHARACTER_MASTER_APPROVED but not APPROVED: {', '.join(sorted(missing))}")
    if any(v["status"] in ("DRAFT", "APPROVED") for v in pack.values()):
        for cid in d.get("costume_ids", []):
            tbd = [k for k, v in costumes.get(cid, {}).get("elements", {}).items() if "TBD" in v]
            if tbd: errs.append(f"{rel}: master pack started while {cid} still TBD ({', '.join(tbd)}) (D-011)")
    return errs

RANK = {"FACT": 3, "PROBABLE": 2, "INTERPRETIVE": 1, "ARTISTIC": 0}
EVIDENCE_PIPES = {"ARCHIVE", "HIGGSFIELD", "AI_STILL", "BLENDER_FLOW"}

def ledger_rules(p, d, facts, rights, routers):
    """P3 (정본 §9 §10, D-013): source-less shot / unresolved rights / over-interpretation -> FAIL."""
    errs, rel = [], p.relative_to(ROOT)
    role = d.get("evidence_role")
    if role is None:
        errs.append(f"{rel}: evidence_role missing (D-013)"); return errs
    if role != "NONE" and not d.get("fact_ids"):
        errs.append(f"{rel}: evidence_role {role} but no fact_ids (source-less shot)")
    if d["pipeline"] in EVIDENCE_PIPES and role == "NONE":
        errs.append(f"{rel}: {d['pipeline']} shot cannot have evidence_role NONE")
    if d["pipeline"] == "ARCHIVE" and not d.get("rights_ids"):
        errs.append(f"{rel}: ARCHIVE shot without rights_ids (unresolved rights)")
    for r in d.get("rights_ids", []):
        if rights.get(r, {}).get("status") == "RED":
            errs.append(f"{rel}: uses RED rights {r}")
        if rights.get(r, {}).get("usage_tier") == "BACKUP_ONLY":
            errs.append(f"{rel}: references BACKUP_ONLY rights {r} - promote to ACTIVE first (D-014)")
    rid = d.get("router_decision_id")
    if d["pipeline"] in ("AI_STILL", "BLENDER_FLOW", "HIGGSFIELD") and not rid:
        errs.append(f"{rel}: AI pipeline without router_decision_id (no router output)")
    if rid:
        r = routers.get(rid)
        if not r: errs.append(f"{rel}: router_decision_id -> unknown router '{rid}'")
        elif r["shot_id"] != d["shot_id"]: errs.append(f"{rel}: router {rid} belongs to {r['shot_id']}")
        elif r["human_decision"] != "OVERRIDDEN" and r["recommended_pipeline"] != d["pipeline"]:
            errs.append(f"{rel}: pipeline {d['pipeline']} != router recommendation {r['recommended_pipeline']} (not OVERRIDDEN)")
    fs = [facts[c] for c in d.get("fact_ids", []) if c in facts]
    if fs:
        best = max(RANK[f["confidence"]] for f in fs)
        if RANK[d["historical_confidence"]] > best:
            errs.append(f"{rel}: historical_confidence {d['historical_confidence']} exceeds strongest fact ({[k for k,v in RANK.items() if v==best][0]}) - over-interpretation")
    if d["pipeline"] in ("HIGGSFIELD", "AI_STILL", "BLENDER_FLOW", "FLOW_VEO") and not d.get("ai_label"):
        errs.append(f"{rel}: AI pipeline without ai_label")
    return errs

def refcheck(paths):
    """Cross-reference check for real instances (not templates): every referenced ID must exist."""
    ids, docs = {}, []
    key = {"era": "era_id", "location": "location_id", "character": "character_id", "costume": "costume_id",
           "fact": "claim_id", "source": "source_id", "rights": "rights_id", "router_decision": "decision_id",
           "camera": "camera_id", "prompt": "prompt_id", "master_frame": "frame_id",
           "scene": "scene_id", "shot": "shot_id", "episode": "episode_id"}
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8")); name = pick(p, data)
        if name in key: ids.setdefault(name, set()).add(data.get(key[name])); docs.append((p, name, data))
    costumes = {d["costume_id"]: d for _, n, d in docs if n == "costume"}
    facts = {d["claim_id"]: d for _, n, d in docs if n == "fact"}
    rights = {d["rights_id"]: d for _, n, d in docs if n == "rights"}
    routers = {d["decision_id"]: d for _, n, d in docs if n == "router_decision"}
    has = lambda kind, v: v in ids.get(kind, set())
    errs = []
    def need(p, kind, vals, field):
        for v in ([vals] if isinstance(vals, str) else vals or []):
            if v != "NONE" and not has(kind, v): errs.append(f"{p.relative_to(ROOT)}: {field} -> unknown {kind} '{v}'")
    for p, name, d in docs:
        if name in ("shot", "scene"):
            need(p, "era", d.get("era"), "era"); need(p, "location", d.get("location"), "location")
            need(p, "character", d.get("characters"), "characters")
        if name == "shot":
            need(p, "costume", d.get("costumes"), "costumes"); need(p, "scene", d.get("scene_id"), "scene_id")
            need(p, "fact", d.get("fact_ids"), "fact_ids"); need(p, "rights", d.get("rights_ids"), "rights_ids")
            errs.extend(ledger_rules(p, d, facts, rights, routers))
        if name == "scene":
            need(p, "shot", d.get("shot_ids"), "shot_ids")
            if d.get("master_frame"): need(p, "master_frame", d["master_frame"], "master_frame")
        if name == "shot":
            for kind, field in (("camera", "camera_id"), ("prompt", "prompt_id"), ("master_frame", "master_frame")):
                if d.get(field): need(p, kind, d[field], field)
        if name == "camera" and d.get("shot_id"): need(p, "shot", d["shot_id"], "shot_id")
        if name == "prompt" and not str(d.get("shot_id", "")).startswith("MASTER_PACK:"): need(p, "shot", d["shot_id"], "shot_id")
        if name == "prompt":
            # reference_images entries "master_frame:<frame_id>" / "character_pack:<character_id>" must resolve (P2 rule)
            for r in d.get("reference_images") or []:
                kind, _, v = str(r).partition(":")
                if kind == "master_frame": need(p, "master_frame", v, "reference_images")
                elif kind == "character_pack": need(p, "character", v, "reference_images")
        if name == "master_frame":
            need(p, "scene", d["scene_id"], "scene_id"); need(p, "shot", d.get("derived_shots"), "derived_shots")
            need(p, "character", d.get("characters"), "characters"); need(p, "location", d["location"], "location")
            if d.get("camera_id"): need(p, "camera", d["camera_id"], "camera_id")
        if name == "character":
            need(p, "era", d.get("era"), "era"); need(p, "costume", d.get("costume_ids"), "costume_ids")
            errs.extend(pack_rules(p, d, costumes))
        if name in ("location", "costume"): need(p, "era", d.get("era"), "era")
        if name == "fact":
            need(p, "source", d.get("source_ids"), "source_ids")
            if d["confidence"] in ("INTERPRETIVE", "ARTISTIC") and not d.get("hedge_required"):
                errs.append(f"{p.relative_to(ROOT)}: {d['confidence']} claim must set hedge_required=true")
        if name == "episode":
            need(p, "era", d.get("era_ids"), "era_ids"); need(p, "location", d.get("location_ids"), "location_ids")
            need(p, "character", d.get("character_ids"), "character_ids"); need(p, "scene", d.get("scene_ids"), "scene_ids")
    return errs

targets = [Path(a) for a in sys.argv[1:]] or sorted((HERE / "examples").glob("*.json")) + INSTANCES
bad = 0
for t in targets:
    path, name, errs = check(t)
    tag = "PASS" if not errs and name != "NO_SCHEMA" else "FAIL"
    if tag == "FAIL": bad += 1
    print(f"[{tag}] {path.relative_to(ROOT) if ROOT in path.parents else path}  ({name})")
    for e in errs: print("       -", e)
print(f"\n{len(targets) - bad}/{len(targets)} passed")
if not sys.argv[1:]:
    ref_errs = refcheck(INSTANCES)
    print(f"cross-reference: {'OK' if not ref_errs else f'{len(ref_errs)} broken'}")
    for e in ref_errs: print("       -", e)
    bad += len(ref_errs)
sys.exit(1 if bad else 0)
