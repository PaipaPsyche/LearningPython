'''
Author: David Paipa 2019
Manual LearningPython

Codigo de prueba para ilustrar.
'''
# RECUERDE  el primer paso suele ser importar las librerias necesarias[GP]

import numpy as np


def dar_edad_aleatoria():

    edad_aleatoria = np.random.randint(30,50) # Edad aleatoria entre 30 y 50

    return edad_aleatoria




print("Mariela, de" , dar_edad_aleatoria() , "anios, se ha hecho amiga de Rafael, que tiene",dar_edad_aleatoria(),"anios.")
