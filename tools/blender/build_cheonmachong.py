# -*- coding: utf-8 -*-
"""
DDABONG EP01 - Cheonmachong construction-site master scene (D-053, Phase 1).
Run headless:
  blender -b --python tools/blender/build_cheonmachong.py -- --out 08_GENERATION_CACHE/EP01/BLENDER --save 04_BLENDER_LIBRARY/scenes/EP01_CHEONMACHONG_MASTER_V01.blend [--only CAM_ID,...] [--passes clay,depth,line]
Spec: 02_SEASONS/S01/EP01/10_BLENDER/SCENE_SPEC_CHEONMACHONG_V01.md
FACT dims: mound 47 m dia / 12.7 m high; chamber 6.6 x 4.2 m; coffin 2.15 x 0.8 m (CLM_EP01_STRUCT_004). Everything else is shape-only (INTERPRETIVE).
"""
import bpy, bmesh, math, random, sys, os, argparse
from mathutils import Vector

# ---------------- args ----------------
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ap = argparse.ArgumentParser()
ap.add_argument("--out", default="08_GENERATION_CACHE/EP01/BLENDER")
ap.add_argument("--save", default="")
ap.add_argument("--only", default="")
ap.add_argument("--passes", default="clay,depth,line")
ap.add_argument("--res", default="1920x1080")
ap.add_argument("--anim", default="")
ap.add_argument("--anim_seconds", type=float, default=5.0)
ap.add_argument("--anim_amount", type=float, default=0.18)
A = ap.parse_args(argv)
OUT = os.path.abspath(A.out); os.makedirs(OUT, exist_ok=True)
random.seed(7)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.unit_settings.system = 'METRIC'

# ---------------- helpers ----------------
def coll(name, parent=None):
    c = bpy.data.collections.new(name); (parent or sc.collection).children.link(c); return c

def link(obj, c):
    for uc in obj.users_collection: uc.objects.unlink(obj)
    c.objects.link(obj)

def mat(name, rgb):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color = (*rgb, 1); m.use_nodes = False; return m

M_EARTH = mat("earth", (0.42, 0.34, 0.24)); M_STONE = mat("stone", (0.55, 0.55, 0.52)); M_WOOD = mat("wood", (0.50, 0.36, 0.20))
M_GRASS = mat("grass", (0.36, 0.42, 0.25)); M_PROXY = mat("proxy", (0.80, 0.78, 0.72)); M_RED = mat("dimension_red", (0.85, 0.10, 0.10)); M_WHITE = mat("white", (0.9, 0.9, 0.9))

def box(name, size, loc, c, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.name = name
    o.scale = size; o.rotation_euler = rot; o.data.materials.append(m); link(o, c); return o

def revolve_mound(name, radius, height, c, m, exp=0.62, rings=48, segs=96):
    """Rounded Silla-style mound: h(r) = H * (1 - (r/R)^2)^exp, revolved."""
    bm = bmesh.new(); prev = None
    for i in range(rings + 1):
        r = radius * i / rings; h = height * max(0.0, 1 - (r / radius) ** 2) ** exp
        ring = []
        if i == 0: ring = [bm.verts.new((0, 0, h))]
        else:
            for j in range(segs):
                a = 2 * math.pi * j / segs; ring.append(bm.verts.new((r * math.cos(a), r * math.sin(a), h)))
        if prev:
            for j in range(segs):
                if len(prev) == 1: bm.faces.new((prev[0], ring[j], ring[(j + 1) % segs]))
                else: bm.faces.new((prev[j], ring[j], ring[(j + 1) % segs], prev[(j + 1) % segs]))
        prev = ring
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free(); me.materials.append(m)
    o = bpy.data.objects.new(name, me); sc.collection.objects.link(o); link(o, c)
    for p in me.polygons: p.use_smooth = True
    return o

def stones(name, c, radius, height, count):
    """Rounded pile of river stones over the chamber (shape only, INTERPRETIVE)."""
    # river stones ~20-40 cm (shape only); a solid inner dome carries the bulk so the pile reads as a mass, stones skin the surface
    dome = revolve_mound(name + "_core", radius * 0.97, height * 0.96, c, M_STONE, exp=0.7)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=0.16); base = bpy.context.object; base.name = name + "_base"; base.data.materials.append(M_STONE); link(base, c)
    me = base.data; objs = []
    for k in range(count):
        a = random.uniform(0, 2 * math.pi); r = radius * math.sqrt(random.random())
        h = height * max(0.0, 1 - (r / radius) ** 2) ** 0.7
        o = bpy.data.objects.new(f"{name}_{k}", me); o.location = (r * math.cos(a), r * math.sin(a), h)
        o.rotation_euler = (random.random() * 3, random.random() * 3, random.random() * 3); s = random.uniform(0.8, 1.5); o.scale = (s, s * 0.85, s * 0.6)
        c.objects.link(o); objs.append(o)
    base.hide_render = True; base.hide_viewport = True
    return objs

