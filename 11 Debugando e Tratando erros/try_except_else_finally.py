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

# Exemplo 5: MAIS COMPLEXO - ERRADO
# def dividir1(a, b):
#     return a / b


# num1 = int(input('Informe o prinmeiro número: '))

# try:  # Tratando entrada incorreta
#     num2 = int(input('Informe o segundo número: '))
# except ValueError:
#     print('O valor precisa ser numerico')

# try:  # Tratando a saida representada pela var 'num2' que não sera vista por ser uma var local
#     print(dividir1(num1, num2))
# except NameError:
#     print('Valor incorreto')

# Exemplo 6: MAIS COMPLEXO - CORRETO - Mais profissional
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!
# def dividir2(a, b):
#     try:
#         return int(a) / int(b)
#     except ValueError:
#         return 'Valor incorreto'
#     except ZeroDivisionError:
#         return 'Não é possivel realizar uma divisão por zero'


# num1 = input('Informe o prinmeiro número: ')
# num2 = input('Informe o segundo número: ')

# print(dividir2(num1, num2))

# Exemplo 7: MAIS COMPLEXO - GENERICO - De forma mais simples e praticas. Utilizando simplemente um 'except: Ele trata
# todos os erros possiveis'


# def dividir3(a, b):
#     try:
#         return int(a) / int(b)
#     except:
#         return 'Valor incorreto'


# num1 = input('Informe o prinmeiro número: ')
# num2 = input('Informe o segundo número: ')

# print(dividir3(num1, num2))

# Exemplo 8: MAIS COMPLEXO - SEMI-GENERICO - De forma mais simples e praticas. Utilizando simplemente um 'except: Ele trata
# todos os erros possiveis'


# def dividir4(a, b):
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Ocorreu um problema: {err}'


# num1 = input('Informe o prinmeiro número: ')
# num2 = input('Informe o segundo número: ')

# print(dividir4(num1, num2))

print('Olá você esta no arquivo try_except_else_finally')
