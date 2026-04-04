# 📋 Documentación técnica - Landing Page Smart Dog

## 📌 Resumen rápido

Este documento te guía para editar cada sección de `Index.html` sin necesidad de conocimientos avanzados de HTML/CSS. Todas las variables clave están claramente marcadas con comentarios.

---

## 🔧 GUÍA RÁPIDA DE CAMBIOS COMUNES

### 1️⃣ Cambiar Email del Formulario
**Ubicación:** Busca `.co/[TU_CORREO@AQUI.COM]` en el archivo `Index.html`

**Línea aproximada:** ~780 (en la sección FORMULARIO)

**Qué cambiar:**
```html
<!-- ANTES -->
<form action="https://formsubmit.co/[TU_CORREO@AQUI.COM]" method="POST">

<!-- DESPUÉS -->
<form action="https://formsubmit.co/tu_email@ejemplo.com" method="POST">
```

⚠️ **IMPORTANTE:** Reemplaza `[TU_CORREO@AQUI.COM]` con tu email real (ej: franquicias@smartdog.com.br)

---

### 2️⃣ Agregar Logo Real
**Ubicación:** Busca todas las instancias de `logo.png`

**Líneas aproximadas:** 96, 206, 780+

**Qué cambiar:**
```html
<!-- ANTES -->
<img src="logo.png" alt="Smart Dog Logo">

<!-- DESPUÉS (opción 1: archivo local) -->
<img src="mi-logo-real.png" alt="Smart Dog Logo">

<!-- DESPUÉS (opción 2: URL online) -->
<img src="https://ejemplo.com/logo.png" alt="Smart Dog Logo">
```

📝 **Tipos de archivos soportados:** PNG, JPG, WEB, SVG

---

### 3️⃣ Agregar Favicon Real
**Ubicación:** Busca `favicon.png` al inicio del archivo (en `<head>`)

**Líneas aproximadas:** 31-32

**Qué cambiar:**
```html
<!-- BEFORE -->
<link rel="icon" type="image/png" href="favicon.png" sizes="32x32">

<!-- AFTER -->
<link rel="icon" type="image/png" href="mi-favicon-real.png" sizes="32x32">
```

💡 **Tamaño recomendado para favicon:** 32x32 píxeles (PNG o ICO)

---

### 4️⃣ Cambiar Colores
**Colores principales del tema:**

| Elemento | Color Hex | Dónde está |
|----------|-----------|-----------|
| **Primario** (amarillo) | `#F9B233` | Botones, títulos destacados, bordes |
| **Acento** (rojo) | `#E33E1B` | Botones secundarios, acentos |
| **Fondo** (oscuro) | `#1A1A1A` | Fondos de secciones |

**Cómo cambiar:**

Busca en el archivo:
```css
:root {
    --color-primary: #F9B233;      /* ← Cambia aquí */
    --color-accent: #E33E1B;       /* ← Cambia aquí */
    --color-dark: #1A1A1A;         /* ← Cambia aquí */
}
```

O usa Find & Replace (Ctrl+H):
- Busca: `#F9B233`
- Reemplaza con: `#TU_NUEVO_COLOR`

---

## 📄 GUÍA DETALLADA POR SECCIÓN

### SECCIÓN 1: HERO (Sección de impacto principal)

**Ubicación:** Líneas ~200-280

**Textos editables:**
```html
<!-- Línea ~219: Pequeña etiqueta -->
<span>🔥 Oportunidad de Franquicia 2025</span>  <!-- Editar aquí -->

<!-- Línea ~225-228: Título principal -->
<h1>Invista em um <span class="text-primary">clássico popular</span> com o toque <span class="text-accent">Smart</span></h1>

<!-- Línea ~232-237: Subtítulo -->
<p>Um modelo de negócio provado com mais de <span class="text-primary font-semibold">30.000 unidades</span> vendidas...</p>

<!-- Línea ~241-249: Stats (números destacados) -->
<p class="text-3xl font-bold text-primary">30k+</p>  <!-- Cambiar número -->
<p class="text-3xl font-bold text-primary">19-31</p> <!-- Cambiar número -->
<p class="text-3xl font-bold text-primary">500+</p>  <!-- Cambiar número -->
```

