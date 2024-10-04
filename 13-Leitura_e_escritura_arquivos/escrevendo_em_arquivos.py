"""Escrevendo em arquivos"""

'''
OBS 1: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma forma, se abrimos
um arquivo para escrita, não podemos lê-lo, somente escrever nele.  
 OBS 2: Ao abrir um arquivo para escrita, o arquivo é criado no SO
OBS 3: Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parametro, caso contrari teremos um TypeError 
OBS 4: Abrindo um arquivo para escrita em modo 'w', se  o arquivo não existir sera criado, caso ele já exista, o 
anteror será apagado e um novo será criado. Dessa forma thodo o conteudo do arquivo é pedrdido.    
'''
# Exemplo 1: modo 'w' que é abrir o arquivo em modo escrita. Modo padrão é para leitura - open('texto.txt')
# with open('novo.txt', 'w') as arquivo:
#     arquivo.write('Escrever dados em arquivo é muito facil.\n')
#     arquivo.write('Podemos colocar quantas linhas quisermos.\n')
#     arquivo.write('Escrever é a ultima linha.')

# Exemplo 2: modo 'w'. Só que vamos a mudar o texto de entrada
# with open('novo.txt', 'w') as arquivo:
#     arquivo.write('Novos dados.\n')
#     arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
#     arquivo.write('Mas esta é a ultima linha.')

# Exemplo 3: Forma tradicional de escrita em arquivo. Forma não Pytonica
# arquivo = open('mais.txt', 'w')

# arquivo.write('Um texto qualquer.\n')
# arquivo.write('Mais um texto.')

# arquivo.close()

# Exemplo 4: modo 'w'. Só que vamos a mudar o texto de entrada
# with open('geeck.txt', 'w') as arquivo:
#     arquivo.write('Alexis ' * 20)

# Exemplo 5: Recebendo dados de usurios
# with open('frutas.txt', 'w') as arquivo:
#     while True:
#         fruta = input('Informe uma fruta ou digite sair: ')
#         if fruta != 'sair':
#             arquivo.write(fruta)
#             arquivo.write('\n')
#         else:
#             break

print('Ola, vc esta no arquivo escrevendo em arquivos')