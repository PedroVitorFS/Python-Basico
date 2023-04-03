# Yield from

def gen1():
    print('COMEÇOU GEN1')
    yield 1 
    yield 2
    yield 3
    print('TERMINOU G1')

def gen2(gen):
    print('COMEÇOU GEN2')
    if gen is None:
        yield from gen
    yield from gen
    yield 4 
    yield 5 
    yield 6
    print('TERMINOU G2')

def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('TERMINOU GEN3')


g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)
