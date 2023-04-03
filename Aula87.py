#isinstance - para saber se objeto e de determinado tipo

lista = [
    'a', 1,1.1,True, [0,1,2], (1,2), {0,1}, {'nome': 'Lui'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)

    if isinstance(item, (int, float))
        print(item, item * 2)
    print(item, isinstance(item, set))

