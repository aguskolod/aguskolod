# Landing brief — Mesal Café

Estado: **propuesta** (2026-09-21). Sin implementar hasta confirmación.
Reemplaza la estructura de secciones de `direction.md` (El día sale).
Tokens visuales que se mantienen: cacao `#533B32`, secondary `#E4D2BC`, fondo `#EFE4D6`, botones sharp 0–4px, logo PNG real, fotos del local.

## Por qué se siente artificial

La página repite el molde de landing generada:

- Cada bloque es ceja + titular serif + párrafo + grilla.
- “Mañana / Mediodía / Noche” es una taxonomía de brochure, no cómo se vive el café.
- Las “reseñas” son frases de prensa con pie interno (`VoC · Red43`).
- Menú e Instagram se confunden.
- La misma foto de comida aparece dos veces.
- Todo está centrado, con el mismo aire, el mismo borde, el mismo ritmo.

Una landing de cafetería tiene que sentirse como el salón: foto, dato, acción. Poco texto. Nada de sistema de cards.

## Estructura final

Una sola página. Secciones apiladas, full width. Sin “El día”. Sin “Prueba”. Sin “Para quedarte”.

1. **Nav**
2. **Hero**
3. **El lugar** (una foto, una frase)
4. **Menú**
5. **Google** (prueba, sin citas inventadas)
6. **Cómo llegar**
7. **Footer**

### 1. Nav

- Desktop: fija. Transparente sobre el hero; al scrollear, fondo `#EFE4D6`.
- Izquierda: logo chico (`logo.png`), link a `#inicio`.
- Derecha: anclas **Menú**, **Cómo llegar**. Nada más. Sin botón Menú suelto.
- Mobile: sin barra encima del hero. Al scrollear, barra chica con logo + “Cómo llegar”.

### 2. Hero

Foto del salón, edge to edge, scrim oscuro para leer.

Encima, alineado al centro en mobile y un poco a la izquierda en desktop (no un póster simétrico):

- Logo PNG claro, grande, halo muy suave que sigue la forma. Sin disco, sin placa, sin frost circular.
- Una sola línea: **Café y bistró de todo el día.**
- Horario: **08:00–00:00**
- Dos botones sharp: **Menú** (fill cacao) y **Cómo llegar** (fill `#E4D2BC`).
- Debajo, en una sola línea, tres datos con icono y label corto: Sin TACC · Pet friendly · Cowork. Sin cajas, sin chips.

El hero ocupa el viewport. En mobile el logo es más chico para que título y botones entren sin cortar los iconos.

### 3. El lugar

No es una sección con título de marketing. Es una foto ancha del salón (distinta a la del hero) y, encima o al lado en desktop, una frase:

> Elaboración propia, en el centro de Esquel.

Sin grilla de tres. Sin mañana/mediodía/noche. Sin cards.

### 4. Menú

Trabajo de la sección: que la persona vea que hay carta y sepa dónde está.

- Título: **La carta**
- Una línea: café, pastelería y platos del día. Sin párrafo de brochure.
- Foto de un plato, distinta a cualquier otra de la página. En desktop, foto a un lado y texto al otro, sin parecer un split de template (la foto puede ir al ras del borde).
- Botón **Menú**: hoy no hay archivo de carta. El botón no debe fingir que Instagram es la carta. Baja a esta sección, y acá el estado es honesto: “La carta digital la publicamos acá. Mientras tanto, está en el local.” Link de texto a Instagram, no botón primario.
- Cuando exista el PDF o la URL, el botón Menú del hero y el de esta sección abren eso.

### 5. Google

Trabajo: prueba, no un widget de testimonios.

- Una línea grande: **4,9** en Google · **281** reseñas.
- Link: **Ver en Google Maps**.
- Sin quotes. Sin slider. Sin “VoC”, “prensa”, “posicionamiento”.
- Si más adelante hay 2–3 textos reales copiados de Maps, se agregan como frases sueltas, sin card, sin estrellas decorativas por cita, sin flechas.

### 6. Cómo llegar

Trabajo: ir o llamar.

- Dirección en titular: **Av. Fontana 769, Esquel**
- Horario repetido en una línea.
- Mapa embebido.
- Un solo botón fill: **Cómo llegar** (abre Maps).
- Teléfono como link de texto: **2945 41-3194**. No compite como segundo botón primario.

### 7. Footer

Fondo cacao. Logo, dirección, horario, Instagram, teléfono, Maps. Sin repetir los CTAs grandes.

## Copy

Voz corta, de local. Una idea por bloque.

Permitido, porque está confirmado:

- Mesal Café, Esquel, Av. Fontana 769
- 08:00–00:00, todos los días
- Elaboración propia
- Sin TACC, pet friendly, cowork / lectura
- 4,9 y 281 en Google
- Teléfono 2945 41-3194
- Instagram @mesalcafe

Prohibido en la página:

- “Sabores que acompañan”
- “Siempre es buen momento”
- “Historias reales”
- Pies de prensa o etiquetas de research
- Precios, WhatsApp, reservas, delivery
- Choco Fest como mensaje principal

## Fotos

Cada imagen se usa una sola vez.

| Lugar | Foto |
|---|---|
| Hero | Salón / barra (`maps-01` o equivalente en `public/assets`) |
| El lugar | Otra toma del salón o el letrero, no la del hero |
| Menú | Un plato, no repetido |

Si una foto no muestra lo que dice el bloque, no se usa. La de “noche” actual (mesa de día) no entra.

## Lo que se borra del build actual

- Sección **El día** completa (markup, fotos de esa grilla, copy mañana/mediodía/noche).
- Slider de reseñas y sus tres citas.
- Botón “Ver en Instagram” tratado como menú.
- Cejas en mayúsculas en cada sección.
- Iconos de amenities dentro de cuadrados.
- Nav sin logo.
- Halo circular detrás del logo.

## Hecho cuando

- No existe “El día”.
- Un visitante nuevo entiende en el primer pantallazo: qué es, hasta qué hora, cómo ver la carta y cómo llegar.
- Ningún texto parece de un generador de landings.
- Ninguna foto está repetida.
- El 4,9 se puede verificar en el link de Maps.
- Mobile: hero entero, botones tocables, iconos visibles.
