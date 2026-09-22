# Anbindung an die Fertigungslinie (INLINE-Modus)

Diese Anleitung beschreibt, wie die **AgnosPCB AI 4050** in eine automatisierte
Fertigungslinie integriert wird, sodass die AOI Platinen von einem Förderband
übernimmt, sie ohne Eingriff eines Bedieners prüft und ein PASS/FAIL-Ergebnis
an die Liniensteuerung zurückmeldet.

Die Integration besteht aus zwei Teilen:

1. Dem **MODBUS-Modul**, das die AOI mit dem Förderband und der Liniensteuerung (SPS) verbindet.
2. Dem **INLINE-Modus** der Inspektionssoftware, der den unbeaufsichtigten Ablauf steuert.

!!! warning "Vor Beginn lesen"

    Die Linienanbindung umfasst elektrische Arbeiten sowohl an der AOI als
    auch an der Förderbandsteuerung. Sämtliche Verkabelung muss bei
    **beiden Systemen im spannungslosen Zustand** und durch Personal erfolgen,
    das für Arbeiten am Schaltschrank der Liniensteuerung qualifiziert ist.

---

## Bevor Sie beginnen

Prüfen Sie, ob Folgendes vorhanden ist:

- Eine bereits ausgepackte, montierte und im Standalone-Modus funktionierende
  **AI 4050**-Einheit. Falls Sie diesen Punkt noch nicht erreicht haben,
  schließen Sie zunächst die [Auspackanleitung](../getting_started/Unboxing.md)
  und den [Anschlussleitfaden](../getting_started/Connection_guide.md) ab.
- Ein bereits aufgenommenes und validiertes **REFERENZ**-Bild für jedes
  Produkt, das auf der Linie laufen wird. Der INLINE-Modus prüft gegen
  vorhandene REFERENZEN — er kann keine erstellen.
- Das für Ihre Einheit von AgnosPCB gelieferte **MODBUS-Modul**.
- Zugang zur Programmierumgebung der Liniensteuerung (SPS).

!!! note "Lizenzierung"

    Der INLINE-Modus und die JSON-Berichtsausgabe sind lizenzpflichtige
    Funktionen. Bestätigen Sie bei
    [support@agnospcb.com](mailto:support@agnospcb.com), dass Ihr
    Kontoprofil diese Funktionen aktiviert hat, bevor Sie die Linie in
    Betrieb nehmen — andernfalls wirken sich die Optionen nicht aus.

---

## 1. Installation des MODBUS-Moduls

<!-- TODO (AgnosPCB-Engineering): Die I/O-Zuordnung und der Anschluss an die
     Verarbeitungseinheit sind anhand der Schaltpläne dokumentiert. Es fehlt
     noch:
     - Wo das Modul montiert wird (DIN-Schiene im Schaltschrank? externes Gehäuse?)
     - Welches Netzteil den 7~36-V-Eingang speist, und dessen Leistung
     - Kabeltyp und maximale Leitungslänge für die RS-485-Verbindung und für die I/O
     - Ob die Relaiskontakte als Öffner oder Schließer verwendet werden, und ihre Nennlast
     - Details zur Verkabelung auf SPS-Seite -->

![Modbus-Verkabelung](../assets/v7/conveyor/modbus_wiring.png){.center}

Das Modul verfügt über **8 Relaisausgänge** und **8 digitale Eingänge**, von
denen die Integration einen Eingang und vier Ausgänge nutzt. Es wird über den
isolierten USB-zu-RS232/485-Konverter an einen **USB-Anschluss der
AgnosPCB-Verarbeitungseinheit** angeschlossen, wie im obigen Diagramm gezeigt.

### Eingänge

Der Eingang muss mit einem **Endschalter** oder einem beliebigen Sensor
verbunden werden, der erkennt, dass die PCBA sich in Position befindet und
bereit zur Prüfung ist.

| Eingang | Signal | Funktion |
|---|---|---|
| **DI1** | `BOARD_LOADED` | Löst eine Inspektion aus, sofern die Inspektionsplattform bereit ist. |

