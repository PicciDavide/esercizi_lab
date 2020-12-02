length = int(input("Scrivere la lunghezza del numero: "))
n_decimale = 0
n_binario = ""
for i in range(length):
    print("Scrivere il", i + 1,"° carattere del numero da destra: ")
    numero = int(input())
    if numero == 0 or 1:
        n_binario += str(numero)
        if numero == 1:
            n_decimale += 2**i
    else:
        print("I numeri binari sono fatti solo da 0 e 1")
        i -= 1
n_binario = n_binario[::-1]
print("Convertito in decimale il numero è:", n_decimale, "(la funzione di python lo converte come:", int(n_binario, 2), ")")
