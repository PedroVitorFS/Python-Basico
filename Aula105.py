# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): #Para pegar os parâmetros do decorador
    def fabrica_de_funcoes(func): #Para pegar a função
        print('Decoradora 1')

        def aninhada(*args, **kwargs): #É a função que irá executar
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores(1,2,3)(lambda x, y: x * y)

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)