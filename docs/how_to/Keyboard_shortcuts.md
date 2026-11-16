# Keyboard shortcuts

This page lists every keyboard shortcut available in the **AgnosPCB inspection software**, together with the mouse actions used to review the detections.

## Main window

| Key | Action |
| --- | --- |
| ++r++ | [Take a REFERENCE image](Inspection_workflow.md#generating-a-reference) (opens the live preview). |
| ++s++ | [Start an inspection](Inspection_workflow.md#capturing-an-uui) (capture the UUI). |
| ++tab++ | Switch the view mode of the [main workspace](Screen-layout.md#main-workspace) (REFERENCE / UUI). |
| ++page-up++ | Switch to the **TOP** side of the loaded REFERENCE (double-sided REFERENCES only). |
| ++page-down++ | Switch to the **BOTTOM** side of the loaded REFERENCE (double-sided REFERENCES only). |
| ++f1++ … ++f8++ | Load the REFERENCE stored in that slot of the [Reference mosaic](Screen-layout.md#reference-mosaic). |
| ++arrow-right++ | Next detection (or next row of the detections list with [Analysis preference](Settings_menu.md#analysis-preference) = **LIST**). |
| ++arrow-left++ | Previous detection (or previous row of the detections list with Analysis preference = **LIST**). |
| ++arrow-up++ | [Report](Inspection_workflow.md#reporting-errors) the detection as an **actual error** (opens the reporting window). On an area with no detection, reports an error not detected by the software. |
| ++arrow-down++ | Report the detection as a **false positive**. |
| ++1++ | [Sensitivity](Set_sensitivity.md): Normal. |
| ++2++ | Sensitivity: High. |
| ++3++ | Sensitivity: Very High. |
| ++space++ | Turn the platform lighting on / off. |
| ++f++ | Show / hide the error report overlay. |
| ++enter++ | Process an image loaded manually. |

!!! note "Note"
    With [user access control](../features/User_control.md) enabled, the ++arrow-up++ and ++arrow-down++ keys require the **Classify detected faults** permission.

## Reviewing detections with the mouse

| Mouse action (on the image) | Action |
| --- | --- |
| Left click on a detection | Report it as an **actual error** (same as ++arrow-up++). On a detection already reported as an error, asks for confirmation before undoing it. |
| Right click on a detection | Report it as a **false positive** (same as ++arrow-down++). |
| Left click on an empty area | Report an error not detected by the software. |
| Keep the pointer still on a detection for about 1 second | Mark it as **seen**. |
| Right click outside a detection | Change the shape of the zoom lens. |
| ++shift++ + right click | Change the shape of the zoom lens, also on top of a detection. |
| Mouse wheel | Change the zoom level. |

The mouse actions of the detections list (thumbnails, buttons, scrolling) are described in [Detections list](Screen-layout.md#detections-list).

## Reporting window

| Key | Action |
| --- | --- |
| ++arrow-up++ / ++arrow-down++ | Move through the options of the drop-down list. |
| ++enter++ | Confirm. |
| ++esc++ | Cancel. |

## Other windows

| Window | Key | Action |
| --- | --- | --- |
| Live preview (REFERENCE / UUI) | ++enter++ | Confirm / OK. |
| Live preview (REFERENCE / UUI) | ++esc++ | Cancel. |
| Reference mosaic | ++f1++ … ++f8++ | Load the REFERENCE of that slot. |
| REFERENCE search list | ++esc++ | Close the window without loading a REFERENCE. |
| Login | ++enter++ | Log in. |
| Settings menu | ++enter++ | OK (save and close). |
| Settings menu | ++esc++ | Close. |
