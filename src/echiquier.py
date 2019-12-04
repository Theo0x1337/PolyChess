# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:13:20 2019

@author: 33762

Pour la représentation on a choisi de commencer avec quelque chose de simple
"""


def affichage(echiquier):
    """
    affichage(List[List[String]])
    -> return None
    
    affiche l'échiquier dans la console python 
    en donnant les différentes lignes de haut en bas en paramètre
    WORK
    """
    c=['0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ']
    tab=['a','z','e','r','t','y','u','i']
    for i in range(0,len(echiquier)):
        tab[i]=echiquier[i]
    premiere_ligne='   '
    trait=' |____|____|____|____|____|____|____|____|'
    for i in range(0,len(c)):
        premiere_ligne=premiere_ligne+c[i]+'   '
    print(premiere_ligne)
    print(trait)
    for i in range(0,len(tab)):
        ligne = str(i)+'| '
        for j in range(0,len(tab)):
            ligne= ligne + tab[i][j] + ' | '
        ligne=ligne
        print(ligne)
        print(trait)

def get_Piece(pos,echiquier):
    """
    get_Piece(List[int,int],List[List[String]])
    -> return string
    
    renvoie la pièce qui est sur la position donnée en paramètre 
    WORK
    """
    x=pos[0]
    y=pos[1]
    return echiquier[y][x] 

def get_NomPiece(pos,echiquier):
    """
    get piece(List[int,int],List[List[String]])
    -> return string 
    
    renvoie le nom de la pièce qui est sur la position donnée en paramètre
    WORK
    """
    piece=get_Piece(pos,echiquier)
    if 'T' in piece :
        return 'tour'
    elif 'C' in piece:
        return 'cavalier'
    elif 'F' in piece:
        return 'fou'
    elif 'D' in piece:
        return 'dame'
    elif 'P' in piece:
        return 'pion'
    elif 'R' in piece:
        return 'roi'

def get_Couleur(pos,echiquier):
    """
    get_Couleur(List[int,int],List[List[String]])
    -> return string
    
    retourne la couleur d'une pièce en donnant les coord. de celle-ci'
    WORK
    """
    x=pos[0]
    y=pos[1]
    if 'n' in get_Piece([x,y],echiquier):
        return 'Noir'
    else :
        return 'Blanc'
    

def get_placesDispo_Blancs(echiquier):
    """
    get_placeDispoBlancs(List[List[String]])
    -> return List
    
    Cette fonction retourne toutes les places libres pour les blancs
    on considérant les places occupés par les noirs comme disponibles 
    WORK
    """
    res=[]
    blancs=['Pb','Tb','Cb','Fb','Rb','Db']
    for i in range(0,len(echiquier)):
        for j in range(0,len(echiquier[i])):
            if echiquier[i][j] not in blancs:
                res.append([j,i])
    return res

def get_placesDispo_Noirs(echiquier):
    """
    get_placesDispo_Noirs(List[List[String]])
    -> return List
    
    Cette fonction retourne toutes les places libres pour les noirs
    on considérant les places occupés par les blancs comme disponibles 
    WORK
    """
    res=[]
    noirs=['Pn','Tn','Cn','Fn','Rn','Dn']
    for i in range(0,len(echiquier)):
        for j in range(0,len(echiquier[i])):
            if echiquier[i][j] not in noirs:
                res.append([j,i])
    return res
