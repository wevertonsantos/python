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

# Acessando as chaves e os valores do dic.
chaves = idades.keys()
valores = idades.values()
print(chaves)

# Limpando dicionário
idades.clear()
print(idades)

# Acessando dicionário dentro de um dicionário

dados_maria = {
    'sexo' : 'feminino',
    'cpf' : '12345678910',
    'rg' : '233232432'
}

dados_joao = {
    'sexo' : 'masculino',
    'cpf' : '12345678910',
    'rg' : '233232233'
}

dados_nome = {
    'maria' : dados_maria,
    'joao' : dados_joao
}

print(dados_nome)
print(dados_nome['joao']['sexo']) # Acessando dados de um dic dentro de outro dic