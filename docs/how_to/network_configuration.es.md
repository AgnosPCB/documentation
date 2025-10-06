# Configuración de la interfaz de red

!!! warning "Advertencia"
    La siguiente guía es **solo para unidades OFFLINE**.

Dado que el usuario OFFLINE no tiene acceso al usuario root del sistema, el sistema operativo personalizado de AgnosPCB permite al usuario cambiar la configuración de la interfaz de red del sistema utilizando un simple archivo de configuración.

Para establecer la configuración de la interfaz, abra un editor de texto y añada su configuración con el siguiente formato:

~~~
{
  "IP": "192.168.1.23",
  "PREFIX": "24",
  "GATEWAY": "192.168.1.1",
  "DNS1": "8.8.8.8",
  "DNS2": "8.8.4.4"
}
~~~

Reemplace los valores por los requisitos de su red. Guarde el archivo como **network.conf** en la carpeta **APP**. 
Reinicie el sistema y, después de 1 minuto, la configuración se aplicará automáticamente.