### Ausgänge

Die Ausgänge melden den Inspektionsstatus an den Rest der Fertigungslinie: an
das nachfolgende Förderband und an die SPS bzw. das Steuerungssystem der
Linie.

| Ausgang | Klemme | Signal | Aktiv, wenn |
|---|---|---|---|
| **DO1** | CH1 | `READY` | Die Inspektionsplattform ist bereit, eine Inspektion zu starten. |
| **DO2** | CH2 | `INSPECTING` | Die Inspektionsplattform führt gerade eine Inspektion durch. |
| **DO3** | CH3 | `BOARD OK` | Die Inspektion ist abgeschlossen und die geprüfte Platine ist in Ordnung. |
| **DO4** | CH4 | `BOARD NOK` | Die Inspektion ist abgeschlossen und an der Platine wurde ein Fehler festgestellt. |

!!! note "Wenn READY inaktiv ist"

    **DO1** ist während der Systeminitialisierung, während eine
    Verarbeitungsaufgabe läuft, oder wenn die Anwendung nicht im Hauptfenster
    angezeigt wird, nicht aktiv — zum Beispiel während das Einstellungsmenü
    oder das Referenz-Mosaik geöffnet ist.

### Gesamtverbindung

Das folgende Diagramm zeigt, wie alle beteiligten Elemente in einer typischen
Installation verbunden sind:

![Gesamtverbindung](../assets/v7/conveyor/general_connection.png){.center}

Vier Gerätegruppen sind an der Integration beteiligt:

- Das **AOI-Förderband**, das die Platine in den Inspektionsbereich befördert und die Kamera sowie den Positionssensor trägt.
- Der **AgnosPCB-Computer**, auf dem die Inspektionssoftware läuft.
- Das **MODBUS-Modul** zusammen mit seinem USB-zu-RS-485-Konverter, das zwischen der Software und den elektrischen Signalen der Linie übersetzt.
- Die **Linienausrüstung**: das auf die AOI folgende Förderband sowie die SPS oder das Steuerungssystem des Kunden.

Die Verbindungen zwischen ihnen sind wie folgt:

| Von | Nach | Verbindung | Zweck |
|---|---|---|---|
| Kamera des AOI-Förderbands | AgnosPCB-Computer | USB | Erfasst die Bilder der Platine. |
| AgnosPCB-Computer | USB-zu-RS232/485-Konverter | USB | Leitet die MODBUS-Kommunikation aus dem Computer heraus. |
| USB-zu-RS232/485-Konverter | MODBUS-Modul | RS-485 (**A+** / **B−**) | Verbindet den Konverter mit dem Relaismodul. |
| Endschalter/Sensor des AOI-Förderbands | Eingang **DI1** des MODBUS-Moduls | Digitaler Eingang | Signalisiert, dass die Platine in Position ist, was die Inspektion auslöst. |
| Ausgang **DO1** des MODBUS-Moduls | Nachfolgendes Förderband | Relaiskontakt | Teilt dem nächsten Förderband mit, dass die AOI bereit ist, eine Platine zu empfangen. |
| Ausgänge **DO2**, **DO3** und **DO4** des MODBUS-Moduls | SPS / Steuerungssystem des Kunden | Relaiskontakte | Melden den Fortschritt und das Ergebnis der Inspektion. |

!!! note "Stromversorgung"

    Zusätzlich zu diesen Verbindungen muss das MODBUS-Modul über seinen
    **7~36-V**-Eingang mit Strom versorgt werden, der im Diagramm nicht
    dargestellt ist.

---

## 2. Konfiguration der Inspektionssoftware

Sobald das Modul installiert ist und kommuniziert, bereiten Sie die Software
für den unbeaufsichtigten Betrieb vor. Alle folgenden Optionen befinden sich
im Fenster **Settings**; die vollständige Referenz finden Sie im
[Einstellungsmenü](../how_to/Settings_menu.md).

### 2.1 INLINE-Modus aktivieren

Öffnen Sie **Settings → Workflow** und aktivieren Sie **INLINE Mode (Conveyor)**.

