"""
Teste de memoria com Generators
"""
#
# Função usando lista:449MB de memoria
# def fib_lista(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a+b
#     return nums

# teste: usando listas: O consumo de memoria é muito alto
# for n in fib_lista(100):
#     print(n)

# Função usando Geradores: 3MB de memoria
# def fib_gen(max):
#     a, b, contador  = 0, 1, 0
#     while contador < max:
#         a, b = b, a+b
#         yield a
#         contador += 1

# Teste 2: Geradores: Geradores se reduze o consumo de memoria
# for n in fib_gen(10):
#     print(n)

print('teste memoria com generators')


