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

array1 = np.zeros((3,3)) # criando matriz de zeros com 3 linhas e 3 colunas
array2 = np.ones((4,4)) # criando matriz com vários um com 4 linhas e 4 colunas

# geração de array com arange
array1 = np.arange(2,16,2) # de 2 a 15 de 2 em 2
array2 = np.arange(4,16)

array = np.full((4,4),10) # matriz 4,4 preenchida com 10 usando full

array_float = np.random.rand(4,4) # matriz 4,4 com números aleatórios float
array_int = np.random.randint(5,10,(5,5)) #  matriz 5,5 com números aleatórios inteiros de 5 a 9

# list comprehension
array = np.array([i for i in range(0,10)])

#list comprehension matriz
array = np.array([
    [i for i in range(0,3)],
    [i for i in range(3,6)],
    [i for i in range(6,9)]
])