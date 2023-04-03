"""
Flag (bandeira_ - Marcar um local
None = Nao valor
is e is not = eh ou nao eh (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)