'''Data la parabola y = ax^2 + bx + c,
definisci tre funzioni per calcolarne i punti significativi:
vertice, fuoco, intersezione con gli assi. 
Le tre funzioni ricevono come parametri i coefficienti a, b, c
e restituiscono il valore calcolato.'''

import numpy as np

def calcola_vertice(a, b, c):
    delta = b**2 - 4*a*c
    vertice = [-b/(2*a), -delta/(4*a)]
    return vertice

def calcola_fuoco(a, b, c):
    delta = b**2 - 4*a*c
    fuoco = [-b/(2*a), (1 - delta)/(4*a)]
    return fuoco
'''
def calcola_intersezioni(a, b, c):
    matrice_coeff = np.array
    ([[a, b, 1], 
    [0, 1, 0]])
    matrice_noti = np.array
    ([-1, 1])
    intersezione_y = np.linalg.solve(matrice_coeff, matrice_noti)
    return intersezione_y
'''
print("Scegli se calcolare il vertice o il fuoco della parabola"
"\nScrivi 0 per il vertice e 1 per il fuoco ")
risposta = int(input())
valori = input("Inserisci a, b e c, separati da una virgola ")
valori = valori.split(",")
if risposta == 0:
    print(calcola_vertice(int(valori[0]), int(valori[1]), int(valori[2])))
if risposta == 1:
    print(calcola_fuoco(int(valori[0]), int(valori[1]), int(valori[2])))