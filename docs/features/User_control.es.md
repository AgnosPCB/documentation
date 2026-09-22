# Control de acceso de usuarios

## ¿Qué es el control de acceso de usuarios?

Por defecto, cualquier persona con acceso a la AOI puede usar el software y cambiar cualquiera de sus ajustes.

El **control de acceso de usuarios** le permite crear cuentas individuales y exigir un **nombre de usuario y una contraseña** cada vez que se inicia el software. Cada cuenta tiene un rol que determina qué puede hacer su usuario, de modo que puede dejar que un operador realice inspecciones mientras mantiene protegida la configuración de la máquina.

## Los dos roles

Cada cuenta tiene uno de estos dos roles:

| | **admin** | **operator** |
| --- | --- | --- |
| Opciones de General, Workflow y Report | Sí | Sí |
| Opciones de Date/time, Path y Share | Sí | No |
| Users, Sequences, Machine y Debug | Sí | No |
| Tomar una imagen de REFERENCIA | Sí | Solo si el modo operador está deshabilitado |
| Gestionar usuarios | Sí | No |
| Calibrar la plataforma | Sí | No |
| Establecer la contraseña de configuración | Sí | No |
| Generar una copia de seguridad | Sí | No |

!!! note "El rol operador y el modo operador no son lo mismo"

    El **rol operador** descrito aquí limita qué pestañas del [menú de configuración](../how_to/Settings_menu.md) puede abrir el usuario.

    El **modo operador**, en *Settings → Workflow*, simplifica la interfaz y bloquea la captura de imágenes de REFERENCIA. Se aplica a quien esté usando la máquina, independientemente de su rol.

    Pueden usarse juntos: una cuenta de operador con el modo operador habilitado obtiene tanto la interfaz simplificada como la configuración restringida.

## Configurarlo

### 1. Abrir la pestaña Users

Abra el [menú de configuración](../how_to/Settings_menu.md) y vaya a la pestaña **Users**. En una máquina que nunca se ha configurado, la lista está vacía y el control de acceso está deshabilitado.

![Pestaña Users](../assets/v7/user_control/users-tab.png){.center}

### 2. Crear primero un administrador

Antes de nada necesita una cuenta **admin**. Si intenta habilitar el control de acceso sin una, el software se lo impide:

![Error de usuario admin inexistente](../assets/v7/user_control/users-no-admin-error.png){width=350px .center}

Pulse **Add user**, rellene el nombre de usuario, seleccione el rol **admin**, deje marcado **Active user** y escriba la contraseña dos veces.

![Añadir un usuario admin](../assets/v7/user_control/users-add-admin.png){width=400px .center}

Pulse **Save**. La nueva cuenta aparece en la lista, con la fecha en que se creó.

![Administrador creado](../assets/v7/user_control/users-admin-created.png){.center}

!!! warning "Importante"

    Guarde la contraseña del administrador en un lugar seguro. Una vez habilitado el control de acceso, esta es la cuenta que le permite volver a entrar en el menú de configuración.

### 3. Habilitar el control de acceso

Con una cuenta admin activa en la lista, habilite **Enable user access control**.

![Control de acceso habilitado](../assets/v7/user_control/users-access-enabled.png){.center}

### 4. Añadir el resto de usuarios

Añada una cuenta para cada persona que vaya a usar la máquina, dándole el rol **operator** a menos que necesite cambiar la configuración.

![Añadir un usuario operador](../assets/v7/user_control/users-add-operator.png){width=400px .center}

La lista muestra cada cuenta con su rol, si está activa, y las fechas en que se creó y se modificó por última vez.

![Lista de usuarios](../assets/v7/user_control/users-list.png){.center}

Pulse **OK** para guardar y cerrar el menú de configuración.

## Iniciar sesión

A partir del siguiente inicio del software, el diálogo **User access required** solicita las credenciales de una de las cuentas que ha creado.

![Diálogo de inicio de sesión](../assets/v7/user_control/users-login.png){width=400px .center}

El software se abre entonces con los permisos de esa cuenta.

Para cerrar la sesión y dejar que otro usuario inicie sesión, use el botón **logout** del [área de estado de la plataforma](../how_to/Screen-layout.md).

## Gestionar las cuentas

Seleccione una cuenta en la lista para trabajar con ella:

- **Edit user** — cambia el rol, la contraseña o el estado activo de la cuenta seleccionada.
- **Delete user** — la elimina permanentemente. Se solicita confirmación.

!!! tip "Desactivar en lugar de eliminar"

    Para impedir que alguien use la máquina sin perder el registro de su cuenta, edite el usuario y desmarque la casilla **Active user**. La cuenta permanece en la lista, pero ya no puede iniciar sesión.

!!! note "Nota"
    Siempre debe haber al menos una cuenta **admin activa**. Téngalo en cuenta antes de desactivar o eliminar a un administrador.
