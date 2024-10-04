"""Documentando funções com docstring"""

"""OBS: Podemos ter Acesso da documentação de uma função em python utilizando a propriedade espacial '__doc__' 
Exemplo: SE queremos saber da documentação de 'print' escrevemos em uma consola 'print.__doc__' e veremos informação
 com respeito a essa função"""
# Exemplos:


def diz_oi():
    """Uma função simples que retorna a string Oi"""
    return 'Oi'


# print(diz_oi())
# print(help(diz_oi))
# print(diz_oi.__doc__)

def exponente(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou 'número' a 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão
    :return: Retorna o exponencial de 'número' por 'potência'.
    """
    return numero ** potencia


# Usando: __doc__
# print(exponente.__doc__)
'''Função que retorna por padrão o quadrado de 'número' ou 'número' a 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão
    :return: Retorna o exponencial de 'número' por 'potência'.'''

# Usando: 'help'
# print(help(exponente))
'''exponente(numero, potencia=2)
    Função que retorna por padrão o quadrado de 'número' ou 'número' a 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão
    :return: Retorna o exponencial de 'número' por 'potência'.'''


print('Olá, você está no arquivo docstrings')