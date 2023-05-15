class Banda:
    def __init__(self, nomedabanda, integrantes, bairro, tipomusical, ctt):
        self.nome = nomedabanda
        self.integrantes = integrantes
        self.endereço = bairro
        self.estilo = tipomusical
        self.dadosctt = ctt

class Local:
    def __init__(self, nome, endereco, tipomusical, ctt):
        self.nome = nome
        self.endereco = endereco
        self.estilo = tipomusical
        self.dadosctt = ctt 