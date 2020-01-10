# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:11:59 2020

@author: 33762
"""
import main as main

print("============================================")
print("                PolyChess            ")
print("============================================")
print("1->   Joueur vs Joueur")
print("2->   Joueur vs IA")
print("3->   IA vs IA")
mode = 99 
while(mode>3 or mode<1):
    mode =int(input("Choisissez votre mode : "))

if mode == 1:
    main.PlayerVsPlayer()
elif mode == 2:
    main.PlayerVsIa()
elif mode == 3:
    main.IaVsIa()