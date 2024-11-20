"""Dunder name e Dunder main"""

'''
* Dunder significa Doble Under
  Dunder Name -> __name__
  Dunder Main -> __main__
Em python são utilizados dunder para criar funções, atributos, propriedades etc, utilizando Double Under para não
gerar conflitos com os nomes desses elementos na programação.

* Linguagem 'C' - Temos uma estrutura da seguinte forma
  int main(){
  
      return 0;
  }
  
* Linguagem 'Java'- Temos uma estrutura da seguinte forma
  public static void main(String[], Args){
  
  }
  
* Em python, se executarmos um modulo python diretamente na linha de comando, internamente o python atribuirá à varia-
vel '__name__' o valor '__main__'; indicando que este módulo é o modulo de execução principal. 
'''

'''mainsignifica PRINCIPAL'''

# Se executamos no terminal (print(dir()) vemos que existen varios metodos 'Dunder'
'''['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
 '__spec__']'''

# from funcoes_com_parametro2 import soma_impares

# print(soma_impares([1, 2, 3, 4, 5, 6]))

'''Exemplo com arquivos externos importados - primeiro.py e segundo.py'''
import primeiro
import segundo