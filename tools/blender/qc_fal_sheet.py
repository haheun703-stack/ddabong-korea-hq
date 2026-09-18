# -*- coding: utf-8 -*-
"""D-057 H07 trial sheet: Blender guide vs yesterday's Higgsfield vs today's fal depth-controlled."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = r"H:\00. 클로드 봇 프로그램 모음_260801\3. 따봉 코리아_유튜브 모음_260814\ddabong-korea-hq"
BV2 = os.path.join(ROOT, "08_GENERATION_CACHE", "EP01", "BLENDER_V02")
BPR = os.path.join(ROOT, "08_GENERATION_CACHE", "EP01", "BLENDER_PHOTOREAL")
FAL = os.path.join(ROOT, "08_GENERATION_CACHE", "EP01", "FAL_PHOTOREAL")
OUT = os.path.join(FAL, "QC_H07_FAL_V01_vs_HIGGSFIELD.jpg")


def kfont(size=18):
    for p in (r"C:\Windows\Fonts\malgun.ttf", r"C:\Windows\Fonts\gulim.ttc"):
        try: return ImageFont.truetype(p, size)
        except OSError: pass
    return ImageFont.load_default()
F = kfont(18)

TILES = [
    (os.path.join(BV2, "CAM_S08_SH002_H07_beauty.png"), "Blender 질감 렌더 (기준 구도)"),
    (os.path.join(BV2, "CAM_S08_SH002_H07_depth.png"), "depth 패스 (fal 에 넣은 구조)"),
    (os.path.join(BPR, "H07_BL_V02_bb3c07bd.png"), "어제 Higgsfield (크기·카메라 드리프트)"),
    (os.path.join(FAL, "CAM_S08_SH002_H07_FAL_V01_0.png"), "fal 후보 1 — 사진 OK / 크기 작음"),
    (os.path.join(FAL, "CAM_S08_SH002_H07_FAL_V01_1.png"), "fal 후보 2 — 사진 OK / 크기 작음"),
    (os.path.join(FAL, "CAM_S08_SH002_H07_FAL_V01_2.png"), "fal 후보 3 — 사진 OK / 크기 작음"),
    (os.path.join(FAL, "CAM_S08_SH002_H07_FAL_V01_3.png"), "fal 후보 4 — 사진 OK / 크기 작음"),
]

CW, CH, PAD, HDR = 660, 377, 6, 28
COLS = 2
rows = (len(TILES) + COLS - 1) // COLS
W = COLS * (CW + PAD) + PAD
H = rows * (CH + HDR + PAD) + PAD
sheet = Image.new("RGB", (W, H), (20, 20, 22))
d = ImageDraw.Draw(sheet)

for i, (p, label) in enumerate(TILES):
    r, c = divmod(i, COLS)
    x = PAD + c * (CW + PAD); y = PAD + r * (CH + HDR + PAD)
    d.text((x + 4, y + 6), label, fill=(255, 208, 88), font=F)
    if not os.path.exists(p):
        d.text((x + 4, y + HDR + 12), "(없음) " + os.path.basename(p), fill=(210, 90, 90), font=F); continue
    im = Image.open(p).convert("RGB")
    im.thumbnail((CW, CH), Image.LANCZOS)
    sheet.paste(im, (x + (CW - im.width) // 2, y + HDR + (CH - im.height) // 2))

sheet.save(OUT, quality=91)
print("SAVED", OUT, sheet.size)
