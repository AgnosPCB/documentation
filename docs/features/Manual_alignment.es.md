# Alineación manual de imágenes

Cuando las imágenes de REFERENCIA y UUI necesitan alinearse con más precisión de la que permite la alineación automática, el software de AgnosPCB incluye una herramienta de alineación manual que mejora la exactitud de la inspección.

## 1. Habilitar la alineación manual

!!! info "Nota"
    Esta función solo está disponible para inspecciones de **imágenes 1x1**.

Al capturar una nueva imagen UUI, active la alineación manual desde el menú de configuración.

![Opción de alineación manual](../assets/v7/manual_align/1-manual-alignment-option.png){.center}

Después, durante la captura de la imagen UUI, active la opción de alineación manual.

![Opción de alineación manual](../assets/v7/manual_align/manual-aling-button.png){.center}

## 2. Alinear las imágenes

Justo después de capturar la imagen UUI, aparece la ventana de alineación manual mostrando las imágenes de REFERENCIA y UUI.

![Ventana de alineación manual](../assets/v7/manual_align/2-MA-zoom.png){.center}

Marque ahora tres puntos de referencia en la imagen de REFERENCIA.

!!! warning "Importante"
    Elija puntos fáciles de reproducir de un panel a otro (taladros, pads, etc.), cercanos a las esquinas del panel y lo más separados entre sí que sea posible.

!!! note "Nota"
    Utilice la rueda del ratón para ampliar la imagen y marcar los puntos con mayor precisión.

![Marcado del primer punto](../assets/v7/manual_align/3-MA-P1.png){.center}

![Marcado del segundo punto](../assets/v7/manual_align/4-MA-P2.png){.center}

![Marcado del tercer punto](../assets/v7/manual_align/5-MA-P3.png){.center}

Una vez definidos los tres puntos de alineación en la imagen de REFERENCIA, marque **los mismos tres puntos** en la imagen UUI.

!!! warning "Importante"
    Para garantizar una alineación correcta, coloque cada punto exactamente sobre el mismo detalle del panel que en la imagen de REFERENCIA.

![Marcado del primer punto](../assets/v7/manual_align/6-MA-UUI-P1.png){.center}

![Marcado del segundo punto](../assets/v7/manual_align/7-MA-UUI-P2.png){.center}

![Marcado del tercer punto](../assets/v7/manual_align/8-MA-UUI-P3.png){.center}

Una vez colocados todos los puntos de alineación, presione el botón **ALIGN** para iniciar el proceso. El software alinea ambas imágenes y a continuación realiza la inspección.

![Imágenes alineadas](../assets/v7/manual_align/MA-final.png){.center}
