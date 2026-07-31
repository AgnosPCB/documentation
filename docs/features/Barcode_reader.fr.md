# **Lecteur de code-barres**

Le logiciel AgnosPCB intègre une fonction de lecture de code-barres qui prend en charge les **codes-barres 1D, QR et Datamatrix**.

Vous pouvez soit prendre une photo de **RÉFÉRENCE**, soit en télécharger une directement depuis vos fichiers en utilisant le bouton **"Ouvrir référence"**.

Sélectionnez le bouton **"dessiner la zone de code-barres"** et dessinez un rectangle dans la zone du code-barres.

![Zone de code-barres sélectionnée](../assets/v7/ui-button4.png){.center}

![Erreurs détectées](../assets/barcode-errors.png){.center}

Le code sera affiché dans le rectangle et dans le nom de la RÉFÉRENCE en haut à gauche. Assurez-vous que le code-barres a été lu avant de procéder à l'inspection.

Une fois la RÉFÉRENCE chargée, passez à l'inspection en prenant une photo de l'UUI. Le code-barres de l'UUI sera lu automatiquement dans la même zone que le code-barres de la RÉFÉRENCE.

Poursuivez le [processus d'inspection](Inspection_workflow.md/) comme d'habitude. 

Le code scanné sera inclus dans le rapport PDF final de l'UUI.

![Rapport avec code-barres inclus](../assets/barcode-report.png){.center}

## Charger une RÉFÉRENCE par code-barres

Si vous avez déjà une **RÉFÉRENCE** stockée, vous pouvez facilement la récupérer en utilisant le code qui lui est associé. Pour ce faire, appuyez sur le bouton **"lire le code-barres"**, puis lisez le code-barres à l'aide du lecteur portable, et la **RÉFÉRENCE** se chargera automatiquement. Il est également possible de saisir le code manuellement.

![Chargement RÉFÉRENCE par code-barres](../assets/v7/ui-barcode-loading.png){.center}

![Chargement RÉFÉRENCE par code-barres](../assets/v7/ui-bc_ref.png){.center}

![Lecteur de code-barres portable](../assets/barcode-handhold.png){.center}