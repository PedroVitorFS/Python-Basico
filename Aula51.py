"""
Introducao ao desempacotamento + tuplas

Por convencao em python utilizasse o hifen para mostrar que a variavel nao sera utilizavel
"""

_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']

#Pegaram o nome na ultima posicao, o *_ retornara o resto da lista



print(nome, _)