#!/usr/bin/env python3
"""Generate NEXUS trailer world backdrops, characters, and music bed."""
from __future__ import annotations

import math
import random
import struct
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORLDS = ROOT / "SourceAssets" / "worlds"
CHARS = ROOT / "SourceAssets" / "characters"
AUDIO = ROOT / "SourceAssets" / "audio"
W, H = 1920, 1080


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def save_jpg(im: Image.Image, name: str) -> None:
    im.convert("RGB").save(WORLDS / name, quality=92, optimize=True)


def save_png(im: Image.Image, name: str) -> None:
    im.save(CHARS / name, optimize=True)


def vignette(im: Image.Image, strength: float = 0.55) -> Image.Image:
    overlay = Image.new("RGB", im.size, (0, 0, 0))
    mask = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((-200, -150, W + 200, H + 150), fill=int(255 * strength))
    mask = mask.filter(ImageFilter.GaussianBlur(120))
    return Image.composite(overlay, im, mask)


def matrix_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (2, 8, 4))
    d = ImageDraw.Draw(im)
    f = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18)
    rng = random.Random(1)
    glyphs = "01アイウエオカキクケコαβγΣ¥$#<>/\\"
    for x in range(0, W, 22):
        y = rng.randint(-40, 40)
        while y < H:
            ch = rng.choice(glyphs)
            g = 40 + rng.randint(0, 180)
            d.text((x, y), ch, fill=(20, g, 40), font=f)
            y += 22
    # site chrome
    d.rounded_rectangle((120, 100, 1800, 980), radius=18, outline=(0, 255, 120), width=2)
    d.rectangle((120, 100, 1800, 160), fill=(0, 40, 20))
    title = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 36)
    d.text((150, 112), "NEXUS://matrix.site", fill=(120, 255, 160), font=title)
    return vignette(im)


def ascii_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (8, 8, 10))
    d = ImageDraw.Draw(im)
    f = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
    rng = random.Random(2)
    dens = "@%#*+=-:. "
    for y in range(0, H, 14):
        row = "".join(dens[rng.randint(0, len(dens) - 1)] for _ in range(140))
        d.text((40, y), row, fill=(180, 180, 190), font=f)
    d.rectangle((200, 180, 1720, 900), outline=(240, 240, 255), width=3)
    big = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 72)
    d.text((260, 240), "ASCII://HOME", fill=(255, 255, 255), font=big)
    return vignette(im, 0.4)


def glass_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (12, 16, 28))
    d = ImageDraw.Draw(im, "RGBA")
    for i, col in enumerate([(40, 80, 200), (180, 60, 220), (20, 180, 200)]):
        x = 220 + i * 420
        d.rounded_rectangle((x, 220, x + 360, 820), radius=28, fill=(*col, 90), outline=(255, 255, 255, 140), width=2)
    base = im.convert("RGB").filter(ImageFilter.GaussianBlur(1))
    d2 = ImageDraw.Draw(base)
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    d2.text((240, 140), "GLASS OS", fill=(230, 240, 255), font=t)
    return vignette(base)


def neon_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (4, 2, 12))
    d = ImageDraw.Draw(im)
    for i in range(0, W, 80):
        d.line((i, 0, i, H), fill=(30, 0, 60), width=1)
    for i in range(0, H, 80):
        d.line((0, i, W, i), fill=(30, 0, 60), width=1)
    # perspective floor
    for i in range(20):
        y = 600 + i * i * 1.2
        if y < H:
            d.line((0, y, W, y), fill=(255, 0, 180), width=1)
    for x in (-800, -400, 0, 400, 800, 1200, 1600, 2000, 2400):
        d.line((960, 580, x, H), fill=(0, 220, 255), width=2)
    glow = im.filter(ImageFilter.GaussianBlur(3))
    im = Image.blend(im, glow, 0.45)
    d = ImageDraw.Draw(im)
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    d.text((160, 120), "NEON GRID", fill=(0, 255, 255), font=t)
    return vignette(im)


