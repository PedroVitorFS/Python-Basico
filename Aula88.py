# Valor Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 Nome False range(0,10)

lista = []  
dicionario = {} 
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
#todos os valores acima retornarão False

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('Teste'))