"""Introdução ao modulo unittest"""
''''unittest = testes unitario
- Testes é a forma de testar unidades individuais de codigo fonte
- Unidades individuaispodem ser: funções, métodos, classes, modulos etc
OBS: Testes unitario não é especifico da linguagem Python.
- Para criar nossos testes, criamos classes que herdam do unittest.TestCase, e a partor de então ganhamos todos os 
- Assertions, presentes no módulo.
- Para rodar todos os testes utilizamos os unittest.main()
-TestCase -> Casos te teste para sua unidade
CONHECENDO OS ASSERTIONS
MÉTODO                      CHECA 
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)

'''
# Exemplo 1: Utilizando a aabordagem TDD
