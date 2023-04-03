import copy

#Exercícios
#Aumente os preços dos produtos a seguir em 10%
#Gere novos produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco' : 10.00},
    {'nome': 'Produto 1', 'preco' : 22.32},
    {'nome': 'Produto 3', 'preco' : 10.11},
    {'nome': 'Produto 2', 'preco' : 105.87},
    {'nome': 'Produto 4', 'preco' : 69.90}
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtor por preço crescente (do menor para maior)
# Gere produtos_ordenados_por_preço por deep copy (cópia profunda)


novos_produtos = [
    {**produto, 'preco' : round(produto['preco'] * 1.10, 2)}
    for produto in produtos
]

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(
    key=lambda item: item['nome'], 
    reverse=True
)

produtos_ordenados_por_preço = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preço.sort(key=lambda item : item['preco'])

print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preço, sep='\n')