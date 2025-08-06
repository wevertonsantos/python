import pandas as pd
data_frame = pd.DataFrame() # criando um data frame

nomes = ['Roger','Lucas','Cristiano','Maria']
#criando data frame a partir da lista
data_frame = pd.DataFrame(nomes)
print(data_frame)