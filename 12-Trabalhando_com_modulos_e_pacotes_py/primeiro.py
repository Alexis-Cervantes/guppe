def funcao1():
    print('Alexis Cervantes - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py esta sendo executado diretamente.')
else:
    print(f'primeiro.py foi importado. {__name__}')

