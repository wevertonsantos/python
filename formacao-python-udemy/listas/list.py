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