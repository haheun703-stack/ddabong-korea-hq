# -*- coding: utf-8 -*-
"""
D-057 track 2: structure-controlled photoreal pass on fal.ai.

Why this exists: Higgsfield's image models take reference images as *content*, not as
geometry, so a Blender clay plate either comes back unchanged or the camera drifts
(see 08_GENERATION_CACHE/EP01/BLENDER_PHOTOREAL/REVIEW_BATCH_A_20260917.md).
fal's flux-general is the one commercial path that exposes structure strength as
numbers: conditioning_scale plus the timestep window start_percentage/end_percentage.
Holding depth only over the first ~45% of steps pins the geometry early and then lets
the surface become a photograph, which is what breaks the copy-vs-drift deadlock.

Geometry comes from Blender's own passes (ground truth), never from a depth estimator
run on the clay PNG - estimating would feed the mound-size error straight back in.

  python tools/api/fal_render.py balance
  python tools/api/fal_render.py shot <CAM_ID> --prompt-file <path> [--out DIR] [--n 4]
        [--depth-scale 0.85] [--depth-end 0.45] [--canny-scale 0.6] [--canny-end 0.30]
        [--steps 30] [--guidance 3.5] [--seed 0] [--dry-run]

Costs money. --dry-run prints the request and the estimated spend without sending.
"""
import os, sys, io, json, time, argparse, base64, mimetypes
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUEUE = "https://queue.fal.run"
MODEL = "fal-ai/flux-general"
# Probed on fal 2026-09-18 (see D-057 notes):
#   jasperai/Flux.1-dev-Controlnet-Depth        -> loads OK
#   Shakker-Labs/FLUX.1-dev-ControlNet-Depth    -> loads OK
#   *-ControlNet-Union-Pro via controlnet_unions -> 422 "controlnet_mode cannot be None"
# So we drive a SINGLE depth controlnet. flux-general accepts only one controlnet per request
# anyway, and start/end_percentage - the reason we came to fal - works the same here.
DEPTH_PATH = "jasperai/Flux.1-dev-Controlnet-Depth"
# The published $0.075/megapixel badly under-predicts reality: on 2026-09-18 the balance fell
# $2.85 across runs whose per-MP estimate summed to ~$0.60, and 512px 6-step probes cost roughly
# $0.25 each (per-MP would say $0.02). flux-general evidently bills GPU time, not pixels, and a
# FAILED job still bills. So the estimator is calibrated on observed spend and deliberately
# pessimistic - it exists to stop surprises, not to be exact. Re-check against the balance.
PRICE_PER_IMAGE_OBSERVED = 0.25   # USD, small/short job floor
PRICE_PER_MP = 0.075              # published figure, kept for reference only


def env():
    d = {}
    p = os.path.join(ROOT, ".env")
    if os.path.exists(p):
        for line in io.open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); d[k.strip()] = v.strip()
    return d


E = env()
KEY = E.get("FAL_KEY", "")


def scrub(s):
    return s.replace(KEY, "<KEY>") if KEY else s


def H(json_ct=True):
    if not KEY:
        sys.exit("FAL_KEY is empty in .env")
    h = {"Authorization": "Key " + KEY}
    if json_ct: h["Content-Type"] = "application/json"
    return h


def balance():
    r = requests.get("https://rest.alpha.fal.ai/billing/user_balance", headers=H(), timeout=30)
    return r.status_code, scrub(r.text)[:200]


def upload(path):
    """fal CDN: initiate -> signed PUT. Returns the public file_url."""
    ct = mimetypes.guess_type(path)[0] or "application/octet-stream"
    r = requests.post("https://rest.alpha.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3",
                      headers=H(), json={"content_type": ct, "file_name": os.path.basename(path)}, timeout=60)
    r.raise_for_status()
    d = r.json()
    with open(path, "rb") as f:
        p = requests.put(d["upload_url"], data=f, headers={"Content-Type": ct}, timeout=300)
    p.raise_for_status()
    return d["file_url"]


def submit(payload):
    r = requests.post(f"{QUEUE}/{MODEL}", headers=H(), json=payload, timeout=120)
    if r.status_code >= 400:
        sys.exit("submit failed %s: %s" % (r.status_code, scrub(r.text)[:500]))
    return r.json()["request_id"]


def wait(request_id, timeout_s=900):
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        r = requests.get(f"{QUEUE}/{MODEL}/requests/{request_id}/status", headers=H(), timeout=60)
        st = r.json().get("status")
        if st == "COMPLETED":
            g = requests.get(f"{QUEUE}/{MODEL}/requests/{request_id}", headers=H(), timeout=120)
            g.raise_for_status(); return g.json()
        if st in ("FAILED", "CANCELLED"):
            sys.exit("job %s: %s" % (st, scrub(r.text)[:400]))
        time.sleep(3)
    sys.exit("timeout waiting for %s" % request_id)


