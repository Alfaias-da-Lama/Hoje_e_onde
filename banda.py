import menu
import logincadas as lc
import datetime as dt
import lcmolde as molde


def mostrar_feedback(destinatario):
    """essa função mostra ao usuario de banda ou local os feedbacks dos shows que ja passaram em formato de tabela
        Parameters:
            destinatario (str): o nome da banda ou local que está procurando os feedbacks"""
    try:
        mostrar = False
        shows = dp.getlist('agenda.csv')
        valshows = dp.getlistagenda()
        for linha in shows:
            if not(linha in valshows):
                show = molde.show(linha)
                if show.feedback and (show.banda == destinatario or show.local == destinatario):
                    for mensagem in show.mensagem.split('/'):
                        print(f"{show.local}, {show.data} --> {mensagem}")
                        mostrar = True
                else:
                    continue
            else:
                continue
        if not mostrar:
            print("Sem feedbacks para shows realizados ainda")
    except:
        print("\33[31mErro ao mostrar shows\33[m")


def alterarbanda(arq, usuario):
    """essa função serve para alterar uma linha específica do arquivo perfilXbanda, usada para
    alterar dados de cadastro de usuarios tipo banda
        Parameters:
            arq (str): nome do arquivo que vai ser alterado
            usuario (obj): usuario como objeto que vai ser usado na função de pegar perfil"""
    try:
        prosseguir = True
        linha = dp.pegarperfil(arq, usuario)
        memoria_csv = dp.getlist(arq)
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
                        if lc.validaruser(usuario=usuario, arqlocal='perfilXlocais.csv', arqbanda='perfilXbandas.csv', arqpublico='perfilXpublico.csv'):
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
            print('\33[31mCadastro atualizado!, faça login novamente\33[m')
        else:
            print( '\33[31mCancelando operação... \33[m')
    except(KeyboardInterrupt):
        print("\33[31mCancelando operação\33[m")


def alterarartist(arq, usuario):
    """essa função serve para alterar uma linha específica do arquivo perfilXbanda, usada para
    alterar dados de cadastro de usuarios do tipo artista
        Parameters:
            arq (str): nome do arquivo que vai ser alterado
            usuario (obj): usuario como objeto que vai ser usado na função de pegar perfil"""
    prosseguir = True
    linha = dp.pegarperfil(arq, usuario)
    memoria_csv = dp.getlist(arq)
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
                    if lc.validaruser(usuario=usuario, arqlocal='perfilXlocais.csv', arqbanda='perfilXbandas.csv', arqpublico='perfilXpublico.csv'):
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
    """essa função é um menu com as funções designadas aos usuarios de bandas e artistas
        Parameters:
            usuario (obj): recebe o usuario como objeto para ser usados nas outras funções associadas"""
    try:
        while True:
            resposta = menu.menu2('Página de Banda', ['Ver outras bandas','Ver locais', 'Ver agenda', 'Alterar perfil', "Ver feedbacks", 'Sair'])
            if resposta == 1:
                dp.mostrarbanda()
            elif resposta == 2:
                dp.mostrarlocal(contato=True)
            elif resposta == 3:
                dp.mostraragenda()
            elif resposta == 4:
                if usuario.tipo == 'artista':
                    alterarartist(arq='perfilXbandas.csv', usuario=usuario)
                else:
                    alterarbanda(arq='perfilXbandas.csv', usuario=usuario)
            elif resposta == 5:
                mostrar_feedback(usuario.usuario)
            elif resposta == 6:
                break
    except(KeyboardInterrupt):
        print("\33[31mVoltando ao menu principal\33[m")