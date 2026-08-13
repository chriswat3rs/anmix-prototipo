/* ============================================================
   ANMIX · Prototipo — comportamiento
   Todo lo de aquí tiene equivalente nativo en Elementor Pro:
   · carrusel del hero  → widget Slides
   · header pegajoso    → efectos de desplazamiento del Header
   · contadores         → widget Counter
   · parallax           → efectos de movimiento del Container
   ============================================================ */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. Header pegajoso ---------- */
  var hdr = document.querySelector('.site-head');
  var hero = document.querySelector('.hero');
  var wa = document.querySelector('.wa');
  function onStick() {
    if (hdr) hdr.classList.toggle('is-stuck', window.scrollY > 24);
    if (wa) wa.classList.toggle('is-on', window.scrollY > (window.innerHeight * 0.75));
  }
  onStick();

  /* ---------- 2. Carrusel del hero ---------- */
  var slides = [].slice.call(document.querySelectorAll('.hero__slide'));
  var tabs = [].slice.call(document.querySelectorAll('.heronav button'));
  var titleEl = document.querySelector('.hero__ttl');
  var subEl = document.querySelector('.hero__sub');
  var markEl = document.querySelector('.hero__mark');
  var ctaEl = document.querySelector('.hero__cta-link');
  var DUR = 7000;
  var idx = 0, timer = null;

  function paint(i) {
    idx = i;
    slides.forEach(function (s, n) { s.classList.toggle('is-active', n === i); });
    tabs.forEach(function (t, n) { t.classList.toggle('is-active', n === i); t.setAttribute('aria-selected', n === i); });
    var d = tabs[i] ? tabs[i].dataset : null;
    if (!d) return;
    if (hero) hero.style.setProperty('--sv', d.color);
    if (titleEl) titleEl.textContent = d.titulo;
    if (subEl) subEl.textContent = d.sub;
    if (markEl && d.logo) { markEl.src = d.logo; markEl.alt = 'ANMIX ' + d.nombre; }
    if (ctaEl) ctaEl.setAttribute('href', d.url);
    // reinicia la barra de progreso
    if (!reduce && tabs[i]) {
      var t = tabs[i];
      t.style.animation = 'none';
      // forzar reflow para reiniciar la animación del ::after
      void t.offsetWidth;
      t.style.animation = '';
    }
  }
  function next() { paint((idx + 1) % slides.length); }
  function play() { stop(); if (!reduce && slides.length > 1) timer = setInterval(next, DUR); }
  function stop() { if (timer) clearInterval(timer); timer = null; }

  tabs.forEach(function (t, n) {
    t.addEventListener('click', function () { paint(n); play(); });
  });
  if (hero) {
    hero.addEventListener('mouseenter', function () { stop(); hero.classList.add('hero-paused'); });
    hero.addEventListener('mouseleave', function () { play(); hero.classList.remove('hero-paused'); });
  }
  if (slides.length) { paint(0); play(); }
  if (hero) requestAnimationFrame(function () { hero.classList.add('is-ready'); });

  /* ---------- 3. Industrias de cobertura ---------- */
  var items = [].slice.call(document.querySelectorAll('.strip__item'));
  var counter = document.querySelector('.strip__count');
  var stripData = items.length ? null : null;
  var open = 2; // la del centro arranca abierta, como en el wireframe

  // ventana de tarjetas visibles: la abierta al centro y las vecinas a los lados
  function stripWindow() {
    var w = window.innerWidth;
    return w > 1180 ? 5 : (w > 760 ? 3 : 1);
  }
  function paintStrip() {
    var N = items.length, W = stripWindow(), half = Math.floor(W / 2);
    items.forEach(function (el, n) {
      var rel = ((n - open) % N + N) % N;        // 0..N-1
      if (rel > N / 2) rel -= N;                 // -N/2..N/2
      var vis = Math.abs(rel) <= half;
      el.classList.toggle('is-vis', vis);
      el.classList.toggle('is-open', n === open);
      el.style.order = vis ? (rel + half) : 99;
    });
    if (counter) counter.textContent = (open + 1) + ' / ' + N;
  }
  items.forEach(function (el, n) {
    el.addEventListener('click', function () { open = n; paintStrip(); });
    el.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open = n; paintStrip(); }
    });
  });
  var prev = document.querySelector('.strip__prev');
  var nxt = document.querySelector('.strip__next');
  if (prev) prev.addEventListener('click', function () { open = (open - 1 + items.length) % items.length; paintStrip(); });
  if (nxt) nxt.addEventListener('click', function () { open = (open + 1) % items.length; paintStrip(); });
  if (items.length) paintStrip();

  /* ---------- 4. Parallax ---------- */
  var pxEls = [].slice.call(document.querySelectorAll('[data-px]'));
  var ticking = false;

  function parallax() {
    var vh = window.innerHeight;
    pxEls.forEach(function (el) {
      var host = el.closest('[data-px-host]') || el.parentElement;
      var r = host.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var speed = parseFloat(el.dataset.px) || 0.12;
      // -1 (sección arriba de la ventana) → 1 (abajo)
      var progress = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2);
      // el desplazamiento nunca puede superar el sobrante del elemento,
      // o aparecerían franjas vacías arriba o abajo
      var box = el.parentElement;
      var avail = Math.max(0, (el.offsetHeight - box.clientHeight) / 2);
      var shift = progress * speed * box.clientHeight;
      shift = Math.max(-avail, Math.min(avail, shift));
      // escala ligada al scroll: la imagen "respira" al entrar en pantalla
      var zoom = parseFloat(el.dataset.pxScale || 0);
      var scale = zoom ? (1 + zoom * Math.min(1, Math.abs(progress))) : 1;
      el.style.transform = 'translate3d(0,' + shift.toFixed(1) + 'px,0)' +
                           (zoom ? ' scale(' + scale.toFixed(4) + ')' : '');
    });
    ticking = false;
  }
  var heroBody = document.querySelector('.hero__body, .phero__body');
  var heroHost = heroBody ? heroBody.closest('.hero, .phero') : null;
  function heroDepth() {
    if (!heroBody || !heroHost || reduce) return;
    var y = window.scrollY;
    var h = heroHost.offsetHeight || 1;
    if (y > h) return;
    var p = Math.min(1, y / h);
    heroBody.style.transform = 'translate3d(0,' + (p * 58).toFixed(1) + 'px,0)';
    heroBody.style.opacity = (1 - p * 0.85).toFixed(3);
  }

  function onScroll() {
    onStick();
    heroDepth();
    if (reduce || ticking) return;
    ticking = true;
    requestAnimationFrame(parallax);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { if (!reduce) parallax(); if (items.length) paintStrip(); }, { passive: true });
  if (!reduce) parallax();

  /* ---------- 5. Revelado al entrar en pantalla ---------- */
  var rv = [].slice.call(document.querySelectorAll('.rv'));
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- 6. Contadores ---------- */
  var nums = [].slice.call(document.querySelectorAll('[data-count]'));
  function runCount(el) {
    var target = parseFloat(el.dataset.count);
    var suffix = el.dataset.suffix || '';
    var dur = 1500, t0 = null;
    if (reduce) { el.textContent = target + suffix; return; }
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); io2.unobserve(e.target); } });
    }, { threshold: 0.5 });
    nums.forEach(function (el) { io2.observe(el); });
  } else {
    nums.forEach(runCount);
  }

  /* ---------- 7. Menú móvil ---------- */
  var drawer = document.querySelector('.drawer');
  var burger = document.querySelector('.burger');
  var closeBtn = document.querySelector('.drawer__close');
  function toggleDrawer(on) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', on);
    document.body.style.overflow = on ? 'hidden' : '';
    if (burger) burger.setAttribute('aria-expanded', on);
  }
  if (burger) burger.addEventListener('click', function () { toggleDrawer(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { toggleDrawer(false); });
  if (drawer) drawer.addEventListener('click', function (e) { if (e.target.tagName === 'A') toggleDrawer(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggleDrawer(false); });

  /* ---------- 8. Ripple de Material 3 ---------- */
  var RIPPLE_SEL = '.btn, .svc, .chip, .other, .strip__item, .svc__go, .cc__i, .pillar';
  document.addEventListener('pointerdown', function (e) {
    if (reduce) return;
    var host = e.target.closest(RIPPLE_SEL);
    if (!host) return;
    var r = host.getBoundingClientRect();
    var size = Math.max(r.width, r.height) * 1.1;
    var span = document.createElement('span');
    span.className = 'ripple';
    span.style.width = span.style.height = size + 'px';
    span.style.left = (e.clientX - r.left - size / 2) + 'px';
    span.style.top = (e.clientY - r.top - size / 2) + 'px';
    if (getComputedStyle(host).position === 'static') host.style.position = 'relative';
    host.appendChild(span);
    setTimeout(function () { span.remove(); }, 520);
  }, { passive: true });

  /* ---------- 9. Escalonado de rejillas ---------- */
  [].slice.call(document.querySelectorAll('.stagger')).forEach(function (grid) {
    [].slice.call(grid.children).forEach(function (child, i) { child.style.setProperty('--i', i); });
  });

  /* ---------- 10. Formulario (sólo prototipo) ---------- */
  var form = document.querySelector('.form');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = form.querySelector('[type=submit]');
    if (btn) { btn.textContent = 'Enviado ✓'; btn.style.background = 'var(--verde-hondo)'; }
  });
})();
