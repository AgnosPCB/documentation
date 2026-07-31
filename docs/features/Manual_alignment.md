# Manual image alignment

For a more precised images alignment between the REFERENCE and the UUI images, the AgnosPCB Inspection Tool Software includes a manual alignment tool which increases the inspection precision.

## Video 
___

For a complete walkthrough of this feature, watch the following video:

<iframe width="100%" height="400" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

## 1. Enabling the manual alignment

!!! info "Note"
    This feature is only available for **1x1 images inspections**.

When capturing a new UUI image, activate the manual alignment from the Live Preview menu.

![Manual alignment option](../assets/v7/manual_align/manual-aling-button.png){.center}

## 2. Aligning the images

Just after the UUI image has been captured, the manual alignment window pops up showing both REFERENCE and UUI images.

![Manual alignment window](../assets/v7/manual_align/1-manual%20alignment.png){.center}

Now mark three reference points in the REFERENCE image.

!!! warning "Important"
    Select points easily reproducible between panels (Holes, pads, etc.) near to the corners of the panel and as far apart from each other as possible.

!!! note "Note"
    Use the mouse wheel to zoom the image and mark the points with more precision


![Marking first point](../assets/v7/manual_align/3-MA-P1.png){.center}

![Marking second point](../assets/v7/manual_align/4-MA-P2.png){.center}

![Marking third point](../assets/v7/manual_align/5-MA-P3.png){.center}

Once the three aligment points are defined in the REFERENCE image, mark **the same three points** in the UUI image.

!!! warning "Important"
    To ensure proper alignment, the points should be placed on the same reference points on the panel as far as possible.

![Marking first point](../assets/v7/manual_align/6-MA-UUI-P1.png){.center}

![Marking second point](../assets/v7/manual_align/7-MA-UUI-P2.png){.center}

![Marking third point](../assets/v7/manual_align/8-MA-UUI-P3.png){.center}

Once all the alignment points are placed, press the **ALIGN** button to start the process.
The software will align both images and then perform the inspection.
