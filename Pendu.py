# BURLOT Alexandre
# GAUD Romain
# 01/12/2020
# subject : Faire un pendu sur console avec un choix de mot dans un fichier.
# TODO :
# - faire une fonction qui, à la place de demander à un autre utilisateur d'entrer un mot, va en prendre un dans un fichier
# - 


class Mot:
    def __init__(self, word):
        mot = word.lower()
        self.ortho = mot
        self.taille = len(self.ortho)
        self.essais = []
        self.fautes = 0

    def mot_cache(self):
        cache = ''
        for lettre in self.ortho:
            if lettre in self.essais or lettre == '-' or lettre == ' ' or lettre == "'":
                print(lettre, end='')
                cache += lettre
            else:
                print("_", end='')
                cache += "_"
        print()
        print()
        print(self.essais)
        if cache == self.ortho:
            return False
        else:
            return True

    def proposition(self):
        print("Quelle lettre pense-tu qu'il y ai dans le mot que ton pote a choisi ?")
        lettre = input()
        print()
        if lettre not in self.ortho:
            self.fautes += 1
        if lettre not in self.essais:
            self.essais.append(lettre)

    def pendu(self):
        if self.fautes == 0:
            print("")
        elif self.fautes == 1:
            print("")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 2:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 3:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 4:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 5:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |       / \\")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 6:
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
            print(self.ortho)
            print()
            print("Eh, t'as perdu.")
            return False
        print()
        return True


print()
print()
print("Bonjour et bienvenu dans ce programme modélsant un pendu")
print("Choisissez un joueur qui devra me donner un mot/phrase ou mot composé, pour que je le fasse deviner à l'autre")
print("Ton message ne doit juste pas contenir de chiffres et pas d'accents")

winning = True
mot_a_deviner = Mot(input("Quel est ton expression ? "))
for i in range(50):
    print()

while winning:
    winning = mot_a_deviner.mot_cache()
    if not winning:
        break
    mot_a_deviner.proposition()
    winning = mot_a_deviner.pendu()
