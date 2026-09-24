#!/usr/bin/env python3
"""Build the NEXUS trailer Tesseract project and apply motion keyframes."""
from __future__ import annotations

import json
import subprocess
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TSRCT = Path.home() / ".local/share/Tesseract/bin/tsrct"
PROJECT = ROOT / "NexusTrailer.tsrct"
EDITABLE = ROOT / ".tesseract-work" / "editable.json"

WORLDS = [
    ("world-matrix", "01-matrix.jpg", "char-matrix", "01-matrix.png", "MATRIX"),
    ("world-ascii", "02-ascii.jpg", "char-ascii", "02-ascii.png", "ASCII"),
    ("world-glass", "03-glass.jpg", "char-glass", "03-glass.png", "GLASS 3D"),
    ("world-neon", "04-neon.jpg", "char-neon", "04-neon.png", "NEON GRID"),
    ("world-brutal", "05-brutalist.jpg", "char-brutal", "05-brutal.png", "BRUTALIST"),
    ("world-chrome", "06-chrome.jpg", "char-chrome", "06-chrome.png", "CHROME"),
    ("world-blue", "07-blueprint.jpg", "char-wire", "07-wire.png", "BLUEPRINT"),
    ("world-hud", "08-hud.jpg", "char-hud", "08-hud.png", "HOLO HUD"),
    ("world-crt", "09-crt.jpg", "char-crt", "09-crt.png", "CRT"),
    ("world-poly", "10-polygon.jpg", "char-poly", "10-poly.png", "POLYGON"),
    ("world-west", "11-west.jpg", "char-west", "11-west.png", "WILD WEST"),
    ("world-chaos", "12-chaos.jpg", "char-chaos", "12-chaos.png", "CHAOS"),
]

DURATION_S = 48.0
DURATION_MS = 48000


def run(args: list[str]) -> str:
    out = subprocess.check_output([str(TSRCT), *args], text=True)
    print(out.strip())
    return out


def wav_ms(path: Path) -> int:
    with wave.open(str(path), "r") as wf:
        return int(wf.getnframes() / wf.getframerate() * 1000)


def transform(ax: float, ay: float, x: float, y: float, sx: float = 100, sy: float = 100, rot: float = 0, op: float = 100) -> dict:
    return {
        "anchorPoint": [ax, ay],
        "position": [x, y],
        "scale": [sx, sy],
        "rotation": rot,
        "opacity": op,
    }


def make_text(
    lid: int,
    name: str,
    start: int,
    dur: int,
    pos: tuple[float, float],
    text: str,
    family: str,
    style: str,
    size: int,
    color: list,
    box_size: tuple[float, float],
    justify: str = "left",
    opacity: float = 100,
) -> dict:
    return {
        "type": "Text",
        "id": lid,
        "name": name,
        "blendMode": "normal",
        "activeRange": {"start": start, "duration": dur},
        "transform": transform(0, 0, pos[0], pos[1], 100, 100, 0, opacity),
        "sourceText": {
            "text": text,
            "fontFamily": family,
            "fontStyle": style,
            "fontSize": size,
            "fillColor": color,
            "justification": justify,
            "boxText": True,
            "boxPosition": [0, 0],
            "boxSize": [box_size[0], box_size[1]],
        },
    }


def make_rect(lid: int, name: str, start: int, dur: int, pos: tuple, size: tuple, color: list, opacity: float = 100) -> dict:
    return {
        "type": "Rect",
        "id": lid,
        "name": name,
        "blendMode": "normal",
        "activeRange": {"start": start, "duration": dur},
        "transform": transform(0, 0, pos[0], pos[1], 100, 100, 0, opacity),
        "rect": {"size": [size[0], size[1]], "fillColor": color},
    }


def make_image(lid: int, name: str, start: int, dur: int, asset: str, pos: tuple, anchor: tuple, scale: float = 100, opacity: float = 100, fit: str = "cover") -> dict:
    return {
        "type": "Image",
        "id": lid,
        "name": name,
        "blendMode": "normal",
        "activeRange": {"start": start, "duration": dur},
        "transform": transform(anchor[0], anchor[1], pos[0], pos[1], scale, scale, 0, opacity),
        "source": {"assetId": asset, "fit": fit},
    }


