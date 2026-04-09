In dieser Anleitung lernen wir, wie die Inspektion der konformen Beschichtung mit **AgnosPCB AOI** durchgeführt wird.

Diese Funktion ermöglicht es den Bedienern, die konforme Beschichtung auf PCBAs visuell mithilfe von UV-Beleuchtung zu überprüfen.

!!! note "Hinweis"
    Diese Funktion erfordert die Installation eines separaten Hardware-Kits. Um das UV-Kit zu installieren, folgen Sie den Anweisungen im folgenden Abschnitt:
    [Installationsanleitung für die UV-konforme Beschichtung](../maintenance/UV_kit_install.md)

!!! warning "Achtung"
    Die Inspektion der konformen Beschichtung verwendet UV-Beleuchtung, daher **empfehlen wir, die im Kit enthaltene Schutzbrille zu tragen**.

    ![UV-Warnung](../assets/v7/UV_inspection/warning_icon.png){ width=200px .center }

## Video

Für eine vollständige Einführung in diese Funktion sehen Sie sich das folgende Video an:

<video width="800" controls style="display: block; margin: 0 auto;">
  <source src="../assets/v7/UV_inspection/UV-mode-video.mp4" type="video/mp4">
  Ihr Browser unterstützt das Video-Tag nicht.
</video>

## 1. REFERENZbild erstellen oder laden

Um ein **REFERENZ**-Bild zu erstellen, folgen Sie den Schritten in der [folgenden Anleitung](../how_to/Inspection_workflow.md#generating-a-reference) oder [laden Sie eine vorhandene REFERENZ](../how_to/Screen-layout.md#load-reference-as-file).

## 2. Live-Ansicht öffnen

Verwenden Sie die UUI-Aufnahmetaste, um das [Live-Ansichtsfenster](../how_to/Inspection_workflow.md#capturing-an-uui) des aktuellen PCBAs zu öffnen.

![Live-Ansichtsfenster](../assets/UUI photo.PNG){ width=100px .center }

## 3. UV-Inspektion aktivieren

Aktivieren Sie im Live-Ansichtsfenster die **UV-Inspektionsoption** am unteren Rand der Benutzeroberfläche.

![UV-Vorschau](../assets/v7/UV_inspection/UV_buttom.png){ .center }

Nach der Aktivierung wird eine Simulation des PCBs unter UV-Beleuchtung angezeigt.

![UV-Simulation](../assets/v7/UV_inspection/UV_active.png){ .center }

!!! warning "Achtung"
    Ab diesem Zeitpunkt ist das Tragen der im Kit enthaltenen Schutzbrille verpflichtend.

    ![UV-Warnung](../assets/v7/UV_inspection/warning_icon.png){ width=100px .center }

Platzieren Sie anschließend das UUI in der Mitte des Inspektionsbereichs und drücken Sie die Schaltfläche **Inspektion starten**, um den Inspektionsprozess zu beginnen.

![Schaltfläche Inspektion starten](../assets/v7/UV_inspection/start-inspection-button.png){ width=250px .center }

## 4. Beschichtung prüfen

Beobachten Sie das PCB unter UV-Beleuchtung, um die korrekte Anwendung und Abdeckung der konformen Beschichtung zu überprüfen.

![UV-Inspektion](../assets/v7/UV_inspection/UV_inspection.png){ .center }

!!! note "Hinweis"
    Diese Inspektion wird manuell durch den Bediener durchgeführt. Es findet keine KI-basierte Erkennung statt, daher muss der Bediener visuell mögliche Defekte oder fehlende Beschichtung erkennen.

Das aufgenommene UV-Bild wird in den finalen Inspektionsbericht zur Dokumentation und Rückverfolgbarkeit aufgenommen.

![UV-Inspektionsbericht](../assets/v7/UV_inspection/UV_report.png){width=500px, .center}