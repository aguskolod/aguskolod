# NEXUS — AI Website Generator Trailer

Fictional product trailer built with Tesseract by Mirage.

| | |
| --- | --- |
| Editable project | `NexusTrailer.tsrct` |
| Finished render | `NexusTrailer.mp4` (48s · 1920×1080 · H.264) |
| Source assets | `SourceAssets/` (worlds, characters, audio, fonts) |
| Previews | `Previews/` |
| Build scripts | `scripts/generate_assets.py`, `scripts/build_project.py` |

## Arc
1. Hook — prompt types “a site that feels like the future”
2. Product — NEXUS app chrome + GENERATE
3. Style parade — 12 website worlds with characters stepping out (~2s each)
4. Mosaic payoff — “infinite styles”
5. End card — **NEXUS** · Generate the impossible.

## Rebuild
```bash
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/lvp_icd.json
python3 scripts/generate_assets.py
python3 scripts/build_project.py
~/.local/share/Tesseract/bin/tsrct export \
  --project NexusTrailer.tsrct --output NexusTrailer.mp4 \
  --encoder-backend external-ffmpeg-command --ffmpeg-path /usr/bin/ffmpeg
```
