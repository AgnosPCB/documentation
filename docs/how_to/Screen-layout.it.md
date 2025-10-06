# Interfaccia Utente

## **Aree di lavoro principali**

L'immagine seguente descrive le aree di lavoro principali del **software di ispezione AgnosPCB**.

![Sezione principale](../assets/v7/ui-layout.png){.center}

## **Stato della piattaforma**

![Area stato](../assets/v7/ui-status.png){.center}

Quest'area visualizza lo stato della connessione con la piattaforma di ispezione e la telecamera. Se la connessione fallisce, le icone diventeranno rosse. Quest'area contiene anche i seguenti pulsanti di azione:

### **Avvia ispezione**


![Pulsante Avvia ispezione](../assets/autoprocess.png){.center}

Il pulsante **Avvia ispezione** avvia l'ispezione dell'immagine **UUI** corrente. Questo pulsante è disponibile quando il [pulsante Processo automatico](#auto-process) è impostato su **OFF**. Questo è utile per evitare di spendere crediti quando si sta testando come scattare foto delle proprie PCBA.

### **Caricamento RIFERIMENTO tramite codice a barre**

![Caricamento RIFERIMENTO codice a barre](../assets/v7/ui-barcode-loading.png){.center}

![Caricamento RIFERIMENTO codice a barre](../assets/v7/ui-bc_ref.png){.center}

Questo pulsante apre una finestra pop-up per inserire un numero di codice a barre. Quando si genera un RIFERIMENTO, qualsiasi [codice a barre che esso contiene può essere letto](#barcode-area-drawing). Questo codice a barre sarà associato al RIFERIMENTO e potrà essere caricato utilizzando quel numero con questa funzione. È anche possibile leggere il codice a barre con un lettore portatile e inserirlo in questo campo. Maggiori informazioni su questa funzionalità [qui](./Barcode_reader.md#load-a-reference-by-barcode).

## **Registro attività**


![Sezione funzionamento interno](../assets/activity-log.png){.center}

L'area del **registro attività** si trova in alto a destra e mostra i **crediti attualmente disponibili** e i dettagli operativi dell'applicazione, come lo stato del processo di analisi.


## **Area di lavoro principale**


![Sezione principale](../assets/v7/ui-working-area.png){.center}

Questa è la sezione principale in cui si lavora con le immagini di **RIFERIMENTO** e **UUI**, che possono essere scambiate premendo il tasto TAB sulla tastiera o [il pulsante sull'applicazione](#swap). I risultati dell'ispezione vengono visualizzati anche in quest'area utilizzando reticoli e numeri accanto agli errori rilevati.


## **Confronto affiancato**


![Sezione confronto](../assets/v7/ui-side_by_side.png){width=400px; .center}

Questa sezione dell'interfaccia è divisa in due parti. La parte superiore visualizza l'immagine di **RIFERIMENTO**, che funge da standard per il confronto, mentre la parte inferiore mostra l'immagine **UUI**. Queste immagini sono ingrandite e si muovono in parallelo mostrando esattamente la stessa area nel **RIFERIMENTO** e nell'**UUI** dove punta il cursore nell'area di lavoro principale.


## **Pannello pulsanti**


![Area pulsanti](../assets/v7/ui-main_buttons.png){.center}

Qui si trovano diverse **funzioni e opzioni** progettate per **ottimizzare** il flusso di lavoro e velocizzare le attività. Ogni funzionalità è definita di seguito:

### **Mosaico di riferimenti**

![Pulsante Mosaico di riferimenti](../assets/v7/ui-button1.png){width=350px; .center}

![Menu Mosaico](../assets/v7/2024-11-14_09-27.png){width=600px; .center}

Il mosaico di riferimenti viene utilizzato per archiviare i RIFERIMENTI come file per trovarli e caricarli rapidamente. Il menu mosaico appare automaticamente dopo aver acquisito un RIFERIMENTO utilizzando il [pulsante scatta foto RIFERIMENTO](#take-a-reference-image) o caricandolo [come file](#load-reference-as-file). In questa finestra è anche possibile nominare il RIFERIMENTO acquisito nella parte in alto a destra della finestra. Un RIFERIMENTO memorizzato nel mosaico può essere caricato rapidamente premendo un **pulsante F** (F1-F10).

### **CARICA RIFERIMENTO come file**

![Pulsante Apri riferimento](../assets/v7/ui-button2.png){width=350px; .center}

![Menu Carica RIFERIMENTO](../assets/v7/ui-ref_search.png){.center}

Utilizzare questa icona per caricare un'immagine precedentemente catturata come **RIFERIMENTO** e consente di ordinarle per nome o data. Tutte le immagini di **RIFERIMENTO** si trovano all'interno della cartella **APP/REFERENCE** in una cartella denominata in base all'ora in cui è stata scattata la foto.

!!! note "Nota"
    Dalla versione 7, il software **non consente** di caricare immagini acquisite da fonti diverse dalla piattaforma stessa poiché le immagini contengono parametri specifici per l'ottica. Ogni immagine di RIFERIMENTO deve essere acquisita utilizzando l'**AI-4050 AOI**.

### **Scambia**
 
![Pulsante Scambia](../assets/v7/ui-button3.png){width=350px; .center}

Alterna tra le immagini di **RIFERIMENTO** e **UUI** nell'[area di lavoro principale](#main-workspace).

### **Disegno area codice a barre**

![Pulsante Apri UUI](../assets/v7/ui-button4.png){width=350px; .center}

![Pulsante Apri UUI](../assets/v7/ui-bc_box.png){.center}

Fare clic su questo pulsante per disegnare manualmente un rettangolo nell'immagine di **RIFERIMENTO** dove è presente un codice a barre. Il software lo leggerà e utilizzerà quel codice per nominare le immagini e includerlo nel **report PDF** finale. Maggiori informazioni sulla funzione di lettura del codice a barre nella [sezione seguente](./Barcode_reader.md).


### **Esclusione**

![Pulsante Esclusione](../assets/v7/ui-button5.png){width=350px; .center}

![Disegna un'area di esclusione](../assets/v7/ui-draw_exclusion.png){.center}

Crea un'area di esclusione dove il sistema non cercherà difetti. È possibile creare tutte le aree necessarie. Questa funzione è dettagliata nella [sezione seguente](Set_exclusion_area.md).

### **Sensibilità**

![Pulsante Sensibilità](../assets/v7/ui-button6.png){width=350px; .center}

Se il processo di produzione richiede un controllo qualità più rigoroso, è possibile aumentare la sensibilità di rilevamento degli errori con questa funzionalità. Aumentando la sensibilità, il software segnalerà errori che normalmente non segnalerebbe con un'impostazione di sensibilità inferiore. Ci sono tre livelli di sensibilità: Normale, Alta e Molto Alta. Può essere impostata utilizzando i tasti 1, 2, 3 della tastiera. Questa funzione è dettagliata nella [sezione seguente](./Set_sensitivity.md).

### **Aiuto**

![Pulsante Aiuto](../assets/v7/ui-button7.png){width=350px; .center}

Questo pulsante vi indirizzerà a questa documentazione.

### **Risultato finale**

![Pulsante Termina ispezione](../assets/v7/ui-button8.png){.center}

![OK o NON OK](../assets/v7/ui-finish_inspection.png){.center}

Una volta che gli errori rilevati sono stati supervisionati dall'operatore, l'ispezione può essere completata premendo questo pulsante e, a seconda dei criteri di produzione, contrassegnare la PCBA ispezionata come **OK** o **NON OK**. Dopodiché, il software creerà un report che include gli errori segnalati dall'operatore su un documento PDF. Per saperne di più su questa funzionalità, consultare la [sezione seguente](./Inspection_workflow.md#generating-a-final-pdf-report).

### **Scatta un'immagine di RIFERIMENTO**

![Pulsante Scatta immagine RIFERIMENTO](../assets/v7/ui-button9.png){.center}

![Finestra RIFERIMENTO](../assets/v7/2024-11-14_09-26.png){.center}


Questo pulsante apre una finestra con le utilità per generare un'immagine di **RIFERIMENTO** da una PCB o pannello. Questa funzione può essere attivata premendo il tasto **r** sulla tastiera. Nella sezione [generare un riferimento](./Inspection_workflow.md/#generating-a-reference) imparerete di più su questa funzione.


### **UUI a RIFERIMENTO**

![Pulsante UUI a RIFERIMENTO](../assets/v7/ui-button10.png){.center}

Questa funzione trasforma l'immagine **UUI** corrente in un **RIFERIMENTO**. Ciò è utile quando alcuni dei componenti della PCBA sono stati cambiati con un equivalente e la **Rete Neurale** lo rileva come un errore a causa di una differenza visiva, ma la PCBA è corretta. Per saperne di più su questa funzionalità, consultare la [sezione seguente](UUI_to_REFERENCE.md).

### **Scatta un'immagine UUI**

![Pulsante Scatta immagine UUI](../assets/v7/ui-button11.png){.center}

![Finestra UUI](../assets/v7/ui-uui_preview.png){.center}

Questa funzione apre una finestra con un'anteprima in tempo reale dell'area di ispezione. Una volta che la PCBA è posizionata correttamente, premere il pulsante **Avvia ispezione** per scattare una foto o più foto della PCBA/Pannello dell'**Unità Sotto Ispezione**. Se il [pulsante processo automatico](#auto-process) è attivo, l'ispezione inizierà automaticamente non appena viene acquisita l'immagine UUI. Questa funzione può anche essere attivata premendo il tasto **s** sulla tastiera o il pulsante di azione fisico situato sul lato destro dell'AOI. Consultare la [sezione seguente](./Inspection_workflow.md/#capturing-an-uui) per saperne di più su questa funzionalità.


### **Gomma**

![Pulsante Rimuovi area](../assets/v7/ui-button12.png){.center}

Elimina un'[**area di esclusione**](./Set_exclusion_area.md) disegnata.

### **Processo automatico**

![Pulsante processo automatico](../assets/v7/ui-button13.png){.center}

Se attivato, la successiva foto **UUI** scattata verrà elaborata **automaticamente**. Ciò significa che l'immagine verrà analizzata per i difetti subito dopo essere stata scattata. Si consiglia di abilitare questa funzione per velocizzare il processo di ispezione.

!!!warning "Importante"
    Per le **UNITÀ ONLINE**, si prega di notare che ogni immagine UUI scattata verrà inviata automaticamente al nostro server per l'elaborazione e **consumerà crediti**. Se si sta solo testando come scattare le foto, si consiglia di disabilitare questa funzione fino a quando non si è sicuri che le foto coprano correttamente la PCBA.

### **Impostazioni**

![Pulsante Impostazioni](../assets/v7/ui-button14.png){.center}


Questo pulsante apre il [menu impostazioni](./Settings_menu.md).
