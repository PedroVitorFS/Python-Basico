"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo 
par de "chave" e "valor"
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis 
como: str, int, float, bool, tuple, ec.
Usamos as chaves = {} - ou a classe dict para criar dicionaários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

pessoa = {
    'nome' : 'Luiz Otávio', 
    'sobrenome' : 'Miranda', 
    'idade' : 18, 
    'altura' : 1.8, 
    'enderecos' : [
        {'rua' : 'tal tal' , 'numero' : 123},
        {'rua' : 'outra rua' , 'numero' : 321}
    ]
}

print(pessoa, type(pessoa))
"""

pessoa = {
    'nome' : 'Luiz Otávio', 
    'sobrenome' : 'Miranda', 
    'idade' : 18, 
    'altura' : 1.8, 
    'enderecos' : [
        {'rua' : 'tal tal' , 'numero' : 123},
        {'rua' : 'outra rua' , 'numero' : 321}
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])

del pessoa['sobrenome']

if pessoa.get('sobrenome') : #tenta pegar a chave, caso não encontre retorna None
    print(pessoa.get('sobrenome'))

for chave in pessoa:
    print(chave, pessoa[chave])

if pessoa.get('sobrenome') is None: #Verifica se a chave existe
    print('Existe')
else:
    print('Nao existe')    
