# Integrazione in linea di produzione (modalità INLINE)

Questa guida spiega come integrare l'**AgnosPCB AI 4050** in una linea di
produzione automatizzata, in modo che l'AOI riceva le schede da un nastro
trasportatore, le ispezioni senza l'intervento dell'operatore e restituisca
un risultato PASS/FAIL al controllore di linea.

L'integrazione si compone di due parti:

1. Il **modulo MODBUS**, che collega l'AOI al nastro trasportatore e al controllore di linea (PLC).
2. La **modalità INLINE** del software di ispezione, che gestisce il flusso di lavoro non presidiato.

!!! warning "Leggere prima di iniziare"

    L'integrazione in linea comporta lavori elettrici sia sull'AOI sia sul
    controllore del nastro trasportatore. Tutti i cablaggi devono essere
    eseguiti con **entrambi i sistemi spenti** e da personale qualificato per
    operare sul quadro di controllo della linea.

---

## Prima di iniziare

Verificate di disporre di quanto segue:

- Un'unità **AI 4050** già disimballata, assemblata e funzionante in modalità
  standalone. Se non avete ancora raggiunto questo punto, completate prima la
  [guida all'unboxing](../getting_started/Unboxing.md) e la
  [guida alla connessione](../getting_started/Connection_guide.md).
- Un'immagine di **RIFERIMENTO** già acquisita e validata per ogni prodotto
  che la linea gestirà. La modalità INLINE ispeziona rispetto a RIFERIMENTI
  esistenti: non può crearli.
- Il **modulo MODBUS** fornito da AgnosPCB per la vostra unità.
- L'accesso all'ambiente di programmazione del controllore di linea (PLC).

!!! note "Licenze"

    La modalità INLINE e l'output del report JSON sono funzionalità sotto
    licenza. Confermate con [support@agnospcb.com](mailto:support@agnospcb.com)
    che il profilo del vostro account le ha abilitate prima di mettere in
    servizio la linea, altrimenti le opzioni non avranno effetto.

---

## 1. Installazione del modulo MODBUS

<!-- TODO (ingegneria AgnosPCB): l'assegnazione degli I/O e il collegamento
     all'unità di elaborazione sono documentati a partire dagli schemi
     elettrici. Manca ancora:
     - Dove viene montato il modulo (guida DIN nel quadro? contenitore esterno?)
     - Quale alimentatore alimenta l'ingresso 7~36 V, e la sua potenza
     - Tipo di cavo e lunghezza massima per il collegamento RS-485 e per gli I/O
     - Se i contatti relè sono usati come NA o NC, e il loro carico nominale
     - Dettaglio del cablaggio lato PLC -->

![Cablaggio Modbus](../assets/v7/conveyor/modbus_wiring.png){.center}

Il modulo fornisce **8 uscite a relè** e **8 ingressi digitali**, di cui
l'integrazione utilizza un ingresso e quattro uscite. Si collega a una
**porta USB dell'unità di elaborazione AgnosPCB** tramite il convertitore
isolato USB-RS232/485, come mostrato nello schema sopra.

### Ingressi

L'ingresso deve essere collegato a un **finecorsa**, o a qualsiasi sensore
che rilevi che la PCBA è in posizione e pronta per essere ispezionata.

| Ingresso | Segnale | Funzione |
|---|---|---|
| **DI1** | `BOARD_LOADED` | Attiva un'ispezione, purché la piattaforma di ispezione sia pronta. |

### Uscite

Le uscite comunicano lo stato dell'ispezione al resto della linea di
assemblaggio: al nastro trasportatore successivo e al PLC o al sistema di
controllo della linea.

| Uscita | Morsetto | Segnale | Attiva quando |
|---|---|---|---|
| **DO1** | CH1 | `READY` | La piattaforma di ispezione è pronta per avviare un'ispezione. |
| **DO2** | CH2 | `INSPECTING` | La piattaforma di ispezione sta eseguendo un'ispezione. |
| **DO3** | CH3 | `BOARD OK` | L'ispezione è completata e la scheda ispezionata è conforme. |
| **DO4** | CH4 | `BOARD NOK` | L'ispezione è completata ed è stato rilevato un difetto sulla scheda. |

!!! note "Quando READY è disattivo"

    **DO1** non è attivo durante l'inizializzazione del sistema, mentre è in
    corso un'attività di elaborazione, o quando l'applicazione non è nella
    finestra principale — per esempio mentre è aperto il menu Impostazioni o
    il mosaico dei riferimenti.

### Connessione generale

Lo schema seguente mostra come sono collegati tutti gli elementi coinvolti in
un'installazione tipica:

![Connessione generale](../assets/v7/conveyor/general_connection.png){.center}

Quattro gruppi di apparecchiature partecipano all'integrazione:

- Il **nastro trasportatore dell'AOI**, che porta la scheda nell'area di ispezione e sostiene la telecamera e il sensore di posizione.
- Il **computer AgnosPCB**, che esegue il software di ispezione.
- Il **modulo MODBUS** insieme al suo convertitore USB-RS-485, che traduce tra il software e i segnali elettrici della linea.
- L'**apparecchiatura di linea**: il nastro trasportatore che segue l'AOI, e il PLC o il sistema di controllo del cliente.

Le connessioni tra di essi sono le seguenti:

| Da | A | Connessione | Scopo |
|---|---|---|---|
| Telecamera del nastro trasportatore dell'AOI | Computer AgnosPCB | USB | Acquisisce le immagini della scheda. |
| Computer AgnosPCB | Convertitore USB-RS232/485 | USB | Trasporta la comunicazione MODBUS fuori dal computer. |
| Convertitore USB-RS232/485 | Modulo MODBUS | RS-485 (**A+** / **B−**) | Collega il convertitore al modulo relè. |
| Finecorsa / sensore del nastro trasportatore dell'AOI | Ingresso **DI1** del modulo MODBUS | Ingresso digitale | Segnala che la scheda è in posizione, il che attiva l'ispezione. |
| Uscita **DO1** del modulo MODBUS | Nastro trasportatore successivo | Contatto relè | Comunica al nastro successivo che l'AOI è pronta a ricevere una scheda. |
| Uscite **DO2**, **DO3** e **DO4** del modulo MODBUS | PLC / sistema di controllo del cliente | Contatti relè | Riportano l'avanzamento e il risultato dell'ispezione. |

!!! note "Alimentazione"

    Oltre a queste connessioni, il modulo MODBUS deve essere alimentato
    tramite il suo ingresso **7~36 V**, non rappresentato nello schema.

---

## 2. Configurazione del software di ispezione

Una volta installato il modulo e stabilita la comunicazione, preparate il
software per il funzionamento non presidiato. Tutte le opzioni seguenti si
trovano nella finestra **Settings**; consultate il
[menu Impostazioni](../how_to/Settings_menu.md) per il riferimento completo.

### 2.1 Abilitare la modalità INLINE

Aprite **Settings → Workflow** e abilitate **INLINE Mode (Conveyor)**.

![Sezione Workflow del menu Impostazioni](../assets/v7/settings/workflow-settings.png){.center}

Questo fa passare il client dal flusso di lavoro manuale, guidato da
tastiera, al flusso di lavoro guidato da API usato su una linea: l'ispezione
è attivata dal controllore di linea anziché dall'operatore che preme **S**.

### 2.2 Impostazioni complementari consigliate

Queste opzioni non sono obbligatorie, ma su una linea non presidiata fanno la
differenza tra un'integrazione pulita e un nastro trasportatore bloccato:

| Impostazione | Posizione | Valore consigliato | Perché |
|---|---|---|---|
| **Operator mode** | Workflow | Abilitato | Nasconde l'acquisizione dei riferimenti e impedisce a un operatore di modificare il RIFERIMENTO o la sensibilità a metà turno. Proteggetelo con una password delle impostazioni (vedi [menu Impostazioni](../how_to/Settings_menu.md)). |
| **Mandatory errors review** | Workflow | **Disabilitato** | Se abilitato, il software attende che una persona esamini ogni difetto prima di consentire l'ispezione successiva: questo bloccherà la linea. |
| **Show errors popup** | Workflow | Disabilitato | Evita che una finestra di dialogo modale attenda un input durante il funzionamento automatico. |
| **Show references mosaic** | Workflow | Disabilitato | Evita un popup dopo l'acquisizione dell'immagine. |
| **Auto report OK / NOK** | Reports | Entrambi abilitati | Genera il PDF di ogni scheda senza l'intervento dell'operatore, in modo che la linea produca un registro di tracciabilità completo. |
| **Create JSON report** | Reports | Abilitato | Risultato leggibile da macchina per il vostro MES/SCADA. Richiede una licenza. |
| **Use barcodes** | Workflow | Abilitato | Consente all'AOI di caricare automaticamente il RIFERIMENTO corretto dal codice a barre della scheda, così le linee multiprodotto non necessitano di un cambio prodotto manuale. Richiede una licenza. Vedi [lettore di codici a barre](../features/Barcode_reader.md). |

!!! note "Nota"

    Con **Auto report** abilitato, ogni difetto viene scritto nel PDF con
    l'etichetta "unknown", perché nessun operatore lo classifica. Questo è
    previsto su una linea: la classificazione viene effettuata in seguito,
    offline, a partire dai report salvati.

### 2.3 Dove vengono scritti i risultati

Gli output dell'ispezione vengono scritti nella cartella **PCB_OUT**,
configurabile in **Settings → Paths**.

Perché il vostro MES o un'unità di rete li raccolga automaticamente,
abilitate le condivisioni in **Settings → Network**: **Share PCB_OUT**,
**Share REFERENCES** e **Share REPORTS** espongono quelle cartelle in rete, e
ognuna mostra il proprio percorso di rete una volta attiva. Per le unità
OFFLINE che necessitano di un'interfaccia di rete specifica, vedi l'articolo
[configurazione dell'interfaccia di rete](../maintenance/network_configuration.md).

---

## 3. Checklist di messa in servizio

Prima di consegnare la cella alla produzione, verificate quanto segue in
ordine. Eseguite le prime prove con il nastro trasportatore in modalità
manuale/jog.

1. **L'ispezione standalone funziona.** Con la modalità INLINE ancora
   disabilitata, eseguite un'ispezione normale da tastiera e confermate che
   il risultato sia corretto. Se l'AOI non ispeziona correttamente a mano,
   non ispezionerà correttamente sulla linea.
2. **I RIFERIMENTI sono caricati** per ogni prodotto che la linea gestirà, e
   ciascuno è stato validato su una scheda nota come buona. Vedi
   [suggerimenti](../help/Tips.md).
3. **La lettura dei codici a barre è affidabile**, se la usate per il cambio
   prodotto. Testatela su più schede, comprese le etichette stampate peggio
   che avete.
4. **Il posizionamento della scheda è ripetibile.** Il nastro trasportatore
   deve presentare la scheda all'interno dell'area di ispezione in una
   posizione costante — l'AOI segnala **WARNING / ROTATED** o
   **WARNING / SHIFTED** quando la scheda si discosta significativamente dal
   RIFERIMENTO. Controllate questi avvisi durante le prime esecuzioni e
   correggete il fermo meccanico o il fissaggio della scheda prima di passare
   alla produzione.
5. **I segnali MODBUS sono attivi** — l'ingresso **DI1** attiva
   un'ispezione, e le uscite **DO1**-**DO4** cambiano stato come previsto sul
   lato linea.
6. **Un ciclo completo viene eseguito da inizio a fine**, con una scheda nota
   come buona e una nota come difettosa, e il controllore di linea riceve
   ogni volta il risultato PASS e FAIL corretto.
7. **I report vengono scritti** in PCB_OUT e sono raggiungibili dal vostro
   MES.
8. **Il comportamento in caso di guasto è corretto.** Arrestate il software
   dell'AOI a metà ciclo e confermate che il controllore di linea rilevi la
   perdita e smetta di alimentare schede invece di lasciarle passare senza
   ispezione.

---

## Risoluzione dei problemi

| Sintomo | Verifica |
|---|---|
| La linea si ferma dopo la prima scheda difettosa | **Mandatory errors review** è abilitato. Disabilitatelo in Settings → Workflow. |
| Una finestra di dialogo attende un input a metà ciclo | Disabilitate **Show errors popup** e **Show references mosaic** in Settings → Workflow. |
| Ogni scheda fallisce su un prodotto nuovo | Il RIFERIMENTO caricato non corrisponde al prodotto. Controllate la lettura del codice a barre, o il RIFERIMENTO selezionato per il lotto. |
| **WARNING / ROTATED** o **WARNING / SHIFTED** sulla maggior parte delle schede | Il nastro trasportatore non presenta le schede in una posizione ripetibile. Correggete il fermo meccanico; l'AOI confronta rispetto alla posizione del RIFERIMENTO. |
| **WARNING / NO CROP** | L'autocrop non ha trovato il bordo della scheda e l'immagine completa è stata confrontata. Riacquisite il RIFERIMENTO, oppure impostate manualmente l'area di ritaglio sull'immagine di riferimento. |
| L'AOI smette di ispezionare e mostra `Engine [ OFFLINE ]` | Solo unità ONLINE: la connessione internet o l'account non sono attivi. Vedi [risoluzione dei problemi](../maintenance/Troubleshooting.md). |
| Crediti esauriti a metà turno | Solo unità ONLINE: appare un avviso sotto i 10 crediti. Contattate [support@agnospcb.com](mailto:support@agnospcb.com). |

Per qualsiasi cosa non trattata qui, contattate
[support@agnospcb.com](mailto:support@agnospcb.com).
