import numpy as np
#propriedades de array
array = np.array([1,2,3])
print(array)
print(array.ndim) # quantas dimensoes tem o array
print(array.size) # número de elementos totais
print(len(array)) # número de elementos totais
print(array.shape) # mostra o formato
print(array.dtype) # tipo de cada elemento
print(array.itemsize) # tamanho por item
print(array.nbytes) # bytes gastos pelo array

# criando array com duas dimensoes
array = np.array([[1,2,3],[4,5,6]])
print(array)

#geradores de arrays
array1 = np.zeros(9) # gerar array com 9 posicoes preenchido com 0
array2 = np.ones(3) # vetor de 3 posicoes preenchido com 1
array3 = np.empty(6) # vetor vazios com 6 posicoes
array4 = np.identity(4) # matriz quadrada com número 1 da diagonal principal
print(array4)