# Prototipo ANMIX — sitio completo

12 páginas: Home, Nosotros, Servicios, Contacto y una página por cada uno de los 8 servicios.

Ábrelo con doble clic en `index.html`. No necesita servidor.
Requiere conexión a internet la primera vez para cargar Lato y Montserrat desde Google Fonts
(son las dos tipografías que ya usa anmix.mx).

```
prototipo/
├── index.html                            ← Home
├── nosotros.html
├── servicios.html                        ← índice de los 8
├── contacto.html
├── servicio-limpieza.html                ┐
├── servicio-jardineria.html              │
├── servicio-arquitectura.html            │
├── servicio-servicios-especiales.html    ├ una por servicio,
├── servicio-software-gestion-residencial.html   │ generadas de la misma
├── servicio-seguridad-privada.html       │ plantilla
├── servicio-detailing-automotriz.html    │
├── servicio-suministros-corporativos.html┘
├── LEEME.md                              ← este archivo
├── GUIA-hero-elementor.md                ← cómo rehacer el hero en Elementor Pro
└── assets/
    ├── css/anmix.css          ← hoja compartida por las 12 páginas
    ├── js/anmix.js            ← carrusel, parallax, contadores, menú
    └── img/
        ├── heros/             ← 8 fondos del hero (1800 px, optimizados)
        ├── logos/             ← logotipos ANMIX por servicio
        ├── clientes/          ← 19 logos de clientes
        ├── industrias/        ← fotos de las industrias de cobertura
        ├── iconos/            ← los 8 SVG, listos para subir a WordPress
        ├── proceso.jpg · nosotros-hero.jpg · contacto-hero.jpg · altura.jpg
        └── (build_pages.py, en la raíz del proyecto, regenera las 11 páginas interiores)
```

---

## Qué quedó construido en el Home

| Sección | Comportamiento | Widget de Elementor Pro al migrar |
|---|---|---|
| Barra superior | Teléfono, correo, ubicación y Sign in. **Se pliega al hacer scroll** y deja sólo la navegación | Header · container superior con efecto de desplazamiento |
| Encabezado | Fijo y transparente sobre el hero; se vuelve negro y se compacta de 112 a 76 px al hacer scroll. Al estar fuera del flujo, el contenido no da ningún salto al plegarse | Theme Builder · Header + efectos de desplazamiento |
| Hero | Carrusel de 8 servicios con avance automático de 7 s, barra de progreso, y cambio de título, texto, color de acento y enlace. Se pausa al pasar el cursor | **Nested Tabs** con las pestañas abajo, no Slides. Ver `GUIA-hero-elementor.md` |
| Heros de servicio | Foto a sangre con velo y parallax, titular, promesa y un solo botón. El color del servicio vive en el submenú, los iconos y las tarjetas, no en un logotipo repetido | Container + **Heading** |
| Tira de servicios | Los 8 iconos SVG al pie del hero; el activo toma el color de su servicio | Son los títulos del mismo **Nested Tabs**, con icono y etiqueta |
| Submenú de Servicios | Panel Material 3 de dos columnas con icono, nombre y descriptor de cada servicio, más un enlace a la vista completa. Se abre al pasar el cursor y con teclado (`:focus-within`) | **Nav Menu** con Mega Menu, plantilla de contenido guardada |
| Clientes | Marquesina infinita sin encabezado: sólo los 19 logos, en escala de grises y a color al pasar el cursor | **Media Carousel** |
| Industrias de cobertura | 8 tarjetas en ventana de 5; la central se abre en blanco. Fondo con parallax | **Loop Carousel** + CPT “Industrias” |
| Nuestro proceso | Dos columnas, foto con parallax, lista de 5 atributos | Container 2 col + **Icon List** |
| Cifras | Contadores animados al entrar en pantalla | **Counter** (24/7 y REPSE con Heading) |
| Servicios | Rejilla de 8 tarjetas Material 3 negras con el trébol ANMIX en contenedor tonal | **Loop Grid** + CPT “Servicios” |
| Banda parallax | Frase de cierre del portafolio sobre foto | Container con efectos de movimiento |
| Cotización | Formulario de 6 campos + datos de contacto | **Form** |
| Mapa | Google Maps en monocromo | **Google Maps** |
| Footer | 4 columnas, redes, REPSE, aviso | Theme Builder · Footer |
| WhatsApp | Aparece al pasar el hero | **Floating Buttons** |

**Parallax:** el hero, las industrias, la foto del proceso y la banda de cierre se mueven a
distinta velocidad que el scroll. El desplazamiento está acotado al sobrante de cada imagen,
así que nunca aparecen franjas vacías. Todo se desactiva si el sistema del usuario tiene
activado “reducir movimiento”.

**Overlays:** ninguna foto lleva texto encima sin velo. El hero usa tres capas superpuestas
—degradado vertical, degradado lateral y un halo verde muy tenue— para garantizar contraste
sin apagar la fotografía.

---

## Material 3 · sólo en lo que se toca

MD3 entra donde el usuario interactúa; el resto del sitio conserva el ángulo recto editorial.
El contraste es deliberado: lo que se lee es plano y cuadrado, lo que se toca tiene radio,
elevación y respuesta táctil.

