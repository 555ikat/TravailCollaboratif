# =============================================================================
# Python : les données
# =============================================================================
# Une variable est une donnée temporaire que l'on stocke dans une case de la 
# mémoire (registre, RAM).
#
# On dit qu'elle est "variable" car c'est une valeur qui peut changer pendant 
# le déroulement du programme.
#
# Une variable est constituée de 2 choses :
# * Elle a une valeur : c'est la donnée qu'elle stocke (par exemple le nombre 5).
# * Elle a un nom : c'est ce qui permet de la reconnaître.
#
# Les variables peuvent contenir des types de données différents et leur type 
# peut évoluer au fil des instructions : Python est un langage à typage dynamique.
#
# L'opérateur = permet d'affecter une valeur à une variable.
#
# Consigne pour le nom de la variable :
# - Le nom de la variable doit être explicite sans être trop long à retaper
# - Il ne doit pas contenir d'espace ou de caractères accentués
# - Il ne doit pas commencer par un symbole ni chiffre
# - Certains mots sont réservés (nan, if, import, print...)
# - La casse doit être respectée (latitude ≠ Latitude)
# =============================================================================

# =============================================================================
# Les entiers (int)
# =============================================================================
# Le type int a pour valeurs les entiers positifs et négatifs
# Opérations arithmétiques : +, -, *, /
# Opérateurs classiques : division entière //, modulo %, puissance **
# Opérateurs de comparaison : <, >, ==, !=, <=, >= (renvoient True ou False)
#
# Fonctions utiles :
# - print() : fonction d'affichage
# - str() : convertit une donnée en string (chaîne de caractères)
# - type() : donne le type de la variable

# On crée une variable 'a' et on lui affecte la valeur entière 3
# Le signe = est l'opérateur d'affectation (pas d'égalité mathématique)
a = 3

# print() affiche le contenu de la variable a dans la console
# Résultat attendu : 3
print(a)

# On veut afficher "a=3" mais a est un entier et "a=" est une chaîne
# str(a) convertit l'entier a en chaîne de caractères "3"
# L'opérateur + concatène (colle) les deux chaînes ensemble
# Résultat attendu : a=3
print("a=" + str(a))

# f"..." est une f-string (formatted string) introduite en Python 3.6
# Tout ce qui est entre {} sera évalué et converti automatiquement en texte
# C'est plus lisible et pratique que la concaténation avec +
# Résultat attendu : a=3
print(f"a={a}")

# type() retourne le type de la variable passée en paramètre
# Résultat attendu : <class 'int'> car a contient un entier
print(type(a))

# Affiche une ligne de séparation pour mieux visualiser les résultats
print("---------")

# On modifie la valeur de a : on prend l'ancienne valeur (3) et on ajoute 4
# a vaut maintenant 7
a = a + 4

# Affiche la nouvelle valeur de a
# Résultat attendu : a=7
print("a=" + str(a))

# Vérifie que le type est toujours int (entier)
# Résultat attendu : <class 'int'>
print(type(a))

print("---------")

# On réaffecte a à 3 (sa valeur précédente est écrasée)
a = 3

# On crée une nouvelle variable b avec la même valeur que a
b = 3

# == est l'opérateur de comparaison "est égal à"
# Compare si a et b ont la même valeur
# Résultat attendu : True (vrai) car 3 == 3
print(a == b)

# != est l'opérateur de comparaison "est différent de"
# Résultat attendu : False (faux) car a et b sont égaux
print(a != b)

