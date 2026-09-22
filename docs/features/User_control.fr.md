# Contrôle d'accès des utilisateurs

## Qu'est-ce que le contrôle d'accès des utilisateurs ?

Par défaut, toute personne ayant accès à l'AOI peut utiliser le logiciel et modifier n'importe lequel de ses paramètres.

Le **contrôle d'accès des utilisateurs** vous permet de créer des comptes individuels et d'exiger un **nom d'utilisateur et un mot de passe** à chaque démarrage du logiciel. Chaque compte possède un rôle qui détermine ce que son utilisateur est autorisé à faire, ce qui vous permet de laisser un opérateur effectuer des inspections tout en gardant la configuration de la machine protégée.

## Les deux rôles

Chaque compte possède l'un de ces deux rôles :

| | **admin** | **operator** |
| --- | --- | --- |
| Options General, Workflow et Report | Oui | Oui |
| Options Date/time, Path et Share | Oui | Non |
| Users, Sequences, Machine et Debug | Oui | Non |
| Prendre une image de RÉFÉRENCE | Oui | Uniquement si le mode opérateur est désactivé |
| Gérer les utilisateurs | Oui | Non |
| Calibrer la plateforme | Oui | Non |
| Définir le mot de passe des paramètres | Oui | Non |
| Générer une sauvegarde | Oui | Non |

!!! note "Le rôle opérateur et le mode opérateur ne sont pas la même chose"

    Le **rôle opérateur** décrit ici limite les onglets du [menu des paramètres](../how_to/Settings_menu.md) que l'utilisateur peut ouvrir.

    Le **mode opérateur**, dans *Settings → Workflow*, simplifie l'interface et bloque la capture d'images de RÉFÉRENCE. Il s'applique à quiconque utilise la machine, quel que soit son rôle.

    Les deux peuvent être combinés : un compte opérateur avec le mode opérateur activé bénéficie à la fois de l'interface simplifiée et des paramètres restreints.

## Le configurer

### 1. Ouvrir l'onglet Users

Ouvrez le [menu des paramètres](../how_to/Settings_menu.md) et allez dans l'onglet **Users**. Sur une machine n'ayant jamais été configurée, la liste est vide et le contrôle d'accès est désactivé.

![Onglet Users](../assets/v7/user_control/users-tab.png){.center}

### 2. Créer d'abord un administrateur

Avant toute chose, vous avez besoin d'un compte **admin**. Si vous essayez d'activer le contrôle d'accès sans en avoir un, le logiciel refuse :

![Erreur d'absence d'utilisateur admin](../assets/v7/user_control/users-no-admin-error.png){width=350px .center}

Appuyez sur **Add user**, renseignez le nom d'utilisateur, sélectionnez le rôle **admin**, laissez **Active user** coché et saisissez le mot de passe deux fois.

![Ajouter un utilisateur admin](../assets/v7/user_control/users-add-admin.png){width=400px .center}

Appuyez sur **Save**. Le nouveau compte apparaît dans la liste, avec sa date de création.

![Administrateur créé](../assets/v7/user_control/users-admin-created.png){.center}

!!! warning "Important"

    Conservez le mot de passe de l'administrateur en lieu sûr. Une fois le contrôle d'accès activé, c'est ce compte qui vous permet de revenir dans le menu des paramètres.

### 3. Activer le contrôle d'accès

Avec un compte admin actif dans la liste, activez **Enable user access control**.

![Contrôle d'accès activé](../assets/v7/user_control/users-access-enabled.png){.center}

### 4. Ajouter les autres utilisateurs

Ajoutez un compte pour chaque personne qui utilisera la machine, en lui attribuant le rôle **operator**, sauf si elle doit modifier la configuration.

![Ajouter un utilisateur opérateur](../assets/v7/user_control/users-add-operator.png){width=400px .center}

La liste affiche chaque compte avec son rôle, son statut actif ou non, et les dates de création et de dernière modification.

![Liste des utilisateurs](../assets/v7/user_control/users-list.png){.center}

Appuyez sur **OK** pour enregistrer et fermer le menu des paramètres.

## Se connecter

Dès le prochain démarrage du logiciel, la fenêtre **User access required** demande les identifiants de l'un des comptes que vous avez créés.

![Fenêtre de connexion](../assets/v7/user_control/users-login.png){width=400px .center}

Le logiciel s'ouvre alors avec les autorisations de ce compte.

Pour fermer la session et permettre à un autre utilisateur de se connecter, utilisez le bouton **logout** de la [zone d'état de la plateforme](../how_to/Screen-layout.md).

## Gérer les comptes

Sélectionnez un compte dans la liste pour agir dessus :

- **Edit user** — modifie le rôle, le mot de passe ou l'état actif du compte sélectionné.
- **Delete user** — le supprime définitivement. Une confirmation est demandée.

!!! tip "Désactiver plutôt que supprimer"

    Pour empêcher quelqu'un d'utiliser la machine sans perdre la trace de son compte, modifiez l'utilisateur et décochez la case **Active user**. Le compte reste dans la liste mais ne peut plus se connecter.

!!! note "Note"
    Il doit toujours exister au moins un compte **admin actif**. Gardez cela à l'esprit avant de désactiver ou de supprimer un administrateur.
