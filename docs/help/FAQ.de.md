## **Allgemeine Fragen**
___

??? question "Gibt es Miet-/Testpläne für die ONLINE- und OFFLINE-Inspektionsplattformen?"

    Ja, wir bieten einen Mietplan für OFFLINE-Einheiten für **mindestens 2 Monate** an. Wenn Sie sich schließlich entscheiden, die Einheit zu behalten, werden die Mietkosten vom Endpreis der Einheit abgezogen. [Kontaktieren Sie uns](mailto:support@agnospcb.com), um ein Angebot anzufordern.

??? question "Wie erstelle ich einen Bericht über nicht erkannte Fehler?"

    Sie können einen nicht erkannten Fehler melden, indem Sie den Cursor auf den Fehlerbereich bewegen und die NACH-UNTEN-Taste drücken. Die Bilder werden an unseren Server gemeldet und wir verwenden sie, um das Neuronale Netzwerk für die Erkennung dieser Fehler zu trainieren. Sie werden im nächsten Update des Neuronalen Netzwerks enthalten sein.

??? question "Was ist die maximale Leiterplattengröße, die mit diesem System inspiziert werden kann?"

    Die neue **AI-4050** ermöglicht die Inspektion von PCBA (bestückten Leiterplatten) bis zu 40 x 50 cm (16 x 19").

??? question "Was ist der Unterschied zwischen „Client-Updates“ und „Updates des Neuronalen Netzwerks“? Wie häufig werden diese Updates bereitgestellt?"

    Client-Upgrades beziehen sich auf die grafische Benutzeroberfläche, die vom Bediener verwendet wird und Funktionen zur Erleichterung der PCBA-Inspektionen enthält. Die Updates des Neuronalen Netzwerks beziehen sich auf die Architektur, die die Inspektionen durchführt und das Ergebnis an die Client-Software zurückgibt. ONLINE-Einheiten benötigen keine Updates des Neuronalen Netzwerks, da sie die neueste auf dem AgnosPCB-Server veröffentlichte Version verwenden. Die OFFLINE-Einheiten können die Architektur des Neuronalen Netzwerks ebenfalls einfach mit einem USB-Laufwerk aktualisieren. Das Neuronale Netzwerk wird üblicherweise alle 3-4 Monate aktualisiert.

??? question "Wie kann ich mein Online-Abonnement verwalten?"

    [Kontaktieren Sie uns](mailto:support@agnospcb.com) jederzeit, wenn Sie eine Änderung an Ihrem Abonnement vornehmen müssen.

??? question "Lernt die AgnosPCB AI selbstständig aus den von ihr verarbeiteten Inspektionen?"

    Nein, das tut sie nicht. Wir können dem Neuronalen Netzwerk nicht erlauben, selbstständig zu lernen, da dies zu einem fehlerhaften Softwareverhalten führen und die Leistung des Systems beeinträchtigen könnte. Unsere Ingenieure überwachen die Trainingsmuster sorgfältig, implementieren sie im Neuronalen Netzwerk und führen gründliche Tests durch, um unerwünschtes Verhalten zu vermeiden.

??? question "Was kann ich tun, wenn das System einen Fehler nicht erkennt?"

    Wenn Sie bemerken, dass die Software einige Fehler nicht erkennt oder ständig ein falsches Positiv markiert, senden Sie uns einfach eine [E-Mail](mailto:support@agnospcb.com) mit den Bildern, auf denen der Fehler nicht erkannt wird (REFERENZ- und UUI-Bilder), und wir werden den Fehler in das nächste Update des Neuronalen Netzwerks aufnehmen.

??? question "Was kann ich mit den erkannten Fehlern tun, die falsche Positive sind?"

    Sie können mit den Pfeiltasten LINKS und RECHTS durch die erkannten Fehler navigieren. Um einen Fehler als falsches Positiv zu markieren, drücken Sie die NACH-OBEN-Taste, und er wird an uns gemeldet (nur bei ONLINE-Einheiten). Bei OFFLINE-Einheiten können Sie ihn ebenfalls mit der NACH-OBEN-Taste als falsches Positiv kennzeichnen. Ein zugeschnittenes Bild wird im Ordner REPORTS erstellt. Senden Sie uns dieses dann per E-Mail zu, und wir werden es in die nächste Architektur des Neuronalen Netzwerks einbinden. Dieses Feedback ist uns wichtig, um die Erkennungsrate zu verbessern.

??? question "Wie funktioniert das System mit QFN-Gehäusen?"

    Die aktuelle Hardware ist nicht in der Lage, die Lötstellen von QFN-Komponenten zu sehen, kann aber eine schlechte Positionierung, Verschiebung, Verdrehungen oder Verunreinigungen in der Nähe des ICs erkennen.

??? question "Ich möchte meine eigene Optik und mein eigenes Beleuchtungssystem verwenden. Wie kann ich die AgnosPCB Inspektionssoftware integrieren?"

    Wenn Sie beabsichtigen, Ihre eigene Hardware zu verwenden, haben Sie 2 Optionen:

    - Verwendung unserer [Windows-Anwendung](https://agnospcb.com/software-tool-download/) + Abschluss eines [unserer Pläne](https://agnospcb.com/pricing-eur/). Dies erfordert einen Windows-Computer und eine stabile Internetverbindung. Auf diese Weise können Sie die von Ihrer eigenen Kamera aufgenommenen Bilder in einem spezifischen Ordner speichern, wo die Software sie automatisch erfasst und inspiziert. Sie können die Bilder auch manuell hochladen, da diese Version keine Fernsteuerung der Kamera unterstützt.

    - Konfiguration unserer [API](https://agnospcb.com/agnospcb-api/) + Abschluss eines GOLD-[Plans](https://agnospcb.com/pricing-eur/) oder höher. Dies ist ein Python-Skript, das es Ihnen ermöglicht, unsere Inspektionssoftware einfach in Ihr System zu integrieren. Es kann auf jedem System ausgeführt werden, das ein Python-Skript ausführen kann. Es erfordert eine stabile Internetverbindung.

??? question "Ich möchte meine eigene Lichtbox bauen. Haben Sie Empfehlungen für die Einrichtung?"

    Für optimale Ergebnisse sollte die Beleuchtung sowohl angemessen als auch konsistent sein, mit dem Ziel, Schatten zu eliminieren. Es wird empfohlen, weißes Licht für beste Klarheit zu verwenden. Ein Beleuchtungsring kann eingesetzt werden, wenn er genügend Beleuchtung bietet. Die wichtigste Überlegung ist jedoch, jederzeit **konsistente Beleuchtungsbedingungen** aufrechtzuerhalten. Seien Sie vorsichtig mit dem Einfluss von externem Licht, das die Bedingungen zwischen Fotos verändern kann. Dies kann zu Problemen für den Erkennungsalgorithmus führen. Wenn Sie können, schließen Sie den Inspektionsbereich so weit wie möglich ein.

??? question "Ermöglicht die OFFLINE-Version eine unbegrenzte Anzahl von Inspektionen?"

    Die OFFLINE-Einheiten erfordern einen einmaligen Kauf mit unbegrenzter Anzahl von Inspektionen.

??? question "Kann ich meine aktuelle Kamera/AOI zur Inspektion verwenden?"

    Ja, das können Sie. Die Bilder können zur automatischen Verarbeitung im Ordner PCB\_IN gespeichert, manuell als Dateien geladen oder direkt an den API-Dienst gesendet werden.

??? question "Welche Kamera wird empfohlen?"

    Eine Kamera mit einer Auflösung von **mindestens 20 MP** sollte genügend Details für die Komponenteninspektion liefern. Was das Objektiv betrifft, sollten Sie eine Brennweite anstreben, die ein Gleichgewicht zwischen der Darstellung der Komponenten groß genug für das Neuronale Netzwerk zur Fehlererkennung bietet und die keine stürzenden Effekte bei hohen Komponenten erzeugt.

??? question "Ist es möglich, THT-Komponenten (Through-Hole Technology) zu inspizieren?"

    Das AOI-System von AgnosPCB ist nicht speziell für THT-Komponenten (Durchkontaktierte Technologie) konzipiert. Dies liegt an den potenziell großen Perspektivunterschieden, die durch die Höhe der THT-Komponenten verursacht werden, was zu falschen Positiven im Neuronalen Netzwerk führen kann. Darüber hinaus sind die Lötstellen von THT-Komponenten oft verdeckt, was die Inspektion in den meisten Fällen erschwert.
    
    Obwohl das AOI-System nicht für THT-Komponenten optimiert ist, kann es dennoch für solche Komponenten verwendet werden. Es kann bei der Erkennung von Verschiebungen, falscher Polarität, Umdrehungen oder falscher Platzierung von THT-Komponenten helfen.

??? question "Wie verwende ich die Kamera, um REFERENZ- und UUI-Bilder mit der Inspektionssoftware aufzunehmen?"

    Die aktuelle Windows-Version unterstützt die Kamerasteuerung nicht, da sie Treiberprobleme aufweist und nur zum Testen der Funktionen des AOI-Systems konzipiert wurde. Die offizielle Version basiert auf Linux und unterstützt Kamerasteuerung, Barcode-Lesen und Berichtserstellung.
    
    Sie können jedoch den Ordner PCB\_IN in Ihrem Netzwerk freigeben, alle Bilder dort ablegen, und die Software verarbeitet sie automatisch. Zuerst müssen Sie die PCBA-REFERENZ in die Software laden und die Schaltfläche zur automatischen Verarbeitung aktivieren.
    ![alt text](../assets/menu-auto-process.png)