"""Bloco With"""

'''
Passos para trabalhar com arquivos:
1.-Abrimos o arquivo
2.-Manipulamos o arquivo
3.-Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechadosapós o block with
'''
# O block With: Ele abre e fecha automaticamente o arquivo para evitar de utilizar 'open/read/close'
# with open('texto.txt') as arquivo:  # com open('texto.txt') coloque um apelido 'arquivo'
#   print(arquivo.readlines())  # imprima o trabalho. Depois de thoda essa interação o arquivo será FECHADO
   # print(arquivo.closed)  # Vamos forjar e fechar ele. Mostra False
# Verificando se o arquivo esta fechado:
# print(arquivo.read())  # ACUSA: ValueError: I/O operation on closed file.

# Fechando o arquivo:
# print(arquivo.closed)  # Mostra true

print('Olá esta no arquivo block with')
