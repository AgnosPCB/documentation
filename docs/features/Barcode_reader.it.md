# Lettore di codici a barre

Il software AgnosPCB incorpora una funzione di lettura di codici a barre che supporta **codici a barre 1D, QR e Datamatrix**.

È possibile scattare una foto di **RIFERIMENTO** o caricarne una direttamente dai propri file utilizzando il pulsante **"Apri riferimento"**.

![Area codice a barre selezionata](../assets/v7/ui-button4.png){.center}

Premete il pulsante **"disegna area codice a barre"** e disegnate un'area dove si trova un codice sul pannello, quindi definite di che tipo di codice si tratta: **ID, Batch ID, Model o Misc**. Ripetete questa operazione per ogni codice che volete far leggere al software, fino a **quattro** tipi diversi.

![Lettura del codice](../assets/v7/barcode/1-bc-menu.png){.center}

Se l'opzione **mandatory barcode** è attivata su un codice specifico, l'ispezione non continuerà finché quel codice non sarà stato letto correttamente. Se non viene rilevato automaticamente, all'operatore verrà richiesto di inserirlo manualmente prima di proseguire.

Una volta caricato il RIFERIMENTO, procedere con l'ispezione scattando una foto della UUI. Ciascuno dei codici della UUI verrà letto automaticamente nelle stesse aree definite sul RIFERIMENTO.

Procedere con il [processo di ispezione](../how_to/Inspection_workflow.md) come di consueto. 

Il codice scansionato sarà incluso nel report PDF finale della UUI.

![Report con codice a barre incluso](../assets/barcode-report.png){.center}

## Caricare un RIFERIMENTO tramite codice a barre

Se si dispone già di un **RIFERIMENTO** archiviato, è possibile recuperarlo facilmente utilizzando il codice ad esso associato. Per fare ciò, premere il pulsante **"leggi codice a barre"**, quindi leggere il codice a barre utilizzando il lettore portatile, e il **RIFERIMENTO** si caricherà automaticamente. È anche possibile inserire il codice manualmente.

![Caricamento RIFERIMENTO codice a barre](../assets/v7/ui-barcode-loading.png){.center}

![Caricamento RIFERIMENTO codice a barre](../assets/v7/ui-bc_ref.png){.center}

![Lettore di codici a barre portatile](../assets/barcode-handhold.png){.center}