# =============================================================================
# Les nombres décimaux - flottants (float)
# =============================================================================
# Le type float a pour valeurs les réels dans [~ -1.8*10^308, ~ 1.8*10^308]
# Mêmes opérations arithmétiques et de comparaison que les entiers
... (473lignes restantes)
Réduire
script1.py
20 Ko
﻿
# =============================================================================
# Python : les données
# =============================================================================
# Une variable est une donnée temporaire que l'on stocke dans une case de la 
# mémoire (registre, RAM).
#
# On dit qu'elle est "variable" car c'est une valeur qui peut changer pendant 
# le déroulement du programme.
#
# Une variable est constituée de 2 choses :
# * Elle a une valeur : c'est la donnée qu'elle stocke (par exemple le nombre 5).
# * Elle a un nom : c'est ce qui permet de la reconnaître.
#
# Les variables peuvent contenir des types de données différents et leur type 
# peut évoluer au fil des instructions : Python est un langage à typage dynamique.
#
# L'opérateur = permet d'affecter une valeur à une variable.
#
# Consigne pour le nom de la variable :
# - Le nom de la variable doit être explicite sans être trop long à retaper
# - Il ne doit pas contenir d'espace ou de caractères accentués
# - Il ne doit pas commencer par un symbole ni chiffre
# - Certains mots sont réservés (nan, if, import, print...)
# - La casse doit être respectée (latitude ≠ Latitude)
# =============================================================================

# =============================================================================
# Les entiers (int)
# =============================================================================
# Le type int a pour valeurs les entiers positifs et négatifs
# Opérations arithmétiques : +, -, *, /
# Opérateurs classiques : division entière //, modulo %, puissance **
# Opérateurs de comparaison : <, >, ==, !=, <=, >= (renvoient True ou False)
#
# Fonctions utiles :
# - print() : fonction d'affichage
# - str() : convertit une donnée en string (chaîne de caractères)
# - type() : donne le type de la variable

# On crée une variable 'a' et on lui affecte la valeur entière 3
# Le signe = est l'opérateur d'affectation (pas d'égalité mathématique)
a = 3

# print() affiche le contenu de la variable a dans la console
# Résultat attendu : 3
print(a)

# On veut afficher "a=3" mais a est un entier et "a=" est une chaîne
# str(a) convertit l'entier a en chaîne de caractères "3"
# L'opérateur + concatène (colle) les deux chaînes ensemble
# Résultat attendu : a=3
print("a=" + str(a))

# f"..." est une f-string (formatted string) introduite en Python 3.6
# Tout ce qui est entre {} sera évalué et converti automatiquement en texte
# C'est plus lisible et pratique que la concaténation avec +
# Résultat attendu : a=3
print(f"a={a}")

# type() retourne le type de la variable passée en paramètre
# Résultat attendu : <class 'int'> car a contient un entier
print(type(a))

# Affiche une ligne de séparation pour mieux visualiser les résultats
print("---------")

# On modifie la valeur de a : on prend l'ancienne valeur (3) et on ajoute 4
# a vaut maintenant 7
a = a + 4

# Affiche la nouvelle valeur de a
# Résultat attendu : a=7
print("a=" + str(a))

# Vérifie que le type est toujours int (entier)
# Résultat attendu : <class 'int'>
print(type(a))

print("---------")

# On réaffecte a à 3 (sa valeur précédente est écrasée)
a = 3

# On crée une nouvelle variable b avec la même valeur que a
b = 3

# == est l'opérateur de comparaison "est égal à"
# Compare si a et b ont la même valeur
# Résultat attendu : True (vrai) car 3 == 3
print(a == b)

# != est l'opérateur de comparaison "est différent de"
# Résultat attendu : False (faux) car a et b sont égaux
print(a != b)

# =============================================================================
# Les nombres décimaux - flottants (float)
# =============================================================================
# Le type float a pour valeurs les réels dans [~ -1.8*10^308, ~ 1.8*10^308]
# Mêmes opérations arithmétiques et de comparaison que les entiers
# Peut être non défini (nan) ou infini (inf)
# Lecture des exposants : 2.1*10^-7 est noté 2.1e-7

# On remet a à 3 (un entier)
a = 3

# Affiche le type de a qui est actuellement int
# Résultat attendu : Le type de a=3 est <class 'int'>.
print(f"Le type de a=3 est {type(a)}.")