def proxy(name, height, loc, facing_deg, c):
    """Mannequin proxy: body cylinder + head sphere. Replaced by master-pack humans at the Higgsfield stage."""
    bpy.ops.mesh.primitive_cylinder_add(radius=0.19, depth=height * 0.78, location=(loc[0], loc[1], height * 0.39)); b = bpy.context.object; b.name = name + "_body"; b.data.materials.append(M_PROXY); link(b, c)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(loc[0], loc[1], height * 0.78 + 0.13)); h = bpy.context.object; h.name = name + "_head"; h.data.materials.append(M_PROXY); link(h, c)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(loc[0] + 0.12 * math.cos(math.radians(facing_deg)), loc[1] + 0.12 * math.sin(math.radians(facing_deg)), height * 0.78 + 0.13)); n = bpy.context.object; n.name = name + "_nose"; n.scale = (0.05, 0.05, 0.05); n.data.materials.append(M_PROXY); link(n, c)

def dim_line(name, p0, p1, c, thick=0.12):
    v = Vector(p1) - Vector(p0); L = v.length; mid = (Vector(p0) + Vector(p1)) / 2
    bpy.ops.mesh.primitive_cylinder_add(radius=thick, depth=L, location=mid); o = bpy.context.object; o.name = name
    o.rotation_euler = v.to_track_quat('Z', 'Y').to_euler(); o.data.materials.append(M_RED); link(o, c)
    for p in (p0, p1):
        bpy.ops.mesh.primitive_cylinder_add(radius=thick, depth=thick * 14, location=p); t = bpy.context.object; t.name = name + "_tick"
        t.rotation_euler = (0, 0, 0) if abs(v.z) < 1e-6 and abs(v.y) < 1e-6 else (0, math.pi / 2, 0); t.data.materials.append(M_RED); link(t, c)

def label(name, text, loc, size, c, rot=(math.pi / 2, 0, 0)):
    bpy.ops.object.text_add(location=loc); t = bpy.context.object; t.name = name; t.data.body = text; t.data.size = size
    t.data.align_x = 'CENTER'; t.rotation_euler = rot; t.data.materials.append(M_RED); t.data.extrude = 0.05; link(t, c)

# ---------------- world / ground ----------------
import json, re, struct
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "02_SEASONS", "S01", "EP01", "10_BLENDER", "data")
M_THATCH = mat("thatch", (0.62, 0.52, 0.33)); M_PATH = mat("path_dirt", (0.47, 0.40, 0.30))
C_ENV = coll("ENV")
bpy.ops.mesh.primitive_plane_add(size=2600); g = bpy.context.object; g.name = "Ground"; g.data.materials.append(M_GRASS); link(g, C_ENV)

# real terrain (AWS terrain tiles, z12 3x3, ~24 km). Flattened inside 1.2 km (basin floor = ground plane), full relief beyond 2.6 km -> real mountain skyline
C_TERR = coll("ENV_TERRAIN")
def load_terrain(c):
    p = os.path.join(DATA, "TERRAIN_HEIGHTMAP_Z12_step2.bin")
    if not os.path.exists(p): print("NO TERRAIN", p); return
    with open(p, "rb") as f:
        nx, ny = struct.unpack("<ii", f.read(8)); X = struct.unpack(f"<{nx}f", f.read(4 * nx)); Y = struct.unpack(f"<{ny}f", f.read(4 * ny)); Zs = struct.unpack(f"<{nx*ny}f", f.read(4 * nx * ny))
    verts = []
    for j in range(ny):
        for i in range(nx):
            r = math.hypot(X[i], Y[j]); w = 0.0 if r < 1200 else (1.0 if r > 2600 else (r - 1200) / 1400)
            verts.append((X[i], Y[j], max(0.0, Zs[j * nx + i]) * w - 0.08))
    faces = [(j * nx + i, (j + 1) * nx + i, (j + 1) * nx + i + 1, j * nx + i + 1) for j in range(ny - 1) for i in range(nx - 1)]
    me = bpy.data.meshes.new("Terrain"); me.from_pydata(verts, [], faces); me.materials.append(M_GRASS)
    for pgn in me.polygons: pgn.use_smooth = True
    o = bpy.data.objects.new("Terrain_Gyeongju", me); c.objects.link(o)
