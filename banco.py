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
    

#================== CRIANDO CONTA ================
def cria_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input("E-mail do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")
    cep: str = input ("informe o CEP do cliente: ")

    cliente: Cliente = Cliente(nome,cpf, email, data_nascimento, cep)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso")
    print("Dados da conta: ")
    print("-----------------")
    print(conta)
    sleep(2)

def efetuar_saque() -> None:
 
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    try:
        numero: int = int(input('Informe o número da conta: ').strip())
        conta: Conta = buscar_conta_por_numero(numero)

        if not conta:
            print(f'Conta {numero} não encontrada.')
            return

        valor: float = float(input('Informe o valor do saque: ').strip())
        conta.sacar(valor)

    except ValueError:
        print("Digite apenas números válidos.")

    sleep(2)


def efetuar_depositor() -> None:
    if not contas:
        print("Nenhuma conta Cadastrada.")
        return
    
    try:
        numero: int = int(input("Informe o número da conta: ").strip())
        conta: Conta = buscar_conta_por_numero(numero)

        if not conta:
            print(f'conta {numero} não encontrada.')
            return
        valor: float = float(input("Informe o valor do despósito: ").strip())
        conta.deposita(valor)


    except ValueError:
        print("Digite apenas números válidos.")

    sleep(2)



def efetuar_transferencia() -> None:
    if not contas:
        print("Nenhuma conta Cadastrada.")
        return
    
    try:
        numero_origem: int = int(input("informe o número da conta: ").strip())
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)
        
        if not conta_origem:
            print(f'Conta {numero_origem} não encontrada')
            return
        
        numero_destino: int = int(input('Informe o número da conta destino.').strip())
        conta_destino: Conta = buscar_conta_por_numero(numero_destino)

        if not conta_destino:
            print(f"Conta {numero_destino} não encontrada")
            return
        valor: float = float(input("Informe o valor da Transferência: ").strip())
        conta_origem.transferir(conta_destino, valor)

        if numero_destino == numero_destino:
            print("Não e possivel Transfereir para mesma conta ")
            return

    except ValueError:
        print("Digite apenas números válidos.")

    sleep(2)

def lista_conta() -> None:
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print(f"Total de contas: {len(contas)}")

    for i, conta in enumerate(contas, start= 1):
        print(f'conta {i}')
        print(conta)
        print('----------------')
        sleep(1)
    
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
    main()