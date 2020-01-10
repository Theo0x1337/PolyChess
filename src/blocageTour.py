# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:03:44 2019
@author: 33762
"""

#ROOK
def monter(pos): 
    """
    monter([int,int]) => return [[int,int],...]
    function that returns the upper's positions of a rook
    """
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(y-1,-1,-1):
        res.append([x,i])
    return res

def descendre(pos): 
    """
    descendre([int,int]) => return [[int,int],...]
    function that returns the lower's positions of a rook
    """
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(y+1,8):
        res.append([x,i])
    return res

def droite(pos): 
    """
    droite([int,int]) => return [[int,int],...]
    function that returns the right's positions of a rook
    """
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(x+1,8):
        res.append([i,y])
    return res

def gauche(pos):
    """
    gauche([int,int]) => return [[int,int],...]
    function that returns the left's positions of a rook
    """
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(x-1,-1,-1):
        res.append([i,y])
    return res
