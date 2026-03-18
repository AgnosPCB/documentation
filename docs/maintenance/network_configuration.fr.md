# Configuration de l'interface réseau

!!! warning "Avertissement"
    Le guide suivant est **uniquement destiné aux unités HORS LIGNE (OFFLINE)**.

Étant donné que l'utilisateur HORS LIGNE n'a pas accès à l'utilisateur root du système, l'OS personnalisé d'AgnosPCB permet à l'utilisateur de modifier les paramètres de l'interface réseau du système en utilisant un simple fichier de configuration.

Pour définir les paramètres de l'interface, ouvrez un éditeur de texte et ajoutez votre configuration dans le format suivant :

~~~
{
  "IP": "192.168.1.23",
  "PREFIX": "24",
  "GATEWAY": "192.168.1.1",
  "DNS1": "8.8.8.8",
  "DNS2": "8.8.4.4"
}
~~~

Remplacez les valeurs par les exigences de votre réseau. Enregistrez le fichier sous le nom **network.conf** dans le dossier **APP**. 
Redémarrez le système et, après 1 minute, la configuration sera appliquée automatiquement.