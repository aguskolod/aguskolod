<!-- impeccable:design-schema 1 -->
# Design

Working draft — identidad mínima para mock / landing. Dirección visual en marcha.

## Visual Intent

Comercio de barrio que resuelve YA: carbón + papel + acento borne eléctrico. Tipografía industrial argentina (Archivo) para UI/marca. Signature del **24 hs**: **cartel neón tradicional** (cursiva + bloque + ícono), no chip ni letras geométricas.

## Signature: cartel neón

Refs del cliente en `brand/refs/`:
- `neon-electric-cinema.jpg` — cursiva “Electric” + bloque “CINEMA”; tubo rojo con núcleo amarillo.
- `neon-tonys.jpg` — tipografía de tubo + ícono (vaso) como pieza del cartel.

Traducción a Baterías CABA:
- **Script:** “Abierto” / “Baterías” / “Siempre” (Great Vibes u otra cursiva de tubo).
- **Bloque caps:** “24 HS” o “CABA” (Archivo Black), tracking amplio.
- **Ícono neón:** batería outline (análogo al vaso de Tony’s).
- **Color de tubo:** envelope rojo + núcleo **borne** `#FFCC33` / hot `#FFE566`.
- **Prototype:** `brand/neon-sign.html` (glow, flicker, on/off).
- **Accesible:** texto equivalente en Archivo (“Abierto 24 horas”).

## Color

| Token | Hex | Rol |
| --- | --- | --- |
| `--carbon` | `#141414` | Logo, títulos, fondos oscuros |
| `--paper` | `#F6F6F4` | Fondo claro |
| `--smoke` | `#5C5C5A` | Texto secundario |
| `--line` | `#D8D8D4` | Bordes |
| `--accent` / borne | `#FFCC33` | CTA + núcleo amarillo del neón |
| `--accent-hot` | `#FFE566` | Núcleo más caliente |
| `--tube-red` | `#FF1E1E` | Envelope del tubo |
| `--glow-red` | `#FF3B3B` | Bloom |

Hover CTA: brightness del borne. Mostaza `#C99800` descartada.

## Typography

1. **Archivo** — voz de marca + UI + bloque del neón (“24 HS”).
2. **Script neón** (Great Vibes u equivalente) — solo la cursiva del cartel.
3. DSEG7 queda opcional si más adelante hay reloj LED aparte; no es el signature.

## Logo direction

Mark mínimo + Archivo Black. El neón vive en el hero como pieza, no dentro del logo.

## Motion

Hum + flicker de tubo; off = tubos fríos. Respetar `prefers-reduced-motion`.