**Imagen a cambiar:**
```html
<!-- Línea ~265 -->
<img src="logo.png" alt="Smart Dog Branding">
<!-- Cambiar a tu imagen real de 400x400 px mínimo -->
```

---

### SECCIÓN 1B: GALERÍA / CARRUSEL (imágenes del producto y operación)

**Ubicación:** Entre la sección `#hero` y la sección `#mercado`

**ID de sección:** `#galeria`

---

#### Cómo reemplazar una imagen placeholder

Cada slide tiene una imagen con `src="https://placehold.co/..."`. Para reemplazar por una foto real:

1. Guarda tu foto en la **misma carpeta** que `index.html`
2. Busca el comentario del slide que quieres cambiar (ej. `SLIDE 1`)
3. Reemplaza el `src`:

```html
<!-- ANTES (placeholder) -->
<img src="https://placehold.co/1200x600/1A1A1A/F9B233?text=Foto+1+—+Produto+Principal" ...>

<!-- DESPUÉS (foto real) -->
<img src="foto-hotdog-principal.jpg" ...>
```

**Tamaño recomendado:** 1200×600px (horizontal). Formatos: JPG, PNG, WEBP.

---

#### Imágenes sugeridas por slide

| Slide | Archivo sugerido | Contenido ideal |
|-------|-----------------|-----------------|
| Slide 1 | `foto-produto.jpg` | Hot dog estrella / producto principal |
| Slide 2 | `foto-ponto-venda.jpg` | Área de trabajo / punto de venta |
| Slide 3 | `foto-atendimento.jpg` | Atención al cliente / ambiente |
| Slide 4 | `foto-equipe.jpg` | Equipo / operación interna |

---

#### Cambiar el texto del pie de cada slide

Cada slide tiene un bloque con título y descripción:

```html
<p class="text-white font-bold text-lg">Nosso Produto Estrela</p>       <!-- título -->
<p class="text-gray-300 text-sm">Hot dog gourmet com molhos exclusivos</p> <!-- subtítulo -->
```

Edita esos dos textos para cada slide.

---

#### Agregar o quitar slides

**Para agregar:** Copia un bloque `<div class="carousel-slide">` completo y pégalo antes del cierre `</div><!-- fin carousel-track -->`. El JS detecta los slides y los puntos automáticamente.

**Para quitar:** Elimina el bloque `<div class="carousel-slide">` completo del slide que no quieras.

---

#### Cambiar el tiempo de autoplay

Por defecto el carrusel avanza cada **4 segundos**. Para cambiarlo, busca en el bloque `<script>`:

```js
autoplayTimer = setInterval(() => goTo(current + 1), 4000); // ← cambia 4000 (ms)
```

---

### SECCIÓN 2: DIFERENCIALES (3 cards con ventajas)

**Ubicación:** Líneas ~300-390

**Estructura de cada card:**
```html
<div class="card-hover bg-gray-900 border border-gray-800 p-8 rounded-xl">
    <div class="text-5xl mb-4">🍽️</div>              <!-- Cambiar emoji -->
    <h3 class="text-2xl font-bold mb-3 text-primary">Receitas Gourmet Exclusivas</h3>  <!-- Cambiar título -->
    <p class="text-gray-400 leading-relaxed">
        Fórmulas probadas...  <!-- Cambiar descripción -->
    </p>
</div>
```

**3 Diferenciales principales:**
1. **Recetas Gourmet** (~línea 320)
2. **Operación Simplificada** (~línea 340)
3. **Alta Rentabilidad** (~línea 360)

