# Projet : Polychess  
> Gestion de projet pour faire un jeu d'échec. 

## Règles : 

### But du jeu :

Faire échec et mat, évidemment, l’adversaire peut abandonner et vous avez la possibilité de gagner au temps.
On dit que le Roi est en échec, lorsque la case qu’il occupe est contrôlée par une pièce adverse. Le Roi doit donc OBLIGATOIREMENT parer cet échec.
Si le Roi ne peut parer l’échec, il perd la partie, puisqu’il est échec et mat.

### Déplacement des pièces 

  #### pion :
  
![](img/deplacement-pion.png)

  #### cavalier :
  
![](img/deplacement-cavalier.png)

  #### fou :
  
![](img/deplacement-fou.png)

  #### tour :
  
![](img/deplacement-tour.png)

  #### dame :
  
![](img/deplacement-dame.png)

  #### roi :
  
![](img/deplacement-roi.png)

### Règles spéciales

  #### La promotion 
Quand le pion atteint la dernière rangée de l’échiquier, il se transforme en une autre pièce de sa couleur (en général une Dame). Le pion ne peut se transformer en Roi.

  #### Roque
Le Roi se décale de deux cases, en direction d’une de ses Tours. La Tour vient sauter par dessus le Roi pour se placer juste à côté(sur une cases adjacente).
Conditions : 

– Ni le Roi, ni la Tour concernés, ne doivent avoir bougé pendant le jeu et aucune pièce ne doit les séparer.

– Le Roi ne peut être en échec.

– Aucune pièce ennemie ne doit contrôler les deux cases que le Roi parcourt pour roquer.

  #### La Prise en passant 
Un pion peut capturer un pion adverse (de colonne adjacente), si celui-ci saute deux cases, comme s’il n’avait avancé que d’une case. On dit que ce pion prend le pion ennemi “en passant”.


### Interface du jeu d'échecs

![](img/interface.png)

Ci-dessus vous pouvez voir l'interface de notre jeu d'échecs. Elle se décline sous forme console, avec une représentation de pièces avec une chaîne de caractères, par exemple la châine "Tn" représente la tour noire, la chaîne "Tb" réprésente la tour blanche. 
Comme vous l'avez compris la première lettre définie le type de pièce et la deuxième sa couleur. 

b : blanc

n : noir

P : pion

T : tour

C : cavalier

F : fou

D : dame

R : roi

Il faudra ensuite que vous sélectionnez une pièce en rentrant ses coordonnées (x,y) : par exemple si vous voulez bougez le pion en (0;1) du plateau vous devrez taper dans la console 0 puis 1 de cette manière :

![](img/interfacePionSelec.png)

Puis le programme vous affiche la liste des déplacements disponibles en affichant les possitions d'arrivée possibles pour cette pièce comme suit : 

![](img/interfacePionSelecPossibi.png)

Il faudra alors séléctionner un déplacement en entrant le chiffre correspondant à celui-ci, ici on choisit de le faire avancer d'une case, on entre donc la valeur 1, et l'affichage de l'échiquier est mis à jour :

![](img/echiquierAJour.png)

### Déroulement d'une partie

Vous pourrez jouer contre un ordinateur aux échecs. Vous commencerez la partie, qui se déroulera tour par tour, la partie se finit lorsque l'un de vous est échec et mat ou que son compteur de temps est a 0.


### Comment utiliser notre programme ? 
  
  Pour se faire il suffit de réaliser ces actions :
  
        - Créer un répertoire sur votre ordinateur pour cloner le dépot git  
        - cloner le dépot du projet en local sur votre machine: 
            En tapant la commande suivante sur git bash : git clone https://github.com/TheoBernardin/PolyChess.git
            En allant directement sur le site https://github.com/TheoBernardin/PolyChess.git où vous pourrez le télécharger directement 
        - Pour lancer le jeu, lancer le programme executable(...PolyChess\src\dist\menu\menu.exe) , a vous de jouer !
        

        
        
       


