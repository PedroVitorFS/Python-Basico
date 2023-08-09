# from modulo_b import fala_oi #nao e possível importar esse modulo para o main
from Aula99_package.modulo_b import fala_oi # e possível utilizar o modulo b na main

__all__ = [
    'variavel', 
    'soma_do_modulo',
    'nova_variavel'
] #define quais funções poderão ser acessadas ao importar o *

variavel  = 'Alguma coisa'
def soma_do_modulo(x, y):
    return x + y

nova_variavel = 'ok'

fala_oi()