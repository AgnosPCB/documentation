In this guide we will learn how to use the conformal coating inspection using the **AgnosPCB AOI**.

This feature allows operators to visually inspect the conformal coating on PCBAs using UV lighting.

!!! note "Note"
    This function requires installing a separate hardware kit. To install the UV kit, follow the instructions in the following section:
    [UV conformal coating installation guide](../maintenance/UV_kit_install.md)

!!! warning "Caution"
    The conformal coating inspection uses UV lighting so **we recommend to use the safety glasses** included with the kit.


    ![UV warning](../assets/v7/UV_inspection/warning_icon.png){width=200px, .center}

## Video 
___

For a complete walkthrough of this feature, watch the following video:
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/NfidLIuWdqY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___


## 1. Generate a REFERENCE image or load it

To generate a **REFERENCE** image follow the steps in the [following guide](../how_to/Inspection_workflow.md#generating-a-reference) or [load a previous REFERENCE](../how_to/Screen-layout.md#load-reference-as-file).

## 2. Open the Live View

Use the UUI capture button to open the [Live View window](../how_to/Inspection_workflow.md#capturing-an-uui) of the current PCBA.

![Live view window](../assets/UUI photo.PNG){width=100px, .center}

## 3. Enable UV inspection

In the Live View window, enable the **UV inspection option** located at the bottom of the interface.

![UV preview](../assets/v7/UV_inspection/UV_buttom.png){.center}

Once enabled, a simulation of the PCB under UV lighting will be displayed.

![UV simulation](../assets/v7/UV_inspection/UV_active.png){.center}


!!! warning "Caution"
    From this point onwards, it is mandatory to wear the safety glasses included with the kit.


    ![UV warning](../assets/v7/UV_inspection/warning_icon.png){width=100px, .center}

Then, place the UUI at the center of the inspection area and press the **Start Inspection** button to begin the inspection process.

![UV preview](../assets/v7/UV_inspection/start-inspection-button.png){width=250px, .center}

## 4. Inspect the coating

Observe the PCB under UV lighting to verify the correct application and coverage of the conformal coating.

![UV preview](../assets/v7/UV_inspection/UV_inspection.png){.center}

!!! note "Note"
    This inspection is performed manually by the operator. No AI-based detection is involved, so the operator must visually identify any defects or missing coating.

The captured UV image is included in the final inspection report for documentation and traceability purposes.

![UV inspection report](../assets/v7/UV_inspection/UV_report.png){width=500px, .center}
