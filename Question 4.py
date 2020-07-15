# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 06:35:24 2020

@author: YODA ISMAEL
"""

# Importation des bibliothèques dont on a besoin

import numpy as np
import matplotlib.pyplot as plt


# Simulation d'une variable aléatoire de taille 10000 suivant une loi uniform

x=np.random.uniform(0,1,10000)
x

# Fonction h(x)

h=np.sqrt(1-x*x)
h

# Approximation de l'intégrale I2
# Nous utilisons ici la loi des grands nombre qui dit que lorsque n tend vers +l'infini alors
# X_barre_n converge vers l'espérance mathématique mu

I2=np.mean(h)
I2

# Vraie valeur de l'intégrale
True_Value= np.pi/4
True_Value

# Observons par graphique l’évolution de cette estimation lorsque n varie 
# et vérifions la cohérence avec la valeur théorique I2 =π/4

# Simulation d'une loi uniforme de parametre U(0,1) et de taille 10000
xi=np.random.uniform(0,1,10000)
# Estimations de la valeur de l'intégrale en fonction de la taille de l'échantillon
n= int (1e4)
S=np.cumsum(np.sqrt(1-xi*xi))/ np.arange (1,n+1)
# S représente les valeurs estimées de l'intégrale pour n=1,2,3.....100000
plt.plot( range (1,n+1),S,"r",label= "Estimation" )
plt.plot ((1,n) ,(0.7853981633974483,0.7853981633974483) ,'b',label= " Valeur Théorique " )
plt.ylabel( 'Estimation Intégrale ' )
plt.xlabel( " Evolution de la taille de l'échantillon " )
plt.legend(loc= ' best ')
plt.title( "Evolution de la valeur de l'estimation de l'intégrle lorsque n varie ")
plt.savefig('C:/Users/YODA ISMAEL/Desktop/Dossier Etudes/Dossiers Master/Semestre1/Mathématiques/Statistiques/Projet Statistiques/MCarlo.jpg',transparent=False, bbox_inches='tight')



# On constate que plus la taille de l'échantillon augmente, plus la valeur de
# l'intégrale est mieux estimée.
    
