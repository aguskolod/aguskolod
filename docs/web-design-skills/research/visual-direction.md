# Research: `visual-direction`

Fecha: 2026-09-20  
Prerequisito: brief confirmado de `web-discovery`.

## Pregunta

¿Cómo se traduce marca (a menudo débil) + audiencia en un sistema web concreto: tipografía, color, expression (radius, motion, assets), y estructura de landing — de forma colaborativa, no autónoma?

## Fuentes

### Tipografía / personalidad
- [Rishfield — Font decision framework](https://www.rishfelddesigns.com/how-to-choose-fonts-for-a-brand-a-designers-decision-framework/) — 3–5 traits → categorías; display/body/functional; máx. 2 familias.
- [Brandhorse — Brand typography](https://brandhorse.com/insights/typography-for-brands-selecting-fonts-communicate-message) — atributos → características; contraste competitivo.
- [Daily Creative — Fonts + personality](https://dailycreativeco.com/how-to-choose-fonts-for-your-brand-personality/) — adjetivos primero; feeling target.
- [Patrick Iverson — Font pairing for non-designers](https://patrickiverson.com/visual-identity/how-to-pick-font-pairing-brand/) — serif+sans / sans+serif / una superfamilia; body primero a veces.
- [Brainy — Font pairing](https://brainy.ink/paper/font-pairing-guide) — brand decide pairing, no la tendencia.
- Prior research (sesión): Scale Composer letterform personality; FontFYI classification mapping; NN/g pairing dos/don’ts.

### Color / tokens / a11y
- [137Foundry — Website color system WCAG](https://137foundry.com/articles/website-color-system-brand-accessibility-guide) — base palette + semantic roles; contrast at token time.
- [Digital Heroes — Color system WCAG](https://digitalheroesco.com/journal/color-system-wcag-compliance/) — primitives vs semantic tokens.
- [AET UI colors](https://ls1intum.github.io/ui-ux-guidelines/docs/colors/) — primary/secondary/neutral/status roles.
- [DesignRock — UI color palette](https://designrockdh.com/ui-color-palette-design/) — 60/30/10; CTA reserved.
- WCAG 2.1: text 4.5:1, large/UI 3:1.

### Expression / brand → digital
- [rampstack identity-system-spec](https://github.com/rampstackco/claude-skills/blob/HEAD/skills/brand-identity/references/identity-system-spec.md) — logo, color tokens, icons, imagery style, motion tokens, reduced-motion.
- [What If Design — Brand guidelines vs design system](https://whatifdesign.co/feeds/blog/brand-guidelines-vs-design-system) — guidelines = how brand shows up; system = how we build; character shapes radius/motion/density but usability leads.
- [5Four style guide](https://www.5fourdigital.com/style-guide) — radius scale, photography direction, motion examples.
- [cofoundy brand-identity skill](https://raw.githubusercontent.com/cofoundy/brand-skills/main/skills/brand-identity/SKILL.md) — visual brief for designer (logo/color/type/imagery).

### Style tiles / dirección antes de layout
- [Kanopi — Style tile vs moodboard](https://kanopi.com/blog/what-is-a-style-tile-or-mood-board-and-why-is-it-helpful/) — tiles ≠ layouts; after strategy; with IA/wireframes.
- [Nonprofit MAR — Create style tiles](https://nonprofitmarcommunity.com/how-to-create-style-tiles-for-web-design/) — adjectives from brief → tile (type, color, buttons, imagery).
- [Vanseo — Style guides / moodboards / tiles](https://vanseodesign.com/web-design/style-guides-mood-boards-style-tiles/) — tiles elicit yes/no on visual language without full comps.

### Estructura landing (contenido antes de pixels)
- Research previo: local service wireframe (hero→proof→process→objections→CTA); Fitzgerald Research→UX→Copy→Visual.
- [Silvia Perini case](https://silvia-perini.com/projects/seo-landingpage) — map what page must say and in what order before Figma.

## Principios que entran

1. **Discovery confirmado primero.** Sin `discovery.md` confirmado → devolver a `web-discovery`.
2. **Adjetivos (3–5) → categoría → opciones.** Tipografía y color salen de personalidad + audiencia, no de gusto del agente.
3. **Sistema, no picks sueltos.** Display + body; color con roles (primary CTA, neutrals, accent); expression rules (radius, density, motion, imagery).
4. **Estructura de secciones en el mismo brief** (orden de mensaje) pero **sin pixel layout**. Style tile ≠ wireframe hi-fi.
5. **2–3 direcciones solo si hay ambigüedad real**; si discovery es claro, 1 recomendada + 1 alternativa corta.
6. **Proponer opciones al humano** (fonts/pairings, radius mood) con porqués en lenguaje simple.
7. **Contraste como constraint** desde el brief (CTA text/fill).
8. **Web fonts prácticos** (Google Fonts / licencia clara, ñ, pesos).
9. **Persistir** `direction.md` para kit + build.
10. **No code / no image gen** aquí — eso es `brand-kit-gen` y `landing-build`.

## Mapping rápido (para la skill)

| Adjetivos típicos (local) | Tipo | Radius | Motion | Imagen |
|---|---|---|---|---|
| Urgente, directo, de oficio | Sans sólida / humanist o grotesque | Bajo–medio (poco “pill”) | Ninguno–sutil | Fotos reales, local, sin stock glam |
| Cálido, barrio, cercano | Humanist sans ± serif suave | Medio | Sutil | Personas/local, luz natural |
| Premium, cuidado | Serif display + sans body | Bajo, más aire | Sutil | Editorial, negativo space |
| Técnico, moderno | Geometric sans | Bajo–0 | Mínimo | Producto limpio, diagramas |

## Output canónico

`docs/web-design-skills/clients/<slug>/direction.md` con: personality, type options + pick, color roles, expression, imagery, motion, section structure, anti-patterns, handoff a kit.

## Descartar v1

- Full design system / component library code
- Dark mode obligatorio
- Logo design completo (solo dirección)
- Motion choreography compleja