def build(prompt, negative, depth_url, canny_url, w, h, a):
    # FLUX.1-dev is guidance-distilled: a negative_prompt only works under real CFG, and without
    # use_real_cfg the server fails with a blank "Could not load pipeline" (bisected 2026-09-18).
    # Real CFG also doubles inference cost, so negatives are opt-in, not default.
    p = {
        "prompt": prompt,
        "image_size": {"width": w, "height": h},
        "num_inference_steps": a.steps,
        "guidance_scale": a.guidance,
        "num_images": a.n,
        "enable_safety_checker": False,
        "output_format": "png",
        "controlnets": [],
    }
    if depth_url:
        p["controlnets"] = [{
            "path": a.depth_path,
            "control_image_url": depth_url,
            "conditioning_scale": a.depth_scale,
            "start_percentage": 0.0,
            "end_percentage": a.depth_end,   # release the geometry after this fraction of steps
        }]
    if negative and getattr(a, "real_cfg", False):
        p["negative_prompt"] = negative
        p["use_real_cfg"] = True
        p["real_cfg_scale"] = a.real_cfg_scale
    if a.seed: p["seed"] = a.seed
    return p


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("balance")
    s = sub.add_parser("shot")
    s.add_argument("cam")
    s.add_argument("--renders", default="08_GENERATION_CACHE/EP01/BLENDER_V02")
    s.add_argument("--out", default="08_GENERATION_CACHE/EP01/FAL_PHOTOREAL")
    s.add_argument("--prompt-file", required=True, help="JSON with .prompt and optional .negative")
    s.add_argument("--n", type=int, default=4)
    s.add_argument("--steps", type=int, default=30)
    s.add_argument("--guidance", type=float, default=3.5)
    s.add_argument("--seed", type=int, default=0)
    s.add_argument("--depth-scale", type=float, default=0.85)
    s.add_argument("--depth-end", type=float, default=0.45)
    s.add_argument("--canny-scale", type=float, default=0.60)
    s.add_argument("--canny-end", type=float, default=0.30)
    s.add_argument("--no-canny", action="store_true")
    s.add_argument("--invert-canny", action="store_true",
                   help="Blender's line pass is dark-on-white; canny controlnets expect white-on-dark.")
    s.add_argument("--depth-path", default=DEPTH_PATH)
    s.add_argument("--real-cfg", action="store_true",
                   help="send the negative prompt under real CFG. Doubles inference cost.")
    s.add_argument("--real-cfg-scale", type=float, default=3.5)
    s.add_argument("--width", type=int, default=1344)
    s.add_argument("--height", type=int, default=768)
    s.add_argument("--ver", default="V01", help="output version tag; a retry MUST bump this or it overwrites the previous take")
    s.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.cmd == "balance":
        print(*balance()); return

    rd = os.path.join(ROOT, a.renders)
    depth_p = os.path.join(rd, a.cam + "_depth.png")
    line_p = os.path.join(rd, a.cam + "_line.png")
    for p in (depth_p,):
        if not os.path.exists(p): sys.exit("missing pass: " + p)

    spec = json.load(io.open(os.path.join(ROOT, a.prompt_file), encoding="utf-8"))
    prompt, negative = spec["prompt"], spec.get("negative", "")

    mp = (a.width * a.height) / 1_000_000.0
    # scale the observed floor by pixels and steps, both of which drive GPU time
    est = PRICE_PER_IMAGE_OBSERVED * a.n * max(mp, 0.3) / 0.3 * (a.steps / 28.0)
    print("shot=%s  %dx%d  n=%d  steps=%d  est=$%.2f  (observed-rate estimate; a FAILED job still bills)" %
          (a.cam, a.width, a.height, a.n, a.steps, est))
    print("depth scale=%.2f end=%.0f%%   canny scale=%.2f end=%.0f%%   steps=%d" %
          (a.depth_scale, a.depth_end * 100, a.canny_scale, a.canny_end * 100, a.steps))

    canny_send = None
    if not a.no_canny and os.path.exists(line_p):
        canny_send = line_p
        if a.invert_canny:
            from PIL import Image, ImageOps
            im = ImageOps.invert(Image.open(line_p).convert("L")).convert("RGB")
            canny_send = os.path.join(rd, a.cam + "_line_inv.png"); im.save(canny_send)
            print("canny plate inverted ->", os.path.basename(canny_send))

    if a.dry_run:
        pay = build(prompt, negative, "<depth_url>", "<canny_url>" if canny_send else None, a.width, a.height, a)
        print(json.dumps(pay, ensure_ascii=False, indent=2)[:2000]); print("\nDRY RUN - nothing sent, $0 spent"); return

    print("uploading control plates ...")
    depth_url = upload(depth_p)
    canny_url = upload(canny_send) if canny_send else None
    pay = build(prompt, negative, depth_url, canny_url, a.width, a.height, a)

    rid = submit(pay); print("request_id", rid)
    res = wait(rid)
    outd = os.path.join(ROOT, a.out); os.makedirs(outd, exist_ok=True)
    saved = []
    for i, im in enumerate(res.get("images", [])):
        b = requests.get(im["url"], timeout=300).content
        fp = os.path.join(outd, "%s_FAL_%s_%d.png" % (a.cam, a.ver, i))
        open(fp, "wb").write(b); saved.append(fp); print("SAVED", fp)
    meta = {"cam": a.cam, "ver": a.ver, "request_id": rid, "model": MODEL, "depth_path": a.depth_path,
            "controls": pay["controlnets"], "steps": a.steps, "guidance": a.guidance,
            "seed": res.get("seed"), "size": [a.width, a.height], "n": a.n,
            "est_usd": round(est, 4), "outputs": [os.path.relpath(p, ROOT) for p in saved]}
    mp_ = os.path.join(outd, "%s_FAL_%s_meta.json" % (a.cam, a.ver))
    io.open(mp_, "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=2))
    print("META", mp_)


if __name__ == "__main__":
    main()
