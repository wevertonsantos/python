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

# acessando elementos do array
array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array[2])
print(array[2:4])

# acessando elementos do array de mais dimensões
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array[0]) # primeira linha do array
print(array[0][0]) # pegando primeira linha do array, primeiro elemento
print(array[0,0]) # pegando primeira linha do array, primeiro elemento
print(array[0:2]) # slices de linhas

#iteração em arrays
array = np.array([1,2,3,4])
for i in array:
    print(i)

#iteração em arrays de mais dimensoes
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in array:
    for j in i:
        print(j)

#iteração em arrays de mais dimensoes em coluna
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(array,order='F'):
    print(i)

# modificando array existente
array = np.array([[1,2,3],[5,6,7],[8,9,10]])
print(array)
array[0] = [1,2,4] # passando novos valores na linha
array[1,1:3] = [0,0] # passando novos valores na linha com slice
array[0,0] = 10 # passando novo valor na linha 1 e coluna 1
array[:,2] = [0,0,0] # passando novos valores na terceira coluna do array
print(array)

# adicionando elementos no array
array = np.array([1,2,3,4])
array = np.append(array,[5,6,7,8])
print(array)

# adicionando elementos no array de mais dimensões
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = np.append(array,[[10,11,12]],axis=0) # adicionando uma linha no array
array2 = np.append(array,[[10],[11],[12]],axis=1) # adiciona coluna no array
print(array1)
print(array2)

# inserindo elemento no array
array = np.array([1,2,3])
array = np.insert(array,1,10) # inserindo na posição 1 o valor 10

# inserindo elemento no array com mais dimensoes
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = np.insert(array,3,[10,11,12],axis=0) # inserindo na linha
print(array1)
array2 = np.insert(array,1,[4,5,6],axis=1) # inserindo na segunda coluna elemento 4,5,6
print(array2)

# removendo elementos do array
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = np.delete(array,1,axis=0) # deletando a linha
array2 = np.delete(array,1,axis=1) # deletando a coluna

# copiando array - por referência
array = np.array([1,2,3])
copy_array = array
copy_array[0] = 0
print(array)

# copiando array - por valor
array = np.array([1,2,3])
copy_array = array.copy() # criado outro objeto
copy_array[0] = 0
print(copy_array)

#alterando dimensões
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array = array.reshape(9) # transformando array em um array normal sem dimensões

#transforma um array normal em array com dimensões
array = np.array([i for i in range(0,27)])
print(array)
array1 = array.reshape(3,9) # 3 linhas e 9 colunas
array2 = array.reshape(9,3) # 9 linhas e 3 colunas
array3 = array.reshape(3,3,3) # 3 tabelas com 3 linhas e 3 colunas
print(array3)

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array = array.flatten() # transformando array em um array normal sem dimensões com flatten
print(array)

# operações com array
array1 = np.array([1,2,3])
array2 = np.array([2,4,6])

print(array1 + array2)
print(array1 - array2)
print(array1 / array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 // array2)

#comparação entre arrays
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
print(array1 > array2)
print(array1 == array2)
print(array1 != array2)
print(np.array_equal(array1,array2)) # verificando se array é igual ao outro

#combinação de arrays
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
array12 = np.concatenate((array1,array2),axis=0) # concatenar arrays a partir da linha
print(array12)

#concatenar vetores com mais de uma dimensão
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12 = np.concatenate((array1,array2),axis=1) # concatenar arrays a partir de coluna
print(array12)
array12 = np.concatenate((array1,array2),axis=0) # concatenar arrays a partir da linha
print(array12)

#usando stack
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array12r = np.vstack((array1,array2)) # vai combinar linha por linha
array12c = np.hstack((array1,array2)) # vai combinar coluna por coluna
print(array12r)
print(array12c)

# combinação por linha ou coluna multidimensional
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12r = np.vstack((array1,array2)) # vai combinar linha por linha
array12c = np.hstack((array1,array2)) # vai combinar coluna por coluna
print(array12r)
print(array12c)

#divisão de array
array = np.array([1,2,3,4,5,6])
print(np.split(array,1)) #divide o array em uma vez
print(np.split(array,2)) #divide o array em duas vezes
print(np.split(array,3)) #divide o array em três vezes

#divisão de array com multipla dimensão
array = np.array([[1,2,3,4],[4,5,6,7]])
print(np.split(array,2))

# array_split
array = np.array([1,2,3,4,5,6])
array1 = np.array_split(array,4) # faz divisões conforme passado mesmo não sendo divisão exata

# array_split com array multidimensional
array = np.array([[1,2,3],[4,5,6]])
array1 = np.array_split(array,2)
print(array1)

#array split horizontalmente
array = np.array([[1,2,3],[4,5,6]])
array1 = np.hsplit(array,3)
print(array1)

#filtrando elementos
array = np.array([1,3,4,2,7,4])
array_find = np.where(array >= 4) # verificando onde no array é maior igual a 5
array_find = np.where((array == 4) | (array == 7)) # verificando onde no array é igual a 4 ou igual a 7

array = np.array([1,-1,-3,0,6,3,-78])
array_find = np.where((array > 0) & (array < 10)) # verificando onde no array é maior que 0 e menor que 10

#ocorrência de um valor - retorna true ou falso
array = np.array([1,3,4,2,7,4])
array_find = np.any(array == 1)
array_find = np.any((array > 0) & (array < 10))
array_find = np.all((array > 6)) # testando se todos atende essa condição
filter = (array == 1) | (array == 2) # filtrando que os elementos sejam igual a 1 ou igual a 2
filter_array = array[filter]
print(filter_array)
filtered_array = np.array([i for i in array if i == 1])
print(filtered_array) # mesmo fluxo de filtro

#ordenando array
array = np.array([4,1,3,2])
print(np.sort(array)) # ordenando com sort
array = np.array([[38,2,1],[5,5,4]])
print(np.sort(array,axis=0)) # ordenando por linha
print(np.sort(array,axis=1)) # ordenando por coluna