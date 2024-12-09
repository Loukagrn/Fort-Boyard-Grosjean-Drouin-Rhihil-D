import random

# Étape 1
def bonneteau():
    bonneteaux = ['A', 'B', 'C']
    tentatives_restantes = 2

    # Étape 2
    print("Bienvenue dans l'épreuve du Bonneteau")
    print("Une clé est cachée sous l'un des bonneteaux : A, B ou C")
    print("Vous avez 2 tentatives pour la trouver")

    # Étape 3
    print(f"Les bonneteaux disponibles sont : {', '.join(bonneteaux)}")

    # Étape 4
    for tentative in range(1, tentatives_restantes + 1):
        # Étape 5
        bonneteau_clef = random.choice(bonneteaux)

        # Étape 6
        print(f"Tentative {tentative}/{tentatives_restantes} :")

        # Étape 7
        choix_joueur = input("Choisissez un bonneteau (A, B ou C) : ")

        # Étape 7a
        if choix_joueur == 'a' or choix_joueur == 'A':
            choix_joueur = 'A'
        elif choix_joueur == 'b' or choix_joueur == 'B':
            choix_joueur = 'B'
        elif choix_joueur == 'c' or choix_joueur == 'C':
            choix_joueur = 'C'
        else:
            # Étape 7b
            print("Choix invalide. Veuillez choisir parmi A, B ou C.")
            continue  # Redemander le choix dans la même tentative

        # Étape 7c
        if choix_joueur == bonneteau_clef:
            print(f"Bien joué ! Vous avez trouvé la clé sous le bonneteau {choix_joueur}.")
            return True
        else:
            print(f"Perdu, la clé n'est pas sous le bonneteau {choix_joueur}.")

    # Étape 8

    # Étape 9
    print(f"Dommage, vous avez perdu ! La clé se trouvait sous le bonneteau {bonneteau_clef}.")
    return False


def jeu_lance_des():
    Nombre_essais= 3

    print("Bienvenue dans le jeu de lancer de dés")
    print("Le premier à obtenir un 6 gagne la partie de lancer de dés.")
    print("Vous avez 3 essais pour gagner contre le maître du jeu.\n")

    for essai in range(1, Nombre_essais + 1):
        print(f"--- Essai {essai}/{Nombre_essais} ---")

        # Étape 3
        input("Appuyez sur 'Entrée' pour lancer vos dés")

        # Étape 4-5
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print(f"Résultat des dés du joueur : {des_joueur[0]} et {des_joueur[1]}")

        # Étape 6
        if 6 in des_joueur:
            print("Bravo ! Vous avez obtenu un 6. Vous remportez la partie et la clé !")
            return True  # Le joueur a gagné

        # Étape 7
        print("\nC'est au tour du maître du jeu de lancer les dés")
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Résultat des dés du maître du jeu : {des_maitre[0]} et {des_maitre[1]}")

        # Étape 8-9
        if 6 in des_maitre:
            print("Le maître du jeu a obtenu un 6. Vous perdez la partie.")
            return False  # Le maître du jeu a gagné

        # Étape 10
        print("Aucun 6 obtenu. On passe au prochain essai\n")

    # Étape 11
    print("Personne n'a obtenu un 6 après trois essais, égalité.")
    return False  # Personne n'a gagné



def epreuve_lancer_des():
    print("🎲 Vous avez sélectionné l'épreuve du lancer de dés !")
    jeu_lance_des()

def epreuve_bonneteau():
    print("🎩 Vous avez sélectionné l'épreuve du Bonneteau !")
    bonneteau()

def epreuve_hasard():
    """
    Sélectionne aléatoirement une épreuve parmi plusieurs fonctions
    et l'exécute.
    """
    # Étape 1
    epreuves = [epreuve_bonneteau, epreuve_lancer_des]

    # Étape 2
    epreuve = random.choice(epreuves)

    # Étape 3
    print("\n🎲 Sélection d'une épreuve aléatoire...\n")
    epreuve()

if __name__ == "__main__":
    epreuve_hasard()
