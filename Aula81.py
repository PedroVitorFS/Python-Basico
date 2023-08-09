#função lambda simples

# A função lambda é uma função como qualquer 
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja,, tudo
# dever ser contido dentro de um único expressão

lista = [
    {'nome' : 'Luiz', 'sobrenome' : 'miranda'},
    {'nome' : 'Maria', 'sobrenome' : 'Oliveira'},
    {'nome' : 'Daniel', 'sobrenome' : 'Silva'},
    {'nome' : 'Eduardo', 'sobrenome' : 'Moreira'},
    {'nome' : 'Aline', 'sobrenome' : 'Souza'},
]

def ordena(item):
    return item['nome']

lista.sort(key=ordena)
lista.sort(key=lambda item: item['nome'])

lista2 = sorted(lista, key=lambda item : item['nome'])
print(lista)