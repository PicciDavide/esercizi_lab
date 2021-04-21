from spalla import Verifica

Verifica.firma("Davide Piccinini")


def es_1():
    es = Verifica.inizia_esercizio(1)
    print(es)
    lista = es.dati
    somma = 0
    for i in lista:
        if i > lista[0]:
            somma += i
    

    es.consegna(somma)

def es_2():
    es = Verifica.inizia_esercizio(2)
    print(es)
    lista = es.dati
    somma = 0
    for i in lista:
        if len(i) > 4:
            somma += 1


def es_3():
    es = Verifica.inizia_esercizio(3)
    print(es)
    lista = es.dati
    lista_n = []
    for i in lista:
        if i > 1 and i % 2 != 0:
            lista_n.append(i)

    es.consegna(lista_n)

def es_4():
    es = Verifica.inizia_esercizio(4)
    print(es)
    lista = es.dati
    lista_n = []
    counter = -1
    for i in lista:
        counter += 1
        if i < 0:
            lista_n.append(counter)
    es.consegna(lista_n)

def es_5():
    es = Verifica.inizia_esercizio(5)
    print(es)
    dic = es.dati
    lista_f = dic["frutta"]
    lista_n = []

    for i in dic["indici"]:
        if lista_f[i] not in lista_n:
            lista_n.append(lista_f[i])
        
    print(lista_n)
    es.consegna(lista_n)

def es_6():
    es = Verifica.inizia_esercizio(6)
    print(es)
    num = es.dati
    lista_n = []
    counter = 0
    for i in range(num):
        lista_n.append(counter)
        counter+=1
    lista_n.append(num)
    lista_n.reverse()
    
    print(lista_n)

    es.consegna(lista_n)

def es_7():
    es = Verifica.inizia_esercizio(7)
    print(es)
    frase = es.dati
    lista_p = []
    parola = ""
    for i in frase:
        parola += i
        if i == " ":
            if parola[0] == "e" or parola[0] == "a":
                parola2 = parola[0:-1]
                lista_p.append(parola2)
            parola = ""

    print(lista_p)
    es.consegna(lista_p)

def es_8():
    es = Verifica.inizia_esercizio(8)
    print(es)
    frase = es.dati

es_6()

Verifica.stampa_voto()
Verifica.stampa_esercizi()