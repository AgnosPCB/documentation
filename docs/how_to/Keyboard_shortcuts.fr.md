# Raccourcis clavier

Cette page répertorie tous les raccourcis clavier disponibles dans le **logiciel d'inspection AgnosPCB**, ainsi que les actions de la souris utilisées pour examiner les détections.

## Fenêtre principale

| Touche | Action |
| --- | --- |
| ++r++ | [Prendre une image de RÉFÉRENCE](Inspection_workflow.md#generation-dune-reference) (ouvre l'aperçu en direct). |
| ++s++ | [Lancer une inspection](Inspection_workflow.md#capture-dune-uui) (capturer l'UUI). |
| ++tab++ | Changer le mode d'affichage de l'[espace de travail principal](Screen-layout.md#espace-de-travail-principal) (RÉFÉRENCE / UUI). |
| ++page-up++ | Passer à la face **TOP** de la RÉFÉRENCE chargée (RÉFÉRENCES recto verso uniquement). |
| ++page-down++ | Passer à la face **BOTTOM** de la RÉFÉRENCE chargée (RÉFÉRENCES recto verso uniquement). |
| ++f1++ … ++f8++ | Charger la RÉFÉRENCE enregistrée dans cet emplacement de la [mosaïque de références](Screen-layout.md#mosaique-de-references). |
| ++arrow-right++ | Détection suivante (ou ligne suivante de la liste des détections avec [Préférence d'analyse](Settings_menu.md#preference-danalyse) = **LIST**). |
| ++arrow-left++ | Détection précédente (ou ligne précédente de la liste des détections avec Préférence d'analyse = **LIST**). |
| ++arrow-up++ | [Signaler](Inspection_workflow.md#signalement-des-erreurs) la détection comme une **erreur réelle** (ouvre la fenêtre de signalement). Sur une zone sans détection, signale une erreur non détectée par le logiciel. |
| ++arrow-down++ | Signaler la détection comme un **faux positif**. |
| ++1++ | [Sensibilité](Set_sensitivity.md) : Normale. |
| ++2++ | Sensibilité : Élevée. |
| ++3++ | Sensibilité : Très élevée. |
| ++space++ | Allumer / éteindre l'éclairage de la plateforme. |
| ++f++ | Afficher / masquer la superposition des erreurs signalées. |
| ++enter++ | Traiter une image chargée manuellement. |

!!! note "Remarque"
    Lorsque le [contrôle d'accès des utilisateurs](../features/User_control.md) est activé, les touches ++arrow-up++ et ++arrow-down++ nécessitent l'autorisation **Classify detected faults**.

## Examiner les détections avec la souris

| Action de la souris (sur l'image) | Action |
| --- | --- |
| Clic gauche sur une détection | La signaler comme **erreur réelle** (comme ++arrow-up++). Sur une détection déjà signalée comme erreur, demande une confirmation avant de l'annuler. |
| Clic droit sur une détection | La signaler comme **faux positif** (comme ++arrow-down++). |
| Clic gauche sur une zone vide | Signaler une erreur non détectée par le logiciel. |
| Garder le pointeur immobile sur une détection pendant environ 1 seconde | La marquer comme **vue**. |
| Clic droit en dehors d'une détection | Changer la forme de la loupe. |
| ++shift++ + clic droit | Changer la forme de la loupe, même sur une détection. |
| Molette de la souris | Changer le niveau de zoom. |

Les actions de la souris dans la liste des détections (miniatures, boutons, défilement) sont décrites dans [Liste des détections](Screen-layout.md#liste-des-detections).

## Fenêtre de signalement

| Touche | Action |
| --- | --- |
| ++arrow-up++ / ++arrow-down++ | Parcourir les options de la liste déroulante. |
| ++enter++ | Confirmer. |
| ++esc++ | Annuler. |

## Autres fenêtres

| Fenêtre | Touche | Action |
| --- | --- | --- |
| Aperçu en direct (RÉFÉRENCE / UUI) | ++enter++ | Confirmer / OK. |
| Aperçu en direct (RÉFÉRENCE / UUI) | ++esc++ | Annuler. |
| Mosaïque de références | ++f1++ … ++f8++ | Charger la RÉFÉRENCE de cet emplacement. |
| Liste de recherche des RÉFÉRENCES | ++esc++ | Fermer la fenêtre sans charger de RÉFÉRENCE. |
| Connexion | ++enter++ | Se connecter. |
| Menu des paramètres | ++enter++ | OK (enregistrer et fermer). |
| Menu des paramètres | ++esc++ | Fermer. |
