# Módulos padrão do Python (import, from, ase *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
#Desvantagens: nomes grandes

#partes - from nome_modulo import objeto1, objeto2
#Vantagens: nomes pequenos
#Desvantagens: Sem o namespace do módulo

#alias 1 - import nome_modulo as apelido
#alias 2 = from nome_modulo import objeto as apelido
#Vantagens: você pode reservar nomes para seu código
#Desvantagens: pode ficar fora do padrão da linguagem

import sys 
from sys import exit, platform #importa
from sys import platform as p #apelido para variavel
import sys as s #apelido do modulo

print(sys.platform)
print(s.platform)
print(platform)
print(p)

#sys.exit() #sai do programa


# má prática - from nome_modulo import *
#vantagens: importa tudo de um módulo
#Desvantagens: importa tudo de um módulo

from sys import *

print(platform)
exit()