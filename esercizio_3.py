parola_r = input("Scrivere la parola in rövarspräket: ")
vocali = "aeiou"
counter = -1
cons_counter = 0
cons_toggle = 3
parola = ""
for l in parola_r:
    counter += 1
    if l not in vocali:
        cons_counter += 1  
    if cons_toggle == 0:
        cons_counter = 0
    if cons_counter == 2:
        if parola_r[l] == parola_r[l - 2]:
            parola = parola + parola_r[l]
    cons_toggle -= 1
print(parola)
