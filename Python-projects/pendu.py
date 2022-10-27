"""
                                 JEU DU PENDU
------------------------------------------------------------------------------------------
Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi.

Le programme devra donc choisir aléatoirement un mot dans "dico_france.txt"
et afficher :
- Le nombre de vies restantes au joueur
- Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
   En expert, la liste n’apparaîtra pas)
- Des “_” pour remplacer les lettres non trouvées
- Les lettres proposées qui se trouvent dans le mot

La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.
------------------------------------------------------------------------------------------
"""

# On importe random pour que le programme puisse parcourir le fichier de facon aléatoirement
import random

# Indiquer au programme qu'il faut parcourir le fichier "dico_france.txt"
# Choisir aléatoirement un mot dedans 
mot_hasard = [""]

with open ("dico_france.txt","r", encoding="ISO-8859-1") as file:
    for lettre in file:
        mot_hasard.append(lettre.rstrip("\n"))
mot_atrouver = random.choice(mot_hasard)
print(mot_atrouver)

# On indique à l'utilisateur la différence entre chaque niveau
# \n indique un retour à la ligne
print(" Débutant 10 vies \n", "Intermediaire 7 vies \n", "Expert 4 vies \n" )

# On propose en suite à l'utilisateur de choisir quel niveau il souhiates
choix_niveau=str(input("Bonjour, à quel niveau souhaites-tu jouer ? \n"))

if choix_niveau == "Débutant" :
    vie = 10
elif choix_niveau == "Intermediaire" :
    vie = 7
elif choix_niveau == "Expert" :
    vie = 4 

print("Nombre de vies restantes : " + str(vie))

# Calculer le nombre de caractère qu'il contient
# Les transformer en underscore "_" 
underscore=""
for lettre in mot_atrouver:
    underscore += "" + ("_ ")


# Si le niveau choisi est débutant ou intermédiaire il faut afficher l'historique des lettres qui ont été proposé
# Mais si le niveau choisi est expert il ne faudra pas l'afficher
historique_l = []

while vie > 0 :

    print(" ")
    print("Mot à trouver:", underscore)
    if choix_niveau != "Expert" :
        print(" ")
        print("Historique des lettres : ", historique_l)
        lettre = input("Quelle lettre proposes tu ? ")
        historique_l.append(lettre)
    else:
        print(" ")
        lettre = input("Quelle lettre proposes tu ? ")
        historique_l.append(lettre)


# Si la réponse est juste 
lettre_trouvee = ""

if lettre in mot_atrouver:
    lettre_trouvee += lettre
    print("Tu y es presque, continue comme ca !")

# Faire comprendre au programme qu'a chaque réponse fausse l'utilisateur perd une vie
# en faisant un décompte à partir du nombre de vie qu'il a à la base
else:
    tentatives = vie - 1
    print("Lache rien, il te reste encore : ", tentatives, "vies")

 # je met à jour l'affichage du mot à trouver

affichage = ""
for x in mot_atrouver:
    if x in lettre_trouvee :
        affichage += x
        affichage += " "
    else:
        affichage += "_ "


#-----------------------------------------------------------------------------------------
#     Il est pas fini... Mais peu importe le temps que ca prendra, je le finirai !
#-----------------------------------------------------------------------------------------