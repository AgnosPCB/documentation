# Scorciatoie da tastiera

Questa pagina elenca tutte le scorciatoie da tastiera disponibili nel **software di ispezione AgnosPCB**, insieme alle azioni del mouse usate per esaminare le rilevazioni.

## Finestra principale

| Tasto | Azione |
| --- | --- |
| ++r++ | [Scattare un'immagine di RIFERIMENTO](Inspection_workflow.md#generazione-di-un-riferimento) (apre l'anteprima dal vivo). |
| ++s++ | [Avviare un'ispezione](Inspection_workflow.md#acquisizione-di-una-uui) (acquisire la UUI). |
| ++tab++ | Cambiare la modalità di visualizzazione dell'[area di lavoro principale](Screen-layout.md#area-di-lavoro-principale) (RIFERIMENTO / UUI). |
| ++page-up++ | Passare al lato **TOP** del RIFERIMENTO caricato (solo RIFERIMENTI a doppia faccia). |
| ++page-down++ | Passare al lato **BOTTOM** del RIFERIMENTO caricato (solo RIFERIMENTI a doppia faccia). |
| ++f1++ … ++f8++ | Caricare il RIFERIMENTO salvato in quella posizione del [mosaico di riferimenti](Screen-layout.md#mosaico-di-riferimenti). |
| ++arrow-right++ | Rilevazione successiva (o riga successiva dell'elenco delle rilevazioni con [Preferenza di analisi](Settings_menu.md#preferenza-di-analisi) = **LIST**). |
| ++arrow-left++ | Rilevazione precedente (o riga precedente dell'elenco delle rilevazioni con Preferenza di analisi = **LIST**). |
| ++arrow-up++ | [Segnalare](Inspection_workflow.md#segnalazione-degli-errori) la rilevazione come **errore reale** (apre la finestra di segnalazione). In un'area senza rilevazioni, segnala un errore non rilevato dal software. |
| ++arrow-down++ | Segnalare la rilevazione come **falso positivo**. |
| ++1++ | [Sensibilità](Set_sensitivity.md): Normale. |
| ++2++ | Sensibilità: Alta. |
| ++3++ | Sensibilità: Molto alta. |
| ++space++ | Accendere / spegnere l'illuminazione della piattaforma. |
| ++f++ | Mostrare / nascondere la sovrapposizione degli errori segnalati. |
| ++enter++ | Elaborare un'immagine caricata manualmente. |

!!! note "Nota"
    Con il [controllo di accesso degli utenti](../features/User_control.md) attivato, i tasti ++arrow-up++ e ++arrow-down++ richiedono l'autorizzazione **Classify detected faults**.

## Esaminare le rilevazioni con il mouse

| Azione del mouse (sull'immagine) | Azione |
| --- | --- |
| Clic sinistro su una rilevazione | Segnalarla come **errore reale** (come ++arrow-up++). Su una rilevazione già segnalata come errore, chiede conferma prima di annullarla. |
| Clic destro su una rilevazione | Segnalarla come **falso positivo** (come ++arrow-down++). |
| Clic sinistro su un'area vuota | Segnalare un errore non rilevato dal software. |
| Tenere il puntatore fermo su una rilevazione per circa 1 secondo | Contrassegnarla come **vista**. |
| Clic destro fuori da una rilevazione | Cambiare la forma della lente d'ingrandimento. |
| ++shift++ + clic destro | Cambiare la forma della lente d'ingrandimento, anche sopra una rilevazione. |
| Rotella del mouse | Cambiare il livello di zoom. |

Le azioni del mouse nell'elenco delle rilevazioni (miniature, pulsanti, scorrimento) sono descritte in [Elenco delle rilevazioni](Screen-layout.md#elenco-delle-rilevazioni).

## Finestra di segnalazione

| Tasto | Azione |
| --- | --- |
| ++arrow-up++ / ++arrow-down++ | Scorrere le opzioni dell'elenco a discesa. |
| ++enter++ | Confermare. |
| ++esc++ | Annullare. |

## Altre finestre

| Finestra | Tasto | Azione |
| --- | --- | --- |
| Anteprima dal vivo (RIFERIMENTO / UUI) | ++enter++ | Confermare / OK. |
| Anteprima dal vivo (RIFERIMENTO / UUI) | ++esc++ | Annullare. |
| Mosaico di riferimenti | ++f1++ … ++f8++ | Caricare il RIFERIMENTO di quella posizione. |
| Elenco di ricerca dei RIFERIMENTI | ++esc++ | Chiudere la finestra senza caricare alcun RIFERIMENTO. |
| Accesso | ++enter++ | Accedere. |
| Menu Impostazioni | ++enter++ | OK (salvare e chiudere). |
| Menu Impostazioni | ++esc++ | Chiudere. |