# On ajoute 4.0 (un float) à a (un int)
# Python convertit automatiquement le résultat en float
# C'est le typage dynamique : le type de a change de int à float
a = a + 4.0

# a vaut maintenant 7.0 (un float, pas un int)
# Résultat attendu : La valeur de a est 7.0.
print(f"La valeur de a est {a}.")

# Confirmation que a est maintenant un float
# Résultat attendu : Le type de a est <class 'float'>.
print(f"Le type de a est {type(a)}.")

print("---------")

# On crée b avec la valeur entière 7
b = 7

# Affiche les valeurs pour comparaison
# Résultat attendu : ? 7==7.0
print(f"? {b}=={a}")

# Compare les valeurs : 7 (int) == 7.0 (float)
# Python compare les valeurs numériques, pas les types
# Résultat attendu : True car 7 et 7.0 ont la même valeur mathématique
print(a == b)

# Compare les types : type(a) est float, type(b) est int
# Résultat attendu : False car les types sont différents
print(type(a) == type(b))

# Typage dynamique démontré : la variable a a changé de type au fil des instructions
# L'opérateur == compare le contenu quelque soit le typage des variables

# Calcul d'un très grand nombre : 1.3 * 10^174
# Python gère les grands nombres mais les convertit en notation scientifique
# Résultat attendu : 1.3000000000000002e+174
print(1.3 * (10**174))

# 10^500 est trop grand même pour un float, donc décommenté pour éviter l'erreur
# print(1.3*(10**500)) # conversion int -> float trop grand

# 1.3e500 est interprété directement comme un float
# Comme c'est trop grand, Python retourne inf (infini)
# Résultat attendu : inf
print(1.3e500)

# Même chose avec un nombre négatif
# Résultat attendu : -inf
print(-1.3e500)

# ATTENTION : Problème de précision des flottants !
# Les nombres décimaux ne sont pas représentés exactement en binaire
# 0.1 + 0.1 + 0.1 n'est PAS exactement égal à 0.3 en représentation binaire
# Résultat attendu : False (surprenant mais normal !)
print(0.1 + 0.1 + 0.1 == 0.3)

# Pour des calculs précis avec des décimaux, on utilise le module Decimal
from decimal import Decimal

# Decimal permet une représentation exacte des nombres décimaux
# On passe les nombres en chaînes de caractères pour éviter l'imprécision
x = Decimal('0.1')
y = Decimal('0.3')

# Avec Decimal, la comparaison est exacte
# Résultat attendu : True
print(x + x + x == y)

# =============================================================================
# Les booléens (bool)
# =============================================================================
# Le type bool a pour valeurs True (vrai) et False (faux)
# Opérations logiques : and (et), or (ou), not (non)

# On crée deux variables entières
a = 2
b = 3

# On compare a et b : 2 == 3 est faux
# Le résultat (False) est stocké dans la variable c
c = (a == b)

# Affiche la valeur de c
# Résultat attendu : False
print(c)

# On crée deux variables booléennes
entree1 = True   # Vrai
entree2 = False  # Faux

# OR (ou) : retourne True si AU MOINS UN des opérandes est True
# True or False = True
# Résultat attendu : True
print(entree1 or entree2)

# | est l'opérateur binaire OR, fonctionne aussi avec les booléens
# Résultat attendu : True
print(entree1 | entree2)

# AND (et) : retourne True si LES DEUX opérandes sont True
# True and False = False
# Résultat attendu : False
print(entree1 and entree2)

# & est l'opérateur binaire AND, fonctionne aussi avec les booléens
# Résultat attendu : False
print(entree1 & entree2)

# NOT (non) : inverse la valeur booléenne
# not True = False
# Résultat attendu : False
print(not entree1)

# Attention à la priorité des opérateurs !
# not a une priorité plus haute que or
# Donc "not True or True" est interprété comme "(not True) or True" = False or True = True
# Résultat attendu : True
print(not True or True)

