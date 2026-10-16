# Lecteur de code-barres

Le logiciel AgnosPCB intègre une fonction de lecture de code-barres qui prend en charge les **codes-barres 1D, QR et Datamatrix**.

Vous pouvez soit prendre une photo de **RÉFÉRENCE**, soit en télécharger une directement depuis vos fichiers en utilisant le bouton **"Ouvrir référence"**.

![Zone de code-barres sélectionnée](../assets/v7/ui-button4.png){.center}

Appuyez sur le bouton **"dessiner la zone de code-barres"** et dessinez une zone où se trouve un code sur le panneau, puis définissez de quel type de code il s'agit : **ID, Batch ID, Model ou Misc**. Répétez cette opération pour chaque code que vous souhaitez faire lire par le logiciel, jusqu'à **quatre** types différents.

![Lecture de code](../assets/v7/barcode/1-bc-menu.png){.center}

Si l'option **mandatory barcode** est activée sur un code donné, l'inspection ne se poursuivra pas tant que ce code n'aura pas été lu correctement. S'il n'est pas détecté automatiquement, l'opérateur est invité à le saisir manuellement avant de poursuivre.

Une fois la RÉFÉRENCE chargée, passez à l'inspection en prenant une photo de l'UUI. Chacun des codes de l'UUI sera lu automatiquement dans les zones définies sur la RÉFÉRENCE.

Poursuivez le [processus d'inspection](../how_to/Inspection_workflow.md) comme d'habitude. 

Le code scanné sera inclus dans le rapport PDF final de l'UUI.

![Rapport avec code-barres inclus](../assets/barcode-report.png){.center}

## Charger une RÉFÉRENCE par code-barres

Si vous avez déjà une **RÉFÉRENCE** stockée, vous pouvez facilement la récupérer en utilisant le code qui lui est associé. Pour ce faire, appuyez sur le bouton **"lire le code-barres"**, puis lisez le code-barres à l'aide du lecteur portable, et la **RÉFÉRENCE** se chargera automatiquement. Il est également possible de saisir le code manuellement.

![Chargement RÉFÉRENCE par code-barres](../assets/v7/ui-barcode-loading.png){.center}

![Chargement RÉFÉRENCE par code-barres](../assets/v7/ui-bc_ref.png){.center}

![Lecteur de code-barres portable](../assets/barcode-handhold.png){.center}
