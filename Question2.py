# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:09:19 2020

@author: YODA ISMAEL
"""

# Importation des librairies pandas, numpy et de la fonction pylab
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1.Importation des données avec la fonction read_csv de pandas  
donnees=pd.read_csv('C:/Users/YODA ISMAEL/Desktop/Dossier Etudes/Dossiers Master/Semestre1/Mathématiques/Statistiques/Projet Statistiques/Question2.csv',names=['xi','yi'],sep=';')
print(donnees)
type(donnees)
# Statistiques descriptive des donnees
donnees.describe()

# 2.Représentation des yi en fonction des xi
sns.regplot(donnees['xi'],donnees['yi'],fit_reg=True)
plt.savefig('C:/Users/YODA ISMAEL/Desktop/Dossier Etudes/Dossiers Master/Semestre1/Mathématiques/Statistiques/Projet Statistiques/fig.jpg',transparent=False, bbox_inches='tight')
plt.title('Représentation des yi en fonction des xi  ')
plt.show()
# L'allure de la représentation ne nous laisse pas soupconner 
# une liaison linéaire entre les deux variables car la droite ne passe pas par la pluspart des points


# 3. Calculons les coefficients de la droite des moindres carrees 
(a_s, b_s, r, tt, stderr) = linregress(donnees['xi'],donnees['yi'])
print('Coefficients de regression calculés par linregress : a=%.5f b=%.5f'  % (a_s,b_s))
# Les coefficients de la droite des moindres carrees sont a=2.73476 et b=1.02134. 
# La droite des moindre carrees est donc Y_reg=2.73476*X + 1.02134

# 4. Donnons les ordonnées des yi calculés par la droite des moindres carrés correspondant aux
# différentes valeurs des xi
Y_reg= 2.73476*donnees['xi']+1.02134
Y_reg
# Les valeurs yi correspondants sont
# yi1= 50.24702
# yi2= 20.16466
# yi3= 39.30798
# yi4= 85.79890
# yi5= 58.45130
# yi6= 14.69514
# yi7= 31.10370
# yi8= 44.77750
# yi9= 72.12510
# yi10= 80.32938

# 5.Tracons la droite sur le même graphique.
sns.regplot(donnees['xi'],donnees['yi'],fit_reg=True,label='Valeurs Observées')
sns.regplot(donnees['xi'],Y_reg,fit_reg=True,color='red',label='Moindres Carrés')
plt.title('Représentation graphique des xi et yi estimés')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show()

# 6. Déterminons une estimation plausible de Y à xi= 21 
Y= 2.73476*21+1.02134
Y
# Une estimation plausible de Y à xi=21 donne 58.4513

# 7. Déterminons l'écart entre la valeur observée de Y à xi= 21 et la valeur estimée avec 
# la droite des moindres carrés 
ecart=62 -Y
ecart
# Cet écart entre Y observée et Y estimée est égale à 3.5486999999999966.
# Cet écart s'appelle l'erreur d'estimation ou le résidu 

# 8. La droite des moindres carrés obtenue en 2 passe par le point (x(bar),y(bar)).
# On ne peut pas généraliser cette conclusion à n’importe quelle droite de régression 
# car cela concerne uniquement les droites de régressions dont les paramètres ont une
# liaison linéaires entre eux.