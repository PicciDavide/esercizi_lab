elenco = input("inserire l'elenco degli studenti con la formula: studente1, lancio1; studente2, lancio2;...\n")
elenco = elenco.split(";")
valori = []
for i in elenco:
    scrittore_toggle = False
    numero = " "
    for l in i:
        if scrittore_toggle:
            numero = numero + l
        if l == ",":
            scrittore_toggle = True
    valori.append(int(numero))
valori.sort()
print("Il lancio più lungo è stato di", valori[0], "m")