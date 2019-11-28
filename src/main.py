# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:51:47 2019

@author: 33762
"""

import moteur_coups_legaux8_8 as mcl
import echiquier as ech
import moteur_blocage as mb
#pieces blanches : Pb Cb Fb Tb Rb Db
#pieces noires : Pn Cn Fn Tn Rn Dn

a=['**','**','**','**','**','**','**','**']
z=['**','**','**','**','**','**','**','**']
e=['**','**','**','**','**','**','**','**']
r=['**','**','**','**','**','**','**','**']
t=['**','**','**','Tn','**','**','**','**']
y=['**','**','**','**','**','**','**','**']
u=['**','**','**','**','**','**','**','**']
i=['**','**','**','**','**','**','**','**']
echiquier=[a,z,e,r,t,y,u,i]

ech.affichage(echiquier)
pos=[3,4]

#print('Ses déplacements : '+str(ech.get_Coups(pos,echiquier)))

#print(ech.get_Piece([0,0],echiquier))