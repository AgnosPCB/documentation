# Integración en línea de producción (modo INLINE)

Esta guía explica cómo integrar la **AgnosPCB AI 4050** en una línea de producción
automatizada, de modo que la AOI reciba placas de una cinta transportadora, las
inspeccione sin intervención del operador y devuelva un resultado PASS/FAIL al
controlador de la línea.

La integración consta de dos partes:

1. El **módulo MODBUS**, que conecta la AOI con la cinta transportadora y con el controlador de línea (PLC).
2. El **modo INLINE** del software de inspección, que gestiona el flujo de trabajo desatendido.

!!! warning "Leer antes de empezar"

    La integración en línea implica trabajo eléctrico tanto en la AOI como en el
    controlador de la cinta transportadora. Todo el cableado debe realizarse con
    **ambos sistemas desconectados** y por personal cualificado para trabajar en el
    armario de control de la línea.

---

## Antes de empezar

Compruebe que dispone de lo siguiente:

- Una unidad **AI 4050** ya desembalada, montada y funcionando en modo autónomo.
  Si aún no ha llegado a ese punto, complete primero la
  [guía de desembalaje](../getting_started/Unboxing.md) y la [guía de conexión](../getting_started/Connection_guide.md).
- Una imagen de **REFERENCIA** ya capturada y validada para cada producto que
  procesará la línea. El modo INLINE inspecciona contra REFERENCIAS existentes:
  no puede crearlas.
- El **módulo MODBUS** suministrado por AgnosPCB para su unidad.
- Acceso al entorno de programación del controlador de línea (PLC).

!!! note "Licencias"

    El modo INLINE y la salida de informe JSON son funciones bajo licencia.
    Confirme con [support@agnospcb.com](mailto:support@agnospcb.com) que el
    perfil de su cuenta las tiene habilitadas antes de poner en marcha la línea;
    de lo contrario, las opciones no surtirán efecto.

---

## 1. Instalación del módulo MODBUS

<!-- TODO (ingeniería de AgnosPCB): la asignación de E/S y la conexión a la
     unidad de procesamiento están documentadas a partir de los esquemas de
     cableado. Falta todavía:
     - Dónde se monta el módulo (¿carril DIN dentro del armario? ¿caja externa?)
     - Qué fuente de alimentación alimenta la entrada de 7~36 V, y su capacidad
     - Tipo de cable y longitud máxima de tramo para el enlace RS-485 y para las E/S
     - Si los contactos de relé se usan como NO o NC, y su carga nominal
     - Detalle del cableado del lado del PLC -->

![Cableado Modbus](../assets/v7/conveyor/modbus_wiring.png){.center}

El módulo proporciona **8 salidas de relé** y **8 entradas digitales**, de las
cuales la integración utiliza una entrada y cuatro salidas. Se conecta a un
**puerto USB de la unidad de procesamiento de AgnosPCB** a través del conversor
aislado USB a RS232/485, tal como se muestra en el diagrama anterior.

### Entradas

La entrada debe conectarse a un **interruptor de final de carrera**, o a
cualquier sensor que detecte que la PCBA está colocada y lista para ser
inspeccionada.

| Entrada | Señal | Función |
|---|---|---|
| **DI1** | `BOARD_LOADED` | Activa una inspección, siempre que la plataforma de inspección esté lista. |

### Salidas

Las salidas comunican el estado de la inspección al resto de la línea de
montaje: a la siguiente cinta transportadora y al PLC o sistema de control de
la línea.

| Salida | Terminal | Señal | Activa cuando |
|---|---|---|---|
| **DO1** | CH1 | `READY` | La plataforma de inspección está lista para iniciar una inspección. |
| **DO2** | CH2 | `INSPECTING` | La plataforma de inspección está realizando una inspección. |
| **DO3** | CH3 | `BOARD OK` | La inspección ha finalizado y la placa inspeccionada está bien. |
| **DO4** | CH4 | `BOARD NOK` | La inspección ha finalizado y se ha detectado un fallo en la placa. |

!!! note "Cuando READY está desactivada"

    **DO1** no está activa durante la inicialización del sistema, mientras hay
    una tarea de procesamiento en curso, o cuando la aplicación no está en la
    ventana principal; por ejemplo, mientras está abierto el menú de
    configuración o el mosaico de referencias.

### Conexión general

El siguiente diagrama muestra cómo se conectan todos los elementos implicados
en una instalación típica:

