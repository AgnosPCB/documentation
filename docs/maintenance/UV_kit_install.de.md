# Installation des UV-Beschichtungskits

Diese Anleitung beschreibt die notwendigen Schritte zur Installation des **UV-Beschichtungs-Inspektionsmoduls** an der **AOI AI-4050**.


## Video-Installationsanleitung

<iframe width="100%" height="400" src="https://www.youtube.com/embed/JY0PqEUxGlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Liste der enthaltenen Teile

## Installation des Stromkabels

!!! note "Hinweis"

    Neue Einheiten enthalten das Stromkabel des UV-Moduls bereits vorinstalliert. Wenn Ihre AOI dieses Kabel bereits installiert hat, fahren Sie mit dem nächsten Schritt fort.
    ![Vormontiertes Stromkabel](../assets/v7/UV_install/power_cable_pre-mounted.png){width=200px .center}


Die Steuerplatine befindet sich im Inneren der Inspektionskammer auf der oberen rechten Seite. Entfernen Sie den Warnaufkleber von der Abdeckung und lösen Sie die Schraube im Inneren mit einem Inbusschraubendreher. Entfernen Sie die Kunststoffabdeckung der Steuerplatine.

![Lage der Steuerplatine](../assets/v7/UV_install/board_location.png){.center}


Lösen Sie die Schrauben an der in der Abbildung gezeigten Klemme.

![Lage der Klemmen](../assets/v7/UV_install/terminals_location.png){.center}

Schließen Sie den schwarzen Draht an die linke Klemme (Minus) und den roten Draht an die rechte Klemme (Plus) an. Achten Sie darauf, dass jeder Draht vollständig in die Klemme eingeführt ist, und ziehen Sie beide Schrauben fest. Überprüfen Sie die Verbindungen, indem Sie leicht daran ziehen.

![Polarität der Klemmen](../assets/v7/UV_install/terminals_polarity.png){.center}

Sobald das Kabel angeschlossen ist, setzen Sie die Gehäuseabdeckung wieder an ihre Position und ziehen Sie die Schraube fest, um sie zu sichern.

## Platzierung und Anschluss des DC-Spannungswandlers

Setzen Sie eine der im Kit enthaltenen M5-Schrauben mit Mutter in die Nut des vertikalen Aluminiumrahmens unterhalb der Steuerplatine ein. Ziehen Sie sie noch nicht vollständig fest.

Setzen Sie die zweite Schraube etwa 10 Zentimeter oberhalb der ersten ein.

![Lage der Schrauben](../assets/v7/UV_install/dc_screws.png){.center}

Positionieren Sie den Spannungsregler mit dem roten Draht nach oben und sichern Sie ihn mit beiden Schrauben.

!!! warning "Wichtig"
    Stellen Sie sicher, dass sich die Muttern in der Nut drehen lassen und die Schrauben fest angezogen sind.


Schließen Sie den schwarzen und den roten Draht an das Stromkabel der Steuerplatine an.

![DC-Wandler installiert](../assets/v7/UV_install/dc_installed.png){.center}

## Installation der UV-LEDs

Platzieren Sie die UV-LEDs am oberen Rand des Ringlichts, an den gelben Dreiecksmarkierungen, oder, falls diese nicht vorhanden sind, in der Mitte jeder Seite.

![Gelbe Markierungen](../assets/v7/UV_install/yellow_marks.png){.center}


Setzen Sie die LED-Halterung oben in den weißen Rand ein, wobei die LED nach oben zeigt, und drücken Sie, bis Sie ein Klicken hören. Wiederholen Sie diesen Vorgang mit den übrigen 3 LEDs.

![Einsetzen der UV-LEDs](../assets/v7/UV_install/insert_uv.png){.center}

Kleben Sie die Kabelführungen oberhalb des Beleuchtungsrings an, mit der Klemmöffnung nach oben. Positionieren Sie sie an den geeignetsten Stellen, um die UV-Kabel leicht verlegen zu können.

![Kabelführungen](../assets/v7/UV_install/cable_holder.png){.center}

## Anschluss der UV-LEDs an den DC-Wandler

Verbinden Sie bei bereits installierten UV-LEDs das „Y“-Stromkabel mit der Unterseite des DC-Spannungswandlers (schwarzer und gelber Draht) und schließen Sie anschließend jede LED an den zugehörigen Pin an. Beachten Sie, dass einer der Drähte kürzer ist als der andere.

Führen Sie die Drähte durch die zuvor installierten Führungen und achten Sie darauf, dass sie für die Kamera nicht sichtbar sind.

![Verlegtes Kabel](../assets/v7/UV_install/cable_routed.png){.center}
