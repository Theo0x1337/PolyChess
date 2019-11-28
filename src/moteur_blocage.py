# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:39:36 2019

@author: 33762
"""

def coups_possibles(pos,piece,echiquier,coups_legaux,couleur):
    """
    il faut d'abord trier les possibilités de coups du plus près au plus loins de la pièce qu'on veut déplacer
    puis pour chaque possibilité on vérifie la dispo avec place_dispo
        si c'est vide on continue 
        si c'est un ennemie on s'arrete en comptant cette case dans les possibilitées (on le mange)
        si c'est un allier on s'arrete et on ne compte pas la case dans les possibilités
    Astuce : pour fou/tour/roi on divise chaque direction de possibilités
    on retourne cette nouvelle liste des possibilités
    """
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
            
