"""LOOP FOR"""

"""Em C ou Java - Estrutura
for(int i = 0, i < 10, i++){
    //execução do loop
}
"""

"""Em Python - Estrutura
for item in iteravel:
    //execução do loop
"""

"""Exemplo de iteraveis:
   - String: 
     nome = 'Alexis Cervantes'
   - Listas:
     lista = [10, 20, 30, 40]
   - Range:
     numeros = range(1, 10)
"""
nome = "Alexis Cervantes"
lista = [10, 20, 30, 40]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1: Iterando uma String
# for letra in nome:
#     print(letra, end='-')
# print()

# Exemplo de for 2: Iterando uma Lista
# for item in lista:
#     print(item, end='*')
# print()

# Exemplo de for 3: Iterando um Range
# for numero in range(1, 10):
#     print(numero, end='/')

# Acessando ao indice de cada item ou elemento: 'ENUMERATE 1'
# for indice, letra in enumerate(nome):
#     print(nome[indice])

# print()

# Acessando ao indice de cada item ou elemento: 'ENUMERATE 2'
# for indice, letra in enumerate(nome):
#     print(letra)

# print()

# Acessando ao indice de cada item ou elemento: 'ENUMERATE 3'
# OBS: Quando não precisamos de uma valor, podemos descarta-lo utilziando um underline (_)
# for _, letra in enumerate(nome):
#     print(letra)

# print()

# Acessando ao indice de cada item ou elemento: 'ENUMERATE 4'
# Utilizando so a variavel valor podemos aceesar aos (indice, letras)
# for valor in enumerate(nome):
#     print(valor)

# print()

# Acessando ao indice de cada item ou elemento: 'ENUMERATE 4.1'
# for valor in enumerate(nome):
#     print(valor[0], "-", valor[1])

"""Exercicios"""
# qtd = int(input('Quantas veses este lopp deve rodar: '))
# soma = 0

# for n in range(1, qtd+1):
#     num = int(input(f"Infome o {n}/{qtd} valor: "))
#     soma = soma + num
# print(f"A soma é: {soma}")

"""Exercicios"""
# Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Origiinal = U+1F60D
# Modificado = U0001F60D
emoji = "U0001F60D"

# for _ in range(3):
#     for num in range(1, 11):
#         print("\U0001F60D" * num)

print('Olá, voce está no arquivo Loop For...')


