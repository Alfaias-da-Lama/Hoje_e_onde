import menu
import logincadas as lc


def getlist(arq):
    with open(arq, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
        for linha in range(len(conteudo)):
            conteudo[linha] =conteudo[linha].split(';')
            for palavra in range(len(conteudo[linha])):
               conteudo[linha][palavra] =conteudo[linha][palavra].strip()
    return(conteudo)


def mostrartabela(excluir=[0,1,2,7], content=[]):
    for index, linha in enumerate(content):
        for palindex, palavra in enumerate(linha):
            if not palindex in excluir:
                if palavra == 'NaN':
                    print('-----'.ljust(20), end=' ')
                else:
                    print(palavra.ljust(20), end=' ')
            else:
                continue
        print()


def mostrartabelafiltro(excluir=[0,1,2,7], content=[], filtro=[]):
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


def mostrarbanda(contato=False):
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


def mostrarlocal(contato = False):
    excluir = [0,1,2]
    if not contato:
        excluir.append(7)
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


def mostraragenda():
    agenda = getlist('agenda.csv')
    mostrartabela(content=agenda)
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


def pegarperfil(arq, usuario):
    memoria_csv = getlist(arq)
    for linha in range(len(memoria_csv)):
        if memoria_csv[linha][0] == usuario.usuario and memoria_csv[linha][1] == usuario.senha:
            break
    return(linha)


def alterarbanda(arq, usuario):
    prosseguir = True
    linha = pegarperfil(arq, usuario)
    memoria_csv = getlist(arq)
    usuario = memoria_csv[linha][0]
    senha = memoria_csv[linha][1]
    tipo = memoria_csv[linha][2]
    nome = memoria_csv[linha][3]
    integrantes = memoria_csv[linha][4]
    endereco = memoria_csv[linha][5]
    tipomusical = memoria_csv[linha][6]
    ctt = memoria_csv[linha][7]
    while True:
        for a in range(len(memoria_csv[linha])):
            print(memoria_csv[linha][a], end=' ')
        print('\no que voce deseja alterar?')
        escolha = menu.menu(['usuario', 'senha', 'nome', 'integrantes', 'bairro', 'estilo', 'contato', 'salvar alterações', 'cancelar'])
        if escolha == 1:
                while True:
                    while True:
                        usuario = input('insira seu nome de usuário: ')
                        if usuario.isalpha():
                            break
                    else:
                        print('\33[31mEsperado pelo menos 1 letra no usuario\33[m')
                    if lc.validaruser(usuario=usuario, arqlocal='perfilXlocais.csv', arqbanda='perfilXbandas.csv'):
                        break
                    else:
                        print(f'ja existe um usuario com o cadastro {usuario}')
                        continue
        elif escolha == 2:
            while True:
                while True:
                    senha = input('escolha uma senha: ')
                    certo = True
                    aviso = True
                    if len(senha) < 8:
                        print('\33[31ma senha precisa ter 8 caracteres ou mais\33[m')
                        certo = False
                    for a in senha:
                        if a in "~!@#$%^&*_-+=`|\()}{[]:;'<>,.?/" and aviso:
                            print('\33[31msenha não pode conter caracteres especiais\33[m')
                            certo = False
                            aviso = False
                    if certo:
                        break
                    else:
                        continue
                confirmacao = input('confirme sua senha: ')
                if senha == confirmacao:
                    break
                else:
                    print('\33[31msenhas não condizem\33[m')
        elif escolha == 3:
            nomebanda = input('insira o novo nome da banda ou artista: ')
        elif escolha == 4:
            numero = input('qual o numero de integrantes da sua banda: ')
            integrantes = []
            for integrante in range(numero):
                pessoa = input(f'insira o nome do integrante {a+1}: ')
                integrantes.append(pessoas)
            integrantes = '/'.join(integrantes)
        elif escolha == 5:
            bairro = input('insira o bairro da sua banda: ')
        elif escolha == 6:
            estilo = input('insira o estilo musical da sua banda: ')
        elif escolha == 7:
            ctt = []
            while True:
                contato = input('digite um numero de celular ou email para contato, ou insira 0 para parar: ')
                if contato == '0':
                    break
                else:
                    ctt.append(contato)
            ctt = '/'.join(ctt)
        elif escolha == 8:
            break
        elif escolha == 9:
            prosseguir = False
            break
        memoria_csv[linha] = [usuario, senha, tipo, nome, integrantes, endereco, tipomusical, ctt]
    print(memoria_csv[linha])
    escolha = input('Digite [ok] para confirmar ou [cancelar] para não registrar as mudanças: ')
    if prosseguir and escolha != 'cancelar':
        with open(arq, 'w', encoding='utf-8') as arquivo:
            arquivo.write('usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato\n')
        with open(arq, 'a', encoding='utf-8') as arquivo:
            for linha in range(1, len(memoria_csv)):
                arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5]};{memoria_csv[linha][6]};{memoria_csv[linha][7].strp()}\n')
        print('\33[31mCadastro atualizado!\33[m')
    else:
        print( '\33[31mCancelando operação... \33[m')


