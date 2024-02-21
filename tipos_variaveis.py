"""TIPOS DE VARIAVEIS"""

'''Tipo Númerico - int'''
num = 1_000_000
# print(num)

'''Tipo Númerico - float
Tambem conhecido como Real, decimal, casas decimais
OBS: O separdor de casas decimais na programação é o ponto não a virgula.
'''
# Errado do ponto de vista do float, mas gera uma dupla
valor1 = 1, 44
# print(valor1)
# print(type(valor1))

# Certo do ponto de vista do float
valor2 = 1.44
# print(valor2)
# print(type(valor2))

# É possivel fazer dupla atribuição:
valor3, valor4 = 1, 44
# print(valor3)
# print(type(valor3))

# print(valor4)
# print(type(valor4))

'''Podemos convertir um float para int
   OBS: Ao convertir um float para int perdemos presição 
'''
res = int(valor2)
# print(res)
# print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j

'''Tipo Booleano
Tem 02 constantes: Verdadeiro e Falso.
True -> Verdadeiro
False -> Falso
'''
ativo = True  # ou False
# print(ativo)

'''Operações Basicas dos tipos booleanos'''
'''Negação (not):
   Fazendo a negação o resultado se for verdadeiro sera Falso e se for falso sera verdadeiro
'''
# print(not ativo)
logado = False

'''OU (or):
Operação binaria que depende de dois valores. Ou um Ou outro devem ser verdadeiros
 - True or True => True
 - True or False => True
 - False or True => True
 - False or False => False
'''
# print(ativo or logado)

# E (and):
'''
Tambem é uma opração binaria. Ou seja, tambem depende de 02 valores.
Ambos os valores deven ser verdadeiros
 - True or True => True
 - True or False => False
 - False or True => False
 - False or False => False
'''
'''Tipo String'''
"""Em Pyton um dado é considerado uma string sempre que:
 - Estiver entre aspas simples =>  'aspas simples', '123', 'a', 'True', '43.5'
 - Estiver entre aspas duplas =>  "aspas simples", "123", "a", "True", "43.5"
 - Estiver entre aspas simples triplas =>  '''aspas simples''', '''123''', '''a''', '''True''', '''43.5'''
"""
# - Estiver entre aspas duplas triplas =>  """aspas simples""", """123""", """a""", """True""", """43.5"""

"""Pulando linnhas nos prints que imprimem uma strig"""
nome1 = 'Alexis Cervantes'
# print(nome1, type(nome1))

nome2 = 'Eaduarda \nCervantes'
# print(nome2, type(nome2))

nome3 = """Rita 
de Cacia"""
# print(nome3, type(nome3))

'''Algumas funções o/ou metodos na manipulação de String'''
# MAIUSCULOS
# print(nome1.upper())

# minusculos
# print(nome1.lower())

# Transforma em uma listas de strings
# print(nome1.split())

'''Slice de strings'''
# print(nome1[0:6])
# print(nome1[7:16])
# print(nome1.split()[0])
# print(nome1.split()[1])
'''[::-1] => Começe do ultimo elemento, va até o ultimo e inverta'''
# print(nome1[::-1])
# Substituindo uma letra por outra:
# print(nome1.replace('a', 'c'))

texto = 'socorram me subino onibus em marrocos'  # PALINDROMO
# print(texto)
# print(texto[::-1])

print('Olá, voce está no arquivo Tipo Varievel...')
