"""
Métodos uteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves 
values - iterável com os valores
items - iterável com chaves e valores
setdefault = adiciona valor se a chave nao existe
copy - retorna uma copia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada
poitem - apaga o ultimo item adicionado 
update - atualiza um dicionario com outro
"""
import copy

pessoa = {
    'nome' : 'Luiz Otávio', 
    'sobrenome' : 'Miranda', 
}

print(len(pessoa))
print(tuple(pessoa.keys()))
print(pessoa.values())
#for chave, valor in pessoa.items():
#    print(chave, valor)
pessoa.setdefault('idade', 0) #seta o valor padrao caso a chave nao exista
pessoa2 = pessoa.copy() #copia nao entra em subníveis, apenas aponta o local da memoria
pessoa3 = copy.deepcopy(pessoa) #faz uma copia profunda com todos os niveis
pessoa.get('nome', 'Nao existe') #sem o segundo método ele retorna None
nome = pessoa.pop('nome') #retira a chave e retorna o valor que estava na chave
ultima_chave = pessoa.popitem() #retira a ultima chave do dicionario
pessoa.update({
    'nome' : 'novo valor', 
    'idade' : 30
})
pessoa.update(nome='novo valor', idade=30)
tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
pessoa.update(tupla)