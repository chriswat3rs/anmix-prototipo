# -*- coding: utf-8 -*-
"""Genera las páginas interiores del prototipo ANMIX.

Contenido: portafolio empresarial (Información ANMIX.pdf).
Los datos duros —cifras, alcances, normas, misión y visión— van textuales.
Los titulares, descripciones y llamados a la acción están reescritos para que
cada bloque suene distinto: el original repite mucho las mismas fórmulas.

Vocabulario de acción unificado en todo el sitio:
  · Solicite su cotización   → acción principal (encabezado, hero, menú móvil)
  · Agende una visita        → cierre de página
  · Enviar solicitud         → botón del formulario
  · Ver servicio             → navegación entre servicios
"Sin costo" se dice una sola vez por página, junto al formulario. Nunca en un botón.
"""
import re, os

OUT = "proto"
SPRITE = re.search(r'(<svg class="ico-sprite".*?</svg>)',
                   open(f"{OUT}/index.html", encoding="utf-8").read(), re.S).group(1)

# ─────────────────────────────── DATOS ───────────────────────────────
SERV = [
 dict(desc="Pisos, cristales y sanitarios", slug="limpieza", n=1, nombre="Limpieza", color="--sv-limpieza", iso="limpieza", lock="limpieza",
      hero="limpieza", tit="Servicios de limpieza industrial y comercial.",
      promesa="Mantenemos sus instalaciones impecables para que usted pueda enfocarse en su operación.",
      card="Pisos, cristales, sanitarios y mobiliario, con rutinas que priorizan las áreas de mayor tránsito y una supervisión que no depende de que usted la pida.",
      cierre="Su operación no debería detenerse para limpiar.",
      inc="Todo esto entra en la tarifa mensual de limpieza.",
      intro="Diseñamos soluciones de limpieza personalizada para cada tipo de inmueble, combinando personal capacitado, supervisión continua y procesos estandarizados para garantizar espacios limpios, seguros y listos para operar al más alto nivel.",
      pilares=[("Ambientes seguros y saludables","Código de colores y protocolos de sanitización que le cierran la puerta a la contaminación cruzada."),
               ("Instalaciones impecables","La primera impresión de su empresa la da el piso del vestíbulo, no el folleto."),
               ("Personal capacitado y confiable","Ficha de identificación de cada persona asignada y capacitación anual certificada."),
               ("Supervisión constante","Auditoría discreta mensual: nos revisamos antes de que usted tenga que hacerlo.")],
      alcance=["Limpieza de pisos","Alfombras","Plafones","Mobiliario en general","Escaleras y elevadores","Sanitarios",
               "Vidrios interiores y exteriores hasta 2.50 m de altura","Lavado de salas","Pulido de pisos","Limpieza de naves industriales"],
      sectores=["Oficinas","Corporativos","Industria","Escuelas","Hospitales","Comercios","Condominios"],
      cc=True),

 dict(desc="Áreas verdes todo el año", slug="jardineria", n=2, nombre="Jardinería", color="--sv-jardineria", iso="jardineria", lock="jardineria",
      hero="jardineria", tit="Servicios de jardinería industrial y comercial.",
      promesa="Áreas verdes que transforman espacios y reflejan profesionalismo.",
      card="Un jardín corporativo se nota cuando está descuidado, no cuando está bien. Mantenimiento, poda, riego y paisajismo los doce meses del año.",
      cierre="El primer contacto con su empresa es la entrada.",
      inc="Todo esto entra en la tarifa mensual de jardinería.",
      intro="Ofrecemos servicios de jardinería profesional para mantener y realzar sus áreas verdes, creando entornos armónicos, saludables y bien cuidados durante todo el año.",
      pilares=[("Mantenimiento integral","Un programa continuo que sigue la temporada, no un corte cada que alguien se queja."),
               ("Poda y recorte","Árboles y arbustos con técnica y calendario de intervención definido."),
               ("Control de maleza y fertilización","Se trabaja el suelo, no sólo lo que se ve encima."),
               ("Riego eficiente","Sistemas y rutinas que cuidan el consumo de agua sin sacrificar el resultado.")],
      alcance=["Diseño de jardines","Mantenimiento de áreas verdes","Sistemas de riego","Instalación de césped",
               "Paisajismo","Poda de árboles y arbustos","Control de maleza","Fertilización"],
      sectores=["Oficinas","Corporativos","Industria","Escuelas","Hospitales","Comercios","Condominios"]),

 dict(desc="Diseño, obra y remodelación", slug="arquitectura", n=3, nombre="Arquitectura", color="--sv-arquitectura", iso="arquitectura", lock="arquitectura",
      hero="arquitectura", tit="Diseñamos, construimos y remodelamos.",
      promesa="Del render a la entrega de llaves, con un solo responsable de por medio.",
      card="Del render a la entrega de llaves. Oficinas, interiores y espacios comerciales, con la coordinación de obra en nuestra cancha y no en la suya.",
      cierre="El espacio que ya tiene puede funcionar mejor.",
      inc="Todo esto va dentro del presupuesto de obra.",
      intro="Creamos soluciones integrales para el desarrollo, renovación y transformación de espacios, cuidando cada etapa del proceso para asegurar funcionalidad, estética y adaptación a las necesidades de cada cliente, desde el diseño conceptual hasta la ejecución de la obra.",
      pilares=[("Diseño conceptual","Partido arquitectónico y programa de necesidades antes de mover un solo muro."),
               ("Diseño ejecutivo","Planos, especificaciones y detalles listos para construir."),
               ("Renders y visualización 3D","Ver el espacio terminado antes de firmar el presupuesto."),
               ("Construcción y ejecución","Oficios, materiales y tiempos coordinados desde una sola mesa."),
               ("Supervisión de obra","Calidad, avance y presupuesto revisados en sitio, no por teléfono.")],
      alcance=["Diseño conceptual","Diseño ejecutivo","Renders y visualización 3D","Construcción y ejecución de obra",
               "Supervisión de obra","Remodelación de interiores","Mantenimiento de inmuebles","Diseño de interiores"],
      sectores=["Arquitectura","Diseño de interiores","Remodelación","Residencial","Comercial"]),

 dict(desc="Alturas y fachadas", slug="servicios-especiales", n=4, nombre="Servicios especiales", color="--sv-especiales", iso="especiales", lock="especiales",
      hero="especiales", tit="Servicios especiales y trabajos en altura.",
      promesa="Donde hace falta arnés, certificación y un permiso firmado antes de empezar.",
      card="Fachadas, cristales y estructuras a la altura que haga falta. Personal con certificación DC-3 y permiso de trabajo firmado antes de cada maniobra.",
      cierre="Lo que está alto también se ensucia.",
      inc="Todo esto va incluido en cada maniobra.",
      intro="Realizamos trabajos en alturas y servicios especiales con personal certificado, equipo especializado y estrictos protocolos de seguridad para garantizar resultados excepcionales en cada proyecto.",
      pilares=[("Trabajos en alturas","Personal con certificación DC-3 y equipo de protección específico por maniobra."),
               ("Limpieza de cristales en altura","Fachadas y ventanales exteriores sin cerrar el edificio."),
               ("Mantenimiento de estructuras","Naves industriales y hangares: instalación, limpieza y conservación."),
               ("Protocolos de seguridad","Plan de trabajo, permiso y supervisión. En ese orden, siempre.")],
      alcance=["Limpieza de vidrios de altura en exteriores","Mantenimiento de fachadas en alturas",
               "Limpieza y mantenimiento de estructuras de altura","Naves industriales y hangares",
               "Lavado de alfombras","Lavado de salas","Pulido de pisos","Limpieza profunda de naves industriales"],
      sectores=["Oficinas","Corporativos","Industria","Escuelas","Hospitales","Comercios","Condominios"]),

 dict(desc="Gestión de condominios", slug="software-gestion-residencial", n=5, nombre="Software para gestión residencial", color="--sv-software", iso="software", lock="software",
      hero="software", tit="La administración de su condominio en una sola plataforma.",
      promesa="Cuotas, amenidades, visitas e incidencias en una sola pantalla.",
      card="Cuotas, pagos, amenidades, visitas e incidencias del condominio en una sola pantalla. Los residentes dejan de llamar al administrador por todo.",
      cierre="La administración de su condominio cabe en una pantalla.",
      inc="Va incluido en la suscripción. No hay módulos que se cobren aparte.",
      intro="Centralice la información, automatice procesos y mantenga una comunicación eficiente con residentes y comités mediante una plataforma diseñada para simplificar la gestión de condominios.",
      pilares=[("Control de cuotas y pagos","Estados de cuenta, recordatorios y conciliación en un solo tablero."),
               ("Reportes financieros en tiempo real","Ingresos, egresos y morosidad sin esperar al cierre de mes."),
               ("Reservación de amenidades","Salones, canchas y áreas comunes sin llamadas ni libreta en caseta."),
               ("Incidencias y mantenimiento","Se reporta, se asigna y se cierra con foto. Todo queda registrado."),
               ("Control de visitas y accesos","Registro digital de entradas y salidas, consultable después."),
               ("Comunicación con residentes","Avisos y encuestas sin depender del grupo de WhatsApp.")],
      alcance=["Control de cuotas y pagos","Reportes financieros","Reservación de amenidades","Gestión de incidencias",
               "Control de visitas","Comunicación con residentes","Documentos del condominio","Directorio de comités"],
      sectores=["Condominios","Privadas","Residenciales","Departamentos","Rentas","Desarrollos"]),

 dict(desc="Guardias y control de accesos", slug="seguridad-privada", n=6, nombre="Seguridad privada", color="--sv-seguridad", iso="seguridad", lock="seguridad",
      hero="seguridad", tit="Seguridad que protege su operación.",
      promesa="Vigilancia que deja rastro: bitácora, evidencia y un responsable por turno.",
      card="Guardias intramuros, control de accesos y rondines que quedan registrados. Si algo pasa a las tres de la mañana, a las ocho hay bitácora.",
      cierre="Tranquilidad es saber que alguien está mirando.",
      inc="Todo esto entra en la tarifa mensual por elemento.",
      intro="Ofrecemos soluciones integrales de seguridad privada adaptables a las necesidades de cada cliente, combinando personal capacitado, supervisión constante y tecnología para proteger personas, instalaciones y activos con los más altos estándares de profesionalismo.",
      pilares=[("Personal capacitado y certificado","Selección, capacitación y evaluación continua de cada elemento."),
               ("Supervisión y control operativo","Rondas verificadas y un mando identificable por turno."),
               ("Evidencia fotográfica y reportes","Cada novedad queda documentada, no contada."),
               ("Bitácoras digitales","El histórico de cada punto de servicio, consultable en línea."),
               ("Atención a incidencias","Protocolo de respuesta acordado con usted, no improvisado."),
               ("Comunicación 24/7","Los 365 días, incluidos los que nadie quiere cubrir.")],
      alcance=["Guardias intramuros","Vigilancia 24/7","Control de accesos","Rondines verificados",
               "Bitácoras digitales","Evidencia fotográfica","Atención a emergencias","Supervisión operativa"],
      sectores=["Oficinas","Corporativos","Industria","Escuelas","Hospitales","Comercios","Condominios"]),

 dict(desc="Pintura, cerámica e interiores", slug="detailing-automotriz", n=7, nombre="Detailing automotriz", color="--sv-detailing", iso="detailing", lock="detailing",
      hero="detailing", tit="Más que limpieza: una experiencia premium.",
      promesa="Su auto entra por una cita y sale como el día que lo compró.",
      card="Corrección de pintura, protección cerámica y limpieza profunda. Su auto entra por una cita, no por una fila, y sale como el día que lo compró.",
      cierre="Su auto merece algo más que una lavada.",
      inc="Va incluido en cada servicio. No hay paquetes escalonados.",
      intro="Restauramos, protegemos y realzamos la apariencia de su vehículo mediante procesos especializados de detallado automotriz, utilizando productos de alta calidad y atención meticulosa en cada detalle.",
      pilares=[("Corrección y restauración de pintura","Pulido por etapas para borrar marcas y devolverle profundidad al color."),
               ("Protección cerámica y selladores","Una capa que aguanta sol, agua y contaminantes durante meses."),
               ("Limpieza profunda interior y exterior","Cada superficie con el producto y la técnica que le corresponde."),
               ("Evidencia visual del proceso","Antes, durante y después. Usted ve qué se hizo y dónde."),
               ("Atención personalizada por cita","Su vehículo no comparte turno con otros cinco."),
               ("Acabados premium","El estándar es que el resultado supere lo que esperaba.")],
      alcance=["Corrección de pintura","Pulido y abrillantado","Protección cerámica","Selladores",
               "Limpieza profunda de interiores","Lavado de tapicería","Descontaminación de pintura","Tratamiento de rines y llantas"],
      sectores=["Particulares","Flotillas","Agencias","Concesionarias","Corporativos"]),

 dict(desc="Papel, químicos y EPP", slug="suministros-corporativos", n=8, nombre="Suministros corporativos", color="--sv-suministros", iso="suministros", lock="suministros",
      hero="suministros", tit="Todo lo que su empresa necesita, con un solo proveedor.",
      promesa="Un pedido, un calendario fijo y ningún faltante a media semana.",
      card="Papel, químicos, despachadores y equipo de protección. Una sola orden de compra, un calendario fijo de entrega y ningún faltante a media semana.",
      cierre="Nunca más un sanitario sin papel.",
      inc="Va incluido en el suministro. No cobramos el servicio aparte.",
      intro="Abastecemos su operación con productos de limpieza, higiene, seguridad y más, garantizando calidad, disponibilidad y entregas puntuales para que su empresa nunca se detenga.",
      pilares=[("Amplio catálogo","Limpieza, higiene, seguridad y consumibles en una sola orden de compra."),
               ("Entregas programadas","Calendario fijo de reabastecimiento. Nadie sale corriendo por papel."),
               ("Químicos identificados por NOM","Biodegradables y etiquetados conforme a la NOM-018-STPS-2015."),
               ("Precios competitivos","El volumen consolidado se refleja en el costo, no en el margen."),
               ("Asesoría de producto","Le decimos cuál sirve para su superficie, aunque sea el más barato.")],
      alcance=["Papel higiénico y toallas","Jabones y sanitizantes","Desinfectantes y limpiadores multiusos",
               "Bolsas y contenedores","Equipo de protección personal","Despachadores","Señalización de seguridad","Utensilios de limpieza"],
      sectores=["Oficinas","Corporativos","Industria","Escuelas","Hospitales","Comercios","Condominios"]),
]

