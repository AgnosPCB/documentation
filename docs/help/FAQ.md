## **General questions**
___

??? question "Are there any rental / trial plans for the ONLINE and OFFLINE inspection platforms?"

    Yes, we have a renting plan for OFFLINE units for **a minimum of 2 month**. If you finally decide to kept it, the renting cost will be discounted from the final price of the unit. [Contact us](mailto:support@agnospcb.com) to require a quote 

??? question "What is the maximum PCB size that can be inspected with this system?"

    The new **AI-4050** allows inspection of PCBA up to 40 x 50 cm (16 x 19").

??? question "What is the difference between "client updates" and "neural network updates"? How frequently are these updates provided?"

    Client upgrades refer to the graphical interface used by the operator that includes features to facilitate PCBA inspections. As for the neural network updates, these refer to the architecture that performs the inspections and returns the result to the client software. ONLINE units do not require neural network updates as they use the latest version released on the AgnosPCB's server. The OFFLINE units can also upgrade the neural network architecture with ease with just a USB drive. The neural network is usually updated every 3-4 months.

??? question "How can I manage my online subscription?"

    [Contact us](mailto:support@agnospcb.com) whenever you need to make a change to your subscription.

??? question "Does the AgnosPCB AI learn by itself from the inspections it processes?"

    No, it does not. We cannot allow the neural network to learn on its own as this could lead to incorrect software behavior and compromise the performance of the system. Our engineers carefully monitor the training samples, implement them in the neural network and perform thorough testing to avoid unwanted behavior.

??? question "What can I do if the system is not detecting a fault?"

    If you notice the software is not detecting some faults or is marking a false positive constantly, just [email us](mailto:support@agnospcb.com) with the images where the error is not detected (REFERENCE and UUI images) and we will implement the fault in the next neural network update.


??? question "What can I do with the detected errors that are false positives?"

    You can move through the detected errors with LEFT and RIGHT arrow keys. To mark as false positive press the UP arrow key and it will be reported to us (on ONLINE units only). For OFFLINE units, you can also flag it as false positive with UP arrwo key. A cropped image will be generated in the REPORTS folder. Then send us by email and we will incorporate it to the next neural network architecture. This feedback is important to us in order to improve the detection rate.

??? question "How does the system work with QFN style packages?"

    Current hardware is not capable of seeing how QFN components are soldered, but it is capable of detecting poor positioning, displacement, twists or contamination near the IC.

??? question "I want to use my own optics and lighting system, how can I integrate the AgnosPCB inspection software?"

    If you plan to use your own hardware you have 2 options:

    - Using our [Windows application](https://agnospcb.com/software-tool-download/) + subscribing to any of [our plans](https://agnospcb.com/pricing-eur/). It requires a Window's computer and a stable Internet conection. This way, you will be able to store the images take by your own camera in a specific folder where the software will capture and inspect them automatically. You can also upload the images manually as this version does not support remote control of the camera.

    - Configuring our [API](https://agnospcb.com/agnospcb-api/) + subscribing to a GOLD [plan](https://agnospcb.com/pricing-eur/) or superior. This is a python script that allows you to integrate our inspection software to your system with ease. It can works in any system that can run a Python script. It requieres a stable Internet conection.


??? question "I would like to build my own lightbox. Do you have any recommendations for setting it up?"

    For optimal results, lighting should be both adequate and consistent, with an aim to eliminate shadows. It is recommended to use white lighting for best clarity. A lighting ring can be employed if it provides enough illumination. However, the key consideration is to maintain consistent lighting conditions at all times. Be careful with the influences of external lighting which can vary the conditions between photos. This may cause some problems to the detection algorithm. If you are able to, enclose the inspection area as much as you can.

??? question "Does the OFFLINE version allow for unlimited inspections?"

    The OFFLINE units entails a one-time purchase with unlimited inspections.


??? question "Can I use my current camera/AOI to inspect?"

    Yes, you can. The images can be stored in the PCB_IN folder for automatic processing, loaded manually as files, or sent directly to the API service.

??? question "Which camera is recommended?"

    A camera with a resolution of at least 20MP should provide sufficient detail for component inspection. As for the lens, you should aim for a focal length that has a balance between displaying components large enough for the neural network to be able to detect faults and that does not produce dwarfing effects on tall components.

??? question "Is it possible to inspect THT components?"

    AgnosPCB's AOI system is not specifically designed for Through-Hole Technology (THT) components. This is due to the potential large perspective differences caused by the height of THT components, which may lead to false positives in the Neural Network. Additionally, the soldering of THT components is often concealed, making inspection difficult in most cases 
    
    However, while not optimized for THT components, the AOI system can still be used for such components. It can aid in detecting displacements, incorrect polarity, flipping, or incorrect placement of THT components.

??? question "How can I use the camera to take REFERENCE and UUI pictures with the inspection tool software? "

    The current Windows version does not support camera control as it has driver issues and was designed just for testing the capabilities of the AOI system. The official version is based on Linux and supports camera control, barcode reading and report generation.
    
    However, you can share the PCB_IN folder in your network, put all the pictures in it and the software automatically will process them. You first have to load the PCBA REFERENCE in the software and activate the auto process button.
    ![alt text](assets/menu-auto-process.png)