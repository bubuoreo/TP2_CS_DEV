# BURLOT Alexandre
# GAUD Romain
# 01/12/2020
# subject : Faire un pendu ave une interface graphique Tkinter et un choix de mot dans un fichier.
# TODO : 
# - interface graphique avec Tkinter
# Problèmes
# - le dessin n'apparait pas, pas eu assez de temps
# - le mot et la liste des essayes ne se mettent pas à jours
# - si depuis la fenetre on clique sur rejouer, la fenetre se met a jour.

import random
import time as time
from tkinter import Tk, Label, Button, Entry, StringVar


class Mot():
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
            self.__winning = self.motCache()
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

    def getOrtho(self):
        return self.__ortho
    
    def getEssais(self):
        return self.__essais

    def motCache(self):
        cache = ''
        for lettre in self.__ortho:
            if lettre in self.__essais:
                print(' ' + lettre, end='')
                cache += lettre
            else:
                print(" _", end='')
                cache += "_"
        # print()
        # print()
        # print(self.__essais)
        if cache == self.__ortho:
            print("Bravo, tu as gagné")
            return (False, cache)
        else:
            return (True, cache)

    def proposition(self):
        #print("trouve une lettre du mot")
        lettre = input()
        #print()
        if lettre in self.__essais:
            # print("Vous avez déja proposé cette lettre. Veuillez réessayer.")
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
        self.__word = Mot()
        self.__mainSize = "400x300"
        self.__gameSize = "400x300"
        self.__ortho = self.__word.getOrtho()
        self.__winning = True
        self.__essais = self.__word.getEssais()
        self.__fautes = 0
        self.__auth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','é','è','î','ê','û','ë','ô',]

    def playMain(self):
        self.__main = Tk()
        self.__main.geometry(self.__mainSize)
        welcomeLabel = Label(self.__main,text = "Bonjour et bienvenu dans un jeu de pendu", fg = "blue")
        welcomeLabel.pack()
        buttonQuit1 = Button(self.__main, text = "Quitter", fg = "red", command = self.__main.destroy)
        buttonQuit1.pack()
        buttonPlay = Button(self.__main, text="Jouer", command = lambda:[self.__main.destroy(),self.playGame()])
        buttonPlay.pack()
        
        self.__main.mainloop()
    
    def Verification(self):
        if self.__champ1.get() in self.__auth:
            if self.__champ1.get() not in self.__essais:
                self.__essais.append(self.__champ1.get())
            if self.__champ1.get() in self.__essais:
                errorMsg = Label(self.__game, text = "Vous ne devez entrer qu'une seule lettre")
            if self.__champ1.get() not in self.__ortho:
                self.__fautes += 1
            
        else:
            errorMsg = Label(self.__game, text = "Vous ne devez entrer qu'une seule lettre")
            errorMsg.pack()


    def playGame(self):
        while self.__winning:
        self.__game = Tk()
        self.__game.geometry(self.__gameSize)
        
        self.__winning,self.__cache = self.__word.motCache()
        self.__essais = self.__word.getEssais()
        motTiret = Label(self.__game, text = self.__cache)
        motTiret['text'] = self.__cache
        motTiret.pack()
        if not self.__winning:
            victoryMsg = Label(self.__game, text = "Bravo vous avez gagné")
            victoryMsg.pack()

        self.__champ1 = Entry(self.__game, text = "coucou", fg ="black")
        self.__champ1.pack()
        tryButton = Button(self.__game, text = "Proposer", fg = "green", command = self.Verification)
        tryButton.pack()
        
        listeMots = Label(self.__game,text = self.__essais)
        listeMots.pack()
        if self.__fautes == 8:
            losingMsg = Label(self.__game, text = "Vous avez perdu")
            losingMsg.pack()
        
        replayButton = Button(self.__game, text = "rejouer", command = lambda:[self.__game.destroy(),self.playGame()])
        replayButton.pack()
        buttonQuit3 = Button(self.__game, text = "Quitter", fg = "red", command = self.__game.destroy)
        buttonQuit3.pack()
        self.__game.mainloop()

jeu = GUI()
jeu.playMain()


# print("Bonjour et bienvenu dans ce programme modélsant un pendu")
# print()
# print()
