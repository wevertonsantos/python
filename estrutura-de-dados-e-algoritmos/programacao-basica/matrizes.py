import numpy as np

matriz = np.array([
    [2,3,1],
    [4,5,7]
]) #criando uma matriz 2 linhas e 3 colunas
print(matriz)
print(matriz.shape) # verificando o formato da matriz
print(matriz[0]) # retornando apenas primeira linha
print(matriz[1])
print(matriz[0][0]) # linha 0 coluna 0

#percorrendo as linhas
for i in range(matriz.shape[0]):
    print(matriz[i])
    #percorrendo colunas
    for j in range(matriz.shape[1]):
        print(matriz[i][j])