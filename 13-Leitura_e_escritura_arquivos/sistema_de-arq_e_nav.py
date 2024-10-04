"""Sistema de arquivos e navegação """

'''Para fazer uso de maniipulação de arquivos do Sistema Operacional, precisamos importar e fazer uso do modulo "OS"
SO -> Sistema operacional
'''
# Fazendo o import
import os

# getwcd() = pega o current work directory - diretorio de trabalho atual
# Retorna o path (caminho alsoluto)
# print(os.getcwd()) # D:\codando\ahorapy\PycharmProjectsNoteNTM\guppeNTM\13-Leitura_e_escritura_arquivos

# Para mudar o diretorio podemos usar - chdir():
# primera uso
# os.chdir('..')
# print(os.getcwd()) # D:\codando\ahorapy\PycharmProjectsNoteNTM\guppeNTM

# segundo uso
# os.chdir('..')
# print(os.getcwd()) # D:\codando\ahorapy\PycharmProjectsNoteNTM\

# tercer uso
# os.chdir('..')
# print(os.getcwd()) # D:\codando\ahorapy\

# quarto uso
# os.chdir('..')
# print(os.getcwd()) # D:\codando\

# quinto uso: Quado chega na raiz não exite mais niveis
# os.chdir('..')
# print(os.getcwd()) # D:\

# PODEMOS CHECAR SE UM DIRETORIO É ABSOLUTO OU RELATIVO
# Absoluto - isabs = é absoluto?
# print(os.path.isabs('d:\\codando\\ahorapy\\')) # \\ em windows
# print(os.path.isabs('d:/codando/ahorapy/')) # / em linux/mac - tambem roda
# deve retornar true por ser absoluto

# PODEMOS IDENTIFICAR O SISTEMA OPERACIONAL
# print(os.name)  # posix (Linux e Mac), nt(windows)

# PODEMOS TER MAIS INFORMAÇÕES DO SO
# print(os.uname()) # este comando so funciona em linux e não no windows

# ADICIONANDO SUB-DIRETORIOS USANDO CODIGOS PYTHON (join)
# Exemplo: D:\\codando\\ahorapy\\sistema

# print(os.getcwd()) # D:\condando\ahorapy\PycharmProjectsCasa\guppe\13-Leitura_e_escrita_arquivos
# res = os.path.join(os.getcwd(), 'pastaexemplo', 'pasta2')
# os.chdir(res)
# print(os.getcwd()) # D:\condando\ahorapy\PycharmProjectsCasa\guppe\13-Leitura_e_escrita_arquivos\pastaexemplo

'''Veja que o 'os.path.join()' recebe 2 parametros, sendo o 1ero o diretorio atual e o 2do o dire-
torio que sera juntado ao atual'''

# Podemos listar os diretorios
# print(os.listdir()) # Mostra umas lista de arquivos e pastas.

# Vamos contar quantos items tem essa lista - len.
# print(len(os.listdir()))

# Podemos passar um path (rota) para veer quantos elementos tem no diretorio raiz
# print(os.listdir('d:\\')) # print(os.listdir('d://')) tambem funciona com contrabarra //

# Vamos a quantidade de elementos:
# print(len(os.listdir('c:\\')))

# Vamos vizualizar mais detalhes - scandir:
# print(os.scandir('d:\\')) # mostra um itereator, ouseja lista

# Vamos vizualizar mais detalhes - scandir: Porem tratando ela como lista
# print(list(os.scandir('d:\\'))) # mostra um itereator, ouseja lista

# Vamos vizualizar mais detalhes - Se queremos que scane o dirtorio atual tiramos o 'path
# print(list(os.scandir()))

# # vamos colocar o conteudo desse print em uma variavel.Vamos vizualizar mais detalhes com o comando scandir. Se
# queremos que scane o dirtorio atual tiramos o 'path
# arquivos1 = list(os.scandir())
# print(arquivos1)
# print(arquivos1[0].name) # mostra o arquivo pyrhon "bloco_with.py"

# vamos aprender mais nomes comando dir e scabdir:
# scanner = os.scandir() # criando variavel scanner para abertura de trabalhos
# arquivos2 = list(scanner)
# print(arquivos2)
# print(arquivos1[0].name)

# print(arquivos2[0].inode()) # ?
# print(arquivos2[0].is_dir()) # è um diretorio? False
# print(arquivos2[0].is_file()) # È um arquivo? True
# print(arquivos2[0].is_symlink()) # È um link Symbolico? False
# print(arquivos2[0].name) # Nome do arquivo
# print(arquivos2[0].path) # Caminho até o arquivo
# print(arquivos2[0].stat()) # Estatistica
'''OBS: Quando utilizamos a função scandir() nós precisamos fechá-la. Assim quando abrimos um arquivo.'''
# scanner.close()

print("sistema de arquivo e navegação")


