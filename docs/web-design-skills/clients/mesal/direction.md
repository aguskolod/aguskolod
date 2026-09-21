# Visual direction — Mesal Café

## Status
- Discovery source: docs/web-design-skills/clients/mesal/discovery.md
- Confirmed by human: **yes** (2026-09-21)
- Stack: web-design-skills · skill `visual-direction`
- Date proposed: 2026-09-21
- Confirmed with: estructura sin Prueba/Para quedarte; reseñas en slider; amenities por simbología en hero

## Personality
- Adjectives (3–5): **cálida**, **contemporánea**, **artesanal**, **vecinal**, **acogedora**
- Feeling we want visitors to have: “puedo venir seguido, quedarme un rato, y se siente de Esquel — no un brochure de turismo ni la confitería de siempre”
- Differentiate from local norm by:
  - vs María Castaña: más nueva, limpia y de “producción propia”, sin vibe de clásico saturado
  - vs Charlá: menos specialty-café cerrado; más **todo el día + quedarse**
  - vs brochure patagónico: montaña como contexto, no como postcard; comida y gente reales primero

## Typography
Sans humanista / grotesque con carácter = cercana y actual; evita la serif “café premium IA” sobre crema.

### Recommended
- Display: **Bricolage Grotesque** (Google Fonts) — títulos, wordmark tipográfico “Mesal Café”
- Body: **Source Sans 3** (Google Fonts) — UI, párrafos, menú meta
- Why (adjectives → category → this pick): cálida + contemporánea + artesanal → grotesque con irregularidad suave (Bricolage) + humanist sans legible en español (Source Sans 3). Buen soporte `ñ`/tildes; licencia libre web.
- Weights to use: Display 600–800; Body 400/600; evitar thin
- Mental test: *“Café & bistró de todo el día, para quedarte.”* / *“Av. Fontana 769 · 08:00–00:00 · sin TACC · pet friendly”*

### Alternatives (1–2)
1. **Más editorial / suave:** Display **Fraunces** (soft) + body **Source Sans 3** — si preferís más “carta de café”, a costa de acercarte al clúster serif-cálido (usamos piedra fría + cacao, no terracota).
2. **Más limpia / menos carácter:** Display **Manrope** + body **Source Sans 3** — más genérica; solo si Bricolage se siente demasiado “diseño”.

## Color roles
Luz de mañana en Esquel (niebla/piedra) + cacao (café / chocolate comunitario) — no naranja de urgencia, no purple glow, no terracota-on-cream default.

| Role | Hex | Usage |
|---|---|---|
| Primary (CTA) | `#4A2C20` | Botón **Menú**, links de acción fuerte |
| Primary hover | `#3A2219` | Hover/active del CTA |
| On-primary | `#F7F4EF` | Texto sobre primary |
| Text | `#1C2420` | Titulares y cuerpo |
| Text muted | `#5C675F` | Meta, horarios, captions |
| Background | `#EEF1EC` | Fondo página (niebla / piedra fría) |
| Surface / muted | `#E2E7E1` | Bandas, cards de prueba, bloques menú |
| Border | `#C5CEC6` | Separadores suaves |
| Accent | `#6B8F71` | Detalles (chips sin TACC / pet / coworking), no CTA |
| Accent soft | `#D7E3D8` | Fondos de chips |
| Map / secondary action | `#1C2420` outline | Botón **Cómo llegar** (ghost/outline sobre fondo) |

- Contrast notes (CTA label on primary): `#F7F4EF` sobre `#4A2C20` ≈ alto contraste (objetivo AA 4.5:1+). Texto muted `#5C675F` sobre `#EEF1EC` revisar en build; si falla, subir a `#4A554E`.

## Expression
- Radius / buttons: **soft-medium** (~10–12px) — cercana, no pill, no 0 sharp industrial
- Density: **airy-moderado** — aire para “quedarse”; no dashboard apretado ni luxury vacío
- Borders / elevation: **flat honest** — bordes suaves, poca sombra; elevación mínima solo en hover de CTAs
- Motion level: **sutil** — fade/slide leve en secciones; respetar `prefers-reduced-motion` en build
- Imagery direction: **fotos reales** del local, platos, pastelería, gente/equipo, Fontana/Esquel; Choco Fest como prueba social puntual, no hero permanente. Evitar stock de cabaña/nieve/mate genérico.
- Icon style (amenities): **simbología casi sin texto** — iconos custom/lineales (sin TACC, pet, coworking/lectura, etc.), legibles por forma; tooltip/`aria-label` para a11y; **no** chips con copy, **no** fila de pills, **no** emoji como sistema

## Section structure
Orden de mensaje (no layout pixel). **Sin** secciones “Prueba” ni “Para quedarte” (rechazadas 2026-09-21).

1. **Hero** — marca **Mesal Café** + oferta en una línea + CTAs **Menú** / **Cómo llegar** + horario 08–00  
   - En el mismo hero (o franja inmediata): **fila de iconos** sin TACC / pet / coworking·lectura — simbología, casi sin texto
2. **La oferta del día** — café, pastelería artesanal, almuerzo, noche (coctelería/tapeo) — elaboración propia
3. **Menú** — preview / CTA fuerte a la carta (asset Open hasta que entreguen PDF/URL)
4. **Reseñas (slider)** — prueba como **carrusel/slider** de reseñas (Google u otro), no bloque estático de “4,9★ + frase”; el score puede ir como meta del slider, no como sección de marketing
5. **Cómo llegar** — dirección Fontana 769 + mapa/link + teléfono secundario
6. **Footer** — IG, horario, NAP (+ repetir iconos amenity solo si hace falta, sin inventar sección)

- Primary CTA placement intent: **Menú** visible en hero y repetido en sección Menú; **Cómo llegar** a la par (secundario visual, igual de claro).
- Amenities: **nunca** como sección titulada ni chips con labels largos; solo iconografía anclada al hero (o al pie del menú si el humano lo pide después).

## Anti-patterns for this brand
- Inter / Roboto / Arial / system como display
- Pills + glow + púrpura; naranja “urgencia”; borne/amarillo ferretería
- Crema + serif alto contraste + terracota (clúster IA)
- Landings café “AI sloppy” (bento grids genéricos, chips de amenities, testimonials template)
- Sección “Para quedarte” / “Lo que nos hace únicos” con pills
- Sección “Prueba” estática tipo quote wall; la prueba es **slider de reseñas**
- Brochure patagónico (glaciar, cabaña stock) como hero
- Clonar look “confitería clásica” de María Castaña
- Inventar precios o WhatsApp
- Hero solo Choco Fest
- Usar PRODUCT.md / DESIGN.md de Baterías CABA

## Alternative (si querés más “café clásico”)
Misma estructura y roles de color, pero tipografía **Fraunces + Source Sans 3** y radius un poco más suave (14px). Feeling más carta de domingo; menos contemporáneo.

## Handoff
- Ready for `brand-kit-gen`: **yes**
- Persist path: `docs/web-design-skills/clients/mesal/direction.md`
