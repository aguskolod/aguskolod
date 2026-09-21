#!/usr/bin/env python3
"""Generate an image via OpenRouter Image API and save to disk."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request


DEFAULT_MODEL = "openai/gpt-image-2.5-sunburst"
API_URL = "https://openrouter.ai/api/v1/images"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", help="Prompt string")
    parser.add_argument("--prompt-file", help="Path to prompt text file")
    parser.add_argument("--out", required=True, help="Output image path")
    parser.add_argument("--model", default=os.environ.get("OPENROUTER_IMAGE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--aspect", default="9:16", help="Aspect ratio, e.g. 9:16, 16:9, 1:1")
    parser.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    parser.add_argument("--resolution", default=None, help="Optional tier: 1K, 2K, 4K")
    parser.add_argument(
        "--ref",
        action="append",
        default=[],
        help="Local image path or http(s) URL as input_references (repeatable)",
    )
    args = parser.parse_args()

    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("OPENROUTER_API_KEY is not set", file=sys.stderr)
        return 1

    if args.prompt_file:
        with open(args.prompt_file, encoding="utf-8") as f:
            prompt = f.read().strip()
    else:
        prompt = (args.prompt or "").strip()
    if not prompt:
        print("Provide --prompt or --prompt-file", file=sys.stderr)
        return 1

    body: dict = {
        "model": args.model,
        "prompt": prompt,
        "aspect_ratio": args.aspect,
        "quality": args.quality,
        "output_format": "png",
        "n": 1,
    }
    if args.resolution:
        body["resolution"] = args.resolution

    refs: list[dict] = []
    for ref in args.ref:
        if ref.startswith("http://") or ref.startswith("https://") or ref.startswith("data:"):
            url = ref
        else:
            with open(ref, "rb") as rf:
                raw = rf.read()
            ext = os.path.splitext(ref)[1].lower()
            mime = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp",
                ".gif": "image/gif",
            }.get(ext, "image/jpeg")
            url = f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"
        refs.append({"type": "image_url", "image_url": {"url": url}})
    if refs:
        body["input_references"] = refs

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/aguskolod/aguskolod",
            "X-Title": "web-design-skills brand-kit-gen",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}: {err_body}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return 1

    data = payload.get("data") or []
    if not data or "b64_json" not in data[0]:
        print(f"Unexpected response: {json.dumps(payload)[:500]}", file=sys.stderr)
        return 1

    out_path = args.out
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(data[0]["b64_json"]))

    usage = payload.get("usage") or {}
    print(json.dumps({"out": out_path, "model": args.model, "usage": usage}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
