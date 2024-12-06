import os

def introduction():
    print("=" * 50)
    print("Bienvenue dans le jeu Fort Boyard !")
    print("Règles du jeu :")
    print("1. Vous devez accomplir des épreuves pour gagner des clés.")
    print("2. L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")
    print("Bonne chance à tous les participants !")
    print("=" * 50)


def composer_equipe():
    equipe = []
    while True:
        try:
            nb_joueurs = int(input("Combien de joueurs voulez-vous inscrire dans l'équipe ? (max 3) : "))
            if 1 <= nb_joueurs <= 3:
                break
            print("Erreur : L'équipe doit comprendre entre 1 et 3 joueurs.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(nb_joueurs):
        print(f"\nInscription du joueur {i + 1} :")
        nom = input("Nom : ").strip()
        profession = input("Profession : ").strip()
        est_leader = input("Est-ce le leader de l'équipe ? (oui/non) : ").strip().lower() == 'oui'
        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": est_leader,
            "cles_gagnees": 0
        }
        equipe.append(joueur)

    if not any(joueur["leader"] for joueur in equipe):
        print("Aucun leader désigné. Le premier joueur devient automatiquement le leader.")
        equipe[0]["leader"] = True

    return equipe


def menu_epreuves():
    print("\nMenu des épreuves disponibles :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Énigme du Père Fouras")

    while True:
        try:
            choix = int(input("Choisissez une épreuve (entrez le numéro correspondant) : "))
            if 1 <= choix <= 4:
                return choix
            print("Erreur : Veuillez choisir un numéro entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def choisir_joueur(equipe):
    print("\nListe des joueurs de l'équipe :")
    for i, joueur in enumerate(equipe, start=1):
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")

    while True:
        try:
            choix = int(input("Entrez le numéro du joueur : "))
            if 1 <= choix <= len(equipe):
                return equipe[choix - 1]
            print("Erreur : Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


def enregistrer_historique(joueur, epreuve, resultat):
    """
    Enregistre l'historique des épreuves dans un fichier texte.
    :param joueur: Dictionnaire représentant le joueur ayant participé.
    :param epreuve: Nom de l'épreuve.
    :param resultat: Résultat de l'épreuve (succès/échec).
    """
    historique_dir = "output"
    historique_file = os.path.join(historique_dir, "historique.txt")

    # Créer le répertoire  sortie si nécessaire
    if not os.path.exists(historique_dir):
        os.makedirs(historique_dir)

    with open(historique_file, 'a', encoding='utf-8') as fichier:
        fichier.write(f"Joueur : {joueur['nom']} ({joueur['profession']})\n")
        fichier.write(f"Épreuve : {epreuve}\n")
        fichier.write(f"Résultat : {resultat}\n")
        fichier.write(f"Clés gagnées : {joueur['cles_gagnees']}\n")
        fichier.write("=" * 50 + "\n")
    print("Historique mis à jour.")
#composer_equipe()