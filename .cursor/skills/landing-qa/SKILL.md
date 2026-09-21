---
name: landing-qa
description: Use in the web-design-skills stack before presenting or shipping a local-business client landing — responsive checks, CTA/links, basic a11y, and fidelity to docs/web-design-skills/clients/<slug>/direction.md. Also use for QA, launch checklist, or a final pass on that stack.
---

# Landing QA

**Core principle:** Verify the page works and still matches the approved direction before calling it done.

## Prerequisites

Built page + `discovery.md` + `direction.md` (kit optional).

## Checklist

### Message & conversion
- [ ] H1/offer match discovery primary offer
- [ ] One clear primary CTA; secondary not competing
- [ ] CTA copy matches the action (call / WhatsApp / etc.)
- [ ] No invented claims vs discovery confirmed facts

### Links & contact
- [ ] `tel:`, `wa.me`, Maps, social URLs correct
- [ ] No dead buttons or `#` placeholders left as primary CTA

### Responsive
- [ ] Usable at ~320–390px width: no horizontal scroll, readable type
- [ ] Desktop layout coherent; images not crushing text
- [ ] Tap targets adequate; sticky UI doesn’t cover CTAs

### Accessibility (basic AA)
- [ ] Text/UI contrast reasonable (flag failures)
- [ ] Logical heading order (one H1)
- [ ] Images have alt (or empty alt if decorative)
- [ ] Focus visible on interactive elements

### Fidelity to direction
- [ ] Fonts, colors, radius, density match `direction.md`
- [ ] Imagery mood consistent with expression rules
- [ ] Section order matches direction structure

## Output

Write `docs/web-design-skills/clients/<slug>/qa.md` with pass/fail notes and follow-ups. Summarize top issues for the human.

## Red flags

- “Looks fine on my laptop” without mobile check
- Shipping with placeholder phone/WhatsApp
- Ignoring contrast failures on the primary CTA
