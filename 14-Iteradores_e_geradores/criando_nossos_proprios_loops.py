"""
Criando nossa propria versão de Lopps:
"""

# Entendendo o loop for:
# for num in [1, 9,7, 4]:
#     print(num)

# for letra in 'Alexis Cervantes':
#     print(letra)

# Por baixo os panos o Python vai pegar os iteraveis de cada for e vai aplicar em cada um deles a função 'iter()' e
# depois para imprimir eles aplica a função 'netx()' para cada elemento a ser mostrado.
# fecha = iter([1, 9, 7, 4])
# nombre = iter('Alexis Cervantes')

# resultado:
# print(next(fecha))
# print(next(fecha))
# print(next(fecha))
# print(next(fecha))

# print(next(nombre))
# print(next(nombre))
# print(next(nombre))
# print(next(nombre))
# print(next(nombre))
# print(next(nombre))

# Vamos criar o nosso loop: Criando uma função
# def meu_for(iteravel):
#     it = iter(iteravel)
#     while True:
#         try:
#             print(next(it))
#         except StopIteration:
#             break

# Utilizando nossa função Loopiana:
# Passamos um nome:
# meu_for('Alexis Cervantes')

# passamos uma lista:
# numeros = [1, 9, 7, 4]
# meu_for(numeros)

print('criando nossos proprios loops')