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
    
    Returns if the box whose position is given as a parameter is enemy / ally or empty compared to a color
!!! Returns enemy that if it is badly written mdrrr it is weird !!!
    #WORK mais étrange
    """
    noirs=['Pn','Cn','Fn','Tn','Rn','Dn']
    blancs=['Pb','Cb','Fb','Tb','Rb','Db']
    
    
    if echiquier[pos[1]][pos[0]] in noirs:
        if couleur == 'Noir':
            return 'Allier'
    if echiquier[pos[1]][pos[0]] in blancs:
        if couleur == 'Blanc':
            return 'Allier'
    elif echiquier[pos[1]][pos[0]] == '**':
        return 'Vide'
    elif echiquier[pos[1]][pos[0]] != '':
        return 'Ennemi'

def coups_possibles_tour(pos,echiquier,couleur):
    """
    coups_possibles_tour(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    returns all possible moves for a tower in a specific position and chessboard
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
    
    returns all possible moves for a bishop in a precise position and chessboard
     #work
   
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
    #movedown bishop
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
    #move right bishop
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
    #move left bishop
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
    
    returns all possible moves for a queen in a specific position and chessboard
     We consider that the queen moves like bishop + a rook
     #work
    """
    return coups_possibles_fou(pos,echiquier,couleur)+coups_possibles_tour(pos,echiquier,couleur)

def coups_possibles_cavalier(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
    return all possibilities for the knight in a specific position
    #WORK
    """
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    for i,j in [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]: #for each knight possibilities 
                coordx=x+i
                coordy=y+j
                if coordx <= 7 and coordy <= 7 and coordx >= 0 and coordy >= 0: #if the movement does not bring the piece out of the chessboard
                    coups.append([coordx,coordy]) #then we add it to the list of theoretically possible moves
    for coup in coups: #For each move in the list of theoretically possible moves
        if place_dispo(coup,echiquier,couleur) != 'Allier': #if there is no ally on the square
            res.append(coup) #then this move is valid so we add it to the list
            
    return res

def coups_possibles_roi(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
   returns all possible moves for a king in a specific position and chessboard
    """
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    for i in [-1,0,1]:
            for j in [-1,0,1]:
                coordx=x+i
                coordy=y+j
                if coordx <= 8 and coordy <= 8 and coordx >= 0 and coordy >= 0:
                    coups.append([coordx,coordy])
    for coup in coups: #For each move in the list of theoretically possible moves
        if place_dispo(coup,echiquier,couleur) != 'Allier': #if there is no ally on the square
            res.append(coup) #then this move is valid so we add it to the list
    return res
  
def coups_possibles_pion(pos,echiquier,couleur):
    """
    coups_possibles_cavalier(List[int,int],List[List[String]],List[List[int,int]],string)
    return -> List[List[int,int]]
    
       returns all possible moves for a king in a specific position and chessboard

    """   
    x=pos[0]
    y=pos[1]
    coups=[]
    res=[]
    if couleur == 'Blanc':
        coups.append([x,y-1])
        if y == 6 and place_dispo([x,y-1],echiquier,couleur) == 'Vide': #If the pawn is in its initial position and it is not blocking then it can advance two spaces
            coups.append([x,y-2])
        for coup in coups:
            if place_dispo(coup,echiquier,couleur) == 'Vide': #the pawn can only eat diagonally, that's why the box must be empty
                res.append(coup)
        #If an enemy is on the nearest diagonal square then he can eat him
        if x!=7:
            if place_dispo([x+1,y-1],echiquier,couleur) == 'Ennemi':
                res.append([x+1,y-1])
        if x!=0:
            if place_dispo([x-1,y-1],echiquier,couleur) == 'Ennemi':
                res.append([x-1,y-1])
    else : #if it is black
        coups.append([x,y+1])
        if y == 1 and place_dispo([x,y+1],echiquier,couleur) == 'Vide': #If the pawn is in its initial position and it is not blocking then it can advance two square
            coups.append([x,y+2])
        for coup in coups:
            if place_dispo(coup,echiquier,couleur) == 'Vide': #the pawn can only eat diagonally, that's why the box must be empty
                res.append(coup)
        #If an enemy is on the nearest diagonal square then he can eat it
        if x!=7:
            if place_dispo([x+1,y+1],echiquier,couleur) == 'Ennemi':
                res.append([x+1,y+1])
        if x!=0:
            if place_dispo([x-1,y+1],echiquier,couleur) == 'Ennemi':
                res.append([x-1,y+1])
    return res
    
    
