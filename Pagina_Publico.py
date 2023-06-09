import banda as bd
import menu
import lcmolde as lc

def alterarpublico(arq, usuario):
    prosseguir = True
    linha = bd.pegarperfil(arq, usuario)
    memoria_csv = getlist(arq)
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
        elif escolha == 8:
            break
        elif escolha == 9:
            prosseguir = False
            break
        memoria_csv[linha] = [usuario, senha]
    print(memoria_csv[linha])
    escolha = input('Digite [ok] para confirmar ou [cancelar] para não registrar as mudanças: ')
    if prosseguir and escolha != 'cancelar':
        try:
            with open(arq, 'w', encoding='utf-8') as arquivo:
                arquivo.write('usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato\n')
            with open(arq, 'a', encoding='utf-8') as arquivo:
                for linha in range(1, len(memoria_csv)):
                    arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5]};{memoria_csv[linha][6]};{memoria_csv[linha][7].strip()}\n')
            print('\33[31mCadastro atualizado!\33[m')
        except:
            print("\33[31mErro ao atualizar cadastro, tente novamente\33[m")
    else:
        print( '\33[31mCancelando operação... \33[m')


def seguirshow(arqusuario, usuario):  
    memoria_show = bd.getlistagenda()
    bd.mostrartabela(excluir=[], content=memoria_show)
    while True:
        try:
            escolha = int(input('qual show voce deseja seguir [index]: '))
        except(ValueError):
            print("\33[31mInsira um numero válido\33[m")
    show = lc.show(memoria_show[escolha])
    usuario.show.append(show)


def mostrarshows(usuario):
    try:
        if usuario.show != []:
            print('shows seguidos:')
            for show in usuario.show:
                print(f'{show.banda<12} {show.local<12} {show.horastart<12} {show.horaend<12}, faltam {show.temporest} dias para o show começar')
        else:
            print(usuario.mensagem)
    except:
        print("\33[31mErro ao mostrar shows seguidos\33[m")


def dar_feedback(usuario):
    cont = 0
    valshow = bd.getlistagenda()
    for show in usuario.show:
        if [show.banda, show.local, show.horastart, show.horaend] in valshow:
            cont+=1
            print(f'{cont} = {show.banda} - {show.local} - {show.data}')
    try:
        escolha = int(input("qual show voce deseja dar feedback: "))
        usuario.show[escolha].feedback(usuario)
        usuario.show[escolha].salvar_dados()
    except:
        print("\33[31mErro ao dar feedback\33[m")


def pagina_publico(usuario):
    while True:
        mostrarshows(usuario)
        escolha = menu.menu2(titulo="Página Público", componentes=["Ver Bandas", "Ver Locais", "Ver Agenda", "Editar Perfil", "Seguir show", "Dar Feedback de shows assistidos", "Sair"])
        if escolha == 1:
            bd.mostrarbanda()
        elif escolha == 2:
            bd.mostrarlocal()
        elif escolha == 3:
            bd.mostraragenda()
        elif escolha == 4:
            alterarpublico(arq='perfilXpublico.csv', usuario=usuario.usuario)
        elif escolha == 5:
            seguirshow(arqusuario='perfilXpublico.csv', usuario=usuario)
        elif escolha == 6:
            dar_feedback(usuario)
        elif escolha == 7:
            break