load_terrain(C_TERR)

# real Daereungwon tomb layout (OpenStreetMap outlines, 2026-09-17). OSM outline of Cheonmachong = 53.5 m vs FACT 47 m -> scale 0.88 applied to all.
# heights = diameter x 0.27 (Cheonmachong ratio) -> INTERPRETIVE. Elongated outlines (twin mounds, e.g. Hwangnamdaechong) -> two mounds on the long axis.
# dating (CLM_EP01_CHRONO_014): PERIOD = already standing; UNCERTAIN = undated/contemporary -> ghost material; PRESENT = unnamed/present-day only
C_TPER = coll("ENV_TOMBS_PERIOD")
C_TUNC = coll("ENV_TOMBS_UNCERTAIN")
C_TPRE = coll("ENV_TOMBS_PRESENT")
PERIOD_NAMES = ("황남대총", "금관총", "Geumgwanchong")
UNCERTAIN_NAMES = ("봉황대", "검총", "미추왕릉", "금령총", "식리총", "서봉총")
M_GHOST = mat("ghost_uncertain", (0.72, 0.74, 0.70))
def tomb_layer():
    p = os.path.join(DATA, "DAEREUNGWON_OSM_TOMBS_20260917.json")
    if not os.path.exists(p): return
    T = json.load(open(p, encoding="utf-8"))["tombs"]; seen = []
    for t in T:
        nm = t["name_ko"] or t["name_en"] or ""
        if t["osm_way"] == 382249601 or math.hypot(t["x_m"], t["y_m"]) < 25: continue
        if t["historic"] == "archaeological_site" or t["eq_diameter_m"] > 130 or t["eq_diameter_m"] < 10: continue
        if not (t["historic"] == "tomb" or re.search("총|릉|봉황대", nm)): continue
        if any(math.hypot(t["x_m"] - a, t["y_m"] - b) < 15 for a, b in seen): continue
        seen.append((t["x_m"], t["y_m"]))
        pts = t["outline_m"]; n = len(pts); mx = sum(q[0] for q in pts) / n; my = sum(q[1] for q in pts) / n
        sxx = sum((q[0] - mx) ** 2 for q in pts) / n; syy = sum((q[1] - my) ** 2 for q in pts) / n; sxy = sum((q[0] - mx) * (q[1] - my) for q in pts) / n
        ang = 0.5 * math.atan2(2 * sxy, sxx - syy); ux, uy = math.cos(ang), math.sin(ang)
        proj_u = [(q[0] - mx) * ux + (q[1] - my) * uy for q in pts]; proj_v = [-(q[0] - mx) * uy + (q[1] - my) * ux for q in pts]
        L = max(proj_u) - min(proj_u); W = max(proj_v) - min(proj_v)
        if any(k in nm for k in PERIOD_NAMES): c, mt = C_TPER, M_GRASS
        elif any(k in nm for k in UNCERTAIN_NAMES): c, mt = C_TUNC, M_GRASS   # D-054: excluded from construction-time shots, shown only in present-day views
        else: c, mt = C_TPRE, M_GRASS
        if W > 0 and L / W > 1.35:
            d = W * 0.88; off = (L - W) / 2 * 0.88
            for s, sgn in (("A", 1), ("B", -1)):
                o = revolve_mound(f"Tomb_{t['osm_way']}_{s}", d / 2, d * 0.27, c, mt); o.location = (mx + sgn * off * ux, my + sgn * off * uy, 0)
        else:
            d = t["eq_diameter_m"] * 0.88
            o = revolve_mound(f"Tomb_{t['osm_way']}", d / 2, d * 0.27, c, mt); o.location = (mx, my, 0)
tomb_layer()

