# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:38:48 2019

@author: 33762
"""




def coup_legaux(pièce,pos):
    """
    """
    x=pos[0]
    y=pos[1]
    x_max=8
    y_max=8
    res=[]
    if pièce == 'pion': #Retourner les différents coups légaux pour un pion
        """
        il suffit de faire x+1 (attention cela n'est pas vrai pour l'ouverture)
        """
        return [x+1,y]
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
                if coordx <= 8 and coordy <= 8 and coordx >= 0 and coordy >= 0:
                    res.append([coordx,coordy])
        return res
    if pièce == 'fou': #Retourner les différents coups légaux pour un fou
        pass
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
        pass 
        

print(coup_legaux('cavalier',[0,0]))

    
