---
name: landing-build
description: Use in the web-design-skills stack when implementing a local-business client landing after discovery and direction are confirmed under docs/web-design-skills/clients/<slug>/, preferably after an approved brand kit. Default stack is Astro with CSS variables from direction.md. Prefer this over Impeccable craft/new-work and over raw single-file HTML/CSS unless the user asks otherwise.
---

# Landing Build

**Core principle:** Build from confirmed docs. Code expresses the brief; it does not redesign the brand mid-flight.

## Default stack

**Astro** + **CSS variables** mapped from `direction.md` (colors, radius, fonts, density).

| Layer | Default | Notes |
|---|---|---|
| Framework | Astro (static output) | Marketing/landing fit; little JS by default |
| Styling | CSS (or scoped CSS) + `:root` tokens | Not Tailwind unless the user asks |
| Motion | CSS / View Transitions first; GSAP island only if needed | Keep intentional, match `direction.md` motion level |
| Location | `docs/web-design-skills/clients/<slug>/site/` | One Astro app per client |

**Overrides:** only if the human says so (e.g. Next, raw HTML mock). Record the choice in the client folder (`build.md` or a line in `direction.md`).

Do **not** default to a lone `index.html` at repo root.

## Prerequisites

1. Confirmed `discovery.md`
2. Confirmed `direction.md`
3. Preferred: human-approved kit images under `kit/` (or explicit “skip kit, build now”)

Also load **`landing-craft`** for every layout decision.

## Process

1. Re-read discovery (offer, CTA, facts, VoC) + direction (type, color, expression, sections).
2. Scaffold Astro in `clients/<slug>/site/` if missing (`npm create astro@latest` or equivalent minimal static template).
3. Set CSS variables from direction tokens; load web fonts named in direction.
4. Implement sections in the agreed order as Astro components/pages; one job each.
5. Wire real `tel:` / WhatsApp / Maps only with confirmed contact facts; mark placeholders clearly if still `Open:`.
6. Mobile-first layout; sticky primary CTA only if it doesn’t cover content.
7. Apply craft rules; no competing primary buttons.
8. `astro dev` for review; stop for creative feedback; do not invent polish that contradicts direction.

## Output

- Astro project under `docs/web-design-skills/clients/<slug>/site/`
- Claims faithful to discovery `Confirmed facts`

## Red flags

- Building without confirmed direction
- Raw HTML/CSS as default when Astro was not waived
- Swapping fonts/colors without updating `direction.md` + human OK
- Filling gaps with fake reviews, prices, or hours claims
- Heavy client JS / carousels that fight “motion: none|subtle” in direction
