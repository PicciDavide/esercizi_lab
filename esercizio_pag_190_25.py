registro = {}
registro_voti = []
for i in range(30):
    nome = input("Inserire il nome dello studente ")
    while True:
        try:
            voto = float(input("Inserire il voto dello studente "))
            break
        except ValueError:
            print("Si deve inserire un numero")
    registro[nome] = voto

registro_ordinato = sorted(registro.items(), key=lambda voto:voto[1])

for l in registro_ordinato:
    print(l[0], "ha preso", l[1])

for l in registro_ordinato:
    if l[1] not in registro_voti:
        registro_voti.append(l[1])

print(registro_voti)