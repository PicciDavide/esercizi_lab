registro = {}
registro_media = []

for i in range(2):
    nome = input("Inserire il nome dello studente ")
    while True:
        try:
            voto = float(input("Inserire il voto dello studente "))
            break
        except ValueError:
            print("Si deve inserire un numero")
    registro[nome] = voto

media = sum(registro.values())/len(registro)

for l in registro:
    if registro[l] > media:
        registro_media.append(l)

print(registro_media)