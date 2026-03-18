# Network interface configuration

!!! warning "Warning"
    The following guide is for **OFFLINE units only**.

Since the OFFLINE user does not have access to the system's root user, the custom AgnosPCB's OS allows the user to change the system's network interface settings by using a simple configuration file.

To set the interface settings, open text editor and add your configuration with the following format:

~~~
{
  "IP": "192.168.1.23",
  "PREFIX": "24",
  "GATEWAY": "192.168.1.1",
  "DNS1": "8.8.8.8",
  "DNS2": "8.8.4.4"
}
~~~

Replace the values to your network requirements. Save the file as **network.conf** in the **APP** folder. 
Reboot the system and, after a 1 minute, the configuration will be applied automatically.