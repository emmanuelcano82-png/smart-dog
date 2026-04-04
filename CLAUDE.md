# Smart Dog — CLAUDE.md

## Descripción del Proyecto

**Smart Dog** es una landing page de franquicia de hot dogs gourmet dirigida a emprendedores e inversores brasileños y latinoamericanos. El objetivo es capturar leads de franquiciados y mostrar tres modelos de inversión.

**Repositorio:** `https://github.com/emmanuelcano82-png/smart-dog.git`

**Sitio en producción:** https://emmanuelcano82-png.github.io/smart-dog/

---

## Stack Tecnológico

- **HTML5** — página única, sin proceso de build
- **Tailwind CSS v3** — cargado via CDN (`https://cdn.tailwindcss.com`)
- **Vanilla JS (ES6)** — sin frameworks
- **Google Fonts** — Poppins (pesos 300–800)
- **FormSubmit.co** — backend de formulario de terceros (sin servidor propio)
- **Feather Icons** — librería de íconos (CDN)

Sin `package.json`, sin herramientas de build, sin backend. Se despliega tal cual en GitHub Pages, Netlify o Vercel.

---

## Estructura de Archivos

```
Dog/
├── index.html          # Todo el sitio (1.176 líneas) — editar aquí todo el contenido
├── logo.png            # Logo de la marca
├── favicon.png         # Ícono del navegador
├── smartdog.png        # Imagen del producto (pequeña)
├── smartdog3.png       # Imagen del producto (grande, usada en el hero)
├── DOCUMENTACION.md    # Guía de contenido por sección (en español)
├── extract_pdf.py      # Utilidad Python para OCR del PDF (herramienta de dev, no se despliega)
└── APRESENTAÇAO SMART DOG.pdf  # PDF de presentación de la franquicia
```

---

## Puntos Clave de Personalización

### Colores de Marca (index.html líneas 44–49)
```css
:root {
    --color-primary: #F9B233;  /* Amarillo */
    --color-accent:  #E33E1B;  /* Rojo */
    --color-dark:    #1A1A1A;  /* Fondo oscuro */
    --color-light:   #F5F5F5;  /* Texto claro */
}
```

### Email del Formulario de Contacto (index.html ~línea 252)
```html
<form action="https://formsubmit.co/[TU_CORREO@AQUI.COM]" method="POST">
```
Reemplazar `[TU_CORREO@AQUI.COM]` con el correo real antes de publicar el sitio.

---

## Secciones de la Página (anchor IDs)

| ID               | Contenido                                         |
|------------------|---------------------------------------------------|
| `#hero`          | Propuesta de valor principal + botones CTA        |
| `#diferenciales` | 3 tarjetas con los diferenciadores clave          |
| `#inversiones`   | 3 modelos de franquicia (NANO, SMART, DRIVE)      |
| `#proceso`       | Timeline de 6 pasos de incorporación             |
| `#contato`       | Formulario de captación de leads                  |
| `footer`         | Enlaces, redes sociales, información legal        |

---

## Modelos de Franquicia

| Modelo | Inversión   | Plazo de ROI | Notas                          |
|--------|-------------|--------------|--------------------------------|
| NANO   | ~$157.000   | 27 meses     | Nivel de entrada               |
| SMART  | ~$229.000   | 19 meses     | Destacado (tarjeta resaltada)  |
| DRIVE  | ~$291.000   | 31 meses     | Premium                        |

---

## Comportamientos JavaScript (todos en index.html, bloque `<script>` al final)

- **Menú móvil** — toggle hamburguesa en pantallas pequeñas
- **Animaciones al scroll** — `IntersectionObserver` agrega la clase `.visible` a los elementos `.animate-fadeInUp`
- **Navbar fijo** — agrega fondo al hacer scroll más allá del hero
- **Scroll suave** — navegación por anclas con desplazamiento suave

---

## Clases de Animación

| Clase                    | Efecto                                      |
|--------------------------|---------------------------------------------|
| `animate-fadeInUp`       | Fade + deslizamiento hacia arriba al scroll |
| `card-hover`             | Elevación + sombra al pasar el cursor       |
| `delay-100/200/300/400`  | Retrasos escalonados de entrada             |
| `pulse-glow`             | Brillo pulsante en los botones CTA          |

---

## Notas de Desarrollo

- Sin instalación ni build — abrir `index.html` directamente en el navegador o servir con cualquier servidor de archivos estáticos.
- Todo el contenido está en portugués/español. Mantener ese idioma al editar textos.
- El script `extract_pdf.py` requiere `fitz` (PyMuPDF) y `easyocr` — solo necesario para re-extraer el PDF de presentación, no para el sitio.
- Las imágenes se referencian con rutas locales — mantenerlas en el directorio raíz junto a `index.html`.

---

## Tareas Frecuentes

**Actualizar montos de inversión:** Buscar en `index.html` los valores monetarios (ej. `R$ 157`) y editar directamente.

**Cambiar el email de contacto:** Buscar `formsubmit.co/` en `index.html` y reemplazar el email.

**Agregar una nueva sección:** Copiar un bloque `<section>` existente, actualizar el `id` y agregar el enlace correspondiente en el `<nav>`.

**Desplegar en GitHub Pages:** El sitio ya está publicado en https://emmanuelcano82-png.github.io/smart-dog/ — cualquier push a la rama `main` actualiza el sitio automáticamente.
