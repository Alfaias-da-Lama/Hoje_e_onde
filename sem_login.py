import menu
import display as dp
def pagina_semlog():
    try:
        escolha = menu.menu2(titulo="Hoje é Onde?", componentes=["Ver locais", "Ver bandas", "Ver agenda","Seguir show", "Voltar ao menu"])
        if escolha == 1:
            dp.mostrarlocal()
        elif escolha == 2:
            dp.mostrarbanda()
        elif escolha == 3:
            dp.mostraragenda()
        elif escolha == 4:
            print("Para seguir shows, voce precisa criar um cadastro de público")
        elif escolha == 5:
            break
        else:
            print("\33[31mEscolha uma opção válida\33[m")
    except(KeyboardInterrupt):
        print("Voltando ao menu principal...")