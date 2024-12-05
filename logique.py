from random import *
def grille_vide():
    return[[" " for _ in range(3)]for _ in range (3)]

def suiv(joueur):
    return(joueur+1)%2

def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        print(" | " + " | ".join(ligne) + " |")
    print("-" * 12)

def demande_position():
    while True:
        try:
            pos=input("Saisir un position (ligne, colonne) :")
            ligne, colonne=
        except ValueError:
            print("Format impossible")


#print(affiche_grille([[" "," ","b"],[" "," "," "],["b"," ","    "],],"départ"))
