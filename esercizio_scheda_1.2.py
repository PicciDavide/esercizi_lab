parole = input("Scrivere una lista di parole con la formula: parola1, parola2, ...\n")
lista_1 = parole.split(",")
lista_2 = []
for i in lista_1:
    lun = len(i)
    lista_2.append(lun - 1)
print("la lunghezza delle parole è rispettivamente di", lista_2)
