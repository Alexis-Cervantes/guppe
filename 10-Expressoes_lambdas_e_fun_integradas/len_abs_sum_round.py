"""Len, Abs, Sum e Round"""

'''len() -> Retorna o tamanho. Numero de itens de um iteravel '''
# Revisando len():
# print(len('Alexis Cervantes'))
# print(len([1, 2, 3, 4, 5]))
# print(len((1, 2, 3, 4, 5)))
# print(len({1, 2, 3, 4, 5}))
# print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
# print(len(range(0, 10)))

# Por debaixo dos panos. Quando utilizamos a função len() o Pythom faz o seguinte:
# print('Alexis Cervantes'.__len__())  # Dunder len. Em Orientação Objetos revisaremos com mais detalhe

'''abs() -> Retorna o valor absoluto de um numero enteiro ou real. De forma básica, seria seu número real sem o sinal'''
# Revisando abs():
# print(abs(-5))
# print(abs(5))
# print(abs(3.14))
# print(abs(-3.14))
# print(abs('alexis'))  # Não existe abs para string

'''sum() -> Recebe como parametro um iteravel, podendo receber um valor incial, e retorna a soma total dos elementos.
incluindo o valor inicial. Valor inicial default é '0'.'''
# Revisando sum():
# print(sum([1, 2, 3, 4, 5]))  # Depois do colchete tem um valor default '0'
# print(sum([1, 2, 3, 4, 5], 5))  # lista + numero
# print(sum([1, 2, 3, 4, 5], -5))  # lista + numero negativo
# print(sum([3.145, 5.678]))  # Lista
# print(sum((1, 2, 3, 4, 5)))  # Tupla
# print(sum({1, 2, 3, 4, 5}))  # Set
# print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))  # Dicionario. especificando valor das chaves

'''round() -> Retorna um número arredondado para "n" digito de precisão após a casa decimal. Se a precisão não for 
informada retorna o inteiro mais próximo da entrada'''
# print(round(10.2))
# print(round(10.5))
# print(round(10.6))
# print(round(1.2121212121, 2))  # o numero 2 segnifica que coloque 2 casas decimais
# print(round(1.21999999, 2))  # se queremos que vire inteiro devemos tirar esse numero 2

print('Olá você está no arquivo len(), abs(), sum(), round()')