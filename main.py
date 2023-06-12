import os
import logincadas as lc
import menu
import sem_login as sl
import banda as bd
import local as lo
import time
import Pagina_Publico as pb

try:
    arqbanda = lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
    arqlocal = lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
    arqpublico = lc.criararquivo(nome='perfilXpublico.csv', cabeçalho='usuario;senha;idx_show')
    arqagenda = lc.criararquivo(nome='agenda.csv', cabeçalho='ordem;banda;local;data;horastart;horaend')
    os.system('cls')
    while True:
        while True:
            resposta = menu.menu2("Tela de cadastro", ["Login", "Cadastro", "Prosseguir sem logar", "Sair"])
            if resposta > 4:
                os.system('cls')
                print('\33[31mInsira uma resposta válida!\33[m')
            else:
                break
        if resposta == 1:
            usuario = lc.login(arqbanda, arqlocal, arqpublico)
        elif resposta == 2:
            usuario = lc.cadastro(arqbanda, arqlocal, arqpublico)
        try:
            if resposta == 3 or usuario[0] == 'sem cadastro':
                sl.pagina_semlog()
        except(NameError):
            pass
        if resposta == 4:
            print("Até a próxima")
            break
        try:
            if usuario[0] == 'banda':
                bd.pagina_de_banda(usuario=usuario[1])
            elif usuario[0] == 'local':
                lo.pagina_de_local(usuario=usuario[1])
            elif usuario[0] == 'publico':
                pb.pagina_publico(usuario= usuario[1])
        except(NameError):
            pass
except(KeyboardInterrupt):
    print("""Saindo do Hoje é onde...
Volte sempre""")
except Exception as e:
    print(f"Ocorreu um erro: {e}")