| Elemento | Tratamiento |
|---|---|
| Tarjetas de servicio | *Filled card* negra de radio 16, texto blanco y sin filete superior. State layer del color del servicio al 10 % en hover, elevación 1 → 4 y desplazamiento de 6 px |
| Contenedor del trébol | Superficie tonal al 20 % del color del servicio sobre negro; en hover sube a 32 % y el radio pasa de 16 a 28 px |
| Campos del formulario | *Outlined text field* con etiqueta flotante que se recorta sobre el borde, radio 4, borde de 2 px al enfocar y placeholder que sólo aparece con el foco |
| Casilla de verificación | Radio de state layer de 40 px, palomita que entra con curva *emphasized decelerate* |
| Botones | Radio completo, state layer, elevación 1 → 3, hundimiento al 97,6 % al presionar |
| Chips, pilares, tarjetas de contacto y de otros servicios | Radio 8–16, elevación al pasar el cursor |
| Ripple | Se dispara en `pointerdown` sobre cualquier superficie interactiva, con el color del elemento |

**Curvas de movimiento** (las oficiales de MD3):
`emphasized` `cubic-bezier(.2,0,0,1)` · `decelerate` `cubic-bezier(.05,.7,.1,1)` ·
`accelerate` `cubic-bezier(.3,0,.8,.15)`. Duraciones de 200, 350, 500 y 700 ms.

**Animaciones nuevas**

- Revelado al entrar en pantalla con opacidad, desplazamiento y una escala de 0,988 a 1.
- Escalonado automático en rejillas: `anmix.js` asigna un `--i` a cada hijo y el retardo sale de ahí (55 ms por posición). Basta con poner la clase `stagger` en el contenedor.
- Profundidad en el hero: el texto sube más rápido que la foto y se desvanece al hacer scroll.
- Parallax con escala: las fotos de fondo hacen un zoom de 5–6 % ligado al scroll, además del desplazamiento vertical.

Todo respeta `prefers-reduced-motion`: con esa preferencia activada no hay parallax, ni ripple,
ni revelados.

---

## El copy, revisado

Lo que sonaba repetitivo tenía tres causas concretas, ya corregidas:

**1. Cinco maneras de decir lo mismo.** Había "Cotizar sin costo", "Solicita tu visita sin
costo", "Solicita tu cotización", "Trabajemos juntos" y "Ver el servicio" conviviendo. Ahora
el vocabulario de acción es uno solo:

| Intención | Texto | Dónde |
|---|---|---|
| Acción principal | **Solicite su cotización** | Encabezado, hero, menú móvil |
| Cierre de página | **Agende una visita** | Banda final |
| Envío | **Enviar solicitud** | Botón del formulario |
| Navegación | **Ver servicio** / **Conozca el servicio** | Tarjetas y hero |

**2. "Sin costo" aparecía cinco veces por página.** Repetir que algo es gratis abarata una
marca premium. Ahora se dice **una sola vez**, junto al formulario, y nunca dentro de un botón.

**3. El mismo párrafo de cierre en doce páginas.** La banda final repetía palabra por palabra
"Un asesor visita tus instalaciones…", que además ya estaba en la sección de contacto. Se
eliminó el párrafo y cada página cierra con una frase propia:

- Home — *Nosotros hacemos el trabajo sucio. Usted, lo suyo.*
- Nosotros — *Veintiocho años se dicen rápido. Se demuestran cada turno.*
- Servicios — *Ocho servicios, un contrato, un solo interlocutor.*
- Limpieza — *Su operación no debería detenerse para limpiar.*
- Jardinería — *El primer contacto con su empresa es la entrada.*
- Arquitectura — *El espacio que ya tiene puede funcionar mejor.*
- Servicios especiales — *Lo que está alto también se ensucia.*
- Software residencial — *La administración de su condominio cabe en una pantalla.*
- Seguridad privada — *Tranquilidad es saber que alguien está mirando.*
- Detailing — *Su auto merece algo más que una lavada.*
- Suministros — *Nunca más un sanitario sin papel.*

**Otros cambios**

- Las ocho descripciones de las tarjetas estaban todas construidas igual: lista de tareas con
  coma y frase de cierre. Ahora cada una tiene su propia forma —contraste, condición,
  consecuencia, promesa— y ninguna empieza como la anterior.
- El bloque de las once cláusulas del contrato se repetía completo en nueve páginas. Ahora va
  completo sólo en `servicios.html`, y las páginas de servicio llevan una versión de seis puntos
  con enlace a la lista larga.
- Las industrias de cobertura empezaban cuatro de ellas con "Limpieza de…". Reescritas.
- **El sitio mezclaba tú y usted** (el portafolio también lo hace). Todo quedó en **usted**,
  incluidos los botones. Cambió una palabra en dos titulares del portafolio: *"Todo lo que
  **su** empresa necesita"* y *"Abastecemos **su** operación"*.
- Se retiraron los comodines: "excelencia", "los más altos estándares" y "soluciones integrales"
  ya no aparecen en texto propio, sólo donde son cita literal del cliente (misión y visión).

