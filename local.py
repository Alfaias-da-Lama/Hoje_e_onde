import os 
import time

def clear():
    return os.system("cls")


def loading():
    clear()
    print("Carregando...")
    time.sleep(1.5)


global nome #nome do local (alterar depois)   

def menu_perfil(): #página inicial do local (alterar depois)
    try:
        clear()
        print('BEM VINDO')
        print('[1]: Criar Perfil')
        print('[2]: Ver Perfil')
        print('[3]: Editar Perfil')
        print('[4]: Menu Principal')
        
        decisao = int(input('Digite o que deseja fazer: '))

        if decisao == 1:
            loading()
            return adicionar_informacoes()
        elif decisao == 2:
            loading()
            return ver_perfil()
        elif decisao == 3:
            loading()
            return editar_perfil()
        elif decisao == 4:
            loading()
            return menu_principal()
        else:
            print('Opção inválida!')
            time.sleep(1)
            return menu_perfil()
        
    except ValueError:
        print('Digite utilizando algarismos numéricos!')
        time.sleep(1.5)
        return menu_perfil()


def menu_principal(): #página principal do local (aterar depois)
    try:
        clear()
        print('[1]: Menu Perfil')
        print('[2]: Ver Locais')
        print('[3]: Ver Bandas')
        print('[4]: Menu Agenda')

        decisao = int(input('Digite o que deseja fazer: '))

        if decisao == 1:
            loading()
            return menu_perfil()
        elif decisao == 2:
            loading()
            return ver_locais()
        elif decisao == 3:
            loading()
            return ver_bandas()
        elif decisao == 4:
            loading()
            return menu_agenda()
        else:
            print('Opção inválida!')
            time.sleep(1.5)
            return menu_principal()
        
    except ValueError:
        print('Digite utilizando algarismos numéricos!')
        time.sleep(1.5)
        return menu_principal()


def menu_agenda(): #menu das funções da agenda (alterar depois)
    try:
        clear()
        print('[1]: Criar Agenda')
        print('[2]: Ver Agenda')
        print('[3]: Editar Agenda')
        print('[4]: Menu Principal')

        decisao = int(input('Digite o que deseja fazer: '))

        if decisao == 1:
            loading()
            return adicionar_agenda()
        elif decisao == 2:
            loading()
            return ver_agenda()
        elif decisao == 3:
            loading()
            return editar_agenda()
        elif decisao == 4:
            loading()
            return menu_principal()
        else:
            print('Opção inválida!')
            time.sleep(1.5)
            return menu_agenda()
        
    except ValueError:
        print('Digite utilizando algarismos numéricos!')
        time.sleep(1.5)
        return menu_agenda()


def ver_perfil():
    try:
        clear()
        with open('local.csv', 'r', encoding='utf8') as f:
            encontrado = False

            linhas = f.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')
                if nome == dados[0]:
                    encontrado = True
                    print(f'Nome: {dados[0]} // Tipo: {dados[1]} // Endereço: {dados[2]} // Tipo musical: {dados[3]} // Contato: {dados[4]}')
                    
            if not encontrado:
                print('Perfil não encontrado')
        f.close()
        input('Aperte enter para voltar: ')
        return menu_perfil()
            
        
    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_perfil() #voltar para o menu


def adicionar_informacoes(): #adicionar informações do próprio perfil
    try:
        clear()
        with open('local.csv', 'a', encoding='utf8') as f:
            tipo = input('Digite o tipo do local: ')
            endereco = input('Digite o endereço do local: ')
            tipo_musical = input('Digite o tipo musical de preferência do local: ')
            contato = input('Digite as informações de contato: ')

            f.write(f'{nome};{tipo};{endereco};{tipo_musical};{contato}\n')

        f.close()
        loading()
        return menu_perfil()
    except:
        print('ERRO DO SISTEMA')
        time.sleep(1.5)
        return menu_perfil() #voltar para o menu

def editar_perfil():
    try:
        clear()
        encontrado = False
        with open('local.csv', 'r', encoding='utf8') as f, open('local_temp.csv', 'w', encoding='utf8') as f_temp:
            linhas = f.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')
                if nome == dados[0]:
                    encontrado = True
                    
                    print(f'Nome: {dados[0]} // Tipo: {dados[1]} // Endereço: {dados[2]} // Tipo musical: {dados[3]} // Contato: {dados[4]}')
                    decisao = input('Qual informação deseja editar: ').lower()

                    if decisao == 'nome':
                        novo_nome = input('Digite o novo nome do local: ')
                        if novo_nome == '':
                            novo_nome = dados[0]
                        f_temp.write(f'{novo_nome};{dados[1]};{dados[2]};{dados[3]};{dados[4]}')
                    
                    elif decisao == 'tipo':
                        novo_tipo = input('Digite o novo tipo do local (ou deixe em branco para apagar): ')
                        f_temp.write(f'{dados[0]};{novo_tipo};{dados[2]};{dados[3]};{dados[4]}')
                    
                    elif decisao == 'endereço':
                        novo_endereco = input('Digite o novo endereço do local (ou deixe em branco para apagar): ')
                        f_temp.write(f'{dados[0]};{dados[1]};{novo_endereco};{dados[3]};{dados[4]}')
                    
                    elif decisao == 'tipo musical':
                        novo_musica = input('Digite o novo tipo musical de preferência (ou deixe em branco para apagar): ')
                        f_temp.write(f'{dados[0]};{dados[1]};{dados[2]};{novo_musica};{dados[4]}')
                    
                    elif decisao == 'contato':
                        novo_contato = input('Digite os novos dados de contato (ou deixe em branco para apagar): ')
                        f_temp.write(f'{dados[0]};{dados[1]};{dados[2]};{dados[3]};{novo_contato}')
                    
                    else:
                        print('Opção inválida!')
                        time.sleep(1.5)
                        return editar_perfil
                
                else:
                    f_temp.write(f'{linha}')

        f.close()
        f_temp.close()

        if encontrado:
            with open('local.csv', 'w', encoding='utf8') as f, open('local_temp.csv', 'r', encoding='utf8') as f_temp:
                f.write(f'{f_temp.read()}')
            f.close()
            f_temp.close()

            with open('local_temp.csv', 'w') as f:
                pass
            f.close()
            
        
            print('Informações atualizadas com sucesso!')
        
        else:
            with open('local_temp.csv', 'w') as f:
                pass
            f.close()

            print('Perfil do local não encontrado')

        input('Aperte enter para voltar: ')
        return menu_perfil()
    
    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_perfil() #voltar para o menu


