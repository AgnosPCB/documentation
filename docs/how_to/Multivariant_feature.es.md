# Variantes de Referencia

Al inspeccionar un PCB, algunos componentes pueden diferir de la referencia y ser detectados por el software como errores (por ejemplo, debido a cambios en el suministro de componentes o diferencias en el etiquetado).

Al marcar este tipo de error como una **Variante de Referencia**, el sistema lo reconocerá en futuras inspecciones y no lo volverá a señalar como error.

## Video

Para una explicación completa de esta funcionalidad, vea el siguiente video:

<video width="800" controls style="display: block; margin: 0 auto;">
  <source src="../assets/ref-variant-video.mp4" type="video/mp4">
  Su navegador no soporta la etiqueta de video.
</video>

## 1. Iniciar la inspección

[Cree una imagen de referencia](../how_to/Inspection_workflow.md#generating-a-reference) o seleccione una [del repositorio](../how_to/Screen-layout.md#load-reference-as-file). Luego, coloque el UUI e inicie la inspección.

## 2. Identificar el error

Navegue hasta el error detectado con las **teclas de flecha izquierda/derecha (←/→)**.

![Error de variante detectado](../assets/ref-variant-error.png){ width=600 .center }

## 3. Clasificar como Variante de Referencia

Presione la **tecla de flecha abajo (↓)** para rechazar el error. En el panel de clasificación, seleccione **Reference variant**.

Aparecerá un cuadro de diálogo donde debe introducir un nombre para la nueva variante (obligatorio) y, opcionalmente, añadir una descripción. Una vez completado, presione **Confirm**.

![Panel de clasificación](../assets/ref-variant-label.png){ width=400 .center }

## Resultado

Una vez clasificada, la variante de referencia se almacena y se vincula a la imagen de referencia. Las variantes guardadas pueden visualizarse abriendo una imagen de referencia almacenada. Se muestran en el panel derecho, debajo de la vista ampliada de la referencia. Desde este panel, las variantes pueden activarse, desactivarse o eliminarse.

![Variante de referencia almacenada](../assets/ref-variant-stored.png){ width=600 .center }

Esta variante ya no se marcará como error en futuras inspecciones.

!!! warning "Precaución"
    Se debe crear manualmente una variante de referencia para cada ubicación en el PCB donde aparezca la variación. El sistema no aplica automáticamente la variante a componentes idénticos en otras posiciones.

![Error de variante detectado](../assets/ref-variant-error.png){ width=400 .center }
![Flecha verde](../assets/green-arrow-down.png){ width=40 .center }
![Variante de referencia](../assets/ref-variant-solved.png){ width=400 .center }

Incluso después de crear una variante de referencia, el sistema seguirá detectando defectos reales en ese componente si se producen.

El informe final de inspección también incluirá la variante de referencia, junto con su imagen, nombre asignado y cualquier observación adicional.

![Reference variant PDF report](../assets/ref-variant-report.png){width=600, .center}