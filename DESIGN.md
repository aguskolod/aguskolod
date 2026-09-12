<!-- impeccable:design-schema 1 -->
# Design

Working draft — identidad mínima para mock / landing. Dirección visual en marcha.

## Visual Intent

Comercio de barrio que resuelve YA: carbón + papel + acento de borne. Tipografía industrial argentina para la voz del negocio. El **24 hs** no es un chip: es un **cartel de neón de tubos** (SVG) con glow, parpadeo e interacción (prender/apagar). Sin look startup, sin violeta AI, sin cards de más.

## Signature: neón 24 hs

- **Formato:** SVG (tubos = strokes: vidrio + glow + núcleo caliente). No Lottie obligatorio; SVG + CSS es liviano e interactivo.
- **Comportamiento:** hum continuo, flicker irregular tipo tubo real, tap/click enciende/apaga, “parpadeo fuerte” opcional.
- **Contenido:** “ABIERTO” en rojo neón + “24 HS” en amarillo borne.
- **Prototype:** `brand/neon-24.html`
- **Accesible:** el SVG es decorativo; texto equivalente “Abierto 24 horas” en Archivo junto al cartel.

## Color

| Token | Hex | Rol |
| --- | --- | --- |
| `--carbon` | `#141414` | Logo, títulos, fondos oscuros |
| `--paper` | `#F6F6F4` | Fondo claro |
| `--smoke` | `#5C5C5A` | Texto secundario |
| `--line` | `#D8D8D4` | Bordes |
| `--accent` | `#FFCC33` | Acento / CTA / neón “24 HS” (**borne eléctrico**, menos mostaza) |
| `--accent-hot` | `#FFE566` | Núcleo del tubo amarillo |
| `--urgent` | `#FF3B3B` | Neón “ABIERTO” |
| `--urgent-soft` | `#FF6B6B` | Núcleo del tubo rojo |

**Decisión abierta (usuario dudando):** el viejo `--accent-dark` `#C99800` (mostaza) queda **descartado como hover**. Hover del CTA = mismo `#FFCC33` un poco más brillante (`filter: brightness(1.08)`) o carbón invertido, no mostaza.

Alternativas vistas en el prototype: `#E8B40A` (anterior), `#F5C518` (safety). Default provisional: `#FFCC33`.

Preview: `brand/palette-mobile.png`, `brand/preview.html`, `brand/neon-24.html`.

## Typography

### 1. Archivo (Omnibus-Type, BA) — voz de marca + UI

- Wordmark, headlines, nav, body, botones.
- Black / Bold títulos; Regular / Medium cuerpo.

### 2. Neón SVG (no font) — pieza 24 hs

- Las letras del cartel son **paths de tubo**, no DSEG7.
- DSEG7 queda como opción secundaria solo si más adelante queremos un reloj LED aparte (idea A); no es el signature ahora.

### Qué no usamos

Inter, Roboto, system-ui como voz de marca; Orbitron “racing”; script/cursive; chips/badges para el 24 hs.

## Logo direction (pendiente de mock)

Mark mínimo + wordmark Archivo Black. El neón puede vivir en el hero como pieza, no necesariamente dentro del logo.

## Motion

- Neón: `hum` + `flicker` irregulares; off state = tubos fríos.
- CTA: hover brightness, sin bounce.
- Respetar `prefers-reduced-motion` (apagar flicker, dejar glow estático).
