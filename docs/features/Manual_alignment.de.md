# Manuelle Bildausrichtung

Wenn das REFERENZ- und das UUI-Bild genauer ausgerichtet werden müssen, als die automatische Ausrichtung erlaubt, enthält die AgnosPCB-Software ein manuelles Ausrichtungswerkzeug, das die Genauigkeit der Inspektion verbessert.

## 1. Manuelle Ausrichtung aktivieren

!!! info "Hinweis"
    Diese Funktion ist nur für Inspektionen mit **1x1-Bildern** verfügbar.

Aktivieren Sie die manuelle Ausrichtung im Einstellungsmenü, bevor Sie ein neues UUI-Bild aufnehmen.

![Option für manuelle Ausrichtung](../assets/v7/manual_align/1-manual-alignment-option.png){.center}

Aktivieren Sie anschließend während der Aufnahme des UUI-Bildes die Option für die manuelle Ausrichtung.

![Option für manuelle Ausrichtung](../assets/v7/manual_align/manual-aling-button.png){.center}

## 2. Bilder ausrichten

Unmittelbar nach der Aufnahme des UUI-Bildes erscheint das Fenster für die manuelle Ausrichtung mit dem REFERENZ- und dem UUI-Bild.

![Fenster für manuelle Ausrichtung](../assets/v7/manual_align/2-MA-zoom.png){.center}

Markieren Sie nun drei Referenzpunkte im REFERENZ-Bild.

!!! warning "Wichtig"
    Wählen Sie Punkte, die von Platine zu Platine leicht reproduzierbar sind (Bohrungen, Pads usw.), möglichst nahe an den Ecken der Platine und so weit wie möglich voneinander entfernt.

!!! note "Hinweis"
    Verwenden Sie das Mausrad, um in das Bild hineinzuzoomen und die Punkte genauer zu setzen.

![Ersten Punkt markieren](../assets/v7/manual_align/3-MA-P1.png){.center}

![Zweiten Punkt markieren](../assets/v7/manual_align/4-MA-P2.png){.center}

![Dritten Punkt markieren](../assets/v7/manual_align/5-MA-P3.png){.center}

Sobald die drei Ausrichtungspunkte im REFERENZ-Bild definiert sind, markieren Sie **dieselben drei Punkte** im UUI-Bild.

!!! warning "Wichtig"
    Um eine korrekte Ausrichtung zu gewährleisten, setzen Sie jeden Punkt genau auf dasselbe Merkmal der Platine wie im REFERENZ-Bild.

![Ersten Punkt markieren](../assets/v7/manual_align/6-MA-UUI-P1.png){.center}

![Zweiten Punkt markieren](../assets/v7/manual_align/7-MA-UUI-P2.png){.center}

![Dritten Punkt markieren](../assets/v7/manual_align/8-MA-UUI-P3.png){.center}

Wenn alle Ausrichtungspunkte gesetzt sind, drücken Sie die Schaltfläche **ALIGN**, um den Vorgang zu starten. Die Software richtet beide Bilder aus und führt anschließend die Inspektion durch.

![Ausgerichtete Bilder](../assets/v7/manual_align/MA-final.png){.center}
