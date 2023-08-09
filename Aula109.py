# combination, permutation e product - Itertools
# Combinação - Ordem não importa - iterável _ tamanho do grupo 
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
          print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas =  [
    ['preta', 'branca'],
    ['p', 'm'], #tamanhos das roupas
    ['masculino', 'feminino'],
    ['algodão', 'poliéster']
]

print(*list(combinations(pessoas, 2)), sep='\n')
print(*list(permutations(pessoas, 2)), sep='\n')
print_iter(product(*camisetas))