![Abschnitt Workflow des Einstellungsmenüs](../assets/v7/settings/workflow-settings.png){.center}

Damit wechselt der Client vom manuellen, tastaturgesteuerten Arbeitsablauf zum
API-gesteuerten Arbeitsablauf, wie er auf einer Linie verwendet wird: Die
Inspektion wird von der Liniensteuerung ausgelöst, statt dass der Bediener
**S** drückt.

### 2.2 Empfohlene Begleiteinstellungen

Diese Optionen sind nicht zwingend erforderlich, machen aber auf einer
unbeaufsichtigten Linie den Unterschied zwischen einer sauberen Integration
und einem stehenden Förderband aus:

| Einstellung | Ort | Empfohlener Wert | Warum |
|---|---|---|---|
| **Operator mode** | Workflow | Aktiviert | Blendet die Referenzaufnahme aus und verhindert, dass ein Bediener die REFERENZ oder die Empfindlichkeit während der Schicht ändert. Schützen Sie es mit einem Einstellungspasswort (siehe [Einstellungsmenü](../how_to/Settings_menu.md)). |
| **Mandatory errors review** | Workflow | **Deaktiviert** | Ist diese Option aktiviert, wartet die Software, bis ein Mensch jeden Fehler überprüft hat, bevor die nächste Inspektion zugelassen wird — dies blockiert die Linie. |
| **Show errors popup** | Workflow | Deaktiviert | Verhindert, dass ein modaler Dialog während des Automatikbetriebs auf eine Eingabe wartet. |
| **Show references mosaic** | Workflow | Deaktiviert | Vermeidet ein Popup nach der Bildaufnahme. |
| **Auto report OK / NOK** | Reports | Beide aktiviert | Erzeugt das PDF für jede Platine ohne Bedienereingriff, sodass die Linie einen vollständigen Rückverfolgbarkeitsnachweis erzeugt. |
| **Create JSON report** | Reports | Aktiviert | Maschinenlesbares Ergebnis für Ihr MES/SCADA. Erfordert eine Lizenz. |
| **Use barcodes** | Workflow | Aktiviert | Ermöglicht es der AOI, die richtige REFERENZ automatisch anhand des Barcodes der Platine zu laden, sodass Linien mit gemischten Produkten keinen manuellen Produktwechsel benötigen. Erfordert eine Lizenz. Siehe [Barcode-Leser](../features/Barcode_reader.md). |

!!! note "Hinweis"

    Bei aktiviertem **Auto report** wird jeder Fehler mit der Kennzeichnung
    „unknown“ in das PDF geschrieben, da kein Bediener ihn klassifiziert.
    Das ist auf einer Linie zu erwarten — die Klassifizierung erfolgt später,
    offline, anhand der gespeicherten Berichte.

### 2.3 Wo die Ergebnisse gespeichert werden

Die Inspektionsergebnisse werden in den Ordner **PCB_OUT** geschrieben, der
unter **Settings → Paths** konfigurierbar ist.

Damit Ihr MES oder ein Netzlaufwerk sie automatisch abholen kann, aktivieren
Sie die Freigaben unter **Settings → Network**: **Share PCB_OUT**,
**Share REFERENCES** und **Share REPORTS** stellen diese Ordner im Netzwerk
bereit, und jede zeigt nach der Aktivierung ihren Netzwerkpfad an. Für
OFFLINE-Einheiten, die eine bestimmte Netzwerkschnittstelle benötigen, siehe
den Artikel zur
[Konfiguration der Netzwerkschnittstelle](../maintenance/network_configuration.md).

---

## 3. Inbetriebnahme-Checkliste

Bevor Sie die Zelle an die Produktion übergeben, prüfen Sie die folgenden
Punkte der Reihe nach. Führen Sie die ersten Tests mit dem Förderband im
manuellen/Tippbetrieb durch.

1. **Die Standalone-Inspektion funktioniert.** Führen Sie bei weiterhin
   deaktiviertem INLINE-Modus eine normale Inspektion über die Tastatur durch
   und bestätigen Sie, dass das Ergebnis korrekt ist. Wenn die AOI manuell
   nicht korrekt prüft, wird sie auch auf der Linie nicht korrekt prüfen.
