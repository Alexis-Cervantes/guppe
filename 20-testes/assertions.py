""""Assertions (afirmações/checagens/questionamentos)"""

'''Em Python utilizamos a palavra reservada 'assert', para realizar simples afirmações utilizadas nos testes

Utilizamos 'assert' em uma expressão que queremos checar se é valido ou não.
Se a epressão foi Verdadeira, retorna None e caso seja falsa levanta um Erro do tipo AssertionError

OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada/

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamemte nos 
testes.   
'''
# Exemplo 1:
# def soma_numeros_positivos(a, b):
#     assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
#     return a + b

# ret = soma_numeros_positivos(2, 4) #6
# ret = soma_numeros_positivos(2, 4) #AssertionError

# print(ret)

# Exemplo 2:
# def comer_fast_food(comida):
#     assert comida in[
#         'pizza',
#         'sorvete',
#         'doces',
#         'batata fritas',
#         'cachorro quente'
#     ], 'A comida precias ser fast food'
#     return f'Eu estou comendo {comida}'

# comida = input('Informa a comida: ')
# print(comer_fast_food(comida))

'''ALERTA / CUIDADO ao usar o 'assert'. Se um programa Python for executada com o parametro -O. nehum assertion será 
validade. Ou seja todas as validações já eram
'''
# Exemplo 3:
# def faca_algo_ruim(usuario):
#     assert usuario.eh_admin, 'somente administradores podem fazer coisas ruins'
#     destroi_tudo_o_sistema()
#     return 'Adeus'

print('assertions')