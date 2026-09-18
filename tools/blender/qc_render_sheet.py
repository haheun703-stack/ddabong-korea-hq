# -*- coding: utf-8 -*-
"""D-057 track 1 QC sheet: yesterday's clay vs today's beauty/normal/mask, per shot."""
import os
from PIL import Image, ImageDraw, ImageFont

def kfont(size=17):
    for p in (r"C:\Windows\Fonts\malgun.ttf", r"C:\Windows\Fonts\malgunsl.ttf",
              r"C:\Windows\Fonts\gulim.ttc", r"C:\Windows\Fonts\batang.ttc"):
        try: return ImageFont.truetype(p, size)
        except OSError: pass
    return ImageFont.load_default()
FONT = kfont(17)

ROOT = r"H:\00. 클로드 봇 프로그램 모음_260801\3. 따봉 코리아_유튜브 모음_260814\ddabong-korea-hq"
OLD = os.path.join(ROOT, "08_GENERATION_CACHE", "EP01", "BLENDER")
NEW = os.path.join(ROOT, "08_GENERATION_CACHE", "EP01", "BLENDER_V02")
OUT = os.path.join(NEW, "QC_RENDER_V02_vs_CLAY.jpg")

SHOTS = [
    ("CAM_S08_SH002_H07", "H07 완성 봉분"),
    ("CAM_S06_SH010_H06", "H06 봉토 원경"),
    ("CAM_S06_SH005_H05", "H05 원로 뒷모습"),
    ("CAM_S04_SH005", "S04_SH005 목곽"),
]
COLS = [("clay", OLD, "어제 clay (입력)"), ("beauty", NEW, "오늘 beauty (질감)"),
        ("normal", NEW, "normal (기하)"), ("mask", NEW, "mask (영역)")]

CW, CH, PAD, HDR = 620, 349, 6, 26
W = len(COLS) * (CW + PAD) + PAD
H = len(SHOTS) * (CH + HDR + PAD) + PAD
sheet = Image.new("RGB", (W, H), (22, 22, 24))
d = ImageDraw.Draw(sheet)

for r, (cam, label) in enumerate(SHOTS):
    y = PAD + r * (CH + HDR + PAD)
    for c, (mode, base, cname) in enumerate(COLS):
        x = PAD + c * (CW + PAD)
        p = os.path.join(base, f"{cam}_{mode}.png")
        d.text((x + 3, y + 6), f"{label} | {cname}", fill=(255, 210, 90), font=FONT)
        if not os.path.exists(p):
            d.text((x + 3, y + HDR + 10), "(없음)", fill=(200, 90, 90), font=FONT); continue
        im = Image.open(p).convert("RGB").resize((CW, CH), Image.LANCZOS)
        sheet.paste(im, (x, y + HDR))

sheet.save(OUT, quality=92)
print("SAVED", OUT, sheet.size)
