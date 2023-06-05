import os
import logincadas as lc
import menu
import sem_login
import banda as bd
import local as lo
import time
import publico as pb


arqbanda=lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
arqlocal=lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
arqpublico = lc.criararquivo(nome='perfilXpublico.csv', cabeçalho='usuario;senha')
arqagenda=lc.criararquivo(nome='agenda.csv', cabeçalho='banda;local;data;horastart;horaend')
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
        if resposta2[0] == 1:
            continue
        elif resposta2[0] == 2:
            break
        elif resposta2[0] == 3:
            break
        else:
            break
elif resposta == 2 or resposta2[0] == 1:
    resposta2=lc.cadastro(arqbanda, arqlocal)
elif resposta == 3 or resposta2[0] == 2:
   sem_login.opcoes_sem_login(resposta)
if resposta2[0] == 'banda':
    bd.pagina_de_banda(usuario=resposta2[1])
elif resposta2[0] == 'local':
    lo.menu_principal()
elif resposta2[0] == 'publico':
    pb.pagina_publico(usuario= resposta2[1])
