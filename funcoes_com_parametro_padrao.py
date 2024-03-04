"""Funções com parametro Padrão - Default Parameters"""

'''Funções onde a passagem de parametro seja OPCIONAL - Não da erro'''
# print('Alexis Cervantes')  # Passo parametro
# print()  # Não passo parametro

'''Funções onde a passagem de parametro seja OBRIGATORIA - Da erro'''


def quadrado(numero):
    return numero ** 2


# print(quadrado(3))  # imprimiu 9 no console
# print(quadrado())  # TypeError


def exponencial1(numero, expoente):
    return numero ** expoente


# print(exponencial1(2, 3))
# print(exponencial1(3, 2))

'''REFATORANDO FUNÇÃO ANTERIOR'''
# Como fazer para que o parametro "expoente" na função exponencial seja "2 - ao quadrado" por PADRÃO


def exponencial2(numero, expoente=2):  # Parametro '2' fica como padrão
    return numero ** expoente


print(exponencial2(3))  # Diante a falta do segundo 'Argumento' fica Implicito o numero '2'. informado na função
print(exponencial2(3, 5))  # Neste caso o Argumento '5' passado é explicito e vai se impor


