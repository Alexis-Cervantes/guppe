"""Funções com Retorno"""

"""OBS: Em Pythom unso uma função não retorna nenhum valor o retorno é NONE"""
# Exemplo função


def quadrado_de_7():
    print(7 * 7)


# verificamos que esa função não retona nada - so imprime:
ret = quadrado_de_7()

print(f"retorno: {ret}")


# Refatorando a função: para que ele retorne o valor
"""OBS: Não presisamos nesesariamente criar uma variavel para recever o retorno de uma função. Podemos pasdar a 
execução da função para outras funções ou para o print"""


def quadrado_de_8():
    return 8 * 8


# ccriamos a variavelpara recevero o retorno da função
ret = quadrado_de_8()

print(f"retorno: {quadrado_de_8()}")
