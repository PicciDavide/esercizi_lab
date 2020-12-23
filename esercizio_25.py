cand1_n = input("nome del primo candidato: ")
cand1_p = int(input("punteggio del primo candidato: "))
cand2_n = input("nome del secondo candidato: ")
cand2_p = int(input("punteggio del secondo candidato: "))
listap = [cand1_p, cand2_p]
listan = [cand1_n, cand2_n]
listap.sort()
listan.sort()
listan.reverse()
print("lista in ordine di punteggio", listap)
print("lista in ordine alfabetico", listan)
