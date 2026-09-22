# Pipeline — web design skills

Stack independiente de Impeccable. Landings de negocio local. Vos guiás; el agente investiga y propone.

## Cómo pedirlo (para que el agente no se vaya a Impeccable)

Frases útiles:

- “Seguí el stack **web-design-skills** / `web-design-pipeline`”
- “Después del discovery, corré **`visual-direction`** (nuestra skill, no Impeccable)”
- “No uses Impeccable ni `PRODUCT.md` de otro cliente”

Hay una regla always-on en `.cursor/rules/web-design-skills.mdc` que fuerza este routing.

## Orden

0. **`web-design-pipeline`** (router) — si el agente no sabe qué skill tocar.
1. **Intake (vos)** — nombre del cliente, rubro, links (IG / FB / Maps / web), notas.
2. **`web-discovery`** — brief en `docs/web-design-skills/clients/<slug>/discovery.md` → **vos confirmás**.
3. **`visual-direction`** — tipografía, color, expression, estructura → `direction.md` → **vos confirmás**. **No** es Impeccable new-work.
4. **`brand-kit-gen`** — brand board + boceto 9:16 (OpenRouter). Requiere `OPENROUTER_API_KEY`. Modelo default: `openai/gpt-image-2.5-sunburst` (override: `OPENROUTER_IMAGE_MODEL`). → **vos aprobás o pedís cambios**.
5. **`landing-build`** (+ **`landing-craft`** en cada edit) — **Astro** + CSS variables desde `direction.md`, en `clients/<slug>/site/`.
6. **`landing-qa`** — checklist → `qa.md`.
7. **`laws-of-ux-correct`** (opcional / pre-ship) — audita código + visual vs [Laws of UX](https://lawsofux.com/); solo fallos + instrucciones de fix.

## Gates

No saltear confirmaciones. Sin discovery confirmado no hay dirección; sin dirección no hay kit/código (salvo que digas explícitamente “saltear kit”).

## Aislamiento de cliente

Cada cliente vive en `docs/web-design-skills/clients/<slug>/`. Ignorá `PRODUCT.md` / `DESIGN.md` de la raíz si son de otro producto (p. ej. Baterías CABA mientras laburás Mesal).

## Research

Cada skill tiene notas con fuentes en [`research/`](research/).

## Skills

| Skill | Path |
|---|---|
| web-design-pipeline | `.cursor/skills/web-design-pipeline/` |
| web-discovery | `.cursor/skills/web-discovery/` |
| visual-direction | `.cursor/skills/visual-direction/` |
| brand-kit-gen | `.cursor/skills/brand-kit-gen/` |
| landing-craft | `.cursor/skills/landing-craft/` |
| landing-build | `.cursor/skills/landing-build/` |
| landing-qa | `.cursor/skills/landing-qa/` |
| laws-of-ux-correct | `.cursor/skills/laws-of-ux-correct/` |
