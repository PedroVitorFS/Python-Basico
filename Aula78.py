"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis omo valor interno.

Criando um set
set(iterável) ou {1,2,3}

Sets são eficientes para remover valores duplicados
de iteráveis.
- eles não tem indexes
- eles não garantem ordem
- eles são iteráveis (for, in, not in)

Métodos úteis
add, update, clear, discard

Operadores úteis
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""
#s1= set() #vazio
#s1 = {'Luiz', 1,2,3} #com dados
s1 = {1,2,3,4,3,3,3,1} #sets eliminam valores repetidos
s1.add('Luiz')
s1.update(('Ola mundo',1,2,3,4))
s1.discard('Ola mundo')
print(s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #une os dois sets
s3 = s1 & s2 #mostra os itens iguais entre os sets
s3 = s1 - s2 #mostra o item que so esta presente no set da esquerda
s3 = s2 ^ s1  #mostra os itens que não estão presentes em ambos