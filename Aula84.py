#List comprehension em Python
#List comprehension e uma forma rápida ara criar listas
#a partir de iteráveis

lista = []
for numero in range(10):
    lista.append(numero)


lista = [
    numero * 2
    for numero in range(10)
]

#print(lista)

produtos = [
    {'nome' : 'p1', 'preco' : 20},
    {'nome' : 'p2', 'preco' : 10},
    {'nome' : 'p3', 'preco' : 30},
]

novos_produtos = [
    {**produto,'preco': produto['preco'] * 10}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
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