def brutalist_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (240, 236, 228))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 220), fill=(10, 10, 10))
    d.rectangle((0, 700, 900, H), fill=(10, 10, 10))
    d.rectangle((1100, 300, W, H), fill=(210, 40, 30))
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
    d.text((40, 40), "BUILD", fill=(255, 255, 255), font=t)
    t2 = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
    d.text((40, 740), "NOW", fill=(255, 255, 255), font=t2)
    return im


def chrome_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (18, 18, 22))
    d = ImageDraw.Draw(im)
    for y in range(H):
        v = int(30 + 90 * abs(math.sin(y / 70)))
        d.line((0, y, W, y), fill=(v, v, v + 8))
    # metallic panels
    for i in range(5):
        x0 = 180 + i * 320
        d.rounded_rectangle((x0, 260, x0 + 280, 860), radius=16, outline=(220, 220, 230), width=3)
        for yy in range(280, 840, 8):
            c = 80 + int(120 * (0.5 + 0.5 * math.sin((yy + i * 40) / 40)))
            d.line((x0 + 20, yy, x0 + 260, yy), fill=(c, c, c + 10))
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
    d.text((200, 120), "LIQUID CHROME", fill=(240, 245, 255), font=t)
    return vignette(im)


def blueprint_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (8, 28, 70))
    d = ImageDraw.Draw(im)
    for i in range(0, W, 40):
        d.line((i, 0, i, H), fill=(20, 60, 120))
    for i in range(0, H, 40):
        d.line((0, i, W, i), fill=(20, 60, 120))
    d.rectangle((240, 180, 1680, 900), outline=(120, 200, 255), width=2)
    d.ellipse((700, 320, 1220, 760), outline=(180, 230, 255), width=2)
    d.line((240, 180, 1680, 900), fill=(90, 170, 230), width=1)
    d.line((1680, 180, 240, 900), fill=(90, 170, 230), width=1)
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 48)
    d.text((260, 120), "BLUEPRINT / v0.9", fill=(160, 220, 255), font=t)
    return vignette(im)


def hud_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (4, 10, 16))
    d = ImageDraw.Draw(im)
    cyan = (0, 230, 255)
    for box in [(80, 80, 520, 320), (1400, 80, 1840, 360), (80, 720, 600, 1000), (1280, 700, 1840, 1000)]:
        d.rectangle(box, outline=cyan, width=2)
        d.line((box[0], box[1] + 28, box[2], box[1] + 28), fill=cyan)
    # crosshair
    d.ellipse((860, 440, 1060, 640), outline=cyan, width=2)
    d.line((960, 400, 960, 680), fill=cyan)
    d.line((820, 540, 1100, 540), fill=cyan)
    mono = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 22)
    d.text((100, 90), "SYS.LOCK // 98.2%", fill=cyan, font=mono)
    d.text((1420, 90), "VECTOR FIELD", fill=cyan, font=mono)
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    d.text((700, 160), "HOLO HUD", fill=(200, 255, 255), font=t)
    return vignette(im)


def crt_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (10, 18, 10))
    d = ImageDraw.Draw(im)
    for y in range(0, H, 3):
        d.line((0, y, W, y), fill=(0, 0, 0))
    f = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 64)
    d.text((200, 200), "> BOOT SEQUENCE", fill=(80, 255, 80), font=f)
    f2 = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 36)
    d.text((200, 320), "loading aesthetic.exe...", fill=(60, 200, 60), font=f2)
    d.text((200, 400), "OK  phosphor persistence", fill=(60, 200, 60), font=f2)
    d.rectangle((160, 160, 1760, 920), outline=(40, 120, 40), width=8)
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    return vignette(im, 0.65)