# construction worksite props (all INTERPRETIVE, shape only, no numbers on screen)
C_WORK = coll("WORKSITE")
def hut(name, x, y, rot):
    bpy.ops.mesh.primitive_cylinder_add(radius=2.0, depth=1.5, location=(x, y, 0.75)); w = bpy.context.object; w.name = name + "_wall"; w.data.materials.append(M_WOOD); link(w, C_WORK)
    bpy.ops.mesh.primitive_cone_add(radius1=2.7, depth=2.3, location=(x, y, 1.5 + 1.15)); r = bpy.context.object; r.name = name + "_roof"; r.data.materials.append(M_THATCH); link(r, C_WORK)
for k, (x, y) in enumerate([(-34, -4), (-37, 7), (-30, -15)]): hut(f"Hut_{k}", x, y, 0)
ss = revolve_mound("StoneStock", 5.5, 2.2, C_WORK, M_STONE); ss.location = (-24, 20, 0)          # river-stone stockpile
for k, (x, y, r, h) in enumerate([(26, 22, 6.5, 3.0), (31, 9, 5.0, 2.4)]):
    e = revolve_mound(f"EarthHeap_{k}", r, h, C_WORK, M_EARTH); e.location = (x, y, 0)          # earth heaps for the mound
bpy.ops.mesh.primitive_torus_add(major_radius=30, minor_radius=1.4, location=(0, 0, 0.02)); tr = bpy.context.object; tr.name = "WorkPathRing"; tr.scale = (1, 1, 0.02); tr.data.materials.append(M_PATH); link(tr, C_WORK)
for k, (a, L) in enumerate([(math.radians(200), 60), (math.radians(35), 45)]):
    box(f"WorkPath_{k}", (L, 2.6, 0.04), ((30 + L / 2) * math.cos(a), (30 + L / 2) * math.sin(a), 0.02), C_WORK, M_PATH, rot=(0, 0, a))

# sun: late afternoon, from camera-left when cameras look north (+Y) -> sun in the WSW, elevation 25 deg (BIBLE v0.2)
bpy.ops.object.light_add(type='SUN', location=(0, 0, 80)); sun = bpy.context.object; sun.name = "Sun_LateAfternoon"
sun.data.energy = 3.5; sun.data.angle = math.radians(1.5)
az, el = math.radians(240), math.radians(25)  # azimuth from +Y clockwise? use direction vector instead
d = Vector((-math.cos(el) * math.sin(az), -math.cos(el) * math.cos(az), -math.sin(el)))
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler(); link(sun, C_ENV)
sc.world = bpy.data.worlds.new("World"); sc.world.color = (0.62, 0.68, 0.75)

# ---------------- tomb core (FACT dims) ----------------
CH_L, CH_W, CH_H = 6.6, 4.2, 2.2   # chamber 6.6 x 4.2 FACT; height shape-only
CF_L, CF_W, CF_H = 2.15, 0.8, 0.75  # coffin FACT

C_S1 = coll("STAGE1_CHAMBER")
# chamber: plank walls (timber), open top
t = 0.18
for nm, size, loc in [("Wall_S", (CH_L, t, CH_H), (0, -CH_W / 2, CH_H / 2)), ("Wall_N", (CH_L, t, CH_H), (0, CH_W / 2, CH_H / 2)),
                      ("Wall_W", (t, CH_W, CH_H), (-CH_L / 2, 0, CH_H / 2)), ("Wall_E", (t, CH_W, CH_H), (CH_L / 2, 0, CH_H / 2)),
                      ("Floor", (CH_L, CH_W, 0.12), (0, 0, 0.06))]:
    box(nm, size, loc, C_S1, M_WOOD)
# corner posts + plank lines (visual only)
for x in (-CH_L / 2, CH_L / 2):
    for y in (-CH_W / 2, CH_W / 2): box(f"Post_{x:+.0f}_{y:+.0f}", (0.3, 0.3, CH_H + 0.4), (x, y, (CH_H + 0.4) / 2), C_S1, M_WOOD)
