"""Bloco Try/Except"""

'''
- Serve para tratar erros que podem acontecer em nosso codigo. Previnindo assim para de funcionar e o ususrio receva
mensagens de erro inesperado.  
- A forma geral mais simples:
try:
    //execução problematica
except:
    //O que deve ser feito em caso de problema
'''
# Exemplo 1: Tratando um erro genérico
# try:  # tente executar a função alexis()
#     alexis()
# except:  # Em casos que, caso vc encontre erro, imprima a mensagem de erro.
#     print('Deu um problema')


# Exemplo 2: Tratando um erro genérico.
# try:
#     len()
# except:  # Em casos que, caso vc encontre erro, imprima a mensagem de erro.
#     print('Deu um problema')

'''
OBS: Tratar o erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
especifica. 
'''
# Exemplo 3:
# try:
#     alexis()
# except NameError:  # Especifico para esse caso.
#     print('Você está utilizando uma função inexistente')

# Exemplo 4:
# try:
#     len(5)
# # except NameError:  # Da erro aqui porque a exception especifica não corresponde ao tipo de tratamento.
# except TypeError:  # Esse exception esta correto para esse tipo de tratamento.
#     print('Deu um problema')

# Exemplo 5:
# try:
#     len(5)
# except TypeError as err:  # podemos guardar essa mensagens no log do sistema. banco de dados.
#     print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 6:
# try:
#     # len(5)  # TypeErro
#     # alexis()  # NameErro
#     print('alexis'[19])  # Except
# except NameError as erra:
#     print(f'Deu NameErro: {erra}')
# except TypeError as errb:
#     print(f'Deu TypeErro: {errb}')
# except:  # Forma generica. Sem especificar
#     print('Deu um erro diferente')

# Exemplo 7:


# def pega_valor(dicionario, chave):
#     return dicionario[chave]


# dic = {'nome': 'Alexis'}
# print(pega_valor(dic, 'nome'))

# Exemplo 8: Tratando o erro


# def pega_valores(dicionario, chave):
#     try:
#         return dicionario[chave]
#     except KeyError:
#         return None

# dic = {'nome': 'Alexis'}
# print(pega_valores(dic, 'game'))  # Game como entrada esta errado e sera tratado.

# Exemplo 9: Tratando masi de 1 erro


# def pega_valores(dicionario, chave):
#     try:
#         return dicionario[chave]
#     except KeyError:
#         return None
#     except TypeError:
#         return None


# dic = {'nome': 'Alexis'}
# print(pega_valores(7, 'game'))  # O '7' como entrada esta errado e será tratado

print('Olá você está no arquivo try/except')