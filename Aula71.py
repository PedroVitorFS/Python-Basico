"""
args - Argumentos não nomeados
* - *args (empacotamentos e desempacotamento)
"""

# Lembre-sse de d\esempacotamento

x, y, *resto = 1,2,3,4
print(x, y, resto)

def soma(*args): #Argumentos não nomeados na função
    total = 0
    for numero in args:
        total = total + numero

    return total    

soma = soma(1,2,3,4,5,6,7,8)


#desempacotamento de funcao 
numeros = 1,2,3,4,5,6,7,8
outra_soma = soma(*numeros)
    
