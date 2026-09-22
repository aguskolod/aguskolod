---
name: laws-of-ux-correct
description: Use when correcting an existing website or landing against Laws of UX (lawsofux.com) — after a build, before ship, or when the user asks for a psychology/UX-laws audit. Correction only: scan code and visuals, report failing laws with precise agent fix steps. Not for greenfield design, brand direction, or replacing landing-craft/landing-qa.
---

# Laws of UX — Correct

**Core principle:** This skill only **audits and corrects**. It does not invent a new visual direction or build from scratch.

**Canonical source:** [Laws of UX](https://lawsofux.com/) by Jon Yablonski — full catalog in [reference.md](reference.md).

**REQUIRED REFERENCE:** Read `reference.md` before scoring. Cite law names + URLs in findings.

## When to use

- “Audita / corregí con Laws of UX”
- Post-`landing-build`, pre-ship psychology pass
- User points at a live URL, Astro `site/`, or HTML and wants failures + fixes

**When not:** Discovery, visual-direction, brand-kit, or first implementation (use those skills first). Technical-only QA without psychology → `landing-qa`. Craft/CTA heuristics without full laws catalog → `landing-craft`.

## Inputs

Need a **concrete target**:

1. Path to site code (e.g. `docs/web-design-skills/clients/<slug>/site/`), and/or
2. Local/dev URL, and/or committed screenshots

If missing, ask once for the target — then proceed.

Also load `direction.md` / `discovery.md` when present (context for Jakob’s Law, mental model, CTAs) — do not redesign the brand.

## Process (mandatory)

1. **Code scan** — Read templates/components/CSS for: CTA count/styles, tap target sizes, spacing/grouping, forms, nav conventions, motion, loading states, heading structure, contrast-related tokens.
2. **Visual scan** — Capture or open **desktop + mobile (~390px)** screenshots of the real page (browser tools / computer use). Read the images. Note hierarchy, grouping, isolation of primary CTA, clutter, end-of-page strength.
3. **Evaluate every law** in `reference.md`. Record only **failures** (or “at risk” if evidence is partial). Skip laws that clearly don’t apply (e.g. multi-step Goal-Gradient on a one-screen landing with no funnel) — mark `N/A` briefly, don’t invent issues.
4. **Write the report** to disk and stop for human priority calls unless they said “fix all P0”.

## Report path

`docs/web-design-skills/clients/<slug>/laws-of-ux-correct.md`  
(or next to the target if no client slug)

## Report template (REQUIRED)

```markdown
# Laws of UX correction — <target>

## Meta
- Target (code / URL):
- Viewports checked:
- Screenshots:
- Related briefs: discovery/direction paths or none

## Summary
- P0 count / P1 count / P2 count
- Top 3 fixes to do first:

## Findings (failures only)

### [P0|P1|P2] <Law name>
- **Source:** https://lawsofux.com/...
- **Evidence (code):** file:line or component + what violates
- **Evidence (visual):** what the screenshot shows
- **Why it fails:** one sentence tied to the law definition/takeaway
- **Fix instructions (agent — do in order):**
  1. …
  2. …
  3. …
- **Done when:** observable acceptance check

## N/A laws
- <Law>: reason

## Out of scope
- Brand/token changes that need `visual-direction` re-approval
```

### Severity

| Level | Meaning |
|---|---|
| **P0** | Blocks primary task/conversion or causes likely mis-taps / decision paralysis on the main path |
| **P1** | Clear law violation harming scanability, trust, or secondary paths |
| **P2** | Polish / edge cases |

## Fix execution rules

- Fix instructions must be **specific to this codebase** (selectors, components, CSS variables) — not generic advice alone.
- Prefer minimal diffs; preserve approved `direction.md` tokens unless the failure requires a visible hierarchy change (then note it).
- After fixes, re-check only the failed laws (quick pass) if the user asked to apply corrections.

## Red flags

| Excuse | Reality |
|---|---|
| “Rediseño todo con otro aesthetic” | Correction skill — targeted fixes |
| “Solo leí el código, no hace falta screenshot” | Visual scan is mandatory |
| “Todo viola las 30 leyes” | Report real evidence only; use N/A |
| “Miller = máximo 7 links siempre” | Don’t misuse Miller; see reference takeaways |

## Relationship to other skills

- After applying P0/P1 fixes → optional `landing-qa`
- If fixes need new brand tokens → `visual-direction` (human confirm) first
