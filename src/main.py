# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:51:47 2019

@author: 33762
"""

import echiquier as ech
import apiSyzygy as api
import IA_random as ia
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
    ech.choisiDeplacement(echiquier)
    FEN = ech.generatorFEN(echiquier)
    finPartie = api.testFDP(FEN)
    
    print("")
    print("----------------")
    print("")
    print("Au tour de l'ordinateur")
    print("")
    print("----------------")
    
    if finPartie == False:
        ia.deplacement_ia(echiquier)
        ech.affichage(echiquier)
        FEN = ech.generatorFEN(echiquier)
        finPartie = api.testFDP(FEN)
    else:
        print("")
        print("----------------")
        print("")
        print("La partie est finie ! il y a echec et mat")
        print("")
        
    