---

## Logotipos ANMIX por servicio

En `Logos ANMIX_clientes` venían mezclados los logos de clientes y los de ANMIX. Ya están
separados y clasificados:

- `lock-{servicio}-claro.png` — logotipo horizontal con la palabra *anmix* en blanco. **Para fondo oscuro.** El prototipo sólo usa la versión verde, en el encabezado, el menú móvil y el footer.
- `lock-{servicio}-oscuro.png` — la misma versión con la palabra en negro. **Para fondo claro.** Encabeza el bloque del servicio en su página, en el lugar donde antes iba el antetítulo.
- `iso-{servicio}.png` — sólo el trébol, en el color del servicio. Se usa en las tarjetas.

⚠️ **Falta el juego de Suministros corporativos.** No existe ningún archivo en morado.
`lock-suministros-oscuro.png` e `iso-suministros.png` los compuse recoloreando el trébol del
lockup verde real, así que la geometría y las proporciones son idénticas a las de los otros
siete; sólo el color es invención. **Hay que pedirle el original al cliente.**

---

## Imágenes que son marcador de posición

Las fotos de industrias de **Oficinas corporativas** y **Hospitales y clínicas** son las
reales: las extraje del PDF `Ideas de visualización`. Las otras seis (hangares, escuelas,
naves industriales, centros comerciales, condominios y cocinas industriales) son recortes de
las fotos de servicio, puestas para que se entienda el patrón. **Hay que sustituirlas.**

También conviene revisar:

- `heros/arquitectura.jpg` — es un collage de antes y después de una cocina; funciona en un
  carrusel de servicios pero no como imagen de portada de un servicio.
- `heros/software.jpg` — es un mockup de la plataforma sobre fondo claro. En un hero con
  texto blanco pierde fuerza. Valdría la pena una toma del edificio o del residencial.

---

## Pendientes de contenido

Los mismos seis puntos del análisis, ninguno bloquea el prototipo:

1. ¿28, 26 o 25 años? Ahora mismo dice **28**, tomado del portafolio.
2. ¿“Trabajo temporal” se retira del catálogo o entra como noveno servicio?
3. ¿A dónde lleva **Sign in**? Está puesto sin destino.
4. ¿Teléfono principal 722 272 0428 o 722 791 0294? Están los dos: el primero en la barra
   superior y el segundo como WhatsApp.
5. ¿Hay testimonios publicables?
6. ¿Existe el logotipo en SVG?

---

## Las once páginas interiores

Todas comparten `assets/css/anmix.css`, `assets/js/anmix.js` y exactamente el mismo encabezado
que el home. Los ocho servicios viven en el **submenú desplegable de “Servicios”**, no en una
barra fija: el panel muestra icono, nombre y descriptor de cada uno, marca el servicio en el que
estás y cierra con un enlace a la vista completa. En móvil siguen listados en el menú lateral.

### `nosotros.html`
Hero sobre la foto del hangar · quiénes somos (los cuatro párrafos del portafolio, textuales) ·
misión y visión en bloque negro · cifras 28+ / 110 / 95 % / 24-7 / REPSE · las seis razones del
sitio actual reescritas · seis valores con foto de trabajos en altura · bloque de cumplimiento
REPSE con IMSS, SAT, INFONAVIT y FONACOT · clientes · cierre.

### `servicios.html`
Índice de los ocho con la promesa de cada uno · **“Sin letras chiquitas”**, las once cosas que
van incluidas en cualquier contrato (tomadas literalmente de la página 4 del portafolio; es el
argumento comercial más fuerte que tiene ANMIX y no estaba en el sitio) · carrusel de clientes ·
el proceso en cuatro pasos · cierre.

### `servicio-*.html` (ocho)
Misma plantilla, distinto contenido y distinto color de acento:
hero con la foto del servicio · el **logotipo ANMIX de esa división** encabezando el bloque, en lugar del antetítulo · promesa e intro del portafolio ·
sectores donde aplica · pilares del servicio · alcance a dos columnas con foto ·
lo que incluye · los otros siete servicios · cierre.
**Limpieza** incluye además la sección de **código de colores** (sanitarios, oficinas,
almacenes, cocinas, comedores), que en el portafolio ocupa una página entera.

### `contacto.html`
Hero corto · tres tarjetas de contacto · formulario con selector de servicio · mapa · clientes.

Se generan con `build_pages.py` a partir de una sola estructura de datos, así que cambiar el
copy de un servicio es editar un diccionario, no ocho archivos. Ese script no va a WordPress:
es sólo para iterar rápido sobre el prototipo.

---

## Notas de contenido para revisar con el cliente

- En **Detailing automotriz**, el portafolio repite la lista genérica de sectores (oficinas,
  hospitales, escuelas…), que parece un arrastre de plantilla. Puse una lista propia:
  particulares, flotillas, agencias, concesionarias y corporativos.
- El texto de **“Sin letras chiquitas”** afirma que las once cosas van incluidas en el precio.
  Conviene confirmarlo con el cliente antes de publicarlo, porque es una promesa contractual.
- La cifra de **95 % de retención de personal** viene de la página Nosotros del sitio actual.
