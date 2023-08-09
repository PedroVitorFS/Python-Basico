import Aula98_m
import importlib

print(Aula98_m.variavel)

for i in range(10):
    print(i)
    import Aula98_m #modulos em python sao singleton, sao iniciados somente uma vez e sao salvos na memoria
    importlib.reload(Aula98_m) #caso queira reiniciar o modulo
    print(i)

print('Fim')