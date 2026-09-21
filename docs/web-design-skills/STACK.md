# Web design skills stack

Stack propio e **independiente de Impeccable** para landings de negocio local.

## Objetivo

Guiar el trabajo de diseño web sin autonomía total: el humano ingresa cliente/redes y aprueba gates; el agente investiga, propone dirección con fundamento, genera brand kit, implementa y hace QA.

## Pipeline

1. **Intake** (humano): nombre del cliente, redes, notas.
2. **`web-discovery`**: brief de cliente/audiencia/oferta/CTA + insights.
3. **`visual-direction`**: sistema visual + expression rules + estructura de secciones.
4. **`brand-kit-gen`**: brand board + boceto 9:16 (OpenRouter / GPT Image).
5. **`landing-build`**: implementar en **Astro** (CSS variables desde direction; con **`landing-craft`** en edits).
6. **`landing-qa`**: checklist técnico + fidelidad a la dirección.

## Build default

- **Framework:** Astro (static)
- **Style:** CSS + tokens de `direction.md` (no Tailwind por defecto)
- **Path:** `docs/web-design-skills/clients/<slug>/site/`
- Override solo si el humano lo pide.

## Skills

| Skill | Rol |
|---|---|
| `web-design-pipeline` | Router: qué skill sigue; bloquea Impeccable en este flujo |
| `web-discovery` | Discovery / competitive + social audit |
| `visual-direction` | Brand → web system (type, color, radius, motion, assets, IA) |
| `brand-kit-gen` | Visualizar dirección con image gen |
| `landing-craft` | Guidelines de craft durante build/correcciones |
| `landing-build` | Implementación Astro fiel al brief + kit |
| `landing-qa` | QA de cierre |

## Autoría

Cada skill se escribe **solo después** de investigación documentada en `research/<skill>.md` con fuentes. Ver plan acordado: research → note → SKILL.md → verificación.

Uso: [`PIPELINE.md`](PIPELINE.md).

## Relación con Impeccable

Ninguna. Este stack no invoca ni depende de comandos Impeccable. Pueden coexistir en el mismo repo.
