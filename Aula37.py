"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira -
Loop infinito -> Quando um código não tem fim

Função continue termina aquele ciclo e volta ao while
Função break termina o while
"""

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        continue

    print(contador)

    if contador == 40:
        break

print('acabou')