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

# acessando valores individuais pelo indice
print(data.iloc[0]['Idade'])
print(data.iloc[0][0])

# acessando duas colunas
print(data[['Idade','Altura']])

#slicing com dataframe
print(data.loc['Cristiano':'Jeferson']) #slicing de index
print(data.iloc[1:4])

#slicing com colunas
print(data.iloc[:,1:3])
print(data.loc[:,"Idade":"Profissão"])

#máscaras com dataframe
mask = data['Idade'] < 50 # verificando na coluna idade que atende a condição
print(mask)

# aplicando máscara no dataframe
novo_dframe = data[mask]
print(novo_dframe)

novo_dframe = data[(data['Idade'] > 40) & (data['Altura'] > 1.75)]
print(novo_dframe)

# atualizando valores no data frame
data.at['Roger','Idade'] = 56
print(data)

#atualizando pelo index
data.iat[2,0] = 100
print(data)

# alterando mais de um valor simultaneamente
data.loc['Cristiano','Idade':'Profissão'] = (45,'Dev')
print(data)

# alterando colunas especificas
data.loc['Cristiano','Idade':'Profissão'] = (45,'Dev')
print(data)

data.loc['José',['Idade','Altura']] = (65,1.72)
print(data)

#usando iloc para alterar
data.iloc[0,2] = 1.94
print(data)

#alterando mais valores
data = pd.read_csv('pessoas.csv',index_col='Nome')
print(data)
data.loc[(data['Idade'] == 34) & (data['Profissão'] == 'Programador'), ['Idade','Altura']] = (80,1.40)
print(data)

#inserindo linhas e colunas
data = pd.read_csv('pessoas.csv',index_col='Nome')
print(data)

#inserindo linha
data.loc['Carlos'] = (56,'Engenheiro',1.76) # passando novo indice e valores
print(data)

data_adicional = pd.DataFrame({'Idade':[34,21,54],
                               'Profissão':['Paraquedista','Professor','Cozinheiro'],
                               'Altura':[1.79,1.76,1.90]
                               }, index=['Julia','Roberto','Jack'])

data_adicional.index.name = 'Nome'

data = pd.concat([data,data_adicional]) # adicionando novo data frame em um data frame existente
print(data)

#inserindo coluna
data = pd.read_csv('pessoas.csv',index_col='Nome')
print(data)

#inserindo coluna com valores diferente para cada linha
data['Sobrenome'] = ['Silva','Sagan','','','','']
print(data)

#inserindo coluna em uma posição específica
data.insert(loc=1,column='Data Nascimento',value=['30/09/2000' for i in range(6)])
print(data)

#remoção de linhas
data = pd.read_csv('pessoas.csv',index_col='Nome')
print(data)

data2 = data.drop(index=['Roger','Diego']) # removendo linha com drop
print(data2)
data.drop(index=['Roger','Diego'],inplace=True) # removendo linha do objeto original
print(data)

#remoção de linha pelo índice
data.drop(index=data.index[[0,1]],inplace=True)
print(data)

#remoção de linha com condicional
data.drop(index=data[data['Altura'] >= 1.7].index,inplace=True)
print(data)