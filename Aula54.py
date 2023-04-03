"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""
lista = []

while True:
    print("Selecione uma opção: ")
    valor = input("[i]inserir [a]apagar [i]listar: ")
    
    if(valor == 'i'):
        valor_inserido = input("Digite o produto que voce quer adicionar: ")
        lista.append(valor_inserido)
    elif(valor == 'a'):
        indice = int(input("Selecione o índice que quer apagar: "))
        try:
            lista.pop(indice)
        except IndexError as e:
            print("Esse indice nao existe na lista")
        except ValueError as e:
            print("o indice deve ser do tipo inteiro")
        except Exception as e:
            print('Erro desconhecido')        
    elif(valor == 'l'):
        try:
            for pos,item in enumerate(lista):
                print(pos, item)
        except:
            print('Nada para mostrar')    
    else:
        print('Valor Invalido')
        