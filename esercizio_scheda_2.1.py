'''Si definisca una funzione che preso un dizionario di studenti e voti, restituisca
un dizionario con gli studenti suddivisi per intervalli di media di voto: k1
(18,23), k2(24,26) e k3(27,30).
Nel calcolo della media la lode permette di arrotondare all’intero successivo,
nel caso in cui nella lista dei voti non sia presente una lode l’arrotondamento è
per difetto. '''

def media_voti(dizionario_studente_voti):
    import math
    elenco_m = {}
    elenco_i = {}
    for d in dizionario_studente_voti:
        if "lode" in dizionario_studente_voti[d]:
            dizionario_studente_voti[d].remove("lode")
            media = sum(dizionario_studente_voti[d])
            media = math.ceil(media / len(dizionario_studente_voti[d]))
        else:
            media = sum(dizionario_studente_voti[d])
            media = math.floor(media / len(dizionario_studente_voti[d]))
        elenco_m[d] = [media]
    for d in elenco_m:
        voto = elenco_m[d][0]
        if voto > 18 and voto <= 23:
            elenco_i[(18, 23)] = [d]
        elif voto > 23 and voto <= 26:
            elenco_i[(23, 26)] = [d]
        elif voto > 26 and voto <=30:
            elenco_i[(27, 30)] = [d] 
            
    return elenco_i

print(media_voti({"alighieri":[24, 30, 26], "giovanni":[30, 29, 30, "lode"]}))