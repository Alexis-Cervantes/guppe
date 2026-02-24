""""TIPO FLOAT (real, decimal
Casas decimales: INGLES - O separador é o PONTO e não a VIRGOLA
"""
# ERRADO
valor1 = 1,44
print(valor1)
# R: (1,44) - POR LA VIRGULA ASUME QUE É UMA TUPLA
print(type(valor1)) # VAMOS VERIFICAR QUAL É O TIPO

# CERTO
valor2 = 1.44
print(valor2)
# R: 1.44 - PONTO É O PADRÃO
print(type(valor2)) # VAMOS VERIFICAR QUE É UM NUMERO FLOAT CORRETO

# É POSSIVEL FZER DUPLA ATRIBUIÇÃO
valor1, valor2 = 1,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# PODEMOS CONVERTIR UM FLOAT PARA INTEIRO. PERDEMOS PRECISÃO, PORQUE SE ARREDONDA PARA INTEIRO
res = int(valor1)
print(res)
print(type(res))

# NUMEROS COMPLEXOS
vaiavel = 5j


