import os
import logincadas as lc
import menu
import sem_login
import banda as bd
import local as lo
import time
import Pagina_Publico as pb


arqbanda=lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
arqlocal=lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
arqpublico = lc.criararquivo(nome='perfilXpublico.csv', cabeçalho='usuario;senha')
arqagenda=lc.criararquivo(nome='agenda.csv', cabeçalho='banda;local;data;horastart;horaend')
os.system('cls')
while True:
    resposta = menu.menu2('Tela de cadastro', ['Login', 'Cadastro', 'Prosseguir sem logar'])
    if resposta > 3:
        os.system('cls')
        print('\33[31mInsira uma resposta válida!\33[m')
    else:
        break
if resposta == 1:
    usuario = lc.login(arqbanda, arqlocal, arqpublico)
elif resposta == 2:
    usuario = lc.cadastro(arqbanda, arqlocal, arqpublico)
elif resposta == 3 or usuario[0] == 'sem cadastro':
   sem_login.opcoes_sem_login(resposta)


if usuario[0] == 'banda':
    bd.pagina_de_banda(usuario=usuario[1])
elif usuario[0] == 'local':
    lo.menu_principal(usuario=usuario[1])
elif usuario[0] == 'publico':
    pb.pagina_publico(usuario= usuario[1])