# Las once cláusulas del contrato (portafolio, pág. 4). Completas sólo en servicios.html.
INCLUYE = [
 "Cobertura total garantizada los 365 días del año.",
 "Material, equipo, herramientas y químicos biodegradables mensuales para operar el servicio.",
 "Uniforme y EPP según la necesidad, coordinados con el equipo de seguridad e higiene del cliente.",
 "Ficha de identificación del personal asignado al servicio.",
 "Plan mensual de auditoría discreta para validar la ejecución precisa de procedimientos.",
 "Programa de capacitación anual impartido por instructores autorizados por la Secretaría del Trabajo.",
 "Rutinas de trabajo personalizadas, con prioridad en las áreas de mayor movimiento.",
 "Reporte mensual de evaluación de las áreas atendidas.",
 "Reporte mensual de cumplimiento fiscal y laboral conforme a REPSE: IMSS, SAT, INFONAVIT y FONACOT.",
 "Análisis de costos anual.",
 "Póliza de responsabilidad civil ante incidentes causados por nuestro personal.",
]
# Versión corta para las 8 páginas de servicio: repetir once puntos ocho veces cansa.
INCLUYE_CORTO = [
 "Cobertura garantizada los 365 días del año.",
 "Material, equipo y químicos biodegradables incluidos.",
 "Ficha de identificación del personal asignado.",
 "Auditoría discreta mensual de la ejecución.",
 "Reporte de cumplimiento REPSE ante IMSS, SAT, INFONAVIT y FONACOT.",
 "Póliza de responsabilidad civil.",
]

