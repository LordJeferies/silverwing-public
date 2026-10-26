# Silverwing — brief y continuidad de producto

Actualizado: 2026-10-26. Este documento registra los requisitos nuevos del propietario; **su incorporación a GitHub no significa que las funciones estén implementadas**.

## Alcance de esta actualización

Solo documentación y continuidad. No se ejecuta ahora el rediseño completo ni se generan imágenes. El propietario pidió preservar el límite de cinco horas. Trabajar en entregas pequeñas y verificables, sin consumir toda la ventana en una reconstrucción de alcance abierto.

## Destinos actuales

- Comercial: https://lordjeferies.github.io/silverwing-public/
- Studio beta: https://lordjeferies.github.io/silverwing-studio/
- Inner Circle: https://lordjeferies.github.io/silverwing-public/inner-circle.html
- Figma: https://www.figma.com/design/xvKL2Xndsi0px6F8I5BdJf
- El repositorio privado original se conserva sin modificar y no es destino de despliegue.

Los dos repositorios públicos se confirmaron mediante el conector de GitHub. La portada comercial se abrió en el navegador integrado y mostró contenido de Silverwing, incluido el cambio de escena a Andes. Eso confirma acceso a la portada, no una auditoría de todas las rutas, dispositivos, acciones o cachés. En este turno no se verificaron de extremo a extremo Studio, Inner Circle, Actions ni los commits servidos por Pages.

## Información nueva que debe conservarse

- Emblema: águila arpía latinoamericana (Harpia harpyja), frontal en vuelo hacia el observador, alas extendidas y garras abiertas. El arte abstracto anterior no debe considerarse la identidad final aprobada.
- Paisajes latinoamericanos: Andes, Amazonía, bosques nubosos y Patagonia. Identidad plata, azul nocturno/hielo y grafito con luz cálida discreta.
- Diseño coherente y componentes consolidados; evitar seguir acumulando parches de CSS. Las referencias orientan calidad, narrativa y acabado, sin copiar imágenes, código propietario o identidad de terceros.
- ES/EN centralizado para la experiencia completa, incluidos textos dinámicos y propuestas; no basta una traducción parcial del DOM.
- Inner Circle independiente con entregas, calendario, enlaces y recompensas propuestas; toda métrica de demo debe identificarse como ilustrativa. No deducir métricas reales de una URL.
- Studio como academia y centro de decisiones: explicar recomendaciones, riesgos, cambios de alcance y capacidad. No publicar costos reales, notas o información confidencial.
- Catálogo único aprobado: separar simulación, aprobación y publicación. La sincronización GitHub requiere un flujo autenticado o un paso manual explícito; no insertar tokens en la web.
- Playground visual aislado de tarifas y datos operativos.
- Revisar PWA, service worker, caché y actualización de versiones antes de atribuir diferencias a un fallo de despliegue.
- Figma editable como apoyo, con implementación y verificación reales en Pages como evidencia de entrega.

## Reglas comerciales invariantes

USD por ciclos de cuatro semanas: Stay Present $399/12 piezas; Daily Authority $799/28; Maximum Visibility $999/64. Material propio incluido, Guided +$500/hasta 8 guiones, Interview +$1.000/hasta 2 entrevistas remotas. Clean incluido; Dynamic +$199 y Cinematic +$399 mejoran 4 Reels seleccionados. Inner Circle incluido con el plan activo, sujeto a disponibilidad real. Sin promesas de viralidad, leads garantizados o gestión publicitaria incluida.

## Entregas acotadas

| Orden | Entrega | Condición para marcarla terminada |
|---|---|---|
| 1 | Auditoría del estado actual | Commits/Pages/Actions/cachés identificados y fallos priorizados con evidencia |
| 2 | Correcciones funcionales y responsive | Flujos afectados probados y versión servida comprobada |
| 3 | Identidad y sistema visual | Arpía y assets legítimos, componentes/tokens coherentes y legibles |
| 4 | ES/EN completo | Navegación, formularios, validaciones, dinámicos y propuestas traducidos |
| 5 | Inner Circle beta | Demo funcional con estados claros y datos simulados identificados |
| 6 | Catálogo aprobado | Simulación separada de aprobación y publicación; autenticación o acción manual documentada |
| 7 | Playground/PWA/Figma | Laboratorio aislado, caché/versionado probado y diseño alineado según acceso |

