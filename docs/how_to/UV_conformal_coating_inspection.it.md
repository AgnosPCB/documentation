# Ispezione del rivestimento conformale UV
In questa guida impareremo come utilizzare l'ispezione del rivestimento conformale usando **AgnosPCB AOI**.

Questa funzione consente agli operatori di ispezionare visivamente il rivestimento conformale sui PCBA utilizzando l'illuminazione UV.

!!! note "Nota"
    Questa funzione richiede l'installazione di un kit hardware separato. Per installare il kit UV, seguire le istruzioni nella seguente sezione:
    [Guida all'installazione del rivestimento conformale UV](../maintenance/UV_kit_install.md)

!!! warning "Attenzione"
    L'ispezione del rivestimento conformale utilizza illuminazione UV, quindi **si consiglia di utilizzare gli occhiali di sicurezza** inclusi nel kit.

    ![Avviso UV](../assets/v7/UV_inspection/warning_icon.png){ width=200px .center }

## Video
___

Per una panoramica completa di questa funzionalità, guarda il seguente video:
 
<iframe width="100%" height="400" src="." title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

## 1. Generare un'immagine di RIFERIMENTO o caricarla

Per generare un'immagine di **RIFERIMENTO**, segui i passaggi nella [seguente guida](../how_to/Inspection_workflow.md#generating-a-reference) oppure [carica un RIFERIMENTO precedente](../how_to/Screen-layout.md#load-reference-as-file).

## 2. Aprire la Live View

Utilizza il pulsante di acquisizione UUI per aprire la [finestra Live View](../how_to/Inspection_workflow.md#capturing-an-uui) del PCBA corrente.

![Finestra Live View](../assets/UUI photo.PNG){ width=100px .center }

## 3. Abilitare l'ispezione UV

Nella finestra Live View, abilita l'**opzione di ispezione UV** situata nella parte inferiore dell'interfaccia.

![Anteprima UV](../assets/v7/UV_inspection/UV_buttom.png){ .center }

Una volta abilitata, verrà mostrata una simulazione del PCB sotto illuminazione UV.

![Simulazione UV](../assets/v7/UV_inspection/UV_active.png){ .center }

!!! warning "Attenzione"
    Da questo momento in poi, è obbligatorio indossare gli occhiali di sicurezza inclusi nel kit.

    ![Avviso UV](../assets/v7/UV_inspection/warning_icon.png){ width=100px .center }

Successivamente, posiziona l'UUI al centro dell'area di ispezione e premi il pulsante **Avvia ispezione** per iniziare il processo.

![Pulsante avvia ispezione](../assets/v7/UV_inspection/start-inspection-button.png){ width=250px .center }

## 4. Ispezionare il rivestimento

Osserva il PCB sotto illuminazione UV per verificare la corretta applicazione e copertura del rivestimento conformale.

![Ispezione UV](../assets/v7/UV_inspection/UV_inspection.png){ .center }

!!! note "Nota"
    Questa ispezione viene eseguita manualmente dall'operatore. Non è presente alcun rilevamento basato su IA, quindi l'operatore deve identificare visivamente eventuali difetti o la mancanza di rivestimento.

L'immagine UV acquisita viene inclusa nel report finale di ispezione per scopi di documentazione e tracciabilità.

![Report ispezione UV](../assets/v7/UV_inspection/UV_report.png){width=500px, .center}