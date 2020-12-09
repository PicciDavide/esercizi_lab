restart = True
while restart:
    controllo_domanda = True
    parola_i = input("Scrivere la parola da tradurre in rövarspräket: ").lower()
    vocali = "bcdfghjklmnpqrstwxyz"
    parola = ""
    for l in parola_i:
        if l in vocali:
            parola = parola + l + "o" + l
        else:
            parola = parola + l
    print("traduzione:", parola)
    while controllo_domanda == True:
        print("Vuoi tradurre un altra parola?")
        risposta = input("Si      No\n").lower()
        if risposta == "si":
            controllo_domanda = False
        elif risposta == "no":
            restart = False
            controllo_domanda = False
        else:
            print("Puoi rispondere con Si o No")
