# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:13:20 2019

@author: 33762

Pour la représentation on a choisi de commencer avec quelque chose de simple
"""
import moteur_blocage as mb

def affichage(echiquier):
    """
    affichage(List[List[String]])
    -> return None
    
    affiche l'échiquier dans la console python 
    en donnant les différentes lignes de haut en bas en paramètre
    WORK
    """
    c=['0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ']
    tab=['a','z','e','r','t','y','u','i']
    for i in range(0,len(echiquier)):
        tab[i]=echiquier[i]
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

def get_Piece(pos,echiquier):
    """
    get_Piece(List[int,int],List[List[String]])
    -> return string
    
    renvoie la pièce qui est sur la position donnée en paramètre 
    WORK
    """
    x=pos[0]
    y=pos[1]
    return echiquier[y][x] 

def get_NomPiece(pos,echiquier):
    """
    get piece(List[int,int],List[List[String]])
    -> return string 
    
    renvoie le nom de la pièce qui est sur la position donnée en paramètre
    WORK
    """
    piece=get_Piece(pos,echiquier)
    if 'T' in piece :
        return 'tour'
    elif 'C' in piece:
        return 'cavalier'
    elif 'F' in piece:
        return 'fou'
    elif 'D' in piece:
        return 'dame'
    elif 'P' in piece:
        return 'pion'
    elif 'R' in piece:
        return 'roi'

def get_Couleur(pos,echiquier):
    """
    get_Couleur(List[int,int],List[List[String]])
    -> return string
    
    retourne la couleur d'une pièce en donnant les coord. de celle-ci'
    WORK
    """
    x=pos[0]
    y=pos[1]
    if 'n' in get_Piece([x,y],echiquier):
        return 'Noir'
    else :
        return 'Blanc'
    

def get_placesDispo_Blancs(echiquier):
    """
    get_placeDispoBlancs(List[List[String]])
    -> return List
    
    Cette fonction retourne toutes les places libres pour les blancs
    on considérant les places occupés par les noirs comme disponibles 
    WORK
    """
    res=[]
    blancs=['Pb','Tb','Cb','Fb','Rb','Db']
    for i in range(0,len(echiquier)):
        for j in range(0,len(echiquier[i])):
            if echiquier[i][j] not in blancs:
                res.append([j,i])
    return res

def get_placesDispo_Noirs(echiquier):
    """
    get_placesDispo_Noirs(List[List[String]])
    -> return List
    
    Cette fonction retourne toutes les places libres pour les noirs
    on considérant les places occupés par les blancs comme disponibles 
    WORK
    """
    res=[]
    noirs=['Pn','Tn','Cn','Fn','Rn','Dn']
    for i in range(0,len(echiquier)):
        for j in range(0,len(echiquier[i])):
            if echiquier[i][j] not in noirs:
                res.append([j,i])
    return res

def initialiseEchiquier():
    """
    creates and initializes the chessboard
    
    """
    a=['Tn','Cn','Fn','Dn','Rn','Fn','Cn','Tn']
    z=['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn']
    e=['**','**','**','**','**','**','**','**']
    r=['**','**','**','**','**','**','**','**']
    t=['**','**','**','**','**','**','**','**']
    y=['**','**','**','**','**','**','**','**']
    u=['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb']
    i=['Tb','Cb','Fb','Db','Rb','Fb','Cb','Tb']
    echiquier=[a,z,e,r,t,y,u,i]
    return echiquier
    
def choisiDeplacement(echiquier):
    coups_possibles = []
    while coups_possibles == []:
        x,y=demandeUtilisateurPosition()
        nom=get_NomPiece([x,y],echiquier)
        if nom=='pion' :
            coups_possibles = mb.coups_possibles_pion([x,y],echiquier,get_Couleur([x,y],echiquier))
        elif nom=='cavalier':
            coups_possibles = mb.coups_possibles_cavalier([x,y],echiquier,get_Couleur([x,y],echiquier))
        elif nom=='tour':
            coups_possibles = mb.coups_possibles_tour([x,y],echiquier,get_Couleur([x,y],echiquier))
        elif nom=='fou':
            coups_possibles = mb.coups_possibles_fou([x,y],echiquier,get_Couleur([x,y],echiquier))
        elif nom=='dame':
            coups_possibles = mb.coups_possibles_dame([x,y],echiquier,get_Couleur([x,y],echiquier))   
        elif nom=='roi':
            coups_possibles = mb.coups_possibles_roi([x,y],echiquier,get_Couleur([x,y],echiquier))
    nbCoup=afficherCoupsPossibles(coups_possibles)
    choix=demanderChoixUtilisateur(nbCoup)
    if choix == 0:
        choisiDeplacement(echiquier) 
    position_arrivee = coups_possibles[choix-1]
    deplacement(echiquier,x,y,position_arrivee[0],position_arrivee[1])
    affichage(echiquier)
    #A faire assoscier le choix a un déplacement et appeler la fonction de déplacement du gourmand !! 
    
def deplacement(echiquier,x_dep,y_dep,x_arr,y_arr):
    pion_d = echiquier[y_dep][x_dep]
    echiquier[y_arr][x_arr] = pion_d
    echiquier[y_dep][x_dep] = "**"
    
    
def afficherCoupsPossibles(coups_possibles):
    print('0=>Annuler')
    for i in range(0,len(coups_possibles)):
        print(str(i+1)+'=>'+str(coups_possibles[i][0])+'-'+str(coups_possibles[i][1]))
    return i

def demanderChoixUtilisateur(coups_possibles):
    choix = 999
    while(choix>coups_possibles+1 or choix<0):
        choix = int(input("Choisir : ")) #!!! si on rentre un string ca plante il faut régler ca
    return choix

def demandeUtilisateurPosition():
    x=99
    y=99
    while x > 7 or x < 0 : 
        x = int(input("X : "))
    while y > 7 or y < 0 : 
        y = int(input("Y : "))
    return x,y

def generatorFEN(echiquier):
    """
    generate the fen to use the Syzygy API
    generatorFEN([List[List[String]])
    return ---> String
    
    """
    fen = ""
    for ligne in echiquier:
        for case in ligne:
            if case == "Tn":
                fen = fen + "r"
            if case == "Tb":
                fen = fen + "R"
            if case == "Cn":
                fen = fen + "n"
            if case == "Cb":
                fen = fen + "N"
            if case == "Fn":
                fen = fen + "b"
            if case == "Fb":
                fen = fen + "B"
            if case == "Dn":
                fen = fen + "q"
            if case == "Db":
                fen = fen + "Q"
            if case == "Rn":
                fen = fen + "k"
            if case == "Rb":
                fen = fen + "K"
            if case == "Pn":
                fen = fen + "p"
            if case == "Pb":
                fen = fen + "P"
            if case == "**":
                fen = fen + "0"
        fen = fen + "/"
    lettres = ['r','R','n','N','b','B','q','Q','k','K','p','P','/']
    fenIntermediaire = fen
    while fenIntermediaire.find('0') != -1:
        startEmpty = fenIntermediaire.find('0')
        ends = []
        for lettre in lettres:
            ends.append(fenIntermediaire.find(lettre,startEmpty))
        for i in range(0,len(ends)):
            if ends[i] == -1:
                ends[i] = 99
        endEmpty = min(ends)
        fenIntermediaire = fenIntermediaire[:startEmpty] + str(endEmpty-startEmpty) + fenIntermediaire[endEmpty:len(fenIntermediaire)]
    return fenIntermediaire[:-1]
  
  
    
    
    
    
    