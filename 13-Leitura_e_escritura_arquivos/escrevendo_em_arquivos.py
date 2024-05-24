"""Escrevendo em arquivos"""

'''
OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma forma, se abrimos
um arquivo para escrita, não podemos lê-lo, somente escrever nele.  


'''
# Exemplo de escrita: modo 'w'
with open('novo.txt', 'w') as arquivo:
    arquivo.write('escrever dados em arquivo é muito facil')
    arquivo.write('')