from sys import getsizeof
"""Generators Expression"""
'''
Estudamos:
- Lista Comprehension
- Dictionary Comprehension
- Set Comprehension
Não estudamos:
- Tupla Comprehension... Porque ela se chama GENERATORS
'''
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# Usando 'Any': Vemos que é uma lista Comprehension
# print(any([nome[0] == 'C' for nome in nomes]))  # A saide da True ou False

# Poderiamos ter utiizado GENERATORS:
# print(any(nome[0] == 'C' for nome in nomes))

# Diferença entre Generators e List Comprehension

# Lista Comprenhesion: Ele tem Colchetes
res1 = [nome[0] == 'C' for nome in nomes]
# print(res1)
# print(type(res1))

# Generator: Ele tem parentesis
res2 = (nome[0] == 'C' for nome in nomes)
# print(res2)
# print(type(res2))

'''OBS: Listas Comprehension e Generator fazem a mesams coisa, porém Generators ocupa menos recuersos em memoria. Ou 
 seja ele é mais performatico'''

# Qual e a utilizadade de getsizeof():
# Retorna a quantidade de bytes em memoria do elemento passado como parametro
# from sys import getsizeof
# print(getsizeof('Alexis'))  # mostra quantos a string "Alexis" esta ocupandop em memoria. Quanto maior a string mais
# # espaço ocupa
# print(getsizeof('Cervantes'))
# print(getsizeof(49))
# print(getsizeof(91))
# print(getsizeof(98653214577))
# print(getsizeof(True))

# Gerando uma lista de nuemros com list Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de nuemros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de nuemros com dicionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de nuemros com GENERATORS
gen1 = getsizeof(x * 10 for x in range(1000))

# print(f'Usando List Comprehension gastamos em memoria: {list_comp} bytes')
# print(f'Usando Set Comprehension gastamos em memoria: {set_comp} bytes')
# print(f'Usando Dictionary Comprehension gastamos em memoria: {dict_comp} bytes')
# print(f'Usando GENERATORS EXPRESSION gastamos em memoria: {gen1} bytes')

# POSSO ITERAR NO GENERATOR EXPRESSION
gen2 = (x * 10 for x in range(1000))
print(gen2)
print(type(gen2))

for num in gen2:
    print(num)

    print('Olá')