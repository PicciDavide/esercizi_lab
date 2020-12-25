"""Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto
è maggiore di 10 oppure la loro somma se il prodotto è minore o uguale a 10.
Esegui poi il programma con diverse coppie di valori per a e b: (-5, 2), (10, 2), (-4, -5), (5, 4), (-3, -2)."""
numeri = input("Inserire le coppie di numeri (esempio: (n1, n2); (n3, n4); ...")
numeri_lista = numeri.split(";")
for i in range(len(numeri_lista)):

    numero_lista = numeri_lista[i].replace("(","").replace(")","")
    numero_lista = numero_lista.split(",")
    
    if int(numero_lista[0]) * int(numero_lista[1]) > 10:
        print("La differenza della", i + 1, "° coppia è:", int(numero_lista[0]) - int(numero_lista[1]))
    else:
        print("La somma della", i + 1, "° coppia è:", int(numero_lista[0]) + int(numero_lista[1]))