import { readdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      await walk(full);
      continue;
    }
    if (!/\.(html|css|js|mjs)$/.test(entry.name)) continue;
    const text = await readFile(full, 'utf8');
    const next = text
      .replaceAll('"/./', '"./')
      .replaceAll("'/./", "'./")
      .replace(/(["'])\/_astro\//g, '$1./_astro/')
      .replace(/(["'])\/assets\//g, '$1./assets/');
    if (next !== text) {
      await writeFile(full, next);
      console.log('fixed', full);
    }
  }
}

await walk(new URL('../dist', import.meta.url).pathname);
