"""Levantando os proprios erros com raise"""

'''
- lança excepções
- Não é uma função, é uma palavra reservada assim como def ou qualquer outra em Pyhon
- Foi pensando para criar as nossas proprias excepções e mensagens de erro.
- O raise, assim como return encerra a função. Nada após o raise é executado 
- Forma geral de utilização: 
raise TipoDoErro ('Mensagem de Erro)

'''
# Exemplo 1:


# def colore(texto, cor):
#     if type(texto) is not str:
#         raise TypeError('Texto precisa ser uma string')
#     if type(cor) is not str:
#         raise TypeError('Cor precisa ser uma string')
#     print(f'O texto {texto} será impreso na cor {cor}')


# colore('Alexis', 'Azul')  # Saida correta
# colore('Cacia', 4)  # saida incorreta

# Exemplo 2: Refatorando o exemplo anterior


# def colores(texto, cor):
#     cores = ('verde', 'amarelo', 'azul', 'branco')
#     if type(texto) is not str:
#         raise TypeError('Texto precisa ser uma string')
#     if type(cor) is not str:
#         raise TypeError('Cor precisa ser uma string')
#     if cor not in cores:
#         raise ValueError(f'A cor precisa ser uma entre cores')
#         # print('Thodo que está depois do raise é ignorado')  # Ignorado
#     print(f'O texto {texto} será impreso na cor {cor}')


# colores('Alexis', 'azul')

print('Olá você está no arquivo raise...')