# Menú de configuración

El **menú de configuración** está dividido en varias secciones, que se describen a continuación.

## Configuración general

![Sección general del menú de configuración](../assets/v7/settings/ui-settings.png){.center}

#### Mostrar exif

Muestra los metadatos de la imagen actual en el [área principal del espacio de trabajo](./Screen-layout.md#espacio-de-trabajo-principal).

#### Mostrar iconos del espacio de trabajo

Habilita un conjunto de funciones en el [área principal del espacio de trabajo](./Screen-layout.md#espacio-de-trabajo-principal). Obtenga más información sobre estas funciones en la [siguiente sección](./Workspace_icons.md).

#### Señalización automática

Por defecto, el software numera cada error después de la inspección. Al deshabilitar esta opción, solo se resalta en color el área afectada, sin número.

#### Color de la máscara

Esta opción le permite cambiar el color del error marcado. Cuando el color del error marcado coincide con el color de la PCBA, es recomendable cambiarlo a un color de mayor contraste para hacer las áreas marcadas más visibles.

#### Idioma

Cambia el idioma de la interfaz. Los idiomas disponibles actualmente son: **inglés, francés, alemán, italiano y español**.

## Opciones de flujo de trabajo

![Sección de flujo de trabajo del menú de configuración](../assets/v7/settings/workflow-settings.png){.center}

#### Usar código de barras

Activa o desactiva la [función de lectura de código de barras](../features/Barcode_reader.md).

#### Mostrar ventana emergente de errores

Al deshabilitar esta opción, la ventana de reporte ya no aparecerá al reportar un error con las flechas **ARRIBA** o **ABAJO**. Los errores reportados se generarán con la etiqueta "**other**" en el informe PDF final.

#### Mostrar mosaico de referencias

Al deshabilitar esta opción, el menú de mosaico no aparecerá después de tomar una imagen de **REFERENCIA**.

#### Modo operador

Habilitar esta opción ocultará varias funciones de la interfaz, simplificando el uso del software. También evita que el operador pueda cambiar la imagen de REFERENCIA o la sensibilidad de las inspecciones. Se puede añadir una [contraseña](#contrasena-de-configuracion) para que solo el administrador pueda deshabilitar esta opción.

#### Sensibilidad habilitada

Permite cambiar la sensibilidad cuando el software está en modo operador.

#### Modo INLINE

Seleccione este modo cuando la AOI esté instalada en una cinta transportadora. Obtenga más información sobre esta funcionalidad en la siguiente sección: [Integración en línea de producción](../maintenance/Conveyor_integration.md)

#### Modo de alineación manual

Habilite esta opción para alinear manualmente las imágenes de REFERENCIA y UUI. Obtenga más información sobre esta funcionalidad en la siguiente sección: [Herramienta de alineación manual](../features/Manual_alignment.md)

#### Recordar sensibilidad

Al activar esta opción, el software mantendrá la sensibilidad de inspección configurada después de realizar una nueva inspección.

#### Revisión obligatoria de errores

Si esta opción está habilitada, el software no continuará inspeccionando nuevos paneles hasta que todos los errores detectados en la inspección actual hayan sido [reportados](Inspection_workflow.md#reporte-de-errores) como errores o falsos positivos.

## Opciones de informe

![Sección de informe del menú de configuración](../assets/v7/settings/reports-settings.png){.center}

#### ID del operador

Establece un ID para el operador actual. Este ID se mostrará en el informe PDF final después de completar la inspección.

#### ID de pedido

Establece un ID para la orden de fabricación actual. Este ID se mostrará en el informe PDF final después de completar la inspección.

#### ID de plataforma

Establece un ID para la AOI.

#### Usar ETIQUETA como

Establece la ETIQUETA (OK o NOK) del informe PDF final como **sufijo** o **prefijo** del nombre del archivo.

#### ETIQUETA OK

Establece una ETIQUETA OK personalizada para el informe PDF final.

#### ETIQUETA NO OK

Establece una ETIQUETA NO OK personalizada para el informe PDF final.

#### Informe automático

Cuando esta opción está habilitada, se generará automáticamente un informe PDF final etiquetado como OK si no se detectan errores después de la inspección. El informe PDF final también se puede generar si se detecta algún error durante la inspección.

!!! note "Nota"
    Al generar un informe PDF automáticamente, todos los errores detectados se marcarán con la etiqueta "unknown".

#### Mostrar todos los fallos

Muestra todos los errores detectados en el informe PDF incluso si el operador no los ha reportado.

#### Crear informe JSON

Genera un **archivo JSON legible por máquina** con los datos de la inspección, además del informe PDF. Utilice esta opción cuando los resultados tengan que ser procesados por otro sistema —un MES, un ERP o una base de datos de trazabilidad— en lugar de ser leídos por una persona.

El archivo JSON se escribe en la misma carpeta que el informe PDF, dentro del directorio [PCB OUT](#pcb-out).

!!! note "Nota"
    Esta es una función con licencia. Si la opción no genera ningún archivo, contacte con [support@agnospcb.com](mailto:support@agnospcb.com) para comprobar si su perfil de cuenta la incluye.

#### Crear informe de BAJA RESOLUCIÓN

Genera un **informe PDF adicional con un tamaño de archivo reducido**. El informe estándar se sigue generando: esta opción añade una copia más ligera, no lo sustituye.

Resulta útil cuando los informes deben enviarse por correo electrónico, archivarse a largo plazo o transferirse a través de una conexión lenta o limitada, donde las imágenes a resolución completa harían que el archivo fuera excesivamente grande.

#### Logotipo

Establece un logotipo para el informe PDF.

## Opciones de fecha/hora

![Sección de fecha del menú de configuración](../assets/v7/settings/date-settings.png){.center}

#### Zona horaria

Establece la zona horaria.

#### Fecha y hora

Establece el día y la hora.

!!! note "Nota"
    Para aplicar los cambios, presione el botón **SET** y reinicie el sistema.

## Opción de ruta

![Sección de ruta del menú de configuración](../assets/v7/settings/path-settings.png){.center}

#### PCB OUT

Cambia la ruta donde se generan las inspecciones.

## Opciones de compartir

![Sección de compartir del menú de configuración](../assets/v7/settings/network-settings.png){.center}

#### Compartir carpetas

Al habilitar estas opciones, el sistema compartirá automáticamente las carpetas PCB_OUT y REFERENCE en su red local. La dirección de acceso se mostrará una vez establecida la opción.

!!! note "Nota"
    Para aplicar los cambios, presione el botón **Apply**.

!!! note "Nota"
    Para las unidades OFFLINE, si necesita cambiar la interfaz de red de su unidad, consulte el [artículo de configuración de red](../maintenance/network_configuration.md).

## Usuarios

![Sección de usuarios del menú de configuración](../assets/v7/settings/users-settings.png){.center}

Esta pestaña solo está disponible para los usuarios con rol de **admin**. Permite crear las cuentas que pueden operar la AOI, cada una con un rol de **admin** u **operator**, y exigir un nombre de usuario y una contraseña cada vez que se inicia el software.

Para habilitar **Enable user access control** debe existir al menos una cuenta **admin** activa.

Obtenga más información sobre esta funcionalidad en la siguiente sección: [Control de acceso de usuarios](../features/User_control.md)

## Secuencias

![Sección de secuencias del menú de configuración](../assets/v7/custom_sequences/sequences.png){.center}

Esta pestaña solo está disponible para los usuarios con rol de **admin**. Permite definir sus propias **secuencias de captura**, es decir, la cuadrícula de fotografías que la cámara toma y une para componer la imagen de una placa grande.

Utilícela cuando ninguna de las secuencias predefinidas se ajuste correctamente a su placa. Las secuencias que guarde aquí aparecerán como opciones **CUSTOM** en la ventana de vista en vivo al tomar una REFERENCIA o al iniciar una inspección.

Obtenga más información sobre esta funcionalidad en la siguiente sección: [Secuencias de captura personalizadas](../features/Custom_sequences.md)

!!! note "Nota"
    Esta pestaña no se muestra en las unidades configuradas en **modo Q1**, que solo realizan una única captura.

## Máquina

![Sección de máquina del menú de configuración](../assets/v7/settings/machine-settings.png){.center}

Esta pestaña solo está disponible para los usuarios con rol de **admin**. Muestra los parámetros de hardware de su unidad, almacenados en el archivo **machine.json**.

La mayoría de los valores se muestran atenuados: son **solo informativos** y no se pueden modificar. Los campos resaltados en azul son los editables:

| Campo | Descripción |
| --- | --- |
| **xacc** / **yacc** / **zacc** | Aceleración de cada eje. |
| **xhome** / **yhome** / **zhome** | Desplazamiento de la posición de origen de cada eje. |
| **capture_gain** | Ganancia de la cámara durante la captura. |
| **exposure** | Tiempo de exposición de la cámara. |

Presione **Save changes** para aplicar los nuevos valores, o **Reset to factory default** para restaurar todos los parámetros a su valor original.

!!! warning "Importante"
    Estos parámetros afectan al movimiento de la plataforma y a la captura de las imágenes. Modificarlos incorrectamente puede degradar la calidad de imagen o el movimiento de los ejes. Cámbielos únicamente cuando [soporte](mailto:support@agnospcb.com) se lo indique.

!!! note "Nota"
    Esta pestaña no se muestra en las unidades sin plataforma XYZ.

## Depuración

![Sección de depuración del menú de configuración](../assets/v7/settings/debug-settings.png){.center}

Esta pestaña solo está disponible para los usuarios con rol de **admin**. Genera un **informe de diagnóstico** que permite a nuestro equipo de soporte analizar el comportamiento de su unidad.

Para generarlo:

1. Coloque la **placa de calibración** en el centro del área de inspección. Si no dispone de ella, utilice una placa de muestra **menor de 20x20 cm**.
2. Presione **Generate DEBUG report**.
3. Espere hasta que la barra de progreso se complete. El área de texto inferior muestra el progreso del proceso.
4. Recopile los archivos generados y envíelos a [support@agnospcb.com](mailto:support@agnospcb.com).

## Sección de información

![Sección de información del menú de configuración](../assets/v7/ui-settings-info.png){width=650px .center}

#### Información AOI

La información de la AOI se muestra en esta sección.

#### Copia de seguridad

Esta función genera automáticamente un archivo comprimido de copia de seguridad de la carpeta **PCB_OUT**. El archivo de copia de seguridad se almacena en la carpeta **APP/BACKUP**.

#### Contraseña de configuración

Establece una contraseña para acceder al menú de configuración.

!!! note "Nota"
    Establezca la contraseña en blanco para deshabilitar el requisito de contraseña.
