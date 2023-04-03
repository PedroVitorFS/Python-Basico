lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))


for pos,nome in enumerate(lista):
    print(pos, nome)

print('\r\n')

for indice in indices:
    print(indice, lista[indice]) 