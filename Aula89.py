# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'
if hasattr(string, metodo): #verifica se existe a função
    print('Existe a função upper')
    print(getattr(string, metodo)())
    print(string.upper())
else:
    print('Nao existe o método', metodo)