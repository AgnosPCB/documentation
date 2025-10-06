## **Red Neuronal**

En el aprendizaje automático, la red neuronal se refiere a un grupo de neuronas artificiales organizadas de una manera específica para realizar una tarea concreta. Cada neurona representa una función matemática. En el caso de **AgnosPCB**, estas neuronas realizan una inspección visual en busca de defectos en las PCBA. La arquitectura de interconexión de estas neuronas se mejora constantemente para aumentar las tasas de detección de fallos.

![Arquitectura de Red Neuronal](../assets/v7/neural_networks.webp){width=700px, .center}

## **REFERENCIA**

La imagen de **REFERENCIA** es la imagen de una PCBA libre de defectos utilizada para las inspecciones. Antes de generar la imagen de REFERENCIA, el operador debe inspeccionar la PCBA de REFERENCIA (placa DORADA o GOLDEN board) para asegurarse de que no tiene errores de fabricación.

![Imagen de Referencia](../assets/v7/ref-example.jpg){width=500px, .center}

## **UUI**

La **Unidad Bajo Inspección (UUI)** es la imagen de la PCBA que se inspeccionará durante la fabricación. Esta imagen se compara con la imagen de REFERENCIA para detectar defectos de fabricación.

![Imagen UUI](../assets/v7/uui-example.jpg){width=500px, .center}

## **Inferencia**

Este es el resultado de comparar las imágenes de REFERENCIA y UUI. Los errores, si los hay, se marcan en rojo sobre la imagen UUI. Todos los errores están numerados para facilitar la referencia.

![Imagen de Inferencia](../assets/v7/inference-example.png){width=500px, .center}

## **Informe (Report)**

Los errores detectados por el software deben ser revisados y confirmados por un operador. Pueden ser reportados como un **error real** o un **falso positivo** y etiquetados con el tipo de error. Todos estos errores reportados se utilizarán para generar un informe de inspección final en PDF.

![Ventana de Informe](../assets/v7/ui-report.png){.center}

## **Error**

Definimos un **error** como un componente que no está ensamblado correctamente, está dañado o falta. Cualquier contaminación o daño en la placa también se considera un error.

## **Falso Positivo**

La detección de **falso positivo** ocurre cuando el software AgnosPCB detecta una diferencia suficiente entre la REFERENCIA y la UUI en un componente como para marcarlo como un error, pero no hay un fallo real que afecte al funcionamiento de la PCBA. Esto puede ser causado por un cambio en el marcado, la forma o el color de un componente que es equivalente al de la referencia.