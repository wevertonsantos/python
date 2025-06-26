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

# 2 - Crie um função que receba um array de números (int ou float) e retorne sua soma.

def soma(array):
    total = 0
    if type(array) == list:
        for num in array:
            total += num
    return total

array = [1,10,50,3]
print("Soma:",soma(array))