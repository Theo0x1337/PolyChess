# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:38:48 2019

@author: 33762
"""
 

def coup_legaux(pièce,pos,couleur):
    """
    coup_legaux(string,list[int,int],string)
    ->return list[list[int,int]]
    
    pour chaque pièce et ses coord. on renvoie les différentes coups légaux sans prendre en compte les blocages
    la couleur est utile pour les pions en effet ce sont les seuls pièces dont le deplacement est différent en fonction de la couleur de celle-ci
    """
    x=pos[0]
    y=pos[1]
    x_max=8
    y_max=8
    res=[]
    if pièce == 'pion': #Retourner les différents coups légaux pour un pion
        """
        il suffit de faire y+1 (attention cela n'est pas vrai pour l'ouverture )
        """
        if couleur == 'Noir' and y<=6: 
            res.append([x,y+1])
        elif couleur == 'Blanc' and y>=1: 
            res.append([x,y-1])
        return res
    if pièce == 'tour': #Retourner les différents coups légaux pour une tour
        """
        On retourne toute les coord. de toute la ligne et de toute la colonne de la pos actuelle de la tour
        """
        for i in range(0,y_max):
            res.append([x,i])
            res.append([i,y])
        return res
    if pièce == 'cavalier': #Retourner les différents coups légaux pour un cavalier
        """
        On retourne les différentes possibilités pour un cavalier en vérifiant qu'on ne sorte pas de l'échiquier
        """
        for i,j in [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]:
                coordx=x+i
                coordy=y+j
                if coordx <= x_max and coordy <= y_max and coordx >= 0 and coordy >= 0:
                    res.append([coordx,coordy])
        return res
    if pièce == 'fou': #Retourner les différents coups légaux pour un fou
        """
        On divise ces deplacement en 4 parties (monter à droite, descendre à droite, monter à gauche, descendre à gauche)
        """
        #monter à gauche
        coordx=x
        coordy=y
        while coordx < x_max-1 and coordy < y_max-1 :
            coordx=coordx+1
            coordy=coordy+1
            res.append([coordx,coordy])
        
        #descendre à droite
        coordx=x
        coordy=y
        while coordx < x_max-1 and coordy > 0 :
            coordx=coordx+1
            coordy=coordy-1
            res.append([coordx,coordy])
        
        #monter à gauche
        coordx=x
        coordy=y
        while coordx > 0  and coordy < y_max-1 :
            coordx=coordx-1
            coordy=coordy+1
            res.append([coordx,coordy])
            
        #decendre à gauche
        coordx=x
        coordy=y
        while coordx > 0  and coordy > 0 :
            coordx=coordx-1
            coordy=coordy-1
            res.append([coordx,coordy])
        
        return res
        
    
    if pièce == 'dame': #Retourner les différents coups légaux pour une dame
        """
        On retourne les différentes possibilités pour une dame en vérifiant qu'on ne sorte pas de l'échiquier
        """
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                coordx=x+i
                coordy=y+j
                if coordx <= 8 and coordy <= 8 and coordx >= 0 and coordy >= 0:
                    res.append([coordx,coordy])
        return res
    if pièce == 'roi': #Retourner les différents coups légaux pour un roi
        """
        On considère que le roi se déplace comme une tour + un fou
        """
        return coup_legaux('fou',[x,y])+coup_legaux('tour',[x,y])
        


    
