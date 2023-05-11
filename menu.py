def menu(componentes):
    cont = 1
    for c in componentes:
        print(f'\33[m[{cont}]\33[m \33[m-> \33[m{c}\33[m')
        cont += 1
    resposta = int(input('''o que deseja fazer? 
    -> '''))
    return(resposta)

def titulo(mensagem):
    mensagem.title()
    parametro = len(mensagem) // 2
    print('=-'*(15-parametro), mensagem, '=-'*(15-parametro))