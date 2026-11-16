# Atajos de teclado

Esta página recoge todos los atajos de teclado disponibles en el **software de inspección AgnosPCB**, junto con las acciones del ratón que se usan para revisar las detecciones.

## Ventana principal

| Tecla | Acción |
| --- | --- |
| ++r++ | [Tomar una imagen de REFERENCIA](Inspection_workflow.md#generacion-de-una-referencia) (abre la vista previa en vivo). |
| ++s++ | [Iniciar una inspección](Inspection_workflow.md#capturando-una-uui) (capturar la UUI). |
| ++tab++ | Cambiar el modo de vista del [espacio de trabajo principal](Screen-layout.md#espacio-de-trabajo-principal) (REFERENCIA / UUI). |
| ++page-up++ | Pasar a la cara **TOP** de la REFERENCIA cargada (solo REFERENCIAS de doble cara). |
| ++page-down++ | Pasar a la cara **BOTTOM** de la REFERENCIA cargada (solo REFERENCIAS de doble cara). |
| ++f1++ … ++f8++ | Cargar la REFERENCIA guardada en esa posición del [mosaico de referencias](Screen-layout.md#mosaico-de-referencias). |
| ++arrow-right++ | Detección siguiente (o fila siguiente de la lista de detecciones con [Preferencia de análisis](Settings_menu.md#preferencia-de-analisis) = **LIST**). |
| ++arrow-left++ | Detección anterior (o fila anterior de la lista de detecciones con Preferencia de análisis = **LIST**). |
| ++arrow-up++ | [Reportar](Inspection_workflow.md#reporte-de-errores) la detección como **error real** (abre la ventana de reporte). En una zona sin detección, reporta un error no detectado por el software. |
| ++arrow-down++ | Reportar la detección como **falso positivo**. |
| ++1++ | [Sensibilidad](Set_sensitivity.md): Normal. |
| ++2++ | Sensibilidad: Alta. |
| ++3++ | Sensibilidad: Muy alta. |
| ++space++ | Encender / apagar la iluminación de la plataforma. |
| ++f++ | Mostrar / ocultar la capa de errores reportados. |
| ++enter++ | Procesar una imagen cargada manualmente. |

!!! note "Nota"
    Con el [control de acceso de usuarios](../features/User_control.md) activado, las teclas ++arrow-up++ y ++arrow-down++ requieren el permiso **Classify detected faults**.

## Revisar detecciones con el ratón

| Acción del ratón (sobre la imagen) | Acción |
| --- | --- |
| Clic izquierdo sobre una detección | Reportarla como **error real** (igual que ++arrow-up++). Sobre una detección ya reportada como error, pide confirmación antes de deshacerlo. |
| Clic derecho sobre una detección | Reportarla como **falso positivo** (igual que ++arrow-down++). |
| Clic izquierdo en una zona vacía | Reportar un error no detectado por el software. |
| Mantener el puntero quieto sobre una detección durante 1 segundo aprox. | Marcarla como **vista**. |
| Clic derecho fuera de una detección | Cambiar la forma de la lupa. |
| ++shift++ + clic derecho | Cambiar la forma de la lupa, también encima de una detección. |
| Rueda del ratón | Cambiar el nivel de zoom. |

Las acciones del ratón en la lista de detecciones (miniaturas, botones, desplazamiento) se describen en [Lista de detecciones](Screen-layout.md#lista-de-detecciones).

## Ventana de reporte

| Tecla | Acción |
| --- | --- |
| ++arrow-up++ / ++arrow-down++ | Recorrer las opciones de la lista desplegable. |
| ++enter++ | Confirmar. |
| ++esc++ | Cancelar. |

## Otras ventanas

| Ventana | Tecla | Acción |
| --- | --- | --- |
| Vista previa en vivo (REFERENCIA / UUI) | ++enter++ | Confirmar / OK. |
| Vista previa en vivo (REFERENCIA / UUI) | ++esc++ | Cancelar. |
| Mosaico de referencias | ++f1++ … ++f8++ | Cargar la REFERENCIA de esa posición. |
| Lista de búsqueda de REFERENCIAS | ++esc++ | Cerrar la ventana sin cargar ninguna REFERENCIA. |
| Inicio de sesión | ++enter++ | Iniciar sesión. |
| Menú de configuración | ++enter++ | OK (guardar y cerrar). |
| Menú de configuración | ++esc++ | Cerrar. |
