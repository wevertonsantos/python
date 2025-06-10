tuple = tuple(('chocolate','bom bom','paçoca'))
tuple = ('chocolate','bom bom','paçoca')
print(tuple)

numeros = (1,1,2,3,4,5)
print(numeros[2]) # Permitido acessar índice.
print(numeros[1:3]) # Slices com tuple
#numeros[0] = '10' # Não é permitido alteração
print(numeros.count(1)) # Ocorrência desse elemento em tuple