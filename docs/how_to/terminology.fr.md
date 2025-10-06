## **Réseau de Neurones**

Dans l'apprentissage automatique, le réseau de neurones fait référence à un groupe de neurones artificiels organisés d'une manière spécifique pour accomplir une tâche donnée. Chaque neurone représente une fonction mathématique. Dans le cas d'**AgnosPCB**, ces neurones effectuent une inspection visuelle des défauts sur les PCBA. L'architecture d'interconnexion de ces neurones est constamment améliorée pour augmenter les taux de détection des défauts.

![Architecture du Réseau de Neurones](../assets/v7/neural_networks.webp){width=700px, .center}

## **RÉFÉRENCE**

L'image de **RÉFÉRENCE** est l'image d'une PCBA exempte de défauts utilisée pour les inspections. Avant de générer l'image de RÉFÉRENCE, l'opérateur doit inspecter la PCBA de RÉFÉRENCE (carte GOLDEN) pour s'assurer qu'elle est exempte d'erreurs de fabrication.

![Image de Référence](../assets/v7/ref-example.jpg){width=500px, .center}

## **UUI**

L'**Unité Sous Inspection (UUI)** est l'image de la PCBA qui sera inspectée pendant la fabrication. Cette image est comparée à l'image de RÉFÉRENCE pour détecter les défauts de fabrication.

![Image UUI](../assets/v7/uui-example.jpg){width=500px, .center}

## **Inférence**

Ceci est le résultat de la comparaison des images de RÉFÉRENCE et UUI. Les erreurs, s'il y en a, sont marquées en rouge sur l'image UUI. Toutes les erreurs sont numérotées pour faciliter la référence.

![Image d'Inférence](../assets/v7/inference-example.png){width=500px, .center}

## **Rapport (Report)**

Les erreurs détectées par le logiciel doivent être examinées et confirmées par un opérateur. Elles peuvent être signalées comme une **erreur réelle** ou un **faux positif** et étiquetées avec le type d'erreur. Toutes ces erreurs signalées seront utilisées pour générer un rapport d'inspection PDF final.

![Fenêtre de Rapport](../assets/v7/ui-report.png){.center}

## **Erreur**

Nous définissons une **erreur** comme un composant qui n'est pas assemblé correctement, qui est endommagé ou qui est manquant. Toute contamination ou dommage sur la carte est également considéré comme une erreur.

## **Faux Positif**

La signalisation de **faux positif** se produit lorsque le logiciel AgnosPCB détecte une différence suffisante entre la RÉFÉRENCE et l'UUI sur un composant pour le signaler comme une erreur, mais qu'il n'y a pas de défaillance réelle affectant le fonctionnement de la PCBA. Cela peut être causé par un changement dans le marquage, la forme ou la couleur d'un composant qui est équivalent à la référence.