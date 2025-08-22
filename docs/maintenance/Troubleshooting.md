# **Troubleshooting**

??? info "The software does not start/respond"
    Remove the **setup.json** file located in the **APP** folder and then launch the application again.
    !!! warning "Warning"
        All configurations, such as the mosaic menu, will be lost. The REFERENCES can be loaded later by using the [Load REFERENCE button](../how_to/Screen-layout.md#load-reference-as-file). They can be reloaded later. **ONLINE** users must log in with their **AgnosPCB** account after deleting the **setup.json** file.

??? info "When trying to launch the application, a message appears saying that the file does not have permissions to launch."
    Open a terminal window (You can use the keyboard shortcut **CTRL + ALT + T**) and type the following:

    ~~~
    chmod +x APP/Agnospcb.sh
    chmod +x APP/Agnospcb.bin
    ~~~

??? info "The camera does not complete the initialization procedure and is colliding with the frame"
    You can adjust the return-to-origin parameters by editing the **machine.json** file, located in the **APP** folder. There are three parameters that adjust the axis endstops:

    ~~~
    {
    ...
    "xhome":60,
    "yhome":50,
    "zhome":30,
    ...
    }
    ~~~

    Modify the parameters of the affected axis by **increasing** the value if the axis **does not stop when it reaches the end.** **Decrease** the value if the axis **does not reach the end**.

??? info "I am getting “time-out” errors when inspecting my circuits. How do I solve it?"

    This could be due to a slow internet connection. Avoid using a Wi-Fi connection to ensure good speed. It could also be that a firewall on your local network is blocking the connection. Try accessing the following [web address](https://ai.agnospcb.com/) from the AOI to check if a firewall is blocking the connection.


??? info "The sensitivity returns to the default value after performing an inspection."

    There is a parameter in the **setup.json** file called **"remember_sensitivity"**. Modify the file and set this value to **1** to hold the sensitivity between inspections.

