# Cómo replicar el hero del Inicio en Elementor Pro

Respuesta corta: **no con el widget Slides. Con Nested Tabs.**

En el LEEME anterior había anotado *Slides* para este bloque, y era una simplificación mía que
conviene corregir antes de que te sientes a maquetar. Slides te da la foto a sangre, el overlay
y el texto por diapositiva, pero su navegación son flechas y puntitos, y no se pueden sustituir
por la tira de ocho iconos con etiqueta. Justo esa tira es la firma del hero.

---

## Por qué Nested Tabs

El widget **Nested Tabs** (Elementor 3.10 en adelante) hace nativamente las tres cosas que el
carrusel no puede:

1. **Icono dentro del título de la pestaña.** Cada pestaña acepta un icono SVG más el texto:
   exactamente la tira de ocho.
2. **La lista de pestañas se puede colocar abajo.** El control de dirección permite arriba,
   abajo, izquierda o derecha. Nosotros la queremos abajo, al pie de la foto.
3. **El contenido de cada pestaña es un Container en blanco.** Ahí metes la imagen de fondo,
   el overlay, el titular, el texto y los dos botones, con todos los efectos de movimiento
   que quieras.

Lo único que Nested Tabs **no** trae es el avance automático cada 7 segundos y la barra de
progreso. Eso son unas veinticinco líneas de código que te dejo abajo, listas para pegar.

---

## Estructura a construir

```
Nested Tabs                     ← clase CSS: anmix-hero
│  Dirección de pestañas: Abajo
│  Alineación: Justificado
│  Alto mínimo: 96vh
│
├─ Pestaña 1 · Limpieza         ← clase CSS: sv-limpieza
│   └─ Container                ← imagen de fondo: heros/limpieza.jpg · Cover · Center
│       ├─ Heading  "Servicios de limpieza industrial y comercial."
│       ├─ Text     "Mantenemos sus instalaciones impecables…"
│       └─ Container horizontal
│           ├─ Button  "Solicite su cotización"  → /contacto
│           └─ Button  "Conozca el servicio"     → /servicios/limpieza
│
├─ Pestaña 2 · Jardinería       ← clase CSS: sv-jardineria
│   └─ … lo mismo
└─ … hasta ocho
```

Al icono de cada pestaña le subes el SVG correspondiente de `assets/img/iconos/`. Recuerda
habilitar antes **Ajustes → Avanzado → Cargar archivos SVG**.

---

## Lo que sí es nativo

| Efecto del prototipo | Dónde se activa en Elementor |
|---|---|
| Foto a sangre | Container de la pestaña → Estilo → Fondo → Imagen · Cover · Center |
| Parallax de la foto | Container → Avanzado → **Efectos de movimiento** → Efectos de desplazamiento → **Desplazamiento vertical**, velocidad 1–2, dirección arriba |
| Zoom ligado al scroll | En el mismo panel → **Escala**, de 100 a 106 |
| El texto sube y se desvanece | Container interior del texto → Efectos de movimiento → **Desplazamiento vertical** + **Transparencia** (Fade Out) |
| Pestaña activa con el color del servicio | Estilo → Pestañas → estado Activo, o el CSS de abajo si quieres un color distinto por servicio |
| Botones con forma Material 3 | Estilo → Botón → Radio del borde 999 px |

El overlay del prototipo son tres degradados superpuestos, y el control de Fondo → Superposición
de Elementor sólo admite uno. Se resuelve con el CSS del siguiente apartado; es una línea.

---

## CSS a pegar

Va en **Ajustes del sitio → CSS personalizado** (Elementor Pro), o en el panel Avanzado →
CSS personalizado del propio widget.

