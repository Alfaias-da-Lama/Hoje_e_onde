import lcmolde as lc
def validaruser(usuario, arqlocal, arqbanda):
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
    validação = True
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

def cadastro(arqbanda, arqlocal):
    from validate_email import validate_email
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
            tipo = input('qual o tipo de cadastro? [local] [artista]: ')
            if tipo != 'local' or tipo != 'artista':
                print('\33[31mSelecione uma opção acima\33[m')
            else:
                break
        if tipo == 'artista':
            grupo = input('voce é artista [solo] ou tem [banda]?')
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
        elif tipo == 'local':
            nomelocal = input('insira o nome do seu local: ')
            endereço = input('insira o endereço do local: ')
            estilo = input('insira o estilo musical de preferencia do local: ')
            ctt = []
            while True:
                contato = input('insira um contato email ou celular, ou 0 para encerrar')
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
    except:
        print('\33[merro ao cadastrar\33[m')

def login(arqbanda, arqlocal):
    import lcmolde as lc
    from getpass import getpass
    import menu
    banda = False
    temperfil = False
    usuario = input('insira seu usuário: ')
    senha = getpass(prompt='insira sua senha: ')
    with open(arqbanda, 'r', newline='', encoding='utf-8') as arquivo:
        perfis = arquivo.readlines()
        for perfil in perfis:
            perfil = perfil.split(';')
            if perfil[0] == usuario and perfil[1] == senha:
                banda = True
                print('perfil encontrado')
                temperfil = True
                usuario = lc.Banda(nomedabanda=perfil[3], integrantes=perfil[4], bairro=perfil[5], tipomusical=perfil[6], ctt=perfil[7])
                return(usuario)
                break
            else:
                continue
    if not banda:
        with open(arqlocal, 'r', newline='', encoding='utf-8') as arquivo:
            perfis = arquivo.readlines()
            print('tentando local')
            for perfil in perfis:
                perfil = perfil.split(';')
                print(perfil)
                if perfil[0] == usuario and perfil[1] == senha:
                    local = True
                    print('perfil encontrado')
                    temperfil = True
                    usuario = lc.Local(nome=perfil[3], endereco=perfil[4], tipomusical=perfil[5], ctt=perfil[6])
                    return(usuario)
                    break
                else:
                    continue
            if not temperfil:
                print('''\33[31mPerfil não encontrado!\33[m''')
                reposta2 = menu.menu(['cadastrar', 'prosseguir sem cadastro'])
                return(reposta2)
            else:
                print('usuário encontrado')

