# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:37:18 2019

@author: 33762
"""

#FOU
def monterGauche(pos):#WORK
    #x=x-1
    #y=y-1
    res=[]
    x=pos[0]
    y=pos[1]
    while x > 0 and y > 0 :
        x=x-1
        y=y-1
        res.append([x,y])
    return res

def monterDroite(pos):#WORK
    #x=x+1
    #y=y-1
    res=[]
    x=pos[0]
    y=pos[1]
    while x < 7  and y > 0 :
        x=x+1
        y=y-1
        res.append([x,y])
    return res

def decendreDroite(pos):#WORK
    #x=x+1
    #y=y+1
    res=[]
    x=pos[0]
    y=pos[1]
    while x < 7  and y < 7 :
        x=x+1
        y=y+1
        res.append([x,y])
    return res

def decendreGauche(pos):#WORK
    #x=x-1
    #y=y+1
    res=[]
    x=pos[0]
    y=pos[1]
    while x > 0  and y < 7 :
        x=x-1
        y=y+1
        res.append([x,y])
    return res


