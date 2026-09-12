<!-- impeccable:design-schema 1 -->
# Design

Working draft — identidad mínima para mock / landing.

## Visual Intent

Comercio de barrio que resuelve YA: carbón + papel + acento borne eléctrico `#FFCC33`. Tipografía Archivo para UI/marca. Sin neón como pieza hero (descartado).

## Signature: barra / carrusel superior

Franja **fina** fija arriba de la página (marquee / ticker) con mensajes rotativos o en scroll infinito. No chip gigante, no cartel neón.

### Contenido propuesto del carrusel

1. `ABIERTO 24 HS`
2. `11 4061-8555`
3. `WhatsApp · te respondemos ya`
4. `Viamonte 2031, CABA`
5. `Venta y carga de baterías`

Separadores sutiles (punto · o barra). Tap en teléfono / WhatsApp = link real.

### Look

- **Definido:** fondo borne `#FFCC33` + texto carbón `#141414`.
- Alto ~36px, Archivo bold, tracking amplio, uppercase.
- Motion: scroll horizontal continuo lento; pausa en hover; estático si `prefers-reduced-motion`.

Prototype: `brand/marquee.html` (variante borne).

## Color

| Token | Hex | Rol |
| --- | --- | --- |
| `--carbon` | `#141414` | Fondos oscuros, barra ticker |
| `--paper` | `#F6F6F4` | Fondo página |
| `--smoke` | `#5C5C5A` | Texto secundario |
| `--line` | `#D8D8D4` | Bordes |
| `--accent` / borne | `#FFCC33` | CTA primario (Llamar) + ticker |
| `--accent-hot` | `#FFE566` | Hover / brillo |
| `--wa` | `#25D366` | CTA secundario WhatsApp (verde real) |

Hover CTA primario: brightness del borne. WhatsApp: verde `#25D366`. Mostaza `#C99800` descartada. Neón descartado.

## Shape

Botones y CTAs **rectangulares** (`border-radius: 0`). Sin pills ni radios suaves de UI genérica.

## Typography

1. **Archivo** — marca, UI, ticker.
2. Sin script neón. Sin DSEG7 como signature.

## Logo direction

Wordmark tipográfico **Baterías CABA** (Archivo Black, stacked con subtítulo `Viamonte · 24 hs` en nav) + **isotipo generado** en `brand/isotype.png` (batería carbón + borne). El “24 hs” también vive en el ticker.

## Landing structure

Ver [`LANDING.md`](LANDING.md): ticker → hero → servicios → cómo funciona → nosotros → reseñas Google → contacto/mapa → footer.  
CTA: **Llamar** primario, WhatsApp secundario.

## Motion

Ticker continuo suave. CTAs: brightness. Respetar `prefers-reduced-motion` (ticker estático o fade entre mensajes).

## Descartado

Cartel neón cursiva/tubos como pieza principal (refs en `brand/refs/` solo histórico).
