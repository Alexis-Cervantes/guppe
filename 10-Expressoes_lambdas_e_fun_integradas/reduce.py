from functools import reduce
"""Reduce"""

'''OBS: A partir do Pythom 3+ a funçãon reduce() não é mais uma função integrada (built-in). Isto é; temos que importar
e utilizar esta função a partoir do modulo "functools" 
 Guido van Rossum: Recomenda utiliza-la se foi preciso; porem só um lopp for é o suficiente
ENTEDENDO O REDUCE():
- Imagina que você tem uma coleção de dados:
  
  dados = [a1, a2, a3, a4 ... an]
  
- Você tem uma função que receve 02 parametros:
  def funcao(x, y):
      :return x * y
- Assim como map() e filter(); reduce() tambem receve 02 parametros: (FUNÇÃO, ITERAVEL)

- Neste caso: 
  reduce(funcao, dados)

- Reduce() funciona da seguinte maneira:
  PASSO 1: res1 = f(a1, a2): Aplica a função nos 02 primeiros elementos da colecão e guarda o resultado.
  PASSO 2: res2 = f(res1, a3): Aplica a função passando o resultado do PASSO 1 + o 3ro. elemento (a3) e guarda o res.
  PASSO 3: res3 = f(res2, a4): Aplica a função passando o resultado do PASSO 2 + o 4tO. elemento (a4) e guarda o res.
  .
  .
  .
  PASSO n: resn = f((resn-1), an): Aplica a função passando o resultado do PASSO (n-1) + o n elemento (an) e guarda o 
  res.

- OU SEJA: Em cada PASSO ele aplica a função passando como primeiro argumento o resultado da aplicação anterior. No 
final reeduce() irá retornar o resultado FINAL  

- ALTERNATIVAMENTE: poderiamos ver a função reduce() como:
  funcao(funcao(funcao(a1, a2), a3), a4) 
'''
# Exemplo 1: Utilizando reduce() para multiplica os elementos de uma lista
# from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# lembrando que a meljor função que podemos usar é "lambda"
multi = lambda x, y: x * y
res1 = reduce(multi, dados)
# print(res1)

# Exemplo 2: Utilizando um Loop normal
res2 = 1
for n in dados:
    res2 *= n

# print(res2)

print('Olá você está no arquivo reduce()')
