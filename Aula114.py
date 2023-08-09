# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter :
# - Um problema que possa ser divido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão 
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim = 10):
    if inicio >= fim:
        return fim
    
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)