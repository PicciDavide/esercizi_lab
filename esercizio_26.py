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
