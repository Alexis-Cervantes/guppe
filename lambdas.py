"""Utilizando Lambdas"""

'''
- São Funções Anonimas/sem nome
- Funções em Python:
  def soma(a, b):
      return a + b 
'''
# Exemplo 1:


def funcao(x):
    return 3 * x + 1

# print(funcao(4))

# Exemplo 2: Refatorando a função anterior com funções Lambda
calc = lambda x: 3 * x + 1
# print(calc(4))

# Podemos ter expressões lambdas com multiples entradas. O strip() elimina espaços em branco. O Title capitaliza 1ra le
# tra
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# print(nome_completo('alexis', 'CERVANTES'))
# print(nome_completo('CACIA', 'morais'))

# Em funções Pythom podemos ter nenhuma ou varias entradas. Em lambda tambem
amar = lambda: 'La vida es un carnaval'
uma = lambda y: 3 * y + 1
duas = lambda a, b: (a * b) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# print(amar())
# print(uma(6))
# print(duas(5, 7))
# print(tres(3, 6, 9))

# Outros Exemplos
# Split(' ') separa uma string por espaçõs em branco
# lower() Transforma as letras em minusculo
nomes = ['Alexis Cervantes', 'Rita de Cacia', 'Eduarda Cervantes', 'Ismael Baltazar Cervantes', 'Olga C. Negreiros',
         'H. M Cervantes', 'Gissela Beatriz Cervantes Negreiros']
# print(nomes)
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# print(nomes)

'''
Função Quadrática
f(x) = a * x ** 2 + b * x + c
'''
# Definindo a função:
def definindo_funcao_quadratica(a,  b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = definindo_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))