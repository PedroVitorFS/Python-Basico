"""
Criem funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""

def duplica(numero):
    return numero * 2

def triplica(numero):
    return numero * 3

def quadruplica(numero):
    return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)    

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))