![Conexión general](../assets/v7/conveyor/general_connection.png){.center}

Cuatro grupos de equipos forman parte de la integración:

- La **cinta transportadora de la AOI**, que lleva la placa hasta el área de inspección y sostiene la cámara y el sensor de posición.
- El **ordenador de AgnosPCB**, que ejecuta el software de inspección.
- El **módulo MODBUS** junto con su conversor USB a RS-485, que traduce entre el software y las señales eléctricas de la línea.
- El **equipo de línea**: la cinta transportadora que sigue a la AOI, y el PLC o sistema de control del cliente.

Las conexiones entre ellos son las siguientes:

| Desde | Hasta | Conexión | Propósito |
|---|---|---|---|
| Cámara de la cinta transportadora de la AOI | Ordenador de AgnosPCB | USB | Captura las imágenes de la placa. |
| Ordenador de AgnosPCB | Conversor USB a RS232/485 | USB | Transporta la comunicación MODBUS fuera del ordenador. |
| Conversor USB a RS232/485 | Módulo MODBUS | RS-485 (**A+** / **B−**) | Enlaza el conversor con el módulo de relés. |
| Final de carrera / sensor de la cinta transportadora de la AOI | Entrada **DI1** del módulo MODBUS | Entrada digital | Indica que la placa está colocada, lo que activa la inspección. |
| Salida **DO1** del módulo MODBUS | Cinta transportadora siguiente | Contacto de relé | Indica a la siguiente cinta que la AOI está lista para recibir una placa. |
| Salidas **DO2**, **DO3** y **DO4** del módulo MODBUS | PLC / sistema de control del cliente | Contactos de relé | Informan del progreso y del resultado de la inspección. |

!!! note "Alimentación"

    Además de estas conexiones, el módulo MODBUS necesita alimentarse a través
    de su entrada de **7~36 V**, que no está representada en el diagrama.

---

## 2. Configuración del software de inspección

Una vez instalado el módulo y establecida la comunicación, prepare el software
para el funcionamiento desatendido. Todas las opciones siguientes se
encuentran en la ventana de **Settings**; consulte el
[menú de configuración](../how_to/Settings_menu.md) para la referencia completa.

### 2.1 Habilitar el modo INLINE

Abra **Settings → Workflow** y habilite **INLINE Mode (Conveyor)**.

![Sección Workflow del menú de configuración](../assets/v7/settings/workflow-settings.png){.center}

Esto cambia el cliente del flujo de trabajo manual, controlado por teclado, al
flujo de trabajo controlado por API que se usa en una línea: la inspección la
activa el controlador de línea en lugar de que el operador pulse **S**.

### 2.2 Ajustes complementarios recomendados

Estas opciones no son obligatorias, pero en una línea desatendida son lo que
marca la diferencia entre una integración limpia y una cinta transportadora
detenida:

| Ajuste | Ubicación | Valor recomendado | Por qué |
|---|---|---|---|
| **Operator mode** | Workflow | Habilitado | Oculta la captura de referencias e impide que un operador altere la REFERENCIA o la sensibilidad a mitad de turno. Protéjalo con una contraseña de configuración (vea el [menú de configuración](../how_to/Settings_menu.md)). |
| **Mandatory errors review** | Workflow | **Deshabilitado** | Si está habilitado, el software espera a que una persona revise cada fallo antes de permitir la siguiente inspección; esto bloqueará la línea. |
| **Show errors popup** | Workflow | Deshabilitado | Evita que un diálogo modal espere entrada durante el funcionamiento automático. |
| **Show references mosaic** | Workflow | Deshabilitado | Evita una ventana emergente tras la captura de la imagen. |
| **Auto report OK / NOK** | Reports | Ambos habilitados | Genera el PDF de cada placa sin intervención del operador, de modo que la línea produce un registro de trazabilidad completo. |
| **Create JSON report** | Reports | Habilitado | Resultado legible por máquina para su MES/SCADA. Requiere licencia. |
| **Use barcodes** | Workflow | Habilitado | Permite que la AOI cargue automáticamente la REFERENCIA correcta a partir del código de barras de la placa, de modo que las líneas de producto mixto no necesitan un cambio manual de producto. Requiere licencia. Vea [lector de código de barras](../features/Barcode_reader.md). |

