from sys import exec_prefix

def reciprocal(n):
    if n == 0:
        raise ZeroDivisionError('No se puede dividir entre cero')
    return 1/n



print(reciprocal(10))
print(reciprocal(0))
