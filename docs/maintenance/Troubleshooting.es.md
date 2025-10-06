# **Solución de Problemas**

??? info "El software no arranca/responde"
    Retire el archivo **setup.json** que se encuentra en la carpeta **APP** y luego inicie la aplicación de nuevo.
    !!! warning "Advertencia"
        Todas las configuraciones, como el menú de mosaico, se perderán. Las REFERENCIAS se pueden cargar más tarde utilizando el [botón Cargar REFERENCIA](../how_to/Screen-layout.md#load-reference-as-file). Se pueden recargar más tarde. Los usuarios **EN LÍNEA** deben iniciar sesión con su cuenta de **AgnosPCB** después de eliminar el archivo **setup.json**.

??? info "Al intentar iniciar la aplicación, aparece un mensaje que dice que el archivo no tiene permisos para ejecutarse."
    Abra una ventana de terminal (puede usar el atajo de teclado **CTRL + ALT + T**) y escriba lo siguiente:

    ~~~
    chmod +x APP/Agnospcb.sh
    chmod +x APP/Agnospcb.bin
    ~~~

??? info "La cámara no completa el procedimiento de inicialización y está colisionando con el marco"
    Puede ajustar los parámetros de retorno al origen editando el archivo **machine.json**, ubicado en la carpeta **APP**. Hay tres parámetros que ajustan los topes finales de los ejes:

    ~~~
    {
    ...
    "xhome":60,
    "yhome":50,
    "zhome":30,
    ...
    }
    ~~~

    Modifique los parámetros del eje afectado **aumentando** el valor si el eje **no se detiene al llegar al final.** **Disminuya** el valor si el eje **no alcanza el final**.

??? info "Estoy recibiendo errores de 'time-out' al inspeccionar mis circuitos. ¿Cómo lo soluciono?"

    Esto podría deberse a una conexión a Internet lenta. Evite usar una conexión **Wi-Fi** para asegurar una buena velocidad. También podría ser que un cortafuegos en su red local esté bloqueando la conexión. Intente acceder a la siguiente [dirección web](https://ai.agnospcb.com/) desde el AOI para verificar si un cortafuegos está bloqueando la conexión.

??? info "La sensibilidad vuelve al valor predeterminado después de realizar una inspección."

    Hay un parámetro en el archivo **setup.json** llamado **"remember_sensitivity"**. Modifique el archivo y establezca este valor en **1** para mantener la sensibilidad entre inspecciones.

??? info "El icono de la aplicación ha desaparecido. ¿Cómo puedo restaurarlo?"

    !!! warning "Importante"

        Seleccione su versión de AOI en las pestañas siguientes.

    === "Versión EN LÍNEA"
        1. Cree un archivo de texto con el siguiente contenido:
            ~~~
            [Desktop Entry]
            Type=Application
            Name=AgnosPCB Client
            GenericName=AgnosPCB Cliente
            Icon=/home/agnospcb/APP/icons/circuit.png
            Exec=/home/agnospcb/APP/AgnosPCB.sh
            TryExec=/home/agnospcb/APP/AgnosPCB.sh
            Terminal=No
            Categories=Development;IDE;Debugger;ParallelComputing
            ~~~
        2. Guárdelo como **AgnosPCB.desktop**
        3. Copie/mueva el archivo a la carpeta Escritorio.
        4. En el escritorio, haga clic derecho en el icono -> **Propiedades** -> **Permisos** -> **Es ejecutable**

            ![Es ejecutable](../assets/maintance/executable.png)
    
    === "Versión SIN CONEXIÓN (OFFLINE)"
        1. Cree un archivo de texto con el siguiente contenido:
            ~~~
            [Desktop Entry]
            Type=Application
            Name=AgnosPCB Client
            GenericName=AgnosPCB Cliente
            Icon=/home/agnospcb/APP/icons/circuit.png
            Exec=/home/agnospcb/APP/AgnosPCB.sh
            TryExec=/home/agnospcb/APP/AgnosPCB.sh
            Terminal=No
            Categories=Development;IDE;Debugger;ParallelComputing
            ~~~
        2. Guárdelo como **AgnosPCB.desktop** y muévalo a la carpeta Escritorio.
        3. Abra el gestor de archivos.

            ![Gestor de archivos](../assets/maintance/icon-1.png)

        4. Haga clic en el icono de las 3 líneas y luego en **Preferencias**.

            ![Preferencias](../assets/maintance/icon-2.png)

        5. Haga clic en la pestaña Comportamiento (Behavior) y seleccione "Preguntarme qué hacer" (Ask me what to do).

            ![Pestaña Comportamiento](../assets/maintance/icon-3.png)

        6. Reinicie la unidad.

        7. Haga clic derecho en el icono > "**Permitir ejecución**" (Allow launching).

            ![Permitir ejecución](../assets/maintance/icon-4.png)

??? info "¿Cómo cambio la distribución del teclado del sistema?"

    !!! warning "Importante"

        Seleccione su versión de AOI en las pestañas siguientes.
        
    === "Versión EN LÍNEA"
        1. Abra el menú de la aplicación desde la parte superior del escritorio o presione la tecla Windows. Seleccione **Configuración del sistema (System Settings)**.
            
            ![Paso 1](../assets/maintance/keyboard-online-1.png)

        2. Navegue a **Dispositivos de entrada (Input Devices)** > **Teclado (Keyboard)** > **Distribución (Layout)**. Habilite **Configurar distribuciones (Configure layouts)** y presione **Añadir (Add)**.

            ![Paso 2](../assets/maintance/keyboard-online-2.png)

        3. Busque la distribución de su teclado y presione **Ok**.

            ![Paso 3](../assets/maintance/keyboard-online-3.png)

        4. Mueva la distribución al primer lugar presionando **Mover hacia arriba (Move up)**.

            ![Paso 4](../