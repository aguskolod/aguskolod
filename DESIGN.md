<!-- impeccable:design-schema 1 -->
# Design

Identidad **Fusión A** — Urgencia sharp (base) + wordmark tipográfico puro.

## Visual Intent

Noche asfalto + señal naranja. Comercio que atiende YA, sin cliché de batería/borne amarillo. Marca = tipografía, no isotipo.

## Signature: barra superior (borne strip)

Franja fina fija arriba con scroll infinito. Fondo **signal** `#FF5A1F`, texto blanco. Alto ~36px, Inter Tight bold, tracking amplio, uppercase.

### Contenido

1. `Abierto 24 horas`
2. `Viamonte 2031 · CABA`
3. `Venta y carga de baterías`
4. `11 4061-8555`
5. `Respuesta inmediata`

Motion: scroll horizontal continuo; estático si `prefers-reduced-motion`.

## Color

| Token | Hex | Rol |
| --- | --- | --- |
| `--asphalt` | `#0E0F10` | Fondo página |
| `--asphalt-2` | `#16181A` | Paneles / bandas |
| `--ink` | `#F2F1EC` | Texto primario |
| `--ink-dim` | `rgba(242,241,236,0.62)` | Texto secundario |
| `--line` | `rgba(242,241,236,0.12)` | Bordes |
| `--signal` | `#FF5A1F` | Acento + CTA Llamar + ticker |
| `--wa` | `#25D366` | CTA WhatsApp (verde real) |

## Shape

Botones y CTAs **rectangulares** (`border-radius: 0`). Sin pills.

## Typography

1. **Saira** (500–800) — display, wordmark, titulares. Industrial/automotriz, legible en español (reemplaza Syne).
2. **Inter Tight** — UI, body, ticker.

## Logo

**Solo wordmark tipográfico:** `BATERÍAS` + `CABA` (CABA en signal) + meta con presencia **`24 hs`** (signal) + **`Viamonte 2031`**. Sin monograma BC, sin isotipo de batería. Sin barrios (Recoleta/Balvanera) en hero.

## CTAs

- **Hero:** botones huecos (borde fuerte), mismo ancho; al hover se rellenan con animación de fill vertical.
- **Sticky mobile:** oculto mientras se ven los CTAs del hero; aparece al scrollear. Rellenos sólidos (Llamar / WhatsApp).
- **Nav desktop:** CTAs sólidos compactos.

## Landing structure

Ver [`LANDING.md`](LANDING.md): ticker → hero → servicios → cómo funciona → nosotros → reseñas Google → contacto/mapa → footer.  
CTA: **Llamar** primario (signal), WhatsApp secundario (verde).

## Motion

Ticker continuo. Fill de botones huecos. Sticky slide-in. Reveals al scroll. Respetar `prefers-reduced-motion`.

## Descartado

- Borne amarillo `#FFCC33` como identidad
- Isotipo / monograma de batería
- Archivo / Syne como display de marca
- Fondos paper/cream claros como base
- Pills, neón cursiva, glow genérico
- Kicker “Recoleta / Balvanera”
