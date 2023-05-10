import os
import logincadas as lc
import menu
os.system('cls')
lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario,senha,tipo,nome, integrantes,endereço,tipomusical,contato')
lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario,senha,tipo,nome,endereço,tipomusical,contato')
menu.titulo('tela de cadastro')
resposta = menu.menu(['Login', 'Cadastro', 'Prosseguir sem logar'])