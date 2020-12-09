def controllo(variabile, range_n1, range_n2):
    if variabile in range(range_n1,range_n2):
        return True
    else:
        return False

while True:
    try:
        quale = int(input("Di cosa vuoi calcolare l'area?\nQuadrato = 0\nRettangolo = 1\nTriangolo = 2\nCerchio = 3\nScrivi il numero corrispondente: "))
        if quale not in range(0,4):
            raise ValueError
        break
    except ValueError:
        print("Puoi solo rispondere con numeri da 0 a 3")
if controllo(quale, 0, 3):
    while True:
        try:
            base = int(input("Inserisci il valore della base: "))
            break
        except ValueError:
            print("Puoi solo inserire numeri interi")
    if controllo(quale, 1, 3):
        while True:
            try:
                altezza = int(input("Inserisci il valore dell'altezza: "))
                break
            except ValueError:
                print("Puoi solo inserire numeri interi")
        if controllo(quale, 1, 2):
            print("L'area del rettangolo è di:", base * altezza)
        else:
            print("L'area del triangolo è di:", (base * altezza)/2)
    else:
        print("L'area del quadrato è di:", base * base)
else:
    while True:
        try:
            raggio = int(input("Inserisci il valore del raggio: "))
            break
        except ValueError:
            print("Puoi solo inserire numeri interi")
    print("L'area del cerchio è di: ", raggio**2*3.14)
    