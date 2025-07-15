'''
7 - Crie uma função  que diga se um objeto é um primitivo 
do Python, informando que é sempre passado valor Ex: [int, float, str, bool], 
ou se é um objeto passado por referência
'''

def testa_objeto(obj):
  if isinstance(obj, (int, float, str, bool)):
    print("Objeto por valor")
  else:
    print("Objeto por referência")

class Objeto:
  def __init__(self):
    pass

obj = Objeto()
valor = 3

testa_objeto(obj)
testa_objeto(valor)
