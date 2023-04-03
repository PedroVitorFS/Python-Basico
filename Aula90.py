import sys

#Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #__item__ e __next__
#A cada next ele aponta para a proxima posição do ponteiro
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#a diferença da lista para o generator e que a mesma guarda todos os dados na memoria
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
#porem generator nao tem tamanho, nao tem indice
for n in generator:
    print(n)
