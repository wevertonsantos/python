import pandas as pd
data_frame = pd.DataFrame() # criando um data frame

nomes = ['Roger','Lucas','Cristiano','Maria']
#criando data frame a partir da lista
data_frame = pd.DataFrame(nomes)
print(data_frame)

# criar tabela com mais colunas
numeros = [
    ['11','12','13','14'],
    ['11','12','13','14'],
    ['11','12','13','14'],
    ['11','12','13','14']
]

data_frame = pd.DataFrame(numeros,columns=['a','b','c','d'],index=['x','y','z','w']) # passando nome das colunas e index como linhas
print(data_frame)

# criar data frame a partir de dicionários
dados = {
    #'Nome':['Roger','Cristiano','Diego','Carla'],
    'Idade':[45,34,56,21],
    'Profissão':['Engenheiro','Desenvolvedor','Metalúrgico','Médica']
}

data_frame = pd.DataFrame(dados,index=['Roger','Cristiano','Diego','Carla'])
print(data_frame)

print(data_frame.loc['Roger']) # capturando colunas pelo índice

# importando arquivo csv
data = pd.read_csv('pessoas.csv',index_col='Nome') # o index vai vir da coluna nome
print(data)

# quantas colunas existem
print(len(data.columns))

print(data.columns) # vetor com nome das colunas

print(len(data.index)) #quantos index o data frame tem

print(data.index) # mostrando os index

print(data.shape) # formato do dataframe

#iterar sobre dataframe
for indice, linha in data.iterrows():
    print(indice,linha[0],linha[1],linha[2])

#iterando coluna
for coluna in data:
    print(coluna)

print(data['Idade']) # verificando coluna

# acessando valores individuais
print(data.loc['Roger']['Idade']) # acessando valor individual passando indice e coluna
print(data.loc['Roger'][0])