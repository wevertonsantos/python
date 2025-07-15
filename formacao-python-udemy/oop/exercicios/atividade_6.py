'''
6 - Cria uma classe que represente um número negativo, 
use propriedades (@property)  para controlar o valor guardado pela classe, 
sem deixar que ele fique positivo (0 pode). Além disso crie alguns operadores 
para comparação e de subtração. Cuide para que nenhum valor positivo surja.
'''

class NumeroNegativo:
  def __init__(self, numero):
    self.__numero =0
    self.numero = numero 
  @property
  def numero(self):
    return self.__numero
  @numero.setter
  def numero(self, value):
    if value <= 0:
      self.__numero = value
  def __lt__(self, outro):
    return self.__numero < outro.__numero
  def __gt__(self,outro):
    return self.numero > outro.__numero
  def __sub__(self, outro):
    sub = self.__numero - outro.__numero
    if sub > 0:
      sub = 0
    return sub

num1 = NumeroNegativo(-10)
num2 = NumeroNegativo(-20)
num3 = NumeroNegativo(10)

print(num1.numero, num2.numero, num3.numero)
print(num1 > num2)
print(num1 - num2)
