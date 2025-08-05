import numpy as np

'''
1 - Crie um array com os números de 0 a 9, utilize somente 1 dimensão.
'''

array = np.arange(10)
print(array)

'''
2.Crie um array com os números de 0 a 9 como o exercício anterior, mas utilize List Compreensions.
'''

array = np.array([i for i in range(0,10)])
print(array)

'''
3.Crie um array com os números de 0 a 8, utilize 2 dimensões, ou seja, com 3 linhas (3x3)
'''

array = np.arange(9).reshape((3,3))
print(array)

'''
4. Crie um array do tipo float, com 10 número de sua escolha, mas utilize 32 bits/4 bytes.
'''

array = np.arange(0,9, dtype='f4')
print(array)

'''
5.Crie um array com os números de 1 a 20, escolhendo o tipo de dado que ocupara
o menor espaço da memoria. Em seguida imprima o quanto ele ocupou em bytes.
'''

array = np.arange(1,21,dtype=np.int8)
print(array)
print(array.nbytes)

'''
6.Crie uma matriz 2x2 e imprima o primeiro elemento da primeira linha, e o último
elemento da última linha.
'''

array = np.arange(4).reshape(2,2)
print(array)
print(array[0,0])
print(array[1,1])