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

def pick(path, data):
    ref = data.get("$schema", "")
    for name in SCHEMAS:
        if ref.endswith(f"{name}.schema.json"): return name
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

targets = [Path(a) for a in sys.argv[1:]] or sorted((HERE / "examples").glob("*.json")) + \
          sorted(ROOT.glob("02_SEASONS/*/*/episode.json"))
bad = 0
for t in targets:
    path, name, errs = check(t)
    tag = "PASS" if not errs and name != "NO_SCHEMA" else "FAIL"
    if tag == "FAIL": bad += 1
    print(f"[{tag}] {path.relative_to(ROOT) if ROOT in path.parents else path}  ({name})")
    for e in errs: print("       -", e)
print(f"\n{len(targets) - bad}/{len(targets)} passed")
sys.exit(1 if bad else 0)