def make_audio(lid: int, name: str, asset: str, start: int, dur: int, intrinsic: int, volume: float, src_start: int = 0) -> dict:
    return {
        "type": "Audio",
        "id": lid,
        "name": name,
        "windowMs": DURATION_MS,
        "activeRange": {"start": start, "duration": dur},
        "sourceRange": {"start": src_start, "duration": dur},
        "sourceIntrinsicDuration": intrinsic,
        "source": {"assetId": asset},
        "volume": volume,
        "captionsEnabled": False,
    }


def import_all() -> None:
    fonts = [
        ROOT / "SourceAssets/fonts/Inter-Bold.ttf",
        ROOT / "SourceAssets/fonts/Inter-Regular.ttf",
        ROOT / "SourceAssets/fonts/Inter-SemiBold.ttf",
        ROOT / "SourceAssets/fonts/JetBrainsMono-Bold.ttf",
        ROOT / "SourceAssets/fonts/JetBrainsMono-Regular.ttf",
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"),
    ]
    for f in fonts:
        if f.exists():
            run(["project", "import-font", "--project", str(PROJECT), "--file", str(f)])

    for asset_id, fname, _cid, _cf, _label in WORLDS:
        run(
            [
                "project",
                "import-asset",
                "--project",
                str(PROJECT),
                "--kind",
                "image",
                "--asset-id",
                asset_id,
                "--file",
                str(ROOT / "SourceAssets/worlds" / fname),
            ]
        )
    for _wid, _wf, asset_id, fname, _label in WORLDS:
        run(
            [
                "project",
                "import-asset",
                "--project",
                str(PROJECT),
                "--kind",
                "image",
                "--asset-id",
                asset_id,
                "--file",
                str(ROOT / "SourceAssets/characters" / fname),
            ]
        )

    for asset_id, fname in [
        ("music", "nexus-bed.wav"),
        ("whoosh", "whoosh.wav"),
        ("impact", "impact.wav"),
        ("click", "click.wav"),
        ("ping", "ping.wav"),
        ("riser", "riser.wav"),
    ]:
        run(
            [
                "project",
                "import-asset",
                "--project",
                str(PROJECT),
                "--kind",
                "audio",
                "--asset-id",
                asset_id,
                "--file",
                str(ROOT / "SourceAssets/audio" / fname),
            ]
        )


