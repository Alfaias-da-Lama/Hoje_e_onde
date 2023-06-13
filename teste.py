import os
import logincadas as lc
import menu
import sem_login as sl
import banda as bd
import local as lo
import time
import Pagina_Publico as pb
import lcmolde as lcm

arqbanda = lc.criararquivo(nome='perfilXbandas.csv', cabeçalho='usuario;senha;tipo;nome;integrantes;endereço;tipomusical;contato')
arqlocal = lc.criararquivo(nome='perfilXlocais.csv', cabeçalho='usuario;senha;tipo;nome;endereço;tipomusical;contato')
arqpublico = lc.criararquivo(nome='perfilXpublico.csv', cabeçalho='usuario;senha;idx_show')
arqagenda = lc.criararquivo(nome='agenda.csv', cabeçalho='ordem;banda;local;data;horastart;horaend')

usuario = lcm.Publico(perfil=['evaldo', '12345678'])

pb.pagina_publico(usuario=usuario)