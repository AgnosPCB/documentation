# FAQ

### **Do we have rental/ trial plan for Online and Offline inspection platform to try it in our lab? If so what is procedure?**

 Yes, we have a renting plan for OFFLINE units for a minimum of 2 month. If you finally decide to kept it, the renting cost will be discounted from the final price of the unit.

### **Also, just for reference in online inspection, if credits are over can we use it as Image capture for manual inspections ?**

 Yes, you can take image as a REFERENCE as much as you want. The credits are spent when you load an UUI and start the inspection procedure.

### **What is the dimension area of the inspection.**

 In the current platform the maximum PCB size that can be inspected with a single shot is **23x30cm**. Larger PCB can be inspected by parts taking various images of the board.

### **If offline platform inspection do we get update for firmware / how often we will be update the firmware (update to Neural network)?**

 The Neural Network is usually updated every 3-4 months. The OFFLINE unit can be updated easily by a USB drive.

### **In online platform, can we subscribe and unsubscribe plans based on needs/requirements ?**

 Yes, you can update/downgrade/cancel any time you want by simply emailing us at support@agnospcb.com

### **What will be the variation of monthly subscription prices over time ? ( will it increase drastically? )**

 We offer several [plans](https://agnospcb.com/products/subscription-service/) to suit your production volume.

### **Is there any other Hidden charges if any kindly let us know.**

 The only additional cost is the shipping prices due is varies with the shipping delivery.

### **What about orientation/polarity of components, what about multiple approved vendors for the same part with different looks/markings?**

The system needs a REFERENCE / GOLDEN SAMPLE to work with. If you, during the inspection / manufacturing process switched to another component reel with equivalent components but with different labelling/look/marking you will need to run an inspection with it, and if everything is fine but the new components (which are marked as faulty as they have been detected as -different-) you only have to do this: Use the Unit Under Inspection image to create a new REFERENCE. That can be easily done from the AgnosPCB inspection tool software user interface just pressing a button (UUI to REFERENCE). From that moment on, the new components with different marking/aspect will not be marked as faulty unless they present a defect.

### **How does it inspect?**

The AOI system works with two images: a REFERENCE and the unit under inspection (UUI). The neuronal network finds differences between both images and marks them. The AOI is capable of assuming small differences that are not errors like: dust, small displacements, Silkscreen variations, light reflections and others. Both images can be taken in the moment with a connected camera or imported by an existing file and the reference can be saved for future inspections. It's is important the reference has no faults in order to take good results. Also, the pictures have to be taken with good and similar light conditions in order to make easy to the neural network recognize the faulty components.  
Once it has been inspected, the inspection tool software shows the issues in the PCB and the operator is able to mark them as a fault or a false positive, choosing what kind of fault it is (wrong polarity, missing parts,...) to make a final PDF report, which can be OK or NOT_OK. This report contains the date, the operator ID, both PCB images and their faults.

### **How to indicate to the system he missed a default?**

If you notice the software is not detecting some faults just email me with the images where the error is not detected (REFERENCE and UUI images) and we will implement a fix in the next neural network update.

### **How to indicate to the system the detected default is wrong?**

You can move through the detected errors with LEFT and RIGHT arrow. To mark as an error press UP arrow. DOWN arrow for false positives and it will be reported to us. This feedback is important to us in order to improve the detection rate.

### **How does the systems work with QFN style package?**

Current hardware is not capable of seeing how QFN components are soldered, but it is capable of detecting poor positioning, displacement, twists or contamination near the IC.

