class Atleta:
    def __init__(self, Visita_Medica, nome_squadra):
        self.Visita_Medica = Visita_Medica
        self.nome_squadra = nome_squadra
    
    def effettua_visita(self):
        self.Visita_Medica = True
    
    def stampa_dati(self):
        print(self.Visita_Medica, self.nome_squadra)
