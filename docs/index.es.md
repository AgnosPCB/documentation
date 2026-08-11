---
hide:
  - navigation
---

<div class="agnos-hero" markdown>

![AgnosPCB](assets/agnospcb-logo.gif)

# Documentación de AgnosPCB

<p class="agnos-hero-tagline">
<strong>Inspección Óptica Automatizada (AOI)</strong> asequible, impulsada por
tecnología de <strong>Red Neuronal</strong>. Aquí encontrará todo lo necesario para
desembalar, configurar y dominar su sistema de inspección.
</p>

<div class="agnos-hero-actions" markdown>
[Primeros pasos :octicons-arrow-right-24:](getting_started/Package_content.md){ .md-button .md-button--primary }
[Cómo usarlo](how_to/Screen-layout.md){ .md-button }
</div>

</div>

<div class="agnos-highlights" markdown>

<div markdown>
<span class="agnos-highlight-icon">:material-brain:</span>
**Inspección neuronal**
<p>Los defectos se detectan comparando cada placa con una REFERENCIA entrenada.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-clock-fast:</span>
**Puesta en marcha rápida**
<p>Del desembalaje a su primera inspección sin programar ningún test.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-file-chart-outline:</span>
**Informes trazables**
<p>Cada inspección genera un informe que puede archivar, compartir y auditar.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-tools:</span>
**Herramientas adicionales**
<p>Lectura de códigos de barras, inspección UV, medición y mucho más.</p>
</div>

</div>

## ¿Por dónde quiere empezar?

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } **Primeros pasos**

    ---

    Desembale su máquina, compruebe qué ha recibido y conecte todo por primera vez.

    * [Contenido del paquete](getting_started/Package_content.md) — qué debería haber recibido
    * [Guía de desembalaje](getting_started/Unboxing.md) — montaje paso a paso
    * [Guía de conexión](getting_started/Connection_guide.md) — cables, alimentación y cámara

    [:octicons-arrow-right-24: Empiece aquí](getting_started/Package_content.md)

-   :material-monitor-dashboard:{ .lg .middle } **Cómo usar el software**

    ---

    Aprenda la interfaz y realice inspecciones, desde lo básico hasta las opciones
    avanzadas.

    * [Terminología](how_to/terminology.md) — REFERENCIA, UUI, inferencia, falso positivo…
    * [Interfaz de usuario](how_to/Screen-layout.md) — distribución de la pantalla y áreas de trabajo
    * [Flujo de trabajo de inspección](how_to/Inspection_workflow.md) — el procedimiento completo
    * [Menú de configuración](how_to/Settings_menu.md) — opciones de interfaz, flujo de trabajo e informes

    [:octicons-arrow-right-24: Aprenda el software](how_to/Screen-layout.md)

-   :material-wrench-outline:{ .lg .middle } **Soporte y mantenimiento**

    ---

    Mantenga el sistema a punto y resuelva incidencias cuando algo no funcione
    como espera.

    * [Mantenimiento](maintenance/maintenance.md) — correas, limpieza y lubricación
    * [Actualizar software](maintenance/update_software.md) — mantenga su ordenador AOI al día
    * [Configuración de red](maintenance/network_configuration.md) — configuración de la interfaz de red
    * [Solución de problemas](maintenance/Troubleshooting.md) — problemas habituales y sus soluciones

    [:octicons-arrow-right-24: Obtenga soporte](maintenance/Troubleshooting.md)

-   :material-lightbulb-on-outline:{ .lg .middle } **Información adicional**

    ---

    Respuestas rápidas y consejos prácticos recogidos de usuarios reales.

    * [Preguntas frecuentes](help/FAQ.md) — respuestas a las consultas más comunes
    * [Consejos](help/Tips.md) — cómo obtener una buena REFERENCIA y una buena inspección

    [:octicons-arrow-right-24: Lea las FAQ](help/FAQ.md)

</div>

## Su primera inspección en cuatro pasos

1. **Prepare la máquina.** Siga la [guía de desembalaje](getting_started/Unboxing.md) y la
   [guía de conexión](getting_started/Connection_guide.md) para montar y alimentar el sistema.
2. **Aprenda el vocabulario.** Una lectura rápida de la página de
   [terminología](how_to/terminology.md) hace que el resto de guías sean mucho más fáciles de seguir.
3. **Cree una REFERENCIA.** Capture una placa correcta conocida — consulte los
   [consejos](help/Tips.md) para obtener una imagen limpia, o convierta una placa ya inspeccionada con
   [UUI a REFERENCIA](how_to/UUI_to_REFERENCE.md).
4. **Inspeccione y genere el informe.** Ejecute el
   [flujo de trabajo de inspección](how_to/Inspection_workflow.md) y genere su informe.

!!! tip "¿No obtiene los resultados esperados?"

    La mayoría de los problemas de detección se reducen a dos ajustes: la
    [sensibilidad](how_to/Set_sensitivity.md) y las
    [áreas de exclusión](how_to/Set_exclusion_area.md) de su REFERENCIA.

## Herramientas y funciones

<div class="grid cards agnos-features" markdown>

-   :material-barcode-scan:{ .lg .middle } **[Lector de código de barras](features/Barcode_reader.md)**

    ---

    Cargue una REFERENCIA automáticamente escaneando el código de barras de la placa.

-   :material-select-off:{ .lg .middle } **[Área de exclusión](how_to/Set_exclusion_area.md)**

    ---

    Ignore las zonas que cambian legítimamente de una placa a otra.

-   :material-tune-vertical:{ .lg .middle } **[Sensibilidad](how_to/Set_sensitivity.md)**

    ---

    Equilibre la detección de defectos frente a los falsos positivos.

-   :material-file-replace-outline:{ .lg .middle } **[UUI a REFERENCIA](how_to/UUI_to_REFERENCE.md)**

    ---

    Convierta una placa inspeccionada en la nueva REFERENCIA.

-   :material-cursor-default-click-outline:{ .lg .middle } **[Iconos del espacio de trabajo](how_to/Workspace_icons.md)**

    ---

    Controles de cruces, auto proceso y color de la máscara de errores.

-   :material-lightbulb-fluorescent-tube-outline:{ .lg .middle } **[Inspección de recubrimiento UV](features/UV_conformal_coating_inspection.md)**

    ---

    Inspeccione el recubrimiento conformal bajo iluminación UV.

-   :material-content-duplicate:{ .lg .middle } **[Variantes de referencia](features/Multivariant_feature.md)**

    ---

    Acepte varias versiones válidas de la misma placa.

-   :material-ruler:{ .lg .middle } **[Herramienta de medición](features/Measurement_tool.md)**

    ---

    Mida distancias directamente sobre la imagen capturada.

-   :material-vector-arrange-above:{ .lg .middle } **[Alineación manual](features/Manual_alignment.md)**

    ---

    Alinee manualmente la REFERENCIA y la UUI cuando sea necesario.

</div>

## ¿Necesita ayuda?

<div class="grid cards" markdown>

-   :material-email-fast-outline:{ .lg .middle } **Contacte con soporte**

    ---

    Nuestro equipo responde a consultas técnicas y ayuda con incidencias de hardware.

    [:octicons-arrow-right-24: support@agnospcb.com](mailto:support@agnospcb.com)

-   :material-web:{ .lg .middle } **Visite nuestra web**

    ---

    Información del producto, precios y novedades sobre el sistema AOI de AgnosPCB.

    [:octicons-arrow-right-24: agnospcb.com](https://agnospcb.com/)

</div>
