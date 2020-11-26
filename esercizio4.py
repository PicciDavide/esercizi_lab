veicoli = []
run = True
while run == True:
    veicolo = int(input("immettere il numero di veicoli transitati oggi: "))
    if veicolo == 0:
        run = False
    else:
        veicoli.append(veicolo)
counter = 0
for i in veicoli:
    counter += i
print(counter,"veicoli totali nell'ultimo periodo")