# Avec les parenthèses, on force l'ordre d'évaluation
# D'abord (True or True) = True, puis not True = False
# Résultat attendu : False
print(not (True or True))

# Conseil : utilisez les parenthèses pour éviter toute ambiguïté !

# =============================================================================
# Les chaînes de caractères (str)
# =============================================================================
# Le type str a pour valeurs tout texte encadré de guillemets simples '' ou doubles ""
# Opérations : + pour la concaténation, * pour la duplication

# Création d'une chaîne avec des guillemets simples
chaine = 'abc'

# Création d'une chaîne avec des guillemets doubles (équivalent)
chaine2 = "bcd"

# str() convertit l'entier 3 en chaîne de caractères "3"
a = str(3)

# Concaténation de plusieurs chaînes avec l'opérateur +
# 'abc' + '3' + 'bcd' = 'abc3bcd'
chaine = chaine + a + chaine2

# Affiche la chaîne résultante
# Résultat attendu : abc3bcd
print(chaine)

# len() retourne la longueur (nombre de caractères) de la chaîne
# 'abc3bcd' contient 7 caractères
# Résultat attendu : 7
print(len(chaine))

# count() compte le nombre d'occurrences d'un caractère dans la chaîne
# 'c' apparaît 2 fois dans 'abc3bcd' (positions 2 et 5)
# Résultat attendu : 2
print(chaine.count('c'))

# L'opérateur * duplique la chaîne
# '3' * 3 = '333'
# Résultat attendu : 333
print(a * 3)

# =============================================================================
# Ensemble de données - Liste
# =============================================================================
# Une liste contient une série de valeurs de types différents séparés par des
# virgules, le tout entre crochets [].
#
# Opérations de base :
# - concaténation : + ou append, extend
# - suppression : remove ou del
# - recherche : in
# - indexation : nomListe[i] (commence à 0)
# - extraction : [debut:fin exclue:pas]

# Création d'une liste vide avec []
listeEntiers = []

# Concaténation avec + : on ajoute [3] à la liste vide
# Résultat : [3]
listeEntiers = listeEntiers + [3]

# Affiche la liste actuelle
# Résultat attendu : [3]
print(listeEntiers)

print("---------")

# Création d'une liste avec des éléments de types différents
# Contient des int (2, 21, 4), un str ('a'), et un str ('5')
listeEntiers2 = [2, 21, 'a', 4, '5']

# append() ajoute UN élément à la FIN de la liste
# listeEntiers devient [3, 10]
listeEntiers.append(10)

# extend() ajoute TOUS les éléments d'une autre liste à la fin
# listeEntiers devient [3, 10, 2, 21, 'a', 4, '5']
listeEntiers.extend(listeEntiers2)

# Affiche la liste complète
# Résultat attendu : [3, 10, 2, 21, 'a', 4, '5']
print(listeEntiers)

print("---------")

# len() retourne le nombre d'éléments dans la liste (7 éléments)
len(listeEntiers)

# Indexation : accès à un élément par sa position
# Les indices commencent à 0 !
# listeEntiers[0] = premier élément = 3
# Résultat attendu : 3
print(listeEntiers[0])

# listeEntiers[3] = quatrième élément = 21
# Résultat attendu : 21
print(listeEntiers[3])

# Indices négatifs : comptent depuis la fin
# listeEntiers[-2] = avant-dernier élément = 4
# Résultat attendu : 4
print(listeEntiers[-2])

print("---------")

# Slicing (extraction) avec [::-1] : inverse la liste
# Le pas -1 parcourt la liste à l'envers
# Résultat : ['5', 4, 'a', 21, 2, 10, 3]
listeEntiers = listeEntiers[::-1]

# Affiche la liste inversée
# Résultat attendu : ['5', 4, 'a', 21, 2, 10, 3]
print(listeEntiers)

