from datetime import date
from datetime import datetime


# =====================================================
# FUNÇÃO 1
# Recebe uma DATA (objeto date)
# e retorna uma STRING formatada no padrão brasileiro
# Exemplo: 2026-03-04 -> "04/03/2026"
# =====================================================
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


# =====================================================
# FUNÇÃO 2
# Recebe uma STRING de data
# e converte para o tipo DATE
# Exemplo: "04/03/2026" -> date(2026, 3, 4)
# =====================================================
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y').date()


# =====================================================
# FUNÇÃO 3
# Recebe um valor FLOAT
# e retorna uma STRING formatada como moeda brasileira
# Exemplo: 1500 -> "R$ 1.500,00"
# =====================================================
def formata_float_str_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}"

# =====================================================
# FUNÇÃO 4
# Validação básica de CPF (APENAS PARA TESTES)
#
# Regras atuais:
# ✔ CPF deve ser string
# ✔ Deve possuir 11 caracteres
# ✔ Deve conter apenas números
#
# OBS:
# Ainda NÃO valida os dígitos oficiais do CPF
# =====================================================
def validar_cpf(cpf: str):

    # verifica se o CPF é texto
    if not isinstance(cpf, str):
        raise TypeError("CPF deve ser uma string")

    # verifica tamanho e se contém somente números
    if len(cpf) != 11 or not cpf.isdigit():
        raise TypeError("CPF inválido")