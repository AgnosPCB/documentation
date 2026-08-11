---
hide:
  - navigation
---

<div class="agnos-hero" markdown>

![AgnosPCB](assets/agnospcb-logo.gif){.center}

# Documentation AgnosPCB

<p class="agnos-hero-tagline">
Un service d'<strong>inspection optique automatisée (AOI)</strong> abordable, basé sur
une technologie de <strong>réseau de neurones</strong>. Vous trouverez ici tout le
nécessaire pour déballer, installer et maîtriser votre système d'inspection.
</p>

<div class="agnos-hero-actions" markdown>
[Démarrer :octicons-arrow-right-24:](getting_started/Package_content.md){.md-button .md-button--primary}
[Comment l'utiliser](how_to/Screen-layout.md){.md-button}
</div>

</div>

<div class="agnos-highlights" markdown>

<div markdown>
<span class="agnos-highlight-icon">:material-brain:</span>
**Inspection neuronale**
<p>Les défauts sont détectés en comparant chaque carte à une RÉFÉRENCE entraînée.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-clock-fast:</span>
**Mise en route rapide**
<p>Du déballage à votre première inspection, sans programmer le moindre test.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-file-chart-outline:</span>
**Rapports traçables**
<p>Chaque inspection génère un rapport à archiver, partager et auditer.</p>
</div>

<div markdown>
<span class="agnos-highlight-icon">:material-tools:</span>
**Outils supplémentaires**
<p>Lecture de codes-barres, inspection UV, mesure et bien plus encore.</p>
</div>

</div>

## Par où souhaitez-vous commencer ?

<div class="grid cards" markdown>

-   :material-package-variant:{.lg .middle} **Mise en route**

    ---

    Déballez votre machine, vérifiez le contenu du colis et raccordez l'ensemble
    pour la première fois.

    * [Contenu du colis](getting_started/Package_content.md) — ce que vous devez avoir reçu
    * [Guide de déballage](getting_started/Unboxing.md) — montage étape par étape
    * [Guide de connexion](getting_started/Connection_guide.md) — câbles, alimentation et caméra

    [:octicons-arrow-right-24: Commencez ici](getting_started/Package_content.md)

-   :material-monitor-dashboard:{.lg .middle} **Comment utiliser le logiciel**

    ---

    Apprenez l'interface et réalisez des inspections, des bases aux options avancées.

    * [Terminologie](how_to/terminology.md) — RÉFÉRENCE, UUI, inférence, faux positif…
    * [Interface utilisateur](how_to/Screen-layout.md) — disposition de l'écran et zones de travail
    * [Flux de travail d'inspection](how_to/Inspection_workflow.md) — la procédure complète
    * [Menu des paramètres](how_to/Settings_menu.md) — options d'interface, de flux de travail et de rapport

    [:octicons-arrow-right-24: Apprendre le logiciel](how_to/Screen-layout.md)

-   :material-wrench-outline:{.lg .middle} **Support et maintenance**

    ---

    Gardez le système en bon état et résolvez les problèmes lorsqu'un comportement
    est inattendu.

    * [Maintenance](maintenance/maintenance.md) — courroies, nettoyage et lubrification
    * [Mise à jour du logiciel](maintenance/update_software.md) — gardez votre ordinateur AOI à jour
    * [Configuration réseau](maintenance/network_configuration.md) — configuration de l'interface réseau
    * [Dépannage](maintenance/Troubleshooting.md) — problèmes courants et solutions

    [:octicons-arrow-right-24: Obtenir de l'aide](maintenance/Troubleshooting.md)

-   :material-lightbulb-on-outline:{.lg .middle} **Informations supplémentaires**

    ---

    Réponses rapides et conseils pratiques issus de l'expérience des utilisateurs.

    * [FAQ](help/FAQ.md) — réponses aux questions les plus fréquentes
    * [Conseils](help/Tips.md) — obtenir une bonne RÉFÉRENCE et une bonne inspection

    [:octicons-arrow-right-24: Lire la FAQ](help/FAQ.md)

</div>

## Votre première inspection en quatre étapes

1. **Installez la machine.** Suivez le [guide de déballage](getting_started/Unboxing.md) et le
   [guide de connexion](getting_started/Connection_guide.md) pour monter et alimenter le système.
2. **Apprenez le vocabulaire.** Une lecture rapide de la page
   [terminologie](how_to/terminology.md) rend tous les autres guides plus faciles à suivre.
3. **Créez une RÉFÉRENCE.** Capturez une carte reconnue conforme — voyez les
   [conseils](help/Tips.md) pour obtenir une image propre, ou convertissez une carte déjà inspectée avec
   [UUI vers RÉFÉRENCE](how_to/UUI_to_REFERENCE.md).
4. **Inspectez et éditez le rapport.** Lancez le
   [flux de travail d'inspection](how_to/Inspection_workflow.md) et générez votre rapport.

!!! tip "Les résultats ne sont pas ceux attendus ?"

    La plupart des problèmes de détection se résument à deux réglages : la
    [sensibilité](how_to/Set_sensitivity.md) et les
    [zones d'exclusion](how_to/Set_exclusion_area.md) de votre RÉFÉRENCE.

## Outils et fonctionnalités

<div class="grid cards agnos-features" markdown>

-   :material-barcode-scan:{.lg .middle} **[Lecteur de code-barres](features/Barcode_reader.md)**

    ---

    Chargez une RÉFÉRENCE automatiquement en scannant le code-barres de la carte.

-   :material-select-off:{.lg .middle} **[Zone d'exclusion](how_to/Set_exclusion_area.md)**

    ---

    Ignorez les zones qui changent légitimement d'une carte à l'autre.

-   :material-tune-vertical:{.lg .middle} **[Sensibilité](how_to/Set_sensitivity.md)**

    ---

    Équilibrez la détection des défauts et les faux positifs.

-   :material-file-replace-outline:{.lg .middle} **[UUI vers RÉFÉRENCE](how_to/UUI_to_REFERENCE.md)**

    ---

    Transformez une carte inspectée en nouvelle RÉFÉRENCE.

-   :material-cursor-default-click-outline:{.lg .middle} **[Icônes de l'espace de travail](how_to/Workspace_icons.md)**

    ---

    Commandes des croix, du traitement automatique et de la couleur du masque d'erreurs.

-   :material-lightbulb-fluorescent-tube-outline:{.lg .middle} **[Inspection du revêtement UV](features/UV_conformal_coating_inspection.md)**

    ---

    Inspectez le revêtement conforme sous éclairage UV.

-   :material-content-duplicate:{.lg .middle} **[Variantes de référence](features/Multivariant_feature.md)**

    ---

    Acceptez plusieurs versions valides d'une même carte.

-   :material-ruler:{.lg .middle} **[Outil de mesure](features/Measurement_tool.md)**

    ---

    Mesurez des distances directement sur l'image capturée.

-   :material-vector-arrange-above:{.lg .middle} **[Alignement manuel](features/Manual_alignment.md)**

    ---

    Alignez manuellement la RÉFÉRENCE et l'UUI si nécessaire.

</div>

## Besoin d'aide ?

<div class="grid cards" markdown>

-   :material-email-fast-outline:{.lg .middle} **Contacter l'assistance**

    ---

    Notre équipe répond aux questions techniques et aide en cas de problème matériel.

    [:octicons-arrow-right-24: support@agnospcb.com](mailto:support@agnospcb.com)

-   :material-web:{.lg .middle} **Visiter notre site web**

    ---

    Informations produit, tarifs et actualités du système AOI AgnosPCB.

    [:octicons-arrow-right-24: agnospcb.com](https://agnospcb.com/)

</div>
