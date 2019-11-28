# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:13:20 2019

@author: 33762

Pour la représentation on a choisi de commencer avec quelque chose de simple
"""
import moteur_coups_legaux8_8 as mcl


def affichage(echiquier):
    """
    affichage(List[List[String]])
    -> return None
    
    affiche l'échiquier dans la console python 
    en donnant les différentes lignes de haut en bas en paramètre
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
    """
    x=pos[0]
    y=pos[1]
    return echiquier[y][x] 

def get_Couleur(pos,echiquier):
    """
    get_Couleur(List[int,int],List[List[String]])
    -> return string
    
    retourne la couleur d'une pièce en donnant les coord. de celle-ci'
    """
    x=pos[0]
    y=pos[1]
    if 'n' in get_Piece([x,y],echiquier):
        return 'Noir'
    else :
        return 'Blanc'
    

def get_Coups(pos,echiquier):
    """
    get_Coups(List[int,int],List[List[String]])
    -> return List
    
    retourne tous les coups d'un piece en donnant les coord. de celle-ci 
    ATTENTION : ne gère pas les collisions et les blocages
    """
    x=pos[0]
    y=pos[1]
    piece=''
    couleur = get_Couleur([x,y],echiquier)
    if couleur == 'Noir' :
        place_dispo=get_placesDispo_Noirs(echiquier)
    else : 
        place_dispo=get_placesDispo_Blancs(echiquier)
    if get_Piece([x,y],echiquier) == 'Pn' or get_Piece([x,y],echiquier) == 'Pb':
        piece='pion'
    elif get_Piece([x,y],echiquier) == 'Tn' or get_Piece([x,y],echiquier) == 'Tb':   
        piece='tour'
    elif get_Piece([x,y],echiquier) == 'Cn' or get_Piece([x,y],echiquier) == 'Cb':   
        piece='cavalier'
    elif get_Piece([x,y],echiquier) == 'Fn' or get_Piece([x,y],echiquier) == 'Fb':   
        piece='fou'
    elif get_Piece([x,y],echiquier) == 'Rn' or get_Piece([x,y],echiquier) == 'Rb':   
        piece='roi'
    elif get_Piece([x,y],echiquier) == 'Dn' or get_Piece([x,y],echiquier) == 'Db':   
        piece='dame'
    print(piece)
    if piece!='' :
        inter = [value for value in mcl.coup_legaux(piece,[x,y],couleur) if value in place_dispo] 
        return inter
    else :
        return None

def get_placesDispo_Blancs(echiquier):
    """
    get_placeDispoBlancs(List[List[String]])
    -> return List
    
    Cette fonction retourne toutes les places libres pour les blancs
    on considérant les places occupés par les noirs comme disponibles 
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
    """
    res=[]
    noirs=['Pn','Tn','Cn','Fn','Rn','Dn']
    for i in range(0,len(echiquier)):
        for j in range(0,len(echiquier[i])):
            if echiquier[i][j] not in noirs:
                res.append([j,i])
    return res
