# Mesal Café — Astro site

Stack: **Astro 7** (static + islands). Ported from the approved HTML kit.

## Commands

```bash
cd docs/web-design-skills/clients/mesal/web
npm install
npm run dev      # http://localhost:4321
npm run build
npm run preview
```

## Structure

- `src/pages/index.astro` — landing
- `src/components/` — Header, Hero, sections, Footer
- `src/styles/global.css` — design tokens from `direction.md`
- `public/assets/` — logo + Maps/IG photos
- `src/scripts/site.ts` — nav scroll + reviews slider (client)

Legacy flat HTML (reference): `../site-legacy/`
