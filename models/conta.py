from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    # Variável de classe usada para gerar número automático da conta
    codigo: int = 1001

    def __init__(self, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100
        Conta.codigo += 1


    # Método que define como o objeto será exibido quando usado no print()
    def __str__(self) -> str:
        return f"Número da conta: {self.numero} \nCliente: {self.cliente.nome}" \
               f"\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}"


    # Property para acessar o número da conta
    @property
    def numero(self) -> int:
        return self.__numero


    # Property para acessar o cliente da conta
    @property
    def cliente(self) -> Cliente:
        return self.__cliente


    # Property para acessar o saldo da conta
    @property
    def saldo(self) -> float:
        return self.__saldo


    # Setter permite alterar o saldo
    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor


    # Property para acessar o limite da conta
    @property
    def limite(self) -> float:
        return self.__limite


    # Setter para alterar o limite
    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor


    # Property que retorna o saldo total disponível
    # (saldo da conta + limite de crédito)
    @property
    def saldo_total(self) -> float:
        return self._calcular_saldo_total()


    # Método interno que calcula o saldo total
    def _calcular_saldo_total(self) -> float:
        return self.saldo + self.limite


    # Método para depositar dinheiro na conta
    def deposita(self, valor: float) -> None:
        self.saldo += valor


    # Método para sacar dinheiro
    def sacar(self, valor: float) -> None:
        pass


    # Método para transferir dinheiro para outra conta
    def transferir(self, destino: object, valor: float) -> None:
        pass