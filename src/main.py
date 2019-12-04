# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:51:47 2019

@author: 33762
"""

import echiquier as ech
import moteur_blocage as mb
#pieces blanches : Pb Cb Fb Tb Rb Db
#pieces noires : Pn Cn Fn Tn Rn Dn

a=['Tn','Cn','Fn','Dn','Rn','Fn','Cn','Tn']
z=['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn']
e=['**','**','**','**','**','**','**','**']
r=['**','**','**','**','**','**','**','**']
t=['**','**','**','**','**','**','**','**']
y=['**','**','**','**','**','**','**','**']
u=['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb']
i=['Tb','Cb','Fb','Db','Rb','Fb','Cb','Tb']


echiquier=[a,z,e,r,t,y,u,i]

ech.affichage(echiquier)
x = int(input("X : "))
y = int(input("y : "))

nom=ech.get_NomPiece([x,y],echiquier)
if nom=='pion' :
    print(mb.coups_possibles_pion([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))
elif nom=='cavalier':
    print(mb.coups_possibles_cavalier([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))
elif nom=='tour':
    print(mb.coups_possibles_tour([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))
elif nom=='fou':
    print(mb.coups_possibles_fou([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))
elif nom=='dame':
    print(mb.coups_possibles_dame([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))    
elif nom=='roi':
    print(mb.coups_possibles_roi([x,y],echiquier,ech.get_Couleur([x,y],echiquier)))
    


