# tupla
tupla = ('Homo sapiens','Canis familiaries','Felis catus')
print(tupla)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla.index('Canis familiaries')) # posição que está

for elemento in tupla:
    print(elemento)

#list
lista = ['Homo sapiens','Canis familiaries','Felis catus']
lista2 = ['Xenopus laevis','Ailuropoda melanoleuca']
lista3 = lista + lista2
print(lista3)
print(lista2)

lista2_2 = lista2 * 2 # duplicando lista
print(lista2_2)
print(lista[0])
print(lista)
print(lista[0:2]) # slicing

lista.append('Gorila gorila') # adicionando elemento
print(lista)

lista.remove('Felis catus') # removendo elemento
print(lista)

del (lista) # deletando lista inteira

for item in lista2_2:
    print(item)

#dicionário
coleta = {
    'Aedes aegypt' : 32,
    'Aedes albopictus' : 22,
    'Anopheles darling' : 14
}
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11 # adicionando novo elemento
print(coleta)

del (coleta)['Aedes albopictus'] # deletando
print(coleta)

print(coleta.items()) # trazendo itens do dicionário
print(coleta.keys()) # trazendo apenas chaves
print(coleta.values()) # trazendo apenas valores

coleta2 = {
    'Anopheles gambiae' : 13,
    'Anopheles deaneorum' : 14
}
print(coleta2)

coleta.update(coleta2) # juntando dois dicionários
print(coleta)

#percorrendo dicionário
for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')
