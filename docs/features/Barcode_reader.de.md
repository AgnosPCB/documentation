# Barcode-Lesegerät

Die AgnosPCB-Software enthält eine Barcode-Lesefunktion, die **1D-Barcodes, QR und Datamatrix** unterstützt.

Sie können entweder ein **REFERENZ**-Foto aufnehmen oder eines direkt aus Ihren Dateien über die Schaltfläche **"Referenz öffnen"** hochladen.

![Ausgewählter Barcode-Bereich](../assets/v7/ui-button4.png){.center}

Drücken Sie die Schaltfläche **"Barcode-Bereich zeichnen"** und zeichnen Sie einen Bereich, in dem sich ein Code auf der Platine befindet. Legen Sie anschließend fest, um welchen Codetyp es sich handelt: **ID, Batch ID, Model oder Misc**. Wiederholen Sie dies für jeden Code, den die Software lesen soll — bis zu **vier** verschiedene Typen.

![Code-Lesevorgang](../assets/v7/barcode/1-bc-menu.png){.center}

Ist die Option **mandatory barcode** für einen bestimmten Code aktiviert, setzt die Software die Inspektion erst fort, wenn dieser Code erfolgreich gelesen wurde. Wird er nicht automatisch erkannt, wird der Bediener aufgefordert, ihn manuell einzugeben, bevor fortgefahren werden kann.

Sobald die REFERENZ geladen ist, fahren Sie mit der Inspektion fort, indem Sie ein Bild der UUI aufnehmen. Jeder Code der UUI wird automatisch in den auf der REFERENZ festgelegten Bereichen gelesen.

Fahren Sie mit dem [Inspektionsprozess](../how_to/Inspection_workflow.md) wie gewohnt fort. 

Der gescannte Code wird in den endgültigen PDF-Bericht der UUI aufgenommen.

![Bericht mit enthaltenem Barcode](../assets/barcode-report.png){.center}

## Eine REFERENZ per Barcode laden

Wenn Sie bereits eine **REFERENZ** gespeichert haben, können Sie diese einfach mithilfe des zugehörigen Codes abrufen. Drücken Sie dazu die Schaltfläche **"Barcode lesen"**, lesen Sie dann den Barcode mit dem Handscanner, und die **REFERENZ** wird automatisch geladen. Es ist auch möglich, den Code manuell einzugeben.

![REFERENZ per Barcode laden](../assets/v7/ui-barcode-loading.png){.center}

![REFERENZ per Barcode laden](../assets/v7/ui-bc_ref.png){.center}

![Handscanner für Barcode](../assets/barcode-handhold.png){.center}
