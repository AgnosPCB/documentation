## **Preguntas generales**
___

??? question "¿Existen planes de alquiler o prueba para las plataformas de inspección EN LÍNEA y SIN CONEXIÓN (OFFLINE)?"

    Sí, tenemos un plan de alquiler para unidades SIN CONEXIÓN por **un mínimo de 2 meses**. Si finalmente decide conservarla, el coste del alquiler se descontará del precio final de la unidad. [Contáctenos](mailto:support@agnospcb.com) para solicitar un presupuesto.

??? question "¿Cómo genero un informe de error no detectado?"

    Puede reportar un fallo no detectado moviendo el cursor al área del fallo y presionando la tecla de **flecha ABAJO**. Las imágenes se reportan a nuestro servidor y las usamos para entrenar la Red Neuronal para detectar estos errores. El error se incluirá en la próxima actualización de la Red Neuronal.

??? question "¿Cuál es el tamaño máximo de PCB que se puede inspeccionar con este sistema?"

    El nuevo **AI-4050** permite la inspección de PCBA (placas de circuito impreso ensambladas) de hasta 40 x 50 cm (16 x 19").

??? question "¿Cuál es la diferencia entre 'actualizaciones del cliente' y 'actualizaciones de la red neuronal'? ¿Con qué frecuencia se proporcionan estas actualizaciones?"

    Las actualizaciones del cliente se refieren a la interfaz gráfica utilizada por el operador que incluye características para facilitar las inspecciones de PCBA. En cuanto a las actualizaciones de la red neuronal, estas se refieren a la arquitectura que realiza las inspecciones y devuelve el resultado al software cliente. Las unidades **EN LÍNEA** no requieren actualizaciones de la red neuronal ya que utilizan la última versión liberada en el servidor de AgnosPCB. Las unidades **SIN CONEXIÓN** también pueden actualizar la arquitectura de la red neuronal fácilmente con solo una unidad USB. La red neuronal se actualiza generalmente cada 3-4 meses.

??? question "¿Cómo puedo gestionar mi suscripción en línea?"

    [Contáctenos](mailto:support@agnospcb.com) siempre que necesite realizar un cambio en su suscripción.

??? question "¿Aprende la IA de AgnosPCB por sí misma de las inspecciones que procesa?"

    No, no lo hace. No podemos permitir que la red neuronal aprenda por sí misma, ya que esto podría llevar a un comportamiento incorrecto del software y comprometer el rendimiento del sistema. Nuestros ingenieros monitorean cuidadosamente las muestras de entrenamiento, las implementan en la red neuronal y realizan pruebas exhaustivas para evitar comportamientos no deseados.

??? question "¿Qué puedo hacer si el sistema no está detectando un fallo?"

    Si nota que el software no está detectando algunos fallos o está marcando un falso positivo constantemente, simplemente [envíenos un correo electrónico](mailto:support@agnospcb.com) con las imágenes donde el error no se detecta (imágenes de REFERENCIA y UUI) y implementaremos el fallo en la próxima actualización de la red neuronal.

??? question "¿Qué puedo hacer con los errores detectados que son falsos positivos?"

    Puede moverse a través de los errores detectados con las teclas de flecha IZQUIERDA y DERECHA. Para marcar como falso positivo presione la tecla de **flecha ARRIBA** y se nos informará (solo en unidades EN LÍNEA). Para las unidades SIN CONEXIÓN, también puede marcarlo como falso positivo con la tecla de flecha ARRIBA. Se generará una imagen recortada en la carpeta REPORTS. Luego, envíenosla por correo electrónico y la incorporaremos a la próxima arquitectura de red neuronal. Este *feedback* es importante para nosotros con el fin de mejorar la tasa de detección.

??? question "¿Cómo funciona el sistema con encapsulados estilo QFN?"

    El *hardware* actual no es capaz de ver cómo están soldados los componentes QFN, pero sí es capaz de detectar un posicionamiento deficiente, desplazamiento, giros o contaminación cerca del circuito integrado (IC).

??? question "Quiero usar mi propio sistema de óptica e iluminación, ¿cómo puedo integrar el software de inspección AgnosPCB?"

    Si planea usar su propio *hardware*, tiene 2 opciones:

    - Usar nuestra [aplicación de Windows](https://agnospcb.com/software-tool-download/) + suscribirse a cualquiera de [nuestros planes](https://agnospcb.com/pricing-eur/). Requiere un ordenador con Windows y una conexión a Internet estable. De esta manera, podrá almacenar las imágenes tomadas por su propia cámara en una carpeta específica donde el software las capturará e inspeccionará automáticamente. También puede cargar las imágenes manualmente ya que esta versión no admite el control remoto de la cámara.

    - Configurar nuestra [API](https://agnospcb.com/agnospcb-api/) + suscribirse a un [plan](https://agnospcb.com/pricing-eur/) GOLD o superior. Este es un *script* de Python que le permite integrar nuestro software de inspección en su sistema con facilidad. Puede funcionar en cualquier sistema que pueda ejecutar un *script* de Python. Requiere una conexión a Internet estable.

??? question "Me gustaría construir mi propia caja de luz. ¿Tienen alguna recomendación para configurarla?"

    Para obtener resultados óptimos, la iluminación debe ser adecuada y consistente, con el objetivo de eliminar las sombras. Se recomienda utilizar **iluminación blanca** para una mejor claridad. Se puede emplear un anillo de iluminación si proporciona suficiente luz. Sin embargo, la consideración clave es mantener **condiciones de iluminación consistentes** en todo momento. Tenga cuidado con las influencias de la iluminación externa que pueden variar las condiciones entre fotos. Esto puede causar algunos problemas al algoritmo de detección. Si puede, encierre el área de inspección tanto como sea posible.

??? question "¿Permite la versión SIN CONEXIÓN inspecciones ilimitadas?"

    Las unidades SIN CONEXIÓN implican una compra única con inspecciones ilimitadas.

??? question "¿Puedo usar mi cámara/AOI actual para inspeccionar?"

    Sí, puede. Las imágenes se pueden almacenar en la carpeta PCB\_IN para su procesamiento automático, cargarse manualmente como archivos o enviarse directamente al servicio API.

??? question "¿Qué cámara se recomienda?"

    Una cámara con una resolución de al menos **20MP** debería proporcionar suficiente detalle para la inspección de componentes. En cuanto a la lente, debe buscar una distancia focal que tenga un equilibrio entre mostrar los componentes lo suficientemente grandes para que la red neuronal pueda detectar fallos y que no produzca efectos de acortamiento en componentes altos.

??? question "¿Es posible inspeccionar componentes THT (Through-Hole Technology)?"

    El sistema AOI de AgnosPCB no está diseñado específicamente para componentes de Tecnología de Orificio Pasante (THT). Esto se debe a las posibles grandes diferencias de perspectiva causadas por la altura de los componentes THT, lo que puede llevar a falsos positivos en la Red Neuronal. Además, la soldadura de los componentes THT a menudo está oculta, lo que dificulta la inspección en la mayoría de los casos.
    
    Sin embargo, aunque no está optimizado para componentes THT, el sistema AOI aún puede utilizarse para dichos componentes. Puede ayudar a detectar desplazamientos, polaridad incorrecta, inversión o colocación incorrecta de componentes THT.

??? question "¿Cómo puedo usar la cámara para tomar fotos de REFERENCIA y UUI con el software de la herramienta de inspección?"

    La versión actual de Windows no es compatible con el control de la cámara, ya que presenta problemas de controladores y fue diseñada solo para probar las capacidades del sistema AOI. La versión oficial está basada en Linux y admite control de cámara, lectura de códigos de barras y generación de informes.
    
    Sin embargo, puede compartir la carpeta PCB\_IN en su red, colocar todas las imágenes en ella y el software las procesará automáticamente. Primero debe cargar la REFERENCIA PCBA en el software y activar el botón de **proceso automático**.
    ![alt text](../assets/menu-auto-process.png)