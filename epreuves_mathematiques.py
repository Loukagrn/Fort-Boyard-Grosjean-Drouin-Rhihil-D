import random
def factorielle(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs." )
    if n == 0:
        return 1
    resultat = 1
    for i in range(1,n+1):
        resultat *= i
    return resultat
def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print(f"Épreuve de Mathématiques: Calculer la factorielle de {n}.")
    resultat_attendu = factorielle(n)
    while True :
        try:
            reponse = int(input("Votre réponse: "))
            if reponse == resultat_attendu :
                print("Correct! Vous gagnez une clé.")
                return True
            else:
                print(f"Faux! Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def epreuve_roulette_mathematique():
    nombres = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['addition', 'soustraction', 'multiplication'])

    print(f"Nombres sur la roulette : {nombres}")
    print(f"calculez le résultat en combinant ces nombres avec une {operation}")

    if operation == 'addition':
        resultat_attendu = sum(nombres)
    elif operation == 'soustraction' :
        resultat_attendu = nombres[0]
        for n in nombres[1:]:
            resultat_attendu -= n
    elif operation == 'multiplication':
        resultat_attendu = 1
        for n in nombres:
            resultat_attendu *= n
    while True :
        try:
            reponse = int(input("Votre réponse: "))
            if reponse == resultat_attendu :
                print("Bonne réponse! Vous avez gagné une clé.")
                return True
            else:
                print("Faux! Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide")
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+ 1 ):
        if n % i == 0:
            return False
    return True
def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n
def epreuve_math_premier():
    n = random.randint(10,20)
    print(f"Épreuve de Mathématiques: Trouver le nombre premier le plus proche de {n} ")
    resultat_attendu = premier_plus_proche(n)
    while True:
        try:
            reponse = int(input("Votre réponse: "))
            if reponse == resultat_attendu :
                print("Correct! Vous gagnez une clé.")
                return True
            else:
                print("Faux! Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")



def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_roulette_mathematique, epreuve_math_premier]
    epreuve = random.choice(epreuves)
    return epreuve()

if __name__ == "__main__":
    epreuve_math()