📝 Para agregar más diferenciales: Duplica un `<div class="card-hover"...>` completo

---

### SECCIÓN 3: TABLA DE INVERSIONES (3 modalidades)

**Ubicación:** Líneas ~430-680

**Estructura de cada tarjeta:**

```html
<!-- MODALIDAD NANO -->
<div class="card-hover bg-gray-900...">
    <h3 class="text-2xl font-bold text-primary">Modalidad NANO</h3>
    <!-- Inversión inicial (línea ~456) -->
    <p class="text-3xl font-bold text-primary">~$157k</p>
    <!-- Retorno (línea ~463) -->
    <p class="text-2xl font-bold text-accent">27 meses</p>
    <!-- Características (línea ~469+) -->
    <li>Punto de venta compacto</li>
    
<!-- Repite para SMART (~línea 490) y DRIVE (~línea 590) -->
```

**Valores fáciles de cambiar:**
- Inversión NANO: `$157k` (~línea 456)
- Inversión SMART: `$229k` (~línea 520)
- Inversión DRIVE: `$291k` (~línea 600)
- Retorno NANO: `27 meses` (~línea 463)
- Retorno SMART: `19 meses` (~línea 530)
- Retorno DRIVE: `31 meses` (~línea 607)

📊 **Cambiar características:** Edita los `<li>` dentro de cada modalidad

---

### SECCIÓN 4: PROCESO (Timeline de 6 pasos)

**Ubicación:** Líneas ~720-870

**Estructura de cada paso:**

```html
<div class="animate-fadeInUp delay-100">
    <div class="w-16 h-16 bg-primary text-dark rounded-full flex items-center justify-center font-bold text-2xl mb-4 border-4 border-dark">
        1️⃣  <!-- Cambiar número/emoji -->
    </div>
    <div class="bg-gray-900 border border-gray-800 rounded-lg p-6 text-center w-full">
        <h3 class="font-bold text-lg text-primary">Conexión</h3>  <!-- Cambiar título -->
        <p class="text-gray-400 text-sm leading-relaxed">
            Primer contacto y conocimiento mutuo... <!-- Cambiar descripción -->
        </p>
    </div>
</div>
```

**Los 6 pasos están en líneas:**
1. Paso 1 "Conexión" (~línea 750)
2. Paso 2 "Evaluación" (~línea 770)
3. Paso 3 "Presentación" (~línea 790)
4. Paso 4 "Formalización" (~línea 810)
5. Paso 5 "Estructuración" (~línea 830)
6. Paso 6 "Inauguración" (~línea 850)

---

### SECCIÓN 5: FORMULARIO (Captura de leads)

**Ubicación:** Líneas ~880-1000

**campos disponibles:**

```html
<!-- Nombre -->
<input type="text" name="nombre" placeholder="Tu nombre aquí" required>

<!-- Email -->
<input type="email" name="email" placeholder="tu@email.com" required>

<!-- Teléfono -->
<input type="tel" name="telefono" placeholder="(11) 9999-9999" required>

<!-- Ciudad -->
<input type="text" name="ciudad" placeholder="Ej: São Paulo, Rio de Janeiro" required>

<!-- Modalidad (selector) -->
<select name="modalidad" required>
    <option value="NANO">NANO (~$157k, 27 meses ROI)</option>
    <option value="SMART">SMART (~$229k, 19 meses ROI)</option>
    <option value="DRIVE">DRIVE (~$291k, 31 meses ROI)</option>
</select>

<!-- Mensaje adicional -->
<textarea name="mensaje" placeholder="Cuéntanos..."></textarea>
```

**Agregar más campos:**
```html
<div>
    <label for="tu-campo">Tu Label</label>
    <input type="text" id="tu-campo" name="tu-campo" required>
</div>
```

