import lcmolde as lc
import menu
from validate_email import validate_email
from getpass import getpass
# import win32com.client as w3

def enviaremail(destinatario,usuario,senha):
    """(N\A) envia um email ao usuario para recuperação de senha
        Parameters:
            destinatario (str): o email para qual vai ser enviada a mensagem
            usuario (str): o nome de usuario da pessoa que quer recuperar a senha
            senha (str): a senha do usuario que vai sern enviada a ele"""
    try:
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
    except:
        print('\33[31mErro ao enviar email, tente novamente mais tarde\33[m')


def validaruser(usuario, arqlocal, arqbanda, arqpublico):
    """verifica se o usuario ja existe nos arquivos que se recebe como parametro
        Parameters:
            usuario (str): nome a ser verificado nos arquivos
            arqlocal (str): o nome do local do arquivo de local
            arqbanda (str): o nome do local do arquivo de banda
            arqpublico (str): o nome do local do arquivo de publico
            
        Returns:
            validacao (bool): Verdadeiro para se o nome não existe em nenhum arquivo
                            e falso para se existe"""
    #iniciando variaveis
    listaarq = [arqbanda, arqlocal, arqpublico] 
    validacao = True 
    memoria = [] 

    #preenchimento da variavel memoria
    try:
        for arquivo in listaarq:
            with open(arquivo, 'r', encoding='utf-8') as arquivo:
                arqsep = arquivo.readlines() 
            cont = 0
            for a in arqsep:
                if cont >0: 
                    memoria.append(a.split(';')[0]) 
                    cont+=1
    except(FileNotFoundError):
        print("\33[31mArquivo não encontrado, reinicie o programa\33[m")
    
    #verificação do nome de usuario
    for a in memoria:
        if a == usuario: 
            validacao = False
        else:
            continue
    return(validacao)


def validar_email(email):
    """verifica se o que foi digitado foi um email, tambem se ele teve atividade recente
        Parameters:
            email (str): o email inserido pelo usuario na hora do cadastro
            
        Returns:
            valido (bool): devolve verdadeiro ou falso para se o email é verdadeiro ou falso"""
    valido= validate_email(f'{email}', verify=True) 
    return(valido)


def conferirarquivo(nome):
    """Verifica se o arquivo escolhido existe ou não
        Parameters:
            nome (str): recebe o nome do arquivo que vai ser verificado
        
        Returns:
            existencia (bool): devolve Verdadeiro para se o arquivo existe e Falso para se não existe"""
    #iniciação das variaveis
    existencia = True
    #verificação do arquivo
    try: 
        a = open(nome, 'r')
        a.close()
    except: 
        existencia = False
    
    return(existencia)


