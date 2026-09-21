---
name: landing-craft
description: Use with the web-design-skills stack while building or creatively editing a local-business client landing — hierarchy, primary CTA, spacing, mobile tap targets, anti-patterns, Nielsen-style usability. Also use when the user asks to move buttons, add sections, or polish layout without nonsensical placement or competing CTAs.
---

# Landing Craft

**Core principle:** Professional landings follow craft rules under creative feedback. This skill guards the build; it does not invent a new brand.

**Use with:** `landing-build` (always) and any creative correction pass.

## Quick rules

| Rule | Do | Don't |
|---|---|---|
| One job / URL | One primary offer + one primary CTA style | Equal-weight “Llamar / WhatsApp / Reservar / Ver más” as four filled buttons |
| Hierarchy | One H1; sections with clear H2; scan in 5s | Walls of equal-size text |
| CTA | Filled primary; secondary as text/outline; repeat same primary after proof | Random button colors per section |
| Sections | One purpose each; follow `direction.md` order | Hero stuffed with stats, address, promo chips, and three offers |
| Mobile | Thumb-reach CTA; `tel:` / `wa.me` work; ≥44px taps | Desktop-only layout; tiny links |
| Trust | Proof near claims; eligibility/hours near action | Fake scarcity or unverified claims |
| Consistency | Same radius/type scale as `direction.md` | Mixing pill + sharp + glow arbitrarily |
| Clarity | Visitor language from discovery VoC | Internal jargon |

## Nielsen → landing (short)

- **Match real world:** words customers use.
- **Consistency:** conventions for links/buttons.
- **Minimalist:** remove competing chrome.
- **Recognition:** visible CTA and contact, don’t hide phone.
- **Error prevention:** state area/hours/limits before the ask.

## When editing after human feedback

1. Map the request to a craft rule (hierarchy, CTA, spacing, proof…).
2. Apply the change **without** breaking primary CTA or direction tokens.
3. If the request conflicts with craft, propose a compliant alternative in one sentence, then implement the agreed fix.

## Red flags

- Two primary buttons side by side
- CTA that doesn’t match the H1 promise
- Decorative buttons that go nowhere
- Sticky bar covering content
- Inventing prices/services to “fill” a section

## When not to use alone

No discovery/direction yet → `web-discovery` / `visual-direction`. Full visual rethink → those skills, not craft patches.
