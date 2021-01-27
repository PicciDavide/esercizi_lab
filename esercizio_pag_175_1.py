giorni_ita = {"lunedì":1, "martedì":2, "mercoledì":3, "giovedì":4, "venerdì":5, "sabato":6, "domenica":7}
elenco = sorted(giorni_ita.values())

elenco_ita = giorni_ita.items()
print(elenco_ita,"s")

for i in elenco:
    for item in elenco_ita:
        if item[1] == i:
            print("Traduci", item[0], "in inglese: ")
            giorni_ita[item[0]] = input()
print(sorted(giorni_ita.items()))
