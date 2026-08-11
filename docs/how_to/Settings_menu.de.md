# Einstellungsmenü

Das **Einstellungsmenü** ist in mehrere Abschnitte unterteilt, die im Folgenden beschrieben werden.

## Allgemeine Einstellungen

![Allgemeiner Abschnitt des Einstellungsmenüs](../assets/v7/settings/ui-settings.png){.center}

#### Exif anzeigen

Zeigt die Metadaten des aktuellen Bildes im [Hauptarbeitsbereich](./Screen-layout.md#hauptarbeitsbereich) an.

#### Symbole des Arbeitsbereichs anzeigen

Aktiviert eine Reihe von Funktionen im [Hauptarbeitsbereich](./Screen-layout.md#hauptarbeitsbereich). Weitere Informationen zu diesen Funktionen finden Sie im [nächsten Abschnitt](./Workspace_icons.md).

#### Automatische Signalisierung

Standardmäßig numeriert die Software jeden Fehler nach der Inspektion. Wenn diese Option deaktiviert ist, wird nur der betroffene Bereich farbig hervorgehoben, ohne Nummer.

#### Maskenfarbe

Mit dieser Option können Sie die Farbe des markierten Fehlers ändern. Wenn die Farbe des markierten Fehlers mit der Farbe der PCBA übereinstimmt, empfiehlt es sich, eine kontrastreichere Farbe zu wählen, damit die markierten Bereiche besser sichtbar sind.

#### Sprache

Ändert die Sprache der Benutzeroberfläche. Derzeit verfügbare Sprachen: **Englisch, Französisch, Deutsch, Italienisch und Spanisch**.

## Workflow-Optionen

![Workflow-Abschnitt des Einstellungsmenüs](../assets/v7/settings/workflow-settings.png){.center}

#### Barcode verwenden

Schaltet die [Barcode-Lesefunktion](../features/Barcode_reader.md) ein oder aus.

#### Fehler-Popup anzeigen

Wenn diese Option deaktiviert ist, erscheint das Berichtsfenster nicht mehr, wenn ein Fehler mit den Pfeiltasten **NACH OBEN** oder **NACH UNTEN** gemeldet wird. Die gemeldeten Fehler werden im endgültigen PDF-Bericht mit der Bezeichnung "**other**" erzeugt.

#### Referenz-Mosaik anzeigen

Wenn diese Option deaktiviert ist, erscheint das Mosaik-Menü nach der Aufnahme eines **REFERENZ**-Bildes nicht mehr.

#### Bediener-Modus

Das Aktivieren dieser Option blendet verschiedene Funktionen der Benutzeroberfläche aus und vereinfacht die Nutzung der Software. Es verhindert auch, dass der Bediener das REFERENZ-Bild oder die Empfindlichkeit der Inspektionen ändern kann. Es kann ein [Passwort](#einstellungs-passwort) hinzugefügt werden, sodass nur der Administrator diese Option deaktivieren kann.

#### Empfindlichkeit aktiviert

Ermöglicht das Ändern der Empfindlichkeit, während sich die Software im Bediener-Modus befindet.

#### INLINE-Modus

Wählen Sie diesen Modus, wenn die AOI an einem Förderband installiert ist. Weitere Informationen zu dieser Funktion finden Sie im folgenden Abschnitt: [Integration in die Produktionslinie](../maintenance/Conveyor_integration.md)

#### Manueller Ausrichtungsmodus

Aktivieren Sie diese Option, um die REFERENZ- und UUI-Bilder manuell auszurichten. Weitere Informationen zu dieser Funktion finden Sie im folgenden Abschnitt: [Manuelles Ausrichtungswerkzeug](../features/Manual_alignment.md)

#### Empfindlichkeit speichern

Wenn Sie diese Option aktivieren, behält die Software die konfigurierte Inspektionsempfindlichkeit auch nach einer neuen Inspektion bei.

#### Pflichtprüfung der Fehler

Wenn diese Option aktiviert ist, setzt die Software die Inspektion neuer Platinen erst fort, wenn alle in der aktuellen Inspektion erkannten Fehler als Fehler oder Falsch-Positive [gemeldet](Inspection_workflow.md#melden-von-fehlern) wurden.

## Berichtsoptionen

![Berichtsabschnitt des Einstellungsmenüs](../assets/v7/settings/reports-settings.png){.center}

#### Bediener-ID

Legt eine ID für den aktuellen Bediener fest. Diese ID wird nach Abschluss der Inspektion im endgültigen PDF-Bericht angezeigt.

#### Auftrags-ID

Legt eine ID für den aktuellen Fertigungsauftrag fest. Diese ID wird nach Abschluss der Inspektion im endgültigen PDF-Bericht angezeigt.

#### Plattform-ID

Legt eine ID für die AOI fest.

#### TAG verwenden als

Legt das TAG (OK oder NOK) des endgültigen PDF-Berichts als **Suffix** oder **Präfix** des Dateinamens fest.

#### TAG OK

Legt ein benutzerdefiniertes OK-TAG für den endgültigen PDF-Bericht fest.

#### TAG NO OK

Legt ein benutzerdefiniertes NO-OK-TAG für den endgültigen PDF-Bericht fest.

#### Automatischer Bericht

Wenn diese Option aktiviert ist, wird automatisch ein endgültiger, mit OK gekennzeichneter PDF-Bericht erzeugt, sofern nach der Inspektion keine Fehler erkannt wurden. Der endgültige PDF-Bericht kann auch erzeugt werden, wenn während der Inspektion Fehler erkannt werden.

!!! note "Hinweis"
    Bei der automatischen Erzeugung eines PDF-Berichts werden alle erkannten Fehler mit der Bezeichnung "unknown" markiert.

#### Alle Fehler anzeigen

Zeigt alle erkannten Fehler im PDF-Bericht an, auch wenn der Bediener sie nicht gemeldet hat.

#### JSON-Bericht erstellen

Erzeugt zusätzlich zum PDF-Bericht eine **maschinenlesbare JSON-Datei** mit den Inspektionsdaten. Verwenden Sie diese Option, wenn die Ergebnisse von einem anderen System verarbeitet werden sollen — einem MES, einem ERP oder einer Rückverfolgbarkeitsdatenbank — anstatt von einer Person gelesen zu werden.

Die JSON-Datei wird im selben Ordner wie der PDF-Bericht innerhalb des Verzeichnisses [PCB OUT](#pcb-out) abgelegt.

!!! note "Hinweis"
    Dies ist eine lizenzpflichtige Funktion. Wenn die Option keine Datei erzeugt, wenden Sie sich an [support@agnospcb.com](mailto:support@agnospcb.com), um zu prüfen, ob Ihr Kontoprofil sie enthält.

#### Bericht mit NIEDRIGER AUFLÖSUNG erstellen

Erzeugt einen **zusätzlichen PDF-Bericht mit geringerer Dateigröße**. Der Standardbericht wird weiterhin erzeugt: diese Option fügt eine leichtere Kopie hinzu, sie ersetzt ihn nicht.

Das ist nützlich, wenn die Berichte per E-Mail versendet, langfristig archiviert oder über eine langsame bzw. volumenbegrenzte Verbindung übertragen werden müssen, wo die Bilder in voller Auflösung die Datei unpraktisch groß machen würden.

#### Logo

Legt ein Logo für den PDF-Bericht fest.

## Datum/Uhrzeit-Optionen

![Datumsabschnitt des Einstellungsmenüs](../assets/v7/settings/date-settings.png){.center}

#### Zeitzone

Legt die Zeitzone fest.

#### Datum und Uhrzeit

Legt Tag und Uhrzeit fest.

!!! note "Hinweis"
    Um die Änderungen anzuwenden, drücken Sie die Schaltfläche **SET** und starten Sie das System neu.

## Pfad-Option

![Pfadabschnitt des Einstellungsmenüs](../assets/v7/settings/path-settings.png){.center}

#### PCB OUT

Ändert den Pfad, in dem die Inspektionen erzeugt werden.

## Freigabeoptionen

![Freigabeabschnitt des Einstellungsmenüs](../assets/v7/settings/network-settings.png){.center}

#### Ordner freigeben

Wenn Sie diese Optionen aktivieren, gibt das System die Ordner PCB_OUT und REFERENCE automatisch in Ihrem lokalen Netzwerk frei. Die Zugriffsadresse wird angezeigt, sobald die Option gesetzt ist.

!!! note "Hinweis"
    Um die Änderungen anzuwenden, drücken Sie die Schaltfläche **Apply**.

!!! note "Hinweis"
    Wenn Sie bei OFFLINE-Einheiten die Netzwerkschnittstelle Ihrer Einheit ändern müssen, lesen Sie bitte den [Artikel zur Netzwerkkonfiguration](../maintenance/network_configuration.md).

## Benutzer

![Benutzerabschnitt des Einstellungsmenüs](../assets/v7/settings/users-settings.png){.center}

Diese Registerkarte ist nur für Benutzer mit der Rolle **admin** verfügbar. Sie erlaubt es, die Konten anzulegen, die die AOI bedienen dürfen — jedes mit der Rolle **admin** oder **operator** — und bei jedem Start der Software einen Benutzernamen und ein Passwort zu verlangen.

Um **Enable user access control** zu aktivieren, muss mindestens ein aktives **admin**-Konto vorhanden sein.

Weitere Informationen zu dieser Funktion finden Sie im folgenden Abschnitt: [Benutzerzugriffskontrolle](../features/User_control.md)

## Sequenzen

![Sequenzabschnitt des Einstellungsmenüs](../assets/v7/custom_sequences/sequences.png){.center}

Diese Registerkarte ist nur für Benutzer mit der Rolle **admin** verfügbar. Sie erlaubt es, eigene **Aufnahmesequenzen** zu definieren, also das Raster von Fotografien, die die Kamera aufnimmt und zum Bild einer großen Platine zusammenfügt.

Verwenden Sie sie, wenn keine der vordefinierten Sequenzen richtig zu Ihrer Platine passt. Die hier gespeicherten Sequenzen erscheinen als **CUSTOM**-Optionen im Live-Vorschaufenster, wenn Sie eine REFERENZ aufnehmen oder eine Inspektion starten.

Weitere Informationen zu dieser Funktion finden Sie im folgenden Abschnitt: [Benutzerdefinierte Aufnahmesequenzen](../features/Custom_sequences.md)

!!! note "Hinweis"
    Diese Registerkarte wird bei Einheiten im **Q1-Modus** nicht angezeigt, da diese nur eine einzige Aufnahme machen.

## Maschine

![Maschinenabschnitt des Einstellungsmenüs](../assets/v7/settings/machine-settings.png){.center}

Diese Registerkarte ist nur für Benutzer mit der Rolle **admin** verfügbar. Sie zeigt die Hardware-Parameter Ihrer Einheit an, die in der Datei **machine.json** gespeichert sind.

Die meisten Werte werden ausgegraut dargestellt: sie dienen **nur zur Information** und können nicht geändert werden. Die blau hervorgehobenen Felder sind die bearbeitbaren:

| Feld | Beschreibung |
| --- | --- |
| **xacc** / **yacc** / **zacc** | Beschleunigung der jeweiligen Achse. |
| **xhome** / **yhome** / **zhome** | Versatz der Ausgangsposition der jeweiligen Achse. |
| **capture_gain** | Kameraverstärkung während der Aufnahme. |
| **exposure** | Belichtungszeit der Kamera. |

Drücken Sie **Save changes**, um die neuen Werte anzuwenden, oder **Reset to factory default**, um alle Parameter auf ihren ursprünglichen Wert zurückzusetzen.

!!! warning "Wichtig"
    Diese Parameter beeinflussen die Bewegung der Plattform und die Bildaufnahme. Eine falsche Änderung kann die Bildqualität oder die Bewegung der Achsen verschlechtern. Ändern Sie sie nur, wenn der [Support](mailto:support@agnospcb.com) Sie dazu auffordert.

!!! note "Hinweis"
    Diese Registerkarte wird bei Einheiten ohne XYZ-Plattform nicht angezeigt.

## Debug

![Debug-Abschnitt des Einstellungsmenüs](../assets/v7/settings/debug-settings.png){.center}

Diese Registerkarte ist nur für Benutzer mit der Rolle **admin** verfügbar. Sie erzeugt einen **Diagnosebericht**, mit dem unser Support-Team das Verhalten Ihrer Einheit analysieren kann.

So erzeugen Sie ihn:

1. Legen Sie die **Kalibrierplatine** in die Mitte des Inspektionsbereichs. Falls Sie sie nicht haben, verwenden Sie eine Musterplatine **kleiner als 20x20 cm**.
2. Drücken Sie **Generate DEBUG report**.
3. Warten Sie, bis der Fortschrittsbalken abgeschlossen ist. Der Textbereich darunter zeigt den Fortschritt des Vorgangs an.
4. Sammeln Sie die erzeugten Dateien und senden Sie sie an [support@agnospcb.com](mailto:support@agnospcb.com).

## Informationsbereich

![Informationsabschnitt des Einstellungsmenüs](../assets/v7/ui-settings-info.png){width=650px .center}

#### AOI-Informationen

Die Informationen der AOI werden in diesem Abschnitt angezeigt.

#### Backup

Diese Funktion erzeugt automatisch eine komprimierte Sicherungsdatei des Ordners **PCB_OUT**. Die Sicherungsdatei wird im Ordner **APP/BACKUP** gespeichert.

#### Einstellungs-Passwort

Legt ein Passwort für den Zugriff auf das Einstellungsmenü fest.

!!! note "Hinweis"
    Lassen Sie das Passwort leer, um die Passwortabfrage zu deaktivieren.
