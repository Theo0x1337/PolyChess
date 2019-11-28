# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:39:36 2019

@author: 33762
"""

def coups_possibles(pos,piece,echiquier,coups_legaux,couleur):
    pass


def place_dispo(pos,echiquier,couleur):
    """
    place_dispo(List[int,int],List[List[String]],String)
    -> return String
    
    Retourne si la case dont la position est donné en paramètre est ennemi/allier ou vide par rapport à une couleur
    WORK
    """
    noirs=['Pn','Cn','Fn','Tn','Rn','Dn']
    if echiquier[pos[1]][pos[0]] in noirs:
        if couleur == 'Noir':
            return 'Allier'
    elif echiquier[pos[1]][pos[0]] == '**':
        return 'Vide'
    else :
        return 'Ennemi'
            
