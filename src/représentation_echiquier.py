# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:13:20 2019

@author: 33762

Pour la représentation on a choisi de commencer avec quelque chose de simple
"""
import moteur_coups_legaux as mpl

a=['Tn','Cn','Fn','Rn','Dn','Fn','Cn','Tn']
z=['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn']
e=['**','**','**','**','**','**','**','**']
r=['**','**','**','**','**','**','**','**']
t=['**','**','**','**','**','**','**','**']
y=['**','**','**','**','**','**','**','**']
u=['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb']
i=['Tb','Cb','Fb','Rb','Db','Fb','Cb','Tb']
echiquier=[a,z,e,r,t,y,u,i]

def get_Echiquier():
    return echiquier

def affichage(a,z,e,r,t,y,u,i):
    """
    affichage(List,List,List,List,List,List,List,List)
    -> return None
    
    affiche l'échiquier dans la console python 
    en donnant les différentes lignes de haut en bas en paramètre
    """
    c=['0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ']
    tab=[a,z,e,r,t,y,u,i]
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

def get_Piece(x,y):
    """
    get_Piece(int,int)
    -> return string
    
    renvoie la pièce qui est sur la position donnée en paramètre 
    """
    return echiquier[y][x] 


def get_Coups(x,y):
    """
    get_Coups(int,int)
    -> return List
    
    retourne tous les coups d'un piece en donnant les coord. de celle-ci 
    ATTENTION : ne gère pas les collisions et les blocages
    """
    piece=''
    if 'n' in get_Piece(x,y) :
        place_dispo=get_placesDispo_Noirs()
    else : 
        place_dispo=get_placesDispo_Blancs()
    if get_Piece(x,y) == 'Pn' or get_Piece(x,y) == 'Pb':
        piece='pion'
    elif get_Piece(x,y) == 'Tn' or get_Piece(x,y) == 'Tb':   
        piece='tour'
    elif get_Piece(x,y) == 'Cn' or get_Piece(x,y) == 'Cb':   
        piece='cavalier'
    elif get_Piece(x,y) == 'Fn' or get_Piece(x,y) == 'Fb':   
        piece='fou'
    elif get_Piece(x,y) == 'Rn' or get_Piece(x,y) == 'Rb':   
        piece='roi'
    elif get_Piece(x,y) == 'Dn' or get_Piece(x,y) == 'Db':   
        piece='dame'
    if piece!='' :
        inter = [value for value in mpl.coup_legaux(piece,[x,y]) if value in place_dispo] 
        return inter
    else :
        return None

def get_placesDispo_Blancs():
    """
    get_placeDispoBlancs()
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

def get_placesDispo_Noirs():
    """
    get_placesDispo_Noirs()
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


affichage(a,z,e,r,t,y,u,i)
print(get_Coups(7,7))