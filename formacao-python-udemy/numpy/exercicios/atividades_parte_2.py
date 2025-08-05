import numpy as np
'''
7.Gere uma array 3x3 com números inteiros aleatórios entre 5 e 20. Então imprima a
primeira coluna e última linha
'''

array = np.random.randint(5,21,(3,3))
print(array,end='\n\n')
print(array[:,0],end='\n\n')
print(array[2,:],end='\n\n')

'''
8. Crie uma matriz 3x3 aleatória. Percorra linha por linha com um laço
e imprima a soma de cada linha.
'''
array = np.random.randint(1,21,(3,3))
print(array,end='\n\n')

for linha in array:
    print(np.sum(linha),end='\n\n')

'''
9.Gere um array com os valores pares de 0 a 100 com list comprehension.
'''
array = np.array([i for i in range(0,101) if i % 2 == 0])
print(array,end='\n\n')

'''
10.Crie uma array 4x9 com valores quaisquer, redimensione para as dimensões 36, e
6x6
'''
array = np.arange(1,37).reshape(4,9)
print(array,end='\n\n')
array = array.reshape(36)
print(array,end='\n\n')
array = array.reshape(6,6)
print(array,end='\n\n')

'''
11. Crie uma função que receba três arrays de mesmo formato, então retorne elas
concatenadas em uma só. Se as matrizes recebidas não forem do mesmo formato
gere uma exceção.
'''

def combina(arr1,arr2,arr3):
  if arr1.shape != arr2.shape or arr1.shape != arr3.shape:
    raise Exception("Formatos são diferentes")
  
  return np.concatenate((arr1,arr2,arr3))

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.array([7,8,9])

print(combina(array1,array2,array3))