!!! note "Nota"

    Con **Auto report** habilitado, cada fallo se escribe en el PDF con la
    etiqueta "unknown", porque ningún operador los clasifica. Esto es lo
    esperado en una línea: la clasificación se realiza más tarde, fuera de
    línea, a partir de los informes almacenados.

### 2.3 Dónde se escriben los resultados

Las salidas de inspección se escriben en la carpeta **PCB_OUT**, configurable
en **Settings → Paths**.

Para que su MES o una unidad de red las recojan automáticamente, habilite los
recursos compartidos en **Settings → Network**: **Share PCB_OUT**,
**Share REFERENCES** y **Share REPORTS** exponen esas carpetas en la red, y
cada una muestra su ruta de red una vez activa. Para unidades OFFLINE que
necesitan una interfaz de red específica, consulte el artículo de
[configuración de la interfaz de red](../maintenance/network_configuration.md).

---

## 3. Lista de comprobación de puesta en marcha

Antes de entregar la célula a producción, verifique lo siguiente en orden.
Ejecute las primeras pruebas con la cinta transportadora en modo manual/jog.

1. **La inspección autónoma funciona.** Con el modo INLINE aún deshabilitado,
   ejecute una inspección normal desde el teclado y confirme que el resultado
   es correcto. Si la AOI no inspecciona correctamente de forma manual, no
   inspeccionará correctamente en la línea.
2. **Las REFERENCIAS están cargadas** para cada producto que procesará la
   línea, y cada una se ha validado en una placa conocida como buena. Vea
   [consejos](../help/Tips.md).
3. **La lectura de código de barras es fiable**, si la está usando para el
   cambio de producto. Pruébela en varias placas, incluidas las etiquetas peor
   impresas que tenga.
4. **La colocación de la placa es repetible.** La cinta transportadora debe
   presentar la placa dentro del área de inspección en una posición
   consistente; la AOI muestra **WARNING / ROTATED** o **WARNING / SHIFTED**
   cuando la placa se desvía significativamente de la REFERENCIA. Compruebe
   estos avisos durante las primeras ejecuciones y corrija el tope mecánico o
   la sujeción de la placa antes de pasar a producción.
5. **Las señales MODBUS están activas**: la entrada **DI1** activa una
   inspección, y las salidas **DO1** a **DO4** cambian de estado como se
   espera en el lado de la línea.
6. **Se ejecuta un ciclo completo de principio a fin**, con una placa conocida
   como buena y con una conocida como defectuosa, y el controlador de línea
   recibe el resultado PASS y FAIL correcto en cada caso.
7. **Los informes se están escribiendo** en PCB_OUT y son accesibles desde su
   MES.
8. **El comportamiento ante fallos es correcto.** Detenga el software de la
   AOI a mitad de ciclo y confirme que el controlador de línea detecta la
   pérdida y deja de alimentar placas en lugar de dejarlas pasar sin
   inspeccionar.

---

## Solución de problemas

| Síntoma | Comprobación |
|---|---|
| La línea se detiene tras la primera placa defectuosa | **Mandatory errors review** está habilitado. Deshabilítelo en Settings → Workflow. |
| Un diálogo espera entrada a mitad de ciclo | Deshabilite **Show errors popup** y **Show references mosaic** en Settings → Workflow. |
| Todas las placas fallan en un producto nuevo | La REFERENCIA cargada no corresponde al producto. Compruebe la lectura del código de barras, o la REFERENCIA seleccionada para el lote. |
| **WARNING / ROTATED** o **WARNING / SHIFTED** en la mayoría de las placas | La cinta transportadora no presenta las placas en una posición repetible. Corrija el tope mecánico; la AOI compara contra la posición de la REFERENCIA. |
| **WARNING / NO CROP** | El autocrop no pudo encontrar el borde de la placa y se comparó la imagen completa. Vuelva a capturar la REFERENCIA, o establezca el área de recorte manualmente en la imagen de referencia. |
| La AOI deja de inspeccionar y muestra `Engine [ OFFLINE ]` | Solo unidades ONLINE: la conexión a internet o la cuenta están caídas. Vea [solución de problemas](../maintenance/Troubleshooting.md). |
| Créditos agotados a mitad de turno | Solo unidades ONLINE: aparece un aviso por debajo de 10 créditos. Contacte con [support@agnospcb.com](mailto:support@agnospcb.com). |

Para cualquier cuestión no cubierta aquí, contacte con
[support@agnospcb.com](mailto:support@agnospcb.com).
