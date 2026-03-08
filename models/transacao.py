from datetime import datetime


class Transacao:

    def __init__(self, tipo: str, valor: float):
        self.__tipo = tipo
        self.__valor = valor
        self.__data = datetime.now()

    # ======================
    # PROPERTIES
    # ======================

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def data(self):
        return self.__data

    # ======================
    # MÉTODO STRING
    # ======================

    def __str__(self):
        return (
            f"{self.data.strftime('%d/%m/%Y %H:%M')} | "
            f"{self.tipo} | "
            f"R$ {self.valor:.2f}"
        )