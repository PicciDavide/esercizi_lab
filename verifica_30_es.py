from spalla import Verifica



def es1():
    es = Verifica.inizia_esercizio(1)
    parola = es.dati
    parola = parola.lower()
    es.consegna(parola)

def es2():
    es = Verifica.inizia_esercizio(2)
    print(es)
    numero = es.dati
    numero = numero * numero
    es.consegna(numero)
def es3():
    es = Verifica.inizia_esercizio(3)
    print(es)
    chiave = es.dati
    valore = chiave["cognome"]
    es.consegna(valore)

def es4():
    es = Verifica.inizia_esercizio(4)
    print(es)
    lista = es.dati
    lunghezza = len(lista)
    es.consegna(lunghezza)

def es5():
    es = Verifica.inizia_esercizio(5)
    print(es)
    lista = es.dati
    lista2 = []
    for l in lista:
        l = l.upper()
        print(l)
        lista2.append(l)
        print(lista2)
    es.consegna(lista2)

def es6():
    es = Verifica.inizia_esercizio(6)
    print(es)
    lista = es.dati
    somma = sum(lista)
    es.consegna(somma)

def es7():
    es = Verifica.inizia_esercizio(7)
    print(es)
    lista = es.dati
    lista2 = []
    for l in lista:
        if l > 5:
            lista2.append(l)
    numero = sum(lista2)
    es.consegna(numero)

def es8():
    es = Verifica.inizia_esercizio(8)
    print(es)
    lista = es.dati
    somma = 0
    for l in lista:
        if l % 2 == 0:
            somma += l
    es.consegna(somma)
def es9():
    es = Verifica.inizia_esercizio(9)
    print(es)
    lista = es.dati
    somma = 0
    for l in lista:
        if l % 2 == 1:
            somma += l
    es.consegna(somma)

def es10():
    es = Verifica.inizia_esercizio(10)
    print(es)
    lista = es.dati
    lista2 = []
    for l in lista:
        l = l.lower()
        lista2.append(l)
    lista.sort()
    print(lista2)
    es.consegna(lista2)
def es11():
    es = Verifica.inizia_esercizio(11)
    print(es)
    lista = es.dati
    lista2 = []
    for l in lista:
        l = l.lower()
        lista2.append(l)
    lista2.sort()
    print(lista2)
    es.consegna(lista2)

def es12():
    es = Verifica.inizia_esercizio(12)
    print(es)
    lista = es.dati
    lista2 = []
    for l in lista:
        l -= 1
        lista2.append(l)
    es.consegna(lista2) 

def es13():
    es = Verifica.inizia_esercizio(13)
    print(es)
    lista = es.dati
    lista2 = []
    for l in range(len(lista)):
        if l + 1 < len(lista):
            somma = lista[l] + lista[l+1]
            lista2.append(somma)
        else:
            lista2.append(lista[l])
    es.consegna(lista2)

def es14():
    es = Verifica.inizia_esercizio(14)
    print(es)
    lista = es.dati
    lista_p = []
    lista_n = []
    lista_z = []
    numeri = {}
    for l in lista:
        if l > 0:
            lista_p.append(l)          
        elif l < 0:
            lista_n.append(l)
        else:
            lista_z.append(l)
    numeri["positivi"] = len(lista_p)
    numeri["negativi"] = len(lista_n)
    numeri["zeri"] = len(lista_z)
    print(numeri)
    es.consegna(numeri)

def es15():
    es = Verifica.inizia_esercizio(15)
    print(es)
    lista = es.dati
    for index, items in enumerate(lista):
        if len(items)%2 == 0:
            lista[index] = items.upper()
    es.consegna(lista)

def es16():
    es = Verifica.inizia_esercizio(16)
    print(es)
    lista = es.dati
    parole= ""
    for index, items in enumerate(lista):
        if index < len(lista) - 1:
           parole += items + " "
        else:
            parole += items
    print(parole)
    es.consegna(parole)

