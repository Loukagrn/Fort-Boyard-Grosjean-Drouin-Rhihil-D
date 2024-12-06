import json
import random

def salle_De_Tresor():
    try:
        with open('indicesSalle.json', 'r', encoding='utf-8') as fichier:
            jeu_tv = json.load(fichier)["Fort Boyard"]
    except FileNotFoundError:
        print("Erreur : fichier 'indicesSalles.json' introuvable.")
        return
    except json.JSONDecodeError:
        print("Erreur : fichier 'indicesSalles.json' invalide.")
        return

    annees = list(jeu_tv.keys())
    annee = random.choice(annees)

    emissions = list(jeu_tv[annee].keys())
    emission = random.choice(emissions)

    details_emission = jeu_tv[annee][emission]
    indices = details_emission["Indices"]
    mot_code = details_emission["MOT-CODE"]

    print(f"Année : {annee}, Émission : {emission}")
    print("Voici les trois premiers indices pour deviner le mot-code :")
    for i, indice in enumerate(indices[:3], start=1):
        print(f"Indice {i} : {indice}")

    essais = 3
    reponse_correcte = False

    while essais > 0:
        reponse = input("Entrez votre proposition pour le mot-code : ").strip()

        if reponse.lower() == mot_code.lower():
            reponse_correcte = True
            break
        else:
            essais -= 1
            if essais > 0:
                print(f"Incorrect ! Il vous reste {essais} essais.")
                if len(indices) > 3:
                    print(f"Nouvel indice : {indices[3]}")
                    indices.pop(3)
            else:
                print(f"Échec ! Le mot-code correct était : {mot_code}")

    if reponse_correcte:
        print("Félicitations ! Vous avez trouvé le mot-code et accédez au trésor ! ")
    else:
        print("Dommage ! Vous n'avez pas réussi à ouvrir la salle du trésor.")

#salle_De_Tresor()
