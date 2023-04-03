#Empacotamento e desempacotamento de dicionarios

a,b =1,2
a,b = b,a

pessoa = {
    'nome' : 'Aline', 
    'sobrenome' : 'souza'
}

(a1,a2), (b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)


pessoa = {
    'nome' : 'Aline', 
    'sobrenome' : 'souza'
}

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.6
}

pessoas_completa = {**pessoa, **dados_pessoa}

#args e kwargs
#args (ja vimos)
#kwargs = keywords arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Nao nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave,valor)

mostro_argumentos_nomeados(1,2,nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)

    