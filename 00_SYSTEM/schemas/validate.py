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
              "facts": "fact", "sources": "source"}

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
            sorted(ROOT.glob("02_SEASONS/*/*/07_SHOTS/*.json"))

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

def refcheck(paths):
    """Cross-reference check for real instances (not templates): every referenced ID must exist."""
    ids, docs = {}, []
    key = {"era": "era_id", "location": "location_id", "character": "character_id", "costume": "costume_id",
           "fact": "claim_id", "source": "source_id", "scene": "scene_id", "shot": "shot_id", "episode": "episode_id"}
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8")); name = pick(p, data)
        if name in key: ids.setdefault(name, set()).add(data.get(key[name])); docs.append((p, name, data))
    costumes = {d["costume_id"]: d for _, n, d in docs if n == "costume"}
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
            need(p, "fact", d.get("fact_ids"), "fact_ids")
        if name == "scene": need(p, "shot", d.get("shot_ids"), "shot_ids")
        if name == "character":
            need(p, "era", d.get("era"), "era"); need(p, "costume", d.get("costume_ids"), "costume_ids")
            errs.extend(pack_rules(p, d, costumes))
        if name in ("location", "costume"): need(p, "era", d.get("era"), "era")
        if name == "fact": need(p, "source", d.get("source_ids"), "source_ids")
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
