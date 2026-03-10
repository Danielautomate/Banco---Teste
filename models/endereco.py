

class Endereco:
    def __init__(self: object, logradouro: str, bairro: str, cidade: str, estado: str):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado= estado
    
    def monstra_endeco(self: object) -> str:
        print("Endereço:")
        print(f"Rua: {self.logradouro}")
        print(f"Bairro: {self.bairro}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")