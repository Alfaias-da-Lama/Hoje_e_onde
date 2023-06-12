def menu(componentes):
    """essa função cria um estilo de menu sem titulo, pede a opção ao usuario
        Parameters:
            componentes (list): recebe os componentes do menu em formato de lista para mostrar ao usuario
            acompanhado de um numero no prompt
            
        Returns:
            resposta (int): devolve a opção escolhida pelo usuario"""
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
    """essa função formata uma string em formato de título
        Parameters:
            mensagem (str): string que vai ser formatada em título"""
    mensagem = mensagem.title()
    parametro = len(mensagem) // 2
    print('=-'*(15-parametro), mensagem, '=-'*(15-parametro))

def menu2(titulo ,componentes):
    """Cria um menu com título e os compontentes como escolha, pede a escolha ao usuario
        Parameters:
            titulo (str): título do menu
            componentes (list): compontentes a serem mostrados como opções no formato de lista
        
        Returns:
            resposta (int): devolve a resposta do usuario em relação a escolha do menu"""
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