def build_layers() -> list[dict]:
    layers: list[dict] = []
    lid = 1

    # Full black base
    layers.append(make_rect(lid, "Void", 0, DURATION_MS, (0, 0), (1920, 1080), [0.02, 0.02, 0.04, 1]))
    lid += 1

    # --- HOOK 0-6000 ---
    layers.append(make_rect(lid, "Cursor", 400, 5200, (240, 520), (18, 56), [0.0, 0.95, 1.0, 1]))
    cursor_id = lid
    lid += 1
    layers.append(
        make_text(
            lid,
            "Prompt",
            900,
            5100,
            (280, 500),
            "a site that feels like the future",
            "JetBrains Mono",
            "Regular",
            42,
            [0.85, 0.95, 1.0, 1],
            (1500, 100),
        )
    )
    prompt_id = lid
    lid += 1

    # --- PRODUCT 6000-14000 ---
    layers.append(make_rect(lid, "AppPanel", 6000, 8000, (160, 120), (1600, 840), [0.06, 0.08, 0.12, 0.92]))
    lid += 1
    layers.append(make_rect(lid, "AppAccent", 6000, 8000, (160, 120), (1600, 8), [0.0, 0.9, 1.0, 1]))
    lid += 1
    layers.append(
        make_text(
            lid,
            "AppTitle",
            6200,
            7800,
            (220, 160),
            "NEXUS",
            "Inter",
            "Bold",
            72,
            [0.95, 0.98, 1.0, 1],
            (600, 100),
        )
    )
    lid += 1
    layers.append(
        make_text(
            lid,
            "AppSub",
            6400,
            7600,
            (220, 250),
            "AI website generator",
            "Inter",
            "Regular",
            32,
            [0.55, 0.65, 0.75, 1],
            (800, 60),
        )
    )
    lid += 1
    layers.append(make_rect(lid, "PromptBox", 7000, 7000, (220, 360), (1200, 72), [0.02, 0.04, 0.08, 1]))
    lid += 1
    layers.append(
        make_text(
            lid,
            "PromptInApp",
            7200,
            6800,
            (240, 375),
            "> describe anything impossible…",
            "JetBrains Mono",
            "Regular",
            28,
            [0.5, 0.9, 1.0, 1],
            (1100, 50),
        )
    )
    lid += 1
    layers.append(make_rect(lid, "GenerateBtn", 9000, 5000, (1480, 360), (220, 72), [1.0, 0.2, 0.7, 1]))
    gen_btn = lid
    lid += 1
    layers.append(
        make_text(
            lid,
            "GenerateLabel",
            9000,
            5000,
            (1510, 375),
            "GENERATE",
            "Inter",
            "Bold",
            26,
            [1, 1, 1, 1],
            (180, 50),
        )
    )
    lid += 1

    # --- PARADE 14000-38000 (12 x 2000) ---
    char_ids = []
    world_ids = []
    for i, (wid, _wf, cid, _cf, label) in enumerate(WORLDS):
        start = 14000 + i * 2000
        layers.append(make_image(lid, f"World-{label}", start, 2000, wid, (960, 540), (960, 540), 100, 100, "cover"))
        world_ids.append(lid)
        lid += 1
        layers.append(make_rect(lid, f"LabelBg-{label}", start, 2000, (64, 64), (360, 56), [0, 0, 0, 0.65]))
        lid += 1
        layers.append(
            make_text(
                lid,
                f"Label-{label}",
                start,
                2000,
                (80, 72),
                label,
                "Inter",
                "Bold",
                28,
                [0.9, 0.95, 1.0, 1],
                (320, 50),
            )
        )
        lid += 1
        # character emerges lower-right, moves toward center-front
        layers.append(
            make_image(
                lid,
                f"Char-{label}",
                start,
                2000,
                cid,
                (1500, 780),
                (350, 900),
                55,
                100,
                "contain",
            )
        )
        char_ids.append(lid)
        lid += 1

    # --- PAYOFF mosaic 38000-42000 ---
    # show a grid of 6 world thumbs
    mosaic_assets = [WORLDS[i][0] for i in (0, 3, 5, 9, 10, 11)]
    positions = [(320, 300), (960, 300), (1600, 300), (320, 780), (960, 780), (1600, 780)]
    for asset, pos in zip(mosaic_assets, positions):
        layers.append(make_image(lid, f"Mosaic-{asset}", 38000, 4000, asset, pos, (480, 270), 48, 100, "cover"))
        lid += 1
    layers.append(
        make_text(
            lid,
            "MosaicTitle",
            38500,
            3500,
            (460, 480),
            "infinite styles",
            "Inter",
            "Bold",
            64,
            [1, 1, 1, 1],
            (1000, 90),
            "center",
        )
    )
    lid += 1

    # --- END CARD 42000-48000 ---
    layers.append(make_rect(lid, "EndVoid", 42000, 6000, (0, 0), (1920, 1080), [0.02, 0.02, 0.05, 1]))
    lid += 1
    layers.append(
        make_text(
            lid,
            "EndLogo",
            42400,
            5600,
            (610, 380),
            "NEXUS",
            "Inter",
            "Bold",
            120,
            [0.95, 0.98, 1.0, 1],
            (700, 150),
            "center",
        )
    )
    end_logo = lid
    lid += 1
    layers.append(
        make_text(
            lid,
            "EndTag",
            43200,
            4800,
            (460, 560),
            "Generate the impossible.",
            "Inter SemiBold",
            "Regular",
            40,
            [0.0, 0.9, 1.0, 1],
            (1000, 70),
            "center",
        )
    )
    lid += 1
    layers.append(make_rect(lid, "EndLine", 43000, 5000, (760, 540), (400, 3), [1.0, 0.25, 0.75, 1]))
    lid += 1

    # --- AUDIO ---
    music_ms = wav_ms(ROOT / "SourceAssets/audio/nexus-bed.wav")
    layers.append(make_audio(lid, "MusicBed", "music", 0, DURATION_MS, music_ms, 0.28))
    lid += 1
    whoosh_ms = wav_ms(ROOT / "SourceAssets/audio/whoosh.wav")
    impact_ms = wav_ms(ROOT / "SourceAssets/audio/impact.wav")
    click_ms = wav_ms(ROOT / "SourceAssets/audio/click.wav")
    ping_ms = wav_ms(ROOT / "SourceAssets/audio/ping.wav")
    riser_ms = wav_ms(ROOT / "SourceAssets/audio/riser.wav")

    # click on prompt, ping on generate, riser into parade, whoosh+impact each world cut
    layers.append(make_audio(lid, "SFX-click", "click", 900, click_ms, click_ms, 0.55))
    lid += 1
    layers.append(make_audio(lid, "SFX-ping", "ping", 9000, ping_ms, ping_ms, 0.45))
    lid += 1
    layers.append(make_audio(lid, "SFX-riser", "riser", 13000, riser_ms, riser_ms, 0.4))
    lid += 1
    for i in range(12):
        t = 14000 + i * 2000
        layers.append(make_audio(lid, f"SFX-whoosh-{i}", "whoosh", t, whoosh_ms, whoosh_ms, 0.35))
        lid += 1
        layers.append(make_audio(lid, f"SFX-impact-{i}", "impact", t + 80, impact_ms, impact_ms, 0.4))
        lid += 1
    layers.append(make_audio(lid, "SFX-end", "impact", 42000, impact_ms, impact_ms, 0.5))
    lid += 1

    # Document array order: index 0 is topmost.
    layers.reverse()

    meta = {
        "cursor_id": cursor_id,
        "prompt_id": prompt_id,
        "gen_btn": gen_btn,
        "char_ids": char_ids,
        "world_ids": world_ids,
        "end_logo": end_logo,
    }
    (ROOT / ".tesseract-work" / "layer-meta.json").write_text(json.dumps(meta, indent=2))
    return layers


