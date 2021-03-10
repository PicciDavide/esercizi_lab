class Prodotto:
    def __init__(self, nome):
        self.nome = nome
    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo

libro = Prodotto("libro")
libro.assegna_prezzo(3)
print(libro.prezzo)