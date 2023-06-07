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
        self.show.append(show)
        self.mensagem = False
    def verify(self):
        for index, show in self.show:
            if show.temporest <= datetime.date(0000/00/00) and not show.feedback:
                self.show.pop(index)
                return(False)
            elif show.temporest <= datetime.date(0000/00/00) and show.feedback:
                print(f'Você pode dar o feedback do show {show.banda} no {show.lugar}!')
                return(True)
        if self.show == []:
            self.mensagem = True
    def salvar_dados(self):
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
    def feedback(usuario):
        mensagem = input(f'Dê seu feedback sobre o show da {self.banda} no {self.local}: ')
        if self.feedback:
            self.mensagem += f'/{usuario.usuario} - {mensagem}'
        else:
            self.mensagem += f'{usuario.usuario} - {mensagem}'
        self.feedback = True
    def salvar_dados(self):
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