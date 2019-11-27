# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:13:20 2019

@author: 33762

Pour la représentation on a choisi de commencer avec quelque chose de simple
"""

a=['Tb','Cb','Fb','Rb','Db','Fb','Cb','Tb']
z=['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb']
e=['**','**','**','**','**','**','**','**']
r=['**','**','**','**','**','**','**','**']
t=['**','**','**','**','**','**','**','**']
y=['**','**','**','**','**','**','**','**']
u=['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn']
i=['Tn','Cn','Fn','Rn','Dn','Fn','Cn','Tn']

def affichage(a,z,e,r,t,y,u,i):
    tab=[a,z,e,r,t,y,u,i]
    for i in range(0,len(tab)):
        ligne = ''
        for j in range(0,len(tab)):
            ligne= ligne + tab[i][j] + '   '
        ligne=ligne+'\n'
        print(ligne)
    
affichage(a,z,e,r,t,y,u,i)