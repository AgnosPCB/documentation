# Secuencias de captura personalizadas

## ¿Qué es una secuencia de captura?

La AOI no fotografía la placa completa en una sola toma. La cámara se desplaza sobre el área de inspección y toma una **cuadrícula de fotografías**, que el software combina después en una sola imagen. Esa cuadrícula es lo que llamamos una **secuencia**.

El software incluye un conjunto de secuencias predefinidas que cubren los tamaños de placa más habituales:

| Secuencia | Cuadrícula | Capturas |
| --- | --- | --- |
| **SMALL** | 1x1 | 1 |
| **MEDIUM** | 1x2 | 2 |
| **LARGE** | 2x2 | 4 |
| **WIDE** | 3x2 | 6 |
| **EXTRA LARGE** | 3x3 | 9 |
| **MAXIMUM** | 3x4 | 12 |

Una **secuencia personalizada** le permite definir su propia cuadrícula cuando ninguna de las predefinidas se ajusta bien a su placa.

## ¿Cuándo necesita una?

Crear una secuencia personalizada merece la pena cuando:

- Su placa tiene una forma que no encaja con ninguna de las cuadrículas predefinidas, normalmente **paneles largos y estrechos**.
- La secuencia predefinida más pequeña que cubre su placa también cubre una gran área vacía a su alrededor, de modo que la AOI fotografía espacio donde no hay placa.
- Inspecciona el mismo producto repetidamente y quiere que la cuadrícula de captura se ajuste a él con la mayor precisión posible.

Cada captura de la cuadrícula se procesa por separado, y la ventana de previsualización en directo muestra cuántas inferencias realiza la secuencia seleccionada. Una cuadrícula ajustada a su placa evita capturas innecesarias.

## Dónde encontrarla

Abra el [menú de configuración](../how_to/Settings_menu.md) y vaya a la pestaña **Sequences**.

![Pestaña Sequences](../assets/v7/custom_sequences/sequences.png){.center}

!!! note "Nota"
    Esta pestaña solo está disponible para usuarios con el rol **admin**.

## Los parámetros

| Campo | Descripción |
| --- | --- |
| **Name** | Nombre de la secuencia. Es el nombre que se mostrará después en la ventana de previsualización en directo. |
| **Size cm** | Área de placa cubierta por la secuencia. Se calcula automáticamente a partir del resto de valores, así que puede usarlo para comprobar que la cuadrícula cubre realmente su placa. |
| **Cols** / **Rows** | Número de columnas y filas de la cuadrícula, de **1 a 8**. |
| **Start X** / **Start Y** | Posición de la **primera captura**, expresada en pasos de motor de la plataforma. |
| **Step X** / **Step Y** | Distancia que recorre la cámara entre una captura y la siguiente, también en pasos de motor. |
| **Crop buffer** | Solapamiento entre capturas adyacentes, en píxeles. |

!!! tip "Sobre el crop buffer"

    Las capturas adyacentes necesitan solaparse ligeramente para que el software pueda combinarlas. Si el solapamiento es demasiado pequeño, las costuras entre capturas pueden hacerse visibles, y si es demasiado grande está fotografiando la misma área dos veces sin ningún beneficio.

## Crear una secuencia personalizada

### 1. Añadir la secuencia

Pulse el botón **+** situado bajo la lista de secuencias para crear una nueva.

![Añadir una secuencia](../assets/v7/custom_sequences/sequences-add.png){width=250px .center}

El botón **−** elimina la secuencia seleccionada en la lista, y **Dup** la duplica. Duplicar una secuencia predefinida que se acerque a lo que necesita suele ser más rápido que empezar desde cero.

### 2. Nombrarla y definir la cuadrícula

Dele a la secuencia un nombre descriptivo —es lo que buscará después en la previsualización en directo— y establezca el número de **columnas** y **filas** que necesita su placa.

![Propiedades de la secuencia](../assets/v7/custom_sequences/sequences-properties.png){.center}

El campo **Size cm** se actualiza automáticamente a medida que cambia los valores, así que puede comprobar si el área resultante cubre su placa.

### 3. Posicionar la cuadrícula y definir el orden de captura

Establezca **Start X** y **Start Y** para situar la primera captura, y **Step X** y **Step Y** para fijar cuánto se desplaza la cámara entre capturas. Después pulse **Recalc coords** para recalcular la posición de cada captura a partir de esos valores.

El lienzo muestra la cuadrícula resultante a escala. **Haga clic en las celdas** en el orden en que quiere que se fotografíen para definir el orden de captura.

![Orden de captura](../assets/v7/custom_sequences/sequences-order.png){.center}

En el ejemplo anterior, un panel alto y estrecho se cubre con **1 columna y 3 filas**. La primera captura está en X 312, Y 53, y con un **Step Y** de 90 las siguientes capturas caen en Y 143 e Y 233. La pestaña **Data** enumera las coordenadas de cada captura, y permite editarlas una a una si necesita ajustar con precisión una posición concreta.

También puede **hacer clic izquierdo y arrastrar** en el lienzo para mover la vista, y **hacer clic derecho y arrastrar** para ajustar visualmente la zona de solapamiento.

### 4. Comprobar el resultado

Seleccione una captura y abra la pestaña **Preview** para ver la imagen de la cámara en directo en esa posición exacta. Es la forma más rápida de confirmar que la cuadrícula cubre realmente su placa antes de guardar.

!!! note "Nota"
    La previsualización requiere que la plataforma esté conectada, ya que la cámara se desplaza físicamente hasta la posición seleccionada.

### 5. Guardar

Pulse **Save Sequences**. La configuración se almacena en el archivo **sequences.json** de su unidad.

## Usar su secuencia

Una vez guardada, su secuencia aparece como una opción **CUSTOM** en la ventana de previsualización en directo, tanto al tomar una imagen de REFERENCIA como al iniciar una inspección.

![Secuencia personalizada en la previsualización en directo](../assets/v7/custom_sequences/sequences-preview.png){.center}

Al seleccionarla se muestra el panel **Sequence Info** con el nombre de la secuencia, el número de inferencias que realiza y el área que cubre.
