"""**kwargs"""

'''
- Podeeriamos charma este parametro (**xis), mas por conveção chamamos de **kwargs
- Este é mais um parâmetro, mas diferente do (*args), que coloca os valores extras em uma tupla, o (**kwargs), exige 
   que utilizamos parametros nomeados, e transforma esses parâmetros extras um Dicionario
'''
# Exemplo 1:


def cores_favoritas1(**kwargs):
    print(kwargs)


# print(cores_favoritas1(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco'))

# Exemplo 2: REFATORANDO A FUNÇÃO ANTERIOS


def cores_favoritas2(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


# cores_favoritas2(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

'''OBS: os parametros *args e **kwargs não são obrigatorios'''
# cores_favoritas2()


# ExempLo mais COMPLEXO
def cumprimento_espacial(**kwargs):
    if 'alexis' in kwargs and kwargs['alexis'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico de Alexis'
    elif 'alexis' in kwargs:
        return f'{kwargs['alexis']} Alexis!'
    return 'Não tenho certeza quem você é...'


# print(cumprimento_espacial())
# print(cumprimento_espacial(alexis='Python'))
# print(cumprimento_espacial(alexis='Oi'))
# print(cumprimento_espacial(alexis='especial'))

'''
OBS: Nas nossas funções, podemos ter(NESTA ORDEM):
- Parâmetros obrigatorios
- *args
- Paramestros DEFAULT (Não obrigatorios).
- **kwargs
'''


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


# minha_funcao(49, 'Alexis')
# minha_funcao(15, 'Eduarda', 4, 5, 3, solteiro=True)
# minha_funcao(53, 'Cacia', eu='Não', voce='Vai')
# minha_funcao(53, 'Gissela', 9, 4, 3, java=False, python=True)

'''VAMOS ENTENDER O PORQUE DA IMPORTANCIA DE MANTER A ORDEM DOS PARAMETROS DA DECLARAÇÃOO'''
# Função com a ordem correta de parametros:

def mostra_info(a, b, *args, instrutor='Alexis', **kwargs):
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3,)
instrutor = 'Alexis'
kwargs = {'sobrenome': 'Cervantes', 'nome': 'Alexis'}
"""
# print(mostra_info(1, 2, 3, sobrenome='Cervantes', nome='Alexis'))

# DESEMPACOTAR COM **kwargs


def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'


nomes = {'nome': 'Alexis', 'sobrenome': 'Cervantes'}

# JEITO ERRADO:
# print(mostra_nomes(nomes))  # TypeError: mostra_nomes() takes 0 positional arguments but 1 was given
# print(mostra_nomes(nome='Alexis', sobrenome='Cervantes'))  # Imprime normal. Não é o metodo mas otimo

# JEITO CERTO:
# print(mostra_nomes(**nomes))

# NÃO É NESESARIO USAR SEMPRE (*args, **kwargs)


def soma_multiplos_numeros1(a, b, c):
    print(a + b + c)


# Chamando a função no modo tradicional
# soma_multiplos_numeros1(1, 2, 3)

# Seguidamente desempacotamos uma lista/tupla/set/dicionario, sem usar ARGS:
lista = [1, 2, 3]
# soma_multiplos_numeros1(*lista)

tupla = (1, 2, 3)
# soma_multiplos_numeros1(*tupla)

conjunto = {1, 2, 3}
# soma_multiplos_numeros1(*conjunto)

# Para desempacotar dicinarios deve utilizarse ** asterisco. E para não dar erro:
dicionario1 = dict(a=1, b=2, c=3)  # Os nomes das chaves do dicionario devem ser os mesmos dos parametros da função.
# soma_multiplos_numeros1(**dicionario1)

"""Junto com um dicionario desempacotado com **. Podemos passar tambem mais elementos"""


def soma_multiplos_numeros2(a, b, c, **kwargs): # Temos que acrecentar na função o **kwargs para evitar dar erro
    print(a + b + c)


dicionario2 = dict(a=1, b=2, c=3, nome='Alexis')

# soma_multiplos_numeros2(**dicionario2, lang='Python')  # Aceita

print('Olá você está no arquivo **kwargs')