# List comprehension em Python
# List comprehension é uma forma rápida ara criar listas a partir de iteráveis.

lista = []
for numero in range(10):
    lista.append(numero)


lista = [
    (numero * 2)
    for numero in range(10)
]

#print(list(range(10)))
#print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome' : 'p1', 'preco' : 20},
    {'nome' : 'p2', 'preco' : 10},
    {'nome' : 'p3', 'preco' : 30},
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 10} #desempacota o preço e altera o valor da chave de preço
    if produto['preco'] > 20 else {**produto} #multiplica o valor do preço por 10 se o valor for maior que 20
    for produto in produtos
    if produto['preco'] > 10 #não inclui os valores menores que 10 na lista
]

print(novos_produtos)

#lista = [n for n in range(10) if n < 5]
#print(lista)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [letra for letra in 'Luiz']
    for x in range(3)
]
print(lista)