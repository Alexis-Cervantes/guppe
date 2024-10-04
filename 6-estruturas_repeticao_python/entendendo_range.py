"""RANGE"""

'''
 - Precisamos conhecer o loop FOR para usar os ranges
 - Presisamos conhecer o range para trabalhar melhor com loop FOR
'''
# FORMA GERAIS
'''FORMA 1:
range(valor da parada)
OBS: valor_da_parada não inclusive (Inicio padrão '0', e passo de 1 em 1)
'''
# Forma 1:
# for num in range(11):
#     print(num, end='-')

'''FORMA 2:
range(valor_de_inicio, valor da parada)
OBS: valor_da_parada não inclusive (Inicio especificado pelo usuario, e passo de 1 em 1)
'''
print('')
# Forma 2:
# for num in range(1, 11):
#     print(num, end='/')

'''FORMA 3:
range(valor_de_inicio, valor da parada, paso)
OBS: valor_da_parada não inclusive (Inicio especificado pelo usuario, e passo esepcificado pelo usuario)
'''
print('')
# Forma 3:
# for num in range(1, 10, 2):
#     print(num, end='*')

'''FORMA 4: inverso - forma 3
range(valor_de_final, valor da parada, paso)
OBS: valor_da_parada não inclusive (Inicio especificado pelo usuario, e passo esepcificado pelo usuario)
'''
print('')
# Forma 3:
# for num in range(10, 0, -1):
#     print(num, end='*')

# Comparação entre list e Range
# Não podemos imprimir um Range direetamente com o print:
# lista = range(1, 10)
# print(lista)

# Se podemos imprimir uma list(range)) iteravel com o print:
# lista = list(range(1, 10))
# print(lista)


print('Olá, voce está no arquivo Entendeno Range...')