CC = [("Sanitarios","#DC242B","Inodoros, mingitorios y lavabos."),
      ("Oficinas","#0696BC","Escritorios, mobiliario y áreas comunes."),
      ("Almacenes","#FDC525","Anaqueles, pisos y zonas de carga."),
      ("Cocinas","#049F8D","Superficies en contacto con alimentos."),
      ("Comedores","#8A8A87","Mesas, sillas y áreas de servicio.")]

CLIENTES = [("bosch","Bosch"),("cfe","CFE"),("suzuki","Suzuki"),("john-deere","John Deere"),("penoles","Peñoles"),
 ("swatch","Swatch Group"),("schwan","Schwan Cosmetics"),("avemex","Avemex"),("universal-aviation","Universal Aviation"),
 ("infra","INFRA"),("innovax","Innovax"),("aluxen","Aluxen"),("cycsa","CYCSA"),("fycsa","Fycsa"),("syscom","Syscom"),
 ("teleco","Teleco"),("cosmetic-colors","Cosmetic Colors"),("performance-air","Performance Air"),("aerovics","Aerovics")]

ICO = {"tel":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.2z%22/></svg>",
 "mail":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z%22/></svg>",
 "pin":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M12 2a7 7 0 00-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 00-7-7zm0 9.5A2.5 2.5 0 1112 6.5a2.5 2.5 0 010 5z%22/></svg>",
 "user":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M12 12c2.8 0 5-2.2 5-5s-2.2-5-5-5-5 2.2-5 5 2.2 5 5 5zm0 2c-3.3 0-10 1.7-10 5v3h20v-3c0-3.3-6.7-5-10-5z%22/></svg>",
 "fb":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H8v3h2v7h3v-7h3l1-3h-4v-2c0-.6.4-1 1-1z%22/></svg>",
 "ig":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M12 2c2.7 0 3 0 4.1.1 1.1 0 1.8.2 2.4.5.7.2 1.2.6 1.7 1.1s.9 1 1.1 1.7c.3.6.4 1.3.5 2.4C22 8.9 22 9.3 22 12s0 3-.1 4.1c0 1.1-.2 1.8-.5 2.4a4.6 4.6 0 01-1.1 1.7c-.5.5-1 .9-1.7 1.1-.6.3-1.3.4-2.4.5-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-1.1 0-1.8-.2-2.4-.5a4.6 4.6 0 01-1.7-1.1 4.6 4.6 0 01-1.1-1.7c-.3-.6-.4-1.3-.5-2.4C2 15.1 2 14.7 2 12s0-3 .1-4.1c0-1.1.2-1.8.5-2.4a4.6 4.6 0 011.1-1.7c.5-.5 1-.9 1.7-1.1.6-.3 1.3-.4 2.4-.5C8.9 2 9.3 2 12 2zm0 5a5 5 0 100 10 5 5 0 000-10zm0 8.2a3.2 3.2 0 110-6.4 3.2 3.2 0 010 6.4zM17.8 6.9a1.2 1.2 0 11-2.3 0 1.2 1.2 0 012.3 0z%22/></svg>",
 "in":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M6.9 8H4v12h2.9V8zM5.4 3.5a1.7 1.7 0 100 3.4 1.7 1.7 0 000-3.4zM20 13.4c0-3.2-1.7-4.7-4-4.7-1.8 0-2.7 1-3.1 1.7V8H10v12h2.9v-6.7c0-1.5.8-2.2 1.9-2.2s1.8.7 1.8 2.2V20H20v-6.6z%22/></svg>",
 "wa":"<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1a13 13 0 01-5.6-4.9c-.4-.6-1-1.5-1-2.9s.7-2 1-2.3c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2 0 .4-.1.5l-.4.5c-.1.2-.3.3-.1.6.4.6.8 1.2 1.4 1.7.7.6 1.3.8 1.5.9.2.1.4.1.5-.1l.7-.8c.2-.2.3-.2.5-.1l2 .9c.2.1.4.2.4.3v.9z%22/></svg>"}
