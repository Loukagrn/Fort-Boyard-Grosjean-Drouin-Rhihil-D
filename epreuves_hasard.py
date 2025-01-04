import random

def bonneteau():
    # Initialisation des bonneteaux
    bonneteaux = ['A', 'B', 'C']
    print("Bienvenue dans le jeu de bonneteau !")
    print("Vous avez deux essais pour deviner sous quel bonneteau (A, B ou C) se cache la clé.")
    print("Les bonneteaux disponibles sont : A, B, C.")

    for tentative in range(1, 3):  # Deux essais
        # Clé placée aléatoirement
        bonneteau_cle = random.choice(bonneteaux)
        print(f"\nTentative {tentative} sur 2.")

        # Demander au joueur de choisir
        choix_joueur = input("Choisissez un bonneteau (A, B ou C) : ").strip().upper()
        if choix_joueur not in bonneteaux:
            print("Choix invalide, veuillez choisir entre A, B ou C.")
            continue
        if choix_joueur == bonneteau_cle:
            print("Félicitations ! Vous avez trouvé la clé.")
            return True
        else:
            print("Dommage ! La clé n'est pas sous ce bonneteau.")

    print(f"Vous avez perdu. La clé était sous le bonneteau {bonneteau_cle}.")
    return False

def jeu_lance_des():
    MAX_ESSAIS = 3
    print("Bienvenue dans le jeu de lancer de dés !")
    print("Le premier à obtenir un 6 avec l'un de ses deux dés remporte la partie.")
    print("Vous avez un maximum de trois essais.")

    for essai in range(1, MAX_ESSAIS + 1):  # Trois essais
        print(f"\nEssai {essai} sur {MAX_ESSAIS}.")

        # Lancer des dés pour le joueur
        input("Appuyez sur Entrée pour lancer les dés...")
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print(f"Vous avez obtenu : {des_joueur}")

        if 6 in des_joueur:
            print("Félicitations ! Vous avez obtenu un 6 et remporté la partie.")
            return True

        # Lancer des dés pour le maître du jeu
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Le maître du jeu a obtenu : {des_maitre}")

        if 6 in des_maitre:
            print("Le maître du jeu a obtenu un 6. Vous avez perdu.")
            return False

        print("Aucun 6 obtenu. On passe au prochain essai.")

    print("Aucun joueur n'a obtenu un 6 après trois essais. Match nul.")
    return False


def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()
