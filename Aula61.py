"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF 
multiplicando cada um dos valor por uma contagem regressiva começando de 10

Ex.: 746.824.890-70 (74682489070)
    10 9  8  7  6  5  4  3  2 
*   7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27 0

Somar todos os resultador:
70+36+48+56+12+20+32+27+0 = 301
Mutiplicar o resultado anterior por 10
301 * 10 = 301-
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
resultado é 0
contrário disso:

O primeiro dígito do CPF é 7
"""
import re
import sys

entrada = str(input('Digite um cpf: '))
#cpf = '412.785.600-92'.replace('.', '').replace('-', '').replace(' ', '')
cpf = re.sub(
    r'[^0-9]',
    '', 
    entrada
) #expressao regular

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if(entrada_e_sequencial):
    print('Voce enviou dados seguenciais')
    sys.exit()

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