def ic(k): return "url('data:image/svg+xml;utf8,%s')" % ICO[k]

# ─────────────────────────────── PARCIALES ───────────────────────────────
def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/anmix.css">
</head>
<body>

{SPRITE}
'''

def _lbl(nombre):
    return (nombre.replace("Software para gestión residencial", "Software<br>residencial")
                  .replace("Servicios especiales", "Servicios<br>especiales")
                  .replace("Seguridad privada", "Seguridad<br>privada")
                  .replace("Detailing automotriz", "Detailing<br>automotriz")
                  .replace("Suministros corporativos", "Suministros<br>corporativos"))

def subnav(active=None):
    rows = []
    for s in SERV:
        cls = ' class="is-active"' if s["slug"] == active else ""
        rows.append(
            f'        <a href="servicio-{s["slug"]}.html"{cls} style="--sv:var({s["color"]})">\n'
            f'          <svg class="ico" aria-hidden="true"><use href="#ic-{s["n"]}"></use></svg>\n'
            f'          <span><b>{s["nombre"]}</b><i>{s["desc"]}</i></span>\n'
            f'        </a>')
    rows.append('        <a class="subnav__all" href="servicios.html"><span><b>Ver todos los servicios</b></span></a>')
    return "\n".join(rows)

def drawer_links():
    return "\n".join(
        f'    <a href="servicio-{s["slug"]}.html" style="--sv:var({s["color"]})">'
        f'<svg class="ico" aria-hidden="true"><use href="#ic-{s["n"]}"></use></svg>{s["nombre"]}</a>'
        for s in SERV)

def header(page, active_svc=None):
    cur = lambda p: ' aria-current="page"' if p == page else ""
    return f'''<div class="site-head site-head--inner">
<div class="topbar">
  <div class="wrap wrap--wide topbar__in">
    <div class="topbar__l">
      <a href="tel:+527222720428"><i class="ic-mini" style="--ic:{ic('tel')}"></i>722 272 0428</a>
      <span class="topbar__sep">·</span>
      <a class="topbar__hide" href="mailto:contacto@anmix.mx">contacto@anmix.mx</a>
      <span class="topbar__sep topbar__hide">·</span>
      <span class="topbar__hide">Toluca, Estado de México</span>
    </div>
    <div class="topbar__r">
      <a href="#"><i class="ic-mini" style="--ic:{ic('user')}"></i>Sign in</a>
    </div>
  </div>
</div>

<header class="hdr">
  <div class="wrap wrap--wide hdr__in">
    <a class="hdr__logo" href="index.html" aria-label="ANMIX, inicio">
      <img src="assets/img/logos/lock-limpieza-claro.png" alt="ANMIX · Alto nivel en servicios" width="260" height="42">
    </a>
    <nav class="nav" aria-label="Principal">
      <span class="nav__item"><a href="index.html"{cur('inicio')}>Inicio</a></span>
      <span class="nav__item"><a href="nosotros.html"{cur('nosotros')}>Nosotros</a></span>
      <span class="nav__item nav__item--sub">
        <a href="servicios.html"{cur('servicios')} aria-haspopup="true">Servicios</a>
        <div class="subnav"><div class="subnav__in">
{subnav(active_svc)}
        </div></div>
      </span>
      <span class="nav__item"><a href="contacto.html"{cur('contacto')}>Contacto</a></span>
    </nav>
    <div class="hdr__cta">
      <a class="btn btn--primary btn--sm" href="contacto.html">Solicite su cotización</a>
      <button class="burger" aria-label="Abrir menú" aria-expanded="false"><span></span></button>
    </div>
  </div>

</header>
</div><!-- /.site-head -->

<div class="drawer" role="dialog" aria-label="Menú">
  <div class="drawer__top">
    <img src="assets/img/logos/lock-limpieza-claro.png" alt="ANMIX">
    <button class="drawer__close" aria-label="Cerrar menú">&times;</button>
  </div>
  <nav>
    <a href="index.html">Inicio</a>
    <a href="nosotros.html">Nosotros</a>
    <a href="servicios.html">Servicios</a>
    <a href="contacto.html">Contacto</a>
{drawer_links()}
  </nav>
  <div class="drawer__foot">
    <a class="btn btn--primary" href="contacto.html">Solicite su cotización</a>
    <a class="btn btn--ghost-inv" href="tel:+527222720428">722 272 0428</a>
  </div>
</div>
'''

def clientes_band():
    """Carrusel de logos, sin texto: sólo las marcas."""
    imgs = "".join(f'<img src="assets/img/clientes/{k}.png" alt="{n}">' for k, n in CLIENTES)
    dup  = "".join(f'<img src="assets/img/clientes/{k}.png" alt="" aria-hidden="true">' for k, _ in CLIENTES)
    return f'''<section class="clientes" aria-label="Clientes de ANMIX">
  <div class="marquee"><div class="marquee__track">{imgs}{dup}</div></div>
</section>
'''

def cta_band(frase, img="assets/img/heros/especiales.jpg", boton="Agende una visita"):
    return f'''<section class="band" data-px-host>
  <div class="band__bg"><img data-px="0.18" data-px-scale="0.06" src="{img}" alt=""></div>
  <div class="band__veil"></div>
  <div class="band__in"><div class="wrap">
    <p class="rv">{frase}</p>
    <a class="btn btn--primary rv rv-d1" href="contacto.html" style="margin-top:36px">{boton}</a>
  </div></div>
