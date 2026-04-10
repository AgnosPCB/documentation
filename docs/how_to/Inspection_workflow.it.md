# **Flusso di lavoro dell'ispezione**
___

### **Avvio del software**
___

- Collegare l'alimentazione alla piattaforma di ispezione sul pannello posteriore
- Accendere il monitor
- Collegare l'alimentazione al computer e accenderlo
- Una volta che il sistema si è avviato, aprire l'app facendo doppio clic sull'icona del desktop
- **Solo per unità ONLINE**: apparirà una finestra di accesso che richiederà le credenziali dell'account AgnosPCB. Le credenziali verranno memorizzate nell'unità per usi futuri e non sarà richiesto di accedere nuovamente.

![Finestra di login](../assets/v7/uui-login.png){.center}

## **Procedura di ispezione**

___

<iframe width="100%" height="400" src="https://www.youtube.com/embed/FirteJF0U1E?si=IiWu4CkiELWYecYR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

### **Generazione di un RIFERIMENTO**

Il software AgnosPCB Inspection tool **"confronterà"** la fotografia del circuito/pannello di **RIFERIMENTO** ("golden sample") con tutte le foto che scatterete del circuito da ispezionare (foto da "ANALIZZARE").

!!!warning "Importante"
    Si consiglia di visitare la nostra sezione [suggerimenti](../help/Tips.md) prima di scattare la prima immagine.

Per procedere con l'acquisizione del RIFERIMENTO, fare clic sull'icona del riferimento nel menu principale:

![Pulsante REF](../assets/v7/ui-button9.png){.center}

Apparirà una nuova finestra con diversi strumenti:

![Finestra REF](../assets/v7/uui-ref_livepreview.png)

In questa finestra dobbiamo impostare le immagini necessarie per coprire l'intera PCBA.

![Dimensioni REF](../assets/v7/uui-ref_livepreview-dimensions.png)

---
#### Acquisizione delle dimensioni del PCB

Per PCBAs di grandi dimensioni, il campo visivo della telecamera potrebbe non essere sufficiente per catturare l'intera scheda in una singola immagine. In questi casi, il sistema acquisisce più immagini e le unisce automaticamente tramite IA in un'unica immagine pronta per l'ispezione.

![Processo di stitching](../assets/stitching.png){ width=600 .center }

Se non sei sicuro di quante immagini siano necessarie, posiziona il PCBA al centro dell'area di ispezione e premi il pulsante **AUTO**. Il sistema eseguirà la scansione della scheda e configurerà automaticamente i parametri ottimali.

![Pulsante AUTO di riferimento](../assets/v7/uui-ref_livepreview-auto.png){ .center }

Puoi anche spostare la telecamera in qualsiasi quadrante del PCBA facendo clic sull'area desiderata nella vista in miniatura.

![Mappa dei quadranti](../assets/v7/uui-ref_livepreview-map.png){ .center }

---

#### Messa a fuoco

Il sistema consente la messa a fuoco manuale del PCB prima di avviare il processo di acquisizione. Premi il pulsante **FOCUS** per regolare l'ottica e verificare che l'area selezionata sia correttamente a fuoco.

![Pulsante FOCUS](../assets/v7/uui-ref_livepreview-focus.png){ .center }

Per impostazione predefinita, la telecamera mette a fuoco automaticamente il centro del PCB. Tuttavia, questa non è sempre l'area ottimale a causa della presenza di componenti alti.

Per un'ispezione accurata, è essenziale mettere a fuoco la **base del PCB**, dove sono montati i componenti. Evita di mettere a fuoco componenti alti, poiché ciò può ridurre la precisione dell'ispezione.

Il PCB non deve essere centrato durante la messa a fuoco manuale. L'operatore può spostarlo liberamente e selezionare qualsiasi area adatta per ottenere una corretta messa a fuoco, purché la base del PCB sia chiaramente a fuoco.

Una volta completato il processo di messa a fuoco, il PCB deve essere riposizionato al centro dell'area di ispezione prima di acquisire l'immagine di riferimento.

!!! warning "Importante"
    Seleziona un'area senza componenti alti e assicurati che la base del PCB sia perfettamente a fuoco.

La parte inferiore della finestra consente di attivare o disattivare la griglia nella vista live e di regolare l'esposizione.

![Barra inferiore di riferimento](../assets/v7/uui-ref_livepreview-exposure.png){ .center }

![Selezione della messa a fuoco](../assets/v7/uui-ref_livepreview-select_focus.png){ .center }

---

Per avviare l'elaborazione dell'acquisizione, è sufficiente fare clic sul pulsante **CATTURA RIFERIMENTO**. L'AOI metterà a fuoco automaticamente nel quadrante selezionato e inizierà a catturare l'intera PCBA in pochi secondi.

![Pulsante Cattura riferimento](../assets/v7/uui-ref_livepreview-capture.png){.center}

![Processo di acquisizione](../assets/v7/uui-ref_stitching.png){.center}

