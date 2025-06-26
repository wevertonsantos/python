'''
1 - Crie uma função chamada “e_negativo” que receba um número, retorna um booleano “True” se o número for negativo, caso contrário retorna “False”.
'''

def e_negativo(num):
 if num < 0:
  return True
 else:
  return False
 
print(e_negativo(-1))
print(e_negativo(0))