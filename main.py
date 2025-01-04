import random
from Enigme_pere_fourras import enigme_pere_fourras
from fonctions_utiles import (introduction, composer_equipe, menu_epreuves, choisir_joueur, enregistrer_historique)
from epreuve_finale import salle_De_Tresor
from logique import jeu_bataille_navale
from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard


def jeu():
    introduction()
    equipe = composer_equipe()

    cles_totales = 3
    cles_obtenues = 0

    print("\nLe jeu commence maintenant !")
    print(f"Vous devez obtenir {cles_totales} clés pour accéder à la salle du trésor.\n")
    while cles_obtenues < cles_totales:
        choix_epreuve = menu_epreuves()

        # Sélectionner un joueur
        joueur = choisir_joueur(equipe)
        if choix_epreuve == 1:  # Épreuve de Mathématiques
            epreuve = "Épreuve de Mathématiques"
            resultat = epreuve_math()
        elif choix_epreuve == 2:  # Épreuve de Logique
            epreuve = "Épreuve de Logique"
            resultat = jeu_bataille_navale()
        elif choix_epreuve == 3:  # Épreuve du Hasard
            epreuve = "Épreuve du Hasard"
            resultat = epreuve_hasard()
        elif choix_epreuve == 4:  # Énigme du Père Fouras
            epreuve = "Énigme du Père Fouras"
            resultat =enigme_pere_fourras()
        else:
            print("Choix d'épreuve invalide.")
            continue

        # Mettre à jour les clés si succès
        if resultat:
            print(f"Félicitations ! {joueur['nom']} a remporté l'épreuve et gagné une clé.\n")
            joueur["cles_gagnees"] += 1
            cles_obtenues += 1
        else:
            print(f"Malheureusement, {joueur['nom']} a échoué dans cette épreuve.\n")

        # Enregistrer l'historique
        enregistrer_historique(joueur, epreuve, "Succès" if resultat else "Échec")

        print(f"Clés obtenues : {cles_obtenues}/{cles_totales}\n")

    print("Félicitations, vous avez obtenu les trois clés nécessaires pour accéder à la salle du trésor !")
    salle_De_Tresor()

jeu()