Antes de empezar una entrega: comprobar qué ya existe. Elegir un único bloque, completar y probarlo, actualizar estado y detenerse antes de ampliar alcance. No repetir pruebas de áreas sin cambios salvo que haya una dependencia real. No existe una garantía de gasto exacto de la ventana: la cuota es compartida y depende del trabajo.

## Estado de esta incorporación

- Hecho: lectura completa del brief; contraste de destinos actuales; conservación de este contexto y requisitos en GitHub.
- No afirmado como hecho: rediseño completo, cobertura total ES/EN, demo ampliada de Inner Circle, sincronización autenticada, auditoría WCAG completa, PWA corregida, cuatro anchos probados o Figma actualizado con esta nueva identidad.
- No se modifican código, catálogo, visibilidad, configuración Pages ni el sitio privado de Sites en esta actualización documental.

## Protocolo para futuras sesiones

Leer README y este documento; consultar el historial y el estado actual del repositorio antes de editar. Añadir en cada entrega: fecha, objetivo, archivos afectados, commit, URL, pruebas reales, limitaciones y próximo paso. Conservar las diferencias entre requisito, demo, simulación y función verificada. Mantener esta documentación alineada entre comercial y Studio sin publicar datos internos. El brief completo sigue debajo como referencia; no es autorización para consumir la ventana entera ni ejecutar todos los apartados en una sola sesión.

---

# Brief completo aportado por el propietario

# CODEX — SILVERWING COMPLETE PRODUCT & DESIGN OVERHAUL

## MISIÓN PRINCIPAL

Actúa como **Senior Product Designer, Apple-level UI/UX Engineer, Creative Director, Frontend Architect y QA Engineer**.

Necesito que audites, reconstruyas, mejores y publiques dos experiencias web de **Silverwing — Powered by Abraxas**, con un nivel de diseño, interacción, estructura y calidad comparable al de las webs de MotionVFX y Apple MacBook Pro, manteniendo una identidad propia.

**No quiero más parches de CSS ni modificaciones que solo cambien un banner. Necesito un rediseño coherente, integral, funcional, responsive y verificado en navegador.**

Tienes autorización para editar y publicar en los repositorios públicos de Silverwing indicados más abajo, pero no para modificar el repositorio privado original ni publicar datos confidenciales.

## 1. REPOSITORIOS Y ENLACES

**Web comercial / Client Experience**

- Repositorio: `LordJeferies/silverwing-public`
- Web: https://lordjeferies.github.io/silverwing-public/

**Business Studio — beta**

- Repositorio: `LordJeferies/silverwing-studio`
- Web: https://lordjeferies.github.io/silverwing-studio/

**Inner Circle — explicación pública**

- URL actual: https://lordjeferies.github.io/silverwing-public/inner-circle.html

**Diseño editable**

- Figma: https://www.figma.com/design/xvKL2Xndsi0px6F8I5BdJf

**Repositorio privado original: `LordJeferies/silverwingabraxas`**

NO modificarlo, publicarlo ni utilizarlo como destino del despliegue.

## 2. PRIMER PASO OBLIGATORIO: AUDITORÍA REAL

Antes de modificar el diseño:

1. Clona o abre ambos repositorios públicos.
2. Revisa la estructura completa, CSS, JavaScript, imágenes, rutas, manifiestos PWA y archivos de configuración.
3. Comprueba que los commits de GitHub realmente están llegando a GitHub Pages.
4. Abre las URLs reales en un navegador con herramientas de desarrollo.
5. Toma capturas de pantalla de todas las secciones en escritorio, tablet y móvil.
6. Identifica problemas de responsive, contraste, espaciado, interacción, legibilidad, rendimiento, accesibilidad y errores de consola.
7. Comprueba si hay service workers o cachés que mantienen una versión antigua.
8. Comprueba la configuración y los resultados de GitHub Actions y del despliegue de Pages.