</section>
'''

def footer():
    svc_links = "\n".join(f'          <li><a href="servicio-{s["slug"]}.html">{s["nombre"]}</a></li>' for s in SERV)
    return f'''<footer class="ftr">
  <div class="wrap wrap--wide">
    <div class="ftr__grid">
      <div>
        <img class="ftr__logo" src="assets/img/logos/lock-limpieza-claro.png" alt="ANMIX · Alto nivel en servicios">
        <p style="font-size:.9rem;line-height:1.7;max-width:34ch">
          Operación y conservación de instalaciones para empresas que no pueden permitirse
          parar. ANMIX Servicios S.A. de C.V.
        </p>
        <span class="repse" style="margin-top:20px"><i></i>REPSE AR154933</span>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
{svc_links}
        </ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="nosotros.html">Nosotros</a></li>
          <li><a href="servicios.html">Todos los servicios</a></li>
          <li><a href="contacto.html">Contacto</a></li>
          <li><a href="https://anmix.mx/aviso/">Aviso de privacidad</a></li>
        </ul>
      </div>
      <div>
        <h4>Encuéntranos</h4>
        <ul>
          <li>Calle Sor Juana Inés de la Cruz No. 2, 1er Nivel, Interior 2, C.P. 50210, Toluca, Estado de México.</li>
          <li><a href="tel:+527222720428">722 272 0428</a></li>
          <li><a href="mailto:contacto@anmix.mx">contacto@anmix.mx</a></li>
        </ul>
        <div class="ftr__soc">
          <a href="#" aria-label="Facebook"><i class="ic-mini" style="--ic:{ic('fb')}"></i></a>
          <a href="#" aria-label="Instagram"><i class="ic-mini" style="--ic:{ic('ig')}"></i></a>
          <a href="#" aria-label="LinkedIn"><i class="ic-mini" style="--ic:{ic('in')}"></i></a>
          <a href="https://wa.me/527227910294" aria-label="WhatsApp"><i class="ic-mini" style="--ic:{ic('wa')}"></i></a>
        </div>
      </div>
    </div>
    <div class="ftr__legal">
      <span>© 2026 ANMIX · Alto nivel en servicios. Todos los derechos reservados.</span>
      <span><a href="https://anmix.mx/aviso/">Aviso de privacidad</a></span>
    </div>
  </div>
</footer>

<a class="wa" href="https://wa.me/527227910294" aria-label="Escríbenos por WhatsApp">
  <i class="ic-mini" style="--ic:{ic('wa')}"></i><span>Hable con un asesor</span>
</a>

<script src="assets/js/anmix.js"></script>
</body>
</html>
'''

def form(preselect=None):
    opts = "".join(f'<option{" selected" if s["nombre"] == preselect else ""}>{s["nombre"]}</option>' for s in SERV)
    return f'''<form class="form rv rv-d1" novalidate>
        <div class="form__grid">
          <label class="field"><input type="text" name="nombre" placeholder="María Hernández" required><span>Nombre completo</span></label>
          <label class="field"><input type="text" name="empresa" placeholder="Grupo Industrial S.A."><span>Empresa</span></label>
          <label class="field"><input type="email" name="correo" placeholder="maria@empresa.mx" required><span>Correo corporativo</span></label>
          <label class="field"><input type="tel" name="telefono" placeholder="722 000 0000" required><span>Teléfono</span></label>
          <label class="field field--full field--select"><select name="servicio">{opts}</select><span>Servicio de interés</span></label>
          <label class="field field--full"><textarea name="mensaje" rows="4" placeholder="Tres sedes en Toluca, turnos de 7 a 19 h, planta baja de alto tránsito…"></textarea><span>Cuéntanos qué necesitas</span><small>Superficie aproximada, número de sedes, horarios y áreas críticas.</small></label>
        </div>
        <div class="form__foot">
          <label class="check"><input type="checkbox" required><span class="box"></span><span>He leído y acepto el <a href="https://anmix.mx/aviso/">aviso de privacidad</a>.</span></label>
          <button class="btn btn--primary" type="submit">Enviar solicitud</button>
        </div>
      </form>'''

def others_grid(exclude):
    return "\n".join(f'''    <a class="other" href="servicio-{s["slug"]}.html" style="--sv:var({s["color"]})">
      <img src="assets/img/logos/iso-{s["iso"]}.png" alt="" width="36" height="36">
      <span>{s["nombre"]}</span>
    </a>''' for s in SERV if s["slug"] != exclude)

def incluye_corto(s):
    lis = "\n".join(f'      <li><i>✓</i>{t}</li>' for t in INCLUYE_CORTO)
    return f'''<section class="sec sec--dark">
  <div class="wrap wrap--wide">
    <p class="eyebrow eyebrow--green rv">Va incluido</p>
    <h2 class="d-l rv" style="color:#fff">Sin cargos por separado.</h2>
    <p class="lead lead--inv rv rv-d1" style="margin-top:20px">{s["inc"]}</p>
    <ul class="include rv rv-d2">
{lis}
    </ul>
    <a class="btn btn--ghost-inv rv rv-d3" href="servicios.html#contrato" style="margin-top:40px">Ver las once cláusulas</a>
  </div>
</section>
'''

def chips(lista, inv=False):
    cls = "chips chips--inv" if inv else "chips"
    return f'<div class="{cls} rv rv-d2">' + "".join(f'<span class="chip"><span>{c}</span></span>' for c in lista) + '</div>'


def marca_servicio(s):
    """Logotipo ANMIX de la división, encabezando el bloque del servicio.
    Variante con la palabra *anmix* en negro, porque el fondo es blanco.
    El morado de Suministros es una composición propia: no existe original."""
    return (f'<img class="marca rv" src="assets/img/logos/lock-{s["lock"]}-oscuro.png" '
            f'alt="ANMIX {s["nombre"]}" width="176" height="52">')

# ─────────────────────────────── PÁGINA: SERVICIO ───────────────────────────────
def page_servicio(s):
    pil = "\n".join(f'      <article class="pillar"><b>{i+1:02d}</b><h3>{t}</h3><p>{d}</p></article>'
                    for i, (t, d) in enumerate(s["pilares"]))
    ncls = "pillars--4" if len(s["pilares"]) == 4 else ("pillars--6" if len(s["pilares"]) >= 6 else "")
    alc = "\n".join(f'        <li><i></i>{a}</li>' for a in s["alcance"])
    cc_block = ""
    if s.get("cc"):
        cc_items = "\n".join(
            f'''      <div class="cc__i"><span class="cc__sw" style="background:{c}"></span><b>{n}</b><span>{d}</span></div>'''
            for n, c, d in CC)
        cc_block = f'''
