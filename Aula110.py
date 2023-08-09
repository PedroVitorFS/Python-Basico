#groupby - agrupando valores (itertools)
from itertools import groupby

alunos = ['a','a','a','a', 'b', 'c', 'a']
grupos = groupby(sorted(alunos))
print(*list(grupos))

for chave, grupo in grupos:
    print(chave)
    print(list(grupo)) #Ele irá retornar apenas o grupo que estão juntos, então o ultimos 'a' será um grupo separado do primeito

alunos = [
    {'nome' :'Luiz', 'nota' : 'A'},
    {'nome': 'Letícia', 'nota' : 'B'}, 
    {'nome': 'Fabrício', 'nota' : 'A'},
    {'nome': 'Rosemary', 'nota' : 'C'},
    {'nome': 'Joana', 'nota' : 'D'},
    {'nome': 'João', 'nota' : 'A'},
    {'nome': 'Eduardo', 'nota' : 'B'},
    {'nome': 'André', 'nota' : 'A'},
    {'nome': 'Anderson', 'nota' : 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupados, key=ordena) #alunos separados em grupos por nota

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)