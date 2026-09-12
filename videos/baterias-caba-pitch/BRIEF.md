---
workflow: product-launch-video
flow: automation
storyboard: no
message: "Cuando te quedás sin batería, entrás desde el celular — y esta landing está hecha para eso"
destination: whatsapp
aspect: 1920x1080
language: es
audience: posibles clientes dueños del local (pitch comercial)
length: 45s
angle: site-showcase-mobile-first
narration: yes
---

## Intent

Video de pitch para mandar a posibles clientes del negocio Baterías CABA (Viamonte 2031).
Muestra la landing real: **mobile es el protagonista** (si te quedás sin batería entrás desde el celular),
y también enseña la versión desktop. Tono directo, comercial, asfalto + naranja señal. No inventar
features: venta, carga, 24 hs, asistencia en el lugar, reseñas Google, llamar / WhatsApp.

## Assets

- Local URL `http://127.0.0.1:8765/index.html` — landing mock en el repo (fuente de captura).
- Brand tokens locked: asphalt `#0E0F10`, ink `#F2F1EC`, signal `#FF5A1F`, WA `#25D366`, Saira + Inter Tight.

## Customizations

- Feature the site's own captured screens as the video's assets (show-it-as-is showcase).
- Mobile viewport captures are primary; desktop is a secondary beat.
- Show phone chrome / device frame for mobile shots; desktop as laptop or full-bleed browser plate.
- Spanish voiceover (offline Kokoro — HeyGen not signed in).
- Soft BGM under VO (offline MusicGen if needed).

## Notes

- Autónomo: usuario dijo "dale / armamelo" — no pausar en storyboard.
- Auth: not signed in to HeyGen; continue offline (Kokoro + local music).
- Aspect 16:9 para ver mobile + desktop en el mismo cuadro sin aplastar el pitch.
- Incluir CTAs reales: 11 4061-8555 / WhatsApp.
