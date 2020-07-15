# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 03:25:40 2020

@author: YODA ISMAEL
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:19:53 2020

@author: YODA ISMAEL
"""
import scipy.special as sps
from math import*
import numpy as np
import matplotlib.pyplot as plt

# 1. Simulation d'un échantillon de taille 10000 suivant une loi binomiale B(30,0.2) et 
# histogramme de l'échantillon obtenue

binomiale = np.random.binomial(30,0.2,size=10000)
binomiale
plt.hist(binomiale,bins=30,range=(1,30),density=True)
plt.show()


# 2. Simulation d'un échantillon de taille 10000 suivant une loi normale N (3, 0.4) et 
# représentation de la fonction de densité de l’échantillon obtenu. Choisir un intervalle 
# contenant 0 pour domaine de représentation.

# Simulation de variable aléatoire suivant une loi normale de taille 10000
mu=3
sigma=0.4
Normale=np.random.normal(mu,sigma,size=10000)
Normale
# Histogramme de la distribution
count, bins, ignored = plt.hist(Normale,bins=20,normed=True)
# Courbe de la fonction de densité de l'échantillon 
y=1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) )
# y représente la fonction de densité
plt.plot(bins, y, linewidth=3, color='r')
plt.show()


# 2. Simulation d'un échantillon de taille 10000 suivant une loi gamma γ (10, 0.5) et 
# représentation de la fonction de densité de l’échantillon obtenu. Choisir un intervalle 
# contenant 0 pour domaine de représentation.

# Simulation de variable aléatoire suivant une loi gamma de taille 10000
shape=10
scale=0.5
Gamma=np.random.gamma(shape,scale,10000)
Gamma
# Histogramme de la distribution
count, bins, ignored = plt.hist(Gamma, 20, normed=True)
# Courbe de la fonction de densité de l'échantillon
y = bins**(shape-1)*(np.exp(-bins/scale)/(sps.gamma(shape)*scale**shape))
# y représente la fonction de densité
plt.plot(bins, y, linewidth=2, color='r')
plt.show()


