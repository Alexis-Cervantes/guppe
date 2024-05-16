"""Seek e Cursor"""

'''
seek() --> É utilizada para mover o cusor pelo arquivo. Ela revece um parametro onde indica onde queremos colocar o 
cursor  
'''
arquivo = open('texto.txt')

print(arquivo.read())

# Movivmentando o cursor com a função seek()
arquivo.seek(0)

print(arquivo.read())