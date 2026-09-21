# Visual direction — Mesal Café

## Status
- Discovery source: docs/web-design-skills/clients/mesal/discovery.md
- Confirmed by human: **yes** (2026-09-21) — estructura / CTAs / amenities
- **Identity revision (2026-09-21):** anclar al **logo IG actual**. Se descarta Bricolage + mist verde por no coincidir con la marca viva.
- Stack: web-design-skills · skill `visual-direction` → `brand-kit-gen`
- Confirmed with: sin secciones Prueba/Para quedarte; reseñas en slider; amenities por simbología en hero

## Brand mark (source of truth)
- Asset: `docs/web-design-skills/clients/mesal/kit/refs/logo-instagram.jpg` (avatar IG `@mesalcafe`)
- Wordmark serif ornamentado **MESAL** + taza oro/bronce + “20 / 25” + tres estrellas naranjas + arco **CAFÉ Y BISTRÓ**
- En web: usar el **logo real** (PNG/JPG ahora; SVG si aparece). No inventar monograma hoja/baya ni reemplazar el wordmark con otra display font.

## Personality
- Adjectives (3–5): **cálida**, **contemporánea**, **artesanal**, **vecinal**, **acogedora**
- Feeling we want visitors to have: “puedo venir seguido, quedarme un rato, y se siente de Esquel — no un brochure de turismo ni la confitería de siempre”
- Differentiate from local norm by:
  - vs María Castaña: más nueva y de producción propia
  - vs Charlá: más todo el día + quedarse
  - vs brochure patagónico: comida/gente reales primero
  - vs kit inventado: **extender el logo existente**, no reinventar marca

## Typography
El display de marca **es el logo**. Titulares HTML: serif cercana al wordmark; body/UI: sans limpia (como “CAFÉ Y BISTRÓ”).

### Recommended
- Brand mark: logo IG (no tipografía sustituta)
- Display (titulares de sección): **Source Serif 4** (Google Fonts)
- Body / UI: **Source Sans 3** (Google Fonts)
- Why: el logo ya aporta el serif ornamentado; Source Serif 4 + Source Sans 3 lo acompañan sin pelear. **No** Bricolage Grotesque como voz de marca.
- Weights: Display 600–700; Body 400/600
- Mental test: logo MESAL + “Café & bistró de todo el día.” + botones Menú / Cómo llegar

### Alternatives (1–2)
1. Display **Libre Baskerville** + body Source Sans 3 — más clásica.
2. Display solo logo + body **Nunito Sans** — más redonda; solo si Source Sans se siente fría.

## Color roles
Del logo: cacao + oro/bronce + naranja estrella, sobre blanco cálido.

| Role | Hex | Usage |
|---|---|---|
| Primary (CTA) | `#3D2A1F` | Botón **Menú**, links fuertes |
| Primary hover | `#2E1F17` | Hover/active |
| On-primary | `#FFFDF9` | Texto sobre primary |
| Text | `#3D2A1F` | Titulares y cuerpo |
| Text muted | `#6B5E52` | Meta, horarios |
| Background | `#FFFDF9` | Fondo página |
| Surface / muted | `#F3EEE6` | Bandas, cards slider, bloques menú |
| Border | `#D9D0C4` | Separadores |
| Gold | `#B8954A` | Acentos finos, icon strokes opcionales (no CTA fill) |
| Star orange | `#D4783A` | Detalle puntual (estrellas / bullets), no CTA |
| Map / secondary | outline `#3D2A1F` | Botón **Cómo llegar** |

- Contrast notes: `#FFFDF9` sobre `#3D2A1F` OK para CTA. Evitar mist-verde `#EEF1EC` / sage `#6B8F71` del kit anterior.

## Expression
- Radius / buttons: **soft-medium** (~10–12px) — cercana, no pill
- Density: **airy-moderado**
- Borders / elevation: **flat honest**
- Motion level: **sutil** (+ `prefers-reduced-motion` en build)
- Imagery: fotos reales del local/platos/gente; Choco Fest como prueba puntual, no hero permanente
- Icon style (amenities): **simbología casi sin texto** — lineales; stroke cacao o gold; no chips, no emoji system
- Logo treatment: claro sobre fondo claro; respetar proporciones; no recolorear a verde

## Section structure
Orden de mensaje. **Sin** “Prueba” ni “Para quedarte”.

1. **Hero** — logo Mesal + oferta + CTAs **Menú** / **Cómo llegar** + horario 08–00 + fila de iconos (sin TACC / pet / coworking)
2. **La oferta del día** — mañana → tarde → noche, elaboración propia
3. **Menú** — preview / CTA a la carta
4. **Reseñas (slider)** — carrusel de reseñas
5. **Cómo llegar** — Av. Fontana 769 + Maps
6. **Footer** — IG, horario, NAP

- Primary CTA: **Menú** en hero + sección Menú; **Cómo llegar** a la par.
- Amenities: solo iconografía en hero, nunca sección titulada ni chips.

## Anti-patterns for this brand
- Reemplazar el logo IG por wordmark tipográfico inventado (Bricolage, hoja, etc.)
- Paleta mist/sage inventada que ignore cacao/oro/naranja del logo
- Inter / Roboto / Arial / system como display
- Pills + glow + púrpura; brochure patagónico stock
- Landings café “AI sloppy” (bento, chips amenities, testimonials template)
- Sección “Para quedarte” / “Prueba” estática
- Inventar precios o WhatsApp
- Hero solo Choco Fest
- PRODUCT.md / DESIGN.md de Baterías CABA

## Handoff
- Ready for `brand-kit-gen`: **yes** (regenerar con logo como `input_references`)
- Persist path: `docs/web-design-skills/clients/mesal/direction.md`
