menu.py

from Banco import Banco

def menu(opcao):
    banco = Banco()
    if opcao == 1:
        banco.cadastrar_entrega()
    elif opcao == 2:
        banco.alterar_entrega()
    elif opcao == 3:
        banco.buscar_entrega()
    elif opcao == 4:
        print ('Saindo... :)')
        exit()


if __name__ == '__main__':
    while True:
        opcao = int(input('digite uma opcao: ')
        menu(opcao)
