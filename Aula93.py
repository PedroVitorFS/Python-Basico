# Try, except, else e finally

try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError: 
    print('Dividiu por zero.')
except NameError:
    print('Nome b nao esta definido')
except (IndexError, TypeError) as error:
    print('TypeError, IndexError')
    print('MSG: ', error)
    print('Nome: ',  error.__class__.__name__)
except Exception:
    print('Erro Desconhecido')
else: #executa caso nao de erro
    print('nao deu erro')
finally: #executa independente do erro
    print('Fechar Arquivo')

print('CONTINUAR')