def es17():
    es = Verifica.inizia_esercizio(17)
    print(es)
    lista = es.dati
    lettere = ""
    for l in lista:
        lettere += l[-1]
    es.consegna(lettere)

def es18():
    es = Verifica.inizia_esercizio(18)
    print(es)
    lista = es.dati
    lettere = ""
    for l in lista:
        if len(l) > 4:
            lettere += l[0]
            print(lettere)
    es.consegna(lettere)

def es19():
    es = Verifica.inizia_esercizio(19)
    print(es)
    numero = es.dati
    divisori = []
    for i in range(1, numero + 1):
        if numero%i == 0:
            divisori.append(i)
    print(divisori)
    es.consegna(divisori)

def es20():
    es = Verifica.inizia_esercizio(20)
    
    diz = es.dati
    lista_numero = []
    lista_figli = []
    for l in diz:
        for d in l:
            if d == "figli":
                lista_figli = l["figli"]
                lista_len = len(lista_figli)
                print(lista_len)      
                lista_numero.append(lista_len)
    print(lista_figli)
    es.consegna(lista_numero)

def es21():
    es = Verifica.inizia_esercizio(21)
    print(es)
    lista = es.dati
    lista_m5 = []
    for l in lista:
        if l <= 5:
            lista_m5.append(l)
    es.consegna(lista_m5)

def es22():
    es = Verifica.inizia_esercizio(22)
    print(es)
    lista = es.dati
    lista_36 = []
    for l in lista:
        if l >= 3 and l <= 6:
            lista_36.append(l)
    es.consegna(lista_36)

def es23():
    es = Verifica.inizia_esercizio(23)
    print(es)
    lista = es.dati
    somma_anni = 0
    for l in lista:
        somma_anni += l["anni"]
    es.consegna(somma_anni)

def es24():
    es = Verifica.inizia_esercizio(24)
    print(es)
    lista = es.dati
    lista_nomi = []
    for l in lista:
        print(l["cognome"][0], l["nome"])
        if l["cognome"][0] == "C":
            lista_nomi.append(l["nome"])
            print(lista_nomi)
    es.consegna(lista_nomi)

def es25():
    es = Verifica.inizia_esercizio(25)
    print(es)
    lista = es.dati
    numero_a = 0
    for l in lista:
        for s in l:
            if s == "a":
                numero_a += 1
    es.consegna(numero_a)

def es26():
    es = Verifica.inizia_esercizio(26)
    print(es)
    lista = es.dati
    lista_i = []
    for l in lista:
        lista_i.append(l * -1)
    es.consegna(lista_i)

def es27():
    es = Verifica.inizia_esercizio(27)
    print(es)
    diz = es.dati
    lista_tot = []
    for l in diz["negozio"]:
        if l not in lista_tot:
            lista_tot.append(l)
    for l in diz["magazzino"]:
        if l not in lista_tot:
            lista_tot.append(l)
            print(lista_tot)
    lista_tot.sort()
    es.consegna(lista_tot)

def es28():
    es = Verifica.inizia_esercizio(28)
    print(es)
    diz = es.dati
    lista_n = []
    lista_tot = []
    lista_tott = []
    diz_inv = {}
    for l in diz["negozio"]:
        lista_tott.append(l)
        if l not in lista_n:
            lista_n.append(l)
            lista_tot.append(l)
    for l in diz["magazzino"]:
        lista_tott.append(l)
    for l in lista_tot:
        valore = 0
        for i in lista_tott:
            if l == i:
                valore += 1
                diz_inv[l] = valore
    print(diz_inv)
    es.consegna(diz_inv)

def es29():
    es = Verifica.inizia_esercizio(29)
    numero = es.dati
    f = 0
    for i in range(numero):
        f = f * (i + 1)
        print(i + 1)
    print(f)
    es.consegna(f)

es29()
Verifica.stampa_voto()
