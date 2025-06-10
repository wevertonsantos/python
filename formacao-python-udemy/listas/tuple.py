tupla = tuple(('chocolate','bom bom','paçoca'))
tupla = ('chocolate','bom bom','paçoca')
print(tupla)

numeros = (1,1,2,3,4,5)
print(numeros[2]) # Permitido acessar índice.
print(numeros[1:3]) # Slices com tuple
#numeros[0] = '10' # Não é permitido alteração
print(numeros.count(1)) # Ocorrência desse elemento em tuple

tupla = (1,2,3)
lista = list(tupla)
lista[0] = 12
lista.append("Fim")
tupla = tuple(lista)
print(tupla)
