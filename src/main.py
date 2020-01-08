# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:51:47 2019

@author: 33762
"""

import echiquier as ech

#pieces blanches : Pb Cb Fb Tb Rb Db
#pieces noires : Pn Cn Fn Tn Rn Dn


echiquier=ech.initialiseEchiquier()
ech.affichage(echiquier)
ech.choisiDeplacement(echiquier)
ech.generatorFEN(echiquier)


