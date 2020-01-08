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

while finPartie == False:

    echiquier=ech.initialiseEchiquier()
    ech.affichage(echiquier)
    ech.choisiDeplacement(echiquier)
    FEN = ech.generatorFEN(echiquier)
    finPartie = print(api.testFDP(FEN))
    
    if finPartie == False:
        ia.deplacement_ia(echiquier)
        ech.affichage(echiquier)
        FEN = ech.generatorFEN(echiquier)
        finPartie = print(api.testFDP(FEN))
        
    

