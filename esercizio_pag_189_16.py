#Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
#Successivamente interroga il dizionario per visualizzare la capitale di una nazione#

nazioni = ["bosnia-erzegovina", "slovenia", "kosovo"]
capitali = ["Sarajevo", "Lubiana", "Pristina"]

naz_cap = {}
while True:
    for l in range(len(nazioni)):
        naz_cap[nazioni[l]] = capitali[l]

    risposta_n = input("Di quale nazione vuoi sapere la capitale? ")
    if risposta_n.lower() in naz_cap:
        print("La capitale è", naz_cap[risposta_n.lower()])
    else:
        aggiunta = input("La nazione non è nella lista, vuoi aggiungere una nazione? (si no) ")
        if aggiunta.lower() == "si":
            nazione = input("Scrivi la nazione che vuoi aggiungere ")
            capitale = input("Scrivi la capitale che vuoi aggiungere ")
            naz_cap[nazione.lower()] = capitale.lower()
    ripeti = input("Vuoi ripetere il programma? ")
    if ripeti.lower() == "no":
        break