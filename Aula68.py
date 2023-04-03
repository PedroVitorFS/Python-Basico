"""
Escopo de funções me Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
"""
x=1

def escopo():
   global x #alterar o x de escopo global
   x = 10 
   def outra_funcao():
        y=2
        print(x, y)
   outra_funcao()
   print(x)     

escopo()
