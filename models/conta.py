from models.cliente import Cliente
from utils.helper import formata_float_str_moeda
from models.transacao import Transacao


class Conta:

    # Variável de classe usada para gerar número automático da conta
    codigo: int = 1001

    def __init__(self, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100
        self.__extrato = list[Transacao] = []
        Conta.codigo += 1


       # Define como o objeto será exibido quando usar print(conta)
    def __str__(self) -> str:
        return (
            f"Número da conta: {self.numero}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Saldo Total: {formata_float_str_moeda(self.saldo_total)}"
        )

    # ======================
    # PROPERTIES (GETTERS)
    # ======================

   # Retorna o número da conta
    @property
    def numero(self) -> int:
        return self.__numero


    # Retorna o cliente da conta
    @property
    def cliente(self) -> Cliente:
        return self.__cliente


    # Retorna o saldo da conta
    @property
    def saldo(self) -> float:
        return self.__saldo


    # Permite alterar o saldo
    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor


    # Retorna o limite da conta
    @property
    def limite(self) -> float:
        return self.__limite


    # Setter para alterar o limite
    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor


    # Retorna o saldo total disponível
    # (saldo da conta + limite de crédito)
    @property
    def saldo_total(self) -> float:
        return self.__saldo + self.__limite
    

     # ======================
    # MÉTODOS DA CONTA
    # ======================

    # Método para depositar dinheiro na conta
    def deposita(self, valor: float) -> None:
        # Verifica se o valor é positivo
        if valor > 0:
            # Soma o valor ao saldo
            self.saldo += valor

            transacao = Transacao("Depósito", valor)
            self.__extrato.append(transacao)

            print("Depósito efetuado com sucesso!")
        else:
            print("Erro ao efetuar depósito. Tente novamente.")


    # Método para sacar dinheiro
    def sacar(self, valor: float) -> None:

        # Verifica se o valor é positivo e se existe saldo disponível
        if valor > 0 and self.saldo_total >= valor:

            # Caso o saldo seja suficiente
            if self.saldo >= valor:
                self.saldo -= valor

            else:
                # Usa o limite quando o saldo não é suficiente
                restante: float = valor - self.saldo
                self.saldo = 0
                self.limite -= restante

            transacao =Transacao("Saque", valor)
            self.__extrato.append(transacao)

            print("Saque efetuado com sucesso!")

        else:
            print("Saque não realizado. Tente novamente!")


    # Método para transferir dinheiro para outra conta
    def transferir(self, destino: object, valor: float) -> None:

        # Verifica se existe saldo suficiente
        if valor > 0 and self.saldo_total >= valor:

            # Realiza o saque da conta atual
            self.sacar(valor)

            # Deposita na conta de destino
            destino.deposita(valor)

            transacao = Transacao("Transferência", valor)
            self.__extrato.append(transacao)

            print("Transferência realizada com sucesso!")

        else:
            print("Transferência não realizada, Tente novamnete!.")