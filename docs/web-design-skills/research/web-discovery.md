# Research: `web-discovery`

Fecha: 2026-09-20  
Skill destino: `.cursor/skills/web-discovery/SKILL.md`

## Pregunta de research

¿Cómo hacen discovery profesional para un sitio/landing de negocio local, y cómo lo estructuran los agentes/skills existentes, para que un humano sin teoría de diseño pueda guiar sin explicar todo?

## Fuentes consultadas

### Discovery de agencia / web
- [William Alexander — Website Discovery Process](https://williamalexander.co/articles/website-discovery-process/) — stakeholder interviews, user research, content audit, technical assessment, competitive analysis; output = project brief. Discovery ≈ risk reduction.
- [LOW/CODE — Website Redesign Discovery](https://www.lowcode.agency/blog/website-redesign-discovery-phase-what-to-expect) — interviews (objections, success at 90 days), competitive audit 3–5 sites (IA, positioning, proof, mobile, CTA), deliverable table ending in approved project brief.
- [okto-digital — Discovery Process](https://oktodigital.com/services/discovery/process/) — Context → Research → Strategy stages.
- [AgencyPro — Creative Brief](https://agencypro.app/blog/how-to-write-a-creative-brief) — sections: overview, objectives, audience, key message, tone, deliverables, competitors, success metrics.
- [Milanote — Website Design Brief](https://milanote.com/templates/creative-briefs/website-design-brief) — background, goals, audience, brand refs, likes/dislikes.
- [Windmill — Website Creative Strategy Brief](https://www.windmillstrategy.com/how-to-write-a-website-creative-strategy-brief/) — competition (like/dislike), ICP, CTA language.
- [yourwebteam — Requirements Document](https://yourwebteam.io/website-requirements-document-template-2026/) — goals (≤3), buying situations, proof needed, objections — useful lean structure for small biz.

### Competitive audit (UX)
- [Google UX — Competitive Audits (Rodriguez notes)](https://p-rodriguez.me/google-ux-design/ux-design-process/module-4/competition/competitive-audits/) — goals → 5–10 competitors → aspects → research → trends/gaps → report.
- [Medium — Steps to conduct a competitive audit](https://osamaabdelnaser.medium.com/steps-to-conduct-a-competitive-audit-6a92958fa07b) — direct vs indirect competitors; document visual design, content, etc.

### Social / GBP / local presence
- [Sprout Social — Social Media Audit](https://sproutsocial.com/insights/social-media-audit/) — inventory platforms, consistency, top content, audience fit.
- [Embedsocial / AgencyAnalytics — GBP audit](https://embedsocial.com/blog/gbp-audit/) — NAP, categories, photos, reviews, hours, website link consistency.
- Social Butterfly Marketing checklist PDF — consistency across FB/IG/GMB (logo, bio, contact).

### Voice of Customer / local messaging
- [TrueReview — Analyze Competitor Reviews](https://www.truereview.co/post/competitor-review-analysis) — 3–4 local competitors; 1★ = gaps, 5★ = language; phrases for headlines.
- [Outscraper — Competitor Review Analysis](https://outscraper.com/competitor-review-analysis/) — recurring themes, customer language for FAQs/service pages.
- [Stacy Eleczko — VoC + JTBD](https://stacyeleczko.com/voice-of-customer-language-the-research-process-behind-messaging-that-converts/) — trigger moment, risks, what they tried, exact words.
- [Search Engine Land — JTBD pages for local](https://searchengineland.com/local-content-playbook-from-service-pages-to-jobs-to-be-done-pages-471833) — situation-first, not service-name-first.
- [Ridiculously Good Looking — Service page jobs](https://goodlookingco.com/playbook/what-a-great-service-page-actually-does) — clarify, fit, proof, process, action.

### Agentes / skills existentes
- [cofoundy/brand-skills](https://github.com/cofoundy/brand-skills) — `brand-context` as foundation file every skill reads; structured package (`brand.yaml` + `context.md`); ask only what’s missing; Spanish/LATAM support.
- [brand-context SKILL.md](https://raw.githubusercontent.com/cofoundy/brand-skills/main/skills/brand-context/SKILL.md) — collect basics, audience, positioning, personality 3–5 words, goals; persist; don’t re-ask known facts.
- [agency-forge](https://github.com/noluyorAbi/agency-forge) — discover→design→build→qa; **consent-first**; design as structured spec not freehand HTML; human owns identity decisions.
- [savvity/local-business-builder](https://github.com/savvity/local-business-builder) — discovery questions then scaffold (SEO-heavy; our stack is design-led landing, take intake pattern only).
- [ChuluuMGL/business-website-skill](https://github.com/ChuluuMGL/business-website-skill) — evidence from source materials before build; IA/direction options first.
- [SiteSeeker](https://siteseeker.ai/ai-website-builder) — listing-as-brief (hours, phone, rating, reviews) — validates that public profile data is enough to start discovery.

## Principios que entran a la skill

1. **Discovery antes de visual/código.** Gate: brief confirmado por el humano.
2. **Proporcionalidad.** Landing local ≠ discovery enterprise. Un brief corto gana.
3. **Intake humano + research del agente.** El humano trae nombre/redes/notas; el agente audita presencia, competencia local, lenguaje de reseñas.
4. **No inventar claims.** Solo hechos confirmados o marcados como hipótesis/`open`.
5. **Competitive audit lean.** 3–5 locales; aspectos fijos: oferta, CTA, prueba, mobile, tono visual (sin diseñar aún).
6. **VoC desde reseñas públicas.** Frases del cliente para messaging posterior; no copiar claims ajenos.
7. **Persistir el brief** en disco para que `visual-direction` lo lea (patrón brand-context / package).
8. **Preguntas mínimas.** Solo huecos que cambian el resultado; no cuestionario.
9. **NAP / consistencia** entre redes y datos de contacto (confianza local).
10. **Human approval** del brief antes de dirección visual (alineado a agency-forge consent/gates).

## Qué se descarta (v1)

- Personas ficticias largas / journey maps elaborados.
- Content inventory de 100+ páginas.
- SEO técnico profundo / programmatic SEO multi-página.
- Scraping agresivo sin links del humano (usar URLs provistas + búsqueda pública razonable).
- Autonomía total (publicar / contactar negocios).

## Output canónico del brief

Campos mínimos (síntesis creative brief + requirements small-biz + brand-context):

- Cliente / rubro / zona
- Oferta principal (una)
- Audiencia + situación de compra (JTBD corto)
- CTA primario (+ secundario si aplica)
- Hechos confirmados vs abiertos
- Insights de redes / GBP (tono, assets, inconsistencias)
- Competencia local (3–5) + gaps/oportunidades
- Lenguaje VoC (frases)
- Constraints / anti-goals
- Next: handoff a `visual-direction`

## Implicaciones para el SKILL.md

- Description: triggers de nuevo cliente, redes, “no sé por dónde empezar”.
- Recipe positiva: intake → audit → competitive → VoC → brief → confirmación.
- Template de brief REQUIRED.
- Path de persistencia: `docs/web-design-skills/clients/<slug>/discovery.md` (o `brand/<slug>/discovery.md` — preferir docs del stack para no chocar con Impeccable `brand/`).
- Red flags: saltar a HTML/CSS; inventar precios/servicios; brief sin CTA; más de una oferta primaria sin priorizar.
