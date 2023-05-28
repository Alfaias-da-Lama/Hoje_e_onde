import os
import logincadas as lc
import menu
import sem_login
arqbanda=lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
arqlocal=lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
os.system('cls')
while True:
    resposta = menu.menu2('Tela de cadastro', ['Login', 'Cadastro', 'Prosseguir sem logar'])
    resposta2 = 0
    if resposta > 3:
        os.system('cls')
        print('\33[31mInsira uma resposta válida!\33[m')
    else:
        break
if resposta == 1:
    while True:
        resposta2 = lc.login(arqbanda, arqlocal)
        if resposta2 == 1:
            continue
        elif resposta2 == 2:
            break
            lc.cadastro(arqbanda, arqlocal)
        elif resposta2 == 3:
            pass
        else:
            break
elif resposta == 2 or resposta2 == 1:
    lc.cadastro(arqbanda, arqlocal)
elif resposta == 3 or resposta2 == 2:
   sem_login.opcoes_sem_login(resposta)
