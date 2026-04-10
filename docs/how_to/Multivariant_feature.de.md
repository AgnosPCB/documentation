# Referenzvarianten

Bei der Inspektion einer Leiterplatte (PCB) können einige Bauteile vom Referenzbild abweichen und vom System als Fehler erkannt werden (z. B. aufgrund von Änderungen in der Bauteilversorgung oder Unterschieden in der Beschriftung).

Durch das Markieren dieses Fehlertyps als **Referenzvariante** erkennt das System ihn bei zukünftigen Inspektionen und meldet ihn nicht mehr als Fehler.

## Video
___

Für eine vollständige Einführung in diese Funktion sehen Sie sich das folgende Video an:
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Y79a7xYpsv0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

## 1. Inspektion starten

[Erstellen Sie ein Referenzbild](../how_to/Inspection_workflow.md#generating-a-reference) oder wählen Sie eines [aus dem Repository](../how_to/Screen-layout.md#load-reference-as-file) aus. Platzieren Sie anschließend das UUI und starten Sie die Inspektion.

## 2. Fehler identifizieren

Navigieren Sie mit den **Pfeiltasten links/rechts (←/→)** zu dem erkannten Fehler.

![Erkannter Variantenfehler](../assets/ref-variant-error.png){ width=600 .center }

## 3. Als Referenzvariante klassifizieren

Drücken Sie die **Pfeiltaste nach unten (↓)**, um den Fehler abzulehnen. Wählen Sie im Klassifizierungsbereich **Reference variant** aus.

![Klassifizierungsbereich](../assets/ref-variant-label.png){ width=400 .center }

Es erscheint ein Dialogfenster, in dem Sie einen Namen für die neue Variante eingeben müssen (erforderlich) und optional eine Beschreibung hinzufügen können. Klicken Sie anschließend auf **Confirm**.

## Ergebnis

Nach der Klassifizierung wird die Referenzvariante gespeichert und mit dem Referenzbild verknüpft. Gespeicherte Varianten können durch Öffnen eines gespeicherten Referenzbildes angezeigt werden. Sie werden im rechten Seitenbereich unterhalb der vergrößerten Referenzansicht angezeigt. In diesem Bereich können Varianten aktiviert, deaktiviert oder gelöscht werden.

![Gespeicherte Referenzvariante](../assets/ref-variant-sored.png){ width=600 .center }

Diese Variante wird bei zukünftigen Inspektionen nicht mehr als Fehler gemeldet.

!!! warning "Achtung"
    Für jede Position auf der Leiterplatte, an der die Abweichung auftritt, muss eine Referenzvariante manuell erstellt werden. Das System wendet die Variante nicht automatisch auf identische Bauteile an anderen Positionen an.

![Erkannter Variantenfehler](../assets/ref-variant-error.png){ width=400 .center }
![Grüner Pfeil](../assets/green-arrow-down.png){ width=40 .center }
![Referenzvariante](../assets/ref-variant-solved.png){ width=400 .center }

Auch nach dem Erstellen einer Referenzvariante erkennt das System weiterhin tatsächliche Defekte an diesem Bauteil, sofern diese auftreten.

Der abschließende Inspektionsbericht enthält ebenfalls die Referenzvariante zusammen mit ihrem Bild, dem vergebenen Namen und eventuellen zusätzlichen Anmerkungen.

![Reference variant PDF report](../assets/ref-variant-report.png){width=600, .center}