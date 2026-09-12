<!-- impeccable:design-schema 1 -->
# Design

Working draft — identidad mínima para mock / landing. Se refinará al construir la primera superficie.

## Visual Intent

Comercio de barrio que resuelve YA: carbón + papel + un acento de “borne de batería”. Tipografía industrial argentina para la voz del negocio; tipografía de display digital solo para el tratamiento de **24 hs** (pieza visual, no chip). Sin look startup, sin violeta AI, sin cards de más.

## Color

| Token | Hex | Rol |
| --- | --- | --- |
| `--carbon` | `#141414` | Logo, títulos, fondos oscuros |
| `--paper` | `#F6F6F4` | Fondo claro |
| `--smoke` | `#5C5C5A` | Texto secundario |
| `--line` | `#D8D8D4` | Bordes |
| `--accent` | `#E8B40A` | CTA / acento |
| `--accent-dark` | `#C99800` | Hover acento |
| `--urgent` | `#C62828` | Badge 24 hs (opcional, controlado) |

Preview: `brand/palette-mobile.png`, `brand/preview.html`.

## Typography

### 1. Archivo (Omnibus-Type, BA) — voz de marca + UI

- **Por qué:** grotesca industrial hecha en Buenos Aires; se siente taller/cartelería sin ser Inter/Geist. Buena en Black (logo/titulares) y Regular (cuerpo).
- **Uso:** wordmark “Baterías CABA”, headlines, nav, body, botones.
- **Pesos:** Black / Bold títulos; Regular / Medium cuerpo y UI.

### 2. DSEG7 Classic — solo el cartelito 24 hs

- **Por qué:** es la familia que imita reloj digital / display de 7 segmentos (LCD). Eso es exactamente el “cartelito de horas” que pediste: presente, reconocible, no gigante.
- **Uso exclusivo:** badge / chip `24` o `24:00` / `24 HS`. No en párrafos ni en el logo principal.
- **Accesible:** el badge visual va acompañado de texto real (“Abierto 24 horas”) en Archivo para lectores de pantalla y SEO.
- **Fallback web fácil (si aún no hosteamos DSEG):** `Share Tech Mono` o `VT323` (Google Fonts) como interim; DSEG7 sigue siendo el target.

### Qué no usamos

Inter, Roboto, system-ui como voz de marca; Orbitron “racing”; script/cursive; una sola font para todo (el 24 hs necesita su propia voz).

## Logo direction (pendiente de mock)

Mark mínimo (batería o rayo geométrico) + wordmark Archivo Black. Sin isotipo elaborado.

## Motion (later)

Poco: hover en CTA, blink suave opcional del colon en el badge 24 hs (muy contenido). Sin bounce.
