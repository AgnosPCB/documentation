# Configurazione dell'interfaccia di rete

!!! warning "Avviso"
    La seguente guida è **solo per le unità OFFLINE**.

Poiché l'utente OFFLINE non ha accesso all'utente root del sistema, il sistema operativo personalizzato di AgnosPCB consente all'utente di modificare le impostazioni dell'interfaccia di rete del sistema utilizzando un semplice file di configurazione.

Per impostare le configurazioni dell'interfaccia, aprire un editor di testo e aggiungere la propria configurazione con il seguente formato:

~~~
{
  "IP": "192.168.1.23",
  "PREFIX": "24",
  "GATEWAY": "192.168.1.1",
  "DNS1": "8.8.8.8",
  "DNS2": "8.8.4.4"
}
~~~

Sostituire i valori con i requisiti della propria rete. Salvare il file come **network.conf** nella cartella **APP**. 
Riavviare il sistema e, dopo 1 minuto, la configurazione verrà applicata automaticamente.