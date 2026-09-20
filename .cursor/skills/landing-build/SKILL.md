---
name: landing-build
description: Use when implementing a local-business landing in HTML/CSS (or the project stack) after discovery and visual direction are confirmed, preferably after an approved brand kit. Also use when turning an approved direction into a working page without inventing new brand rules.
---

# Landing Build

**Core principle:** Build from confirmed docs. Code expresses the brief; it does not redesign the brand mid-flight.

## Prerequisites

1. Confirmed `discovery.md`
2. Confirmed `direction.md`
3. Preferred: human-approved kit images under `kit/` (or explicit “skip kit, build now”)

Also load **`landing-craft`** for every layout decision.

## Process

1. Re-read discovery (offer, CTA, facts, VoC) + direction (type, color, expression, sections).
2. Set CSS variables from direction tokens (colors, radii, fonts via linked web fonts).
3. Implement sections in the agreed order; one job each.
4. Wire real `tel:` / WhatsApp / Maps only with confirmed contact facts; mark placeholders clearly if still `Open:`.
5. Mobile-first layout; sticky primary CTA only if it doesn’t cover content.
6. Apply craft rules; no competing primary buttons.
7. Stop for creative review with the human; do not invent polish that contradicts direction.

## Output

- Page file(s) in the project convention (e.g. `index.html` or client folder).
- Keep claims faithful to discovery `Confirmed facts`.

## Red flags

- Building without confirmed direction
- Swapping fonts/colors “because it looks better” without updating `direction.md` + human OK
- Filling gaps with fake reviews, prices, or 24hs claims
