---
name: web-discovery
description: Use when starting a new local-business website or landing, when the user provides a client name plus social/Maps links, or when visual/brand work is requested but there is no confirmed discovery brief yet. Also use when the user says they do not know where to start, need competitor or review research, or asks to analyze a client's Instagram, Facebook, or Google Business Profile before designing.
---

# Web Discovery

**Core principle:** Understand the client, audience, and local landscape before any visual direction or code. Discovery reduces wrong builds.

**REQUIRED NEXT:** After the human confirms the brief, use `visual-direction`. Do not invent visual systems here.

## When to use

- New client intake (name + networks + notes)
- “Analizá sus redes / Maps / competencia”
- Someone asks to design/build but no `discovery.md` exists yet

**When not to use:** Refining an already-approved discovery brief; pure visual or copy edits with discovery already confirmed.

## Process

1. **Collect intake** (do not re-ask known facts). Need at least: business name, what they sell, service area or city, and any of: Instagram, Facebook, Google Maps/GBP, existing site, WhatsApp/phone, human notes.
2. **Audit presence** from the links given (and public search if needed): NAP consistency, hours, offer clarity, photos/style clues, bio tone, reviews volume/themes, obvious gaps.
3. **Competitive audit (lean):** 3–5 local competitors (direct first). Per competitor note: offer framing, primary CTA, proof used, mobile feel, what to match vs avoid. Goal: gaps and opportunities — not copying.
4. **Voice of Customer:** From client + competitor public reviews, extract recurring praise, complaints, and verbatim phrases (Spanish AR when the market is AR). Tag: trigger situation, fears, proof that matters.
5. **Synthesize one primary offer + one primary CTA.** If several offers exist, recommend a priority for this landing and list the rest as secondary.
6. **Write the brief** to disk and **stop for confirmation**. No fonts, colors, or HTML in this skill.

### Questions (only gaps that change the outcome)

Ask at most 2–3 per round. Prefer asserting a likely reading and inviting correction. Never ask for CSS or aesthetic lanes (that is `visual-direction`).

## Persist path

Write:

`docs/web-design-skills/clients/<slug>/discovery.md`

`<slug>` = lowercase kebab-case from the business name.

If the file exists, update it; do not scatter parallel briefs.

## Brief template (REQUIRED)

Fill every section. Mark unknowns as `Open:` — never invent services, prices, hours, or claims.

```markdown
# Discovery — <Business Name>

## Status
- Confirmed by human: no | yes (date)

## Business
- Name:
- Category / trade:
- Area (city / barrios):
- One-line offer (primary):
- Secondary offers (if any):

## Audience & situation
- Who arrives:
- Trigger / job-to-be-done (situation, not jargon):
- What they need to believe before acting:
- Objections that stop them:

## Conversion
- Primary CTA (one):
- Secondary CTA (optional):
- Contact facts (phone, WhatsApp, address, hours) — confirmed only:

## Confirmed facts
- …

## Open / unknowns
- …

## Presence audit (redes / GBP / site)
- Channels reviewed (URLs):
- Consistency (NAP, hours, offer):
- Visual/tone clues (facts only — no system yet):
- Assets available vs missing:
- Review themes (own listing):

## Competitive audit (3–5)
| Competitor | Offer / angle | CTA | Proof | Notes (match / avoid) |
|---|---|---|---|---|
| | | | | |

## Opportunities & gaps
- …

## Voice of Customer (phrases)
- Praise language:
- Pain / complaint language:
- Phrases usable in messaging (not invented):

## Anti-goals
- What this landing must not feel like / not claim:

## Handoff
- Ready for `visual-direction`: no | yes (pending human confirm)
```

## After writing

1. Show a short summary (offer, CTA, top 3 insights, open questions).
2. Ask the human to confirm or correct the brief.
3. On confirmation, set `Confirmed by human: yes` and point to the file path.
4. Do **not** start `visual-direction` until they confirm (unless they explicitly say to continue).

## Red flags — STOP

| Excuse | Reality |
|---|---|
| “Ya entiendo, arranco el HTML” | Sin brief confirmado = discovery incompleto. |
| “Inventemos un precio/servicio para completar” | Va en `Open:`. Nunca como hecho. |
| “Tiro 10 preguntas de una” | Máximo 2–3 por ronda; research primero. |
| “Copiemos el sitio del competidor” | Audit = gaps; no clonar. |
| “No hay reseñas, skip VoC” | Anotá la ausencia; buscá lenguaje en competidores. |

## Common mistakes

- Mixing discovery with font/color decisions
- Multiple primary CTAs (“llamá y escribí y reservá” sin prioridad)
- Personas noveladas en vez de situación de compra
- Brief solo en el chat (se pierde; siempre persistir)
