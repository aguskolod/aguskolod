---
name: visual-direction
description: Use when a confirmed discovery brief exists and the user needs visual direction for a local-business landing — typography, color roles, button radius, motion, imagery style, and section structure. Also use when choosing fonts or a brand look from audience/personality, when the brand has weak or no identity guidelines, or before generating a brand kit or writing page HTML/CSS.
---

# Visual Direction

**Core principle:** Brand personality and audience decide the system. Taste does not. Translate discovery into a web-ready direction the human can approve before any kit or code.

**REQUIRED BACKGROUND:** Confirmed `docs/web-design-skills/clients/<slug>/discovery.md`. If missing or unconfirmed → run `web-discovery` first.

**REQUIRED NEXT:** After human confirms direction → `brand-kit-gen` (visualize) then `landing-build`.

## When to use

- Post-discovery: “elegí fonts / colores / cómo se siente”
- Brand sin manual: hay que derivar identidad para la web
- Antes de mockups IA o HTML

**When not:** Discovery no confirmado; solo copy edits; QA técnico.

## Process

1. **Read discovery** (offer, audience, CTA, VoC, anti-goals, presence clues).
2. **Lock 3–5 personality adjectives** grounded in discovery. If weak brand, derive from audience + job-to-be-done + what competitors look like (differentiate, don’t clone). Confirm adjectives with the human if ambiguous.
3. **Typography**
   - Map adjectives → category (serif / geometric sans / humanist sans / slab / etc.).
   - Propose **2–3 concrete pairings** (display + body), each with why, web-license note, and Spanish/`ñ` support.
   - Prefer max **two families**. Test mentally with real headline + body from the offer — not Lorem.
   - Recommend one pairing; let the human pick.
4. **Color roles** (not a random rainbow)
   - Primary (CTA / key action), neutrals (bg/text/border), optional accent.
   - Check intended CTA text-on-fill contrast (target WCAG AA: 4.5:1 normal text).
   - Use discovery clues (existing logo/IG) when present; otherwise derive from personality + local category norms with a clear differentiation note.
5. **Expression rules** (identity in UI)
   - Radius: sharp / soft / pill — tied to adjectives.
   - Density: compact (urgency/utility) vs airy (calm/premium).
   - Borders/shadows: flat honest vs elevated.
   - Motion: none / subtle / present (+ honor `prefers-reduced-motion` later in build).
   - Imagery: real local / product / people; stock policy; avoid clichés named in anti-goals.
6. **Section structure** (message order, not pixels)
   - One primary offer, one primary CTA.
   - Default local flow unless discovery says otherwise: Hero → Proof/trust → Offer/process → Objections/FAQ → Contact/CTA.
   - One job per section (headline intent only).
7. **Write `direction.md`, summarize, stop for confirmation.** No HTML. No image generation in this skill.

### How many directions?

- Clear discovery → **1 recommended** + optional short “alternative if you want softer/harder”.
- Ambiguous personality → **2 directions** max, equal clarity, human picks.

## Persist path

`docs/web-design-skills/clients/<slug>/direction.md`

## Direction template (REQUIRED)

```markdown
# Visual direction — <Business Name>

## Status
- Discovery source: docs/web-design-skills/clients/<slug>/discovery.md
- Confirmed by human: no | yes (date)

## Personality
- Adjectives (3–5):
- Feeling we want visitors to have:
- Differentiate from local norm by:

## Typography
### Recommended
- Display:
- Body:
- Why (adjectives → category → this pick):
- Weights to use:
### Alternatives (1–2)
- …

## Color roles
| Role | Hex | Usage |
|---|---|---|
| Primary (CTA) | | |
| Text | | |
| Background | | |
| Surface / muted | | |
| Accent (optional) | | |
- Contrast notes (CTA label on primary):

## Expression
- Radius / buttons:
- Density:
- Borders / elevation:
- Motion level:
- Imagery direction:
- Icon style (if any):

## Section structure
1. …
2. …
- Primary CTA placement intent:

## Anti-patterns for this brand
- …

## Handoff
- Ready for `brand-kit-gen`: no | yes (pending confirm)
```

## Teaching while deciding (keep short)

When proposing fonts/colors, add **one sentence** of theory in plain language (e.g. “Sans humanista = más cercana; geométrica = más técnica”). Do not dump a course.

## Red flags — STOP

| Excuse | Reality |
|---|---|
| “Elijo Inter/Roboto por default” | Solo si los adjetivos lo justifican; documentá el porqué. |
| “Salteo discovery, ya sé el vibe” | Sin brief confirmado no hay dirección. |
| “Genero el mock YA” | Primero direction confirmada; kit es la skill siguiente. |
| “Pills + glow + purple porque vende” | Expression sigue a adjetivos + anti-goals, no a moda IA. |
| “Cinco fonts para variedad” | Máximo ~2 familias. |

## Common mistakes

- Picking type before adjectives
- Primary color on everything (CTA loses power)
- Style tile confused with full page layout
- Inventing services/prices inside the direction doc
