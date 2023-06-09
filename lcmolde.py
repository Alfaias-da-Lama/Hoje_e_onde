import banda as bd
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
        self.mensagem = True
    def seguindo(self, show):
        """adiciona mais um show que o cadastrado como Público vai seguir
            Parameters:
                show (obj): o show como objeto no molde contido nesse arquivo que o usuario quer seguir"""
        self.show.append(show)
        self.mensagem = False
    
    
    def salvar_dados(self):
        """função que pega as alterações feitas em relação a shows seguidos e feedbacks e salva
        no arquivo csv"""
        memoria_csv = bd.getlist('perfilXpublico.csv')
        for publico in memoria_csv:
            if publico[0] == self.usuario:
                pulbico = [self.usuario, self.senha, self.show]
        with open('perfilXpublico.csv', 'w', encoding='utf-8') as file:
            for publico in memoria_csv:
                file.write(publico)



class show:
    def __init__(self,show):
        self.banda = show[0]
        self.local = show[1]
        self.data = show[2]
        self.horastart = show[3]
        self.horaend = show[4]
        try:
            self.mensagem = show[5]
        except(IndexError):
            self.feedback = False
        else:
            self.feedback = True
    def temporest(self):
        """Pega a hora do show e calcula quantos dias faltam para o show começar
            Returns:
                delta.days (int): quantos dias faltam para o show começar"""
        datapadrao = self.data.split('/')
        dia = int(datapadrao[0])
        mes = int(datapadrao[1])
        ano = int(datapadrao[2])
        datapadrao = dt.date(ano, mes, dia)
        hoje = dt.date.today()
        if datapadrao > hoje:
            delta = datapadrao - hoje
        elif datapadrao <= hoje:
            delta = hoje - datapadrao
        return(delta.days)
    def feedback(self, usuario):
        """cria uma mensagem de feedback no show, para ser salvo posteriormente
            Parameters:
                usuario (object): o usuario que está criando a mensagem de feedback"""
        mensagem = input(f'Dê seu feedback sobre o show da {self.banda} no {self.local}: ')
        if self.feedback:
            self.mensagem += f'/{usuario.usuario} - {mensagem}'
        else:
            self.mensagem += f'{usuario.usuario} - {mensagem}'
        self.feedback = True
    def salvar_dados(self):
        """salva as alterações em relação a shows seguidos no arquivo csv"""
        memoria_csv = bd.getlist('agenda.csv')
        for show in memoria_csv:
            if show[0] == self.banda:
                if self.feedback:
                    show = [self.banda, self.local, self.data, self.horastart, self.horaend]
                else:
                    show = [self.banda, self.local, self.data, self.horastart, self.horaend, self.mensagem]
        with open('agenda.csv', 'w', encoding='utf-8') as file:
            for show in memoria_csv:
                file.write(show)