import display as dp
import menu 

def ler_ultimo_index(arq):
    '''Recebe como parametro o nome do arquivo csv de banco de dados em que ela vai procurar na posição do numero da
    show(index 0) o numero do ultimo show e o retornar, caso não haja shows ele retorna 0.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.

        Returns:
           (int):retorna o numero do ultimo numero de transação, se não houver retorna 0.
    '''
    try:
        memoria_csv = []
        memoria_csv = dp.getlist(arq)
        if len(memoria_csv) > 1:
            ultima_linha = memoria_csv[len(memoria_csv)-1]
            return (int(ultima_linha[0]))
        else:
            return(0)
    except(FileNotFoundError):
        print("\33[31mErro ao encontrar arquivo, reinicie o programa\33[m")


def criar_evento(local):
    """cria uma nova linha no arquivo agenda.csv com informações recebidas do usuario sobre um show
        Parameters:
            local (str):  nome do local do usuario que está criando o show"""
    try:
        while True:
            banda = input("digite qual banda vai tocar no show: ")
            while True:
                try:
                    dia = int(input("digite qual o dia do show: "))
                except(ValueError):
                    print("\33[31mInsira um valor em numero!\33[m")
                else:
                    break
            while True:
                try:
                    mes = int(input("digite qual o mes do show: "))
                except(ValueError):
                    print("\33[31mInsira um valor em numero!\33[m")
                else:
                    break
            while True:
                try:
                    ano = int(input("digite qual o ano do show: "))
                except(ValueError):
                    print("\33[31mInsira um valor em numero!\33[m")
                else:
                    break
            data = f"{dia}/{mes}/{ano}"
            horastart = input("insira p horario que vai começar o show: ")
            horaend = input("insira o horario previsto para o termino do show: ")
            show = f"{ler_ultimo_index(arq='agenda.csv')};{banda};{local};{data};{horastart};{horaend}"
            print(f'''o show vai ficar: 
        {show}''')
            while True:
                confirmacao = input("digite [ok] para confirmar ou [cancela] para não registrar o show: ").lower()
                if confirmacao != 'ok' and confirmacao != 'cancela':
                    print("insira uma resposta válida")
                else:
                    break
            if confirmacao == 'ok':
                with open('agenda.csv', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(show)
                break
            elif confirmacao == 'cancela':
                print("\33[31mCancelando operação e voltando ao menu\33[m")
                while True:
                    escolha = menu.menu(['Voltar ao menu', 'Tentar novamente'])
                    if escolha > 2:
                        print("\33[31mInsira um valor válido\33[m")
                    else:
                        break
                if escolha == 1:
                    break
                if escolha == 2:
                    continue
    except(KeyboardInterrupt):
        print("\33[31mCancelando operação\33[m")


def reescritor_de_arquivo(memoria_csv):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e uma matriz com todos os dados de todas as 
    transações salvas, e com esses dados reescreve todo o banco de dados com as novas informações atualizadas.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.
        memoria_csv (list):uma matriz com todos os dados dos shows.
    '''    
    with open("agenda.csv", 'w', encoding='utf-8') as arquivo:
        arquivo.write('ordem;banda;local;horastart;horaend;feedback\n')
    with open(arq, 'a', encoding='utf-8') as arquivo:
        for linha in range(1, len(memoria_csv)):
            try:
                arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5].strip()}\n')
            except(IndexError):
                arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4].strip()}\n')
        print('\33[32mShow atualizado!\33[m')


def atualizar(local):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e mostra todo o arquivo em formato de tabela,
    esperando do usuário a escolha de qual linha será atualizada, atualizando todas as informações exceto:
    index,data e hora.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.

    Raises:
        AttributeError:
        ValueError:
    '''
    try:
        memoria_csv = dp.getlistagenda()
        dp.mostrartabelafiltro(content=memoria_csv, filtro=[2, local])
        while True:
            try:
                ordem = int(input("qual o show que voce quer alterar?: "))
            except(ValueError):
                print("\33[31mInsira um valor em numero!\33[m")
        novabanda = input("qual banda vai tocar no show: ")
        while True:
            try:
                dia = int(input("digite qual o dia do show: "))
            except(ValueError):
                print("\33[31mInsira um valor em numero!\33[m")
            else:
                break
        while True:
            try:
                mes = int(input("digite qual o mes do show: "))
            except(ValueError):
                print("\33[31mInsira um valor em numero!\33[m")
            else:
                break
        while True:
            try:
                ano = int(input("digite qual o ano do show: "))
            except(ValueError):
                print("\33[31mInsira um valor em numero!\33[m")
            else:
                break
        novadata = f"{dia}/{mes}/{ano}"
        horastart = input("insira p horario que vai começar o show: ")
        horaend = input("insira o horario previsto para o termino do show: ")

        memoria_csv[ordem][1] = novabanda
        memoria_csv[ordem][3] = novadata
        memoria_csv[ordem][4] = horastart
        memoria_csv[ordem][5] = horaend

        print(f'o show ficou: {memoria_csv[ordem][0]} - {memoria_csv[ordem][1]}, {memoria_csv[ordem][2]}, {memoria_csv[ordem][3]}, {memoria_csv[ordem][4]}, {memoria_csv[ordem][5]}')
        while True:
            continuar = input("digite [ok] para continuar e [cancela] para cancelar: ")
            if continuar != 'ok' and continuar != 'cancela':
                print("\33[31mInsira uma opção válida\33[m")
            else:
                break
        
        if continuar == 'ok':
            reescritor_de_arquivo(memoria_csv)
        else:
            print('\33[31mCancelando operação... \33[m')
    except(KeyboardInterrupt):
        print("\33[31mCancelando operação\33[m")


def alterar_local(arq, usuario):
    """essa função serve para alterar uma linha específica do arquivo perfilXlocais.
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
        endereco = memoria_csv[linha][4]
        tipomusical = memoria_csv[linha][5]
        ctt = memoria_csv[linha][6]
        while True:
            for a in range(len(memoria_csv[linha])):
                print(memoria_csv[linha][a], end=' ')
            print('\no que voce deseja alterar?')
            escolha = menu.menu(['usuario', 'senha', 'nome do local', 'endereço', 'estilo de preferencia', 'contato', 'salvar alterações'])
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
                nomelocal = input('insira o novo nome do local: ')
            elif escolha == 4:
                bairro = input('insira o endereço do local: ')
            elif escolha == 5:
                estilo = input('insira o estilo de preferencia do local: ')
            elif escolha == 6:
                tipo = input("qual o tipo de estabelecimento: ")
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
            memoria_csv[linha] = [usuario, senha, tipo, nome, bairro, estilo, ctt]
        print(memoria_csv[linha])
        escolha = input('Digite [ok] para confirmar ou [cancelar] para não registrar as mudanças: ')
        if prosseguir and escolha != 'cancelar':
            with open(arq, 'w', encoding='utf-8') as arquivo:
                arquivo.write('usuario;senha;tipo;nome;endereço;tipomusical;contato\n')
            with open(arq, 'a', encoding='utf-8') as arquivo:
                for linha in range(1, len(memoria_csv)):
                    arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5]};{memoria_csv[linha][6]};{memoria_csv[linha][7].strip()}\n')
            print('\33[31mCadastro atualizado!\33[m')
        else:
            print( '\33[31mCancelando operação... \33[m')
    except(KeyboardInterrupt):
        print("\33[31mCancelando operação\33[m")


def pagina_de_local(usuario):
    """essa função cria um menu com as funções disponiveis aos usuarios do tipo locais
        Parameters:
            usuario (obj): recebe o usuario como objeto para ser usado nas funções associadas"""
    try:
        while True:
            resposta = menu.menu2('Página de Local', ['Ver bandas','Ver outros locais', 'Ver agenda', "Criar evento","Editar Evento", 'Alterar perfil', "Ver feedbacks", 'Sair'])
            if resposta == 1:
                dp.mostrarbanda(contato=True)
            elif resposta == 2:
                dp.mostrarlocal()
            elif resposta == 3:
                dp.mostraragenda()
            elif resposta == 4:
                criar_evento(usuario.nome)
            elif resposta == 5:
                atualizar(usuario.nome)
            elif resposta == 6:
                alterar_banda("perfilXlocais", usuario.usuario)
            elif resposta == 7:
                mostrar_feedback(usuario.nome)
            elif resposta == 8:
                break
    except(KeyboardInterrupt):
        print("\33[31mVoltando ao menu principal...\33[m")