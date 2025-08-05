import pandas as pd
series = pd.Series([1,2,3,4,5]) # criando uma série
print(series)

series = pd.Series([1,2,3,4,5],dtype='i4') # definindo tipo 
print(series)

series = pd.Series([1,2,3,4,5],dtype='i4',name="Meus Números") # adicionando propriedade
print(series)

series = pd.Series([1,2,3,4,5],dtype='i4',name="Meus Números",index=["Um","Dois","Três","Quatro","Cinco"]) # atribuindo index para serie
print(series)