# Slicing [1::2] : commence à l'indice 1, prend un élément sur 2
# Indices : 1, 3, 5 → valeurs : 4, 21, 10
# Résultat attendu : [4, 21, 10]
print(listeEntiers[1::2])

# Slicing [0:2:1] : de l'indice 0 à 2 (exclu), pas de 1
# Indices : 0, 1 → valeurs : '5', 4
# Résultat attendu : ['5', 4]
print(listeEntiers[0:2:1])

print("---------")

# remove() supprime la PREMIÈRE occurrence de la valeur spécifiée
# Supprime le 2 de la liste
listeEntiers.remove(2)

# Affiche la liste après suppression
# Résultat attendu : ['5', 4, 'a', 21, 10, 3]
print(listeEntiers)

# L'opérateur 'in' vérifie si une valeur est présente dans la liste
# 5 (entier) n'est PAS dans la liste (on a '5' qui est une chaîne)
# Résultat attendu : False
print(5 in listeEntiers)

# 10 est bien présent dans la liste
# Résultat attendu : True
print(10 in listeEntiers)

# index() retourne la position (indice) de la première occurrence
# 10 est à l'indice 4
# Résultat attendu : 4
print(listeEntiers.index(10))

print("---------")

# Les chaînes de caractères sont indicées comme des listes !
chaine = "bonjour"

# Slicing [0:3] : caractères des indices 0, 1, 2
# Résultat attendu : bon
print(chaine[0:3])

# Indice négatif : avant-dernier caractère
# Résultat attendu : u
print(chaine[-2])

# Rappel : une liste est ordonnée, indicée de 0 à N-1 (ou -1 à -N)
# On peut la renverser [::-1], la trier avec sort()

# =============================================================================
# Dictionnaire
# =============================================================================
# Un dictionnaire est un ensemble de données non ordonnées, indicées par une clé
# Défini par {"clé": valeur} entre accolades {}
# Chaque élément est une paire clé:valeur

# Création d'un dictionnaire vide
poisson1 = {}

# Création d'un dictionnaire avec 3 paires clé:valeur
# Les clés sont : "nom", "age", "taille"
# Les valeurs sont : "merouBrun", 4, 40
poisson1 = {"nom": "merouBrun", "age": 4, "taille": 40}

# Accès à une valeur par sa clé (comme un indice mais avec la clé)
# poisson1["nom"] retourne la valeur associée à la clé "nom"
# Résultat attendu : merouBrun
print(poisson1["nom"])

print("---------")

# Parcours des clés du dictionnaire avec une boucle for
# 'cle' prend successivement les valeurs : "nom", "age", "taille"
# poisson1[cle] retourne la valeur associée à cette clé
for cle in poisson1:
    print(cle, poisson1[cle])
# Résultat attendu :
# nom merouBrun
# age 4
# taille 40

print("---------")

# items() retourne les paires (clé, valeur) sous forme de tuples
# On peut les décomposer directement dans le for
# \t est une tabulation pour aligner l'affichage
for cle, valeur in poisson1.items():
    print(cle, "\t: ", valeur)
# Résultat attendu :
# nom    :  merouBrun
# age    :  4
# taille :  40

# values() retourne toutes les valeurs du dictionnaire
# list() les convertit en liste
# Résultat : ['merouBrun', 4, 40]
list(poisson1.values())

# On peut stocker plusieurs dictionnaires dans une liste
# C'est utile pour représenter une collection d'objets similaires
poisson2 = {"nom": "plie", "age": 3, "taille": 25}

# Liste contenant les deux dictionnaires poisson
listePoissons = [poisson1, poisson2]

# Parcours de la liste : affiche chaque dictionnaire complet
for p in listePoissons:
    print(p)
# Résultat attendu :
# {'nom': 'merouBrun', 'age': 4, 'taille': 40}
# {'nom': 'plie', 'age': 3, 'taille': 25}

