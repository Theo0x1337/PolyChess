# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:51:47 2019

@author: 33762
"""

import echiquier as ech
import apiSyzygy as api
import IA_random as ia
import IA_white_random as iaWhite
import time


def IaVsIa():
    """
    function that start a game between two AI
    """
    finPartie = False
    echiquier=ech.initialiseEchiquier()
    while finPartie == False:
        
        print("")
        print("----------------")
        print("")
        print("Au tour de l'ordinateur 1")
        print("")
        print("----------------")
        
        ech.affichage(echiquier)
        iaWhite.deplacement_ia_white(echiquier)
        ech.affichage(echiquier)
        time.sleep(1)
        FEN = ech.generatorFEN(echiquier)
        finPartie = api.testFDP(FEN,'w')[0]
        
        print("")
        print("----------------")
        print("")
        print("Au tour de l'ordinateur 2")
        print("")
        print("----------------")
        
        if finPartie == False:
            ia.deplacement_ia(echiquier)
            ech.affichage(echiquier)
            time.sleep(1)
            FEN = ech.generatorFEN(echiquier)
            reponse = api.testFDP(FEN,'b')
            finPartie = reponse[0]
            if finPartie == True:
                print("")
                print("----------------")
                print("")
                couleur = reponse[1]
                if couleur == "w":
                    gagnants = "noirs"
                else :
                    gagnants = "blancs"
                print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
                print("")
                fin_de_partie=input("Appuyer pour quitter ...")
        else:
            print("")
            print("----------------")
            print("")
            couleur = reponse[1]
            if couleur == "w":
                gagnants = "noirs"
            else :
                gagnants = "blancs"
            print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
            print("")
            fin_de_partie=input("Appuyer pour quitter ...")
        
def PlayerVsIa(): 
    """
    function that start a game between a player and an AI
    """
    finPartie = False
    echiquier=ech.initialiseEchiquier()
    while finPartie == False:
        
        print("")
        print("----------------")
        print("")
        print("Au tour du joueur")
        print("")
        print("----------------")
        
        ech.affichage(echiquier)
        ech.choisiDeplacement(echiquier)
        FEN = ech.generatorFEN(echiquier)
        finPartie = api.testFDP(FEN,'w')[0]
        
        print("")
        print("----------------")
        print("")
        print("Au tour de l'ordinateur")
        print("")
        print("----------------")
        
        if finPartie == False:
            ia.deplacement_ia(echiquier)
            ech.affichage(echiquier)
            time.sleep(1)
            FEN = ech.generatorFEN(echiquier)
            reponse = api.testFDP(FEN,'b')
            finPartie = reponse[0]
            if finPartie == True:
                print("")
                print("----------------")
                print("")
                couleur = reponse[1]
                if couleur == "w":
                    gagnants = "noirs"
                else :
                    gagnants = "blancs"
                print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
                print("")
                fin_de_partie=input("Appuyer pour quitter ...")
        else:
            print("")
            print("----------------")
            print("")
            couleur = reponse[1]
            if couleur == "w":
                gagnants = "noirs"
            else :
                gagnants = "blancs"
            print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
            print("")
            fin_de_partie=input("Appuyer pour quitter ...")

            
def PlayerVsPlayer():
    """
    function that start a game between two player
    """
    finPartie = False
    echiquier=ech.initialiseEchiquier()
    while finPartie == False:
        
        print("")
        print("----------------")
        print("")
        print("Au tour du joueur 1")
        print("")
        print("----------------")
        
        ech.affichage(echiquier)
        ech.choisiDeplacement(echiquier)
        FEN = ech.generatorFEN(echiquier)
        finPartie = api.testFDP(FEN,'w')[0]
        
        print("")
        print("----------------")
        print("")
        print("Au tour du joueur 2")
        print("")
        print("----------------")
        
        if finPartie == False:
            ech.affichage(echiquier)
            ech.choisiDeplacement(echiquier)
            FEN = ech.generatorFEN(echiquier)      
            reponse = api.testFDP(FEN,'b')
            finPartie = reponse[0]
            if finPartie == True:
                print("")
                print("----------------")
                print("")
                couleur = reponse[1]
                if couleur == "w":
                    gagnants = "noirs"
                else :
                    gagnants = "blancs"
                print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
                print("")
                fin_de_partie=input("Appuyer pour quitter ...")
        else:
            print("")
            print("----------------")
            print("")
            couleur = reponse[1]
            if couleur == "w":
                gagnants = "noirs"
            else :
                gagnants = "blancs"
            print("La partie est finie ! il y a echec et mat ! Les "+gagnants+" ont gagné !")
            print("")
            fin_de_partie=input("Appuyer pour quitter ...")
