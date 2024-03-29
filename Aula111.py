from functools import partial
from types import GeneratorType
#map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    
produtos = [
    {'nome' : 'Produto 5', 'preco': 10.00}, 
    {'nome' : 'Produto 1', 'preco': 22.32}, 
    {'nome' : 'Produto 3', 'preco': 10.11}, 
    {'nome' : 'Produto 2', 'preco': 105.87}, 
    {'nome' : 'Produto 4', 'preco': 69.90}, 
]

def aumentar_porcetagem(valor, porcentagem):
    return round(valor*porcentagem)

aumentar_dez_porcent  = partial(
    aumentar_porcetagem, 
    porcentagem=1.1
)

novos_produtos = [
    {**p,
      'preco' : aumentar_dez_porcent(p['preco'])}
     for p in produtos
]

print(novos_produtos)


def muda_preco_de_produtos(produto):
    return {
        **produto, 
        'preco' : aumentar_dez_porcent(
            produto['preco']
        )
    }

novos_produtos = map(
    muda_preco_de_produtos, 
    produtos
)

print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))


print(map(
            lambda x: x*3,
            [1,2,3,4]
        )
    )