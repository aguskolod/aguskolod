# Research: `landing-build` + `landing-qa`

Fecha: 2026-09-20

## Fuentes build
- Conversion order: Research→UX→Copy→Visual (prior).
- Tokens from direction → CSS variables.
- agency-forge: structured design spec → assemble (don’t freehand contradicting direction).
- User rules: hero budget, brand-first, no default AI aesthetic clusters, motion intentional.

## Fuentes QA
- [Leadpages landing QA](https://leadpages.com/blog/landing-page-qa-checklist)
- [qa-checklist.dev launch QA](https://qa-checklist.dev/qa-guides/website-launch-qa-checklist)
- [yourwebteam acceptance criteria](https://yourwebteam.io/website-launch-acceptance-criteria-template-2026/)
- WCAG 2.2 contrast AA

## Principios build
1. Prerequisites: confirmed discovery + direction (+ preferred approved kit).
2. **Default framework: Astro** (static) under `clients/<slug>/site/` — not raw root HTML unless waived.
3. Implement tokens as CSS variables from `direction.md`; follow section structure.
4. Apply `landing-craft` continuously.
5. Copy AR from discovery VoC; no invented claims.
6. Mobile viewport first for local businesses.
7. Motion: CSS/View Transitions first; GSAP only if direction asks and craft allows.

## Decisión Astro (2026-09-21)

Elegido como default del stack para landings de negocio local: performance, poco JS, buen fit marketing. No es el path más fácil para motion pesado (Framer/Webflow/Next+GSAP lo son más); motion ambicioso se agrega con islas/GSAP cuando el brief lo pida.

## Principios QA
1. Message match to discovery offer/CTA.
2. Links/tel/wa.me work; one primary CTA hierarchy.
3. Responsive 320→desktop; no horizontal scroll.
4. Contrast, headings, alt, focus basics.
5. Fidelity check vs direction.md (fonts, colors, radius, density).
6. Persist QA report next to client folder.
