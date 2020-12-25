"""calcola la media degli stipendi dei dipendenti di un'azienda, acquisiti con una ripetizione fino a quando 
si inserisce il valore -1 per segnalare la fine dell'input dei dati"""

stipendi = []
run = True
while run == True:
    stipendio = int(input("immettere lo stipendio del dipendente: "))
    if stipendio == -1:
        run = False
    else:
        stipendi.append(stipendio)
media = 0
counter = 0
for i in stipendi:
    media += i
    counter += 1
media = media/counter
print("La media degli stipendi è", media)