def commit_document(layers: list[dict]) -> None:
    run(["project", "checkout", "--project", str(PROJECT), "--output", str(EDITABLE)])
    doc = json.loads(EDITABLE.read_text())
    doc["dimensions"] = {"width": 1920, "height": 1080}
    doc["duration"] = DURATION_S
    doc["composition"]["layers"] = layers
    EDITABLE.write_text(json.dumps(doc, indent=2))
    run(["project", "commit", "--project", str(PROJECT), "--file", str(EDITABLE)])


def keyframe(id_: str, layer_time: int, value: float, easing: str = "cubic") -> dict:
    ease = {"type": "linear"} if easing == "linear" else {"type": "cubicBezier", "x1": 0.2, "y1": 0.0, "x2": 0.2, "y2": 1.0}
    return {
        "id": id_,
        "layerTime": layer_time,
        "value": {"type": "float", "value": value},
        "easing": ease,
    }


def apply_motion() -> None:
    meta = json.loads((ROOT / ".tesseract-work" / "layer-meta.json").read_text())
    actions: list[dict] = []

    # cursor blink via opacity
    cid = meta["cursor_id"]
    actions.append(
        {
            "type": "setFxPropertyKeyframes",
            "compositionId": "main",
            "property": {"layerId": cid, "propertyType": "opacity"},
            "keyframes": [
                keyframe("c0", 0, 100, "linear"),
                keyframe("c1", 200, 0, "linear"),
                keyframe("c2", 400, 100, "linear"),
                keyframe("c3", 600, 0, "linear"),
                keyframe("c4", 800, 100, "linear"),
                keyframe("c5", 2000, 100, "linear"),
                keyframe("c6", 2200, 0, "linear"),
                keyframe("c7", 2400, 100, "linear"),
            ],
        }
    )

    # characters: scale + position + opacity burst
    for i, ch in enumerate(meta["char_ids"]):
        actions.append(
            {
                "type": "setFxPropertyKeyframes",
                "compositionId": "main",
                "property": {"layerId": ch, "propertyType": "opacity"},
                "keyframes": [
                    keyframe(f"cho{i}a", 0, 0, "linear"),
                    keyframe(f"cho{i}b", 180, 100),
                    keyframe(f"cho{i}c", 1600, 100, "linear"),
                    keyframe(f"cho{i}d", 2000, 0),
                ],
            }
        )
        actions.append(
            {
                "type": "setFxPropertyKeyframes",
                "compositionId": "main",
                "property": {"layerId": ch, "propertyType": "scaleX"},
                "keyframes": [
                    keyframe(f"csx{i}a", 0, 45),
                    keyframe(f"csx{i}b", 700, 95),
                    keyframe(f"csx{i}c", 2000, 110),
                ],
            }
        )
        actions.append(
            {
                "type": "setFxPropertyKeyframes",
                "compositionId": "main",
                "property": {"layerId": ch, "propertyType": "scaleY"},
                "keyframes": [
                    keyframe(f"csy{i}a", 0, 45),
                    keyframe(f"csy{i}b", 700, 95),
                    keyframe(f"csy{i}c", 2000, 110),
                ],
            }
        )
        actions.append(
            {
                "type": "setFxPositionKeyframes",
                "compositionId": "main",
                "layerId": ch,
                "positionX": {
                    "keyframes": [
                        keyframe(f"cpx{i}a", 0, 1580),
                        keyframe(f"cpx{i}b", 900, 1180),
                        keyframe(f"cpx{i}c", 2000, 980),
                    ]
                },
                "positionY": {
                    "keyframes": [
                        keyframe(f"cpy{i}a", 0, 820),
                        keyframe(f"cpy{i}b", 900, 720),
                        keyframe(f"cpy{i}c", 2000, 640),
                    ]
                },
            }
        )

        # world slight zoom
        wid = meta["world_ids"][i]
        actions.append(
            {
                "type": "setFxPropertyKeyframes",
                "compositionId": "main",
                "property": {"layerId": wid, "propertyType": "scaleX"},
                "keyframes": [keyframe(f"wsx{i}a", 0, 100), keyframe(f"wsx{i}b", 2000, 112)],
            }
        )
        actions.append(
            {
                "type": "setFxPropertyKeyframes",
                "compositionId": "main",
                "property": {"layerId": wid, "propertyType": "scaleY"},
                "keyframes": [keyframe(f"wsy{i}a", 0, 100), keyframe(f"wsy{i}b", 2000, 112)],
            }
        )

    # generate button pulse
    gb = meta["gen_btn"]
    actions.append(
        {
            "type": "setFxPropertyKeyframes",
            "compositionId": "main",
            "property": {"layerId": gb, "propertyType": "scaleX"},
            "keyframes": [
                keyframe("gba", 0, 100),
                keyframe("gbb", 200, 108),
                keyframe("gbc", 450, 100),
            ],
        }
    )

    actions_path = ROOT / ".tesseract-work" / "motion.json"
    actions_path.write_text(json.dumps(actions, indent=2))
    run(["project", "apply", "--project", str(PROJECT), "--actions", str(actions_path)])


def main() -> None:
    if PROJECT.exists():
        PROJECT.unlink()
    run(["project", "create", "--project", str(PROJECT)])
    import_all()
    layers = build_layers()
    commit_document(layers)
    apply_motion()
    print("PROJECT_READY", PROJECT)


if __name__ == "__main__":
    main()
