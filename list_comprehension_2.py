"""List comprehension - parte 2"""

'''
- Podemos adicionar estruturas condicionais lógicas
 '''

# Exemplo 1
numeros1 = [1, 2, 3, 4, 5, 6]

pares1 = [numero for numero in numeros1 if numero % 2 == 0]
impares1 = [numero for numero in numeros1 if numero % 2 != 0]

# print(pares1)
# print(impares1)

# Refatorando
# Qualquer numero par modulo de 2 é 0, em Python 0 é FALSE. NOT FALSE = True
pares2 = [numero for numero in numeros1 if not numero % 2]

# Qualquer numero impar modulo de 2 é 1, em Python 1 é True
impares2 = [numero for numero in numeros1 if numero % 2]

# print(pares2)
# print(impares2)

# Exemplo 2
# pega esse numero e multiplica por 2; se esse numero modulo de 2 é igual a 0 (ou seja par), se não divide por 2. Para
# cada numnero em numeros1
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros1]

# print(res)

print('Olá você está no arquivo List Comprenhension - parte 2')