"""Sistema de arquivo - Manipulação"""
'''Importando os'''
import os
import tempfile

# COMO DESCOBRIR SE UMA ARQUIVO OU DIRETORIO EXISTE
# ARQUIVO:
# print(os.path.exists('arquivo.txt')) # retornar FALSE porque não existe esse arquivo
# print(os.path.exists('frutas.txt')) # retornar TRUE porque SI existe esse arquivo

'''DIRETORIO (PASTA)'''
# PATH RELATIVOS:
# print(os.path.exists('diretorioExemplo')) # retornar TRUE porque existe diretorio
# print(os.path.exists('diretorioExemplo/subdiretorioExemplo')) # retornar TRUE porque SI existe subdiretorio
# print(os.path.exists('outro')) # retornar TRUE porque não existe esse diretorio

'''DIRETORIO (PASTA)'''
# PATH ABSOLUTOS:
# print(os.path.exists('D:/codando/ahorapy/PycharmProjectsNoteNTM/guppeNTM/13-Leitura_e_escritura_arquivos')) # True
# print(os.path.exists('D:/codando/ahorapy/guppeNTM')) # retornar FALSE porque NO existe subdiretorio 'guppe' dentro de
# 'ahorapy'

'''CRIANDO AEQUUIVOS:'''
# FORMA 1:
# open('arquivo-teste.txt', 'w').close()

'''FORMA 2:'''
# open('arquivo-teste2.txt', 'a').close()

'''FORMA 3:'''
# with open('arquivo-teste3.txt', 'w') as arquivo:
#     pass

'''FORMA 4: A MELHOR FORMA DE CRIAR -  arquivos'''
# os.mknod('arquivo-teste4.txt') # Em Windows não funciona. AttributeError: module 'os' has no attribute 'mknod'

# FORMA 5: A MELHOR FORMA DE CRIAR - arquivos
# os.mknod('D:/codando/ahorapy/PycharmProjectsNoteNTM/arquivo-teste5.txt') # em windows não funciona

'''FORMA 6: A MELHOR FORMA DE CRIAR - Diretorios'''
# Path Relativos
# os.mkdir('templates1')
# OBS: A função 'mkdir' cria diretorio se este não existir. Caso ecista temo FileExistError

# Path Absoluto:
# os.mkdir('D:/codando/ahorapy/PycharmProjectsCasa/guppe/templates3')
# OBS: Se não tivermos permissão para criar o diretorio teremos um PermissionError

'''CRIANDO MULTI DIRETORIOS DE VEZ'''
# Criando arvore de diretorios:
# os.makedirs('dir1/subdir2de1/subdir3de2')
# OBS: Se ja existir todos vai acusar um FileExistsError. Se não estiver pelo menos um não da erro

# Tratando erros:
# os.makedirs('dir2/dir3/dir4', exist_ok=True) # Cria esses diretorios. Se não existir ignora

'''RENOMEANDO ARQUIVOS E DIRETORIOS'''
# DIRETORIOS
# os.rename('dir1', 'dir74')

# os.rename('dir74/subdir2de1', 'dir74')
# OBS: Se o diretorio mudou de nome então não existe. Teremos um FileNotFoundError
# OBS: Se o diretorio que quremos renomear não estiver vazio teremos um OSErro

# ARQUIVOS:
# os.rename('dir2/dir3/arquivo1.txt', 'dir2/dir3/arquivox.txt')

# Exemplo: Mudando nome de um arquivo especifico:
# os.rename('frutas.txt', 'melones.txt')

'''REMOVENDO ARQUIVOS'''
# ADVERTENCIA: Tome cuidado com os documentos que apaga. Eles não vão para LIXEIRA
# os.remove('novo.txt')
# OBS: Se estiver no windows e o arquivo que quiser deletar estiver em uso acusara um erro
# OBS: Caso o arquuivo não exista teremos um FileNotFoundError
# OBS: Se vc informar um diretorio ao ao inves de um aarquivo teremos um IsADirectoryError

'''REMOVENDO DIRETORIOS VAZIOS'''
# os.rmdir('templates')
# OBS: Se o diretorio tiver qualquer conteúdo teremos um OSError

# os.rmdir('templates2')
# OBS: Se o diretorio não exitir teremos um FileNotFoundError

'''REMOVENDO UMA ARVORE DE DIRETORIOS'''
# para isso criamos 1 diretorio com 2 arquuivos: dir/arq1.txt arq2.txt
# for arquivo in os.scandir('dir'):
#     print(f'- {arquivo.name}')
#     if arquivo.is_file():
#         os.remove(arquivo.path)

# Podemos remover uma arvore de diretorios vazios
# os.removedirs('dir3/dir4')
# OBS: Se algun dos diretorios contiver arquivos ou outros diretorios, o processo para

'''DIRECIONANDO ARQUIVOS E DIRETORIOS PARA LIXEIRA - Biblioteca Send2trash'''
# Importando biblioteca
# from send2trash import send2trash

# os.remove('cesta2') # Não vai para lixeira. É deletada imediatamente
'''VS'''
# send2trash('melones.txt') # Vai para lixeira. Pode ser restaurado
# OBS: Se o arquivo não existir dra um ESError

'''TRABALHANDO COM ARQUIVOS E DIRETORIOS TEMPOSRARIOS'''
# para isto temeos que importar biblioteca 'temfile
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivos_temporarios.txt'), 'w') as arquivo:
        arquivo.write('Alexis Cervantes\n')
    input()
# OBS: Estamos criando um arquivo temporario, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um
# texto. No final usamos só o input() so para mantermos os arquivo temporarios 'vivos' dentro dos blocos with.





