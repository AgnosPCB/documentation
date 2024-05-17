# User guide
___

## **User interface**
___

Upon launching the Agnospcb inspection tool software, the user interface will appear. It has different panels and inspection areas:

- **Reference panel (green )**: The “golden sample” image. Can be loaded using the LOAD icon (from the Reference area). 
- **Unit Under Inspection (orange)**: this is the image of the panel to be inspected. Can be loaded using the LOAD icon (from the inspection area)
- **Magnification canvas** : this frame will display, the same areas of the REFERENCE and RESULT circuit/panels. Move the mouse to check different zones of the circuit. Use the mouse’s wheel to modify the zoom magnification. 
- **Activity log**: provides useful information about the inspection process
- **Settings**: where the configuration ICONs are. Useful tools in your inspection process.

  ![Screen](assets/ui-pcb.png)


## **The inspection button**
___

![Inspection button](assets/inspection_button.PNG){ align=right }

**The Inspection button** will let you take the best possible photo of your circuits / panels just pressing it. It will quickly start the process of configuring the camera with the best parameters, prepare the software, so it can use the latest photo taken, and analyze it looking for faults. Just in a matter of a fraction of a second.

 **This button can be used for:**

1) **SET** a **REFERENCE** image: PRESS it for 5 seconds until you hear the camera shooting. The AOI software will use that image as **REFERENCE** to compare all the next images of the circuits.

2) **INITIALIZE** the inspection process: Just press it for a second and the camera will capture an image of the circuit / panel to be analyzed. Alternatively, you can click, with the mouse, on the INSPECTION BUTTON (icon below) on the user interface to do the same.

## **Inspection process**
___

At this point, you should have already set up the inspection platform and everything should be connected to the laptop.

The points listed below will guide you through the steps you need to make to inspect a circuit/ panel your first time.

**1.** Turn **ON** the **LEDs** panels using the switch and/or remote control. Set, using the UP and DOWN arrows, their brightness. If you are inside a well-lit room, you may not need to set them to their maximum brightness.

**2.** **Turn ON** the CAMERA.

**3.** Quick-check if the camera is set in **aperture** mode (A).

**4.** **Turn ON** the computer and wait for the system to boot.

**5.** **The Inspection software tool** needs to be launched.

**6.** Check if the camera respond to the **INSPECTION BUTTON**, pressing it for 5 seconds (or key “R”). That should set a **REFERENCE** image. This is a photo taken  to a circuit/panel you already know is in good condition. As the camera parameters are controlled from the laptop, you do not have to do           anything. Just check if the image is in focus. You can use the mouse’s wheel to increase the zoom magnification and take a closer look at the     elements. 

**7.** Once the **REFERENCE** photo of the circuit/panel has been set, you can now take photos of the units you want to inspect (units under inspection). Press the **INSPECTION BUTTON** for **one second** to take a photo (or key “S”)

**8.** You are ready to go. The system should be now indicating, if any, faults on the UUI (Unit Under Inspection). Go to point 7 and repeat the process  once a new UUI has been placed under the camera.

All the inspection results will be stored in the PCB_OUT folder you will find in the external USB drive. The REFERENCE images will be moved to the folder called “REFERENCE”. You can find all of them there , in the case you need any of the REFERENCE images previously used.


!!! note inline  "Note"

    The “R” key from the keyboard will work as a camera trigger button too. “R” will set a REFERENCE image. “S” will take a photo of an image to be inspected.

!!! note "Note"

    If you activate the AUTO-ANALYSIS option, all the photos taken pressing “R” or the INSPECTION BUTTON for one second, will be automatically processed.

!!! warning "Important"

    By default, we send the camera already configured, but from time to time, re-check the camera is operating with the Aperture MODE enabled.

![Camera parts](assets/CAMER_INSPECTION.PNG)

First, tap on the round button indicated above. The select rotating the dial, the Aperture MODE **(A)**. Then, using the same dial, select the value F8.0 (right image). Setting the aperture to F8.0 will let you get the most detailed photos of your circuits / panels.

With some tips about how to improve the fault detection results and comments about what not to do.

![Lights on the sides of the camera and no PCB rotation](assets/TIPS.PNG)

## **Light sources and panel/circuit orientation**
___

The inspection platform uses 2 LED lights and diffuser panels to get rid of cast shadows. But if you take photos of the circuits varying its orientation every inspection, large electronic elements (like capacitors, coils and connectors) present on the circuits/ panels will be seen differently from the camera’s point of view.

**Try to place the circuit always with the same orientation.** 

The software is capable, within a second, of auto-aligning the images, but the light projected will fall very differently over the electronic components if the circuit is rotated by 90/180 degrees. That will lead the neural network to make mistakes when looking for faults. Try to avoid it always placing the panels/circuits with the same orientation.

![Optical zoom and digital zoom](assets/optical-digital.PNG){ align=right }


## **Cropping tool**
___

Useful when the panel/circuit in the photo is too small. Cropping the image will “force” the software to focus on the selected area and will reduce the inspection time.
 
**You can only crop an image in the REFERENCE canvas.**

The software will automatically look for the same area in every photo taken of the panels to be inspected after the cropping boundary has been set. To remove the CROP boundaries, click on the CROP icon again.

## **Circuit / Panel with many small electronic elements**
___

![PCB with many small electronic elements](assets/circuit.PNG)

The neural network powering the Agnospcb software behaves as a very skilled technician. But it can only detect faults **that can be seen**. Any minor displacement, solder paste change or short-circuit “hidden” under a shadow or light reflection may become **identifiable** if we **slightly** change **the lighting conditions / orientation of the panel/ circuit.** 

If you are inspecting a panel/ circuit with electronic elements casting pronounced shadows over other component/s, elements with very small pins or just obstructing the camera point of view, we recommend following this methodology which can lead to increase the detection rate:

**1)** Run a **regular inspection** and check results.

**2)** Slightly rotate the panel/ circuit and **run a second inspection.** 

**3)** Every inspection takes between 1-4 seconds so, a third one could be done quickly. Run a third inspection but, in this case, rotating in the opposite direction the panel/ circuit.


The vast majority of inspections do not require this methodology, but it is interesting to note the possibility **of increasing the detection capability of the system by carrying out this process.**

**The camera does not respond**

Check if the battery dummy is connected to the correct USB power supply, capable of delivering 3A. Check if the USB cable is properly connected and fully inserted. Does the R and S keys of the keyboard trigger the camera? 
