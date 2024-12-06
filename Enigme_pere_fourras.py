import json
import random

def charger_enigme(fichier): ##charger le fichier demandé
    try:
        with open(fichier, 'r',encoding='utf-8') as f:
            enigmes=json.load(f)
        return enigmes
    except FileNotFoundError:
        print(f"Le fichier {fichier} est introuvable")
        return []

def enigme_pere_fourras():
    enigmes=charger_enigme('enigmesPF.json')
    if not enigmes:
        print("impossible sans énigmes ")
        return False
    enigmes=random.choice(enigmes)
    question= enigmes['question']
    reponse_correcte=enigmes['reponse'].strip().lower()
    print("\n L'énigme du Pere_Fourras" )
    print(f"Voici votre énigme : {question} ")

    essais_restants=3
    while essais_restants<=3:
        reponse=input("Votre réponse :").strip().lower()
        if reponse==reponse_correcte:
            print("Bravo C'est la bonne réponse!!!")
            return True
        else:
            essais_restants-=1
            if essais_restants>0:
                print(f"Mauvaise réponse il vous reste {essais_restants} essai(s). ")
            else:
                print(f" Vous avez échoué. La bonne réponse était : {reponse_correcte}.")
                return False

#enigme_pere_fourras()
