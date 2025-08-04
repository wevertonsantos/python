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