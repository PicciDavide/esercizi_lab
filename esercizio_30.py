length = int(input("Scrivere la lunghezza del numero: "))
n_decimale = 0
n_binario = ""
for i in range(length):
    print("Scrivere il", i + 1,"° carattere del numero da destra: ")
    numero = int(input())
    if numero == 0 or 1:
        n_binario += str(numero)
        if numero == 1:
            n_decimale += 2**(length - i)
    else:
        print("I numeri binari sono fatti solo da 0 e 1")
        i -= 1
for i in range(8 - length):
    n_binario += "0"
print("Convertito in decimale il numero è:", n_decimale, "(la funzione di python lo converte come:", int(bin(n_decimale), 2)), ")"