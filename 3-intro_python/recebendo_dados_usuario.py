"""
Recebendo Dadps do Usuario

Se digitamos no terminal:
dir() ENTER
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

dir(__builtins__) ENTER
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError',
'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning',
'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError'
, 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning',
'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__',
'__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint',
'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits','delattr',
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr',
'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len',
'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow',
'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

Escolhemos a função "INPUT"

Recebendo dados do usuario:

input(): Thodo dado recebido via input é de tipo string

 Em Python, String é thodo o que este entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;

 Exemplos:
 - Aspas simples -> 'Alexis Cervantes'
 - Aspas duplas -> "Alexis Cervantes"
 - Aspas simples triplas -> '''Alexis Cervantes'''
"""

# Aspas duplas triplas -> """Alexis Cervantes"""
# Entrada de dados
# print('Qual é seu nome')
# nome = input()
# nome = input('Quál seu nome: ')

# Exemplo de print antigo 'python 2.x'
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print moderno 'python 3.x'
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print mais atual 'python 3.7'
# print(f'Seja bem-vindo(a) {nome}')

# print('Qual é seu idade')
# idade = input()

# idade = int(input('Qual seu idade: '))

# Processamento
# Saida de dados

# Exemplo de print antigo 'python 2.x'
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print moderno 'python 3.x'
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print mais atual 'python 3.7'
# print(f'O {nome} tem {idade} anos')
'''
# int(idade) => Cast
Cast é a conversão de um tipo para outro,
'''
# print(f'{nome} nasceu em {2024 - idade} ')

print('Olá, voce está no arquivo Recebendo Dados do usuario...')
