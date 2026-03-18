# Konfiguration der Netzwerkschnittstelle

!!! warning "Warnung"
    Die folgende Anleitung gilt **nur für OFFLINE-Einheiten**.

Da der OFFLINE-Benutzer keinen Zugriff auf den Root-Benutzer des Systems hat, ermöglicht das benutzerdefinierte AgnosPCB-Betriebssystem dem Benutzer, die Netzwerkschnittstelleneinstellungen des Systems mithilfe einer einfachen Konfigurationsdatei zu ändern.

Um die Schnittstelleneinstellungen festzulegen, öffnen Sie einen Texteditor und fügen Sie Ihre Konfiguration im folgenden Format hinzu:

~~~
{
  "IP": "192.168.1.23",
  "PREFIX": "24",
  "GATEWAY": "192.168.1.1",
  "DNS1": "8.8.8.8",
  "DNS2": "8.8.4.4"
}
~~~

Ersetzen Sie die Werte entsprechend Ihren Netzwerkanforderungen. Speichern Sie die Datei als **network.conf** im Ordner **APP**. 
Starten Sie das System neu, und nach 1 Minute wird die Konfiguration automatisch angewendet.