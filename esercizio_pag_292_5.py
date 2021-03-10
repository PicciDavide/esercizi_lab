'Elenca proprietà e metodi della classe Prodotto'

class Prodotto:
    def __init__(self, nome):
        self.nome = nome

libro = Prodotto("libro")

for i in dir(libro):
    print(i)