#Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
#Successivamente interroga il dizionario per visualizzare la capitale di una nazione#

nazioni = ["bosnia-erzegovina", "slovenia", "kosovo"]
capitali = ["Sarajevo", "Lubiana", "Pristina"]

naz_cap = {}

for l in range(len(nazioni)):
    naz_cap[nazioni[l]] = capitali[l]

risposta_n = input("Di quale nazione vuoi sapere la capitale? ")
try:
    print("La capitale è", naz_cap[risposta_n.lower()])
except ValueError:
    print("Errore, la nazione non è presente nell'elenco")