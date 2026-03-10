from  datetime import date
from utils.helper import date_para_str, str_para_date
from utils.helper import validar_cpf
from models.endereco import Endereco
from utils.validador_cep import busca_endereco_por_cep



class Cliente:
    contador: int = 101

    def __init__(self, nome: str, cpf: str, email: str, data_nascimento: str, cep: str) -> None:
        validar_cpf(cpf)

        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: str  = cpf
        self.__email: str  = email
        self.__data_nascimento:  date = str_para_date(data_nascimento)
        self.__cep: str = cep

        self.__endereco: Endereco | None = None

        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

        self.__busca_endereco() 


        def __buscar_endereco(self) -> None:
            try:
                  dados = busca_endereco_por_cep(self.__cep)
                  self.__endereco = Endereco(
                        dados.get("logradouro"),
                        dados.get("bairro"),
                        dados.get("cidade"),
                        dados.get("estado")
                      
                  )
            except ValueError as e:
                print(f"Erro de CEP: {e}")

            except ConnectionError:
                print("Erro ao conector com serviço de CEP")

            except Exception as e:
                print(f"Erro inesperado {e}"
                      )




   # ======================
    # PROPERTIES
    # ======================

    @property
    def codigo(self) -> int:
        return self.__codigo
    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def email(self) -> str:
        return self.__email

    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def cep(self) -> str:
        return self.__cep

    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadastro)
    
    @property
    def endereco(self) -> Endereco | None:
        return self.__endereco

    # ======================
    # MÉTODO STRING
    # ======================

    def __str__(self) -> str:

        endereco_str = ""

        if self.__endereco:
            endereco_str = str(self.__endereco)

        return (
            f'Código: {self.codigo}\n'
            f'Nome: {self.nome}\n'
            f'Data de Nascimento: {self.data_nascimento}\n'
            f'Cadastro: {self.data_cadastro}\n'
            f'{endereco_str}'
        )

        