**Necesito evidencia de que los cambios se ven en producción. No es suficiente hacer commit o comprobar que el HTML contiene una clase CSS.**

Si existe deuda técnica importante, refactoriza y consolida componentes y estilos en lugar de seguir acumulando reglas contradictorias.

## 3. REFERENCIAS VISUALES OBLIGATORIAS

Estudia las páginas reales:

- https://www.motionvfx.com/
- https://www.apple.com/macbook-pro/
- https://developer.apple.com/design/human-interface-guidelines/

Utiliza sus principios de:

- Storytelling cinematográfico.
- Jerarquía tipográfica.
- Navegación premium.
- Presentación visual de productos y servicios.
- Secciones inmersivas con fotografías y videos.
- Animaciones vinculadas al scroll.
- Transiciones entre escenas.
- Microinteracciones profesionales.
- Espaciado y alineación.
- Diseño responsive.
- Materiales translúcidos y Liquid Glass.

La página de Apple MacBook Pro es una referencia especial para **la estructura narrativa del producto**: grandes secciones visuales, mensajes breves, jerarquías claras, cambios de ritmo y demostraciones progresivas.

MotionVFX es la referencia para **el acabado visual y la manera de presentar capacidades creativas**.

Queremos un resultado de calidad equivalente, pero NO reutilizar sus imágenes, logotipos, textos, código propietario ni copiar literalmente sus diseños. Construye una interpretación original para Silverwing.

## 4. IDENTIDAD VISUAL DE SILVERWING

El símbolo de Silverwing es un **águila arpía latinoamericana (Harpia harpyja)**.

No es un águila calva ni una escultura abstracta genérica.

**La posición deseada para el emblema principal es un águila arpía vista frontalmente, volando hacia el espectador, con las alas extendidas y las garras abiertas, a punto de capturar una presa.**

Desarrolla un símbolo profesional, escalable y reconocible en tamaños pequeños.

Dirección artística:

- Paisajes épicos latinoamericanos.
- Cordillera de los Andes.
- Amazonía y bosques nubosos.
- Patagonia, montañas, fiordos y glaciares.
- Niebla, profundidad atmosférica, iluminación dramática.
- Fotografía cinematográfica con gradación de color cuidada.
- Plata, azul nocturno, azul hielo, grafito y matices sutiles de luz cálida.
- Liquid Glass sobre ambientes visualmente ricos.
- Alto contraste y elegancia, no saturación excesiva.

### Recursos visuales

Revisa los recursos ya existentes en `assets/`.

Genera o incorpora legítimamente las imágenes adicionales necesarias para crear una experiencia completa. Necesitamos:

- Varios fondos distintos.
- Banners rotativos.
- Fotos para tarjetas.
- Imágenes editoriales.
- Escenas de transición.
- Imágenes que expliquen los servicios.
- Assets para Inner Circle.
- Iconografía personalizada.
- Versiones optimizadas para escritorio y móvil.

No utilices URLs temporales de Figma como imágenes de producción. Guarda los recursos optimizados en el repositorio.

No inventes casos de éxito reales: identifica cualquier imagen, trabajo o resultado no real como ejemplo conceptual o demostración.

## 5. LIQUID GLASS — SISTEMA COMPLETO

Liquid Glass debe ser parte del diseño completo y no limitarse a dos tarjetas.

Diseña e implementa componentes consistentes:

- Navbar translúcida.
- Header flotante.
- Menús y submenús.
- Botones principales y secundarios.
- Tarjetas de servicios.
- Configurador de planes.
- Inputs y selectores.
- Tabs y controles segmentados.
- Modales y paneles.
- Estadísticas y dashboards.
- Navegación móvil.
- Paneles de Inner Circle.

Añade reflejos, profundidad, desenfoque, iluminación contextual, bordes sutiles y transiciones cuando tengan sentido.

