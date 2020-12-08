# BURLOT Alexandre
# GAUD Romain
# 01/12/2020
# subject : Faire un pendu sur console avec un choix de mot dans un fichier. 8 fautes max.
# TODO :

import random

class Mot:
    def __init__(self):
        with open("Dico.txt","r") as Dico :
            liste = Dico.readlines() # Lit le dictionnaire et place les lignes dans une liste
            i = random.randint(0,len(liste)-1) # fait un random
            mot = liste[i] # choisi le mot
            mot = mot.rstrip("\n") # enleve le passage à la ligne sur les éléments de la liste
        mot = mot.lower() # met en minuscule
        self.__ortho = mot # stocke le mot en clair
        self.__essais = [] # liste des essais
        self.__fautes = 0 # Nombre de fautes
        self.__winning = True # confirme que le jeu continu car nous sommes en train de gagner
        self.__essais.append(self.__ortho[0]) # Ajout de la première lettre du mot dans la liste des essaies 
        self.play() # appelle la fonction play 

    def play(self):
        while self.__winning:
            self.__winning = self.mot_cache()
            if not self.__winning:
                break
            self.proposition()
            self.__winning = self.pendu()
        print("Voulez-vous rejouer ? 'O' = Oui, 'N'= Non.")
        while True:
            choice = input()
            if choice == 'O':
                print()
                Mot()
                break
            if choice == 'N':
                break
            else:
                print("Je n'ai pas compris votre demande, veuillez réessayer.")

    def mot_cache(self):
        cache = ''
        for lettre in self.__ortho:
            if lettre in self.__essais or lettre == '-' or lettre == ' ' or lettre == "'":
                print(lettre, end='')
                cache += lettre
            else:
                print("_", end='')
                cache += "_"
        print()
        print()
        print(self.__essais)
        if cache == self.__ortho:
            print("Bravo, tu as gagné")
            return False
        else:
            return True

    def proposition(self):
        print("trouve une lettre du mot")
        lettre = input()
        print()
        if lettre in self.__essais:
            print("Vous avez déja proposé cette lettre. Veuillez réessayer.")
            self.proposition()
        if lettre not in self.__essais:
            self.__essais.append(lettre)
        if lettre not in self.__ortho:
            self.__fautes += 1


    def pendu(self):
        if self.__fautes == 0:
            print("")
        elif self.__fautes == 1:
            print("")
            print("___/|\\___")
        elif self.__fautes == 2:
            print("")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 3:
            print("     _________")
            print("    |/")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 4:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 5:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 6:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 7:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |       / \\")
            print("    |")
            print("___/|\\___")
        elif self.__fautes == 8:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |       \\|/")
            print("    |        |")
            print("    |       / \\")
            print("    |")
            print("___/|\\___")
            print()
            print(self.__ortho)
            print()
            print("Eh, t'as perdu.")
            return False
        print()
        return True


print("Bonjour et bienvenu dans ce programme modélsant un pendu")
print()
print()
mot_a_deviner = Mot()

