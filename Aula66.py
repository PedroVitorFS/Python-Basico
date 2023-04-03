"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(x+y)

soma(1,2)

#Todos os argumentos que foram nomeados, os próximos obrigatoriamente precisarão ser nomeados também
soma(y=2, x=1)