#Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul', 
    'preco':2.5,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in produto.items()
    #if isinstance(valor, float) #so ira ser adicionado tipo float no dict
}

print(dc)

