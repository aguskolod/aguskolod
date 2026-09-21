# Visual direction — Mesal Café

## Status
- Discovery source: `docs/web-design-skills/clients/mesal/discovery.md`
- Confirmed by human (estructura / CTAs / amenities): **yes** (2026-09-21)
- **Identity rebuild (2026-09-21):** reescrito desde logo IG medido + posts IG + fotos Google Maps del local. **Confirmado humano** (+ ajustes expression/hero).
- Stack: web-design-skills · skill `visual-direction` → `brand-kit-gen`
- Confirmed with: sin secciones Prueba/Para quedarte; reseñas en slider; amenities por simbología en hero; **UI sharp** (botones rectangulares); **hero full-bleed** foto + texto encima; mock **desktop 16:9** (no mobile-first sketch)


## Evidence (fuentes de identidad)
| Fuente | Path / id | Qué aporta |
|---|---|---|
| Logo IG avatar | `kit/refs/logo-instagram.jpg` | Tipografía Didone + sans arco; cacao / oro taza / naranja estrellas |
| Posts IG | `kit/refs/post-1..3.jpg` | Chaqueta naranja viva; letrero madera; proceso/comida; montaña Esquel |
| Maps place photos | `kit/refs/maps/maps-01..10.jpg` (dataset `MTu95ynBeK7pGaDae`) | Salón real: listones sage-gris, madera, ladrillo, piso geométrico, menú backlight, platos |

## Brand mark (source of truth)
- Asset: `kit/refs/logo-instagram.jpg` (+ letrero físico en Maps/IG)
- Composición circular: taza oro brush + **20 / 25** · wordmark **MESAL** · tres estrellas · arco **CAFÉ Y BISTRÓ**
- Tipografía del mark (no sustituir):
  - **MESAL** = Didone de alto contraste (verticales gruesas, serifs finas, swash en **L**, flourish en **M**) — familia tipo Bodoni/Didot, no transitional serif
  - **CAFÉ Y BISTRÓ** + numerales **20/25** = sans geométrica/limpia, all-caps, tracking abierto
- En web: **logo real** (JPG/PNG; SVG si aparece). No inventar monograma hoja/baya ni reemplazar el wordmark con otra display.

## Personality
- Adjectives (3–5): **cálida**, **contemporánea**, **artesanal**, **vecinal**, **acogedora**
- Feeling: “puedo venir seguido, quedarme un rato, y se siente de Esquel — café nuevo de ciudad chica, no brochure patagónico ni confitería de siempre”
- Differentiate:
  - vs María Castaña: más nueva, producción propia, look contemporáneo del salón
  - vs Charlá: todo el día + quedarse (08–00)
  - vs brochure patagónico: comida/gente/salón reales primero
  - vs kits anteriores: **extender logo + materiales del local**, no reinventar marca ni inventar mist/Bricolage

## Typography
El display de marca **es el logo**. Titulares HTML: Didone cercana al wordmark. Body/UI: sans limpia como el arco “CAFÉ Y BISTRÓ”.

### Recommended
- Brand mark: logo IG (no tipografía sustituta del nombre)
- Display (H1/H2 de sección): **Source Serif 4** (Google Fonts) — serif legible; Bodoni Moda descartada por legibilidad en web
- Body / UI / botones: **DM Sans** (Google Fonts)
- Why: el logo sigue siendo el Didone de marca; en HTML preferimos lectura clara sobre contraste tipográfico extremo.
- Weights: Display 600–700; Body 400/500/600
- Mental test: logo MESAL + “Café & bistró de todo el día.” + botones **Menú** / **Cómo llegar**

### Alternatives (1–2)
1. Display **Lora** + body DM Sans — un poco más redonda.
2. Display **Libre Baskerville** + body DM Sans — más clásica.

## Color roles
Medidos del logo (Pillow, regiones) + chaqueta IG + materiales Maps.

| Role | Hex | Source | Usage |
|---|---|---|---|
| Primary (CTA) | `#533B32` | Letras MESAL (median) | Botón **Menú**, links fuertes |
| Primary hover | `#3F2C25` | darken cacao | Hover/active |
| On-primary | `#F6EDE3` | crema marrón clara | Texto sobre primary (no blanco puro) |
| Secondary | `#E4D2BC` | madera/crema salón | Fill del botón outline **Cómo llegar**, paneles suaves — **marroncito**, no blanco |
| Secondary hover | `#D9C4AA` | — | Hover secondary |
| Text | `#533B32` | cacao logo | Titulares y cuerpo |
| Text muted | `#6F645C` | — | Meta, horarios |
| Background | `#EFE4D6` | crema más marrón | Fondo página (menos “blanco”, más cacao claro) |
| Surface | `#E2D2C0` | — | Bandas de sección, track slider, bloques menú |
| Interior sage | `#8A877A` | listones / mostrador Maps | Superficie ocasional / icon wells — **del local**, no inventado |
| Border | `#C9B59E` | — | Separadores |
| Gold | `#A47A33` | taza del logo | Acentos finos, strokes, underline — **no** CTA fill |
| Star terracotta | `#D85931` | estrellas logo | Bullets / detalle puntual |
| Jacket orange | `#F4400B` | chaqueta IG | Energía de marca / hover spark / event — **no** CTA fill |
| Wood (cue) | `#C3A283` | letrero / mesas | Solo en foto o textura sutil, no fill UI masivo |

