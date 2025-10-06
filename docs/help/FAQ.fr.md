## **Questions générales**
___

??? question "Existe-t-il des plans de location / d'essai pour les plateformes d'inspection EN LIGNE et HORS LIGNE ?"

    Oui, nous avons un plan de location pour les unités HORS LIGNE pour **un minimum de 2 mois**. Si vous décidez finalement de la conserver, le coût de la location sera déduit du prix final de l'unité. [Contactez-nous](mailto:support@agnospcb.com) pour demander un devis.

??? question "Comment puis-je générer un rapport d'erreur non détectée ?"

    Vous pouvez signaler une défaillance non détectée en déplaçant le curseur sur la zone de la défaillance et en appuyant sur la flèche BAS. Les images sont signalées à notre serveur et nous les utilisons pour entraîner le Réseau Neuronal à détecter ces erreurs. L'erreur sera incluse dans la prochaine mise à jour du Réseau Neuronal.

??? question "Quelle est la taille maximale de PCB qui peut être inspectée avec ce système ?"

    Le nouveau **AI-4050** permet l'inspection de PCBA (cartes de circuits imprimés assemblées) jusqu'à 40 x 50 cm (16 x 19").

??? question "Quelle est la différence entre les 'mises à jour du client' et les 'mises à jour du réseau neuronal' ? À quelle fréquence ces mises à jour sont-elles fournies ?"

    Les mises à jour du client font référence à l'interface graphique utilisée par l'opérateur, qui comprend des fonctionnalités pour faciliter les inspections de PCBA. Quant aux mises à jour du réseau neuronal, elles font référence à l'architecture qui effectue les inspections et renvoie le résultat au logiciel client. Les unités EN LIGNE n'ont pas besoin de mises à jour du réseau neuronal car elles utilisent la dernière version publiée sur le serveur d'AgnosPCB. Les unités HORS LIGNE peuvent également mettre à jour l'architecture du réseau neuronal facilement avec une simple clé USB. Le réseau neuronal est généralement mis à jour tous les 3-4 mois.

??? question "Comment puis-je gérer mon abonnement en ligne ?"

    [Contactez-nous](mailto:support@agnospcb.com) chaque fois que vous avez besoin d'apporter une modification à votre abonnement.

??? question "L'IA d'AgnosPCB apprend-elle seule à partir des inspections qu'elle traite ?"

    Non. Nous ne pouvons pas permettre au réseau neuronal d'apprendre seul, car cela pourrait entraîner un comportement logiciel incorrect et compromettre les performances du système. Nos ingénieurs surveillent attentivement les échantillons de formation, les implémentent dans le réseau neuronal et effectuent des tests approfondis pour éviter tout comportement indésirable.

??? question "Que puis-je faire si le système ne détecte pas une défaillance ?"

    Si vous constatez que le logiciel ne détecte pas certaines défaillances ou marque constamment un faux positif, envoyez-nous simplement un [e-mail](mailto:support@agnospcb.com) avec les images où l'erreur n'est pas détectée (images de RÉFÉRENCE et d'UUI), et nous implémenterons la défaillance dans la prochaine mise à jour du réseau neuronal.

??? question "Que puis-je faire avec les erreurs détectées qui sont de faux positifs ?"

    Vous pouvez naviguer à travers les erreurs détectées avec les flèches GAUCHE et DROITE. Pour marquer comme faux positif, appuyez sur la flèche HAUT et cela nous sera signalé (uniquement sur les unités EN LIGNE). Pour les unités HORS LIGNE, vous pouvez également le signaler comme faux positif avec la flèche HAUT. Une image recadrée sera générée dans le dossier REPORTS. Envoyez-la-nous ensuite par e-mail et nous l'incorporerons à la prochaine architecture de réseau neuronal. Ce retour d'information est important pour nous afin d'améliorer le taux de détection.

??? question "Comment le système fonctionne-t-il avec les boîtiers de style QFN ?"

    Le matériel actuel n'est pas capable de voir comment les composants QFN sont soudés, mais il est capable de détecter un mauvais positionnement, un déplacement, des torsions ou une contamination près du circuit intégré.

??? question "Je souhaite utiliser mes propres optiques et système d'éclairage, comment puis-je intégrer le logiciel d'inspection AgnosPCB ?"

    Si vous prévoyez d'utiliser votre propre matériel, vous avez 2 options :

    - Utiliser notre [application Windows](https://agnospcb.com/software-tool-download/) + vous abonner à l'un de [nos plans](https://agnospcb.com/pricing-eur/). Cela nécessite un ordinateur Windows et une connexion Internet stable. De cette façon, vous pourrez stocker les images prises par votre propre caméra dans un dossier spécifique où le logiciel les capturera et les inspectera automatiquement. Vous pouvez également télécharger les images manuellement car cette version ne prend pas en charge le contrôle à distance de la caméra.

    - Configurer notre [API](https://agnospcb.com/agnospcb-api/) + vous abonner à un [plan] GOLD (https://agnospcb.com/pricing-eur/) ou supérieur. Il s'agit d'un script Python qui vous permet d'intégrer facilement notre logiciel d'inspection à votre système. Il peut fonctionner sur tout système capable d'exécuter un script Python. Cela nécessite une connexion Internet stable.

??? question "Je souhaite construire ma propre boîte lumineuse. Avez-vous des recommandations pour la configurer ?"

    Pour des résultats optimaux, l'éclairage doit être à la fois adéquat et cohérent, dans le but d'éliminer les ombres. Il est recommandé d'utiliser un éclairage blanc pour une meilleure clarté. Un anneau lumineux peut être utilisé s'il fournit suffisamment d'illumination. Cependant, la considération clé est de maintenir des **conditions d'éclairage cohérentes** à tout moment. Soyez prudent avec les influences de l'éclairage externe qui peuvent varier les conditions entre les photos. Cela peut causer des problèmes à l'algorithme de détection. Si vous le pouvez, enfermez la zone d'inspection autant que possible.

??? question "La version HORS LIGNE permet-elle des inspections illimitées ?"

    Les unités HORS LIGNE impliquent un achat unique avec des inspections illimitées.

??? question "Puis-je utiliser ma caméra/AOI actuelle pour inspecter ?"

    Oui, vous le pouvez. Les images peuvent être stockées dans le dossier PCB\_IN pour un traitement automatique, chargées manuellement sous forme de fichiers, ou envoyées directement au service API.

??? question "Quelle caméra est recommandée ?"

    Une caméra avec une résolution d'au moins **20 MP** devrait fournir suffisamment de détails pour l'inspection des composants. Quant à l'objectif, vous devriez viser une longueur focale qui assure un équilibre entre l'affichage de composants suffisamment grands pour que le réseau neuronal puisse détecter les défauts et qui ne produit pas d'effets de distorsion sur les composants hauts.

??? question "Est-il possible d'inspecter les composants THT (composants traversants) ?"

    Le système AOI d'AgnosPCB n'est pas spécifiquement conçu pour les composants à technologie traversante (THT - Through-Hole Technology). Cela est dû aux potentielles grandes différences de perspective causées par la hauteur des composants THT, ce qui peut entraîner de faux positifs dans le Réseau Neuronal. De plus, le soudage des composants THT est souvent dissimulé, ce qui rend l'inspection difficile dans la plupart des cas.
    
    Cependant, bien que non optimisé pour les composants THT, le système AOI peut toujours être utilisé pour de tels composants. Il peut aider à détecter des déplacements, une polarité incorrecte, un basculement ou un placement incorrect des composants THT.

??? question "Comment puis-je utiliser la caméra pour prendre des photos de RÉFÉRENCE et d'UUI avec le logiciel d'inspection ?"

    La version Windows actuelle ne prend pas en charge le contrôle de la caméra car elle présente des problèmes de pilote et a été conçue uniquement pour tester les capacités du système AOI. La version officielle est basée sur Linux et prend en charge le contrôle de la caméra, la lecture de codes-barres et la génération de rapports.
    
    Cependant, vous pouvez partager le dossier PCB\_IN sur votre réseau, y placer toutes les photos, et le logiciel les traitera automatiquement. Vous devez d'abord charger la RÉFÉRENCE PCBA dans le logiciel et activer le bouton de traitement automatique.
    ![alt text](../assets/menu-auto-process.png)