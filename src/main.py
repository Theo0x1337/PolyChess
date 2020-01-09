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
#pieces blanches : Pb Cb Fb Tb Rb Db
#pieces noires : Pn Cn Fn Tn Rn Dn


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
    iaWhite.deplacement_ia_white(echiquier)
    ech.affichage(echiquier)
    time.sleep(1)
    #ech.choisiDeplacement(echiquier)
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
        
    

#!!! un pion a mangé son allié !!! erreur à corrigé 
# on peut maintenant ajouter la couleur au FEN 