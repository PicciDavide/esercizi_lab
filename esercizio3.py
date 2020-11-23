run = True
while run == True:
    stipendio = int(input("stipendio del dipendente: "))
    stipendi = []
    if stipendio == -1:
        run == True
    else:
        stipendi += stipendio
media = 0
counter = 0
for i in stipendi:
    media += i
    counter += 1
media = media/counter
print(media)