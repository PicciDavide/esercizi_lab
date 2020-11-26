voti1 = int(input("voti primo candidato "))
voti2 = int(input("voti del secondo candidato "))
voti_tot = voti1 + voti2
print("il primo candidato ha ottenuto il:", int((voti1/voti_tot)*100), "% dei voti")
print("il secondo candidato ha ottenuto il:", int((voti2/voti_tot)*100), "% dei voti")
if voti1 > voti2:
  print("e ha vinto il primo candidato")
elif voti1 < voti2:
  print("e ha vinto il secondo candidato")
else:
  print("è un pareggio")
