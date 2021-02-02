#Dato un elenco di nazioni (lista) e di capitali (lista) (nazione e relativa capitale si trovano a indici uguali nelle rispettive liste),
#visualizza la capitale della nazione che viene inserita. Nel caso la nazione non sia nella lista,
#stampa un messaggio di errore

nazioni = ["bosnia-erzegovina", "slovenia", "kosovo"]
capitali = ["Sarajevo", "Lubiana", "Pristina"]

risposta_n = input("Di quale nazione vuoi sapere la capitale? ")
try:
    print("La capitale è", capitali[nazioni.index(risposta_n.lower())])
except ValueError:
    print("Errore, la nazione non è presente nell'elenco")