**Configuración FormSubmit:**
```html
<form action="https://formsubmit.co/[TU_CORREO@AQUI.COM]" method="POST">
    <!-- Aquí van los campos -->
    <input type="hidden" name="_subject" value="Nueva Solicitud de Franquicia Smart Dog">
    <input type="hidden" name="_captcha" value="false">
</form>
```

---

### SECCIÓN 6: FOOTER (Pie de página)

**Ubicación:** Líneas ~1020-1100

**Enlaces y contacto editables:**

```html
<!-- Columna 1: Sobre Smart Dog (línea ~1040) -->
<p>Franquiciadora de hot dogs gourmet...</p>  <!-- Cambiar descripción -->

<!-- Columna 2: Enlaces rápidos (línea ~1055+) -->
<a href="#hero">Inicio</a>
<a href="#diferenciales">Diferenciales</a>
<!-- Agregar/cambiar links aquí -->

<!-- Columna 3: Legal (línea ~1065+) -->
<a href="#">Términos y Condiciones</a>
<!-- Cambiar URLs a tus páginas reales -->

<!-- Columna 4: Contacto (línea ~1080+) -->
<a href="mailto:contato@smartdog.com.br">Email</a>
<a href="tel:+551130000000">Teléfono</a>
<!-- Cambiar email y teléfono -->

<!-- Copyright (línea ~1100) -->
<p>© 2025 Smart Dog. Todos los derechos reservados.</p>
<!-- Cambiar año y nombre de empresa -->

<!-- Redes sociales (línea ~1105+) -->
<a href="https://www.facebook.com/smartdog">f</a>
<a href="https://www.instagram.com/smartdog">📷</a>
<!-- Cambiar URLs de redes sociales -->
```

---

## 🎨 PERSONALIZACIÓN AVANZADA

### Cambiar Fuente
**Ubicación:** Línea ~28 (en `<head>`)

```html
<!-- ANTES: Poppins -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<!-- DESPUÉS: Otra fuente (ej: Roboto) -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

También actualiza la fuente en CSS:
```css
* {
    font-family: 'Roboto', sans-serif;  /* Cambiar aquí */
}
```

### Cambiar Espacios (Padding/Margin)
**Ejemplo - Aumentar espacio en hero:**
```html
<!-- ANTES -->
<section id="hero" class="pt-32 pb-16 sm:pt-40 sm:pb-20">