<section class="sec sec--bone">
  <div class="wrap wrap--wide">
    <p class="eyebrow rv">Método</p>
    <h2 class="d-l rv">Código de colores</h2>
    <p class="lead rv rv-d1" style="margin-top:20px">
      Cada utensilio —franela, mechudo, cubeta, guante— tiene un color y un área asignada.
      Nada que tocó un sanitario vuelve a tocar una cocina. Es la medida más simple contra la
      contaminación cruzada y <b>reduce hasta un 80&nbsp;% el riesgo de transmisión de patógenos.</b>
    </p>
    <div class="cc stagger rv rv-d2">
{cc_items}
    </div>
  </div>
</section>
'''
    return head(f'{s["nombre"]} · ANMIX', s["promesa"]) + header("servicios", s["slug"]) + f'''
<main style="--sv:var({s["color"]})">

<section class="phero" data-px-host>
  <div class="phero__bg"><img data-px="0.12" data-px-scale="0.05" src="assets/img/heros/{s["hero"]}.jpg" alt="{s["nombre"]} · ANMIX" fetchpriority="high"></div>
  <div class="phero__veil"></div>
  <div class="phero__in"><div class="wrap wrap--wide">
    <div class="phero__body">
      <h1 class="d-xl rv">{s["tit"]}</h1>
      <p class="phero__sub rv rv-d1">{s["promesa"]}</p>
      <a class="btn btn--primary rv rv-d2" href="contacto.html">Solicite su cotización</a>
    </div>
  </div></div>
</section>

<section class="sec">
  <div class="wrap wrap--wide">
    <div class="split">
      <div>
        {marca_servicio(s)}
        <h2 class="d-m rv">{s["promesa"]}</h2>
      </div>
      <div>
        <p class="lead rv rv-d1">{s["intro"]}</p>
        <p class="eyebrow rv rv-d2" style="margin-top:40px;margin-bottom:0">Dónde lo aplicamos</p>
        {chips(s["sectores"])}
      </div>
    </div>

    <div class="pillars {ncls} stagger rv" style="margin-top:var(--sp-8)">
{pil}
    </div>
  </div>
</section>

<section class="sec sec--bone">
  <div class="wrap wrap--wide">
    <div class="split split--rev">
      <div>
        <p class="eyebrow rv">Alcance</p>
        <h2 class="d-m rv">Qué hacemos exactamente</h2>
        <ul class="scope rv rv-d1">
{alc}
        </ul>
      </div>
      <div class="split__media rv rv-d1" data-px-host>
        <img data-px="0.1" data-px-scale="0.05" src="assets/img/heros/{s["hero"]}.jpg" alt="">
      </div>
    </div>
  </div>
</section>
{cc_block}
{incluye_corto(s)}

<section class="sec">
  <div class="wrap wrap--wide">
    <p class="eyebrow rv">El resto del catálogo</p>
    <h2 class="d-m rv">Todo bajo el mismo contrato</h2>
    <div class="others stagger rv rv-d1">
{others_grid(s["slug"])}
    </div>
  </div>
</section>

{cta_band(s["cierre"], img=f'assets/img/heros/{s["hero"]}.jpg')}
</main>
''' + footer()


# ─────────────────────────────── PÁGINA: SERVICIOS ───────────────────────────────
def page_servicios():
    cards = "\n".join(f'''      <a class="svc" href="servicio-{s["slug"]}.html" style="--sv:var({s["color"]})">
        <span class="svc__mark"><img class="svc__iso" src="assets/img/logos/iso-{s["iso"]}.png" alt="" width="44" height="44"></span>
        <h3>{s["nombre"]}</h3>
        <p>{s["card"]}</p>
        <span class="svc__go">Ver servicio</span>
      </a>''' for s in SERV)
    lis = "\n".join(f'      <li><i>✓</i>{t}</li>' for t in INCLUYE)
    return head("Servicios · ANMIX",
                "Limpieza, jardinería, arquitectura, trabajos en altura, software de gestión residencial, seguridad privada, detailing automotriz y suministros corporativos.") \
        + header("servicios") + f'''
<main>

<section class="phero" data-px-host>
  <div class="phero__bg"><img data-px="0.12" data-px-scale="0.05" src="assets/img/heros/limpieza.jpg" alt="" fetchpriority="high"></div>
  <div class="phero__veil"></div>
  <div class="phero__in"><div class="wrap wrap--wide">
    <div class="phero__body">
      <h1 class="d-xl rv">Ocho servicios.<br>Una sola factura.</h1>
      <p class="phero__sub rv rv-d1">
        Contrate uno o los ocho. En cualquier caso tratará con el mismo interlocutor, firmará
        un solo contrato y recibirá un solo reporte mensual.
      </p>
      <a class="btn btn--primary rv rv-d2" href="contacto.html">Solicite su cotización</a>
    </div>
  </div></div>
</section>

<section class="sec">
  <div class="wrap wrap--wide">
    <p class="eyebrow rv">Catálogo</p>
    <h2 class="d-l rv">Qué hacemos</h2>
    <div class="svc-grid stagger rv rv-d1">
{cards}
    </div>
  </div>
</section>

<section class="sec sec--dark" id="contrato">
  <div class="wrap wrap--wide">
    <p class="eyebrow eyebrow--green rv">El contrato</p>
    <h2 class="d-l rv" style="color:#fff">Sin letras chiquitas.</h2>
    <p class="lead lead--inv rv rv-d1" style="margin-top:20px">
      Estas once cláusulas van dentro del precio de cualquiera de nuestros servicios. No son
      extras, no se facturan aparte y no dependen de que usted las pida.
    </p>
    <ul class="include rv rv-d2">
{lis}
    </ul>
  </div>
</section>

{clientes_band()}

