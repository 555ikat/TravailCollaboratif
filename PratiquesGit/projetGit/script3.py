
# =============================================================================
# Python : les données
# =============================================================================
# Une variable est une donnée temporaire que l'on stocke dans une case de la 
# mémoire (registre, RAM).
#
A
# =============================================================================
# Python : les scripts et structures de contrôle
# =============================================================================
# 
# SCRIPT
# ------
Afficher plus
script_et_structures.py
15 Ko
﻿
# =============================================================================
# Python : les scripts et structures de contrôle
# =============================================================================
# 
# SCRIPT
# ------
# Pour réutiliser les lignes d'instructions saisies en console, il faut les
# sauvegarder dans un fichier dont l'extension est .py pour être reconnu.
# Ce fichier peut être ouvert avec des éditeurs de texte (Notepad, gedit, VS Code...)
#
# ATTENTION : Microsoft Word ou LibreOffice Writer ne sont PAS des éditeurs de texte !
# Ce sont des traitements de texte, inadaptés à l'écriture de programme.
# L'encodage risque de ne pas être interprété correctement par Python.
#
# Reading : https://pythonscript.readthedocs.io/introduction.html#scripts
# =============================================================================

# =============================================================================
# EXERCICE 1 : Premier Script
# =============================================================================
# Créez un fichier PremierScript.py avec le code suivant :

# Une ligne précédée par # est un commentaire
# Les commentaires sont ignorés par l'interpréteur Python
# Ils servent à documenter le code pour le programmeur

# voici votre premier script

# print() affiche un message à l'écran
# Ici on demande à l'utilisateur son nom
print('Quel est votre nom ?')

# input() attend que l'utilisateur tape du texte et appuie sur Entrée
# Le texte saisi est stocké dans la variable 'nom'
nom = input()

# On demande ensuite le prénom
print('Quel est votre prénom ?')

# On stocke le prénom saisi dans la variable 'prenom'
prenom = input()

# On demande le nombre de lignes déjà programmées
print('Combien de lignes python avez-vous déjà programmé ?')

# input() retourne toujours une chaîne de caractères (str)
# int() convertit cette chaîne en entier pour pouvoir faire des calculs
# Si l'utilisateur tape "10", input() retourne "10" (texte)
# int("10") convertit en 10 (nombre)
experience = int(input())

# \n dans une chaîne crée un retour à la ligne
# On concatène (+) plusieurs chaînes pour créer le message de bienvenue
print('\n Bonjour ' + prenom + ' ' + nom + ' et bienvenue dans ce cours python.')

# str() convertit un nombre en chaîne pour pouvoir le concaténer
# experience + 30 fait le calcul (ex: 10 + 30 = 40)
# str(40) convertit en "40" pour l'affichage
print('Après cette séance, vous aurez écrit un minimum de ' + str(experience + 30) + ' lignes python.')

# Pour exécuter ce script :
# 1. Ouvrez un terminal (cmd sous Windows, terminal sous Linux)
# 2. Naviguez vers le dossier contenant le fichier : cd chemin/vers/dossier
# 3. Lancez : python PremierScript.py

# =============================================================================
# LES STRUCTURES DE CONTRÔLE
# =============================================================================
# Les structures de contrôle permettent de :
# - Tester une condition avant d'exécuter une instruction (if)
# - Répéter des instructions (boucles for, while)
# =============================================================================

# =============================================================================
# STRUCTURES CONDITIONNELLES - IF (si alors)
# =============================================================================
# Si on veut exécuter un bloc d'instructions seulement sous certaines conditions,
# on utilise une structure conditionnelle (if).
#
# Une condition est une expression booléenne (vraie ou fausse).
# Il s'agit souvent d'une comparaison entre variables et/ou valeurs.
#
# Opérateurs de comparaison :
# - == : égalité (est égal à)
# - != : inégalité (est différent de)
# - <, >, <=, >= : comparaisons numériques
#
# Syntaxe :
# - Le mot réservé 'if' précède la condition
# - La condition est suivie de ':' (deux-points)
# - Les instructions concernées sont INDENTÉES (décalées de 4 espaces)

# On affecte -9 à la variable a
a = -9

# On affiche la valeur de a
# str(a) convertit l'entier en chaîne pour la concaténation
print('a=' + str(a))

# Test conditionnel : on vérifie si a est pair
# a % 2 calcule le reste de la division de a par 2 (modulo)
# Si le reste est 0, le nombre est pair
# == compare si le résultat est égal à 0
if a % 2 == 0:
    # Ce bloc est exécuté SEULEMENT si la condition est vraie
    # Ici, -9 % 2 = -1 (pas 0), donc ce bloc ne s'exécute PAS
    print(f"{a} est un nombre pair")

# On change la valeur de a pour tester avec un nombre pair
a = -10

print('a=' + str(a))

