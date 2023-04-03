import Aula98_m
import importlib

print(Aula98_m.variavel)

for i in range(10):
    print(i)
    import aula98_m #modulos em python sao singonton, sao iniciados somente uma vez e sao salvos na memoria
    importlib.reload(aula98_m) #caso queira reiniciar o modulo
    print(i)

print('Fim')