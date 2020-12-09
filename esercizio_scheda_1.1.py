parola = input("Scrivere la parola da processare: ")
parola_1 = parola[::-1]
if parola == parola_1:
    print(parola, "è un palindromo.")
else:
    print(parola, "non è un palindromo.")
