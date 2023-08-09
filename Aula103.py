# Funções decoradoras e decoradores
# Decorar = Adicionar / remover / restringir / alterar
# Fugões decoradores são funções que decorar outras funções
# Decoradores são usados para fazer o Python
# Usar funções decoradoras em outras funções

#kwargs = keywords arguments (argumentos nomeados)
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

#inverte_string_checando_parametro = criar_funcao(inverte_string)
#print(inverte_string_checando_parametro('123'))
print(inverte_string('123'))