def ver_locais(): #ver todos os locais
    try:
        clear()
        with open('local.csv', 'r', encoding='utf8') as f:
            linhas = f.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')

                print(f'Nome: {dados[0]} // Tipo: {dados[1]} // Endereço: {dados[2]} // Tipo musical: {dados[3]} // Contato: {dados[4]}')
        f.close()
        input('Aperte enter para voltar: ')
        return menu_principal()

    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_principal() #voltar para o menu
    

def ver_bandas(): #ver todas as bandas
    try:
        clear()
        with open('banda.csv', 'r', encoding='utf8') as f:
            linhas = f.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')

                print(f'Nome: {dados[0]} // Tipo: {dados[1]} // Integrantes: {dados[2]} // Tipo musical: {dados[3]} // Contato: {dados[4]}')
            f.close()
            input('Aperte enter para voltar: ')
            return menu_principal()

    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_principal() #voltar para o menu
    

def ver_agenda():
    try:
        clear()
        with open('agenda.csv', 'r', encoding='utf8') as f:
            linhas = f.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')

                print(f'Banda: {dados[0]} // Local: {dados[1]} // Data: {dados[2]} // Horário de início: {dados[3]} // Horário de encerramento: {dados[4]}')
        f.close()
        input('Aperte enter para voltar: ')
        return menu_agenda()

    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_agenda() #voltar para o menu

def adicionar_agenda(): #adicionar um show na agenda
    try:
        clear()
        with open('agenda.csv', 'a', encoding='utf8') as f:
            banda = input('Digite o nome da banda: ')
            data = input('Digite a data: ')
            hora_i = input('Digite o horário de início: ')
            hora_f = input('Digite o horário de encerramento: ')

            f.write(f'{banda};{nome};{data};{hora_i};{hora_f}\n')
        f.close()
        loading()
        return menu_agenda()

    except:
        print('ERRO DO SISTEMA')
        time.sleep(1.5)
        return menu_agenda() #voltar para o menu


def editar_agenda():
    try:
        clear()
        encontrado = False
        with open('agenda.csv', 'r', encoding='utf8') as f, open('agenda_temp.csv', 'w', encoding='utf8') as f_temp:
            linhas = f.readlines()
            banda = input('Digite o nome da atração do show: ')
            
            for linha in linhas:
                dados = linha.strip().split(';')

                if banda == dados[0] and nome == dados[1]:
                    encontrado = True

                    print(f'Banda: {dados[0]} // Local: {dados[1]} // Data: {dados[2]} // Horário de início: {dados[3]} // Horário de encerramento: {dados[4]}')
                    decisao = input('Qual informação deseja editar: ').lower()

                    if decisao == 'banda':
                        nova_banda = input('Digite o novo nome da atração: ')
                        if nova_banda == '':
                            nova_banda = dados[0]
                        linha = f'{nova_banda};{dados[1]};{dados[2]};{dados[3]};{dados[4]}'
                    
                    elif decisao == 'local':
                        novo_local = input('Digite o novo local: ')
                        if novo_local == '':
                            novo_local = dados[1]
                        linha = f'{dados[0]};{novo_local};{dados[2]};{dados[3]};{dados[4]}'
                    
                    elif decisao == 'data':
                        nova_data = input('Digite a nova data (ou deixe em branco para apagar): ')
                        linha = f'{dados[0]};{dados[1]};{nova_data};{dados[3]};{dados[4]}'
                    
                    elif decisao == 'horário de início':
                        novo_hora_i = input('Digite o novo horário de início (ou deixe em branco para apagar): ')
                        linha = f'{dados[0]};{dados[1]};{dados[2]};{novo_hora_i};{dados[4]}'
                    
                    elif decisao == 'horário de encerramento':
                        novo_hora_f = input('Digite o novo horário de encerramento (ou deixe em branco para apagar): ')
                        linha = f'{dados[0]};{dados[1]};{dados[2]};{dados[3]};{novo_hora_f}'
                    
                    else:
                       linha = f'{linha}'
                
                f_temp.write(f'{linha}')
        f.close()
        f_temp.close()
        if encontrado:
            with open('agenda.csv', 'w', encoding='utf8') as f, open('agenda_temp.csv', 'r', encoding='utf8') as f_temp:
                f.write(f'{f_temp.read()}')

            f.close()
            f_temp.close()

            with open('local_temp.csv', 'w') as f:
                pass
            f.close()
        
            print('Agenda atualizada com sucesso!')
        
        else:
            with open('local_temp.csv', 'w') as f:
                pass
            f.close()

            print('Nenhum show correspondente encontrado!')
        
        input('Aperte enter para voltar: ')
        return menu_agenda()

    except FileNotFoundError:
        print('ERRO DO SISTEMA (arquivo inexistente)')
        time.sleep(1.5)
        return menu_agenda() #voltar para o menu
    
menu_principal()