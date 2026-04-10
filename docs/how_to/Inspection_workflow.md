# **Inspection workflow**
___

### **Launching the software**
___

- Connect the power supply to the inspection platform on the rear panel
- Turn on the monitor
- Connect the power supply to the computer and turn on it
- Once the system have started, open the app by pressing doubleclick in the desktop icon
- **For ONLINE units only**: a login windows will pop up asking for your AgnosPCB's account credentials. The credentials will be stored in the unmkdit for future use and it will not require to login again.

![Login window](../assets/v7/uui-login.png){.center}

## **Inspection procedure**

___

<iframe width="100%" height="400" src="https://www.youtube.com/embed/FirteJF0U1E?si=IiWu4CkiELWYecYR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

### **Generating a REFERENCE**

The Agnospcb Inspection tool software will **“compare”** the photograph of your **REFERENCE** circuit/panel (“golden sample”) with all the photos you will take of the circuit to be inspected (photos to “ANALYZE“)

!!!warning "Important"
    We recommend you to visit our [tips](../help/Tips.md) section before taking your first image.

To proceed with the REFERENCE taken, click in the reference icon in the main menu:

![REF button](../assets/v7/ui-button9.png){.center}

A new window will pop up with mutiple tools:

![REF window](../assets/v7/uui-ref_livepreview.png)

In this window we have to set the images needed to cover all the PCBA.

![REF dimensions](../assets/v7/uui-ref_livepreview-dimensions.png)

---

#### Capturing the PCB Size

For larger PCBAs, the camera field of view may not be sufficient to capture the entire board in a single image. In these cases, the system captures multiple images and automatically stitches them together using AI into a single image ready for inspection.

![Stitching process](../assets/stitching.png){ width=600 .center }

If you are unsure how many images are required, place the PCBA in the center of the inspection area and press the **AUTO** button. The system will scan the board and automatically set the optimal configuration.

![REF AUTO button](../assets/v7/uui-ref_livepreview-auto.png){ .center }

You can also move the camera to any quadrant of the PCBA by clicking on the desired area in the miniature view.

![Quadrants map](../assets/v7/uui-ref_livepreview-map.png){ .center }

---

#### Focus

The system allows manual focusing of the PCB before starting the capture process. Press the **FOCUS** button to adjust the optics and verify that the selected area is correctly focused.

![FOCUS button](../assets/v7/uui-ref_livepreview-focus.png){ .center }

By default, the camera focuses automatically on the center of the PCB. However, this may not always be the optimal area due to the presence of tall components.

For accurate inspection, it is essential to focus on the **base of the PCB**, where the components are mounted. Avoid focusing on tall components, as this may reduce inspection accuracy.

The PCB does not need to be centered during manual focusing. The operator can move it freely and select any suitable area to achieve proper focus, as long as the base of the PCB is clearly in focus.

After completing the focusing process, the PCB must be repositioned at the center of the inspection area before capturing the reference image.

!!! warning "Important"
    Select an area without tall components and ensure that the PCB base is sharply focused.

The lower section of the window allows enabling or disabling the grid in the live preview and adjusting the exposure.

![REF lower bar](../assets/v7/uui-ref_livepreview-exposure.png){ .center }

![Focus selection](../assets/v7/uui-ref_livepreview-select_focus.png){ .center }

---

To start the capture processing simply click the **CAPTURE REFERENCE** button. The AOI will focus automatically on the selected quadrant and start capturing the entire PCBA in a matter of seconds.

![Capture reference button](../assets/v7/uui-ref_livepreview-capture.png){.center}

![Capturing process](../assets/v7/uui-ref_stitching.png){.center}

After capturing the PCBA, the mosaic window will pop up allowing to store the image for quick usage.

!!! note "Note"
    All taken REFERENCES will be stored automatically. The mosaic helps to quickly load the most used REFERENCES.

![Capturing process](../assets/v7/ui-mosaic_after_ref.png){.center}

Once the capture process is finished, the REFERENCE image will be displayed in the main window and will allow you to set [exclusion mask](Set_exclusion_area.md) or [draw a barcode](Barcode_reader.md) area for reading.

![Reference image](../assets/v7/ui-reference.png){.center}

### **Capturing an UUI**

After generating or uploading a previous REFERENCE image, we can proceed with the capture of the **UUI** (Unit Under Inspection) image by pressing the button.

![UUI button](../assets/v7/ui-button11.png){.center}

A livepreview window will pop up showing a gosthing of the REFERENCE image. This helps to align the UUI PCBA with the REFERENCE.

!!! warning "Important"
    The **AgnosPCB** software is capable to align both images (**REFERENCE** and **UUI**) automatically. However, it is important to position the UUI PCBA correctly to avoid geometric deformations that can cause false positive detections.

![UUI livepreview](../assets/v7/ui-uui_preview.png){.center}

The capturing process will start by clicking in the **START INSPECTION** button.

!!! note "Note"
    Focusing is not necessary as the focus parameter is already stored with the REFERENCE image, making the inspection really fast.

The inspection process shall be executed in parallel in case of a multi-image inspection.

Once the capturing process have ended the fineal result will be returned showing the detected errors if there is any. It is possible to change the [detection sensitivity](Set_sensitivity.md) by pressing the button in the main window or by pressing **1, 2 or 3 key.**

![Sensitivity button](../assets/v7/ui-button6.png){.center}

![UUI inference](../assets/v7/ui-uui_report.png){.center}

If errors are detected, a **red frame** will appear around the main window. **Green frame** if there are no errors.

### **Reporting errors**

Once the inspection is complete, the operator must monitor the flagged errors, marking them as **actual error** or **false positive detection**.
To do this, simply scroll through the errors using the **left and right arrows** on the keyboard.

To mark a real error, just move to the fault and press the **up arrow** on your keyboard. A new window will appear showing the bug in detail and allowing you to categorise it by selecting a type of fault of the list.

![Report window](../assets/v7/ui-report.png){.center}

In addition, there is a empty fiel to **add a comment.**

In case the operator founds an error **not detected** by the software, it possible to flag and report it by moving the cursor to the fault area and press **up arrow** key. The reporting window will appear as usual. 

When the software marks an area that is not an actual error, the operator can flagged it as a **false positive** by pressing **down arrow** key. Also a window will appear allowing to add a comment.

![False positive window](../assets/v7/ui-fp_report.png){.center}

!!! note "Note"
    Note the **red icon** ![Red icon](../assets/v7/ui-report_red.png){width=20px} marks the actual faults and the **green icon** ![Green icon](../assets/v7/ui-report_green.png){width=20px}  the false positive faults.

### **Generating a final PDF report**

Once the reporting have finished, the operator can generate a final PDF report by pressing the following button:

![Final report](../assets/v7/ui-button8.png){.center}

A window appears allowing you to mark the inspection as **OK** or **NOT OK**. If the PCBA passes the quality check successfully, press the green icon.

![OK NOK](../assets/v7/ui-finish_inspection.png){.center}

It is possible to add comments that will be included in the report. The PDF will be generated in the **REPORTS** folder.

![PDF report](../assets/v7/pdf-report1.png){.center}

![PDF report](../assets/v7/pdf-report2.png){.center}