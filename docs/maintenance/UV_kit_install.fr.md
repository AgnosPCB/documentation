# Installation du kit de revêtement UV

Ce guide indique les étapes nécessaires pour installer le **module d'inspection du revêtement UV** sur l'**AOI AI-4050**.


## Guide d'installation vidéo

<iframe width="100%" height="400" src="https://www.youtube.com/embed/JY0PqEUxGlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Liste des pièces incluses

## Installation du câble d'alimentation

!!! note "Note"

    Les nouvelles unités incluent le câble d'alimentation du module UV préinstallé. Si votre AOI dispose déjà de ce câble, passez à l'étape suivante.
    ![Câble d'alimentation préinstallé](../assets/v7/UV_install/power_cable_pre-mounted.png){width=200px .center}


La carte de contrôle se trouve à l'intérieur de la chambre d'inspection, en haut à droite. Retirez l'autocollant d'avertissement du capot et dévissez la vis intérieure à l'aide d'un tournevis hexagonal. Retirez le capot en plastique de la carte de contrôle.

![Emplacement de la carte de contrôle](../assets/v7/UV_install/board_location.png){.center}


Desserrez les vis du bornier indiqué sur l'image.

![Emplacement des bornes](../assets/v7/UV_install/terminals_location.png){.center}

Connectez le fil noir à la borne de gauche (négative) et le fil rouge à la borne de droite (positive). Assurez-vous que chaque fil est entièrement inséré dans la borne, puis serrez les deux vis. Vérifiez que les connexions sont solides en tirant doucement dessus.

![Polarité des bornes](../assets/v7/UV_install/terminals_polarity.png){.center}

Une fois le câble connecté, remettez le capot du boîtier en place et serrez la vis pour le fixer.

## Mise en place et connexion du convertisseur abaisseur de tension CC

Placez l'une des vis M5 avec son écrou, fournis avec le kit, dans la rainure du cadre en aluminium vertical situé sous la carte de contrôle. Ne la serrez pas complètement pour l'instant.

Placez la seconde vis au-dessus de la première, à environ 10 centimètres de distance.

![Emplacement des vis](../assets/v7/UV_install/dc_screws.png){.center}

Positionnez le régulateur de tension avec le fil rouge orienté vers le haut et fixez-le avec les deux vis.

!!! warning "Important"
    Veillez à ce que les écrous tournent bien dans la rainure et que les vis soient correctement serrées.


Connectez les fils noir et rouge au câble d'alimentation de la carte de contrôle.

![Convertisseur CC installé](../assets/v7/UV_install/dc_installed.png){.center}

## Installation des LED UV

Placez les LED UV sur le bord supérieur de l'anneau lumineux, au niveau des repères en triangle jaune, ou, s'ils ne sont pas marqués, au milieu de chaque côté.

![Repères jaunes](../assets/v7/UV_install/yellow_marks.png){.center}


Insérez le support de LED dans le haut du bord blanc, en laissant la LED vers le haut, et appuyez jusqu'à entendre un clic. Répétez cette opération pour les 3 LED restantes.

![Insertion des LED UV](../assets/v7/UV_install/insert_uv.png){.center}

Collez les guide-câbles au-dessus de l'anneau d'éclairage, l'ouverture de la pince orientée vers le haut. Positionnez-les aux meilleurs emplacements pour faciliter le passage des câbles UV.

![Guide-câbles](../assets/v7/UV_install/cable_holder.png){.center}

## Connexion des LED UV au convertisseur CC

Une fois les LED UV installées, connectez le câble d'alimentation en « Y » à la partie inférieure du convertisseur abaisseur de tension CC (fils noir et jaune), puis continuez en connectant chaque LED à sa broche correspondante. Notez que l'un des fils est plus court que l'autre.

Faites passer les fils dans les guides précédemment installés, en veillant à ce qu'ils ne soient pas visibles par la caméra.

![Câble acheminé](../assets/v7/UV_install/cable_routed.png){.center}
