# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:57:54 2020

@author: 33699
"""
import random
import moteur_blocage as mb
import echiquier as ech


def ia_select_dep(echiquier):
    """
    moteur de jeux d'echec random qui joue  qui retourne le pion de départ
    choisi et le mouvement effectué
    return---> ([int, int], [int, int])
    return---> ([x_départ, y_départ], [x_arrivée,y_arrivée])
    
                  
    
    """
    pos_dep=[random.randint(0,7),random.randint(0,7)]
    
    if echiquier[pos_dep[1]][pos_dep[0]] == "**" or echiquier[pos_dep[1]][pos_dep[0]][1]!="n":
        return ia_select_dep(echiquier)
    else:
        if echiquier[pos_dep[1]][pos_dep[0]][0]=="P":
            if mb.coups_possibles_pion(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_pion(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="T":
            if mb.coups_possibles_tour(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_tour(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="F":
            if mb.coups_possibles_fou(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_fou(pos_dep,echiquier,"Noir")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="D":
            if mb.coups_possibles_dame(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_dame(pos_dep,echiquier,"Noir")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="R":
            if mb.coups_possibles_roi(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_roi(pos_dep,echiquier,"Noir")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="C":
            if mb.coups_possibles_cavalier(pos_dep,echiquier,"Noir")==[]:
                return ia_select_dep(echiquier)
            else:
                return random.choice(mb.coups_possibles_cavalier(pos_dep,echiquier,"Noir")),pos_dep

 
        

def deplacement_ia(echiquier):
    print("NOIR :")
    selected=ia_select_dep(echiquier)
    print("depart : "+str(selected[1][0])+","+str(selected[1][1]))
    print("arrivee : "+str(selected[0][0])+","+str(selected[0][1]))
    ech.deplacement(echiquier,selected[1][0],selected[1][1],selected[0][0],selected[0][1])
    return echiquier

#ici j'ai regler le problème en fait le selected[1] = depart et le 0 = arrivée


