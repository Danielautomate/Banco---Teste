from models.conta import Conta
from models.cliente import Cliente

from utils.validador_cep import busca_endereco_por_cep

try:
    cep = input("Digite o CEP: ")

    end = busca_endereco_por_cep(cep)

    print("\nEndereço encontrado:")
    print(end)

except ValueError as e:
    print("Erro:", e)

except ConnectionAbortedError as e:
    print("Erro de conexão:", e)