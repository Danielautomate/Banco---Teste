from typing import List, Dict, Optional
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: list[Conta] = []


def main( ) -> None:
    while True:
        menu()


######################## MENU #######################
def menu() -> None:
    print('\n==============================================')
    print('=================== Bem Vindo ==================')
    print('================= Banco Center =================')
    print('================================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Criar conta')
    print('2 - Saque')
    print('3 - Desposito ')
    print('4 - Transferir ')
    print('5 - Lista Conta')
    print('6 - Saldo ')
    print('7 - Sair ')
    
    try:
        opcao = input('Opção: ').strip()
        

        op = {

            '1': cria_conta,
            '2': efetuar_saque,
            '3': efetuar_depositor,
            '4': efetuar_transferencia,
            '5': lista_conta,
            '6': saldo,
            '7': sair
        }
        if opcao in op:
            op[opcao]()
        else:
            print("Opção invalida ")



    except ValueError:
        print("Erro: Digite apena opção validas ")
    


def cria_conta() -> None:
    pass

def efetuar_saque() -> None:
    pass


def efetuar_depositor() -> None:
    pass


def efetuar_transferencia() -> None:
    pass


def lista_conta() -> None:
    pass
    
def saldo() -> None:
    pass

def buscar_conta_por_numero(numero: int) -> Optional[Conta]:
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None


def sair():
    print("Saindo do Sistema.......")
    sleep(2)
    exit()



if __name__ == '__main__':
    main