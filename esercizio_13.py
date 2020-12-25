""" verfica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a 0)."""
while True:
    try:
        numero = int(input("Scrivere il numero da verificare: "))
        break
    except ValueError:
        print("Bisogna inserire un numero intero")
if (numero//2)*2 == numero:
    print("Il numero è pari")
else:
    print("il numero è dispari")