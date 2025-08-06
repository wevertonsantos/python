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