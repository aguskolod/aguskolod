# Research: `brand-kit-gen`

Fecha: 2026-09-20

## Fuentes
- [OpenRouter Image Generation docs](https://openrouter.ai/docs/guides/overview/multimodal/image-generation) — `POST /api/v1/images`, models e.g. `openai/gpt-image-2`, `aspect_ratio` including `9:16`, quality, `input_references`.
- [OpenRouter image tutorial](https://openrouter.ai/blog/tutorials/image-generation/) — b64_json save pattern; references.
- [OpenRouter multimedia-explorer](https://github.com/OpenRouterTeam/multimedia-explorer) — brand moodboard → inject into generation.
- [Kanopi style tiles](https://kanopi.com/blog/what-is-a-style-tile-or-mood-board-and-why-is-it-helpful/) — tile ≠ full layout; approve direction visually.
- Prior: direction.md as source of truth for prompts.

## Principios
1. No kit without confirmed `direction.md`.
2. Two artifacts: brand board (tokens visible) + landing sketch **9:16**.
3. Prompts must include real business name, real offer words, hex/fonts from direction — no invented claims.
4. Human iterates (“más seco / más cálido”) before build.
5. Persist images under `docs/web-design-skills/clients/<slug>/kit/`.
6. Script uses `OPENROUTER_API_KEY`; default model configurable (prefer OpenAI GPT Image via OpenRouter slug; verify current slug at runtime).

## Descartar
- Autopublish; generating without direction; treating kit as final production art.
