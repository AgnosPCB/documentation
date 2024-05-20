# **User Interface**
___

## **Main working areas**
___
The following image describes the main working areas of the **AgnosPCB inspection software**.

![Main section](assets/ui_areas.png)


## **Start inspection**
___

![Start inspection button](assets/autoprocess.png)

The **Inspection start** button is located in the upper left corner. A simple click triggers a sequence of actions to inspect the current **UUI** image. This buttom is available when the [Auto process button](#auto-process) is set **OFF**. This is useful to avoid spend credits when you are testing how to take pictures of your PCBAs.


## **Activity log**
___

![Inner workings section](assets/activity-log.png)

The **activity log** area is located in the top right side and shows the **current avaible credits** and application's operational details. This log serves as a guide, offering clarity and insights into the application's functionality and performance.


## **Main workspace**
___

![Main section](assets/screen3.png)

This is the main section where you work with the images, whether it's the **REFERENCE** or the **UUI.**


## **Side-by-side comparison**
___

![comparison section](assets/side-by-side_comparsion.png){width=400px}

This interface section, is divided in two parts. The first displays the **REFERENCE** image, serving as a standard for comparison, while the second part shows the **UUI** image. These images are maginified and move in parallel showing exactly the same area in the **REFERENCE** and **UUI**. This areas are defined by where the cursor is pointing in the image.


## **Buttons panel**
___

![buttons panel](assets/screen5.png)

Here are located various **buttons and options**.They're designed to **optimize** your workflow and speed up your tasks.

### **Reference mosaic**

![Reference mosaic button](assets/menu-mosaic.png)

![Mosaic menu](assets/mosaic2.png){width=600px}

The reference mosaic is used to store REFERENCES as files to quickly find and load any fo them. The mosaic menu automatically appears after taking a REFERENCE by using the software with the [take REFERENCE photo button](#take-reference-photo) or by loading it with [as a file](#load-reference-as-file). A stored REFERENCE stored in the mosaic can be quickly loaded by pressing a **F button** (F1-F10).

### **LOAD REFERENCE as file**

![Open reference button](assets/menu-load-ref-file.png)

Use this icon to load a image file as a **REFERENCE**. If you have stored a **“reference”** image and want to retrieve it to use it again, use this button. All the **REFERENCE** photos can be found inside the folder **APP/REFERENCE** in a folder named after the time the picture was taken.


### **Swap**
 
![Swap button](assets/menu-tab.png)

Toggles between **REFERENCE** and **UUI** images in the [main workspace area](#main-workspace).

### **LOAD a UUI as file**

![Open UUI button](assets/menu-load-uui-file.png)

It loads a **UUI** image from a file stored in the unit.


### **Exclusion**

![Exclusion button](assets/menu-exclusion.png)

Creates an exclusion area where the system will not look for faults. You can create as many areas as required. This function is detailed in the [following section](Set_exclusion_area.md).

### **Sensitivity**

![Sensitivity button](assets/menu-sensitivity.png)

Change the system fault detection sensitivity (NORMAL/HIGH/VERY HIGH). Set back to normal, automatically after carrying out a new inspection. Shortcut: 1, 2 ,3 Keys

### **Barcode reader**

![Barcode reader button](assets/menu-barcode.png)

Select this button to draw a barcode area in your **REFERENCE** board image to read it.

### **Help**

![Help button](assets/menu-help.png)

This button will get you to this **USER GUIDE**

### **Report**

![Finish inspection button](assets/menu-report.png)

Selecting this button will create a report that will includes the detected errors. This report could be a **OK** or **NOT OK** inspection depending the manufacturing criteria. To learn more about this feature go to the following [section](Generating%20_a_report.md).

### **Take REFERENCE photo**

![Take REFERENCE photo button](assets/menu-take-ref.png)

Take a photo of what will be a REFERENCE PCB/Panel. Shortcut: R

### **UUI to REFERENCE**

![UUI to REFERENCE button](assets/menu-uui-to-ref.png)

This function turns the current **UUI** image in a **REFERENCE**. This is useful when some of the components of the PCBA has been changed for a equivalent and the **Neural Network** detects it as an error due to a visual difference but the PCBA is correct. To learn more about this feature go to the following [section](UUI_to_REFERENCE.md).

### **Take an UUI photo**

![Take UUI photo button](assets/menu-take-uui.png)

Takes a photo of a **Unit Under Inspection** PCBA/Panel from the connected camera. Shortcut: s

### **Eraser**

![remove area button](assets/menu-rm-exclusion.png)

Deletes a drawn **exclusion area**.

### **Auto process**

![auto process button](assets/menu-auto-process.png)

If activated, the next photo taken will be **automatically** processed. That means that the image will be analyzed for faults right after being taken. This option reduces the processing time for every inspection.

!!!warning "Important"
    For **ONLINE UNITS** please note that each processed image will automatically be sent to our server and **will consume credits**. If you are testing how to take your photos we recommend to disable this function until you are sure the photos are good enough in order to avoid spending credits unnecessarily.

### **Settings**

![Settings button](assets/menu-settings.png)


With this button you can change other functions to suit your needs.


