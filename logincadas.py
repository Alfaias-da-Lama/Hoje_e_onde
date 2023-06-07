import lcmolde as lc
import menu
from validate_email import validate_email


def enviaremail(destinatario,usuario,senha):
    import win32com.client as w3
    integracao = w3.Dispatch('outlook.application')
    email = integracao.CreateItem(0)
    email.To = f'{destinatario}'
    email.Subject = 'Recuperacao de senha'
    email.HTMLBody = f"""
    <p> Ola usuario {usuario}</p>
    <p>voce solicitou uma recuperação de senha em nosso app Hoje é onde</p>
    <p>sua senha é: {senha}</p>
    <p>se ainda assim a sua senha não funcionar responda esse e-mail com o assunto: </p>
    <p>ERRO DE SENHA </p>
    <p> que alguem da equipe o atenderá</p>
    <p> atensiosamente: Alfaias da Lama</p>"""
    email.Send()

def validaruser(usuario, arqlocal, arqbanda, arqpublico):
    with open(arqbanda, 'r', encoding='utf-8') as arquivo:
        arqsep = arquivo.readlines()
        memoria = []
        for a in arqsep:
            memoria.append(a.split(';')[0])
        memoria.pop(0)
    with open(arqlocal, 'r', encoding='utf-8') as arquivo:
        arqsep = arquivo.readlines()
        cont = 0
        for a in arqsep:
            if cont >0:
                memoria.append(a.split(';')[0])
            else:
                cont+=1
    with open(arqpublico, 'r', encoding='utf-8') as arquivo:
        arqsep = arquivo.readlines()
    cont = 0
    for a in arqsep:
        if cont >0:
            memoria.append(a.split(';')[0])
        else:
            cont+=1
    validacao = True
    for a in memoria:
        if a == usuario:
            validacao = False
        else:
            continue
    return(validacao)

def validar_email(email):
    from validate_email import validate_email
    valido= validate_email(f'{email}', verify=True)
    return(valido)

def conferirarquivo(nome):
    existencia = True
    try:
        a = open(nome, 'r')
        a.close()
    except:
        #print('\33[31mArquivo não existente, criando arquivo...\33[m')
        existencia = False
    return(existencia)

