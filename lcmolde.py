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
        self.idx_show = perfil[3].split("/")
        self.show = []
        self.mensagem = True

    
    def regatar_shows(self):
        shows = bd.getlist('agenda.csv')
        for numero in idx_show:
            self.show.append(show(shows[numero]))


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
        with open('perfilXpublico.csv', 'w', encoding='utf-8') as file:
            for publico in memoria_csv:
                if publico[0] == self.usuario and publico[1] == self.senha:
                    idx = ("/").join(self.idx_show)
                    pulbico = f"{self.usuario};{self.senha};{idx}"
                file.write(publico)



class show:
    def __init__(self,show):
        self.idx = show[0]
        self.banda = show[1]
        self.local = show[2]
        self.data = show[3]
        self.horastart = show[4]
        self.horaend = show[5]
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
        nota = float(input(f"Dê uma nota de 0-5 sobre o show da {self.banda} no {self.local}: "))
        mensagem = input(f'Dê seu feedback sobre o show da {self.banda} no {self.local}: ')
        if self.feedback:
            self.mensagem += f'/{usuario.usuario}- nota: {nota} - {mensagem}'
        else:
            self.mensagem += f'{usuario.usuario}- nota: {nota} - {mensagem}'
        self.feedback = True
    def salvar_dados(self):
        """salva as alterações em relação a shows seguidos no arquivo csv"""
        memoria_csv = bd.getlist('agenda.csv')
        for show in memoria_csv:
            if show[0] == self.banda:
                if self.feedback:
                    show = [self.banda, self.local, self.data, self.horastart, self.horaend]
                else:
                    show = f"{self.banda};{self.local};{self.data};{self.horastart};{self.horaend};{self.mensagem}"
        with open('agenda.csv', 'w', encoding='utf-8') as file:
            for show in memoria_csv:
                file.write(show)