2. **Die REFERENZEN sind geladen** für jedes Produkt, das auf der Linie
   laufen wird, und jede wurde an einer bekannt guten Platine validiert.
   Siehe [Tipps](../help/Tips.md).
3. **Das Lesen der Barcodes ist zuverlässig**, sofern Sie es für den
   Produktwechsel verwenden. Testen Sie es an mehreren Platinen, einschließlich
   der am schlechtesten gedruckten Etiketten, die Sie haben.
4. **Die Platinenpositionierung ist wiederholbar.** Das Förderband muss die
   Platine innerhalb des Inspektionsbereichs in einer konsistenten Position
   präsentieren — die AOI meldet **WARNING / ROTATED** oder
   **WARNING / SHIFTED**, wenn die Platine deutlich von der REFERENZ
   abweicht. Achten Sie während der ersten Durchläufe auf diese Warnungen und
   korrigieren Sie den mechanischen Anschlag oder die Platinenaufnahme, bevor
   Sie in die Produktion übergehen.
5. **Die MODBUS-Signale sind aktiv** — der Eingang **DI1** löst eine
   Inspektion aus, und die Ausgänge **DO1** bis **DO4** ändern ihren Zustand
   wie auf der Linienseite erwartet.
6. **Ein vollständiger Zyklus läuft von Anfang bis Ende**, sowohl mit einer
   bekannt guten als auch mit einer bekannt fehlerhaften Platine, und die
   Liniensteuerung erhält jedes Mal das korrekte PASS- bzw. FAIL-Ergebnis.
7. **Berichte werden geschrieben** in PCB_OUT und sind von Ihrem MES aus
   erreichbar.
8. **Das Verhalten bei einem Ausfall ist korrekt.** Stoppen Sie die
   AOI-Software mitten im Zyklus und bestätigen Sie, dass die Liniensteuerung
   den Ausfall erkennt und die Zufuhr von Platinen stoppt, statt sie
   ungeprüft durchlaufen zu lassen.

---

## Fehlerbehebung

| Symptom | Prüfung |
|---|---|
| Die Linie stoppt nach der ersten fehlerhaften Platine | **Mandatory errors review** ist aktiviert. Deaktivieren Sie es unter Settings → Workflow. |
| Ein Dialog wartet mitten im Zyklus auf eine Eingabe | Deaktivieren Sie **Show errors popup** und **Show references mosaic** unter Settings → Workflow. |
| Jede Platine schlägt bei einem neuen Produkt fehl | Die geladene REFERENZ passt nicht zum Produkt. Prüfen Sie die Barcode-Erkennung oder die für die Charge ausgewählte REFERENZ. |
| **WARNING / ROTATED** oder **WARNING / SHIFTED** bei den meisten Platinen | Das Förderband präsentiert die Platinen nicht in einer wiederholbaren Position. Korrigieren Sie den mechanischen Anschlag; die AOI vergleicht mit der Position der REFERENZ. |
| **WARNING / NO CROP** | Der Autocrop konnte die Platinenkante nicht finden, und das gesamte Bild wurde verglichen. Nehmen Sie die REFERENZ erneut auf, oder legen Sie den Zuschnittbereich manuell im Referenzbild fest. |
| Die AOI stoppt die Inspektion und zeigt `Engine [ OFFLINE ]` | Nur ONLINE-Einheiten: Die Internetverbindung oder das Konto ist ausgefallen. Siehe [Fehlerbehebung](../maintenance/Troubleshooting.md). |
| Guthaben mitten in der Schicht aufgebraucht | Nur ONLINE-Einheiten: Unterhalb von 10 Credits erscheint eine Warnung. Kontaktieren Sie [support@agnospcb.com](mailto:support@agnospcb.com). |

Bei allem, was hier nicht abgedeckt ist, wenden Sie sich an
[support@agnospcb.com](mailto:support@agnospcb.com).
