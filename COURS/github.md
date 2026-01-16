# 🐙 Cours GitHub - Les Bases

## Table des matières

1. [Introduction à Git et GitHub](#1-introduction-à-git-et-github)
2. [Installation et Configuration](#2-installation-et-configuration)
3. [Premiers Pas avec Git](#3-premiers-pas-avec-git)
4. [Les Concepts Fondamentaux](#4-les-concepts-fondamentaux)
5. [Commandes Git Essentielles](#5-commandes-git-essentielles)
6. [GitHub : Interface Web](#6-github--interface-web)
7. [Travail avec les Branches](#7-travail-avec-les-branches)
8. [Collaboration sur GitHub](#8-collaboration-sur-github)
9. [Pull Requests](#9-pull-requests)
10. [Gestion des Conflits](#10-gestion-des-conflits)
11. [Fichiers Spéciaux](#11-fichiers-spéciaux)
12. [Bonnes Pratiques](#12-bonnes-pratiques)
13. [Workflows Avancés](#13-workflows-avancés)

---

## 1. Introduction à Git et GitHub

### Qu'est-ce que Git ?

**Git** est un **système de contrôle de version distribué** (DVCS - Distributed Version Control System). Il permet de :

- ✅ **Suivre les modifications** de fichiers au fil du temps
- ✅ **Collaborer** avec d'autres développeurs
- ✅ **Revenir en arrière** à n'importe quelle version précédente
- ✅ **Travailler en parallèle** sur différentes fonctionnalités
- ✅ **Fusionner** les modifications de plusieurs personnes

### Qu'est-ce que GitHub ?

**GitHub** est une **plateforme web** qui héberge des dépôts Git. C'est le plus grand hébergeur de code source au monde.

**Fonctionnalités principales** :
- 🌐 Interface web pour gérer les dépôts
- 👥 Collaboration en équipe
- 🔀 Pull Requests et code review
- 🐛 Gestion des issues (problèmes)
- 📊 Outils de visualisation (graphiques, statistiques)
- 🚀 GitHub Actions (CI/CD)
- 📝 Wiki et documentation

### Pourquoi utiliser Git/GitHub ?

1. **Historique complet** : Chaque modification est enregistrée
2. **Sécurité** : Possibilité de revenir en arrière en cas d'erreur
3. **Collaboration** : Plusieurs personnes peuvent travailler ensemble
4. **Backup** : Code sauvegardé en ligne
5. **Professionnel** : Standard de l'industrie

---

## 2. Installation et Configuration

### Installation de Git

#### Sur Windows
1. Télécharger depuis [git-scm.com](https://git-scm.com/download/win)
2. Installer avec les options par défaut
3. Vérifier : Ouvrir Git Bash et taper `git --version`

#### Sur macOS
```bash
# Via Homebrew
brew install git

# Vérifier
git --version
```

#### Sur Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
git --version
```

### Configuration initiale

```bash
# Configurer votre nom
git config --global user.name "Votre Nom"

# Configurer votre email
git config --global user.email "votre.email@example.com"

# Vérifier la configuration
git config --list

# Configurer l'éditeur par défaut (optionnel)
git config --global core.editor "code --wait"  # VS Code
```

### Créer un compte GitHub

1. Aller sur [github.com](https://github.com)
2. Cliquer sur "Sign up"
3. Choisir un nom d'utilisateur
4. Vérifier votre email

### Configurer SSH (recommandé)

#### Générer une clé SSH

```bash
# Générer une nouvelle clé SSH
ssh-keygen -t ed25519 -C "votre.email@example.com"

# Appuyer sur Entrée pour accepter l'emplacement par défaut
# Entrer un mot de passe (optionnel mais recommandé)
```

#### Ajouter la clé à GitHub

```bash
# Copier la clé publique
cat ~/.ssh/id_ed25519.pub
```

1. Sur GitHub : Settings → SSH and GPG keys → New SSH key
2. Coller la clé publique
3. Tester la connexion :

```bash
ssh -T git@github.com
```

---

## 3. Premiers Pas avec Git

### Créer un nouveau dépôt

#### Méthode 1 : Dépôt local

```bash
# Créer un nouveau dossier
mkdir mon-projet
cd mon-projet

# Initialiser Git
git init

# Créer un fichier
echo "# Mon Projet" > README.md

# Ajouter le fichier
git add README.md

# Faire le premier commit
git commit -m "Initial commit"
```

#### Méthode 2 : Cloner un dépôt existant

```bash
# Cloner un dépôt depuis GitHub
git clone https://github.com/utilisateur/nom-du-repo.git

# Ou avec SSH
git clone git@github.com:utilisateur/nom-du-repo.git

# Entrer dans le dossier
cd nom-du-repo
```

### Le cycle de vie des fichiers

```
┌─────────────┐
│ Untracked   │  (fichier non suivi)
└──────┬──────┘
       │ git add
       ▼
┌─────────────┐
│ Staged      │  (fichier ajouté, prêt à être commité)
└──────┬──────┘
       │ git commit
       ▼
┌─────────────┐
│ Committed   │  (fichier sauvegardé dans l'historique)
└─────────────┘
       │ modification
       ▼
┌─────────────┐
│ Modified    │  (fichier modifié mais pas encore ajouté)
└──────┬──────┘
       │ git add
       ▼
┌─────────────┐
│ Staged      │
└─────────────┘
```

### Vérifier l'état

```bash
# Voir l'état des fichiers
git status

# Version courte
git status -s
```

**Exemple de sortie** :
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   fichier.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        nouveau-fichier.py

no changes added to commit (use "git add" to commit)
```

---

## 4. Les Concepts Fondamentaux

### Dépôt (Repository / Repo)

Un **dépôt** est un dossier qui contient votre projet et tout l'historique Git.

- **Dépôt local** : Sur votre ordinateur
- **Dépôt distant (remote)** : Sur GitHub ou un autre serveur

### Commit

Un **commit** est une **sauvegarde** de l'état de vos fichiers à un moment donné.

```bash
# Chaque commit contient :
# - Un identifiant unique (hash)
# - Un message descriptif
# - L'auteur et la date
# - Un pointeur vers le commit précédent
```

### Branche (Branch)

Une **branche** est une **ligne de développement indépendante**.

- `main` ou `master` : Branche principale (par défaut)
- Autres branches : Pour développer des fonctionnalités séparément

```
main:     A---B---C---D
                \
feature:         E---F
```

### HEAD

**HEAD** est un pointeur qui indique sur quelle branche/commit vous êtes actuellement.

### Remote (Dépôt distant)

Un **remote** est une référence à un dépôt distant (comme GitHub).

- `origin` : Nom par défaut du dépôt distant

```bash
# Voir les remotes
git remote -v

# Ajouter un remote
git remote add origin https://github.com/user/repo.git
```

---

## 5. Commandes Git Essentielles

### Ajouter des fichiers

```bash
# Ajouter un fichier spécifique
git add fichier.txt

# Ajouter tous les fichiers modifiés
git add .

# Ajouter tous les fichiers d'un type
git add *.py

# Ajouter interactivement
git add -i
```

### Faire un commit

```bash
# Commit avec message
git commit -m "Ajout de la fonctionnalité X"

# Commit avec message détaillé
git commit -m "Titre" -m "Description détaillée"

# Ajouter et commiter en une commande (seulement pour fichiers déjà suivis)
git commit -am "Message"

# Modifier le dernier commit
git commit --amend
```

### Voir l'historique

```bash
# Historique complet
git log

# Historique sur une ligne
git log --oneline

# Historique avec graphique
git log --oneline --graph --all

# Historique d'un fichier
git log fichier.txt

# Voir les modifications d'un commit
git show <hash-du-commit>
```

### Annuler des modifications

```bash
# Annuler les modifications d'un fichier (avant git add)
git restore fichier.txt
# ou (ancienne syntaxe)
git checkout -- fichier.txt

# Retirer un fichier du staging (après git add, avant commit)
git restore --staged fichier.txt
# ou
git reset HEAD fichier.txt

# Annuler le dernier commit (garder les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (supprimer les modifications)
git reset --hard HEAD~1

# ⚠️ Attention : reset --hard est destructif !
```

### Ignorer des fichiers (.gitignore)

Créer un fichier `.gitignore` à la racine du projet :

```gitignore
# Fichiers Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
env/

# Fichiers de l'éditeur
.vscode/
.idea/
*.swp
*.swo
*~

# Fichiers système
.DS_Store
Thumbs.db

# Fichiers de logs
*.log

# Variables d'environnement
.env
.env.local

# Dossiers de build
dist/
build/
*.egg-info/
```

### Pousser et récupérer

```bash
# Pousser vers le dépôt distant
git push origin main

# Récupérer les modifications (sans fusionner)
git fetch origin

# Récupérer et fusionner
git pull origin main

# Pousser une nouvelle branche
git push -u origin nom-de-la-branche
```

---

## 6. GitHub : Interface Web

### Créer un nouveau dépôt sur GitHub

1. Cliquer sur le bouton **"+"** en haut à droite
2. Sélectionner **"New repository"**
3. Remplir les informations :
   - **Repository name** : Nom du dépôt
   - **Description** : Description (optionnel)
   - **Visibility** : Public ou Private
   - **Initialize with README** : Cocher si vous voulez un README
4. Cliquer sur **"Create repository"**

### Lier un dépôt local à GitHub

```bash
# Si le dépôt GitHub est vide
git remote add origin https://github.com/user/repo.git
git branch -M main
git push -u origin main

# Si le dépôt GitHub a déjà des fichiers
git remote add origin https://github.com/user/repo.git
git branch -M main
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Interface GitHub

#### Onglets principaux

- **Code** : Fichiers du projet
- **Issues** : Problèmes et demandes de fonctionnalités
- **Pull Requests** : Demandes de fusion
- **Actions** : Automatisation CI/CD
- **Projects** : Gestion de projet
- **Wiki** : Documentation
- **Security** : Sécurité
- **Insights** : Statistiques

#### Actions rapides

- **⭐ Star** : Marquer comme favori
- **🍴 Fork** : Créer une copie dans votre compte
- **👁️ Watch** : Recevoir des notifications
- **📋 Clone** : Copier l'URL du dépôt

---

## 7. Travail avec les Branches

### Pourquoi utiliser des branches ?

Les branches permettent de :
- Développer des fonctionnalités isolément
- Tester sans affecter le code principal
- Collaborer sans conflits
- Organiser le travail

### Créer et utiliser des branches

```bash
# Créer une nouvelle branche
git branch nom-de-la-branche

# Se déplacer sur une branche
git checkout nom-de-la-branche

# Créer et se déplacer en une commande
git checkout -b nom-de-la-branche

# Nouvelle syntaxe (Git 2.23+)
git switch -c nom-de-la-branche

# Voir toutes les branches
git branch

# Voir les branches distantes
git branch -r

# Voir toutes les branches (locales et distantes)
git branch -a

# Supprimer une branche locale
git branch -d nom-de-la-branche

# Supprimer une branche distante
git push origin --delete nom-de-la-branche
```

### Fusionner des branches

```bash
# Se placer sur la branche de destination (ex: main)
git checkout main

# Fusionner une branche
git merge nom-de-la-branche

# Fusionner avec un message
git merge nom-de-la-branche -m "Fusion de la fonctionnalité X"

# Supprimer la branche après fusion
git branch -d nom-de-la-branche
```

### Types de fusion

#### Fast-forward merge

Quand la branche à fusionner est directement en avance :

```
main:    A---B
              \
feature:       C---D
```

Après fusion :
```
main:    A---B---C---D
```

#### Merge commit

Quand les deux branches ont divergé :

```
main:    A---B---E
              \
feature:       C---D
```

Après fusion :
```
main:    A---B---E---M
              \     /
feature:       C---D
```

### Rebase (alternative au merge)

```bash
# Rebase interactif
git rebase -i main

# Rebase simple
git checkout feature
git rebase main
```

**Différence** :
- **Merge** : Crée un commit de fusion, préserve l'historique
- **Rebase** : Réécrit l'historique, linéaire mais peut être dangereux

---

## 8. Collaboration sur GitHub

### Fork (Fourche)

Un **fork** est une copie d'un dépôt dans votre compte GitHub.

**Utilisation** :
1. Forker un projet open source
2. Cloner votre fork
3. Faire des modifications
4. Pousser vers votre fork
5. Créer une Pull Request vers le projet original

### Clone vs Fork

- **Clone** : Copie locale d'un dépôt
- **Fork** : Copie sur GitHub dans votre compte

### Collaborateurs

#### Ajouter un collaborateur

1. Aller dans **Settings** → **Collaborators**
2. Cliquer sur **"Add people"**
3. Entrer le nom d'utilisateur ou l'email
4. L'invitation sera envoyée

#### Permissions

- **Read** : Lecture seule
- **Write** : Lecture et écriture
- **Admin** : Accès complet

### Organisations

Les **organisations** permettent de gérer plusieurs dépôts et équipes.

**Fonctionnalités** :
- Gestion d'équipes
- Permissions granulaires
- Facturation centralisée
- Statistiques d'équipe

---

## 9. Pull Requests

### Qu'est-ce qu'une Pull Request (PR) ?

Une **Pull Request** est une demande de fusion de modifications d'une branche vers une autre.

### Créer une Pull Request

#### Depuis GitHub

1. Pousser votre branche :
```bash
git push -u origin ma-branche
```

2. Sur GitHub :
   - Cliquer sur **"Compare & pull request"**
   - Remplir le titre et la description
   - Ajouter des reviewers (optionnel)
   - Cliquer sur **"Create pull request"**

#### Depuis la ligne de commande

```bash
# GitHub CLI (si installé)
gh pr create --title "Titre" --body "Description"
```

### Structure d'une Pull Request

- **Titre** : Description courte et claire
- **Description** : Détails des modifications
- **Files changed** : Diff des modifications
- **Commits** : Liste des commits
- **Checks** : Tests automatisés
- **Reviews** : Commentaires et approbations

### Bonnes pratiques pour les PR

```markdown
## Description
Expliquez ce que fait cette PR et pourquoi.

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Refactoring
- [ ] Documentation

## Comment tester
1. Étape 1
2. Étape 2

## Checklist
- [ ] Code testé
- [ ] Documentation mise à jour
- [ ] Pas de warnings
```

### Review et Merge

#### Approuver une PR

1. Examiner le code dans l'onglet **"Files changed"**
2. Ajouter des commentaires si nécessaire
3. Cliquer sur **"Review changes"**
4. Choisir :
   - **Approve** : Approuver
   - **Request changes** : Demander des modifications
   - **Comment** : Commenter seulement

#### Fusionner une PR

Options de merge :
- **Create a merge commit** : Crée un commit de fusion
- **Squash and merge** : Combine tous les commits en un seul
- **Rebase and merge** : Réécrit l'historique de manière linéaire

### Fermer une PR

- **Merge** : Fusionne et ferme automatiquement
- **Close** : Ferme sans fusionner

---

## 10. Gestion des Conflits

### Qu'est-ce qu'un conflit ?

Un **conflit** survient quand Git ne peut pas fusionner automatiquement deux modifications sur la même partie d'un fichier.

### Quand surviennent les conflits ?

- Lors d'un `git merge`
- Lors d'un `git pull`
- Lors d'un `git rebase`

### Résoudre un conflit

#### 1. Identifier le conflit

```bash
git status
# Vous verrez : "both modified: fichier.txt"
```

#### 2. Ouvrir le fichier

Le fichier contiendra des marqueurs :

```python
<<<<<<< HEAD
# Code de la branche actuelle
print("Version actuelle")
=======
# Code de la branche à fusionner
print("Nouvelle version")
>>>>>>> nom-de-la-branche
```

#### 3. Résoudre manuellement

Choisir quelle version garder ou combiner :

```python
# Solution 1 : Garder la version actuelle
print("Version actuelle")

# Solution 2 : Garder la nouvelle version
print("Nouvelle version")

# Solution 3 : Combiner
print("Version actuelle")
print("Nouvelle version")
```

#### 4. Marquer comme résolu

```bash
# Après avoir modifié le fichier
git add fichier.txt

# Finaliser le merge
git commit
```

### Outils de résolution

- **VS Code** : Interface graphique intégrée
- **GitKraken** : Outil visuel
- **Meld** : Comparaison de fichiers
- **GitHub** : Résolution en ligne

### Prévenir les conflits

1. **Communiquer** avec l'équipe
2. **Puller régulièrement** : `git pull` avant de travailler
3. **Travailler sur des fichiers différents** quand possible
4. **Faire des commits fréquents**
5. **Utiliser des branches courtes** (fusionner rapidement)

---

## 11. Fichiers Spéciaux

### README.md

Le **README** est le premier fichier que les visiteurs voient.

**Exemple** :

```markdown
# Nom du Projet

Description courte du projet.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```python
python main.py
```

## Contribution

Les contributions sont les bienvenues !

## Licence

MIT
```

### .gitignore

Fichier qui indique à Git quels fichiers ignorer (voir section 5).

### LICENSE

Fichier de licence (MIT, Apache, GPL, etc.).

### CONTRIBUTING.md

Guide pour les contributeurs.

```markdown
# Comment contribuer

1. Fork le projet
2. Créer une branche
3. Faire vos modifications
4. Créer une Pull Request
```

### .github/

Dossier pour les configurations GitHub :

- **workflows/** : GitHub Actions
- **ISSUE_TEMPLATE/** : Templates d'issues
- **PULL_REQUEST_TEMPLATE.md** : Template de PR

---

## 12. Bonnes Pratiques

### Messages de commit

#### Format recommandé

```
type(scope): sujet court

Description détaillée (optionnel)

Corps du message (optionnel)
```

#### Types courants

- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage
- `refactor` : Refactoring
- `test` : Tests
- `chore` : Tâches de maintenance

#### Exemples

```bash
git commit -m "feat(auth): ajout de l'authentification OAuth"

git commit -m "fix(api): correction du bug de timeout"
git commit -m "Corrige le problème de timeout dans l'API"

git commit -m "docs: mise à jour du README"
```

### Fréquence des commits

- ✅ **Commits fréquents** : Petites modifications logiques
- ❌ **Éviter** : Un seul gros commit avec tout

### Nommage des branches

**Conventions** :

```
feature/nom-de-la-fonctionnalite
bugfix/description-du-bug
hotfix/description-urgente
refactor/nom-du-refactoring
docs/description
```

**Exemples** :
- `feature/user-authentication`
- `bugfix/login-error`
- `hotfix/security-patch`

### Workflow recommandé

```bash
# 1. Mettre à jour la branche principale
git checkout main
git pull origin main

# 2. Créer une nouvelle branche
git checkout -b feature/ma-fonctionnalite

# 3. Développer et commiter
git add .
git commit -m "feat: ajout de la fonctionnalité X"

# 4. Pousser la branche
git push -u origin feature/ma-fonctionnalite

# 5. Créer une Pull Request sur GitHub

# 6. Après fusion, nettoyer
git checkout main
git pull origin main
git branch -d feature/ma-fonctionnalite
```

### Sécurité

- ❌ **Ne jamais commiter** :
  - Mots de passe
  - Clés API
  - Fichiers `.env` avec secrets
  - Clés privées

- ✅ **Utiliser** :
  - Variables d'environnement
  - Fichiers `.env` (dans `.gitignore`)
  - Services de gestion de secrets (GitHub Secrets)

### Documentation

- Maintenir un README à jour
- Documenter le code (commentaires)
- Utiliser les Issues pour tracker les bugs
- Écrire des messages de commit clairs

---

## 13. Workflows Avancés

### GitHub Flow

Workflow simple pour les petits projets :

1. Créer une branche depuis `main`
2. Faire des commits
3. Ouvrir une Pull Request
4. Discuter et réviser
5. Fusionner dans `main`
6. Déployer

### Git Flow

Workflow avec branches de release :

```
main (production)
  │
  ├── develop (développement)
  │     │
  │     ├── feature/* (fonctionnalités)
  │     ├── release/* (préparation release)
  │     └── hotfix/* (corrections urgentes)
```

### GitHub Actions (CI/CD)

Automatisation des tâches :

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

### Tags et Releases

```bash
# Créer un tag
git tag v1.0.0
git push origin v1.0.0

# Tag annoté (recommandé)
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0

# Voir les tags
git tag

# Créer une release sur GitHub
# GitHub → Releases → Draft a new release
```

### Stash (Mise de côté temporaire)

```bash
# Mettre de côté les modifications
git stash

# Voir les stashes
git stash list

# Récupérer les modifications
git stash pop

# Appliquer sans supprimer
git stash apply

# Supprimer un stash
git stash drop
```

### Cherry-pick

Appliquer un commit spécifique sur une autre branche :

```bash
# Sur la branche de destination
git cherry-pick <hash-du-commit>
```

### Submodules

Inclure un autre dépôt Git dans votre projet :

```bash
# Ajouter un submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Cloner un projet avec submodules
git clone --recursive https://github.com/user/repo.git

# Mettre à jour les submodules
git submodule update --remote
```

---

## Ressources et Aller Plus Loin

### Documentation officielle

- 📚 **Git** : [git-scm.com/doc](https://git-scm.com/doc)
- 🐙 **GitHub** : [docs.github.com](https://docs.github.com)
- 📖 **GitHub Guides** : [guides.github.com](https://guides.github.com)

### Outils utiles

- **GitKraken** : Interface graphique
- **SourceTree** : Client Git gratuit
- **GitHub Desktop** : Client officiel GitHub
- **VS Code** : Intégration Git excellente

### Commandes de référence rapide

```bash
# Configuration
git config --global user.name "Nom"
git config --global user.email "email@example.com"

# Dépôt
git init
git clone <url>
git remote add origin <url>

# Modifications
git status
git add <fichier>
git commit -m "Message"
git push
git pull

# Branches
git branch
git checkout -b <branche>
git merge <branche>

# Historique
git log
git log --oneline --graph --all
```

### Prochaines étapes

1. ✅ **Pratiquez** : Créez des projets et utilisez Git
2. ✅ **Contribuez** : Participez à des projets open source
3. ✅ **Apprenez** : Explorez les workflows avancés
4. ✅ **Automatisez** : Utilisez GitHub Actions
5. ✅ **Collaborez** : Travaillez en équipe sur GitHub

---

## Conclusion

Git et GitHub sont des outils essentiels pour tout développeur. Ce cours couvre les **fondamentaux** :

- ✅ Concepts de base (commits, branches, remotes)
- ✅ Commandes essentielles
- ✅ Collaboration (Pull Requests, forks)
- ✅ Gestion des conflits
- ✅ Bonnes pratiques

**Pour progresser** :
- Pratiquez régulièrement
- Contribuez à des projets open source
- Explorez les fonctionnalités avancées
- Participez à la communauté

**Bon courage avec Git et GitHub ! 🐙✨**
