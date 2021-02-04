nazioni = ["bosnia-erzegovina", "slovenia", "kosovo"]
capitali = ["sarajevo", "lubiana", "pristina"]

naz_cap = {}
while True:
    for l in range(len(nazioni)):
        naz_cap[nazioni[l]] = capitali[l]

    risposta_n = input("Di quale nazione vuoi sapere la capitale? ")
    if risposta_n.lower() in naz_cap:
        print("La capitale è:", naz_cap[risposta_n.lower()])
    else:
        aggiunta = input("La nazione non è nella lista, vuoi aggiungere una capitale? (si no) ")
        if aggiunta.lower() == "si":
            nazione = risposta_n
            capitale = input("Scrivi la capitale che vuoi aggiungere ")
            naz_cap[nazione.lower()] = capitale.lower()
    ripeti = input("Vuoi ripetere il programma? (si no) ")
    if ripeti.lower() == "no":
        break

cap_naz = {}
for d in naz_cap:
    cap_naz[naz_cap[d]] = d
while True:
    risposta_c = input("Di quale capitale vuoi sapere la nazione? ")
    if risposta_c.lower() in cap_naz:
        print("La nazione è:", cap_naz[risposta_c.lower()])
    else:
        print("La capitale non è nella lista")
    ripeti = input("Vuoi ripetere il programma? (si no) ")
    if ripeti.lower() == "no":
        break