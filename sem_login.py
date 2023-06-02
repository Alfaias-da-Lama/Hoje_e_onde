import datetime

def remover_acentos(texto):
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a', 'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o', 'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'ç': 'c', 'Ç': 'C'
    }
    texto_sem_acentos = ''.join(acentos.get(char, char) for char in texto)
    return texto_sem_acentos


def verBandas(nome):
    try:
        file = open(nome, 'r')
        for linha in file:
            dados_linha = linha.split(';')
            print(f'{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}{dados_linha[6]:^15}')
    except FileNotFoundError:
        return "Deu erro na busca de arquivo"


def filtrar_bandas(nome):
    try:
        filtro = str(input("Digite a sua pesquisa: "))
        file = open(nome, "r")
        print(f'{"Tipo":^15}{"Nome":^15}{"Integrantes":^15}{"Endereço":^15}{"Tipo Musical":^15}')
        encontrado = False
        for linha in file:
            dados_linha = linha.lower().split(';')
            for j in dados_linha:
                if remover_acentos(j) == remover_acentos(filtro):
                    print(f'{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}{dados_linha[6]:^15}')
                    encontrado = True
        if not encontrado:
            print('Não existe agenda de acordo com a sua pesquisa')
        file.close()
    except TypeError as e:
        print("\33[31mErro: Entrada inválida.\33[m,", e)


def verLocais(nome):
    try:
        file = open(nome, 'r')
        for linha in file:
            dados_linha = linha.split(';')
            print(f'{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}')
    except FileNotFoundError:
        return "Deu erro na busca de arquivo"


def filtrar_locais(nome):
    try:
        filtro = str(input("Digite a sua pesquisa: "))
        file = open(nome, "r")
        print(f'{"Tipo":^15}{"Nome":^15}{"Endereço":^15}{"Tipo Musical":^15}')
        encontrado = False
        for linha in file:
            dados_linha = linha.lower().split(';')
            for j in dados_linha:
                if remover_acentos(j) == remover_acentos(filtro):
                    print(f'{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}')
                    encontrado = True
        if not encontrado:
            print('Não existe agenda de acordo com a sua pesquisa')
        file.close()
    except TypeError as e:
        print("\33[31mErro: Entrada inválida.\33[m,", e)


def ver_agenda(nome):
    try:
        file = open(nome, 'r')
        data_hoje = datetime.datetime.now().date()
        for linha in file:
            dados_linha = linha.split(';')
            dados_linha[4] = dados_linha[4].replace('\n', '')
            data_eventos = datetime.datetime.strptime(dados_linha[3], '%d/%m/%Y').date()
            if data_hoje <= data_eventos:
                print(f'{dados_linha[1]:^15}{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}')
    except FileNotFoundError:
        return "Deu erro na busca de arquivo"
    
def filtrar_agenda(nome):
    try:
        filtro = str(input("Digite a sua pesquisa: "))
        file = open(nome, "r")
        print(f'{"Banda":^15}{"Local":^15}{"Data":^15}{"Horário Início":^15}{"Horário Encerramento":^15}')
        encontrado = False
        data_hoje = datetime.datetime.now().date()
        for linha in file:
            dados_linha = linha.lower().split(';')
            dados_linha[4] = dados_linha[4].replace('\n', '')
            data_eventos = datetime.datetime.strptime(dados_linha[3], '%d/%m/%Y').date()
            for j in dados_linha:
                if remover_acentos(j) == remover_acentos(filtro) and data_hoje <= data_eventos:
                    print(f'{dados_linha[1]:^15}{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}')
                    encontrado = True
        if not encontrado:
            print('Não existe agenda de acordo com a sua pesquisa')
        file.close()
    except TypeError as e:
        print("\33[31mErro: Entrada inválida.\33[m,", e)


def opcoes_sem_login(resposta):
    answer = input('Deseja pesquisar? sim ou não? ')
    if answer.lower() != 'sim':
        res = input('Digite o que deseja ver: Agenda, Locais ou Bandas? ')
        if res.lower() == 'agenda':
            ver_agenda(nome='agenda.csv')
        elif res.lower() == 'locais':
            verLocais(nome='perfilXlocais.csv')
        elif res.lower() == 'bandas':
            verBandas(nome='perfilXbandas.csv')
    else:
        res1 = input('Onde deseja pesquisar: Agenda, Locais ou Bandas? ')
        if res1.lower() == 'agenda':
            filtrar_agenda(nome='agenda.csv')
        elif res1.lower() == 'locais':
            filtrar_locais(nome='perfilXlocais.csv')
        elif res1.lower() == 'bandas':
            filtrar_bandas(nome='perfilXbandas.csv')
