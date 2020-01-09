# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:39:36 2019

@author: 33762
"""
import blocageTour as bT
import blocageFou as bF


def place_dispo(pos,echiquier,couleur):
    """
    
    
    place_dispo(List[int,int],List[List[String]],String)
    -> return String

    <FR>    
    Retourne si la case dont la position est donné en paramètre est ennemi/allier ou vide par rapport à une couleur
    
    
    <EN>
    Return if the square which the position is given in parameters is an ennemy or an ally or empty by a color
    
    """
    noirs=['Pn','Cn','Fn','Tn','Rn','Dn']
    blancs=['Pb','Cb','Fb','Tb','Rb','Db']
    
    print(str(pos[1])+":"+str(pos[0]))
    if echiquier[pos[1]][pos[0]] in noirs and pos[1]<8 and pos[0]<8 and pos[1]>=0 and pos[0]>=0:
        if couleur == 'Noir':
            return 'Allier'
    if echiquier[pos[1]][pos[0]] in blancs and pos[1]<8 and pos[0]<8 and pos[1]>=0 and pos[0]>=0:
        if couleur == 'Blanc':
            return 'Allier'
    elif echiquier[pos[1]][pos[0]] == '**' and pos[1]<8 and pos[0]<8 and pos[1]>=0 and pos[0]>=0:
        return 'Vide'
    elif echiquier[pos[1]][pos[0]] != '' and pos[1]<8 and pos[0]<8 and pos[1]>=0 and pos[0]>=0:
        return 'Ennemi'

def coups_possibles_tour(pos,echiquier,couleur):
    """
    coups_possibles_tour(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour une tour dans un position et un echiquier précis
    #WORK
    
    <EN>
    return every chess move possible for a ROOK in a position and a chessboard
    
    """
    res=[]
    #Déplacement en bas de la tour
    coups_bas=bT.descendre(pos)
    for coup in coups_bas:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement en haut de la tour
    coups_haut=bT.monter(pos)
    for coup in coups_haut:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement à droite de la tour
    coups_droite=bT.droite(pos)
    for coup in coups_droite:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement à gauche de la tour
    coups_gauche=bT.gauche(pos)
    for coup in coups_gauche:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
        
    return res


def coups_possibles_fou(pos,echiquier,couleur):
    """
    coups_possibles_fou(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour un fou dans un position et un echiquier précis
    #WORK
    
    <EN>
    return every chess move possible for a BISHOP in a position and a chessboard
    
    
    """
    res=[]
    #Déplacement en bas à droite du fou
    coups_bas_doite=bF.decendreDroite(pos)
    for coup in coups_bas_doite:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement en bas à gauche du fou
    coups_bas_gauche=bF.decendreGauche(pos)
    for coup in coups_bas_gauche:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement en haut à droite du fou
    coups_haut_droite=bF.monterDroite(pos)
    for coup in coups_haut_droite:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
    #Déplacement en haut à gauche du fou
    coups_haut_gauche=bF.monterGauche(pos)
    for coup in coups_haut_gauche:
        if place_dispo(coup,echiquier,couleur) == 'Allier':
            break
        elif place_dispo(coup,echiquier,couleur) == 'Ennemi':
            res.append(coup)
            break
        elif place_dispo(coup,echiquier,couleur) == 'Vide':
            res.append(coup)
        else: 
            break
        
    return res


def coups_possibles_dame(pos,echiquier,couleur):
    """
    coups_possibles_dame(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour une dame dans un position et un echiquier précis
    On considère que la dame se déplace comme un fou + une tour 
    #WORK
    
    <EN>
    return every chess move possible for a QUEEN in a position and a chessboard
    A queen is at the same time a Bishop and a Rook
    """
    
    return coups_possibles_fou(pos,echiquier,couleur)+coups_possibles_tour(pos,echiquier,couleur)

def coups_possibles_cavalier(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour un cavalier dans un position et un echiquier précis
    #WORK
    
    <EN>
    return every chess move possible for a KNIGHT in a position and a chessboard
    
    """
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    for i,j in [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]: #pour chaque possibilités de déplacement d'un cavalier en général
                coordx=x+i
                coordy=y+j
                if coordx <= 7 and coordy <= 7 and coordx >= 0 and coordy >= 0: #si le déplacement ne fait pas sortir la pièce de l'échiquier
                    coups.append([coordx,coordy]) #alors on l'ajoute à la liste des coups théoriquement possibles
    for coup in coups: #Pour chaque coup dans la liste des coups théoriquement possibles
        if place_dispo(coup,echiquier,couleur) != 'Allier': #si il n'y a pas d'allier sur la case
            res.append(coup) #alors ce déplacement est valide donc on l'ajoute à la liste
            
    return res

def coups_possibles_roi(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour un roi dans un position et un echiquier précis
    #WORK
    
    <EN>
    return every chess move possible for a KING in a position and a chessboard
    
    """
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    for i in [-1,0,1]:
            for j in [-1,0,1]:
                coordx=x+i
                coordy=y+j
                if coordx < 8 and coordy < 8 and coordx >= 0 and coordy >= 0:
                    coups.append([coordx,coordy])
    for coup in coups: #Pour chaque coup dans la liste des coups théoriquement possibles
        if place_dispo(coup,echiquier,couleur) != 'Allier': #si il n'y a pas d'allier sur la case
            res.append(coup) #alors ce déplacement est valide donc on l'ajoute à la liste
    return res
  
def coups_possibles_pion(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    <FR>
    retourne tous les coups possibles pour un pion dans un position et un echiquier précis
    #WORK
    
    <EN>
    return every chess move possible for a PAWN in a position and a chessboard
    """   
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    if couleur == 'Blanc':
        coups.append([x,y-1])
        if y == 6 and place_dispo([x,y-1],echiquier,couleur) == 'Vide': #Si le pion est sur sa position initial et qu'il n'est pas bloquer alors il peut avancer de deux cases
            coups.append([x,y-2])
        for coup in coups:
            if place_dispo(coup,echiquier,couleur) == 'Vide': #le pion ne peut manger que en diagonal c'est pour cela que la case doit être vide
                res.append(coup)
        #Si un ennemi se trouve sur la case diagonal la plus proche alors il peut le manger
        if x!=7:
            if place_dispo([x+1,y-1],echiquier,couleur) == 'Ennemi':
                res.append([x+1,y-1])
        if x!=0:
            if place_dispo([x-1,y-1],echiquier,couleur) == 'Ennemi':
                res.append([x-1,y-1])
    else : #Si le pion est noir
        coups.append([x,y+1])
        if y == 1 and place_dispo([x,y+1],echiquier,couleur) == 'Vide': #Si le pion est sur sa position initial et qu'il n'est pas bloquer alors il peut avancer de deux cases 
            coups.append([x,y+2])
        for coup in coups:
            if place_dispo(coup,echiquier,couleur) == 'Vide': #le pion ne peut manger que en diagonal c'est pour cela que la case doit être vide
                res.append(coup)
        #Si un ennemi se trouve sur la case diagonal la plus proche alors il peut le manger
        if x!=7:
            if place_dispo([x+1,y+1],echiquier,couleur) == 'Ennemi':
                res.append([x+1,y+1])
        if x!=0:
            if place_dispo([x-1,y+1],echiquier,couleur) == 'Ennemi':
                res.append([x-1,y+1])
    return res
    
    
