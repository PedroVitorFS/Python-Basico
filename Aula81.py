#funcao lambda simples

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