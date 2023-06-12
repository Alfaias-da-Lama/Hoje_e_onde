import display as dp
import menu

def getlist(arq):
    """essa função cria uma matriz separando os valores do arquivo csv por linha e palavra
        Parameters:
            arq (str): recebe como parametro uma string com o nome do arquivo que vai gerar a matriz
        
        Returns:
            conteudo (list): retorna uma matriz com todas os valores do arquivos separados por linha e por valor"""
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.readlines()
            for linha in range(len(conteudo)):
                conteudo[linha] =conteudo[linha].split(';')
                for palavra in range(len(conteudo[linha])):
                    conteudo[linha][palavra] =conteudo[linha][palavra].strip()
        return(conteudo)
    except(FileNotFoundError):
        print("\33[31mArquivo não encontrado reinicie o programa\33[m")


def getlistagenda():
    """essa função pega o arquivo da agenda e cria uma matriz com os shows, filtrando 
    pela data, se o show ja aconteceu de acordo com a data atual ele não é selecionado
        Returns:
            conteudofiltrado (list): devolve uma matriz com o conteudo do arquivo agenda.csv separado por linha e por palavra"""
    try:
        conteudo = getlist('agenda.csv')
        conteudofiltrado = []
        for index, linha in enumerate(conteudo):
            if index == 0:
                conteudofiltrado.append(linha)
            else:
                try:
                    if (dt.datetime.now().year <= int(linha[2].split('/')[2])): 
                        conteudofiltrado.append(linha)
                    elif (dt.datetime.now().year == int(linha[2].split('/')[2])):
                        if (dt.datetime.now().month <= int(linha[2].split('/')[1])):
                            conteudofiltrado.append(linha)
                        elif (dt.datetime.now().month == int(linha[2].split('/')[1])):
                            if (dt.datetime.now().day <= int(linha[2].split('/')[0])):
                                conteudofiltrado.append(linha)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                except(IndexError):
                    continue
        return(conteudofiltrado)
    except(FileNotFoundError):
        print("\33[31mArquivo não encontrado reinicie o programa\33[m")


def mostrartabela(excluir=[0,1,7], content=[]):
    """recebe uma matriz e coloca ela no terminal em formato de tabela, pode excluir alguns termos da tabela
    por defalt vem excluindo o 0,1,7 que corresponde ao login, senha e contato
        Parameters:
            excluir (list): lista dos index a serem excluidos
            content (list): lista que vai ser formatada no terminal"""
    try:
        for index, linha in enumerate(content):
            if index > 0:
                print(f'{index}'.ljust(5), end=' ')
            else:
                print('index', end =' ')
            for palindex, palavra in enumerate(linha):
                if not palindex in excluir:
                    if palavra == 'NaN':
                        print('-----'.ljust(20), end=' ')
                    else:
                        print(palavra.ljust(20), end=' ')
                else:
                    continue
            print()
    except Exception as e:
        print(f"\33[31mErro ao mostrar tabela: {e}\33[m")


def mostrartabelafiltro(excluir=[0,1,2,7], content=[], filtro=[]):
    """essa função formata uma matriz em tabela no terminal, alem disso ela filtra o que ta mostrando
    por um filtro que vem como parametro
        Parameters:
            excluir (list): lista dos index a serem excluidos
            content (list): lista que vai ser formatada no terminal
            filtro (list): lista para filtragem no termo 0 vem o index que vai ser filtrado, e no index 1 
            vem a palavra de referencia para o filtro"""
    try:
        for index, linha in enumerate(content):
            for palindex, palavra in enumerate(linha):
                if filtro[1] in linha[filtro[0]] or index == 0:
                    if not palindex in excluir:
                        if palavra == 'NaN':
                            print('-----'.ljust(20), end=' ')
                        else:
                            print(palavra.ljust(20), end=' ')
                    else:
                        continue
                else:
                    continue
            print()
    except Exception as e:
        print(f"\33[31mErro ao mostrar tabela: {e}\33[m")


def mostrarbanda(contato=False):
    """essa função mostra o conteudo do arquivo perfilXbandas e pergunta ao usuario se ele quer fazer algum filtro em sua busca
    caso queira há 3 opções de filtro que podem ser aplicadas
        Parameters:
            contato (bool): essa função passa como verdadeira se o usuario tem acesso ao contato das bandas"""
    try:
        excluir = [0,1,2]
        if not contato:
            excluir.append(7)
        bandas = getlist('perfilXbandas.csv')
        mostrartabela(content=bandas)
        resposta = menu.menu(['procurar por nome', 'procurar por estilo', 'procurar por endereço', 'voltar'])
        if resposta == 1:
            filtro = input('por qual nome voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[3, filtro], excluir=excluir)
        elif resposta == 2:
            filtro = input('por qual estilo musical deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[4, filtro], excluir=excluir)
        elif resposta == 3:
            filtro = input('por qual bairro voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[5, filtro], excluir=excluir)
        elif resposta == 4:
            pass
    except Exception as e:
        print(f"\33[31mErro ao executar função: {e}\33[m")


def mostrarlocal(contato = False):
    """essa função mostra o conteudo do arquivo perfilXlocais e pergunta ao usuario se ele quer fazer algum filtro em sua busca
    caso queira há 3 opções de filtro que podem ser aplicadas
        Parameters:
            contato (bool): essa função passa como verdadeira se o usuario tem acesso ao contato dos locais"""
    try:
        excluir = [0,1,2]
        if not contato:
            excluir.append(6)
        locais = getlist('perfilXlocais.csv')
        mostrartabela(content=locais)
        resposta = menu.menu(['procurar por nome', 'procurar por bairro', 'procurar por estilo musical'])
        if resposta == 1:
            filtro = input('por qual nome voce deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[3, filtro], excluir=excluir)
        elif resposta == 2:
            filtro = input('por qual bairro deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[6, filtro], excluir=excluir)
        elif resposta == 3:
            filtro = input('por qual estilo musical voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[8, filtro], excluir=excluir)
    except Exception as e:
        print(f"\33[31mErro ao executar função: {e}\33[m")


def mostraragenda():
    """essa função mostra o conteudo do arquivo agenda e pergunta ao usuario se ele quer fazer algum filtro em sua busca
    caso queira há 3 opções de filtro que podem ser aplicadas"""
    try:
        agenda = getlistagenda()
        mostrartabela(content=agenda, excluir = [])
        resposta = menu.menu(['procurar por bairro', 'procurar por local', 'procurar por banda', 'sair'])
        if resposta == 1:
            filtro = input('por qual bairro voce deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[3, filtro], excluir=[999])
        elif resposta == 2:
            filtro = input('por qual local deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[1, filtro], excluir=[999])
        elif resposta == 3:
            filtro = input('por qual banda voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[0, filtro], excluir=[999])
        elif resposta == 4:
            pass
    except Exception as e:
        print(f"\33[31mErro ao executar função: {e}\33[m")


def pegarperfil(arq, usuario):
    """essa função verifica onde se o usuario se encontra no arquivo e devolve a linha dele
        Parameters:
            arq (str): recebe o nome do arquivo como string
            usuario (obj): recebe o usuario como objeto para procurar seu login e senha"""
    try:
        memoria_csv = dp.getlist(arq)
        for linha in range(len(memoria_csv)):
            if memoria_csv[linha][0] == usuario.usuario and memoria_csv[linha][1] == usuario.senha:
                break
        return(linha)
    except(IndexError):
        print("\33[31mErro de lista\33[m")