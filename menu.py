def menu(componentes):
    cont = 1
    for c in componentes:
        print(f'\33[m[{cont}]\33[m \33[m-> \33[m{c}\33[m')
        cont += 1
    while True:
        try:
            resposta = int(input('''o que deseja fazer? 
    -> '''))
        except(ValueError):
            print("\33[31mInsira um número válido\33[m")
        else:
            break
    return(resposta)

def titulo(mensagem):
    mensagem = mensagem.title()
    parametro = len(mensagem) // 2
    print('=-'*(15-parametro), mensagem, '=-'*(15-parametro))

def menu2(titulo ,componentes):
    print('-'*42)
    print(f'{titulo.center(42)}')
    print('-'*42)
    cont=1
    for a in componentes:
        print(f'\33[34m{cont} - \33[33m{a}\33[m')
        cont+=1
    print('-'*42)
    while True:
        try:
            resposta = int(input('insira sua opção: '))
        except(ValueError):
            print("\33[31mInsira um número válido\33[m")
        else:
            break
    return(resposta)