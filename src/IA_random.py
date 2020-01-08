# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:57:54 2020

@author: 33699
"""
import random
import moteur_blocage as mb

a=['Tn','Cn','Fn','Dn','Rn','Fn','Cn','Tn']
z=['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn']
e=['**','**','**','**','**','**','**','**']
r=['**','**','**','**','**','**','**','**']
t=['**','**','**','**','**','**','**','**']
y=['**','**','**','**','**','**','**','**']
u=['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb']
i=['Tb','Cb','Fb','Db','Rb','Fb','Cb','Tb']
echiquier=[a,z,e,r,t,y,u,i]

random.choice(a)
random.randint(0,7)

def ia_select_dep():
    """
    moteur de jeux d'echec random qui joue  qui retourne le pion de départ
    choisi et le mouvement effectué
    return---> ([int, int], [int, int])
    return---> ([x_départ, y_départ], [x_arrivée,y_arrivée])
    
                  
    
    """
    pos_dep=[random.randint(0,7),random.randint(0,7)]
    
    if echiquier[pos_dep[1]][pos_dep[0]] == "**" or echiquier[pos_dep[1]][pos_dep[0]][1]!="n":
        return ia_select_dep()
    else:
        if echiquier[pos_dep[1]][pos_dep[0]][0]!="P":
            if mb.coups_possibles_pion(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_pion(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]!="T":
            if mb.coups_possibles_tour(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_tour(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]!="F":
            if mb.coups_possibles_fou(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_fou(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]!="D":
            if mb.coups_possibles_dame(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_dame(pos_dep,echiquier,"Noir")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]!="R":
            if mb.coups_possibles_roi(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_roi(pos_dep,echiquier,"Noir")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]!="C":
            if mb.coups_possibles_cavalier(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep()
            else:
                return random.choice(mb.coups_possibles_cavalier(pos_dep,echiquier,"Noir")),pos_dep
            
    
    
    
print(ia_select_dep()[0])