# Même test avec a = -10
# -10 % 2 = 0, donc la condition est vraie
if a % 2 == 0:
    # Ce bloc S'EXÉCUTE car -10 est pair
    # Résultat affiché : -10 est un nombre pair
    print(f"{a} est un nombre pair")

# =============================================================================
# STRUCTURES CONDITIONNELLES - IF ELSE (si alors sinon)
# =============================================================================
# Dans le cas où la condition n'est pas vraie et qu'on souhaite exécuter
# un autre bloc d'instructions, on ajoute une alternative avec 'else'.
#
# Syntaxe :
# - 'else' doit être au même niveau d'indentation que le 'if'
# - 'else' est suivi de ':' (deux-points)
# - Le bloc else est indenté

# On importe le module random pour générer des nombres aléatoires
# Un module est une bibliothèque de fonctions prêtes à l'emploi
import random

# random.randint(a, b) génère un entier aléatoire entre a et b inclus
# Ici, on génère un nombre entre 0 et 100
x = random.randint(0, 100)

# Test de parité avec alternative
if x % 2 == 0:
    # Bloc exécuté si x est PAIR (condition vraie)
    print('x=' + str(x))
    print('x est pair')
else:
    # Bloc exécuté si x est IMPAIR (condition fausse)
    # 'else' capture tous les cas où la condition if n'est pas vraie
    print('x=' + str(x))
    print('x est impair')

# =============================================================================
# EXERCICE 2 : Script de parité
# =============================================================================
# (1) Créer un fichier scriptPair.py avec le code ci-dessus
# (2) Modifier pour demander à l'utilisateur de saisir un nombre :
#
# print("Entrez un nombre entier :")
# x = int(input())
# if x % 2 == 0:
#     print(f"{x} est pair")
# else:
#     print(f"{x} est impair")

# =============================================================================
# EXERCICE 3 : Comptage de 'e'
# =============================================================================
# Compter le nombre de 'e' dans une chaîne saisie par l'utilisateur

print("\n--- EXERCICE 3 : Comptage de 'e' ---")
print("Entrez une chaîne de caractères :")

# On lit la chaîne saisie par l'utilisateur
chaine = input()

# count() compte le nombre d'occurrences d'un caractère dans une chaîne
nombre_e = chaine.count('e')

# On affiche un message différent selon le résultat
if nombre_e == 0:
    # Cas où aucun 'e' n'a été trouvé
    print("Aucun 'e' n'a été saisi dans votre chaîne.")
else:
    # Cas où au moins un 'e' a été trouvé
    print(f"Vous avez saisi {nombre_e} 'e' dans votre chaîne.")

# =============================================================================
# LES BOUCLES - RÉPÉTITIONS
# =============================================================================
# Pour éviter de répéter des lignes d'instructions correspondant à la même action,
# on utilise des boucles.
# Imaginez devoir tester toutes les lettres de l'alphabet une par une !
# =============================================================================

# =============================================================================
# BOUCLE FOR
# =============================================================================
# La boucle for permet de répéter un bloc d'instructions un nombre de fois SPÉCIFIÉ.
# Elle itère sur une séquence (liste, range, chaîne...).
#
# Syntaxe :
# for variable in séquence:
#     instructions à répéter

print("\n--- BOUCLE FOR : Test des 10 premiers chiffres ---")

# range(10) génère les entiers de 0 à 9 (10 valeurs, mais 10 est EXCLU)
# À chaque tour de boucle, x prend la valeur suivante : 0, 1, 2, ..., 9
for x in range(10):
    # Ce bloc est exécuté 10 fois, une fois pour chaque valeur de x
    if x % 2 == 0:
        # Si x est pair
        print(f'x={x} est pair')
    else:
        # Si x est impair
        print(f'x={x} est impair')

# =============================================================================
# LA FONCTION RANGE
# =============================================================================
# range() permet d'itérer sur une gamme de valeurs entières.
#
# Syntaxes :
# - range(fin) : de 0 à fin-1
# - range(debut, fin) : de debut à fin-1
# - range(debut, fin, pas) : de debut à fin-1 avec un pas
#
# Pour voir le contenu d'un range, il faut le convertir en liste : list(range(...))

print("\n--- FONCTION RANGE avec pas ---")

# range(1, 20, 3) génère : 1, 4, 7, 10, 13, 16, 19
# Commence à 1, s'arrête avant 20, avance de 3 en 3
listeEntiers = list(range(1, 20, 3))

# On affiche la liste pour voir son contenu
print(f"Liste générée par range(1, 20, 3) : {listeEntiers}")

# On parcourt cette liste avec une boucle for
for x in listeEntiers:
    if x % 2 == 0:
        print(f'x={x} est pair')
    else:
        print(f'x={x} est impair')

