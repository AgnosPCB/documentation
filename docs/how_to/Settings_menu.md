# Settings menu

The **settings menu** is divided into several sections, which are described below.

![Settings menu](../assets/v7/ui-settings.png){.center}

## **Interface options**

![Settings menu interface section](../assets/v7/ui-settings-interface.png){width=350px; .center}

#### Show exif

Displays the metadata of the current image in the [main workspace area](./Screen-layout.md#main-workspace).

#### Show workspace icons

Enable a set of features in the main [main workspace area](./Screen-layout.md#main-workspace). Learn more about these features in the [next section](./Workspace_icons.md).

#### Auto signaling

By default, the software will numerate the errors after the inspection. Disabling this option, only the affected area will be highlighted in color.

#### Mask color

This option allows you to change the color of the marked error. When the color of the marked error matches the color of the PCBA, it's advisable to change it to a higher contrast color to make the marked areas more visible.

#### Language

Change the interface language. The current available laguanges are: **English, French, German, Italian and Spanish**.

## **Workflow options**

![Settings menu workflow section](../assets/v7/ui-settings-workflow.png){width=350px; .center}

#### Auto process

Toggles the [auto process function](./Screen-layout.md#auto-process).

#### Use barcode

Toggles the [barcode reading function](./Barcode_reader.md)

#### Auto process PCB_IN folder

Enabling this, all the **UUI images** contained in the **APP/PCB_IN** folder will be automatically process using the loaded REFERENCE in the application. This function is only available on the **ONLINE** version.

!!! warning "Warning"
    Since version 7 this feature is no longer operative.

#### Show errors popup

By disabling this option, the reporting window will no longer popup when reporting an error with **UP** or **DOWN** arrow. The reported errors will be generated with the "**other**" label in the final PDF report.

#### Show references mosaic

By disabling this option, the mosaic menu won't popup after taking a **REFERENCE** image.

#### Operator mode

Enabling this option will hide several features from the interface, simplifying the software's use. It also prevents the operator can change the REFERENCE image or the sensivity of the inspections. A [password](Settings_menu.md#settings-password) can be added so that only the administrator can disable this option.

#### Sensitivity enabled

It allows you to change sensivity when in operator mode.

## **Report options**

![Settings menu report section](../assets/v7/ui-settings-report.png){width=350px; .center}

#### Operator ID

Set an ID for the current operator. This ID will be displayed in the final PDF report after the inspection is complete.

#### Order ID

Set an ID for the current manufacturing order. This ID will be displayed in the final PDF report after the inspection is complete.

#### Platform ID

Set an ID for the AOI. 

#### TAG

Set the TAG (OK or NOK) of the final PDF report as a suffix or a prefix to the file name.

#### TAG OK

Set a custom OK TAG for the final PDF report. 

#### TAG NO OK

Set a custom NO OK TAG for the final PDF report.

#### Auto report

When this option is enabled, a final PDF report labeled OK will be automatically generated if no errors are detected after the inspection. The final PDF report can also be generated if any errors are detected during the inspection.

!!! note "Note"
    When generating a PDF report automatically, all errors detected will be marked with the "unknown" label.

#### Show all faults

Displays all detected errors in the PDF report even if the operator has not reported them.

#### Logo

Set a logo for the PDF report.

## **Date/time options**

![Settings menu date section](../assets/v7/ui-settings-date.png){width=350px; .center}

#### Time zone

Set the time zone.

#### Date and time

Set day and time.

!!! note "Note"
    To apply the changes press the **SET** button and reboot the system.

## **Path option**

![Settings menu path section](../assets/v7/ui-settings-path.png){width=350px; .center}

#### PCB OUT

Change the path where the inspections are generated.

## **Share options**

![Settings menu share section](../assets/v7/ui-settings-share.png){width=350px; .center}

#### Share folders

By enabling these options, the system will automatically share the PCB_OUT and REFERENCE folders in your local network. The access address will be displayed once the option is set.

!!! note "Note"
    To apply the changes press the **SET** button.

!!! note "Note"
    For the OFFLINE units, if you need to change the network interface of your unit, please refer to the [network configuration article](./network_configuration.md).

## **Info section**

![Settings menu info section](../assets/v7/ui-settings-info.png){width=650px; .center}

#### AOI info

The AOI information is displayed in this section.

#### Backup

This function generates a backup compressed file of the PCB_OUT folder automatically. The backup file is stored in the **APP/BACKUP** folder.

#### Settings password

Set a password to access the settings menu.

!!! note "Note"
    Set the password to blank to disable the password requirement.