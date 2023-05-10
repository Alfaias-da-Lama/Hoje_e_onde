import lcmolde as lc
def conferirarquivo(nome):
    existencia = True
    try:
        a = open(nome, 'r')
        a.close()
    except:
        print('\33[31mArquivo não existente, criando arquivo...\33[m')
        existencia = False
    return(existencia)

def criararquivo(nome):
    existencia = conferirarquivo()
    if not existencia:
        with open(nome, 'w') as arquivo:
            arquivo.write('ordem,nome,categoria,valor,data,hora\n')
        print('\33[32mArquivo controle.csv criado, com sucesso\33[m')
    else:
        print('Encontrado arquivo controle.csv')
    return(nome)

def cadastro(arqbanda, arqlocal):
    print('dados do cadastro')
    usuario = input('insira seu nome de usuário: ')
    senha = input('escolha uma senha: ')
    tipo = input('qual o tipo de cadastro? [local] [banda]: ')
    if tipo == 'banda':
        nomebanda = input('qual o nome da sua banda: ')
        estilo = input('qual o estilo musical da banda: ')
        bairro = input('digite o bairro da sau banda: ')
        qtdinte = int(input('quantos integrantes tem a sua banda: '))
        integrantes = []
        for integrante in range(qtdinte):
            integrantes.append(input(f'digite o nome do integrante {integrante+1}: '))
        integrantes = ';'.join(integrantes)
        ctt = []
        while True:
            contato = input('insira um contato email ou celular ou 0 para parar: ')
            if contato == '0':
                break
            else:
                ctt.append(contato)
            ctt = ';'.join(ctt)
        with open(arq,'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{usuario},{senha},{tipo},{nomebanda},{integrantes},{bairro},{estilo},{ctt}')
    elif tipo == 'local':
        nomelocal = input('insira o nome do seu local: ')
        endereço = input('insira o endereço do local')
        estilo = input('insira o estilo musical de preferencia do local: ')
        ctt = []
        while True:
            contato = input('insira um contato email ou celular, ou 0 para encerrar')
            if contato == '0':
                break
            else:
                ctt.append(contato)
        ctt = ';'.join(ctt)
        with open(arq,'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{usuario},{senha},{tipo},{nomelocal},{endereço},{estilo},{ctt}')

def login(arqbanda, arqlocal):
    from getpass import getpass
    usuario = input('insira seu usuário: ')
    senha = getpass(prompt='insira sua senha: ')
    with open(arqbanda, 'r', newline='', encoding='utf-8') as arquivo:
        perfis = arquivo.readlines()
        for perfil in perfis:
            if perfil[0] == usuario and perfil[1] == 'senha':
                banda = True
                print('perfil encontrado')
                usuario = lc.Banda(nomedabanda=perfil[3], integrantes=perfil[4], bairro=perfil[5], tipomusical=perfil[6], ctt=perfil[7])
            else:
                continue
    if not banda:
        with open(arqlocal, 'r', newline='', encoding='utf-8') as arquivo:
            perfis = arquivo.readlines()
            for perfil in perfis:
                if perfil[0] == usuario and perfil[1] == 'senha':
                    local = True
                    print('perfil encontrado')
                    lc.Local(nome=perfil[3], endereco=perfil[4], tipomusical=perfil[5], ctt=perfil[6])
                else:
                    continue
    
