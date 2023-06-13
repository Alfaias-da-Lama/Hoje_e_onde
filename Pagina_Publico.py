import banda as bd
import menu
import lcmolde as lc
import display as dp
import logincadas as lic

def alterarpublico(arq, usuario):
    """essa função serve para alterar uma linha específica do arquivo perfilXpublico.
        Parameters:
            arq (str): nome do arquivo que vai ser alterado
            usuario (obj): usuario como objeto que vai ser usado na função de pegar perfil"""
    prosseguir = True
    linha = dp.pegarperfil(arq, usuario)
    memoria_csv = dp.getlist(arq)
    usuario = memoria_csv[linha][0]
    senha = memoria_csv[linha][1]
    while True:
        for a in range(len(memoria_csv[linha])):
            print(memoria_csv[linha][a], end=' ')
        print('\no que voce deseja alterar?')
        escolha = menu.menu(['usuario', 'senha','salvar alterações', 'cancelar'])
        if escolha == 1:
                while True:
                    while True:
                        usuario = input('insira seu nome de usuário: ')
                        if usuario.isalpha():
                            break
                    else:
                        print('\33[31mEsperado pelo menos 1 letra no usuario\33[m')
                    if lic.validaruser(usuario=usuario, arqlocal='perfilXlocais.csv', arqbanda='perfilXbandas.csv', arqpublico='perfilXpublico.csv'):
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
            break
        elif escolha == 4:
            prosseguir = False
            break
        memoria_csv[linha] = [usuario, senha]
    print(memoria_csv[linha])
    escolha = input('Digite [ok] para confirmar ou [cancelar] para não registrar as mudanças: ')
    if prosseguir and (escolha != 'cancelar'):
        try:
            with open(arq, 'w', encoding='utf-8') as arquivo:
                arquivo.write('usuario;senha;idx_show\n')
            with open(arq, 'a', encoding='utf-8') as arquivo:
                for linha in range(1, len(memoria_csv)):
                    if len(linha) == 3:
                        arquivo.write(f'\n{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2].strip()}\n')
                    else:
                        arquivo.write(f'\n{memoria_csv[linha][0]};{memoria_csv[linha][1].strip()}\n')
            print('\33[32mCadastro atualizado!, faça login novamente\33[m')
        except:
            print("\33[31mErro ao atualizar cadastro, tente novamente\33[m")
    else:
        print('\33[31mCancelando operação... \33[m')


def seguirshow(usuario):
    """essa função faz o usuario seguir um evento especifico da agenda.csv para acompanhar quantos
    dias faltam para a data do evento e posteriormente ser capaz de dar feedbacks
        Parameters:
            usuario (obj): recebe o usuario como objeto para associar o show seguido a ele"""
    try:
        memoria_show = dp.getlistagenda()
        dp.mostrartabela(excluir=[], content=memoria_show, idx=False)
        while True:
            try:
                escolha = input('qual show voce deseja seguir [ordem]: ')
            except(ValueError):
                print("\33[31mInsira um numero válido\33[m")
            else:
                break
        for shows in memoria_show:
            print(shows)
            if shows[0] == escolha:
                show = lc.show(shows)
                usuario.show.append(show)
    except(KeyboardInterrupt):
        print("\33[31mVoltando ao menu\33[m")


def mostrarshows(usuario):
    """essa função mostra os shows seguidos ao usuario, mostrando as informações do show e quantos dias faltam para a data
        Parameters:
            usuario (obj): recebe o usuario como objeto para verificar os shows associados"""
    #try:
    if True:
        if usuario.show != []:
            print('shows seguidos:')
            for show in usuario.show:
                dias = show.temporest()
                print(f'{show.banda.ljust(12)} {show.local.ljust(12)} {show.horastart.ljust(12)} {show.horaend.ljust(12)}, faltam {dias} dias para o show começar')
        else:
            print(usuario.mensagem)
    #except:
        #print("\33[31mErro ao mostrar shows seguidos\33[m")


def dar_feedback(usuario):
    """essa função cria uma mensagem de feedback para um show seguido pelo usuario e associa ao show
        Parameters:
            usuario (obj): recebe o usuario para verificação de show e para associar o nome ao feedback"""
    cont = 0
    valshow = dp.getlistagenda()
    for idx, show in enumerate(usuario.show):
        if [show.banda, show.local, show.data] == [valshow[idx][0], valshow[idx][1]]:
            cont+=1
            print(f'{cont} = {show.banda} - {show.local} - {show.data}')
    try:
        escolha = int(input("qual show voce deseja dar feedback: "))
        usuario.show[escolha].feedback(usuario)
        usuario.show[escolha].salvar_dados()
    except:
        print("\33[31mErro ao dar feedback\33[m")


def pagina_publico(usuario):
    """função com o menu da pagina de usuarios cadastrados como público, com suas devidas funções
        Parameters:
            usuario (obj): recebe o usuario como objeto para ser usado nas funções associadas"""
    usuario.resgatar_shows()
    while True:
        mostrarshows(usuario)
        escolha = menu.menu2(titulo="Página Público", componentes=["Ver Bandas", "Ver Locais", "Ver Agenda", "Editar Perfil", "Seguir show", "Dar Feedback de shows assistidos", "Sair"])
        if escolha == 1:
            dp.mostrarbanda()
        elif escolha == 2:
            dp.mostrarlocal()
        elif escolha == 3:
            dp.mostraragenda()
        elif escolha == 4:
            alterarpublico(arq='perfilXpublico.csv', usuario=usuario)
        elif escolha == 5:
            seguirshow(usuario=usuario)
        elif escolha == 6:
            dar_feedback(usuario)
        elif escolha == 7:
            break
