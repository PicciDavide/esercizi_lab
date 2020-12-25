"""Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado a x + b = 0.
Il processo risolutivo dipende dai valori assunti dai coefficenti a e b secondo la tabella che segue
                    b
            = 0     != 0
a  = 0   indeter.   imposs.
  != 0   x = 0      x = -b/a"""

equazione = input("Inserire l'equazione(ax + b = 0): ")
equazione = equazione.replace("x","")
lista_eq = equazione.split("+")
fine_lista = lista_eq[1].index("=")
lista_eq[1] = lista_eq[1][:fine_lista]
if int(lista_eq[0]) == 0:
    if int(lista_eq[1]) != 0:
        print("l'equazione è impossibile")
    else:
        print("l'equazione è indeterminata")
else:
    if int(lista_eq[1]) != 0:
        print("la soluzione è: x = -", lista_eq[1], "/", lista_eq[0])
    else:
        print("la soluzione è: x = 0")

