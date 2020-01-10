# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:57:54 2020

@author: 33699
"""
import random
import moteur_blocage as mb
import echiquier as ech


def ia_white_select_dep(echiquier):
    """
    random chess engine that plays which returns the chosen starting pawn 
    and the movement made
    ia_select_dep([List[List[String]])
    return---> ([int, int], [int, int])
    return---> ([x_départ, y_départ], [x_arrive,y_arrive])
    """
    pos_dep=[random.randint(0,7),random.randint(0,7)]
    

    if echiquier[pos_dep[1]][pos_dep[0]] == "**" or echiquier[pos_dep[1]][pos_dep[0]][1]!="b":
        return ia_white_select_dep(echiquier)
    else:
        if echiquier[pos_dep[1]][pos_dep[0]][0]=="P":#if it is a bishop
            if mb.coups_possibles_pion(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_pion(pos_dep,echiquier,"Blanc")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="T":#if it is a bishop
            if mb.coups_possibles_tour(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_tour(pos_dep,echiquier,"Blanc")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="F":#if it is a bishop
            if mb.coups_possibles_fou(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_fou(pos_dep,echiquier,"Blanc")),pos_dep
            
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="D":#if it is a bishop
            if mb.coups_possibles_dame(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_dame(pos_dep,echiquier,"Blanc")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="R":#if it is a bishop
            if mb.coups_possibles_roi(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_roi(pos_dep,echiquier,"Blanc")),pos_dep
        
        elif echiquier[pos_dep[1]][pos_dep[0]][0]=="C":#if it is a bishop
            if mb.coups_possibles_cavalier(pos_dep,echiquier,"Blanc")==[]:
                return ia_white_select_dep(echiquier)
            else:#we make a random choice in the possibilities 
                return random.choice(mb.coups_possibles_cavalier(pos_dep,echiquier,"Blanc")),pos_dep
            
        

def deplacement_ia_white(echiquier):
    """
    move AI pawns and return the chessboard
    deplacement_ia([List[List[String]]))
    return ---> [List[List[String]]
    
    """
    print("BLANC :")
    selected=ia_white_select_dep(echiquier)
    print("depart : "+str(selected[1][0])+","+str(selected[1][1]))
    print("arrivee : "+str(selected[0][0])+","+str(selected[0][1]))
    ech.deplacement(echiquier,selected[1][0],selected[1][1],selected[0][0],selected[0][1])
    return echiquier

#ici j'ai regler le problème en fait le selected[1] = depart et le 0 = arrivée


