# Lector de código de barras

El software AgnosPCB incorpora una función de lectura de código de barras que soporta **códigos de barras 1D, QR y Datamatrix**.

Puede tomar una foto de **REFERENCIA** o subir una directamente desde sus archivos usando el botón **"Abrir referencia"**.

![Área de código de barras seleccionada](../assets/v7/ui-button4.png){.center}

Pulse el botón **"dibujar área de código de barras"** y dibuje un área donde se encuentra un código en el panel, luego defina de qué tipo de código se trata: **ID, Batch ID, Model o Misc**. Repita esto por cada código que quiera que el software lea, hasta **cuatro** tipos distintos.

![Lectura de código](../assets/v7/barcode/1-bc-menu.png){.center}

Si la opción **mandatory barcode** está activada en un código concreto, la inspección no continuará hasta que ese código se haya leído correctamente. Si no se detecta automáticamente, se solicitará al operador que lo introduzca manualmente antes de continuar.

Una vez que la REFERENCIA esté cargada, proceda con la inspección tomando una foto de la UUI. Cada uno de los códigos de la UUI se leerá automáticamente en las mismas áreas definidas en la REFERENCIA.

Continúe con el [proceso de inspección](../how_to/Inspection_workflow.md) como de costumbre. 

El código escaneado se incluirá en el informe PDF final de la UUI.

![Informe con código de barras incluido](../assets/barcode-report.png){.center}

## Cargar una REFERENCIA por código de barras

Si ya tiene una **REFERENCIA** almacenada, puede recuperarla fácilmente usando el código asociado a ella. Para hacer esto, presione el botón **"leer código de barras"**, luego lea el código de barras usando el lector de mano, y la **REFERENCIA** se cargará automáticamente. También es posible ingresar el código manualmente.

![Carga de REFERENCIA por código de barras](../assets/v7/ui-barcode-loading.png){.center}

![Carga de REFERENCIA por código de barras](../assets/v7/ui-bc_ref.png){.center}

![Lector de código de barras de mano](../assets/barcode-handhold.png){.center}
