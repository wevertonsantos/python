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

#conjuntos (set)

biomoleculas = ('proteína','ácidos nucleicos','carboidrato','lipídeo','ácidos nucleicos','carboidrato','carboidrato','carboidrato')

print(set(biomoleculas)) # trás elementos que não se repetem

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2) # fazendo intersecção
print(c3)

print(c1.difference(c2)) # fazendo diferença