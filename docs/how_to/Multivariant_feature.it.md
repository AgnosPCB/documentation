# Varianti di riferimento

Durante l'ispezione di un PCB, alcuni componenti possono differire dal riferimento ed essere rilevati dal software come errori (ad esempio, a causa di cambiamenti nella fornitura dei componenti o differenze di etichettatura).

Contrassegnando questo tipo di errore come **Variante di riferimento**, il sistema lo riconoscerà nelle future ispezioni e non lo segnalerà più come errore.

## Video
___

Per una panoramica completa di questa funzionalità, guarda il seguente video:
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Y79a7xYpsv0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

## 1. Avviare l'ispezione

[Crea un'immagine di riferimento](../how_to/Inspection_workflow.md#generating-a-reference) oppure selezionane una [dal repository](../how_to/Screen-layout.md#load-reference-as-file). Quindi, posiziona l'UUI e avvia l'ispezione.

## 2. Identificare l'errore

Naviga tra gli errori rilevati utilizzando i **tasti freccia sinistra/destra (←/→)**.

![Errore variante rilevato](../assets/ref-variant-error.png){ width=600 .center }

## 3. Classificare come Variante di riferimento

Premi il **tasto freccia giù (↓)** per rifiutare l'errore. Nel pannello di classificazione, seleziona **Reference variant**.

![Pannello di classificazione](../assets/ref-variant-label.png){ width=400 .center }

Comparirà una finestra di dialogo in cui dovrai inserire un nome per la nuova variante (obbligatorio) e, facoltativamente, aggiungere una descrizione. Una volta completato, premi **Confirm**.

## Risultato

Una volta classificata, la variante di riferimento viene salvata e collegata all'immagine di riferimento. Le varianti salvate possono essere visualizzate aprendo un'immagine di riferimento memorizzata. Sono mostrate nel pannello laterale destro, sotto la vista di riferimento ingrandita. Da questo pannello, le varianti possono essere abilitate, disabilitate o eliminate.

![Variante di riferimento salvata](../assets/ref-variant-sored.png){ width=600 .center }

Questa variante non verrà più segnalata come errore nelle future ispezioni.

!!! warning "Attenzione"
    Una variante di riferimento deve essere creata manualmente per ogni posizione sul PCB in cui compare la variazione. Il sistema non applica automaticamente la variante a componenti identici in altre posizioni.

![Errore variante rilevato](../assets/ref-variant-error.png){ width=400 .center }
![Freccia verde](../assets/green-arrow-down.png){ width=40 .center }
![Variante di riferimento](../assets/ref-variant-solved.png){ width=400 .center }

Anche dopo aver creato una variante di riferimento, il sistema continuerà a rilevare eventuali difetti reali su quel componente, qualora si verifichino.

Il report finale di ispezione includerà anche la variante di riferimento, insieme alla sua immagine, al nome assegnato e a eventuali osservazioni aggiuntive.

![Reference variant PDF report](../assets/ref-variant-report.png){width=600, .center}