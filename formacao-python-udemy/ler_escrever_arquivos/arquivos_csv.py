#criar arquivo csv com a biblioteca
import csv

with open("pessoas.csv","w") as arquivo:
    escritorCsv = csv.writer(arquivo,delimiter=',') # permite criar arquivo csv e escrever nele (passando o arquivo e um delimitador)
    escritorCsv.writerow(["id","nome"]) #escrever uma linha no arquivo csv (passando nome das colunas)
    escritorCsv.writerow(["1","Fernando"])

# criar arquivo csv apartir de um conteúdo de uma lista
linhas = [["id","nome"],["1","Fernando"]]

with open('pessoas2.csv','w') as arquivo2:
    escritorCsv = csv.writer(arquivo2)
    escritorCsv.writerows(linhas) # escrevendo várias linhas ao mesmo tempo.