```css
/* ---- color de acento por servicio ---- */
.anmix-hero .sv-limpieza      { --sv:#70B540 }
.anmix-hero .sv-jardineria    { --sv:#049F8D }
.anmix-hero .sv-arquitectura  { --sv:#FC7E2F }
.anmix-hero .sv-especiales    { --sv:#FDC525 }
.anmix-hero .sv-software      { --sv:#0696BC }
.anmix-hero .sv-seguridad     { --sv:#A6A6A6 }
.anmix-hero .sv-detailing     { --sv:#DC242B }
.anmix-hero .sv-suministros   { --sv:#8551DF }

/* ---- velo de tres capas sobre la foto ---- */
.anmix-hero .e-con.e-child > .elementor-background-overlay,
.anmix-hero [role="tabpanel"] > .e-con::before{
  content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(180deg,rgba(0,0,0,.78) 0%,rgba(0,0,0,.34) 28%,rgba(0,0,0,.56) 62%,rgba(0,0,0,.92) 100%),
    linear-gradient(100deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.22) 55%,transparent 100%),
    radial-gradient(120% 80% at 12% 88%,rgba(112,181,64,.18) 0%,transparent 62%);
}

/* ---- tira de pestañas ---- */
.anmix-hero [role="tab"]{
  position:relative;border:0;background:none;
  border-top:2px solid transparent;
  color:rgba(255,255,255,.62);
  transition:color .3s cubic-bezier(.2,0,0,1), background .3s cubic-bezier(.2,0,0,1);
}
.anmix-hero [role="tab"]:hover{ color:#fff; background:rgba(255,255,255,.04) }
.anmix-hero [role="tab"][aria-selected="true"]{
  color:#fff; background:rgba(255,255,255,.04); border-top-color:var(--sv);
}
.anmix-hero [role="tab"][aria-selected="true"] svg{ color:var(--sv); fill:var(--sv) }

/* ---- barra de progreso de los 7 s ---- */
.anmix-hero [role="tab"][aria-selected="true"]::after{
  content:'';position:absolute;top:-2px;left:0;height:2px;
  background:rgba(255,255,255,.85);
  animation:anmixBar 7s linear forwards;
}
@keyframes anmixBar{ from{width:0} to{width:100%} }
.anmix-hero:hover [role="tab"][aria-selected="true"]::after{ animation-play-state:paused }

@media (prefers-reduced-motion:reduce){
  .anmix-hero [role="tab"][aria-selected="true"]::after{ animation:none;width:100% }
}
```

La barra de progreso se reinicia sola: al cambiar `aria-selected`, el pseudo-elemento se crea de
nuevo y la animación arranca desde cero. No hace falta tocarla desde JavaScript.

---

## JavaScript del avance automático

Va en **Elementor → Código personalizado** (Elementor Pro), ubicación **Body – End**, con la
condición de visualización puesta en la página de inicio.

```html
<script>
document.addEventListener('DOMContentLoaded', function () {
  var wrap = document.querySelector('.anmix-hero');
  if (!wrap) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // Elementor ha cambiado los nombres de clase entre versiones,
  // por eso se busca por rol ARIA y sólo se recurre a la clase como respaldo.
  var tabs = wrap.querySelectorAll('[role="tab"]');
  if (!tabs.length) tabs = wrap.querySelectorAll('.e-n-tab-title');
  if (tabs.length < 2) return;

  var DUR = 7000, i = 0, timer = null;

  function current() {
    for (var n = 0; n < tabs.length; n++) {
      if (tabs[n].getAttribute('aria-selected') === 'true') return n;
    }
    return 0;
  }
  function next() { i = (current() + 1) % tabs.length; tabs[i].click(); }
  function play() { stop(); timer = setInterval(next, DUR); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }

  wrap.addEventListener('mouseenter', stop);
  wrap.addEventListener('mouseleave', play);
  tabs.forEach(function (t) { t.addEventListener('click', play); });   // reinicia el conteo al elegir a mano

  play();
});
</script>
```

Si algún día Elementor cambia el marcado y el avance deja de funcionar, lo único que hay que
revisar es la línea de `querySelectorAll`.

---

## Si prefieres cero código

Dos caminos, ambos con concesiones:

- **Widget Slides tal cual.** Renuncias a la tira de iconos y te quedas con puntos o flechas.
  Se maqueta en veinte minutos y no requiere mantenimiento. El hero pierde su rasgo distintivo.
- **Un addon de terceros.** Unlimited Elements o Essential Addons traen carruseles con
  miniaturas y pestañas con autoplay. Resuelve el problema, pero suma un plugin más al sitio
  y una dependencia que hay que actualizar. Para veinticinco líneas de JavaScript propio, no
  me parece un cambio ventajoso.

Mi recomendación es Nested Tabs con el snippet. Es el único camino que reproduce el prototipo
tal cual, y todo lo pesado —el parallax, el zoom, el desvanecido del texto, el diseño de cada
pestaña— lo sigue manejando Elementor de forma nativa y editable.

---

## Antes de empezar a maquetar

Sin esto, cualquier bloque que armes va a llevar estilos escritos a mano:

1. **Ajustes del sitio → Colores globales**: cargar negro, blanco, los tres verdes y los ocho
   colores de servicio.
2. **Ajustes del sitio → Fuentes globales**: Lato y Montserrat con la escala del sistema de diseño.
3. **Ajustes → Avanzado → Cargar archivos SVG**: activar, para poder subir los ocho iconos.
4. **Experimentos → Nested Elements**: comprobar que está activo, o el widget no aparece.
