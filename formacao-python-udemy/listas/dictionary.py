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

# Removendo item
idades.pop('ana')
print(idades)

# Removendo último item
idades.popitem()
print(idades)