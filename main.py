import os
import logincadas as lc
import menu
os.system('cls')
arqbanda=lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
arqlocal=lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
menu.titulo('tela de cadastro')
resposta = menu.menu(['Login', 'Cadastro', 'Prosseguir sem logar'])
if resposta == 1:
    resposta2 = lc.login(arqbanda, arqlocal)
elif resposta == 2 or resposta2 == 1:
    lc.cadastro(arqbanda, arqlocal)
elif resposta == 3 or resposta2 == 2:
    pass
else:
    print('\33[31mInsira uma resposta válida!\33[m')