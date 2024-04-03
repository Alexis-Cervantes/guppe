"""Try / Except / Else / Finally"""

'''
Dica de quando e onde tratar codigo:
- TODA ENTRADA (DE USUARIO) DEVE SER TRATADA!
- OBS: A função do USUARIO é destruir seu sistama
- o uso de try e Except são usados muito comumente
- O uso de Else e Finally não são usados comumente
Finally: È usado geralmente para fechar ou deslocar recursos 
'''
# Exemplo 1:
# num = int(input('Informe um numero: '))
# print(f'Você digitou {num}')

# Exemplo 2: Tratando essa entrada
# num= 0  # Criamos aqui a var para que não de erro
# try:
#     num = int(input('Informe um numero: '))  # var local
# except ValueError:
#     print('Valor Incorreto')
#
# print(f'Você digitou {num}')  # Se try não consegue então não tem acesso a var local 'num'

# Exemplo 3: Uso de 'Else'
# try:
#     num = int(input('Informe um numero: '))
# except ValueError:  # Ele entra em ação se digitamos um dado incorreto
#     print('Valor Incorreto')
# else:  # Ele é executado somente se não ocorrer o erro.
#     print(f'Você digitou: {num}')


# Exemplo 4: Uso d 'Finally'
# try:
#     num = int(input('Informe um numero: '))
# except ValueError:  # Ele entra em ação se digitamos um dado incorreto
#     print('Valor Incorreto')
# else:  # Ele é executado somente se não ocorrer o erro.
#     print(f'Você digitou: {num}')
# finally:  # É sempre executado. Independente se houve exceção ou não
#     print('Executando o Finally')

# Exemplo 5: MAIS COMPLEXO
def dividir(a, b):
    return a / b


num1 = int(input('Informe o prinmeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

