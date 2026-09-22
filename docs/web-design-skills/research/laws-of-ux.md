# Research: `laws-of-ux-correct`

Fecha: 2026-09-22

## Fuente canónica

- [Laws of UX](https://lawsofux.com/) — Jon Yablonski
- [llms.txt](https://lawsofux.com/llms.txt) — guía para agentes
- 30 páginas de leyes descargadas con `Accept: text/markdown` (definiciones + takeaways oficiales)

## Propósito de la skill

Skill de **solo corrección**: auditar una web ya presentada (código + captura visual) contra las 30 leyes; devolver fallos con instrucciones precisas de arreglo para el agente.

No reemplaza discovery / visual-direction / brand-kit / landing-build.

## Relación con el stack

| Skill | Rol |
|---|---|
| `landing-craft` | Heurísticas de craft durante build/edits |
| `landing-qa` | Checklist técnico (links, a11y básica, responsive) |
| `laws-of-ux-correct` | Psicología/UX laws con evidencia code+visual |

## Método

1. Catálogo en `reference.md` = definición + takeaways oficiales + fail signals + fix steps.
2. Severidad P0/P1/P2.
3. Persistencia del reporte en `clients/<slug>/laws-of-ux-correct.md`.

## Nota sobre Miller

Los takeaways oficiales advierten no usar “máximo 7” como límite arbitrario de menú; la skill debe chunking, no superstición.
