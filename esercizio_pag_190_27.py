rubrica = {"br1":"0522 149 3278", "gianni":"06 2423571", "anna":"06 88972866", "marco":"06 290395", "giulio":"06 83978868"}
while True:
    try:
        nome = input("Inserire il nome ")
        numero = rubrica[nome]
        print("Il numero è", numero)
    except KeyError:
        print("Il nome non è presente nell'elenco")
    ripeti = input("Vuoi ripetere la ricerca?(si no) ")
    if ripeti.lower() == "no":
        break 