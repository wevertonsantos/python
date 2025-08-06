import pandas as pd

'''
Crie um dataframe com a estrutura abaixo. Os índices
devem ser as Equipes “X Racing”, “Equatorial”, “Typo”,
“Blue Race”,”Capa Racing”. Utilize um dicionário.
'''

dados = {
    'Sede':['Nova Iorque','São Paulo','Nova Iorque','Londres','Londres'],
    'Piloto':['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
    'Mundiais':[10,11,0,3,44],
    'Vitórias':[321,229,12,44,1023]
}

data = pd.DataFrame(dados,index=['X Racing','Equatorial','Type','Blue Race','Capa Racing'])

print(data,end='\n\n')

'''
2.Mostre todas as informações da equipe Blue Race
'''

print(data.loc['Blue Race'],end='\n\n')

'''
3. Mostre o número de mundiais da equipe Capa
Racing
'''

print(data.loc['Capa Racing','Mundiais'],end='\n\n')

'''
4. Mostre apenas as equipes que tem 10 ou mais
mundiais
'''

print(data[data['Mundiais'] >= 10],end='\n\n')

'''
5. Mostre apenas as equipes que tem 10 ou mais
mundiais e mais de 300 vitórias
'''
print(data[(data['Mundiais'] >= 10) & (data['Vitórias'] > 300)],end='\n\n')

'''
6. Atualize o nome do piloto da Equipe Equatorial para
Antônio Racer
'''

data.loc['Equatorial','Piloto'] = 'Antônio Racer'
print(data,end='\n\n')

'''
7. Atualize em um mesmo comando a equipe X Racing,
definindo sede como São Paulo e Vitórias com 322
'''

data.loc['X Racing',['Sede','Vitórias']] = ('São Paulo',322)
print(data,end='\n\n')

'''
8.Inclua uma nova equipe Red Cow, com sede em São
Paulo, Pitolo Fernando Vetel, Mundiais zero e Vitórias
zero
'''

data.loc['Red Cow'] = ('São Paulo','Fernando Vetel',0,0)
print(data,end='\n\n')

'''
9. Ordene o dataframe de forma decrescente pelo número
de vitórias
'''

new_data = data.sort_values('Vitórias',ascending=False)
print(new_data)