def criararquivo(nome, cabeçalho):
    """Verifica se um arquiv ja existe, se não existir ele cria e ja escreve um cabeçalho no arquivo
        Parameters:
            nome (str): nome do arquivo que vai ser verificado ou criado
            cabeçalho (str): o cabeçalho que vai ser escrito no arquivo
            
        Returns:
            nome (str): nome atribuido ao arquivo criado"""
    existencia = conferirarquivo(nome) 
    
    if not existencia: 
        with open(nome, 'w', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{cabeçalho}\n') 
    else:
        pass

    return(nome)


def cadastro_artista(usuario, senha, arqbanda):
    """essa função recebe informações de cadastro do usuario e salva elas no arquivo csv como uma nova linha
        Parameters:
            usuario (str): recebe como string o usuario para salvar no arquivo
            senha (str): recebe como string a senha para salvar no arquivo
            arqbanda (str): recebe como string o nome do arquivo que vai receber o novo cadastro
            
        Returns:
            cadastrado (list): volta uma lista que no index 0 tem o tipo de cadastro realizado e no 1 tem o usuario como objeto"""
    while True:
        grupo = input('voce é artista [solo] ou tem [banda]? ')
        if grupo != 'banda' and grupo != 'solo':
            print('escolha uma opção válida')
        else:
            break
    if grupo == 'banda':
        nomebanda = input('Qual o nome da sua banda: ')
        tipo = 'banda'
    elif grupo == 'solo':
        nomebanda = input('Qual o seu nome artístico: ')
        tipo = 'solo'

    if tipo == 'solo':
        estilo = input('Qual seu estilo musical: ')
        bairro = input('Qual o seu bairro: ')
        integrantes = 'NaN'
    else:
        estilo = input('Qual o estilo musical da banda: ')
        bairro = input('Digite o bairro da sua banda: ')
        qtdinte = int(input('Quantos integrantes tem a sua banda: '))
        integrantes = []
        for integrante in range(qtdinte):
            integrante_nome = input(f'Digite o nome do integrante {integrante+1}: ')
            if '/' in integrante_nome:
                print("Por favor, não use o caracter (/) no preenchimento")
            else:
                integrantes.append(integrante_nome)
        integrantes = '/'.join(integrantes)
        
    ctt = []
    while True:
        contato = input('insira um contato email ou celular ou 0 para parar: ')
        if contato == '0':
            break
        else:
            if '/' in contato:
                print('por favor não use caracter (/) no preenchimento')
            ctt.append(contato)
    ctt = '/'.join(ctt)
    try:
        with open(arqbanda,'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{usuario};{senha};{tipo};{nomebanda};{integrantes};{bairro};{estilo};{ctt}\n')
    except(FileNotFoundError):
        print('\33[31mArquivo não encontrado, reinicie o programa\33[31m')
    except:
        print('\33[31mErro ao cadastrar, tente novamente\33[m')
    else:
        print('\33[33mCadastro realizado com sucesso!\33[m')
        user = lc.Banda(perfil=[usuario,senha,tipo,nomebanda,integrantes,bairro,estilo,ctt])
        cadastrado = ['banda',user]
        return(cadastrado) 


def cadastro_local(usuario, senha, arqlocal):
    """essa função recebe informações de cadastro do usuario e salva elas no arquivo csv como uma nova linha
        Parameters:
            usuario (str): recebe como string o usuario para salvar no arquivo
            senha (str): recebe como string a senha para salvar no arquivo
            arqlocal (str): recebe como string o nome do arquivo que vai receber o novo cadastro
            
        Returns:
            cadastrado (list): volta uma lista que no index 0 tem o tipo de cadastro realizado e no 1 tem o usuario como objeto"""
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
            if '/' in contato:
                print('por favor não use caracter (/) no preenchimento')
            else:
                ctt.append(contato)
    ctt = '/'.join(ctt)
    try:
        with open(arqlocal,'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{usuario};{senha};{tipo};{nomelocal};{endereço};{estilo};{ctt}\n')
    except(FileNotFoundError):
        print('\33[31mArquivo não encontrado, reinicie o programa\33[31m')
    #except:
     #   print('\33[31mErro ao cadastrar, tente novamente\33[m')
    else:
        print('\33[33mCadastro realizado com sucesso!\33[m')
        user = lc.Local([usuario,senha,tipo,nomelocal,endereço,estilo,ctt])
        return('local', user)


def cadastro_publico(usuario, senha, arqpublico):
    """essa função recebe informações de cadastro do usuario e salva elas no arquivo csv como uma nova linha
        Parameters:
            usuario (str): recebe como string o usuario para salvar no arquivo
            senha (str): recebe como string a senha para salvar no arquivo
            arqpublico (str): recebe como string o nome do arquivo que vai receber o novo cadastro
            
        Returns:
            cadastrado (list): volta uma lista que no index 0 tem o tipo de cadastro realizado e no 1 tem o usuario como objeto"""
    try:
        with open(arqpublico,'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{usuario};{senha}\n')
    except(FileNotFoundError):
        print('\33[31mArquivo não encontrado, reinicie o programa\33[31m')
    except:
        print('\33[31mErro ao cadastrar, tente novamente\33[m')
    else:
        print('\33[33mCadastro realizado com sucesso!\33[m')
        user = lc.Local([usuario,senha,tipo,nomelocal,endereço,estilo,ctt])
        return('publico', user)


def verificar_perfil(arq, user, password):
    """essa função procura no arquivo se já existe um cadastro com o mesmo nome e senha do usuario
        Parameters:
            arq (str): recebe o nome do arquivo que vai ser procurado como string
            user (str): recebe o nome de usuario a ser verificado como string
            password (str): recebe a senha do usuario a ser verificado como string"""
    try:
        with open(arq, 'r', newline='', encoding='utf-8') as arquivo:
            perfis = arquivo.readlines()
            for perfil in perfis:
                perfil = perfil.split(';')
                if perfil[0] == user and perfil[1] == password:
                    local = True
                    print('perfil encontrado')
                    temperfil = True
                    break
                else:
                    temperfil = False
            return([temperfil, perfil])
    except(FileNotFoundError):
        print("\33[31mArquivo não encontrado, reinicie o programa\33[m")


def cadastro(arqbanda, arqlocal, arqpublico):
    """função para criar um cadastro no arquivo csv, vai receber os dados do cadastro do usuario e dependendo
    da escolha dele em relação ao tipo de cadastro escolhido
        Parameters:
            arqbanda (str): o nome do arquivo dos usuarios do tipo banda
            arqlocal (str): o nome do arquivo dos usuarios do tipo local
            arqpublico (str): o nome do arquivo dos usuarios do tipo publico
            
        Returns:
            castrado (list): retorna em uam tupla o tipo do cadastro no index 0 e o objeto de usuario seguindo o molde do
            arquivo lcmolde no index 1
            sc (list): retorna uma lista que no index 0 indica que o usuario vai prosseguir  sem cadastro"""
    print('dados do cadastro')
    try:
        while True:
            while True:
                usuario = input('insira seu nome de usuário: ')
                if usuario.isalpha(): 
                    break
                else:
                    print('\33[31mEsperado pelo menos 1 letra no usuario\33[m')
            if validaruser(usuario=usuario, arqlocal=arqlocal, arqbanda=arqbanda, arqpublico=arqpublico): #validação se ja existe alguem com o mesmo nome
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
            cadastrado = cadastro_artista(usuario, senha, arqbanda)
            return(cadastrado)


        elif escolha == 'local':
            cadastrado = cadastro_local(usuario, senha, arqlocal)
            return(cadastrado)


        elif escolha == 'publico':
            cadastrado = cadastro_publico(usuario, senha, arqpublico)
            return(cadastrado)
    except(KeyboardInterrupt):
        print('\33[31mCadastro cancelado\33[m')
        sc = ['sem cadastro']
        return(sc)
    except:
        print(f'\33[31mErro ao cadastrar\33[m')
        sc = ['sem cadastro']
        return(sc)


def login(arqbanda, arqlocal, arqpublico):
    """essa função pede ao usuario o nome de usuario e senha e verifica se esses dados batem com o de algum arquivo
    caso não bata ele da outro menu em que o usuario pode tentar novamente, cadastrar ou seguir sem login
        Parameters:
            arqbanda (str): nome do arquivo de perfil de banda em string
            arqlocal (str): nome do arquivo de perfil de locais em string
            arqpublico (str): nome do arquivo de perfil de publico em string
            
        Returns: 
        cadastrado (list): devolve uma lista que no index 0 diz o tipo de cadastro
        sc (list): devolve uma lista que no index 0 indica que o usuario vai prosseguir sem cadastro"""
    try:
        while True:
            banda = False
            local = False
            user = input('insira seu usuário: ')
            password = getpass(prompt='insira sua senha: ')
            temperfil = verificar_perfil(arq=arqbanda, user=user, password=password)
            if temperfil[0]:
                print("/33[32mUsuario encontrado como Artista/Banda\33[m")
                usuario = lc.Banda(perfil=temperfil[1])
                banda = True
                cadastrado = ["banda", usuario]
                return(cadastrado)
                break

            if not banda:
                temperfil = verificar_perfil(arq=arqlocal, user=user, password=password)
                if temperfil[0]:
                    print("/33[32mUsuario encontrado como Dono de estabelecimento\33[m")
                    usuario = lc.Local(perfil=temperfil[1])
                    local = True
                    cadastrado = ["local", usuario]
                    return(cadastrado)
                    break

            if not banda and not local:
                temperfil = verificar_perfil(arq=arqpublico, user=user, password=password)
                if temperfil[0]:
                    print("/33[32mUsuario encontrado como Público\33[m")
                    usuario = lc.Publico(perfil=perfil)
                    cadastrado = ["Publico", usuario]
                    return(cadastrado)
                    break

            if temperfil[0] == False:
                print('''\33[31mPerfil não encontrado!\33[m''')
                resposta2 = menu.menu(['tentar novamente', 'cadastrar', 'prosseguir sem cadastro'])
                if resposta2 == 1:
                    continue
                elif resposta2 == 2:
                    cadastrado = cadastro(arqbanda, arqlocal, arqpublico)
                    return(cadastrado)
                elif resposta2 == 3:
                    sc = ['sem cadastro']
                    return(sc)
                    break   
                else:
                    print('usuário encontrado')
                    break
    except(KeyboardInterrupt):
        print("\33[31mLogin cancelado\33[m")
        sc = ["sem cadastro"]
        return(["sem cadastro"])
    except:
        print("\33[31mErro ao fazer login\33[m")
        sc = ["sem cadastro"]
        return(["sem cadastro"])