def polygon_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (14, 12, 22))
    d = ImageDraw.Draw(im)
    rng = random.Random(10)
    pts = [(rng.randint(0, W), rng.randint(200, H)) for _ in range(40)]
    # terrain fan
    for i in range(len(pts) - 2):
        tri = [pts[i], pts[i + 1], (960, 200)]
        c = (40 + (i * 17) % 120, 60 + (i * 9) % 100, 120 + (i * 13) % 100)
        d.polygon(tri, fill=c, outline=(220, 220, 255))
    # angular UI
    d.polygon([(80, 80), (520, 80), (480, 200), (80, 200)], fill=(30, 30, 50), outline=(255, 255, 255))
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
    d.text((110, 110), "POLY.SITE", fill=(255, 255, 255), font=t)
    return vignette(im)


def west_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (40, 22, 14))
    d = ImageDraw.Draw(im)
    # sunset sky
    for y in range(0, 620):
        r = int(40 + y * 0.25)
        g = int(20 + y * 0.08)
        b = int(14 + y * 0.02)
        d.line((0, y, W, y), fill=(min(r, 255), min(g, 180), min(b, 80)))
    d.ellipse((1320, 120, 1520, 320), fill=(255, 180, 60))
    d.rectangle((0, 620, W, H), fill=(62, 40, 24))
    # wanted poster panel
    d.rectangle((620, 140, 1300, 920), fill=(235, 220, 180), outline=(40, 20, 10), width=6)
    serif = font("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 72)
    d.text((700, 180), "WANTED", fill=(40, 10, 10), font=serif)
    serif2 = font("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 36)
    d.text((690, 280), "a website with grit", fill=(60, 30, 20), font=serif2)
    d.rectangle((700, 360, 1220, 780), outline=(40, 20, 10), width=3)
    return vignette(im, 0.35)


def chaos_world() -> Image.Image:
    im = Image.new("RGB", (W, H), (8, 8, 8))
    d = ImageDraw.Draw(im)
    rng = random.Random(99)
    for _ in range(80):
        x0, y0 = rng.randint(0, W), rng.randint(0, H)
        x1, y1 = x0 + rng.randint(80, 420), y0 + rng.randint(60, 280)
        col = (rng.randint(20, 255), rng.randint(20, 255), rng.randint(20, 255))
        d.rectangle((x0, y0, x1, y1), fill=col, outline=(255, 255, 255))
    t = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
    d.text((120, 80), "MAXIMAL", fill=(255, 255, 0), font=t)
    d.text((120, 170), "CHAOS", fill=(255, 0, 180), font=t)
    return vignette(im, 0.3)


WORLD_BUILDERS = [
    ("01-matrix.jpg", matrix_world),
    ("02-ascii.jpg", ascii_world),
    ("03-glass.jpg", glass_world),
    ("04-neon.jpg", neon_world),
    ("05-brutalist.jpg", brutalist_world),
    ("06-chrome.jpg", chrome_world),
    ("07-blueprint.jpg", blueprint_world),
    ("08-hud.jpg", hud_world),
    ("09-crt.jpg", crt_world),
    ("10-polygon.jpg", polygon_world),
    ("11-west.jpg", west_world),
    ("12-chaos.jpg", chaos_world),
]


def character(kind: str, color: tuple[int, int, int], style: str) -> Image.Image:
    im = Image.new("RGBA", (700, 1000), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx, cy = 350, 520

    if style == "matrix":
        d.ellipse((cx - 70, 120, cx + 70, 260), fill=(*color, 230))
        d.polygon([(cx, 260), (cx - 140, 700), (cx + 140, 700)], fill=(*color, 210))
        d.rectangle((cx - 40, 700, cx - 5, 920), fill=(*color, 220))
        d.rectangle((cx + 5, 700, cx + 40, 920), fill=(*color, 220))
    elif style == "ascii":
        f = font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 28)
        art = [
            "  ####  ",
            " #    # ",
            "#  ..  #",
            " #    # ",
            "  ####  ",
            "   ||   ",
            "  /||\\  ",
            " / || \\ ",
            "   ||   ",
            "  /  \\  ",
            " /    \\ ",
        ]
        y = 160
        for line in art:
            d.text((180, y), line, fill=(*color, 255), font=f)
            y += 50
    elif style == "glass":
        d.rounded_rectangle((200, 140, 500, 880), radius=40, fill=(*color, 120), outline=(255, 255, 255, 200), width=3)
        d.ellipse((270, 200, 430, 360), fill=(255, 255, 255, 90))
    elif style == "neon":
        pts = [(cx, 140), (cx - 90, 400), (cx - 40, 400), (cx - 60, 900), (cx - 20, 900), (cx, 520), (cx + 20, 900), (cx + 60, 900), (cx + 40, 400), (cx + 90, 400)]
        d.line(pts + [pts[0]], fill=(*color, 255), width=6)
        d.ellipse((cx - 55, 150, cx + 55, 260), outline=(*color, 255), width=6)
    elif style == "brutal":
        d.rectangle((220, 120, 480, 320), fill=(*color, 255))
        d.rectangle((250, 320, 450, 720), fill=(*color, 255))
        d.rectangle((250, 720, 330, 940), fill=(*color, 255))
        d.rectangle((370, 720, 450, 940), fill=(*color, 255))
    elif style == "chrome":
        for i, a in enumerate(range(220, 40, -20)):
            d.ellipse((220 + i, 140 + i, 480 - i, 880 - i), outline=(min(255, color[0] + i * 3),) * 3 + (a,))
        d.ellipse((270, 200, 430, 360), fill=(230, 230, 240, 200))
    elif style == "wire":
        d.ellipse((cx - 60, 150, cx + 60, 270), outline=(*color, 255), width=3)
        d.line([(cx, 270), (cx, 620), (cx - 100, 900)], fill=(*color, 255), width=3)
        d.line([(cx, 620), (cx + 100, 900)], fill=(*color, 255), width=3)
        d.line([(cx, 360), (cx - 120, 520)], fill=(*color, 255), width=3)
        d.line([(cx, 360), (cx + 120, 520)], fill=(*color, 255), width=3)
    elif style == "hud":
        d.polygon([(cx, 140), (cx + 80, 260), (cx + 50, 260), (cx + 50, 700), (cx + 90, 900), (cx + 40, 900), (cx, 740), (cx - 40, 900), (cx - 90, 900), (cx - 50, 700), (cx - 50, 260), (cx - 80, 260)], outline=(*color, 255), width=3)
        d.ellipse((cx - 40, 170, cx + 40, 250), outline=(*color, 255), width=3)
    elif style == "crt":
        d.ellipse((cx - 70, 140, cx + 70, 280), fill=(*color, 160))
        d.rectangle((cx - 50, 280, cx + 50, 700), fill=(*color, 140))
        d.rectangle((cx - 70, 700, cx - 20, 920), fill=(*color, 140))
        d.rectangle((cx + 20, 700, cx + 70, 920), fill=(*color, 140))
        for y in range(140, 920, 4):
            d.line((cx - 80, y, cx + 80, y), fill=(0, 0, 0, 60))
    elif style == "poly":
        d.polygon([(cx, 120), (cx + 120, 280), (cx + 40, 280), (cx + 90, 900), (cx + 10, 900), (cx, 500), (cx - 10, 900), (cx - 90, 900), (cx - 40, 280), (cx - 120, 280)], fill=(*color, 230), outline=(255, 255, 255, 255))
        d.polygon([(cx - 40, 160), (cx + 40, 160), (cx + 55, 240), (cx - 55, 240)], fill=(30, 30, 40, 255), outline=(255, 255, 255, 255))
    elif style == "west":
        # cowboy silhouette
        d.ellipse((cx - 55, 200, cx + 55, 310), fill=(*color, 255))
        d.polygon([(cx - 120, 180), (cx + 120, 180), (cx + 90, 210), (cx - 90, 210)], fill=(*color, 255))  # brim
        d.rectangle((cx - 40, 160, cx + 40, 200), fill=(*color, 255))  # crown
        d.polygon([(cx, 310), (cx - 110, 700), (cx + 110, 700)], fill=(*color, 255))
        d.rectangle((cx - 35, 700, cx - 5, 940), fill=(*color, 255))
        d.rectangle((cx + 5, 700, cx + 35, 940), fill=(*color, 255))
    else:  # chaos
        rng = random.Random(7)
        for _ in range(18):
            x0 = rng.randint(120, 500)
            y0 = rng.randint(100, 850)
            d.rectangle((x0, y0, x0 + rng.randint(40, 120), y0 + rng.randint(40, 160)), fill=(*rng.choice([(255, 0, 180), (255, 255, 0), (0, 255, 255), (255, 80, 0)]), 200))
        d.ellipse((cx - 60, 160, cx + 60, 280), fill=(255, 255, 255, 230))
    return im


CHAR_SPECS = [
    ("01-matrix.png", (0, 255, 120), "matrix"),
    ("02-ascii.png", (240, 240, 255), "ascii"),
    ("03-glass.png", (120, 180, 255), "glass"),
    ("04-neon.png", (0, 255, 255), "neon"),
    ("05-brutal.png", (20, 20, 20), "brutal"),
    ("06-chrome.png", (200, 205, 220), "chrome"),
    ("07-wire.png", (140, 210, 255), "wire"),
    ("08-hud.png", (0, 230, 255), "hud"),
    ("09-crt.png", (80, 255, 80), "crt"),
    ("10-poly.png", (120, 90, 255), "poly"),
    ("11-west.png", (20, 10, 5), "west"),
    ("12-chaos.png", (255, 0, 180), "chaos"),
]


def write_music(path: Path, seconds: float = 48.0, sr: int = 44100) -> None:
    """Synthetic driving tech bed — no external music dependency."""
    n = int(seconds * sr)
    rng = random.Random(42)
    frames = bytearray()
    for i in range(n):
        t = i / sr
        # kick every 0.5s
        kick_phase = (t % 0.5) / 0.5
        kick = math.exp(-kick_phase * 18) * math.sin(2 * math.pi * (80 + 40 * kick_phase) * t) * 0.55
        # hat
        hat = 0.0
        if (t % 0.25) < 0.03:
            hat = (rng.random() * 2 - 1) * 0.12 * math.exp(-(t % 0.25) * 80)
        # bass pulse
        bass = 0.22 * math.sin(2 * math.pi * 55 * t) * (0.5 + 0.5 * math.sin(2 * math.pi * 2 * t))
        # arpeggio
        arp_notes = [220, 277, 330, 370, 440, 554]
        note = arp_notes[int(t * 4) % len(arp_notes)]
        arp = 0.09 * math.sin(2 * math.pi * note * t) * (0.5 + 0.5 * math.sin(2 * math.pi * 8 * t))
        # riser into parade (~14s) and end
        riser = 0.0
        if 12.5 < t < 14.2:
            riser = (t - 12.5) / 1.7 * 0.2 * (rng.random() * 2 - 1)
        if 37.5 < t < 38.5:
            riser = (t - 37.5) * 0.25 * math.sin(2 * math.pi * 600 * t)
        sample = max(-1.0, min(1.0, kick + hat + bass + arp + riser))
        # soft fade in/out
        if t < 0.4:
            sample *= t / 0.4
        if t > seconds - 0.8:
            sample *= max(0.0, (seconds - t) / 0.8)
        val = int(sample * 30000)
        frames += struct.pack("<h", val)
    with wave.open(str(path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(frames)


def main() -> None:
    WORLDS.mkdir(parents=True, exist_ok=True)
    CHARS.mkdir(parents=True, exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)
    for name, builder in WORLD_BUILDERS:
        print("world", name)
        save_jpg(builder(), name)
    for name, color, style in CHAR_SPECS:
        print("char", name)
        save_png(character(name, color, style), name)
    music = AUDIO / "nexus-bed.wav"
    print("music", music)
    write_music(music, 48.0)
    print("done")


if __name__ == "__main__":
    main()