def criararquivo(nome, cabeçalho):
    existencia = conferirarquivo(nome)
    if not existencia:
        with open(nome, 'w', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{cabeçalho}\n')
        #print('\33[32mArquivo controle.csv criado, com sucesso\33[m')
    else:
        pass
    #else:
        #print('Encontrado arquivo controle.csv')
    return(nome)

def cadastro(arqbanda, arqlocal, arqpublico):
    print('dados do cadastro')
    try:
        while True:
            while True:
                usuario = input('insira seu nome de usuário: ')
                if usuario.isalpha():
                    break
                else:
                    print('\33[31mEsperado pelo menos 1 letra no usuario\33[m')
            if validaruser(usuario=usuario, arqlocal=arqlocal, arqbanda=arqbanda):
                break
            else:
                print(f'ja existe um usuario com o cadastro {usuario}')
                continue
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
        while True:
            email = input('insira seu email: ')
            validacao = validate_email(email)
            if validacao:
                print('\33[32mE-mail válido\33[m')
                break
            else:
                print('\33[31mInsira um e-mail válido\33[m')
        while True:
            escolha = input('qual o tipo de cadastro? [local] [artista] [publico]: ')
            if escolha != 'local' and escolha != 'artista' and escolha != 'publico':
                print('\33[31mSelecione uma opção acima\33[m')
            else:
                break
        if escolha == 'artista':
            grupo = input('voce é artista [solo] ou tem [banda]? ')
            if grupo == 'banda':
                nomebanda = input('qual o nome da sua banda: ')
                solo = False
            elif grupo == 'solo':
                nomebanda = input('qual o seu nome artístico: ')
                solo = True
            if solo:
                estilo = input('qual seu estilo musical: ')
            else:
                estilo = input('qual o estilo musical da banda: ')
            if solo:
                bairro = input('qual o seu bairro: ')
            else:
                bairro = input('digite o bairro da sua banda: ')
            if solo:
                integrantes = 'NaN'
            else:
                qtdinte = int(input('quantos integrantes tem a sua banda: '))
                integrantes = []
                for integrante in range(qtdinte):
                    integrantes.append(input(f'digite o nome do integrante {integrante+1}: '))
                integrantes = '/'.join(integrantes)
            ctt = []
            while True:
                contato = input('insira um contato email ou celular ou 0 para parar: ')
                if contato == '0':
                    break
                else:
                    ctt.append(contato)
            ctt = '/'.join(ctt)
            try:
                with open(arqbanda,'a', newline='', encoding='utf-8') as arquivo:
                    arquivo.write(f'{usuario};{senha};{tipo};{nomebanda};{integrantes};{bairro};{estilo};{ctt}\n')
            except:
                print('\33[31mErro ao cadastrar, tente novamente\33[m')
            else:
                print('\33[33mCadastro realizado com sucesso!\33[m')
                user = lc.Publico([usuario,senha])
                return(['banda',user])
        elif escolha == 'local':
            nomelocal = input('insira o nome do seu local: ')
            endereço = input('insira o endereço do local: ')
            estilo = input('insira o estilo musical de preferencia do local: ')
            tipo = input('insira o tipo do seu local [bar, restaurante, casa de show]: ')
            ctt = []
            while True:
                contato = input('insira um contato email ou celular, ou 0 para encerrar: ')
                if contato == '0':
                    break
                else:
                    ctt.append(contato)
            ctt = '/'.join(ctt)
            try:
                with open(arqlocal,'a', newline='', encoding='utf-8') as arquivo:
                    arquivo.write(f'{usuario};{senha};{tipo};{nomelocal};{endereço};{estilo};{ctt}\n')
            except:
                print('\33[31mErro ao cadastrar, tente novamente\33[m')
            else:
                print('\33[33mCadastro realizado com sucesso!\33[m')
                user = lc.Local([usuario,senha,tipo,nomelocal,endereço,estilo,ctt])
                return('local', user)
        elif escolha == 'publico':
            try:
                with open(arqpublico,'a', newline='', encoding='utf-8') as arquivo:
                    arquivo.write(f'{usuario};{senha}\n')
            except:
                print('\33[31mErro ao cadastrar, tente novamente\33[m')
            else:
                print('\33[33mCadastro realizado com sucesso!\33[m')
                user = lc.Local([usuario,senha,tipo,nomelocal,endereço,estilo,ctt])
                return('publico', user)
    except:
        print('\33[31mErro ao cadastrar\33[m')


def login(arqbanda, arqlocal):
    from getpass import getpass
    banda = False
    temperfil = False
    local = False
    user = input('insira seu usuário: ')
    password = getpass(prompt='insira sua senha: ')
    with open(arqbanda, 'r', newline='', encoding='utf-8') as arquivo:
        perfis = arquivo.readlines()
        for perfil in perfis:
            perfil = perfil.split(';')
            if perfil[0] == user and perfil[1] == password:
                banda = True
                temperfil = True
                usuario = lc.Banda(perfil=perfil)
                return(["banda", usuario])
                break
            else:
                continue
    if not banda:
        with open(arqlocal, 'r', newline='', encoding='utf-8') as arquivo:
            perfis = arquivo.readlines()
            for perfil in perfis:
                perfil = perfil.split(';')
                if perfil[0] == user and perfil[1] == password:
                    local = True
                    print('perfil encontrado')
                    temperfil = True
                    usuario = lc.Local(perfil=perfil)
                    return(["local", usuario])
                    break
                else:
                    continue
    if not banda and not local:
        with open(arqpublico, 'r', newline='', encoding='utf-8') as arquivo:
            perfis = arquivo.readlines()
            for perfil in perfis:
                perfil = perfil.split(';')
                if perfil[0] == user and perfil[1] == password:
                    local = True
                    print('perfil encontrado')
                    temperfil = True
                    usuario = lc.Publico(perfil=perfil)
                    return(["local", usuario])
                    break
                else:
                    continue
            if not temperfil:
                print('''\33[31mPerfil não encontrado!\33[m''')
                reposta2 = menu.menu(['tentar novamente', 'cadastrar', 'prosseguir sem cadastro'])
                local = True
                return([reposta2])
            else:
                print('usuário encontrado')

