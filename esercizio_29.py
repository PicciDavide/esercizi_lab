while True:
    try:
        escursione_termica = float(input("Scrivere il valore dell'escursione termica: "))
        break
    except ValueError:
        print("Si possono inserire solo numeri")
elenco_città = []
elenco_temp_max = []
elenco_temp_min = []
elenco_temp = []
soluzione = []
while True:
    print("Inserire 0 se si vuole terminare la selezione delle città")
    città = input("Scrivere il nome della città e la temperatura massima e minima (nome_città, 25, 7 ): ")
    if città == "0":
        break
    else:
        città = città.split(",")
        elenco_città.append(città[0])
        elenco_temp_max.append(float(città[1]))
        elenco_temp_min.append(float(città[2]))
for l in range(len(elenco_città)):
    elenco_temp.append(elenco_temp_max[l] - elenco_temp_min[l])
for l in range(len(elenco_città)):
    if elenco_temp[l] > escursione_termica:
        soluzione.append(elenco_città[l])
print("Le città con escursione termica maggiore di", escursione_termica, "sono:", soluzione)