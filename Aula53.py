"""
enumerate = enumera iteraveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

lista_enumerada = enumerate(lista)

#se colocar o enumerate() em uma variavel ele lera o for apenas uma vez, pois o ponteiro parou no ultimo valor da lista
#for item in lista_enumerada:
#    print(item)


for item in enumerate(lista):
    #indice, nome = item
    print(item)