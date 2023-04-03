"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Luiz Otávio'
#string[3] = 'ABC' #Erro, pois variaveis em python sao imutaveis
outra_variavel = f'{string[:3]}ABC{string[4:]}' #Criasse outra variavel
print(outra_variavel)