# Parcours de la liste : accède à une clé spécifique de chaque dictionnaire
for p in listePoissons:
    print(p["taille"])
# Résultat attendu :
# 40
# 25

# =============================================================================
# Tuples - liste non modifiable
# =============================================================================
# Les tuples sont des structures non mutables (= non modifiables)
# Définis avec des parenthèses () au lieu de crochets []
# Utiles pour manipuler des données sans risquer de les modifier par erreur

# Création d'un tuple avec 3 éléments
# Les parenthèses sont optionnelles mais recommandées pour la lisibilité
p1 = ('merouBrun', 4, 40)

# Unpacking (déballage) : on assigne chaque élément à une variable
# x = 'merouBrun', y = 4, z = 40
[x, y, z] = p1

# ATTENTION : les tuples sont immuables !
# p1[2] = 1  # Cette ligne provoquerait une erreur TypeError
# On ne peut pas modifier un élément d'un tuple après sa création

# Affiche la première valeur extraite
# Résultat attendu : merouBrun
print(x)

print("-------")

# Création d'un deuxième tuple
p2 = ('plie', 3, 25)

# On peut mettre des tuples dans une liste
listeTuple = [p1, p2]

# Affiche la liste de tuples
# Résultat attendu : [('merouBrun', 4, 40), ('plie', 3, 25)]
print(listeTuple)

# Parcours de la liste : accède au 3ème élément (indice 2) de chaque tuple
for p in listeTuple:
    print(p[2])
# Résultat attendu :
# 40
# 25

# =============================================================================
# DataFrame / Pandas
# =============================================================================
# Pandas est une librairie Python pour manipuler facilement des données :
# - Tableaux avec étiquettes de variables (colonnes) et d'individus (lignes)
# - Appelés DataFrames, similaires aux dataframes sous R
# - Se comporte comme un dictionnaire (clés = noms colonnes, valeurs = séries)
# - Lecture/écriture facile depuis/vers fichiers CSV, Excel, etc.
# - Création de graphiques facile avec matplotlib

# Variable pour contrôler l'installation de pandas
# Mettre à True la première fois si pandas n'est pas installé
installPanda = False

# Installation conditionnelle de pandas
if installPanda:
    import sys
    # La ligne suivante installerait pandas (décommentée dans un notebook Jupyter)
    # !{sys.executable} -m pip install pandas

# Import des librairies nécessaires
# pd est l'alias conventionnel pour pandas
import pandas as pd
# np est l'alias conventionnel pour numpy (calcul numérique)
import numpy as np

# Création d'un dictionnaire de Series pandas
# Chaque clé sera un nom de colonne
# Chaque valeur est une Series (liste indexée)
dico = {
    'Name': pd.Series(['MerouBrun', 'Plie']),      # Colonne des noms
    'Age': pd.Series([4, 3]),                       # Colonne des âges
    'Taille': pd.Series([40, 25])                   # Colonne des tailles
}

# Création du DataFrame à partir du dictionnaire
# Un DataFrame est un tableau 2D avec des lignes et colonnes étiquetées
df = pd.DataFrame(dico)

# Affiche le DataFrame formaté
# Résultat attendu :
#        Name  Age  Taille
# 0  MerouBrun    4      40
# 1       Plie    3      25
print(df)

print("------")

# itertuples() permet de parcourir le DataFrame ligne par ligne
# Chaque ligne est retournée sous forme de tuple nommé
for e in df.itertuples():
    # df['Name'] accède à la colonne entière 'Name'
    # Attention : ici on affiche toute la colonne à chaque itération
    print(df['Name'])
# Résultat : affiche 2 fois la colonne Name complète

print("------")

# iat[] permet d'accéder à une cellule par ses indices (ligne, colonne)
# iat[1, 0] = ligne 1 (2ème ligne), colonne 0 (1ère colonne) = 'Plie'
# Résultat attendu : Plie
print(df.iat[1, 0])