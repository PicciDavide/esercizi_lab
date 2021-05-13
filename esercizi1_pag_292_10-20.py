class Orologio():
    def __init__(self, ore, minuti, secondi):
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi
    def reset(self):
        self.ore = 0
        self.minuti = 0
        self.secondi = 0
    def set_time(self, ore, minuti, secondi):
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi
    def get_time(self):
        self.time = [self.ore, self.minuti, self.secondi]
        return time

my_orologio = Orologio(10, 50, 12)

class ContrattoTelefonico():
    def __init__(self, nome, credito):
        self.nome = nome
        self.credito = credito
    def reset_credito(self):
        self.credito = 0
    def scala_credito(self, n):
        self.credito -= n

class Trapezio():
    def __init__(self, base, BASE, lato_1, altezza, lato_2 = lato_1):
        self.base = float(base)
        self.BASE = float(BASE)
        self.lato_1 = float(lato_1)
        self.lato_2 = float(lato_2)
        self.altezza = float(altezza)
    def get_area(self):
        self.area = ((self.base + self.BASE) * self.altezza)/2
        return self.area
    def get_perimetro(self):
        self.perimetro = self.base + self.BASE + self.lato_1 + self.lato_2
        return self.perimetro

class Automobile():
    def __init__(self, km_percorsi, litri_usati):
        self.km_percorsi = km_percorsi
        self.litri_usati = litri_usati
    def get_consumo_km(self):
        self.consumo_km = self.litri_usati/self.km_percorsi
        return self.consumo_km

class Libro():
    def __init__(self, titolo, autore, anno, pagine, editore, città, soggetto, InPrestito = False):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.pagine = pagine
        self.editore = editore
        self.città = città
        self.soggetto = soggetto
        self.InPrestito = InPrestito
    def presta(self):
        self.InPrestito = True
    def restituisci(self):
        self.InPrestito = False

class Punto():
    def __init__(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

class Utente():
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
    def set_utente(self, nome, password):
        self.nome = nome
        self.password = password

class Studente():
    def __init__(self, nome, scuola):
        self.nome = nome
        self.scuola = scuola
studenti = []
while True:
    nome = input("Nome dello studente: ")
    scuola = input("Nome della scuola: ")

    studenti.append(Studente(nome, scuola))
    
    ripeti = input("Vuoi inserire un altro studente? si/no ")

    if ripeti == no:
        break

def elenco_studenti():
    elenco = []
    for i in studenti:
        elenco.append(studenti[i.nome])
    return elenco

    