<!-- DESPUÉS (más grande) -->
<section id="hero" class="pt-40 pb-24 sm:pt-48 sm:pb-32">
```

**Valores Tailwind comunes:**
- `pt-` = padding top
- `pb-` = padding bottom
- `px-` = padding horizontal
- `py-` = padding vertical
- Números: 4, 8, 12, 16, 20, 24, 32, etc.

### Agregar Animaciones Personalizadas
**Ubicación:** Línea ~85 (en `<style>`)

```css
/* Agregar nueva animación */
@keyframes tuAnimacion {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.animate-tuAnimacion {
    animation: tuAnimacion 0.8s ease-out forwards;
}
```

---

## ✅ CHECKLIST DE EDICIÓN

Antes de publicar, verifica:

- [ ] Email del formulario reemplazado con tu correo real
- [ ] Logo real agregado (reemplazar `logo.png`)
- [ ] Favicon real agregado (reemplazar `favicon.png`)
- [ ] Todos los textos traduccidos / editados a português Brasil
- [ ] Números de inversión actualizados (~líneas 456, 520, 600)
- [ ] Tiempos de ROI actualizados (~líneas 463, 530, 607)
- [ ] Contacto en footer actualizado (~líneas 1080)
- [ ] URLs de redes sociales correctas (~líneas 1105+)
- [ ] Campos del formulario revisados
- [ ] Colores personalizados si deseas (si no, usa los actuales)

---

## 🚀 TESTING RÁPIDO

### Test Local (sin subir a internet)
1. Guarda el archivo `Index.html`
2. Abre el archivo en un navegador web (doble clic)
3. Verifica que todo se vea bien
4. Completa el formulario y presiona "Enviar"
5. Confirma que recibiste el email

### Test Responsive (mobile/tablet)
1. En navegador, presiona `F12` (DevTools)
2. Presiona `Ctrl+Shift+M` (device toggle)
3. Simula iPhone 12, iPad, Desktop
4. Verifica que todo se vea bien en cada tamaño

### Test de Velocidad
1. Abre DevTools (`F12`)
2. Ve a la pestaña "Lighthouse"
3. Click "Analyze page load"
4. Objetivo: Score >80 en Performance

---

## 📞 SOPORTE & PREGUNTAS RESPONDIDAS

### "¿Cómo agregar más imágenes?"

Edita la sección de HERO o agrega nueva:

```html
<img src="tu-imagen.png" alt="Descripción" class="w-full h-auto rounded-xl">
```

### "¿Cambiar tamaño de botones?"

```html
<!-- ANTES (normal) -->
<button class="btn-primary text-white px-8 py-3 rounded-lg">Botón</button>

<!-- DESPUÉS (más grande) -->
<button class="btn-primary text-white px-12 py-4 rounded-lg text-lg">Botón</button>

<!-- DESPUÉS (más pequeño) -->
<button class="btn-primary text-white px-4 py-2 rounded-lg text-sm">Botón</button>
```

### "¿Agregar secciones nuevas?"

Copia una sección existente y modifica:
1. El `id` de la sección
2. El título (`<h2>`)
3. El contenido interno
4. Agrega un link en la navegación

### "¿El formulario no envía emails?"

1. Verifica que hayas reemplazado `[TU_CORREO@AQUI.COM]` con tu email real
2. Revisa la carpeta de spam/promociones
3. Abre la página en navegador (no local), luego prueba

---

## 📚 REFERENCIAS RÁPIDAS

### Clases Tailwind útiles

| Clase | Efecto |
|-------|---------|
| `bg-dark` | Fondo oscuro (#1A1A1A) |
| `text-primary` | Texto amarillo (#F9B233) |
| `text-accent` | Texto rojo (#E33E1B) |
| `rounded-xl` | Bordes redondeados |
| `shadow-lg` | Sombra |
| `hover:text-primary` | Efecto al pasar mouse |
| `transition` | Animación suave |
| `grid md:grid-cols-3` | 3 columnas en desktop, 1 en mobile |

### Estructura HTML

```html
<!-- Sección base -->
<section id="nombre" class="py-16 sm:py-20 bg-dark">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Contenido -->
    </div>
</section>
```

---

**Última actualización:** 4 de abril, 2025  
**Versión:** 1.0  
**Soporte:** Consulta los comentarios del HTML para más detalles específicos

---

## Missão, Visão e Valores (Placeholder comentado no HTML)

Esta seção existe no `index.html` como um bloco comentado entre as seções "Diferenciais" e "Inversiones". Para ativá-la, remova os delimitadores `<!--` e `-->` ao redor do bloco `<section id="missao-visao-valores">`.

### Conteúdo extraído do PDF da franquia

**Missão**
> Oferecer alimentos de qualidade com rapidez e cuidado, criando uma experiência acessível ao consumidor e oportunidades sustentáveis para empreendedores.

**Visão**
> Ser referência nacional em franquias de hot dogs, reconhecida pela simplicidade do modelo, excelência operacional e forte conexão com o consumidor.

**Valores**
- Compromisso com a qualidade
- Respeito (franqueados, clientes, fornecedores, equipe)
- Clareza e transparência
- Simplicidade e eficiência
- Espírito colaborativo
- Resiliência

### Como ativar a seção

Busca no `index.html` o comentário `SEÇÃO MISSÃO / VISÃO / VALORES` e remove os dois delimitadores de comentário HTML (`<!--` e `-->`) que envolvem o bloco `<section>`.
