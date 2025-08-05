import numpy
'''
12.Crie uma função que divida um array em N pedaços, mas mantenha so o valor
absolutos dos valores deste array.
'''

def divide_abs(arr,n):
  arr = numpy.array_split(arr,n)
  arr = numpy.abs(arr)
  return arr

array1 = numpy.array([1,2,3,-4,5,-7])
print(divide_abs(array1,2))

'''
13.Crie uma função que receba um array e retorne quantos números positivos ela
contêm
'''
def retorno_positivo(arr):
  return numpy.where(arr > 0)[0].size

array = numpy.array([2,3,4,5,0])
print(retorno_positivo(array))

'''
14.Crie uma função que receba uma matriz e retorne os índices dos números que
são divisíveis por 3.
'''

def divisiveis_por_3(arr):
  return numpy.where(arr % 3 == 0)[0]

array = numpy.array([4,5,6,7,8,9])
print(divisiveis_por_3(array))

# 15.Crie uma função que diga se um array possui números negativos

import numpy

def tem_negativo(arr):
  return numpy.any(arr <0)

array = numpy.array([4,-5,6,7,8])
print(tem_negativo(array))

# 16.Crie uma função que remova os números negativos de uma array.

import numpy
def tira_negativo(arr):
  filter = arr >=0
  return arr[filter]

array = numpy.array([1,-5,5,4,3,-2,-1])
print(tira_negativo(array))

# 17.Crie uma função que receba um número inicial e final, e uma array. 
# A função deve retornar uma nova array somente com os números 
# dentro deste intervalo.

import numpy

def remove_valores(arr, inicial, final):
  filter = (arr >= inicial) & (arr <= final)
  return arr[filter]

array = numpy.array([i for i in range(-10,11)])
print(array)
print(remove_valores(array,0,7))

# 18.Crie uma função que ordene uma matriz e remova todos os números impares.

import numpy

def ordena_pares(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return arr[filter]

array = numpy.random.randint(0,10,(100))  
print(ordena_pares(array))

# 19.Realize o mesmo exercício anterior, mas remova valores duplicados.

import numpy

def ordena_pares_unicos(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return numpy.unique( arr[filter])

array = numpy.random.randint(0,10,(100))  
print(ordena_pares_unicos(array))