Dopo aver catturato la PCBA, apparirà la finestra del mosaico che consente di archiviare l'immagine per un utilizzo rapido.

!!! note "Nota"
    Tutti i RIFERIMENTI acquisiti verranno archiviati automaticamente. Il mosaico aiuta a caricare rapidamente i RIFERIMENTI più utilizzati.

![Processo di acquisizione](../assets/v7/ui-mosaic_after_ref.png){.center}

Una volta terminato il processo di acquisizione, l'immagine di RIFERIMENTO verrà visualizzata nella finestra principale e vi consentirà di impostare [maschere di esclusione](Set_exclusion_area.md) o [disegnare un'area codice a barre](Barcode_reader.md) per la lettura.

![Immagine di riferimento](../assets/v7/ui-reference.png){.center}

### **Acquisizione di una UUI**

Dopo aver generato o caricato una precedente immagine di RIFERIMENTO, possiamo procedere con l'acquisizione dell'immagine **UUI** (Unità Sotto Ispezione) premendo il pulsante.

![Pulsante UUI](../assets/v7/ui-button11.png){.center}

Apparirà una finestra di anteprima live che mostra un'immagine fantasma dell'immagine di RIFERIMENTO. Questo aiuta ad allineare la PCBA UUI con il RIFERIMENTO.

!!! warning "Importante"
    Il software **AgnosPCB** è in grado di allineare automaticamente entrambe le immagini (**RIFERIMENTO** e **UUI**). Tuttavia, è importante posizionare correttamente la PCBA UUI per evitare deformazioni geometriche che possono causare rilevamenti di falsi positivi.

![Anteprima live UUI](../assets/v7/ui-uui_preview.png){.center}

Il processo di acquisizione inizierà facendo clic sul pulsante **AVVIA ISPEZIONE**.

!!! note "Nota"
    La messa a fuoco non è necessaria poiché il parametro di messa a fuoco è già memorizzato con l'immagine di RIFERIMENTO, rendendo l'ispezione molto veloce.

Il processo di ispezione sarà eseguito in parallelo in caso di ispezione multi-immagine.

Una volta terminato il processo di acquisizione, verrà restituito il risultato finale che mostra gli errori rilevati, se presenti. È possibile modificare la [sensibilità di rilevamento](Set_sensitivity.md) premendo il pulsante nella finestra principale o premendo il **tasto 1, 2 o 3.**

![Pulsante Sensibilità](../assets/v7/ui-button6.png){.center}

![Inferenza UUI](../assets/v7/ui-uui_report.png){.center}

Se vengono rilevati errori, apparirà una **cornice rossa** attorno alla finestra principale. **Cornice verde** se non ci sono errori.

### **Segnalazione degli errori**

Una volta completata l'ispezione, l'operatore deve monitorare gli errori segnalati, contrassegnandoli come **errore effettivo** o **rilevamento falso positivo**.
Per fare ciò, è sufficiente scorrere gli errori utilizzando le **frecce sinistra e destra** sulla tastiera.

Per contrassegnare un errore reale, basta spostarsi sul difetto e premere la **freccia su** sulla tastiera. Apparirà una nuova finestra che mostra il difetto in dettaglio e consente di classificarlo selezionando un tipo di difetto dall'elenco.

![Finestra di segnalazione](../assets/v7/ui-report.png){.center}

Inoltre, c'è un campo vuoto per **aggiungere un commento.**

Nel caso in cui l'operatore trovi un errore **non rilevato** dal software, è possibile segnalarlo e riportarlo spostando il cursore sull'area del difetto e premendo il **tasto freccia su**. La finestra di segnalazione apparirà come di consueto. 

Quando il software segnala un'area che non è un errore effettivo, l'operatore può contrassegnarla come **falso positivo** premendo il **tasto freccia giù**. Apparirà anche una finestra che consente di aggiungere un commento.

![Finestra falso positivo](../assets/v7/ui-fp_report.png){.center}

!!! note "Nota"
    Si noti che l'**icona rossa** ![Icona rossa](../assets/v7/ui-report_red.png){width=20px} contrassegna i difetti effettivi e l'**icona verde** ![Icona verde](../assets/v7/ui-report_green.png){width=20px} i difetti falso positivo.

### **Generazione di un report PDF finale**

Una volta terminata la segnalazione, l'operatore può generare un report PDF finale premendo il seguente pulsante:

![Report finale](../assets/v7/ui-button8.png){.center}

Appare una finestra che consente di contrassegnare l'ispezione come **OK** o **NON OK**. Se la PCBA supera il controllo qualità con successo, premere l'icona verde.

![OK NOK](../assets/v7/ui-finish_inspection.png){.center}

È possibile aggiungere commenti che verranno inclusi nel report. Il PDF verrà generato nella cartella **REPORTS**.

![Report PDF](../assets/v7/pdf-report1.png){.center}

![Report PDF](../assets/v7/pdf-report2.png){.center}