def alterarartist(arq, usuario):
    prosseguir = True
    linha = pegarperfil(arq, usuario)
    memoria_csv = getlist(arq)
    usuario = memoria_csv[linha][0]
    senha = memoria_csv[linha][1]
    tipo = memoria_csv[linha][2]
    nome = memoria_csv[linha][3]
    integrantes = memoria_csv[linha][4]
    endereco = memoria_csv[linha][5]
    tipomusical = memoria_csv[linha][6]
    ctt = memoria_csv[linha][7]
    while True:
        for a in range(len(memoria_csv[linha])):
            print(memoria_csv[linha][a], end=' ')
        print('\no que voce deseja alterar?')
        escolha = menu.menu(['usuario', 'senha', 'nome', 'bairro', 'estilo', 'contato', 'salvar alterações'])
        if escolha == 1:
                while True:
                    while True:
                        usuario = input('insira seu nome de usuário: ')
                        if usuario.isalpha():
                            break
                    else:
                        print('\33[31mEsperado pelo menos 1 letra no usuario\33[m')
                    if lc.validaruser(usuario=usuario, arqlocal='perfilXlocais.csv', arqbanda='perfilXbandas.csv'):
                        break
                    else:
                        print(f'ja existe um usuario com o cadastro {usuario}')
                        continue
        elif escolha == 2:
            while True:
                while True:
                    senha = input('escolha uma senha: ')
                    certo = True
                    aviso = True
                    if len(senha) < 8:
                        print('\33[31ma senha precisa ter 8 caracteres ou mais\33[m')
                        certo = False
                    for a in senha:
                        if a in "~!@#$%^&*_-+=`|\()}{[]:;'<>,.?/" and aviso:
                            print('\33[31msenha não pode conter caracteres especiais\33[m')
                            certo = False
                            aviso = False
                    if certo:
                        break
                    else:
                        continue
                confirmacao = input('confirme sua senha: ')
                if senha == confirmacao:
                    break
                else:
                    print('\33[31msenhas não condizem\33[m')
        elif escolha == 3:
            nomebanda = input('insira o novo nome artistico: ')
        elif escolha == 4:
            bairro = input('insira o bairro da sua banda: ')
        elif escolha == 5:
            estilo = input('insira o estilo musical da sua banda: ')
        elif escolha == 6:
            ctt = []
            while True:
                contato = input('digite um numero de celular ou email para contato, ou insira 0 para parar: ')
                if contato == '0':
                    break
                else:
                    ctt.append(contato)
            ctt = '/'.join(ctt)
        elif escolha == 7:
            break
        memoria_csv[linha] = [usuario, senha, tipo, nome, integrantes, endereco, tipomusical, ctt]
    print(memoria_csv[linha])
    escolha = input('Digite [ok] para confirmar ou [cancelar] para não registrar as mudanças: ')
    if prosseguir and escolha != 'cancelar':
        with open(arq, 'w', encoding='utf-8') as arquivo:
            arquivo.write('usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato\n')
        with open(arq, 'a', encoding='utf-8') as arquivo:
            for linha in range(1, len(memoria_csv)):
                arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5]};{memoria_csv[linha][6]};{memoria_csv[linha][7].strip()}\n')
        print('\33[31mCadastro atualizado!\33[m')
    else:
        print( '\33[31mCancelando operação... \33[m')


def pagina_de_banda(usuario):
    while True:
        resposta = menu.menu2('Página de Banda', ['Ver outras bandas','Ver locais', 'Ver agenda', 'Alterar perfil', 'Sair'])
        if resposta == 1:
            mostrarbanda()
        elif resposta == 2:
            mostrarlocal(contato=True)
        elif resposta == 3:
            mostraragenda()
        elif resposta == 4:
            if usuario.tipo == 'artista':
                alterarartist(arq='perfilXbandas.csv', usuario=usuario)
            else:
                alterarbanda(arq='perfilXbandas.csv', usuario=usuario)
        elif resposta == 5:
            break