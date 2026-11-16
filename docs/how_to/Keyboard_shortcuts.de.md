# Tastenkombinationen

Diese Seite listet alle Tastenkombinationen der **AgnosPCB-Inspektionssoftware** auf, zusammen mit den Mausaktionen, mit denen die Erkennungen geprüft werden.

## Hauptfenster

| Taste | Aktion |
| --- | --- |
| ++r++ | [Ein REFERENZ-Bild aufnehmen](Inspection_workflow.md#generieren-einer-referenz) (öffnet die Live-Vorschau). |
| ++s++ | [Eine Inspektion starten](Inspection_workflow.md#aufnehmen-einer-uui) (UUI aufnehmen). |
| ++tab++ | Ansichtsmodus des [Hauptarbeitsbereichs](Screen-layout.md#hauptarbeitsbereich) wechseln (REFERENZ / UUI). |
| ++page-up++ | Zur **TOP**-Seite der geladenen REFERENZ wechseln (nur doppelseitige REFERENZEN). |
| ++page-down++ | Zur **BOTTOM**-Seite der geladenen REFERENZ wechseln (nur doppelseitige REFERENZEN). |
| ++f1++ … ++f8++ | Die in diesem Platz des [Referenz-Mosaiks](Screen-layout.md#referenz-mosaik) gespeicherte REFERENZ laden. |
| ++arrow-right++ | Nächste Erkennung (bzw. nächste Zeile der Erkennungsliste bei [Analysepräferenz](Settings_menu.md#analysepraferenz) = **LIST**). |
| ++arrow-left++ | Vorherige Erkennung (bzw. vorherige Zeile der Erkennungsliste bei Analysepräferenz = **LIST**). |
| ++arrow-up++ | Die Erkennung als **echten Fehler** [melden](Inspection_workflow.md#melden-von-fehlern) (öffnet das Meldefenster). In einem Bereich ohne Erkennung wird ein von der Software nicht erkannter Fehler gemeldet. |
| ++arrow-down++ | Die Erkennung als **Falsch-Positiv** melden. |
| ++1++ | [Empfindlichkeit](Set_sensitivity.md): Normal. |
| ++2++ | Empfindlichkeit: Hoch. |
| ++3++ | Empfindlichkeit: Sehr hoch. |
| ++space++ | Beleuchtung der Plattform ein- / ausschalten. |
| ++f++ | Überlagerung der gemeldeten Fehler ein- / ausblenden. |
| ++enter++ | Ein manuell geladenes Bild verarbeiten. |

!!! note "Hinweis"
    Bei aktivierter [Benutzerzugriffskontrolle](../features/User_control.md) erfordern die Tasten ++arrow-up++ und ++arrow-down++ die Berechtigung **Classify detected faults**.

## Erkennungen mit der Maus prüfen

| Mausaktion (auf dem Bild) | Aktion |
| --- | --- |
| Linksklick auf eine Erkennung | Als **echten Fehler** melden (wie ++arrow-up++). Bei einer bereits als Fehler gemeldeten Erkennung wird vor dem Rückgängigmachen eine Bestätigung abgefragt. |
| Rechtsklick auf eine Erkennung | Als **Falsch-Positiv** melden (wie ++arrow-down++). |
| Linksklick auf einen leeren Bereich | Einen von der Software nicht erkannten Fehler melden. |
| Zeiger etwa 1 Sekunde still auf einer Erkennung halten | Als **gesehen** markieren. |
| Rechtsklick außerhalb einer Erkennung | Form der Lupe ändern. |
| ++shift++ + Rechtsklick | Form der Lupe ändern, auch über einer Erkennung. |
| Mausrad | Zoomstufe ändern. |

Die Mausaktionen in der Erkennungsliste (Miniaturansichten, Schaltflächen, Scrollen) sind unter [Erkennungsliste](Screen-layout.md#erkennungsliste) beschrieben.

## Meldefenster

| Taste | Aktion |
| --- | --- |
| ++arrow-up++ / ++arrow-down++ | Durch die Optionen der Auswahlliste blättern. |
| ++enter++ | Bestätigen. |
| ++esc++ | Abbrechen. |

## Weitere Fenster

| Fenster | Taste | Aktion |
| --- | --- | --- |
| Live-Vorschau (REFERENZ / UUI) | ++enter++ | Bestätigen / OK. |
| Live-Vorschau (REFERENZ / UUI) | ++esc++ | Abbrechen. |
| Referenz-Mosaik | ++f1++ … ++f8++ | Die REFERENZ dieses Platzes laden. |
| REFERENZ-Suchliste | ++esc++ | Das Fenster schließen, ohne eine REFERENZ zu laden. |
| Anmeldung | ++enter++ | Anmelden. |
| Einstellungsmenü | ++enter++ | OK (speichern und schließen). |
| Einstellungsmenü | ++esc++ | Schließen. |
