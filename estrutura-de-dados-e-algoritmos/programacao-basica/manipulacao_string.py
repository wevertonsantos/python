a = 'casaco'
print(a)

maisucula = a.upper() # letra maiúscula
print(maisucula)

minuscula = maisucula.lower() # letra minúscula
print(minuscula)

capital = a.capitalize() # primeira letra maiúscula
print(capital)

metade_palavra = a[0:3] # slicing do 0 até o índice 2
print(metade_palavra)

ultimas_letras = a[3:] # do índice 3 em diante
print(ultimas_letras)

b = a.replace('aco','inha') # substituir 'aco' por 'inha'
print(a)
print(b)

c = a.replace('o','a')
print(c)

print(c.find('s')) # irá retornar índice
print(c.find('a'))
print(c.find('b')) # se não existe retorna -1