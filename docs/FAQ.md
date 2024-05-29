# **FAQ**

??? question "Are there any rental / trial plans for the Online and Offline inspection platforms?"

    Yes, we have a renting plan for OFFLINE units for a minimum of 2 month. If you finally decide to kept it, the renting cost will be discounted from the final price of the unit. For further information click "[here](Products-and-services.md "Products and services")"

??? question "If we spend all the credits from our subscription plan, can we still use the platform as an Image capture device for manual inspections?"

    Yes, you can take images as a REFERENCE, as much as you want. The credits are spent when you load an UUI and start the inspection procedure.

??? question "What is the maximum PCB size that can be inspected with this system?"

    In the current platform the maximum PCB size that can be inspected with a single shot is **23x30cm**. Larger PCBs can be inspected by parts taking various images of the board.

??? question "Are there firmware updates available for the offline inspection platform? If so, how frequently are these updates provided to enhance the neural network?"

    The Neural Network is usually updated every 3-4 months. The OFFLINE unit can be updated easily by a USB drive.

??? question "Having an online subscription plan, can you change or cancel it based on needs/requirements?"

    Yes, you can update/downgrade/cancel any time you want by simply emailing us at support@agnospcb.com

??? question "What will be the variation of monthly subscription prices over time?"

    We offer several [plans](https://agnospcb.com/products/subscription-service/) to suit your production volume.

??? question "Are there any other hidden charges?"

     The only additional charge is the shipping cost, which we quote according to the customer's delivery address.

??? question "How does the inspection process works?"

    The AOI system works with two images: a REFERENCE and the unit under inspection (UUI). The neuronal network finds differences between both images and marks them. The AOI is capable of assuming small differences that are not errors like: dust, small displacements, Silkscreen variations, light reflections and others. Both images can be taken in the moment with a connected camera or imported by an existing file and the reference can be saved for future inspections. It's is important that the reference has no faults in order to deliver good results. Also, the pictures have to be taken with good and similar light conditions achieve the best performance of the AI model.
    
    Once it has been inspected, the inspection tool software shows the issues in the PCB and the operator is able to mark them as a fault or a false positive, choosing what kind of fault it is (wrong polarity, missing parts,...) to make a final PDF report, which can be OK or NOT_OK. This report contains the date, the operator ID, both PCB images and their faults.

??? question "What can I do if the system is not detecting a fault?"

    If you notice the software is not detecting some faults just email us with the images where the error is not detected (REFERENCE and UUI images) and we will implement a fix in the next neural network update.


??? question "What can I do with the detected errors that are false positives?"

    You can move through the detected errors with LEFT and RIGHT arrow keys. To mark as an error press the UP arrow key. Press the DOWN arrow key to flag false positives, and they will be reported to us (on online platforms). This feedback is important to us in order to improve the detection rate.

??? question "How does the system work with QFN style packages?"

    Current hardware is not capable of seeing how QFN components are soldered, but it is capable of detecting poor positioning, displacement, twists or contamination near the IC.

??? question "Do you have any recommendations for setting up a basic lightbox? How should we effectively illuminate the board, particularly from the side?"

    For optimal results, lighting should be both adequate and consistent, with an aim to eliminate shadows. It is recommended to use white lighting for best clarity. A lighting ring can be employed if it provides enough illumination. However, the key consideration is to maintain consistent lighting conditions at all times.

??? question "Does the offline version allow for unlimited inspections?"

    The offline version entails a one-time purchase with unlimited inspections.


??? question "Can I use my current camera/AOI to inspect?"

    The AgnosPCB software currently supports remote control of Sony cameras exclusively. We cannot guarantee compatibility with all camera models. Optionally, images can be stored in the PCB_IN folder for automatic processing, loaded manually as files, or sent directly to the API service.

??? question "Which camera is recommended?"

    A camera with a resolution of at least 20MP should provide sufficient detail for component inspection. We recommend Sony cameras to ensure compatibility with AgnosPCB's client software and to avoid potential future compatibility issues

??? question "Is it possible to inspect THT components?"

    AgnosPCB's AOI system is not specifically designed for Through-Hole Technology (THT) components. This is due to the potential large perspective differences caused by the height of THT components, which may lead to false positives in the Neural Network. Additionally, the soldering of THT components is often concealed, making inspection difficult in most cases 
    
    However, while not optimized for THT components, the AOI system can still be used for such components. It can aid in detecting displacements, incorrect polarity, flipping, or incorrect placement of THT components.

??? question "How can I use the camera to take reference and UUI pictures in the inspection tool software? "

    The current Windows version does not support camera control as it has driver issues and was designed just for testing the capabilities of the AOI system. The official version is based on Linux and supports camera control, barcode reading and report generation.
    
    However, you can share the PCB_IN folder in your network, put all the pictures in it and the software automatically will process them. You first have to load the PCBA REFERENCE in the software and activate the auto process button.
    ![alt text](assets/menu-auto-process.png)