<section class="sec sec--bone">
  <div class="wrap wrap--wide">
    <p class="eyebrow rv">Cómo empieza</p>
    <h2 class="d-l rv">De la primera llamada al primer turno.</h2>
    <div class="pillars pillars--4 stagger rv rv-d1" style="margin-top:var(--sp-7)">
      <article class="pillar"><b>01</b><h3>Visita</h3><p>Un asesor recorre sus instalaciones y levanta lo que hay: superficies, horarios, accesos y las áreas que no pueden fallar.</p></article>
      <article class="pillar"><b>02</b><h3>Propuesta</h3><p>Alcance, plantilla, insumos y costo desglosado. Lo que ve en el papel es lo que llega en la factura.</p></article>
      <article class="pillar"><b>03</b><h3>Arranque</h3><p>Personal seleccionado, capacitado y con ficha de identificación. Las rutinas quedan por escrito desde el día uno.</p></article>
      <article class="pillar"><b>04</b><h3>Seguimiento</h3><p>Auditoría discreta mensual, reporte de áreas y comprobación de pagos ante IMSS, SAT, INFONAVIT y FONACOT.</p></article>
    </div>
  </div>
</section>

{cta_band("Ocho servicios, un contrato, un solo interlocutor.")}
</main>
''' + footer()


# ─────────────────────────────── PÁGINA: NOSOTROS ───────────────────────────────
def page_nosotros():
    valores = [
      ("Disciplina","Cada tarea se ejecuta con precisión y respeto por los espacios de nuestros clientes."),
      ("Compromiso","Nos hacemos responsables del resultado, no sólo de la actividad."),
      ("Trabajo en equipo","Dentro de la empresa y con el personal de cada cliente."),
      ("Transparencia","Costos, procesos y cumplimiento fiscal a la vista, siempre."),
      ("Honestidad","En cada vínculo que construimos con quienes confían en nosotros."),
      ("Mejora continua","Resiliencia ante los desafíos más exigentes y revisión permanente de lo que hacemos."),
    ]
    val = "\n".join(f'      <div class="value"><b>{t}</b><p>{d}</p></div>' for t, d in valores)
    pilares = [
      ("Personal","Retenemos al 95 % de nuestro equipo. Quien atiende su cuenta el primer mes sigue ahí el año siguiente."),
      ("Experiencia","Veintiocho años ininterrumpidos, especializados en limpieza empresarial y de hangares."),
      ("Calidad","Procedimientos estandarizados y en proceso de certificación ISO 9001."),
      ("Servicio a la medida","Ajustamos alcance, horarios y costo a la exigencia de cada cliente."),
      ("Confidencialidad","Lo que su equipo ve dentro de su empresa no sale de ahí."),
      ("Metodología","Procedimientos aplicables a los sectores comercial, industrial, corporativo y residencial."),
    ]
    pil = "\n".join(f'      <article class="pillar"><b>{i+1:02d}</b><h3>{t}</h3><p>{d}</p></article>'
                    for i, (t, d) in enumerate(pilares))
    return head("Nosotros · ANMIX",
                "Veintiocho años de experiencia en limpieza empresarial y de hangares. Misión, visión, valores y cumplimiento REPSE de ANMIX Servicios S.A. de C.V.") \
        + header("nosotros") + f'''
<main>

<section class="phero" data-px-host>
  <div class="phero__bg"><img data-px="0.12" data-px-scale="0.05" src="assets/img/nosotros-hero.jpg" alt="Personal de ANMIX trabajando dentro de un hangar" fetchpriority="high"></div>
  <div class="phero__veil"></div>
  <div class="phero__in"><div class="wrap wrap--wide">
    <div class="phero__body">
      <h1 class="d-xl rv">Nos contratan<br>para que no se note.</h1>
      <p class="phero__sub rv rv-d1">
        Un servicio de limpieza bien hecho es invisible. Sólo se nota cuando falta.
        Llevamos veintiocho años del lado invisible.
      </p>
    </div>
  </div></div>
</section>

<section class="sec">
  <div class="wrap wrap--wide">
    <div class="split">
      <div>
        <p class="eyebrow rv">Quiénes somos</p>
        <h2 class="d-m rv">Especialistas en limpieza empresarial y de hangares.</h2>
        <p class="lead rv rv-d1" style="margin-top:24px">
          Con 28 años de experiencia ininterrumpida, ajustamos nuestros servicios a su medida,
          exigencias y costos.
        </p>
      </div>
      <div>
        <p class="txt rv rv-d1">
          Nos comprometemos a cumplir con la entera satisfacción de nuestros clientes, con precios
          competitivos que no se logran sacrificando la calidad ni afectando a nuestro personal.
          Esa segunda parte importa: la rotación es el enemigo de este oficio.
        </p>
        <p class="txt rv rv-d2" style="margin-top:20px">
          Nuestra labor se sustenta en la disciplina, el compromiso y la responsabilidad, pilares
          que nos permiten ejecutar cada tarea con precisión y respeto por los espacios de nuestros
          clientes. Valoramos el trabajo en equipo, la transparencia y la honestidad, tanto puertas
          adentro como en cada vínculo que construimos.
        </p>
        <p class="txt rv rv-d3" style="margin-top:20px">
          Cada servicio es una oportunidad para demostrar que la limpieza especializada puede ser
          sinónimo de calidad, confianza y distinción.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--dark" style="padding-block:0">
  <div class="wrap wrap--wide" style="padding-block:var(--sec-y)">
    <div class="mv rv">
      <div class="mv__c">
        <h3>Misión</h3>
        <p>Transformamos cada espacio en un entorno limpio, ordenado y agradable, cuidando cada detalle
        para ofrecer la más alta calidad posible y superar las expectativas de quienes confían en nosotros.</p>
      </div>
      <div class="mv__c">
        <h3>Visión</h3>
        <p>Seguir creciendo sobre la base de 28 años de experiencia, llevando nuestra calidad y compromiso
        a cada rincón de México y siendo referente en soluciones de limpieza profesional.</p>
      </div>
    </div>
  </div>
  <div class="stats">
    <div class="stat"><span class="stat__n" data-count="28" data-suffix="+">28+</span><span class="stat__l">Años de experiencia</span></div>
    <div class="stat"><span class="stat__n" data-count="110">110</span><span class="stat__l">Clientes satisfechos</span></div>
    <div class="stat"><span class="stat__n" data-count="95" data-suffix="%">95%</span><span class="stat__l">Retención de personal</span></div>
    <div class="stat"><span class="stat__n">24/7</span><span class="stat__l">Operación continua</span></div>
    <div class="stat"><span class="stat__n stat__n--w">REPSE</span><span class="stat__l">Empresa registrada</span></div>
  </div>
</section>

