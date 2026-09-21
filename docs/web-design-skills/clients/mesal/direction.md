# Visual direction — Mesal Café

## Status
- Discovery source: docs/web-design-skills/clients/mesal/discovery.md
- Confirmed by human: no
- Stack: web-design-skills · skill `visual-direction`
- Date proposed: 2026-09-21

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
- Icon style (if any): lineales simples, stroke medio, esquina acorde al radius; sin emoji como sistema

## Section structure
Orden de mensaje (no layout pixel):

1. **Hero** — marca **Mesal Café** + oferta en una línea + CTAs **Menú** / **Cómo llegar** + señal de horario 08–00
2. **Prueba** — 4,9★ / reseñas + una frase VoC (“ciudad grande / montaña” o “punto de encuentro”)
3. **La oferta del día** — café, pastelería artesanal, almuerzo, noche (coctelería/tapeo) — elaboración propia
4. **Para quedarte** — sin TACC · pet friendly · coworking/lectura (chips, no cards de marketing)
5. **Menú** — preview / CTA fuerte a la carta (asset Open hasta que entreguen PDF/URL)
6. **Esquel / cómo llegar** — dirección Fontana 769 + mapa/link + teléfono secundario
7. **Footer** — IG, horario, NAP

- Primary CTA placement intent: **Menú** visible en hero y repetido en sección Menú; **Cómo llegar** siempre a la par (secundario visual, igual de claro).

## Anti-patterns for this brand
- Inter / Roboto / Arial / system como display
- Pills + glow + púrpura; naranja “urgencia”; borne/amarillo ferretería
- Crema + serif alto contraste + terracota (clúster IA)
- Brochure patagónico (glaciar, cabaña stock) como hero
- Clonar look “confitería clásica” de María Castaña
- Inventar precios o WhatsApp
- Hero solo Choco Fest
- Usar PRODUCT.md / DESIGN.md de Baterías CABA

## Alternative (si querés más “café clásico”)
Misma estructura y roles de color, pero tipografía **Fraunces + Source Sans 3** y radius un poco más suave (14px). Feeling más carta de domingo; menos contemporáneo.

## Handoff
- Ready for `brand-kit-gen`: no (pending confirm)
- Persist path: `docs/web-design-skills/clients/mesal/direction.md`
