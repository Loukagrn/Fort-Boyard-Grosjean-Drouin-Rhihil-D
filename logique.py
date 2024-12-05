from random import *
def grille_vide():
    return[[" " for _ in range(3)]for _ in range (3)]

def suiv(joueur):
    return(joueur+1)%2

def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        print(" | " + " | ".join(ligne) + " |")
    print("-" * 14)

def demande_position():
    while True:
        pos = input("Entrez la position (ligne,colonne) entre 0 et 2 : ") ##changer de 0 et 2 a 1 et 3
        if ',' in pos:  # Vérifie si la virgule est présente
            parts = pos.split(',')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                ligne = int(parts[0])
                colonne = int(parts[1])
                if 0 <= ligne < 3 and 0 <= colonne < 3:  # changer ici aussi
                    return ligne, colonne
                else:
                    print("Position hors des limites. Réessayez.")
            else:
                print("Entrée invalide. Assurez-vous de saisir deux nombres séparés par une virgule.")
        else:
            print("Format invalide. Utilisez le format 'ligne,colonne'.")

def init():
    grille=grille_vide()
    print("Placez vos deux bateau")
    bateau_placé=0
    while bateau_placé<2:
        ligne, colonne=demande_position()
        if grille[ligne][colonne]== " ":
            grille[ligne][colonne]="B"
            bateau_placé+=1
        else:
            print("Place déjà occupée")
    affiche_grille(grille,"Découvrez votre grille de jeu avec vos bteau")
    return grille

def tour(joueur,grille_tir_joueur,grille_adversaire):
    if joueur==0: ##joueur reel
        affiche_grille(grille_tir_joueur,"Rappel de l'historique des tirs que vous avez éffectués:")
        print("Entrez la position (ligne,colonne) entre 0 et 2 pour tirer:")
        ligne, colonne = demande_position()
    else: ##maitre du jeu #bot
        ligne, colonne= random.randit(0,2),random.randit(0,2)
        print(f"Le maître du jeu tire en position({ligne},{colonne})")

    if grille_adversaire[ligne][colonne]=="B":
        print("Touché coulé")
        grille_tir_joueur[ligne][colonne]="x"
        grille_tir_joueur[ligne][colonne]="x"
    else:
        print("Dans l'eau...")
        grille_tir_joueur[ligne][colonne] = "."

def gagne(grille_tirs_joueur):
    return sum(row.count("x") for row in grille_tirs_joueur) == 2

def jeu_bataille_navale():
    print("Bienvenue dans le jeu de bataille navale simplifié !")
    print("Chaque joueur doit placer 2 bateaux sur une grille 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    grille_joueur=init()
    grille_maitre=grille_vide()

##print(init())
