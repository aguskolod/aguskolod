// @ts-check
import { defineConfig } from 'astro/config';

// Relative base so preview works on gh-pages / raw.githack (not only domain root).
export default defineConfig({
  site: 'https://aguskolod.github.io',
  base: './',
});
