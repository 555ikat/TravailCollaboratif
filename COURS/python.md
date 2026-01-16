# 🐍 Cours Python - Les Bases

## Table des matières

1. [Introduction à Python](#1-introduction-à-python)
2. [Installation et Configuration](#2-installation-et-configuration)
3. [Premiers Pas](#3-premiers-pas)
4. [Types de Données](#4-types-de-données)
5. [Variables et Opérateurs](#5-variables-et-opérateurs)
6. [Structures de Contrôle](#6-structures-de-contrôle)
7. [Structures de Données](#7-structures-de-données)
8. [Fonctions](#8-fonctions)
9. [Modules et Packages](#9-modules-et-packages)
10. [Gestion des Fichiers](#10-gestion-des-fichiers)
11. [Gestion des Erreurs](#11-gestion-des-erreurs)
12. [Programmation Orientée Objet (Bases)](#12-programmation-orientée-objet-bases)
13. [Bonnes Pratiques](#13-bonnes-pratiques)

---

## 1. Introduction à Python

### Qu'est-ce que Python ?

Python est un langage de programmation **interprété**, **haut niveau** et **polyvalent**. Créé par Guido van Rossum en 1991, il est aujourd'hui l'un des langages les plus populaires au monde.

### Caractéristiques principales

- ✅ **Syntaxe simple et lisible** : Le code Python se lit presque comme de l'anglais
- ✅ **Multi-paradigme** : Supporte la programmation procédurale, orientée objet et fonctionnelle
- ✅ **Bibliothèque standard riche** : Nombreuses fonctionnalités intégrées
- ✅ **Communauté active** : Large écosystème de packages (PyPI)
- ✅ **Multi-plateforme** : Fonctionne sur Windows, macOS, Linux

### Domaines d'application

- 🌐 **Développement web** : Django, Flask, FastAPI
- 📊 **Data Science** : NumPy, Pandas, Matplotlib
- 🤖 **Intelligence Artificielle** : TensorFlow, PyTorch, scikit-learn
- 🔧 **Automatisation** : Scripts système, DevOps
- 🎮 **Développement de jeux** : Pygame
- 📱 **Applications desktop** : Tkinter, PyQt

---

## 2. Installation et Configuration

### Installation

#### Sur Windows
1. Télécharger Python depuis [python.org](https://www.python.org/downloads/)
2. Cocher "Add Python to PATH" lors de l'installation
3. Vérifier : `python --version`

#### Sur macOS
```bash
# Python est souvent pré-installé
python3 --version

# Ou installer via Homebrew
brew install python3
```

#### Sur Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Vérifier
python3 --version
```

### Éditeurs de code recommandés

- **VS Code** : Éditeur gratuit avec extensions Python
- **PyCharm** : IDE complet (version Community gratuite)
- **Jupyter Notebook** : Idéal pour la data science
- **Sublime Text** : Léger et rapide

### Premier programme

Créer un fichier `hello.py` :

```python
print("Hello, World!")
```

Exécuter :
```bash
python hello.py
# ou
python3 hello.py
```

---

## 3. Premiers Pas

### La fonction `print()`

Affiche du texte à l'écran :

```python
print("Bonjour le monde")
print(42)
print("Python", "est", "génial")  # Plusieurs arguments
print("Ligne 1", end=" ")  # Pas de retour à la ligne
print("Ligne 2")
```

### Les commentaires

```python
# Ceci est un commentaire sur une ligne

"""
Ceci est un commentaire
sur plusieurs lignes
(chaîne de documentation)
"""

# Les commentaires permettent d'expliquer le code
age = 25  # L'âge de l'utilisateur
```

### L'indentation

**Important** : En Python, l'indentation est **obligatoire** et a une signification syntaxique.

```python
if True:
    print("Ceci est indenté")  # 4 espaces (ou 1 tab)
    print("Toujours indenté")
print("Ceci n'est pas dans le if")
```

⚠️ **Règle** : Utilisez 4 espaces (recommandé) ou des tabulations, mais pas les deux mélangés.

### Lire les entrées utilisateur

```python
nom = input("Quel est votre nom ? ")
print(f"Bonjour, {nom}!")

# Conversion de type
age = int(input("Quel âge avez-vous ? "))
print(f"Vous avez {age} ans")
```

---

## 4. Types de Données

### Types numériques

#### Entiers (`int`)

```python
x = 42
y = -10
z = 0
print(type(x))  # <class 'int'>
```

#### Nombres décimaux (`float`)

```python
pi = 3.14159
temperature = -5.5
print(type(pi))  # <class 'float'>
```

#### Nombres complexes (`complex`)

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

### Chaînes de caractères (`str`)

```python
# Déclaration
nom = "Alice"
prenom = 'Bob'
phrase = """Ceci est une
chaîne sur plusieurs lignes"""

# Concaténation
full_name = nom + " " + prenom

# Formatage (f-strings - Python 3.6+)
age = 25
message = f"Je m'appelle {nom} et j'ai {age} ans"

# Méthodes courantes
texte = "  Hello World  "
print(texte.upper())      # "  HELLO WORLD  "
print(texte.lower())      # "  hello world  "
print(texte.strip())      # "Hello World"
print(texte.replace("World", "Python"))
print(len(texte))         # Longueur
```

### Booléens (`bool`)

```python
est_vrai = True
est_faux = False

# Résultats de comparaisons
resultat = 5 > 3  # True
print(type(resultat))  # <class 'bool'>
```

### Conversion de types

```python
# Conversion explicite
x = int("42")        # "42" → 42
y = float("3.14")    # "3.14" → 3.14
z = str(100)         # 100 → "100"
b = bool(1)          # 1 → True

# Vérifier le type
age = 25
print(isinstance(age, int))  # True
```

---

## 5. Variables et Opérateurs

### Déclaration de variables

```python
# Pas besoin de déclarer le type
nom = "Alice"
age = 25
taille = 1.65
est_etudiant = True

# Affectation multiple
x, y, z = 1, 2, 3
a = b = c = 0

# Échanger deux variables
x, y = y, x
```

### Règles de nommage

- ✅ Commence par une lettre ou `_`
- ✅ Peut contenir lettres, chiffres et `_`
- ✅ Sensible à la casse (`age` ≠ `Age`)
- ✅ Ne peut pas être un mot-clé Python

```python
# Bon
nom_utilisateur = "Alice"
_age = 25
total123 = 100

# Mauvais
2nom = "Alice"      # Ne commence pas par une lettre
nom-utilisateur = "Alice"  # Caractère invalide
if = 5              # Mot-clé réservé
```

### Opérateurs arithmétiques

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7  (soustraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division)
print(a // b)  # 3  (division entière)
print(a % b)   # 1  (modulo - reste)
print(a ** b)  # 1000 (puissance)

# Opérateurs d'affectation
x = 5
x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 2   # x = x * 2 → 12
x /= 3   # x = x / 3 → 4.0
```

### Opérateurs de comparaison

```python
a = 5
b = 3

print(a == b)  # False (égal)
print(a != b)  # True  (différent)
print(a < b)   # False (inférieur)
print(a > b)   # True  (supérieur)
print(a <= b)  # False (inférieur ou égal)
print(a >= b)  # True  (supérieur ou égal)
```

### Opérateurs logiques

```python
x = True
y = False

print(x and y)  # False (ET)
print(x or y)   # True  (OU)
print(not x)    # False (NON)

# Exemples pratiques
age = 20
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Étudiant majeur")
```

### Opérateurs d'appartenance

```python
liste = [1, 2, 3, 4, 5]

print(3 in liste)      # True
print(10 not in liste) # True

texte = "Python"
print("Py" in texte)    # True
```

---

## 6. Structures de Contrôle

### Condition `if / elif / else`

```python
age = 20

if age < 18:
    print("Mineur")
elif age < 65:
    print("Adulte")
else:
    print("Senior")

# Condition ternaire
statut = "Majeur" if age >= 18 else "Mineur"
```

### Boucle `while`

```python
# Boucle avec condition
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# Boucle infinie avec break
while True:
    reponse = input("Tapez 'quit' pour sortir: ")
    if reponse == "quit":
        break
    print(f"Vous avez tapé: {reponse}")

# Utiliser continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Passe à l'itération suivante
    print(i)  # Affiche seulement les impairs
```

### Boucle `for`

```python
# Parcourir une séquence
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Avec début et fin
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# Avec pas
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Parcourir une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Avec index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Parcourir une chaîne
for lettre in "Python":
    print(lettre)
```

### `break` et `continue`

```python
# break : sort de la boucle
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue : passe à l'itération suivante
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9
```

### `else` avec les boucles

```python
# else s'exécute si la boucle se termine normalement (sans break)
for i in range(5):
    print(i)
else:
    print("Boucle terminée normalement")
```

---

## 7. Structures de Données

### Listes (`list`)

Les listes sont **mutables** (modifiables) et ordonnées.

```python
# Création
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = [1, "deux", 3.0, True]

# Accès
print(fruits[0])      # "pomme" (premier élément)
print(fruits[-1])     # "orange" (dernier élément)

# Modification
fruits[1] = "cerise"

# Ajout
fruits.append("kiwi")           # À la fin
fruits.insert(1, "mangue")      # À une position

# Suppression
fruits.remove("banane")         # Par valeur
del fruits[0]                   # Par index
fruits.pop()                    # Dernier élément
fruits.pop(1)                   # Par index

# Opérations
print(len(fruits))              # Longueur
print("pomme" in fruits)        # Vérifier présence
fruits.sort()                   # Trier
fruits.reverse()                # Inverser
nouvelle_liste = fruits.copy()  # Copie

# Slicing (tranches)
nombres = [0, 1, 2, 3, 4, 5]
print(nombres[1:4])    # [1, 2, 3]
print(nombres[:3])     # [0, 1, 2]
print(nombres[3:])     # [3, 4, 5]
print(nombres[::2])    # [0, 2, 4] (pas de 2)
```

### Tuples (`tuple`)

Les tuples sont **immuables** (non modifiables) et ordonnés.

```python
# Création
point = (10, 20)
coordonnees = (1, 2, 3)

# Accès
print(point[0])  # 10

# Déballage (unpacking)
x, y = point

# Utilisation
# - Retourner plusieurs valeurs d'une fonction
# - Clés de dictionnaires
# - Données qui ne doivent pas changer
```

### Dictionnaires (`dict`)

Stockent des paires **clé-valeur**.

```python
# Création
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès
print(personne["nom"])           # "Alice"
print(personne.get("age"))        # 25
print(personne.get("email", "N/A"))  # "N/A" (valeur par défaut)

# Modification
personne["age"] = 26
personne["email"] = "alice@example.com"

# Suppression
del personne["ville"]
email = personne.pop("email")

# Méthodes
print(personne.keys())      # Toutes les clés
print(personne.values())    # Toutes les valeurs
print(personne.items())     # Toutes les paires

# Parcourir
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

### Sets (`set`)

Collections **non ordonnées** d'éléments **uniques**.

```python
# Création
fruits = {"pomme", "banane", "orange"}
nombres = {1, 2, 3, 4, 5}

# Ajout
fruits.add("kiwi")

# Suppression
fruits.remove("banane")     # Erreur si n'existe pas
fruits.discard("cerise")    # Pas d'erreur si n'existe pas

# Opérations ensemblistes
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union: {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Différence: {1, 2}
print(a ^ b)   # Différence symétrique: {1, 2, 4, 5}
```

### Listes en compréhension

Syntaxe concise pour créer des listes.

```python
# Syntaxe de base
nombres = [x for x in range(10)]
carres = [x**2 for x in range(10)]

# Avec condition
pairs = [x for x in range(20) if x % 2 == 0]

# Exemple pratique
mots = ["python", "java", "c++", "javascript"]
longueurs = [len(mot) for mot in mots]

# Dictionnaires en compréhension
carres_dict = {x: x**2 for x in range(5)}
```

---

## 8. Fonctions

### Définition de fonction

```python
def dire_bonjour():
    print("Bonjour!")

dire_bonjour()
```

### Fonctions avec paramètres

```python
def saluer(nom):
    print(f"Bonjour, {nom}!")

saluer("Alice")

# Paramètres par défaut
def saluer(nom, langage="fr"):
    if langage == "fr":
        print(f"Bonjour, {nom}!")
    elif langage == "en":
        print(f"Hello, {nom}!")

saluer("Alice")
saluer("Bob", "en")

# Arguments nommés
saluer(langage="en", nom="Charlie")
```

### Retour de valeurs

```python
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)  # 8

# Retourner plusieurs valeurs
def diviser(a, b):
    quotient = a // b
    reste = a % b
    return quotient, reste

q, r = diviser(10, 3)
```

### Arguments variables

```python
# *args : arguments positionnels variables
def somme(*args):
    total = 0
    for nombre in args:
        total += nombre
    return total

print(somme(1, 2, 3, 4, 5))  # 15

# **kwargs : arguments nommés variables
def afficher_info(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

afficher_info(nom="Alice", age=25, ville="Paris")
```

### Portée des variables

```python
# Variable globale
x = 10

def fonction():
    # Variable locale
    y = 20
    print(x)  # Peut accéder à x
    print(y)

# Modifier une variable globale
def modifier_globale():
    global x
    x = 30

modifier_globale()
print(x)  # 30
```

### Fonctions lambda

Fonctions anonymes courtes.

```python
# Syntaxe
carre = lambda x: x ** 2
print(carre(5))  # 25

# Utilisation avec map, filter
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
pairs = list(filter(lambda x: x % 2 == 0, nombres))
```

### Documentation de fonctions

```python
def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    
    Args:
        nombres: Liste de nombres
        
    Returns:
        float: La moyenne des nombres
    """
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)

# Accéder à la documentation
help(calculer_moyenne)
```

---

## 9. Modules et Packages

### Importer un module

```python
# Import complet
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.14159...

# Import avec alias
import math as m
print(m.sqrt(25))

# Import sélectif
from math import sqrt, pi
print(sqrt(36))
print(pi)

# Import de tout (non recommandé)
from math import *
```

### Modules de la bibliothèque standard

```python
# math : fonctions mathématiques
import math
print(math.sqrt(16))
print(math.sin(math.pi/2))

# random : nombres aléatoires
import random
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

# datetime : dates et heures
from datetime import datetime, date
maintenant = datetime.now()
print(maintenant.strftime("%Y-%m-%d %H:%M:%S"))

# os : interaction avec le système
import os
print(os.getcwd())  # Répertoire courant
print(os.listdir("."))  # Liste des fichiers

# sys : paramètres système
import sys
print(sys.version)
print(sys.argv)  # Arguments de la ligne de commande
```

### Créer son propre module

Créer un fichier `mon_module.py` :

```python
# mon_module.py
def saluer(nom):
    return f"Bonjour, {nom}!"

PI = 3.14159
```

Utiliser dans un autre fichier :

```python
import mon_module
print(mon_module.saluer("Alice"))
print(mon_module.PI)
```

### Packages

Un package est un dossier contenant plusieurs modules.

```
mon_package/
    __init__.py
    module1.py
    module2.py
```

```python
# Utilisation
from mon_package import module1
import mon_package.module2
```

---

## 10. Gestion des Fichiers

### Ouvrir et fermer un fichier

```python
# Méthode classique
fichier = open("fichier.txt", "r")
contenu = fichier.read()
fichier.close()

# Méthode recommandée (fermeture automatique)
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()
# Le fichier est automatiquement fermé ici
```

### Modes d'ouverture

- `"r"` : Lecture (read)
- `"w"` : Écriture (écrase le fichier)
- `"a"` : Ajout (append)
- `"x"` : Création (erreur si existe)
- `"b"` : Mode binaire
- `"t"` : Mode texte (défaut)

### Lire un fichier

```python
# Lire tout le fichier
with open("fichier.txt", "r") as f:
    contenu = f.read()

# Lire ligne par ligne
with open("fichier.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())  # strip() enlève \n

# Lire toutes les lignes dans une liste
with open("fichier.txt", "r") as f:
    lignes = f.readlines()
```

### Écrire dans un fichier

```python
# Écrire (écrase le contenu)
with open("fichier.txt", "w") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")

# Ajouter à la fin
with open("fichier.txt", "a") as f:
    f.write("Nouvelle ligne\n")
```

### Fichiers JSON

```python
import json

# Écrire
donnees = {"nom": "Alice", "age": 25}
with open("donnees.json", "w") as f:
    json.dump(donnees, f)

# Lire
with open("donnees.json", "r") as f:
    donnees = json.load(f)
    print(donnees["nom"])
```

---

## 11. Gestion des Erreurs

### `try / except`

```python
try:
    nombre = int(input("Entrez un nombre: "))
    resultat = 10 / nombre
    print(f"Résultat: {resultat}")
except ValueError:
    print("Ce n'est pas un nombre valide!")
except ZeroDivisionError:
    print("Division par zéro impossible!")
except Exception as e:
    print(f"Erreur: {e}")
```

### `else` et `finally`

```python
try:
    fichier = open("fichier.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier introuvable")
else:
    print("Fichier lu avec succès")
    print(contenu)
finally:
    print("Cette partie s'exécute toujours")
    fichier.close()
```

### Lever une exception

```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible!")
    return a / b

try:
    resultat = diviser(10, 0)
except ValueError as e:
    print(e)
```

### Types d'exceptions courantes

- `ValueError` : Valeur incorrecte
- `TypeError` : Type incorrect
- `IndexError` : Index hors limites
- `KeyError` : Clé absente du dictionnaire
- `FileNotFoundError` : Fichier introuvable
- `ZeroDivisionError` : Division par zéro

---

## 12. Programmation Orientée Objet (Bases)

### Classe et objet

```python
class Personne:
    # Constructeur
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    # Méthode
    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

# Créer un objet
alice = Personne("Alice", 25)
print(alice.se_presenter())
print(alice.nom)
```

### Attributs et méthodes

```python
class Voiture:
    # Attribut de classe
    nombre_voitures = 0
    
    def __init__(self, marque, modele):
        # Attributs d'instance
        self.marque = marque
        self.modele = modele
        self.kilometrage = 0
        Voiture.nombre_voitures += 1
    
    def rouler(self, km):
        self.kilometrage += km
        print(f"La voiture a roulé {km} km")
    
    def afficher_info(self):
        return f"{self.marque} {self.modele} - {self.kilometrage} km"

voiture1 = Voiture("Toyota", "Corolla")
voiture1.rouler(100)
print(voiture1.afficher_info())
```

### Héritage

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom
    
    def parler(self):
        return "L'animal fait un bruit"

class Chien(Animal):
    def parler(self):
        return f"{self.nom} aboie: Wouf!"

class Chat(Animal):
    def parler(self):
        return f"{self.nom} miaule: Miaou!"

chien = Chien("Rex")
chat = Chat("Mimi")
print(chien.parler())
print(chat.parler())
```

### Encapsulation

```python
class CompteBancaire:
    def __init__(self, solde_initial):
        self.__solde = solde_initial  # Privé (__)
    
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
    
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Solde insuffisant")
    
    def get_solde(self):
        return self.__solde

compte = CompteBancaire(1000)
compte.deposer(500)
print(compte.get_solde())
```

---

## 13. Bonnes Pratiques

### Style de code (PEP 8)

```python
# ✅ Noms de variables en snake_case
nom_utilisateur = "Alice"
age_utilisateur = 25

# ✅ Noms de classes en PascalCase
class Utilisateur:
    pass

# ✅ Constantes en MAJUSCULES
PI = 3.14159
MAX_CONNEXIONS = 100

# ✅ Indentation : 4 espaces
if condition:
    faire_quelque_chose()

# ✅ Lignes de max 79 caractères (recommandé)
# ✅ Espaces autour des opérateurs
x = 5 + 3
```

### Documentation

```python
def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    
    Args:
        nombres (list): Liste de nombres
        
    Returns:
        float: La moyenne, ou 0 si la liste est vide
        
    Raises:
        TypeError: Si nombres n'est pas une liste
    """
    if not isinstance(nombres, list):
        raise TypeError("nombres doit être une liste")
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)
```

### Gestion des erreurs

```python
# ✅ Spécifier les exceptions
try:
    resultat = operation_risquee()
except ValueError as e:
    logger.error(f"Erreur de valeur: {e}")
except FileNotFoundError:
    logger.error("Fichier introuvable")
except Exception as e:
    logger.error(f"Erreur inattendue: {e}")

# ❌ Éviter except: sans spécification
```

### Tests

```python
# Exemple simple de test
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    print("Tests réussis!")

# Utiliser unittest ou pytest pour des tests plus avancés
```

### Ressources pour aller plus loin

- 📚 **Documentation officielle** : [docs.python.org](https://docs.python.org/fr/)
- 🎓 **Tutoriels** : [python.org/tutorial](https://docs.python.org/fr/3/tutorial/)
- 📦 **Packages** : [pypi.org](https://pypi.org/)
- 💡 **PEP 8** : Guide de style Python
- 🐍 **Communauté** : Stack Overflow, Reddit r/learnpython

---

## Conclusion

Ce cours couvre les **fondamentaux de Python**. Pour progresser :

1. ✅ **Pratiquez régulièrement** : Écrivez du code tous les jours
2. ✅ **Lisez du code** : Explorez des projets open source
3. ✅ **Construisez des projets** : Créez des applications concrètes
4. ✅ **Participez à la communauté** : Posez des questions, aidez les autres

**Bon courage dans votre apprentissage de Python ! 🐍✨**
