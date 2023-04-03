#Desempacotamento em chamadas
#de metodos e funcoes

string = 'ABCD'
lista = ['Maria', 'Helena',1,2,3, 'Eduarda']
tupla = 'Python', 'e', 'legal'
salas = [
    ['Maria', 'Helena'], 
    ['Elaine'],
    ['Luiz', 'Pedro', 'Eduarda']
]

#a, b, c, *_, ultimo = lista
#print(a, c, ultimo)


#for nome in lista:
#    print(nome, end=' ', sep=' ')

#print(*lista, end=' ')


print(*salas, sep='\n')