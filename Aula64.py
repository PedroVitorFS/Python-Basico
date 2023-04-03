"""
Criador de cpf
"""
import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

soma_valores_digito1 = 0
for pos1, digito in enumerate(cpf[:9]):
    digito = int(digito)
    valor_multiplicado_1 = digito *  (10 - pos1)
    soma_valores_digito1 += valor_multiplicado_1

valor_total_digito_1 = soma_valores_digito1 * 10
resto_valor_digito_1 = valor_total_digito_1 % 11
digito_1 = 0 if resto_valor_digito_1 > 9 else resto_valor_digito_1

soma_valores_digito2 = 0
for pos2, digito in enumerate(cpf[:10]):
    digito = int(digito)
    valor_multiplicado_2 = digito *  (11 - pos2)
    soma_valores_digito2 += valor_multiplicado_2

valor_total_digito_2 = soma_valores_digito2 * 10
resto_valor_digito_2 = valor_total_digito_2 % 11
digito_2 = 0 if resto_valor_digito_2 % 11 > 9 else resto_valor_digito_2

novo_cpf = f'{cpf[:9]}{digito_1}{digito_2}'

if(novo_cpf == cpf) :
    print('cpf valido', novo_cpf)
else:
    print('cpf invalido', novo_cpf)    