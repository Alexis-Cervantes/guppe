"""Sorted()"""

"""
- OBS1: Não confunda, a pesar do nome, com a função do sort() que já estudamos em listas. O sort() só funciona em listas  
- OBS2: Envia sempre uma nova lista com os iteraveis ordenados
- USO: Com qualquer iteravel.
- SERVE: ordenar.
"""
# Exemplo 1:
numeros_lista = [6, 1, 8, 2]
numeros_tupla = (7, 3, 5, 8)
numeros_set = {9, 4, 8, 10}

print(f"lista: {numeros_lista}")
print(sorted(numeros_lista))
print(f' Lista Original: {numeros_lista}')

print(f"Tupla: {numeros_tupla}")
print(sorted(numeros_tupla))
print(f' tupla Original: {numeros_tupla}')

print(f"Set: {numeros_set}")
print(sorted(numeros_set))
print(f' set Original: {numeros_set}')
