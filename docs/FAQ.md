# FAQ

??? question "Is there a rental/ trial plan for Online and Offline inspection platform to try it?"

    Yes, we have a renting plan for OFFLINE units for a minimum of 2 month. If you finally decide to kept it, the renting cost will be discounted from the final price of the unit. For further information click "[here](Products-and-services.md "Title")"

??? question "if credits are over can we use it as Image capture for manual inspections?"

    Yes, you can take image as a REFERENCE as much as you want. The credits are spent when you load an UUI and start the inspection procedure.

??? question "What is the dimension area of the inspection?"

    In the current platform the maximum PCB size that can be inspected with a single shot is **23x30cm**. Larger PCB can be inspected by parts taking various images of the board.

??? question "Are firmware updates available for offline platform inspection? If so, how frequently are these updates provided to enhance the neural network?"

    The Neural Network is usually updated every 3-4 months. The OFFLINE unit can be updated easily by a USB drive.

??? question "In online platform, can you subscribe and unsubscribe plans based on needs/requirements ?"

    Yes, you can update/downgrade/cancel any time you want by simply emailing us at support@agnospcb.com

??? question "What will be the variation of monthly subscription prices over time?"

    We offer several [plans](https://agnospcb.com/products/subscription-service/) to suit your production volume.

??? question "Is there any other Hidden charges?"

     The only additional cost is the shipping prices due is varies with the shipping delivery.

??? question "How does it inspect?"

    The AOI system works with two images: a REFERENCE and the unit under inspection (UUI). The neuronal network finds differences between both images and marks them. The AOI is capable of assuming small differences that are not errors like: dust, small displacements, Silkscreen variations, light reflections and others. Both images can be taken in the moment with a connected camera or imported by an existing file and the reference can be saved for future inspections. It's is important the reference has no faults in order to take good results. Also, the pictures have to be taken with good and similar light conditions in order to make easy to the neural network recognize the faulty components.  
    
    Once it has been inspected, the inspection tool software shows the issues in the PCB and the operator is able to mark them as a fault or a false positive, choosing what kind of fault it is (wrong polarity, missing parts,...) to make a final PDF report, which can be OK or NOT_OK. This report contains the date, the operator ID, both PCB images and their faults.

??? question "How to indicate to the system he missed a default?"

    If you notice the software is not detecting some faults just email us with the images where the error is not detected (REFERENCE and UUI images) and we will implement a fix in the next neural network update.


??? question "How to indicate to the system the detected default is wrong?"

    You can move through the detected errors with LEFT and RIGHT arrow. To mark as an error press UP arrow. DOWN arrow for false positives and it will be reported to us. This feedback is important to us in order to improve the detection rate.

??? question "How does the systems work with QFN style package?"

    Current hardware is not capable of seeing how QFN components are soldered, but it is capable of detecting poor positioning, displacement, twists or contamination near the IC.

??? question "Do you have any recommendations for establishing a basic lightbox? How should we effectively illuminate the board, particularly from the side?"

    For optimal results, lighting should be both adequate and consistent, with an aim to eliminate shadows. It is recommended to use white lighting for best clarity. A lighting ring can be employed if it provides ample illumination. However, the paramount consideration is to maintain consistent lighting conditions at all times.

??? question "Does the offline version allow for unlimited inspections?"

    The offline version entails a one-time purchase with unlimited inspections.

??? question "What is the maximum size of a card that can be captured with the offline system?"

    On the current platform, the maximum PCB size that can be inspected in a single shot is 23x30cm. To view the product you can use this link: [Link to product](https://agnospcb.com/product/agnospcb-offline-inspection-plaftorm/)

??? question "Can I use my current camera/AOI to inspect?"

    The AgnosPCB software currently supports remote control of Sony cameras exclusively. We cannot guarantee compatibility with all camera models. Optionally, images can be stored in the PCB_IN folder for automatic processing, loaded manually as files, or connected directly to the API.

??? question "Which camera is recommended?"

    A camera with a resolution of at least 20MP should provide sufficient detail for component inspection. We recommend Sony cameras to ensure compatibility with AgnosPCB's client software and to avoid potential future compatibility issues

??? question "Is it possible to inspect THT components?"

    AgnosPCB's AOI system is not specifically designed for Through-Hole Technology (THT) components. This is due to the potential large perspective differences caused by the height of THT components, which may lead to false positives in the Neural Network. Additionally, the soldering of THT components is often concealed, making inspection difficult in most cases 
    
    However, while not optimized for THT components, the AOI system can still be used for such components. It can aid in detecting displacements, incorrect polarity, flipping, or incorrect placement of THT components.