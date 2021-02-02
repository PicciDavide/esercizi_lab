'''Scrivere un programma che registri in ordine di arrivo i nomi dei pazienti di laboratorio,
successivamente stampa il paziente che deve essere sottoposto all'esame per primo
perché è il primo della coda'''

coda = []

while True:
    print("Scrivere 0 per terminare l'inserimento")
    paziente = input("Scrivere il nome del paziente: ")
    if paziente == "0":
        break
    coda.append(paziente)
for l in range(len(coda)):
    print("Il nome del prossimo paziente è:", coda[0])
    input("Premere invio per proseguire")
    coda.pop(0)
print("Termine coda")