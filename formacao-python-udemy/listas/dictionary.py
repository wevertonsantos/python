idades = {'ana':10,'maria':20,'joão':34,'fernando':'indefinido'}
print(idades)
# Forma de pegar valor da chave
print(idades['maria'])
print(idades['fernando'])

# Usando get para pegar valor da chave
print(idades.get('fernando'))

# Atualizando valor da chave
idades['maria'] = 30
idades.update({"joão":40})
print(idades)

# Atribuindo item
idades['marcos'] = 20

# Removendo item
idades.pop('ana')
print(idades)

# Removendo último item
idades.popitem()
print(idades)

# Percorrendo nova lista com itens do dicionário
lista = idades.items()
print(lista)
for item in lista:
    print(item[0],item[1])