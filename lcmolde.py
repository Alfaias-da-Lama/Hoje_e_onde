import datetime as dt

class Banda:
    def __init__(self, perfil):
        self.usuario = perfil[0]
        self.senha = perfil[1]
        self.tipo = perfil[2]
        self.nome = perfil[3]
        self.integrantes = perfil[4]
        self.endereco = perfil[5]
        self.tipo_musical = perfil[6]
        self.contato = perfil[7]

class Local:
    def __init__(self, perfil):
        self.usuario = perfil[0]
        self.senha = perfil[1]
        self.tipo = perfil[2]
        self.nome = perfil[3]
        self.endereco = perfil[4]
        self.tipo_musical = perfil[5]
        self.ctt = perfil[6]

class Publico:
    def __init__(self, perfil):
        self.usuario = perfil[0]
        self.senha = perfil[1]
        self.show = []
        self.mensagem = 'voce atualmente não segue shows'
    def seguindo(self, show):
        self.show.append(show)
#criar classe específica para show parece uma boa ideia