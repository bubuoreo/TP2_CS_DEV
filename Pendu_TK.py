# BURLOT Alexandre
# GAUD Romain
# 01/12/2020
# subject : Faire un pendu ave une interface graphique Tkinter et un choix de mot dans un fichier.
# TODO : 
# - interface graphique avec Tkinter
# - 

import random
from tkinter import Tk, Label, Button


class Mot:
    def __init__(self):
        with open("Dico.txt","r",encoding="latin-1") as Dico :
            liste = Dico.readlines()
            i = random.randint(0,len(liste)-1)
            mot = liste[i]
            mot = mot.rstrip("\n")
        mot = mot.lower()
        self.__ortho = mot
        self.__taille = len(self.__ortho)
        self.__essais = []
        self.__fautes = 0
        self.__winning = True
        self.__essais.append(self.__ortho[0])
        # self.play()

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


class GUI(Mot):
    def __init__(self):
        self.__mainSize = "400x300"
        self.__gameSize = "200x100"
        self.__replaySize = "500x500"

    def playMain(self):
        self.__main = Tk()
        self.__main.geometry(self.__mainSize)
        welcomeLabel = Label(self.__main,text = "Bonjour et bienvenu dans un jeu de pendu", fg = "blue")
        welcomeLabel.pack()
        buttonQuit1 = Button(self.__main, text = "Quitter", fg = "red", command = self.__main.destroy)
        buttonQuit1.pack()
        buttonPlay = Button(self.__main, text="Jouer", command = lambda:[self.__main.destroy(),self.playReplay(),]) # Changer cette fct par la fct jeu
        buttonPlay.pack()
        
        self.__main.mainloop()
    
    # def playGame(self):
        # tryButton = Button(self.__game, text = "Proposer", fg = "green", command = "FONCTION") # une fonction à appeler qui fera le jeu

    def playReplay(self):
        self.__replay = Tk()
        buttonQuit3 = Button(self.__replay, text = "Quitter", fg = "red", command = self.__replay.destroy)
        buttonQuit3.pack()
        replayButton = Button(self.__replay, text = "rejouer") #command = self.playGame) à faire apres que la fonction jeu soit ok
        replayButton.pack()
        self.__replay.mainloop()



jeu = GUI()
jeu.playMain()


# print("Bonjour et bienvenu dans ce programme modélsant un pendu")
# print()
# print()
# mot_a_deviner = Mot()