**Regla imprescindible: ninguna superficie translúcida puede perjudicar la legibilidad.**

Asegura texto legible sobre imágenes claras y oscuras. Utiliza scrims, fondos más opacos o cambios de color donde sea necesario.

Evita el abuso de blur, glow y animaciones que reduzcan el rendimiento o parezcan decorativos sin propósito.

## 6. DIRECTRICES APPLE HIG Y ACCESIBILIDAD

Revisa las recomendaciones actuales de Apple Human Interface Guidelines, adaptándolas apropiadamente a la web.

Implementa:

- Áreas táctiles adecuadas, con referencia mínima de 44 × 44 puntos CSS cuando corresponda.
- Espaciado coherente mediante tokens.
- Separación suficiente entre elementos interactivos.
- Controles alineados y del tamaño correcto.
- Estados hover, focus, pressed, selected y disabled.
- Navegación por teclado.
- Responsive sin overflow horizontal.
- Contraste WCAG AA para texto y controles aplicables.
- `prefers-reduced-motion`.
- `prefers-reduced-transparency` cuando exista soporte.
- Tipografía fluida y legible.
- Safe areas en dispositivos móviles.
- Etiquetas accesibles y estructura semántica.

Crea un sistema de componentes y tokens reutilizable. Evita estilos inline dispersos.

## 7. CLIENT EXPERIENCE — WEB COMERCIAL

La finalidad es que una persona que nunca haya oído hablar de Silverwing pueda:

1. Entender rápidamente qué hacemos.
2. Ver la calidad creativa que podemos ofrecer.
3. Comprender qué problema resolvemos.
4. Explorar nuestras capacidades.
5. Comparar los planes.
6. Configurar un servicio.
7. Ver una propuesta clara con precios.
8. Conocer Inner Circle.
9. Saber qué hacer para contratar o contactar.

Diseña una web con ritmo cinematográfico:

**Hero:** impacto visual, águila arpía, mensaje potente y CTA claro.

**Capacidades:** videos, Reels, carruseles, edición, storytelling, piezas visuales e entrevistas.

**Proceso:** cómo pasamos del conocimiento del cliente al contenido listo para publicar.

**Demostraciones:** ejemplos visuales claramente marcados cuando sean conceptuales.

**Niveles de edición:** Clean, Dynamic y Cinematic, explicados con claridad.

**Planes:** tres opciones comerciales y sus límites.

**Configurador:** selección guiada de volumen, fuente de contenido y acabado.

**Inner Circle:** introducción y enlace a la experiencia explicativa independiente.

**Contacto y propuesta:** una acción final clara, sin formularios engañosos ni promesas de envíos que todavía no existan.

Quiero transiciones coordinadas, fondos repartidos por toda la página, distintos ritmos visuales y fotografías integradas en el contenido.

No quiero una sucesión interminable de tarjetas iguales.

## 8. INFORMACIÓN COMERCIAL QUE DEBE CONSERVARSE

Ciclos de cuatro semanas:

| Plan | Precio | Piezas |
|---|---:|---:|
| Stay Present | $399 | 12 |
| Daily Authority | $799 | 28 |
| Maximum Visibility | $999 | 64 |

Fuentes de contenido:

- You Record, We Create: incluido.
- We Plan, You Record: +$500, hasta 8 guiones.
- We Interview, We Create: +$1,000, hasta 2 entrevistas remotas.

Acabados:

- Clean & Professional: incluido.
- Dynamic & Engaging: +$199, para 4 Reels seleccionados.
- Cinematic & Premium: +$399, para 4 Reels seleccionados.

Inner Circle está incluido con el plan activo, sujeto a la disponibilidad real de sus beneficios.

No prometer gestión publicitaria, viralidad, leads garantizados ni servicios no incluidos.

Verifica también los desgloses por tipo de pieza y elimina contradicciones entre secciones.

## 9. BUSINESS STUDIO — ACADEMIA Y CENTRO DE OPERACIONES

Business Studio es una herramienta para que el equipo de Silverwing aprenda, comprenda y gestione el negocio.

