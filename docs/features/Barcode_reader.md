# Barcode reader

The AgnosPCB software incorporates a barcode reader function that supports **1D barcodes, QR and Datamatrix**.

You can either take a **REFERENCE** photo or upload one directly from your files using the **"Open reference"** button.


![Barcode area selected](../assets/v7/ui-button4.png){.center}

Press the **"draw barcode area"** button and draw an area where a code is placed on the panel, then define what type of code it is: **ID, Batch ID, Model or Misc**. Repeat this for every code you want the software to read — up to **four** different types.

![Barcode read](../assets/v7/barcode/1-bc-menu.png){.center}

If the **mandatory barcode** option is set on a specific code, the inspection won't continue until that code has been read successfully. If it isn't detected automatically, the operator is prompted to enter it manually before proceeding.

Once the REFERENCE is loaded, proceed with the inspection by taking a picture of the UUI. Each of the UUI's codes will be read automatically from the same areas defined on the REFERENCE.

Proceed with the [inspection process](../how_to/Inspection_workflow.md) as usual. 

The scanned codes will be included in the final PDF report of the UUI.

![Report with barcode included](../assets/barcode-report.png){.center}

## Load a REFERENCE by barcode

If you already have a **REFERENCE** stored, you can easily retrieve it using the code associated with it. To do this, press the **"read barcode"** button, then read the barcode using the handheld reader, and the **REFERENCE** will load automatically. It is also possible to enter the code manually.

![Barcode REFERENCE loading](../assets/v7/ui-barcode-loading.png){.center}

![Barcode REFERENCE loading](../assets/v7/ui-bc_ref.png){.center}

![Barcode handhold](../assets/barcode-handhold.png){.center}
