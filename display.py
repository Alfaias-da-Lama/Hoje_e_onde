import display as dp

def getlist(arq):
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


def mostrartabela(excluir=[0,1,2,7], content=[]):
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
    try:
        excluir = [0,1,2]
        if not contato:
            excluir.append(7)
        bandas = getlist('perfilXbandas.csv')
        mostrartabela(content=bandas)
        resposta = menu.menu(['procurar por nome', 'procurar por estilo', 'procurar por endereço'])
        if resposta == 1:
            filtro = input('por qual nome voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[3, filtro], excluir=excluir)
        elif resposta == 2:
            filtro = input('por qual estilo musical deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[4, filtro], excluir=excluir)
        elif resposta == 3:
            filtro = input('por qual bairro voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[5, filtro], excluir=excluir)
    except Exception as e:
        print(f"\33[31mErro ao executar função: {e}\33[m")


def mostrarlocal(contato = False):
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
    try:
        agenda = getlistagenda()
        mostrartabela(content=agenda, excluir = [])
        resposta = menu.menu(['procurar por bairro', 'procurar por local', 'procurar por banda'])
        if resposta == 1:
            filtro = input('por qual bairro voce deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[3, filtro], excluir=[999])
        elif resposta == 2:
            filtro = input('por qual local deseja buscar? ')
            mostrartabelafiltro(content=locais, filtro=[1, filtro], excluir=[999])
        elif resposta == 3:
            filtro = input('por qual banda voce deseja buscar? ')
            mostrartabelafiltro(content=bandas, filtro=[0, filtro], excluir=[999])
    except Exception as e:
        print(f"\33[31mErro ao executar função: {e}\33[m")


def pegarperfil(arq, usuario):
    try:
        memoria_csv = dp.getlist(arq)
        for linha in range(len(memoria_csv)):
            if memoria_csv[linha][0] == usuario.usuario and memoria_csv[linha][1] == usuario.senha:
                break
        return(linha)
    except(IndexError):
        print("\33[31mErro de lista\33[m")