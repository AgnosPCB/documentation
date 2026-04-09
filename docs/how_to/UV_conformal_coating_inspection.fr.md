Dans ce guide, nous allons apprendre à utiliser l’inspection du revêtement conformal avec **AgnosPCB AOI**.

Cette fonctionnalité permet aux opérateurs d’inspecter visuellement le revêtement conformal des PCBAs à l’aide d’un éclairage UV.

!!! note "Note"
    Cette fonctionnalité nécessite l’installation d’un kit matériel séparé. Pour installer le kit UV, suivez les instructions dans la section suivante :
    [Guide d’installation du revêtement conformal UV](../maintenance/UV_kit_install.md)

!!! warning "Attention"
    L’inspection du revêtement conformal utilise un éclairage UV, donc **nous recommandons de porter les lunettes de sécurité** incluses dans le kit.

    ![Avertissement UV](../assets/v7/UV_inspection/warning_icon.png){ width=200px .center }

## Vidéo

Pour une présentation complète de cette fonctionnalité, regardez la vidéo suivante :

<video width="800" controls style="display: block; margin: 0 auto;">
  <source src="../assets/v7/UV_inspection/UV-mode-video.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la balise vidéo.
</video>

## 1. Générer une image de RÉFÉRENCE ou la charger

Pour générer une image de **RÉFÉRENCE**, suivez les étapes dans le [guide suivant](../how_to/Inspection_workflow.md#generating-a-reference) ou [chargez une RÉFÉRENCE existante](../how_to/Screen-layout.md#load-reference-as-file).

## 2. Ouvrir la vue en direct (Live View)

Utilisez le bouton de capture UUI pour ouvrir la [fenêtre de vue en direct](../how_to/Inspection_workflow.md#capturing-an-uui) du PCBA actuel.

![Fenêtre de vue en direct](../assets/UUI photo.PNG){ width=100px .center }

## 3. Activer l’inspection UV

Dans la fenêtre de vue en direct, activez l’**option d’inspection UV** située en bas de l’interface.

![Aperçu UV](../assets/v7/UV_inspection/UV_buttom.png){ .center }

Une fois activée, une simulation du PCB sous éclairage UV sera affichée.

![Simulation UV](../assets/v7/UV_inspection/UV_active.png){ .center }

!!! warning "Attention"
    À partir de ce moment, il est obligatoire de porter les lunettes de sécurité incluses dans le kit.

    ![Avertissement UV](../assets/v7/UV_inspection/warning_icon.png){ width=100px .center }

Ensuite, placez le UUI au centre de la zone d’inspection et appuyez sur le bouton **Démarrer l’inspection** pour lancer le processus.

![Bouton démarrer l’inspection](../assets/v7/UV_inspection/start-inspection-button.png){ width=250px .center }

## 4. Inspecter le revêtement

Observez le PCB sous éclairage UV afin de vérifier la bonne application et la couverture du revêtement conformal.

![Inspection UV](../assets/v7/UV_inspection/UV_inspection.png){ .center }

!!! note "Note"
    Cette inspection est réalisée manuellement par l’opérateur. Aucune détection basée sur l’IA n’est utilisée, l’opérateur doit donc identifier visuellement tout défaut ou absence de revêtement.

L’image UV capturée est incluse dans le rapport final d’inspection à des fins de documentation et de traçabilité.

![Rapport d’inspection UV](../assets/v7/UV_inspection/UV_report.png){width=500px, .center}