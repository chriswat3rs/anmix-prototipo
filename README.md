# ANMIX · Prototipo de rediseño

Prototipo HTML del nuevo sitio de [ANMIX Servicios](https://anmix.mx), previo a su
maquetación en WordPress con Elementor Pro.

**Demo:** https://chriswat3rs.github.io/anmix-prototipo/

> ⚠️ Material en revisión. El contenido, las cifras y parte de la fotografía todavía no
> están aprobados por el cliente. El sitio lleva `noindex` y un `robots.txt` que bloquea
> a los buscadores.

---

## Qué es esto

Doce páginas estáticas —Home, Nosotros, Servicios, Contacto y una por cada uno de los ocho
servicios— construidas para afinar el lenguaje visual antes de tocar WordPress.

Paleta verde, blanco y negro. Tipografías Lato y Montserrat, las mismas que ya carga el sitio
actual. Material 3 aplicado sólo a los elementos interactivos: tarjetas, formulario, botones
y chips; el resto conserva el ángulo recto editorial.

Sin dependencias ni proceso de compilación. Se abre con doble clic en `index.html`.

## Estructura

```
index.html · nosotros.html · servicios.html · contacto.html
servicio-{limpieza, jardineria, arquitectura, servicios-especiales,
          software-gestion-residencial, seguridad-privada,
          detailing-automotriz, suministros-corporativos}.html

assets/css/anmix.css     hoja compartida por las 12 páginas
assets/js/anmix.js       carrusel, parallax, contadores, ripple, menú
assets/img/              heros · logos · clientes · industrias · iconos

build_pages.py           regenera las 11 páginas interiores desde un solo diccionario
LEEME.md                 documentación del sistema, decisiones y pendientes
GUIA-hero-elementor.md   cómo rehacer el hero con Nested Tabs en Elementor Pro
```

## Documentación

- **[LEEME.md](LEEME.md)** — sistema de diseño, animaciones, revisión de copy, imágenes que
  son marcador de posición y las preguntas abiertas con el cliente.
- **[GUIA-hero-elementor.md](GUIA-hero-elementor.md)** — el hero es el bloque menos obvio de
  migrar. Aquí está la estructura, el CSS y el JavaScript listos para pegar.

## Editar el contenido

El copy de los ocho servicios vive en `build_pages.py`, en una sola lista de diccionarios.
Cambiar un texto y correr `python3 build_pages.py` regenera las once páginas interiores.
Ese script es sólo para iterar el prototipo; no forma parte del sitio ni viaja a WordPress.
