# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        print(locals()) #mostra quais sao as variáveis locais dessa função
        print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        #variáveis fora do escopo só podem ser lidas, mas não alteradas
        nonlocal valor_final #informar que a variável não é local para buscar o valor anterior
        valor_final += valor_a_concatenar 
        return valor_final
    return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)