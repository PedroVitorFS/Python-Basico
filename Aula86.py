lista = [
    ('a', 'valor a'), 
    ('b','valor b'), 
    ('c', 'valor c')
]

dc = {
    chave: valor
    for chave, valor in lista
}

dict(dc) #mesma função

print(dc)

s1 = {i for i in range(10)}
print(s1)