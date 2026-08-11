# Menu Impostazioni

Il **menu Impostazioni** è diviso in diverse sezioni, descritte di seguito.

## Impostazioni generali

![Sezione generale del menu Impostazioni](../assets/v7/settings/ui-settings.png){.center}

#### Mostra exif

Mostra i metadati dell'immagine corrente nell'[area di lavoro principale](./Screen-layout.md#area-di-lavoro-principale).

#### Mostra icone dell'area di lavoro

Abilita una serie di funzioni nell'[area di lavoro principale](./Screen-layout.md#area-di-lavoro-principale). Per maggiori informazioni su queste funzioni, consultate la [sezione successiva](./Workspace_icons.md).

#### Segnalazione automatica

Per impostazione predefinita, il software numera ogni errore dopo l'ispezione. Disabilitando questa opzione, viene evidenziata a colori solo l'area interessata, senza numero.

#### Colore della maschera

Questa opzione consente di cambiare il colore dell'errore contrassegnato. Quando il colore dell'errore contrassegnato coincide con quello della PCBA, è consigliabile scegliere un colore a contrasto maggiore per rendere più visibili le aree contrassegnate.

#### Lingua

Cambia la lingua dell'interfaccia. Le lingue attualmente disponibili sono: **inglese, francese, tedesco, italiano e spagnolo**.

## Opzioni del flusso di lavoro

![Sezione flusso di lavoro del menu Impostazioni](../assets/v7/settings/workflow-settings.png){.center}

#### Usa codici a barre

Attiva o disattiva la [funzione di lettura dei codici a barre](../features/Barcode_reader.md).

#### Mostra finestra degli errori

Disabilitando questa opzione, la finestra di segnalazione non comparirà più quando si segnala un errore con i tasti freccia **SU** o **GIÙ**. Gli errori segnalati verranno generati con l'etichetta "**other**" nel report PDF finale.

#### Mostra mosaico dei riferimenti

Disabilitando questa opzione, il menu a mosaico non comparirà dopo l'acquisizione di un'immagine di **RIFERIMENTO**.

#### Modalità operatore

Abilitando questa opzione verranno nascoste diverse funzioni dell'interfaccia, semplificando l'uso del software. Impedisce inoltre all'operatore di cambiare l'immagine di RIFERIMENTO o la sensibilità delle ispezioni. È possibile aggiungere una [password](#password-impostazioni) affinché solo l'amministratore possa disabilitare questa opzione.

#### Sensibilità abilitata

Consente di modificare la sensibilità quando il software è in modalità operatore.

#### Modalità INLINE

Selezionate questa modalità quando l'AOI è installata su un nastro trasportatore. Per maggiori informazioni su questa funzionalità, consultate la sezione seguente: [Integrazione in linea di produzione](../maintenance/Conveyor_integration.md)

#### Modalità di allineamento manuale

Abilitate questa opzione per allineare manualmente le immagini di RIFERIMENTO e UUI. Per maggiori informazioni su questa funzionalità, consultate la sezione seguente: [Strumento di allineamento manuale](../features/Manual_alignment.md)

#### Ricorda sensibilità

Attivando questa opzione, il software manterrà la sensibilità di ispezione configurata dopo aver eseguito una nuova ispezione.

#### Revisione obbligatoria degli errori

Se questa opzione è abilitata, il software non continuerà a ispezionare nuovi pannelli finché tutti gli errori rilevati nell'ispezione corrente non saranno stati [segnalati](Inspection_workflow.md#segnalazione-degli-errori) come errori o falsi positivi.

## Opzioni del report

![Sezione report del menu Impostazioni](../assets/v7/settings/reports-settings.png){.center}

#### ID operatore

Imposta un ID per l'operatore corrente. Questo ID verrà visualizzato nel report PDF finale al termine dell'ispezione.

#### ID ordine

Imposta un ID per l'ordine di produzione corrente. Questo ID verrà visualizzato nel report PDF finale al termine dell'ispezione.

#### ID piattaforma

Imposta un ID per l'AOI.

#### Usa TAG come

Imposta il TAG (OK o NOK) del report PDF finale come **suffisso** o **prefisso** del nome del file.

#### TAG OK

Imposta un TAG OK personalizzato per il report PDF finale.

#### TAG NO OK

Imposta un TAG NO OK personalizzato per il report PDF finale.

#### Report automatico

Quando questa opzione è abilitata, verrà generato automaticamente un report PDF finale etichettato come OK se non vengono rilevati errori dopo l'ispezione. Il report PDF finale può essere generato anche se vengono rilevati errori durante l'ispezione.

!!! note "Nota"
    Quando si genera automaticamente un report PDF, tutti gli errori rilevati vengono contrassegnati con l'etichetta "unknown".

#### Mostra tutti i difetti

Mostra tutti gli errori rilevati nel report PDF anche se l'operatore non li ha segnalati.

#### Crea report JSON

Genera un **file JSON leggibile da una macchina** con i dati dell'ispezione, in aggiunta al report PDF. Utilizzate questa opzione quando i risultati devono essere elaborati da un altro sistema — un MES, un ERP o un database di tracciabilità — invece di essere letti da una persona.

Il file JSON viene scritto nella stessa cartella del report PDF, all'interno della directory [PCB OUT](#pcb-out).

!!! note "Nota"
    Questa è una funzione con licenza. Se l'opzione non genera alcun file, contattate [support@agnospcb.com](mailto:support@agnospcb.com) per verificare se il vostro profilo account la include.

#### Crea report a BASSA RISOLUZIONE

Genera un **report PDF aggiuntivo con dimensioni di file ridotte**. Il report standard continua a essere generato: questa opzione aggiunge una copia più leggera, non lo sostituisce.

È utile quando i report devono essere inviati per e-mail, archiviati a lungo termine o trasferiti tramite una connessione lenta o limitata, dove le immagini a piena risoluzione renderebbero il file troppo grande.

#### Logo

Imposta un logo per il report PDF.

## Opzioni data/ora

![Sezione data del menu Impostazioni](../assets/v7/settings/date-settings.png){.center}

#### Fuso orario

Imposta il fuso orario.

#### Data e ora

Imposta il giorno e l'ora.

!!! note "Nota"
    Per applicare le modifiche premete il pulsante **SET** e riavviate il sistema.

## Opzione percorso

![Sezione percorso del menu Impostazioni](../assets/v7/settings/path-settings.png){.center}

#### PCB OUT

Cambia il percorso in cui vengono generate le ispezioni.

## Opzioni di condivisione

![Sezione condivisione del menu Impostazioni](../assets/v7/settings/network-settings.png){.center}

#### Condividi cartelle

Abilitando queste opzioni, il sistema condividerà automaticamente le cartelle PCB_OUT e REFERENCE sulla rete locale. L'indirizzo di accesso verrà visualizzato una volta impostata l'opzione.

!!! note "Nota"
    Per applicare le modifiche premete il pulsante **Apply**.

!!! note "Nota"
    Per le unità OFFLINE, se dovete cambiare l'interfaccia di rete della vostra unità, consultate l'[articolo sulla configurazione di rete](../maintenance/network_configuration.md).

## Utenti

![Sezione utenti del menu Impostazioni](../assets/v7/settings/users-settings.png){.center}

Questa scheda è disponibile solo per gli utenti con ruolo **admin**. Consente di creare gli account che possono utilizzare l'AOI, ciascuno con un ruolo **admin** oppure **operator**, e di richiedere nome utente e password ogni volta che il software viene avviato.

Per abilitare **Enable user access control** deve esistere almeno un account **admin** attivo.

Per maggiori informazioni su questa funzionalità, consultate la sezione seguente: [Controllo accessi utenti](../features/User_control.md)

## Sequenze

![Sezione sequenze del menu Impostazioni](../assets/v7/custom_sequences/sequences.png){.center}

Questa scheda è disponibile solo per gli utenti con ruolo **admin**. Consente di definire le vostre **sequenze di acquisizione**, ovvero la griglia di fotografie che la telecamera scatta e unisce per comporre l'immagine di una scheda grande.

Utilizzatela quando nessuna delle sequenze predefinite si adatta correttamente alla vostra scheda. Le sequenze salvate qui appaiono come opzioni **CUSTOM** nella finestra di anteprima dal vivo quando si acquisisce un RIFERIMENTO o si avvia un'ispezione.

Per maggiori informazioni su questa funzionalità, consultate la sezione seguente: [Sequenze di acquisizione personalizzate](../features/Custom_sequences.md)

!!! note "Nota"
    Questa scheda non viene visualizzata sulle unità configurate in **modalità Q1**, che eseguono una sola acquisizione.

## Macchina

![Sezione macchina del menu Impostazioni](../assets/v7/settings/machine-settings.png){.center}

Questa scheda è disponibile solo per gli utenti con ruolo **admin**. Mostra i parametri hardware della vostra unità, memorizzati nel file **machine.json**.

La maggior parte dei valori è visualizzata in grigio: sono mostrati **solo a titolo informativo** e non possono essere modificati. I campi evidenziati in blu sono quelli modificabili:

| Campo | Descrizione |
| --- | --- |
| **xacc** / **yacc** / **zacc** | Accelerazione di ciascun asse. |
| **xhome** / **yhome** / **zhome** | Scostamento della posizione di origine di ciascun asse. |
| **capture_gain** | Guadagno della telecamera durante l'acquisizione. |
| **exposure** | Tempo di esposizione della telecamera. |

Premete **Save changes** per applicare i nuovi valori, oppure **Reset to factory default** per ripristinare tutti i parametri al valore originale.

!!! warning "Importante"
    Questi parametri influiscono sul movimento della piattaforma e sull'acquisizione delle immagini. Modificarli in modo errato può degradare la qualità dell'immagine o il movimento degli assi. Modificateli solo quando il [supporto](mailto:support@agnospcb.com) ve lo richiede.

!!! note "Nota"
    Questa scheda non viene visualizzata sulle unità senza piattaforma XYZ.

## Debug

![Sezione debug del menu Impostazioni](../assets/v7/settings/debug-settings.png){.center}

Questa scheda è disponibile solo per gli utenti con ruolo **admin**. Genera un **report diagnostico** che consente al nostro team di supporto di analizzare il comportamento della vostra unità.

Per generarlo:

1. Posizionate la **scheda di calibrazione** al centro dell'area di ispezione. Se non ne disponete, utilizzate una scheda di prova **più piccola di 20x20 cm**.
2. Premete **Generate DEBUG report**.
3. Attendete il completamento della barra di progresso. L'area di testo sottostante mostra l'avanzamento del processo.
4. Raccogliete i file generati e inviateli a [support@agnospcb.com](mailto:support@agnospcb.com).

## Sezione informazioni

![Sezione informazioni del menu Impostazioni](../assets/v7/ui-settings-info.png){width=650px .center}

#### Informazioni AOI

Le informazioni dell'AOI vengono visualizzate in questa sezione.

#### Backup

Questa funzione genera automaticamente un file compresso di backup della cartella **PCB_OUT**. Il file di backup viene salvato nella cartella **APP/BACKUP**.

#### Password impostazioni

Imposta una password per accedere al menu Impostazioni.

!!! note "Nota"
    Lasciate la password vuota per disabilitare la richiesta di password.
