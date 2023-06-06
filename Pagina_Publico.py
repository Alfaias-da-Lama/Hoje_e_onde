import banda as bd
import menu


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
        with open(arq, 'w', encoding='utf-8') as arquivo:
            arquivo.write('usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato\n')
        with open(arq, 'a', encoding='utf-8') as arquivo:
            for linha in range(1, len(memoria_csv)):
                arquivo.write(f'{memoria_csv[linha][0]};{memoria_csv[linha][1]};{memoria_csv[linha][2]};{memoria_csv[linha][3]};{memoria_csv[linha][4]};{memoria_csv[linha][5]};{memoria_csv[linha][6]};{memoria_csv[linha][7].strp()}\n')
        print('\33[31mCadastro atualizado!\33[m')
    else:
        print( '\33[31mCancelando operação... \33[m')


def seguirshow(arqagenda):
    bd.mostraragenda()
    escolha = input('qual show voce deseja seguir: index')


def showsseguindo(usuario):
    for show in usuario.show:
        conteudo = show.split(';')
        data = conteudo[2].split('/')
        dia = data[0]
        mes = data[1]
        ano = data[2]
        datapadrao = datetime.date(ano, mes, dia)
        hoje = datetime.date.today()
        if datapadrao > hoje:
            delta = datapadrao - hoje
        elif datapadrao <= hoje:
            delta = hoje - datapadrao
        conteudo.append(delta.days)
        for palavra in conteudo:
            print(f'{palavra}'.ljust(12), end=' ')
        print()
    

def pagina_publico(usuario):
    while True:
        escolha = menu.menu2(titulo="Página Público", componentes=["Ver Bandas", "Ver Locais", "Ver Agenda", "Editar Perfil", "Sair"])
        if escolha == 1:
            bd.mostrarbanda()
        elif escolha == 2:
            bd.mostrarlocal()
        elif escolha == 3:
            bd.mostraragenda()
        elif escolha == 4:
            alterarpublico(arq='perfilXpublico.csv', usuario=usuario.usuario)
        elif escolha == 5:
            break