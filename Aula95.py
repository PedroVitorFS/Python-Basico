# raise - lançando exceções (erros)

"""
def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('____')
        raise #relança o erro
"""

def divide(n, d):
    if d == 0:
        raise ZeroDivisionError('Voce esta tentando dividindo por zero')
        
    return n/d

print(divide(8, 0))