La prioridad no es mostrar información por mostrarla, sino **enseñar a decidir correctamente**.

Organiza la experiencia alrededor de estas preguntas:

**Qué ofrecemos:** servicios, beneficios, entregables, límites y ejemplos.

**Cómo lo vendemos:** diagnóstico del cliente, objeciones, selección de paquetes y propuestas.

**Cómo lo producimos:** materiales necesarios, proceso, revisiones, plazos y responsables.

**Cuánto cobramos y ganamos:** precios, costos, márgenes, escenarios y capacidad.

### Simulador de clientes

Incluye casos interactivos:

- Médico sin tiempo para grabar.
- Abogado con grabaciones existentes.
- Consultor que necesita guiones.
- Clínica con varios especialistas.
- Podcaster con episodios recurrentes.

Permite cambiar condiciones:

- Disponibilidad de material.
- Número de revisiones.
- Retrasos en aprobaciones.
- Cambios de alcance.
- Volumen.
- Complejidad de edición.
- Fecha inicial.

Muestra recomendaciones razonadas, riesgos, consecuencias de cada decisión y estimaciones de entrega.

No presentes hipótesis de tiempos como garantías contractuales.

### Pricing Lab

Debe permitir:

- Cambiar precios de planes y complementos.
- Simular combinaciones.
- Ver ingresos por pieza.
- Comparar costo y margen.
- Explorar escenarios.
- Restaurar valores.
- Exportar configuraciones.
- Identificar tarifas aprobadas frente a simulaciones.

## 10. SINCRONIZACIÓN STUDIO → GITHUB → CLIENT EXPERIENCE

Queremos una fuente única de información comercial.

El flujo deseado:

1. Editamos tarifas y características en Studio.
2. Visualizamos su impacto.
3. Aprobamos los cambios.
4. El sistema guarda una versión controlada en GitHub.
5. GitHub Actions valida y publica.
6. Client Experience utiliza automáticamente el catálogo aprobado.

Actualmente existe un archivo `catalog.json` en el repositorio público y un exportador de tarifas en Studio.

Revisa y termina esta arquitectura, evitando la duplicación de datos.

**Nunca pongas tokens de GitHub, claves ni costos confidenciales en archivos públicos.**

Si no hay autenticación y backend disponibles, implementa la mejor solución segura posible y documenta exactamente qué acción manual queda pendiente.

## 11. INNER CIRCLE — PÁGINA Y DEMO

La página `inner-circle.html` debe ser una experiencia independiente y elaborada.

Debe explicar:

- Qué es Inner Circle.
- Por qué está incluido.
- Cómo recibe contenido el cliente.
- Cómo puede ver publicaciones pendientes.
- Cómo registra enlaces de publicaciones.
- Cómo se verifican.
- Qué métricas podrá consultar.
- Cómo funcionan los puntos.
- Qué beneficios podrían canjearse.
- Qué está disponible hoy y qué sigue en beta.

La demo debe permitir explorar:

- Entregas.
- Calendario.
- Publicaciones realizadas.
- Publicaciones pendientes.
- Registro de enlaces.
- Rendimiento ilustrativo.
- Programa propuesto de recompensas.

No mostrar estadísticas simuladas como reales.

Las integraciones auténticas con redes sociales requieren APIs y permisos oficiales. No inventar métricas a partir de URLs.

## 12. IDIOMAS ES / EN

Las tres experiencias deben permitir seleccionar:

- Español.
- English.

El cambio debe abarcar **toda la experiencia**, incluyendo:

- Navegación.
- Botones.
- Formularios.
- Validaciones.
- Configuradores.
- Simuladores.
- Propuestas.
- Mensajes de error.
- Textos dinámicos.
- Inner Circle.

Conserva la preferencia al navegar entre páginas.

Si el sistema actual reemplaza textos del DOM de forma parcial o frágil, sustitúyelo por una arquitectura de traducciones centralizada y mantenible.

## 13. PLAYGROUND DE DISEÑO E INTERACCIONES

