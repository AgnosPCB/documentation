# Manual image alignment

When the REFERENCE and UUI images need to be aligned more precisely than the automatic alignment allows, the AgnosPCB software includes a manual alignment tool that improves the accuracy of the inspection.


## 1. Enabling the manual alignment

!!! info "Note"
    This feature is only available for **1x1 images inspections**.

When capturing a new UUI image, activate the manual alignment from the settings menu.

![Manual alignment option](../assets/v7/manual_align/1-manual-alignment-option.png){.center}

Then, during the UUI image capturing, activate the manual alignment option.

![Manual alignment option](../assets/v7/manual_align/manual-aling-button.png){.center}

## 2. Aligning the images

Just after the UUI image has been captured, the manual alignment window pops up showing both REFERENCE and UUI images.

![Manual alignment window](../assets/v7/manual_align/2-MA-zoom.png){.center}

Now mark three reference points in the REFERENCE image.

!!! warning "Important"
    Choose points that are easy to reproduce from panel to panel (holes, pads, etc.), close to the corners of the panel and as far apart from each other as possible.

!!! note "Note"
    Use the mouse wheel to zoom into the image and mark the points more precisely.


![Marking first point](../assets/v7/manual_align/3-MA-P1.png){.center}

![Marking second point](../assets/v7/manual_align/4-MA-P2.png){.center}

![Marking third point](../assets/v7/manual_align/5-MA-P3.png){.center}

Once the three alignment points are defined in the REFERENCE image, mark **the same three points** in the UUI image.

!!! warning "Important"
    To ensure a correct alignment, place each point on exactly the same feature of the panel as in the REFERENCE image.

![Marking first point](../assets/v7/manual_align/6-MA-UUI-P1.png){.center}

![Marking second point](../assets/v7/manual_align/7-MA-UUI-P2.png){.center}

![Marking third point](../assets/v7/manual_align/8-MA-UUI-P3.png){.center}

Once all the alignment points are placed, press the **ALIGN** button to start the process. The software aligns both images and then performs the inspection.

![Images aligned](../assets/v7/manual_align/MA-final.png){.center}
