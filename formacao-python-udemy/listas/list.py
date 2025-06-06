# Formas de declaração de lista
array = []
array = list()

numeros = [1,2,3] # Lista com números
floats = [5.3,-2.2,0.5] # Lista com pontos flutuantes
strings = ["A","B","C"] # Lista com strings
misto = [2,2.3,"ABC"] # Lista com dados diferentes

array = list([1,2,3]) # Método lista com números
elemento = array[0] # Acessando elemento de uma lista
print(elemento)

# Alterando valor de uma lista
array[0] = 4
print(array)

# Fazendo slice com lista
print(array[1:3])

# Inserindo elemento no final da lista
array = [10,2,3]
array.append(2)
print(array)

# Inserindo elemento em determinada posição
array.insert(2,4) #inserindo o 4 na posição 2 do array
print(array)

# Removendo elemento pelo valor
array = [10,2,3,20,"3"]
array.remove(10)
array.pop(2) # Removendo elemento pelo índice
print(array)
print(len(array)) # Verificando comprimento do array

# Limpando completamente o array
array.clear()
print(array)

array = [1,'teste',1.3,True]
print(1 in array) # Verificando se existe valor na lista
print(False not in array)

# Verifica quantas vezes o elemento aparece na lista
lista = [5,6,7,2,3,4,7]
print(lista.count(7))

# Verifica em qual posição o elemento aparece na lista
print(lista.index(5))

# Juntando array
arr = [1,2,3]
array = [3,4,5]
completo = arr + array
print(completo)
print(completo * 2) # Multiplicando array e mostrando ele x vezes

# Atribuindo elemento do array para cada variável
numero = ["um","dois","três"]
x,y,_ = numero
print(x,y)