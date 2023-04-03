"""
Crie uma função que mutiplica todos os argumentos
não nomeados recebidos
Retorner o total para uma variável e mostre o valor
da variavel

crie uma função fala se um número é par ou ímpart

retrone se o número é parte ou impar
"""


def multplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total      

mulplicado = multplica(1,2,3,4,5)
print(mulplicado)


def parImpar(numero):
    if (numero % 2 == 0):
        return f'O numero {numero} e par'
    else:
        return f'O número {numero} é impar'

print(parImpar(2))
print(parImpar(1))