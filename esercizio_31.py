numero = int(input("Scrivere il numero da trasformare: "))
numero_bin = bin(numero)
resto = ""
while numero > 0:
    resto += str(numero % 2)
    numero = numero//2
print("Il numero in binario è:", resto[::-1] ,"\n(con la funzione di python", numero_bin, ")")