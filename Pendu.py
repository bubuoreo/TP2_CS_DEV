# BURLOT Alexandre
# GAUD Romain
# 01/12/2020
# subject : Faire un pendu sur console avec un choix de mot dans un fichier.
# TODO :
# - faire une fonction qui, à la place de demander à un autre utilisateur d'entrer un mot, va en prendre un dans un fichier

import random
import tkinter


class Mot:
    def __init__(self):
        with open("Dico.txt","r") as Dico :
            liste = Dico.readlines()
            i = random.randint(0,len(liste)-1)
            print(i)
            print(liste)
            mot = liste[i]
            mot = mot.rstrip("\n")
        mot = mot.lower()
        self.__ortho = mot
        self.__taille = len(self.__ortho)
        self.__essais = []
        self.__fautes = 0

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
            return False
        else:
            return True

    def proposition(self):
        print("trouve une lettre du mot")
        lettre = input()
        print()
        if lettre not in self.__ortho:
            self.__fautes += 1
        if lettre not in self.__essais:
            self.__essais.append(lettre)

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

winning = True
mot_a_deviner = Mot()

while winning:
    winning = mot_a_deviner.mot_cache()
    if not winning:
        break
    mot_a_deviner.proposition()
    winning = mot_a_deviner.pendu()

