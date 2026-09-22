---
name: web-design-pipeline
description: Use when the user starts or continues a local-business client landing with the web-design-skills stack (discovery, Instagram/Maps, visual direction, brand kit, build, QA), mentions a client name like Mesal, or asks what skill comes next after discovery. Use instead of Impeccable for this pipeline. Also use when the agent is about to open PRODUCT.md/DESIGN.md or Impeccable new-work for a different client.
---

# Web Design Pipeline (router)

**This stack is independent of Impeccable.** For client landings, do not run Impeccable init / new-work / concept-seed / decision page unless the user explicitly asks for Impeccable.

## Route

| Situation | Skill |
|---|---|
| New client / redes / no brief | `web-discovery` |
| Discovery confirmed; fonts/colors/feel/structure | `visual-direction` |
| Direction confirmed; mock / brand board / 9:16 | `brand-kit-gen` |
| Building or editing the page | `landing-build` + `landing-craft` (Astro default) |
| Final pass | `landing-qa` |
| Psychology / Laws of UX correction | `laws-of-ux-correct` |

Read `docs/web-design-skills/PIPELINE.md`.

## Client isolation

- Persist only under `docs/web-design-skills/clients/<slug>/`.
- Ignore root `PRODUCT.md` / `DESIGN.md` unless the user says this work is for that product.
- Never copy another client’s brand into the current slug.

## After discovery

Next skill is always **`visual-direction`**, not Impeccable.
