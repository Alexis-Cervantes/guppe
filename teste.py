vendedores = ['Marcus', 'Amanda', 'Ale', 'Karol']
vendas = [15, 10, 20, 30]

# Iteração 01:
for vendedor in vendedores:
    print(vendedor)

print('*****************')

# Iteração 02: RANGE 1:
'''Temos que usar uma lista de indices "tamanho_lista" para que seja iteravel em Range'''
tamanho_lista = len(vendedores)
for i in range(tamanho_lista):
    print(vendedores[i])

print('*****************')

# Iteração 02: RANGE 2:
tamanho_lista = len(vendedores)
for i in range(tamanho_lista):
    print(vendedores[i])
    print(vendas[i])

print('*****************')

# Iteração 03: ENUMERATE:
for i, vendedor in enumerate(vendedores):
    print(vendedor)
    print(vendas[i])

print('*****************')

# Iteração 04: ZIP:
for vendedor, venda in zip(vendedores, vendas):
    print(vendedor)
    print(venda)