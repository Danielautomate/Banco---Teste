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
            '3': efetuar_deposito,
            '4': efetuar_transferencia,
            '5': lista_conta,
            '6': extrato,
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

#===================== SAQUE ==========================

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

#==================== DESPOSITO =======================
def efetuar_deposito() -> None:
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

#==================== TRANSFERENCIA ==================
def efetuar_transferencia() -> None:

    # Verifica se existe alguma conta cadastrada
    if not contas:
        print("Nenhuma conta cadastrada.")
        sleep(2)
        return

    try:
        # Solicita o número da conta de origem
        numero_origem: int = int(input("Informe o número da conta de origem: ").strip())

        # Busca a conta na lista de contas
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        # Se a conta não existir
        if not conta_origem:
            print(f"Conta {numero_origem} não encontrada.")
            sleep(2)
            return

        # Solicita a conta de destino
        numero_destino: int = int(input("Informe o número da conta destino: ").strip())

        # Verifica se o usuário tentou transferir para a mesma conta
        if numero_origem == numero_destino:
            print("Não é possível transferir para a mesma conta.")
            sleep(2)
            return

        # Busca a conta destino
        conta_destino: Conta = buscar_conta_por_numero(numero_destino)

        # Verifica se a conta destino existe
        if not conta_destino:
            print(f"Conta {numero_destino} não encontrada.")
            sleep(2)
            return

        # Solicita o valor da transferência
        valor: float = float(input("Informe o valor da transferência: ").strip())

        # Valida valor
        if valor <= 0:
            print("Valor inválido.")
            sleep(2)
            return

        # Executa a transferência
        conta_origem.transferir(conta_destino, valor)

        print("Transferência realizada com sucesso!")

    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Digite apenas números válidos.")

    # Pausa para o usuário ver a mensagem
    sleep(2)

# ======================= CONTAS CADASTRADA ===========
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

#=============== EXTRATO ================================
def extrato(self):

    print("\n===== EXTRATO =====")

    if not self.__extrato:
        print("Nenhuma movimentação.")
        return

    for transacao in self.__extrato:
        print(transacao)

    print("--------------------")
    print(f"Saldo atual: R$ {self.saldo_total:.2f}")


#================= PROCURA CONTA ========================
def buscar_conta_por_numero(numero: int) -> Optional[Conta]:
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None

#====================== FINALIZAR SISTEMA ================
def sair():
    print("Saindo do Sistema.......")
    sleep(2)
    exit()



if __name__ == '__main__':
    main()