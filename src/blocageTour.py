# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:03:44 2019

@author: 33762
"""

#TOUR
def monter(pos): #WORK
    #x = same 
    #y-1
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(y-1,-1,-1):
        res.append([x,i])
    return res

def descendre(pos): #WORK
    #x = same 
    #y+1
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(y+1,8):
        res.append([x,i])
    return res

def droite(pos): #WORK
    #x+1
    #y = same
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(x+1,8):
        res.append([i,y])
    return res

def gauche(pos): #WORK
    #x-1
    #y = same
    x=pos[0]
    y=pos[1]
    res=[]
    for i in range(x-1,-1,-1):
        res.append([i,y])
    return res
