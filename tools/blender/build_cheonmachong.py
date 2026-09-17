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
C_ENV = coll("ENV")
bpy.ops.mesh.primitive_plane_add(size=600); g = bpy.context.object; g.name = "Ground"; g.data.materials.append(M_GRASS); link(g, C_ENV)
# distant Daereungwon mounds (existence FACT, positions shape-only)
for i, (x, y, r, h) in enumerate([(170, 120, 18, 9), (-150, 190, 22, 11), (230, -60, 16, 8), (-210, -50, 20, 10), (40, 210, 20, 10)]):
    m = revolve_mound(f"DistantMound_{i}", r, h, C_ENV, M_GRASS); m.location = (x, y, 0)

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

C_S3 = coll("STAGE3_STONES")
stones("Stone", C_S3, radius=9.0, height=4.2, count=2600)   # shape-only, no numbers on screen
# scaffold ring (shape-only): posts + rails around the stone pile
for k in range(14):
    a = 2 * math.pi * k / 14; x, y = 11.5 * math.cos(a), 11.5 * math.sin(a)
    box(f"ScafPost_{k}", (0.22, 0.22, 3.2), (x, y, 1.6), C_S3, M_WOOD)
    box(f"ScafRail_{k}", (0.15, 5.2, 0.15), (x, y, 2.6), C_S3, M_WOOD, rot=(0, 0, a))
    box(f"ScafPlank_{k}", (0.9, 5.0, 0.06), (x * 0.93, y * 0.93, 1.55), C_S3, M_WOOD, rot=(0, 0, a))

C_S4 = coll("STAGE4_EARTH_RISING")
revolve_mound("MoundRising", 18.0, 8.0, C_S4, M_EARTH)   # shape-only (about 60%)

C_S5 = coll("STAGE5_COMPLETE")
revolve_mound("MoundComplete", 23.5, 12.7, C_S5, M_EARTH)  # FACT 47 m dia / 12.7 m high

# ---------------- proxies (per-shot, placed in a collection each) ----------------
C_PX = coll("PROXIES")
PX = {
 "H01": [("Lab1", 1.67, (-14.5, -9.2), 60), ("Lab2", 1.67, (-11.6, -10.4), 120)],
 "H02b": [("Lab1", 1.67, (-3, -3.5), 30), ("Lab2", 1.67, (4, 3.2), 200), ("Lab3", 1.67, (-9, 6), 90), ("Att1", 1.68, (5.5, -5), 140)],
 "H03": [("Att1", 1.68, (3.6, -1.9), 90)],
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
    cam.data.lens = lens; cam.data.clip_end = 2000
    if ortho: cam.data.type = 'ORTHO'; cam.data.ortho_scale = ortho
    cam["portrait"] = portrait; link(cam, C_CAM); return cam

STAGE_SETS = {  # which stage collections are visible
 "S1": ["STAGE1_CHAMBER"], "S2": ["STAGE1_CHAMBER", "STAGE2_GOODS"], "S3": ["STAGE1_CHAMBER", "STAGE2_GOODS", "STAGE3_STONES"],
 "S4": ["STAGE1_CHAMBER", "STAGE2_GOODS", "STAGE3_STONES", "STAGE4_EARTH_RISING"], "S5": ["STAGE5_COMPLETE"],
}
CAMS = [  # (id, stage, proxies, location, target, lens, ortho, portrait, dims)
 ("CAM_S04_SH004_H01", "S1", "H01", (-18, -14, 1.4), (-12.5, -10, 0.6), 35, None, False, False),
 ("CAM_S04_SH005", "S1", None, (0, -12, 1.6), (0, 0, 1.0), 28, None, False, False),
 ("CAM_S04_SH006_H02b", "S1", "H02b", (-22, -26, 2.2), (0, 0, 0.8), 24, None, False, False),
 ("CAM_S05_SH005_H03", "S2", "H03", (5.2, -4.6, 1.1), (2.9, -0.9, 0.55), 50, None, False, False),
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
def set_visible(names, with_proxies, with_dims, section=False):
    for c in sc.collection.children:
        vis = c.name in names or c.name in ("ENV", "CAMERAS")
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
            set_visible(STAGE_SETS[s], None, False); render(cam, f"{cid}_{s}", "clay")
            set_visible(STAGE_SETS[s], None, False); render(cam, f"{cid}_{s}", "line")
        continue
    if cid == "CAM_G04_SECTION":
        set_visible(["STAGE1_CHAMBER", "STAGE2_GOODS"], None, False, section=True); render(cam, cid, "clay"); render(cam, cid, "line"); continue
    set_visible(STAGE_SETS[st], px, bool(cam.get("dims")))
    for m in passes: render(cam, cid, m)

if A.save:
    os.makedirs(os.path.dirname(os.path.abspath(A.save)), exist_ok=True); bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(A.save)); print("SAVED", A.save)
print("DONE")