- Contrast: `#F6EDE3` sobre `#533B32` OK para CTA AA; texto cacao sobre Secondary `#E4D2BC` OK.
- Regla CTA: **solo cacao**. Secondary = marrón claro (no blanco). Oro / terracotta / jacket = acento. Sage = superficie del salón, no “marca verde”.
- Descartar: blanco/off-white `#FFFDF8` / `#F7F3EC` como secundario o fondo de página; mist inventado; Bricolage.

## Expression
- Radius / buttons: **sharp** — rectangulares, **0–4px** max (casi sin redondeo). No soft-medium, no pill.
- Density: **airy-moderado**
- Borders / elevation: **flat honest**; luz cálida en fotos, no glow UI
- Motion: **sutil** (+ `prefers-reduced-motion` en build) — fade/slide del slider de reseñas; hover CTA suave
- Hero layout: **full-bleed photo background** + texto/CTAs encima (overlay moderno). Gradiente/scrim oscuro o cacao suave solo para legibilidad — no cards flotantes, no hero inset, no media en columna lateral.
- Imagery (prioridad):
  1. **Salón Maps** — barra + máquina + vitrina + menú backlight (maps-01) — preferido como fondo de hero
  2. **Platos** — brunch/café (maps-04, maps-06, maps-03)
  3. **Letrero / logo físico** — madera + backlight (post-2, maps-05, maps-07)
  4. **Gente / chaqueta** — vecinal, proceso (post-1, post-3)
  5. Choco Fest = prueba comunitaria puntual, **no** hero permanente
- Texturas opcionales (sutiles): listones verticales; piso geométrico semicircular — como atmósfera, no patrón ruidoso
- Icon style (amenities): iconos claros + **label corto** (Sin TACC / Pet friendly / Cowork) — lineales; no chips
- Logo treatment: **PNG** (`logo.png` / `logo-on-cream.png`) sobre disco crema para contraste en hero full-bleed; no en el nav
- Nav: **fixed**; transparente sobre el hero; fondo crema al scrollear (`is-scrolled`). Sin logo en la barra.

## Section structure
Orden de mensaje. **Sin** “Prueba” ni “Para quedarte”.

**Layout debajo del hero: secciones apiladas a full-width**, una debajo de la otra — **no** grilla de 4 columnas en una sola banda.

1. **Hero (full-bleed)** — foto salón edge-to-edge; encima: logo Mesal + una línea de oferta + CTAs **Menú** / **Cómo llegar** + horario 08–00 + fila de iconos (sin TACC / pet / coworking)
2. **La oferta del día** — sección propia; mañana → tarde → noche, elaboración propia
3. **Menú** — sección propia; preview / CTA a la carta
4. **Reseñas (slider)** — sección propia; carrusel de reseñas (4,9★ / 281)
5. **Cómo llegar** — sección propia; Av. Fontana 769 + Maps
6. **Footer** — IG, horario, NAP

- Primary CTA: **Menú** en hero + sección Menú; secondary **Cómo llegar** = fill `#E4D2BC` + borde/texto cacao (sharp), no blanco.
- Amenities: solo iconografía en hero, nunca sección titulada ni chips con labels largos.
- Copy: **Esquel**, Fontana 769 — no inventar ciudad ni claims no confirmados.
- Anti: mock con 4 columnas iguales bajo el hero; nav “Reservar” inventado.


## Anti-patterns for this brand
- Reemplazar el logo IG por wordmark tipográfico inventado (Bricolage, hoja, etc.)
- Display **transitional** (Source Serif 4) o Inter/Roboto/Arial como voz de marca
- Paleta mist/sage **inventada** sin anclar al salón; o al revés: teñir toda la web de verde
- Usar jacket orange / gold como fill del CTA (roba al cacao del logo)
- Pills + glow + púrpura; botones redondeados / soft radius
- Hero inset, card de foto, collage, o layout “mobile centered” cuando el deliverable es desktop
- Debajo del hero: **4 columnas en una sola fila** en lugar de secciones stacked
- Secundario / fondos en blanco puro o cream casi blanco
- Brochure patagónico stock; Japandi genérico sin foto del local
- Landings café “AI sloppy” (bento, chips amenities, testimonials template, ciudad inventada)

- Sección “Para quedarte” / “Prueba” estática
- Inventar precios o WhatsApp
- Hero solo Choco Fest / barra de chocolate
- PRODUCT.md / DESIGN.md de otro cliente

## Handoff
- Ready for `brand-kit-gen`: **yes** — kit aprobado humano (2026-09-21)
- Kit: `kit/brand-board.png` + `kit/landing-16x9.png`
- Build: `docs/web-design-skills/clients/mesal/site/` (landing HTML)
- Persist path: `docs/web-design-skills/clients/mesal/direction.md`
