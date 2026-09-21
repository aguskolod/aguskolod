---
name: brand-kit-gen
description: Use in the web-design-skills stack after confirmed direction.md when the user wants a brand board, style tile, or 9:16 landing sketch via OpenRouter GPT Image. Also use when iterating those mocks before HTML/CSS. Prefer this over Impeccable visualize or Higgsfield for this pipeline unless the user asks otherwise.
---

# Brand Kit Gen

**Core principle:** Visualize the approved direction before coding. The kit shows the system; it does not invent a new one.

**REQUIRED:** Confirmed `docs/web-design-skills/clients/<slug>/direction.md` (and discovery).  
**REQUIRED NEXT:** Human approves kit → `landing-build`.

## Artifacts (generate both unless user asks for one)

1. **Brand board** — `aspect_ratio: 16:9` or `1:1`: palette swatches with hex, type specimens (display + body names from direction), sample primary button (correct radius), imagery mood note.
2. **Landing sketch** — `aspect_ratio: 9:16`: first-viewport + hint of following sections; real business name; real offer/CTA words from discovery; no fake prices.

Save under:

`docs/web-design-skills/clients/<slug>/kit/`

Names: `brand-board.png`, `landing-9x16.png` (or timestamped if iterating).

## Prompt rules

- Lead with direction adjectives, hex roles, font names, radius, density, imagery.
- Include exact legal/business name and primary CTA label.
- Forbid invented services, ratings, or discounts not in discovery.
- Style: cohesive mock / style tile — not a screenshot of a random template.

## OpenRouter

1. Require `OPENROUTER_API_KEY` in the environment.
2. Default model: `openai/gpt-image-2.5-sunburst` (OpenAI GPT Image 2.5). Override with `OPENROUTER_IMAGE_MODEL` (e.g. `openai/gpt-image-2.5-flare` or `openai/gpt-image-2`). If a slug 404s, list models via `GET https://openrouter.ai/api/v1/images/models`.
3. Run the helper:

```bash
python3 .cursor/skills/brand-kit-gen/scripts/generate_image.py \
  --prompt-file path/to/prompt.txt \
  --out path/to/out.png \
  --aspect 9:16 \
  --quality high
```

4. Show images to the human; iterate prompts on feedback; do not jump to HTML until they approve the direction visually (or explicitly skip kit).

## Process

1. Read discovery + direction.
2. Write two prompt files into `kit/prompts/`.
3. Generate board then landing sketch.
4. Summarize what to look at (type, color, radius, hero message).
5. Stop for approval / revision notes.

## Red flags

- Generating without confirmed direction
- Pretty mock that ignores hex/fonts in `direction.md`
- Treating kit as final production photography
- Spending credits looping without human feedback
