# Variantes de référence

Lors de l’inspection d’un PCB, certains composants peuvent différer de la référence et être détectés par le logiciel comme des erreurs (par exemple en raison de changements d’approvisionnement des composants ou de différences d’étiquetage).

En marquant ce type d’erreur comme **Variante de référence**, le système le reconnaîtra lors des inspections futures et ne le signalera plus comme une erreur.

## Vidéo
___

Pour une présentation complète de cette fonctionnalité, regardez la vidéo suivante :
 
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Y79a7xYpsv0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
___

## 1. Démarrer l’inspection

[Créer une image de référence](../how_to/Inspection_workflow.md#generating-a-reference) ou en sélectionner une [depuis le dépôt](../how_to/Screen-layout.md#load-reference-as-file). Ensuite, placez l’UUI et lancez l’inspection.

## 2. Identifier l’erreur

Naviguez jusqu’à l’erreur détectée à l’aide des **touches fléchées gauche/droite (←/→)**.

![Erreur de variante détectée](../assets/ref-variant-error.png){ width=600 .center }

## 3. Classer comme Variante de référence

Appuyez sur la **touche flèche bas (↓)** pour rejeter l’erreur. Dans le panneau de classification, sélectionnez **Reference variant**.

Une fenêtre de dialogue apparaîtra dans laquelle vous devrez saisir un nom pour la nouvelle variante (obligatoire) et, éventuellement, ajouter une description. Une fois terminé, cliquez sur **Confirm**.

![Panneau de classification](../assets/ref-variant-label.png){ width=400 .center }

## Résultat

Une fois classée, la variante de référence est enregistrée et liée à l’image de référence. Les variantes enregistrées peuvent être consultées en ouvrant une image de référence sauvegardée. Elles sont affichées dans le panneau latéral droit, sous la vue de référence agrandie. Depuis ce panneau, les variantes peuvent être activées, désactivées ou supprimées.

![Variante de référence enregistrée](../assets/ref-variant-stored.png){ width=600 .center }

Cette variante ne sera plus signalée comme une erreur lors des inspections futures.

!!! warning "Attention"
    Une variante de référence doit être créée manuellement pour chaque emplacement sur le PCB où la variation apparaît. Le système n’applique pas automatiquement la variante aux composants identiques situés à d’autres positions.

![Erreur de variante détectée](../assets/ref-variant-error.png){ width=400 .center }
![Flèche verte](../assets/green-arrow-down.png){ width=40 .center }
![Variante de référence](../assets/ref-variant-solved.png){ width=400 .center }

Même après avoir créé une variante de référence, le système continuera à détecter les défauts réels sur ce composant s’ils se produisent.

Le rapport final d’inspection inclura également la variante de référence, ainsi que son image, le nom attribué et toute observation supplémentaire.

![Rapport PDF de la variante de référence](../assets/ref-variant-report.png){ width=600 .center }