# =============================================================================
# EXERCICE 3bis : Comptage des voyelles
# =============================================================================
# Étendre l'exercice 3 au comptage et affichage de chaque voyelle

print("\n--- EXERCICE 3bis : Comptage des voyelles ---")
print("Entrez une chaîne de caractères :")

chaine = input()

# On définit la liste des voyelles à compter
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

# On parcourt chaque voyelle avec une boucle for
for voyelle in voyelles:
    # count() compte les occurrences de chaque voyelle
    nombre = chaine.count(voyelle)
    
    # On affiche le résultat pour chaque voyelle
    if nombre == 0:
        print(f"Aucun '{voyelle}' trouvé.")
    else:
        print(f"'{voyelle}' apparaît {nombre} fois.")

# =============================================================================
# BOUCLE WHILE (tant que)
# =============================================================================
# La boucle while répète un bloc d'instructions TANT QUE la condition est vraie.
# Elle s'arrête quand la condition devient fausse.
#
# ATTENTION : Si la condition ne devient jamais fausse, la boucle est INFINIE !
#
# Syntaxe :
# while condition:
#     instructions à répéter

print("\n--- BOUCLE WHILE : Génération de nombres pairs ---")

# On réimporte random (déjà importé plus haut, mais par sécurité)
import random

# Nombre maximal de nombres pairs à trouver
Nbmax = 10

# Compteur de nombres pairs trouvés (commence à 0)
compteur = 0

# Liste vide pour stocker les nombres pairs trouvés
liste = []

# Compteur de passages dans la boucle (pour statistiques)
passage = 0

# La boucle continue TANT QUE compteur < Nbmax
# Dès que compteur atteint 10, la condition devient fausse et on sort
while compteur < Nbmax:
    # Génère un nombre aléatoire entre 0 et 1000
    x = random.randint(0, 1000)
    
    # Vérifie si le nombre est pair
    if x % 2 == 0:
        # Si pair, on l'ajoute à la liste
        liste = liste + [x]
        # On incrémente le compteur de nombres pairs
        compteur = compteur + 1
    
    # On compte chaque passage dans la boucle (pair ou impair)
    passage = passage + 1

# Affichage des résultats après la boucle
print(f"Il a fallu {passage} passages dans la boucle pour obtenir {Nbmax} nombres pairs")
print(f"liste = {liste}")

# =============================================================================
# EXERCICE 4 : Amélioration du code précédent
# =============================================================================

print("\n--- EXERCICE 4 (v1) : Saisie du nombre maximal ---")
print("Combien de nombres pairs voulez-vous générer ?")

# L'utilisateur saisit le nombre maximal
Nbmax_user = int(input())

# On réinitialise les variables
compteur = 0
liste = []
passage = 0

# Même boucle mais avec Nbmax_user
while compteur < Nbmax_user:
    x = random.randint(0, 1000)
    if x % 2 == 0:
        liste = liste + [x]
        compteur = compteur + 1
    passage = passage + 1

print(f"Il a fallu {passage} passages pour obtenir {Nbmax_user} nombres pairs")
print(f"liste = {liste}")

# -----------------------------------------------------------------------------
# EXERCICE 4 (v2) : Tri de la liste sans fonction particulière
# -----------------------------------------------------------------------------
# Algorithme de tri par insertion : on insère chaque élément à sa bonne place

print("\n--- EXERCICE 4 (v2) : Tri manuel (tri par insertion) ---")

# On copie la liste pour ne pas modifier l'originale
liste_triee = liste.copy()

# Parcours de chaque élément à partir du 2ème (indice 1)
for i in range(1, len(liste_triee)):
    # Élément courant à insérer à sa place
    cle = liste_triee[i]
    # Position de comparaison (élément précédent)
    j = i - 1
    
    # Tant qu'on n'est pas au début ET que l'élément précédent est plus grand
    while j >= 0 and liste_triee[j] > cle:
        # On décale l'élément vers la droite
        liste_triee[j + 1] = liste_triee[j]
        # On recule d'une position
        j = j - 1
    
    # On insère l'élément à sa bonne place
    liste_triee[j + 1] = cle

print(f"Liste triée manuellement : {liste_triee}")

# -----------------------------------------------------------------------------
# EXERCICE 4 (v3) : Tri avec numpy
# -----------------------------------------------------------------------------

print("\n--- EXERCICE 4 (v3) : Tri avec numpy ---")

# On importe le module numpy
# numpy est une bibliothèque puissante pour le calcul numérique
import numpy as np

# np.sort() trie un tableau et retourne une copie triée
liste_triee_numpy = np.sort(liste)

print(f"Liste triée avec numpy : {liste_triee_numpy}")

# Alternative : la méthode sort() de Python modifie la liste sur place
liste_copie = liste.copy()
liste_copie.sort()
print(f"Liste triée avec sort() de Python : {liste_copie}")
script_et_structures.py
15 Ko