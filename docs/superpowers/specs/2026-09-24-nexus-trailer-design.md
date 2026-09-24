# NEXUS — AI Website Generator Trailer

Approved direction for a Tesseract motion piece. User asked to implement without further questions.

## Product

**NEXUS** — fictional AI website generator. Tagline: “Generate the impossible.”  
Describe a site → get extreme modern builds (matrix, ASCII, glass 3D, neon, brutalist, chrome, HUD, CRT, polygon, wild west, collage, etc.).

## Specs

| Field | Value |
| --- | --- |
| Format | 1920×1080 landscape |
| Duration | ~48s |
| Audio | Music + SFX only (no VO) |
| Engine | Tesseract CLI 0.2.0 |
| Deliverables | Editable `.tsrct` + source assets + final MP4 |

## Arc

| Time | Beat |
| --- | --- |
| 0–6s | Hook — cursor blink, prompt types: `a site that feels like the future` |
| 6–14s | Product — NEXUS chrome, generate, push into canvas |
| 14–38s | Style parade — 12 worlds × ~2s, whip cuts, style labels, characters step out of each site |
| 38–42s | Payoff — mosaic of worlds → NEXUS home |
| 42–48s | End card — logo + *Generate the impossible.* |

## Worlds (parade order)

1. Matrix rain terminal — green silhouette steps out  
2. ASCII art site — ASCII figure solidifies forward  
3. Glass / frosted 3D cards — frosted figure leans out  
4. Neon cyber grid — neon outline runner  
5. Brutalist mega-type — block-head figure  
6. Liquid chrome — chrome mannequin  
7. Blueprint / wireframe — wireframe pilot  
8. Holographic HUD — hologram operator  
9. Retro CRT / scanlines — CRT ghost  
10. Low-poly / polygon — faceted rider from the mesh  
11. Wild west — cowboy silhouette from wanted-poster UI  
12. Maximalist chaos collage — collage figure bursts out  

## Look

- Black void, soft vignette, glass UI panels  
- Accent: electric cyan → hot magenta on generate  
- UI type: geometric sans (Inter / Public Sans)  
- World type: mono / slab / display swapped per world  
- Motion: smooth product; hard/whip parade; character scale+push out of frame  

## Technical notes

- Worlds authored as image backdrops + native text/shape overlays (editable motion kept in Tesseract)  
- Characters as transparent PNGs or vector silhouettes animated as layers  
- Export via external FFmpeg H.264; lavapipe for headless Vulkan  
- Project root: `tesseract-projects/nexus-trailer/`