<section class="sec">
  <div class="wrap wrap--wide">
    <p class="eyebrow rv">Por qué ANMIX</p>
    <h2 class="d-l rv">Seis razones que se pueden comprobar.</h2>
    <div class="pillars pillars--6 stagger rv rv-d1" style="margin-top:var(--sp-7)">
{pil}
    </div>
  </div>
</section>

<section class="sec sec--bone">
  <div class="wrap wrap--wide">
    <div class="split split--rev">
      <div>
        <p class="eyebrow rv">Cómo trabajamos</p>
        <h2 class="d-m rv">Estos valores tienen consecuencias operativas.</h2>
        <div class="values rv rv-d1" style="grid-template-columns:1fr 1fr">
{val}
        </div>
      </div>
      <div class="split__media rv rv-d1" data-px-host>
        <img data-px="0.1" data-px-scale="0.06" src="assets/img/altura.jpg" alt="Cuadrilla de ANMIX trabajando sobre una cubierta">
      </div>
    </div>
  </div>
</section>

<section class="sec sec--dark">
  <div class="wrap wrap--wide">
    <div class="split">
      <div>
        <p class="eyebrow eyebrow--green rv">Cumplimiento</p>
        <h2 class="d-m rv" style="color:#fff">Empresa registrada ante la Secretaría del Trabajo.</h2>
      </div>
      <div>
        <p class="lead lead--inv rv rv-d1">
          ANMIX forma parte del Registro de Prestadores de Servicios Especializados con el número
          <b style="color:#fff">AR154933</b>. Eso significa que subcontratar con nosotros no le
          traslada un riesgo laboral a su empresa.
        </p>
        <p class="lead lead--inv rv rv-d2" style="margin-top:20px;font-size:1rem">
          Cada mes recibe el reporte de cumplimiento con los pagos comprobados ante IMSS, SAT,
          INFONAVIT y FONACOT, además de la póliza de responsabilidad civil que cubre cualquier
          incidente causado por nuestro personal.
        </p>
        {chips(["REPSE AR154933","IMSS","SAT","INFONAVIT","FONACOT","Certificación DC-3","Póliza de responsabilidad civil"], inv=True)}
      </div>
    </div>
  </div>
</section>

{clientes_band()}

{cta_band("Veintiocho años se dicen rápido. Se demuestran cada turno.", img="assets/img/nosotros-hero.jpg")}
</main>
''' + footer()


# ─────────────────────────────── PÁGINA: CONTACTO ───────────────────────────────
def page_contacto():
    return head("Contacto · ANMIX",
                "Escríbenos, llámanos o mándanos un WhatsApp. Toluca, Estado de México. 722 272 0428 · contacto@anmix.mx") \
        + header("contacto") + f'''
<main>

<section class="phero" data-px-host style="min-height:min(56vh,470px)">
  <div class="phero__bg"><img data-px="0.12" data-px-scale="0.05" src="assets/img/contacto-hero.jpg" alt="" fetchpriority="high"></div>
  <div class="phero__veil"></div>
  <div class="phero__in"><div class="wrap wrap--wide">
    <div class="phero__body">
      <h1 class="d-xl rv">Hablemos.</h1>
      <p class="phero__sub rv rv-d1">
        Escríbanos, llámenos o mándenos un WhatsApp. Respondemos el mismo día hábil.
      </p>
    </div>
  </div></div>
</section>

<section class="sec">
  <div class="wrap wrap--wide">
    <div class="cinfo stagger rv">
      <div class="cinfo__i">
        <i style="--ic:{ic('tel')}"></i>
        <b>Teléfono y WhatsApp</b>
        <a href="tel:+527222720428">722 272 0428</a>
        <a href="https://wa.me/527227910294">WhatsApp 722 791 0294</a>
      </div>
      <div class="cinfo__i">
        <i style="--ic:{ic('mail')}"></i>
        <b>Correo</b>
        <a href="mailto:contacto@anmix.mx">contacto@anmix.mx</a>
        <p style="color:var(--g500);font-size:.88rem;margin-top:6px">Para licitaciones y compras, escriba directo aquí.</p>
      </div>
      <div class="cinfo__i">
        <i style="--ic:{ic('pin')}"></i>
        <b>Oficinas</b>
        <p>Calle Sor Juana Inés de la Cruz No. 2, 1er Nivel, Interior 2, C.P. 50210, Toluca, Estado de México.</p>
        <p style="color:var(--g500);font-size:.88rem;margin-top:6px">Entre Calle Morelos y Vía José López Portillo, a cinco minutos de la Villa Charra.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec cta" id="cotizar" style="padding-top:0">
  <div class="wrap wrap--wide">
    <div class="cta__grid">
      <div>
        <p class="eyebrow rv">Cotización</p>
        <h2 class="d-m rv">Cuéntenos qué necesita.</h2>
        <p class="txt rv rv-d1" style="margin-top:20px">
          Un asesor recorre sus instalaciones, levanta el requerimiento y le entrega una propuesta
          con alcance y costo desglosado. <b>La visita y la propuesta no tienen costo.</b>
        </p>
        <p class="txt rv rv-d2" style="margin-top:20px">
          Si prefiere hablarlo, llámenos al <a href="tel:+527222720428" style="color:var(--verde-hondo)">722 272 0428</a>
          o escríbanos por <a href="https://wa.me/527227910294" style="color:var(--verde-hondo)">WhatsApp</a>.
        </p>
        {chips(["Visita en sitio","Propuesta desglosada","Respuesta el mismo día"])}
      </div>
      {form()}
    </div>
  </div>
</section>

<section class="mapa" aria-label="Ubicación de ANMIX en Toluca">
  <iframe title="Mapa de ubicación de ANMIX" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
    src="https://www.google.com/maps?q=Sor%20Juana%20In%C3%A9s%20de%20la%20Cruz%202%2C%2050210%20Toluca%2C%20M%C3%A9xico&output=embed"></iframe>
</section>

{clientes_band()}
</main>
''' + footer()


# ─────────────────────────────── ESCRITURA ───────────────────────────────
if __name__ == "__main__":
    written = []
    for s in SERV:
        p = f'{OUT}/servicio-{s["slug"]}.html'
        open(p, "w", encoding="utf-8").write(page_servicio(s)); written.append(p)
    for name, fn in (("servicios", page_servicios), ("nosotros", page_nosotros), ("contacto", page_contacto)):
        p = f"{OUT}/{name}.html"
        open(p, "w", encoding="utf-8").write(fn()); written.append(p)
    for p in written:
        print(f"{os.path.getsize(p)//1024:>4} KB  {p}")
