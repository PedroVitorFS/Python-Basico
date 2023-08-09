# try, except, else e finally

try:
    print('abrir arquivo')
except ZeroDivisionError:
    print('dividui zero')
else:
        print('nao deu erro')
finally: #irá executar de qualquer maneiro
     print('fechar arquivo')