Crea una sección o ruta de **Silverwing Playground**, disponible como laboratorio de demostración.

Su objetivo es permitirnos probar y comparar:

- Variantes de Liquid Glass.
- Intensidad de blur y transparencia.
- Gradientes e iluminación.
- Parallax.
- Scroll reveals.
- Fondos.
- Animaciones.
- Carruseles.
- Botones.
- Tarjetas.
- Menús.
- Transiciones.

Debe servir para experimentar sin romper la experiencia principal.

Si es posible, permite alternar entre presets visuales y copiar configuraciones de diseño.

El Playground no debe exponer datos internos ni activar cambios comerciales automáticamente.

## 14. PWA Y EXPERIENCIA DE APLICACIÓN

Las experiencias deben sentirse como aplicaciones modernas sin sacrificar la utilidad web.

Revisa:

- Manifest.
- Iconos.
- Service workers.
- Actualizaciones del caché.
- Instalación móvil.
- Navegación interna.
- Modo standalone.
- Estados offline.
- Rendimiento.
- Errores al cambiar de versión.

Elimina cualquier configuración que cause que una versión antigua permanezca visible después del despliegue.

## 15. FIGMA

Si tienes acceso al plugin o integración de Figma:

- Revisa el archivo existente.
- Consolida los nuevos componentes.
- Alinea las pantallas con la implementación web real.
- Crea variantes responsive.
- Incorpora las imágenes originales.
- Mantén textos y controles editables.
- Documenta tokens, espaciado, tipografía, colores y estados.

Figma debe funcionar como referencia de diseño, pero los cambios de producción deben quedar implementados en código y GitHub Pages.

Si no hay acceso, continúa con la implementación y documenta la limitación sin detener todo el trabajo.

## 16. PRUEBAS Y CONTROL DE CALIDAD

Antes de dar por terminado el trabajo, ejecuta pruebas reales con Playwright o una herramienta de navegador equivalente.

Comprueba, como mínimo:

- Vista de escritorio 1440 px.
- Tablet 768 px.
- Móvil 390 px.
- Móvil pequeño 320 px.
- Chrome y WebKit/Safari cuando sea posible.
- Textos legibles.
- Botones sin superposiciones.
- Menús utilizables.
- Enlaces válidos.
- Imágenes cargadas.
- Formularios accesibles.
- Configurador funcionando.
- Precios coherentes.
- Cambio de idiomas.
- Simulaciones.
- Inner Circle.
- Scroll y parallax.
- Preferencias de movimiento reducido.
- Consola sin errores importantes.
- Ausencia de overflow horizontal.
- Caché actualizado después de publicar.

Incluye capturas de antes y después.

Si una prueba falla, corrige el problema y repítela.

## 17. PUBLICACIÓN Y RESULTADO FINAL

Trabaja directamente sobre los repositorios públicos autorizados.

Puedes crear commits y configurar los flujos de despliegue necesarios.

No te detengas después de redactar un plan. Ejecuta las mejoras, prueba y publica todo lo que permitan los accesos disponibles.

Al finalizar, necesito:

1. Enlaces de GitHub Pages.
2. Enlace de la página Inner Circle.
3. Enlace del Playground.
4. Enlace de Figma actualizado, si corresponde.
5. Enlaces de los commits.
6. Capturas de pantalla reales del resultado.
7. Lista breve de mejoras implementadas.
8. Resultados de pruebas funcionales y responsive.
9. Problemas que aún estén pendientes y por qué.
10. Confirmación de que GitHub Pages sirve realmente la versión nueva.

**Criterio de éxito:** Silverwing debe sentirse como un estudio creativo de alto nivel, con una experiencia comparable en sofisticación y claridad a las referencias MotionVFX y Apple, pero con una identidad propia basada en el águila arpía latinoamericana, paisajes cinematográficos, Liquid Glass y una arquitectura funcional para vender, aprender y operar.

No des por terminado el trabajo simplemente porque los commits se hayan realizado. Termínalo cuando los cambios estén verificados en las URLs públicas.
