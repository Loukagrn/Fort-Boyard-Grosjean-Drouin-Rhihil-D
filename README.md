Fort-Boyard Projet
Contiibuteur:
-Louka Grosjean
-Saad Rhihil
-Olivier Drouin

Ce projet simule une partie du jeu 'Fort_Boyard', trois clés sont attendues pour accéder à la salle finale et réussir le jeu, les types d'épreuves sont des énigmes, de l'aléatoire/hasard, de mathématiques et de logique.

Les fonctionnalitées principales sont: 
jeu() qui permet de lancer la partie/ enigme_pere_fourras qui choisi et lance une énigme au hasard/ epreuve_finale qui se lance apres avoir récupérée les trois clés et lance une enigme/ les fonctions épreuves maths/hasard/logique qui consituent le jeu en lui-même. Enfin les fonction_utiles sont l'ensemble des fonctions qui sont nécéssaires au bon fonctionnement du programme, ajouté a celles-ci enregistrer_historique, fonction bonus, qui enregistre chaque avanacement de partie.

Le langage de programmation utilisé est exclusivement pyhton et les bibliothèques utilisées sont 'random' pour la génération aléatoire et 'json' pour l'exctraction et l'utilisation des données. 'Os' a aussi été utilisée bien que interdit dans le cadre de la fonction enregister_historique.

Pour cloner ce dépot Git il faut copier le lien suivant: https://github.com/Loukagrn/Fort-Boyard.git
Puis ouvrir GitBash, et taper 'git clone' suivi de l'url que vous souhaitez copier.

Pour lancer ce programme il vous suffit de lancer le programme 'main'.

Algorithme de jeu():
1-Lancement de la fonction introduction qui donne les règles du jeu et composer_équipes qui crée l'équipe qui vas participer.
2-initialisation des variables pour suivre le nombre de clés.

lancement du jeu:
3-tant que les clés obtenues sont inférieur au nombre de clés voulues on lance un jeu.
4-on lance le choix des épreuves via menu_epreuves
5-on choisi un joueur avec choisir_joueur
6-Selection des épreuves (parmis logique/hasard/maths/énigme PF), si nombre choisi est supérieur à 4 alors: "Choix d'épreuve invalide"

Vérification des clés:
7-Si le joueur à réussi alors: Clés +1 et 'Félicitation'
8-Sinon: 'joueur n'as pas réussi'
9- enregistrer historique 
10- si clés obtenues egales à 3 alors: 'bravo' lancer salle_de_trésor()

Fonctions implémentées:
Module enigme_PF:
Charger_enigme prend en paramètre le nom d'un fichier Json et retourne la liste des énigmes.
Enigme_pere_fourras ne prend pas de paramètre et vas chosir une enigme grâce à charger_enigme, la poser au joueur et renvoyer un bool en fonction de la réponse du joueur qui aura 3 chances pour répondre correctement.

Module epreuve_finale:
Une seule fonction: Salle_de_tresor qui ne prend pas de paramètre et qui ouvre 'indicesSalle', choisi une énigme et renvoie si le joueur à trouvé ou non, il a 3 essai et si il trouve il gagne le jeu.

Module fonctions_utiles:
Introduction: Ne prend pas de paramètre et ecrit les règles du jeu 
composer_equipe: pas de paramètre/ renvoi une liste contenant la liste des joueurs max 3
menu_épreuve: pas de paramètre/ demande à choisir entre les 4 tyes d'épreuves disponible, erreur affichée si nb supérieur à 4 
choisir_joueur: prend en parametre la liste retournée dans composer_équipe et demande au joueur d'en choisir un.
enregistrer_historique: prend en paramètre le joueur choisi précedement,l'épreuve choisie et le résultat de l'épreuve (bool)

Module mathématiques:
factorielle: calcule la factorielle d'un nombre n 
epreuve_math_factorielle: lance l'épreuve demandant de calculer la factorielle, renvoi un bool
epreuve_roulette_mathematique: renvoi un bool/ pas de paramètre
epreuve_math_premier: renvoi un bool/ pas de paramètre/ se sert de est_premier qui calcule si un nb n est premier et premier_plus_proche qui renvoi le premier plus provhe d'un nb n 
epreuve_math: lance aléatoirement une des trois épreuves (epreuve_math_factorielle, epreuve_roulette_mathematique, epreuve_math_premier)

Module hasard:
bonneteau/jeu_de_des: renvoi toutes les deux un bool/ ne prennent pas de paramètre
epreuve_hasard: choisi au hasard parmis les deux épreuves 

Module logique:
jeu_bataille_navale: pas de paramètres/ regroupe toutes les fonctions du module logique et lance le jeu de logique(bataille navale)
suiv: prend en paramètre le joueur qui vient de jouer pour renvoyer celui qui doit jouer
affiche_grille: prend en paramètre une grille a afficher (ex:la grille de tir du joueur) et un message à afficher
tour: va prendre en paramètre le joueur qui doit jouer la grille de tir de ce joueur et la grille de l'adversaire/simule un tour donc le joueur tir et un message annonce si touché ou non 
gagne:prend en paramètre la grille de tir du joueur et renvoi un bool True il a 2 'X' qui équivaut à deuc bateaux coulés et donc une partie gagnées


Gestion des erreurs:
Nous avins systématiquement vérifiés les input (type, itervalles)
Pour les fichiers Json nous avons vérifiés avec Try/except si le fichier etait présent ou non
Si le fichier Json est mal formaté alors JsonDecodeError
Boucle si la saisie des joueurs est incorrecte.

Bon jeu!!
