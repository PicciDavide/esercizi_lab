"""Alla fine della giornata di elezioni per il ballottaggio tra due candidati, si aquisiscono i voti ottenuti dai due candidati.
Scrivi il programma che calcoli le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore"""

voti1 = int(input("voti primo candidato "))
nome1 = input("nome del primo candidato ")
voti2 = int(input("voti del secondo candidato "))
nome2 = input("nome del secondo candidato ")
voti_tot = voti1 + voti2
print("il primo candidato ha ottenuto il:", int((voti1/voti_tot)*100), "% dei voti")
print("il secondo candidato ha ottenuto il:", int((voti2/voti_tot)*100), "% dei voti")
if voti1 > voti2:
  print("e ha vinto", nome1)
elif voti1 < voti2:
  print("e ha vinto", nome2)
else:
  print("è un pareggio")
