# Introducao as Generator functions em Python
# generator = (n fon n in range(1000000))

def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mas uma...')
    yield 3
    print('Vou terminar')
    return 'Acabou'
    

gen = generator(n=0)
print(next(gen)) #vai pausar no 1
print(next(gen)) #ira continuar o codigo
print(next(gen)) #ira continuar o codigo

for n in gen:
    print(n)

def generator(n=0, maximum=10):
    while True:
        yield n

        if n >= maximum:
            return 
        
        n+=1

gen = generator(maximum=1000000)
for n in gen:
    print(n)