# coffin, west-shifted, head east (LAYOUT_001)
box("Coffin", (CF_L, CF_W, CF_H), (-0.9, 0, 0.12 + CF_H / 2), C_S1, M_WOOD)
# timber yard (H01) south-west of the chamber
for k in range(14):
    box(f"Beam_{k}", (5.5, 0.25, 0.25), (-13 + random.uniform(-1, 1), -10 + (k % 7) * 0.5, 0.13 + (k // 7) * 0.26), C_S1, M_WOOD, rot=(0, 0, random.uniform(-0.05, 0.05)))

C_S2 = coll("STAGE2_GOODS")
box("GoodsChest", (0.9, 2.2, 0.7), (1.9, 0, 0.12 + 0.35), C_S2, M_WOOD)  # T-shaped to the coffin head (east)
for k in range(6): box(f"Vessel_{k}", (0.3, 0.3, 0.35), (2.6 + (k % 3) * 0.45, -1.4 + (k // 3) * 0.6, 0.12 + 0.18), C_S2, M_STONE)
# H03: low wooden preparation table OUTSIDE the chamber (south-east), plain grey stoneware + folded hemp cloths, no gold (FACT: gold is worn by the occupant)
TX, TY, TH = 5.0, -4.2, 0.62
box("PrepTable_Top", (1.8, 0.8, 0.06), (TX, TY, TH), C_S2, M_WOOD)
for dx in (-0.8, 0.8):
    for dy in (-0.33, 0.33): box(f"PrepTable_Leg_{dx:+.1f}_{dy:+.1f}", (0.07, 0.07, TH - 0.03), (TX + dx, TY + dy, (TH - 0.03) / 2), C_S2, M_WOOD)
for k, (dx, r, hgt) in enumerate([(-0.55, 0.13, 0.30), (-0.2, 0.10, 0.22), (0.12, 0.15, 0.26)]):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=hgt, location=(TX + dx, TY + 0.1, TH + 0.03 + hgt / 2)); v = bpy.context.object; v.name = f"TableVessel_{k}"; v.data.materials.append(M_STONE); link(v, C_S2)
for k in range(3): box(f"HempCloth_{k}", (0.34, 0.26, 0.035), (TX + 0.55, TY - 0.12, TH + 0.05 + k * 0.036), C_S2, M_WHITE)

C_S3 = coll("STAGE3_STONES")
stones("Stone", C_S3, radius=9.0, height=4.2, count=2600)   # shape-only, no numbers on screen
# internal timber framework (CLM_EP01_BUILD_016: posts + cross-beams, concentric, stones piled inside the frame; Jjoksaem 44 / Geumgwanchong).
# Replaces the earlier outer scaffold, which had no evidence. Post count is NOT Jjoksaem's 108 (shape only).
for ring, (rad, n, hgt) in enumerate([(5.0, 12, 4.6), (7.6, 18, 3.4)]):
    tops = []
    for k in range(n):
        a = 2 * math.pi * k / n; x, y = rad * math.cos(a), rad * math.sin(a)
        box(f"FramePost_{ring}_{k}", (0.2, 0.2, hgt), (x, y, hgt / 2), C_S3, M_WOOD); tops.append((x, y))
    for k in range(n):
        (x0, y0), (x1, y1) = tops[k], tops[(k + 1) % n]; L = math.hypot(x1 - x0, y1 - y0); a = math.atan2(y1 - y0, x1 - x0)
        box(f"FrameBeam_{ring}_{k}", (L, 0.14, 0.14), ((x0 + x1) / 2, (y0 + y1) / 2, hgt - 0.25), C_S3, M_WOOD, rot=(0, 0, a))
for k in range(12):   # radial tie beams between rings (lattice)
    a = 2 * math.pi * k / 12
    box(f"FrameRadial_{k}", (2.6, 0.12, 0.12), (6.3 * math.cos(a), 6.3 * math.sin(a), 3.2), C_S3, M_WOOD, rot=(0, 0, a))

# stage-1 layout marking: stakes + cord around the planned mound edge (CLM_EP01_BUILD_016, Jjoksaem 44 step 2)
C_MARK = coll("STAGE1_LAYOUT_MARK")
for k in range(36):
    a = 2 * math.pi * k / 36; box(f"Stake_{k}", (0.07, 0.07, 0.9), (23.5 * math.cos(a), 23.5 * math.sin(a), 0.45), C_MARK, M_WOOD)
bpy.ops.mesh.primitive_torus_add(major_radius=23.5, minor_radius=0.02, location=(0, 0, 0.72)); cord = bpy.context.object; cord.name = "LayoutCord"; cord.data.materials.append(M_THATCH); link(cord, C_MARK)

C_S4 = coll("STAGE4_EARTH_RISING")
revolve_mound("MoundRising", 18.0, 8.0, C_S4, M_EARTH)   # shape-only (about 60%)

C_S5 = coll("STAGE5_COMPLETE")
revolve_mound("MoundComplete", 23.5, 12.7, C_S5, M_EARTH)  # FACT 47 m dia / 12.7 m high

# ---------------- proxies (per-shot, placed in a collection each) ----------------
C_PX = coll("PROXIES")
PX = {
 "H01": [("Lab1", 1.67, (-14.5, -9.2), 60), ("Lab2", 1.67, (-11.6, -10.4), 120)],
 "H02b": [("Lab1", 1.67, (-3, -3.5), 30), ("Lab2", 1.67, (4, 3.2), 200), ("Lab3", 1.67, (-9, 6), 90), ("Att1", 1.68, (5.5, -5), 140)],
 "H03": [("Att1", 1.68, (6.05, -3.55), 250)],
 "H04": [("Elder", 1.72, (0, -6), 90), ("Att1", 1.68, (2, 2), 250), ("Att2", 1.68, (2.8, 1.2), 250), ("Lab1", 1.67, (-4, 8), 300), ("Lab2", 1.67, (-5, 7), 320)],
 "H05": [("Elder", 1.72, (0, -17.5), 90), ("Lab1", 1.67, (-6, 9), 40), ("Lab2", 1.67, (7, 10), 140), ("Lab3", 1.67, (2, 12), 90)],
 "H06": [("Grp1", 1.67, (-26, -20), 30), ("Grp2", 1.67, (-25, -21.2), 30), ("Grp3", 1.67, (30, -8), 150)],
}
PXC = {}
for shot, lst in PX.items():
    c = coll(f"PX_{shot}", C_PX); PXC[shot] = c
    for nm, h, (x, y), f in lst: proxy(f"{shot}_{nm}", h, (x, y), f, c)

# scale bar + dimension lines (G14) in their own collection
C_DIM = coll("DIMENSIONS")
box("ScaleBar10m", (10, 0.4, 0.4), (-35, -28, 0.2), C_DIM, M_RED)
dim_line("Dim_Diameter47", (-23.5, -30, 0.3), (23.5, -30, 0.3), C_DIM)
label("Lbl_47", "47 m", (0, -31.5, 1.2), 3.2, C_DIM)
dim_line("Dim_Height12_7", (26.5, -30, 0), (26.5, -30, 12.7), C_DIM)
label("Lbl_12_7", "12.7 m", (31.5, -30, 6.0), 2.6, C_DIM)
label("Lbl_scale", "10 m", (-30, -29.5, 1.0), 2.0, C_DIM)

# ---------------- cameras ----------------
C_CAM = coll("CAMERAS")
def camera(name, loc, target, lens, ortho=None, portrait=False):
    bpy.ops.object.camera_add(location=loc); cam = bpy.context.object; cam.name = name
    dvec = Vector(target) - Vector(loc); cam.rotation_euler = dvec.to_track_quat('-Z', 'Y').to_euler()
    cam.data.lens = lens; cam.data.clip_end = 40000
    if ortho: cam.data.type = 'ORTHO'; cam.data.ortho_scale = ortho
    cam["portrait"] = portrait; link(cam, C_CAM); return cam

STAGE_SETS = {  # which stage collections are visible
 "S1": ["STAGE1_CHAMBER", "STAGE1_LAYOUT_MARK"], "S2": ["STAGE1_CHAMBER", "STAGE2_GOODS", "STAGE1_LAYOUT_MARK"], "S3": ["STAGE1_CHAMBER", "STAGE2_GOODS", "STAGE3_STONES", "STAGE1_LAYOUT_MARK"],
 "S4": ["STAGE1_CHAMBER", "STAGE2_GOODS", "STAGE3_STONES", "STAGE4_EARTH_RISING"], "S5": ["STAGE5_COMPLETE"],
}
CAMS = [  # (id, stage, proxies, location, target, lens, ortho, portrait, dims)
 ("CAM_S04_SH004_H01", "S1", "H01", (-18, -14, 1.4), (-12.5, -10, 0.6), 35, None, False, False),
 ("CAM_S04_SH005", "S1", None, (0, -12, 1.6), (0, 0, 1.0), 28, None, False, False),
 ("CAM_S04_SH006_H02b", "S1", "H02b", (-22, -26, 2.2), (0, 0, 0.8), 24, None, False, False),
 ("CAM_S05_SH005_H03", "S2", "H03", (5.9, -6.3, 1.0), (4.9, -4.0, 0.72), 50, None, False, False),
 ("CAM_S06_SH002_H04", "S2", "H04", (0, -14, 1.5), (0, 0, 1.2), 28, None, False, False),
 ("CAM_S06_SH005_H05", "S3", "H05", (0.6, -20, 1.5), (0, 0, 2.5), 35, None, False, False),
 ("CAM_S06_SH010_H06", "S4", "H06", (-40, -45, 1.7), (0, 4, 4), 24, None, False, False),
 ("CAM_S08_SH002_H07", "S5", None, (3, -75, 1.6), (0, 5, 5), 35, None, False, False),
 ("CAM_G04_SECTION", "S5", None, (90, 0, 6), (0, 0, 5), 50, 56, False, False),
 ("CAM_G05_BUILD", "S1", None, (-60, -60, 45), (0, 0, 3), 50, 70, False, False),
 ("CAM_G14_ELEVATION", "S5", None, (0, -120, 6), (0, 0, 6), 50, 76, False, True),
 ("CAM_SHORTS_01", "S5", None, (0, -60, 1.5), (0, 0, 8), 24, None, True, False),
 ("CAM_SHORTS_02", "S3", "H05", (0.6, -16, 1.5), (0, 0, 2.5), 35, None, True, False),
 ("CAM_SHORTS_03", "S2", None, (0, -9, 9), (0, 0, 0.5), 35, None, True, False),
 ("CAM_ESTABLISH_AERIAL", "S3", "H05", (-150, -170, 62), (40, 25, 4), 35, None, False, False),
 ("CAM_G03_LANDSCAPE_PRESENT", "S5", None, (60, -620, 360), (40, 90, 0), 50, None, False, False),
]
for cid, st, px, loc, tgt, lens, ortho, portrait, dims in CAMS:
    cam = camera(cid, loc, tgt, lens, ortho, portrait); cam["stage"] = st; cam["proxies"] = px or ""; cam["dims"] = dims

# G04 section: bisected copies of stage-5 mound + stones (x > 0 removed)
C_SEC = coll("SECTION_G04")
for src in ("MoundComplete",):
    o = bpy.data.objects[src].copy(); o.data = o.data.copy(); o.name = src + "_Section"; sc.collection.objects.link(o); link(o, C_SEC)
    bm = bmesh.new(); bm.from_mesh(o.data)
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0), plane_no=(1, 0, 0), clear_outer=True)
    bm.to_mesh(o.data); bm.free()
# stone-dome section: reuse individual stones with x<=0 only
for o in list(C_S3.objects):
    if o.name.startswith("Stone_") and o.location.x <= 0:
        d = o.copy(); d.name = o.name + "_Sec"; C_SEC.objects.link(d)

# ---------------- render ----------------
w, h = [int(v) for v in A.res.lower().split("x")]
def set_visible(names, with_proxies, with_dims, section=False, distant=True, present=False, worksite=None):
    # distant = real terrain + period tombs; present = present-day-only tombs; worksite defaults to "construction stage visible"
    if worksite is None: worksite = distant and "STAGE5_COMPLETE" not in names
    for c in sc.collection.children:
        vis = c.name in names or c.name in ("ENV", "CAMERAS")
        if c.name in ("ENV_TERRAIN", "ENV_TOMBS_PERIOD"): vis = distant
        if c.name == "ENV_TOMBS_UNCERTAIN": vis = present   # D-054 owner: uncertain tombs removed from construction-time scenes
        if c.name == "ENV_TOMBS_PRESENT": vis = present
        if c.name == "WORKSITE": vis = worksite
        if c.name == "PROXIES":
            vis = True
            for sub in c.children: sub.hide_render = sub.name != f"PX_{with_proxies}"
        if c.name == "DIMENSIONS": vis = with_dims
        if c.name == "SECTION_G04": vis = section
        c.hide_render = not vis

def render(cam, tag, mode):
    sc.camera = cam
    portrait = bool(cam.get("portrait")); sc.render.resolution_x, sc.render.resolution_y = (h, w) if portrait else (w, h)
    sc.render.image_settings.file_format = 'PNG'; sc.render.image_settings.color_depth = '16' if mode == "depth" else '8'
    sc.render.engine = 'BLENDER_WORKBENCH'; sh = sc.display.shading
    sh.light = 'STUDIO'; sh.color_type = 'MATERIAL'; sh.show_shadows = True; sh.show_cavity = True; sh.show_object_outline = False
    sc.display.render_aa = '8'
    sc.use_nodes = False
    if mode == "line":
        sh.light = 'FLAT'; sh.color_type = 'SINGLE'; sh.single_color = (0.95, 0.95, 0.95); sh.show_shadows = False; sh.show_cavity = False; sh.show_object_outline = True
    if mode == "depth":
        sc.view_layers[0].use_pass_z = True; sc.use_nodes = True; nt = sc.node_tree
        for n in list(nt.nodes): nt.nodes.remove(n)
        rl = nt.nodes.new('CompositorNodeRLayers'); nz = nt.nodes.new('CompositorNodeNormalize'); comp = nt.nodes.new('CompositorNodeComposite')
        nt.links.new(rl.outputs['Depth'], nz.inputs[0]); nt.links.new(nz.outputs[0], comp.inputs[0])
        sh.light = 'FLAT'; sh.show_shadows = False; sh.show_cavity = False
    sc.render.filepath = os.path.join(OUT, f"{tag}_{mode}.png"); bpy.ops.render.render(write_still=True)
    print("RENDERED", sc.render.filepath)

only = set(A.only.split(",")) if A.only else None
passes = A.passes.split(",")
for cid, st, px, *_ in CAMS:
    if only and cid not in only: continue
    cam = bpy.data.objects[cid]
    if cid == "CAM_G05_BUILD":
        for s in ("S1", "S2", "S3", "S4", "S5"):
            set_visible(STAGE_SETS[s], None, False, distant=False); render(cam, f"{cid}_{s}", "clay")
            set_visible(STAGE_SETS[s], None, False, distant=False); render(cam, f"{cid}_{s}", "line")
        continue
    if cid == "CAM_G04_SECTION":
        set_visible(["STAGE1_CHAMBER", "STAGE2_GOODS"], None, False, section=True, distant=False); render(cam, cid, "clay"); render(cam, cid, "line"); continue
    if cid == "CAM_G03_LANDSCAPE_PRESENT":
        set_visible(STAGE_SETS[st], None, False, distant=True, present=True, worksite=False)
    else:
        set_visible(STAGE_SETS[st], px, bool(cam.get("dims")), distant=not bool(cam.get("dims")))
    for m in passes: render(cam, cid, m)

# optional camera move (Blender camera animation, no jitter): --anim CAM_ID  -> PNG sequence + mp4 via ffmpeg outside
if A.anim:
    cid = A.anim; cam = bpy.data.objects[cid]; st = cam.get("stage"); px = cam.get("proxies") or None
    set_visible(STAGE_SETS[st], px, False, distant=True)
    start = cam.location.copy(); tgt = Vector(dict((c[0], c[4]) for c in CAMS)[cid])
    end = start.lerp(tgt, A.anim_amount)
    sc.frame_start, sc.frame_end = 1, int(A.anim_seconds * 24); sc.render.fps = 24
    cam.location = start; cam.keyframe_insert("location", frame=1)
    cam.location = end; cam.keyframe_insert("location", frame=sc.frame_end)
    for fc in (cam.animation_data.action.fcurves if cam.animation_data and cam.animation_data.action else []):
        for kp in fc.keyframe_points: kp.interpolation = 'BEZIER'; kp.easing = 'EASE_IN_OUT'
    sc.camera = cam; sc.render.engine = 'BLENDER_WORKBENCH'; sh = sc.display.shading
    sh.light = 'STUDIO'; sh.color_type = 'MATERIAL'; sh.show_shadows = True; sh.show_cavity = True; sc.use_nodes = False
    sc.render.resolution_x, sc.render.resolution_y = 1280, 720; sc.render.image_settings.file_format = 'PNG'; sc.render.image_settings.color_depth = '8'
    seq = os.path.join(OUT, f"ANIM_{cid}"); os.makedirs(seq, exist_ok=True); sc.render.filepath = os.path.join(seq, "f_")
    bpy.ops.render.render(animation=True); print("ANIM_RENDERED", seq)

if A.save:
    os.makedirs(os.path.dirname(os.path.abspath(A.save)), exist_ok=True); bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(A.save)); print("SAVED", A.save)
print("DONE")
