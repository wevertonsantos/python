'''
Crie um arquivo CSV separado por virgula para guardar informações de sua família.
Nesse arquivo deve constar em cada linha o nome de um membro da família e o grau de
parentesco(Ex: pai). Escreva 5 membros da família no arquivo. Faça uma função que ira
escrever no arquivo, e outra que ira ler o arquivo.
'''

import csv

def escreve_arquivo():
  with open('exercicio5.csv','w') as arquivo:
    escritorCSV = csv.writer(arquivo, delimiter=',')
    escritorCSV.writerow(["Nome","Parentesco"])
    escritorCSV.writerow(["Pedro","Avô"])
    escritorCSV.writerow(["Maria","Avó"])
    escritorCSV.writerow(["José","Pai"])
    escritorCSV.writerow(["Ana","Mãe"])
    escritorCSV.writerow(["Amanda","Filha"])

def le_arquivo():
  with open('exercicio5.csv','r') as arquivo:
    leitor = csv.reader(arquivo, delimiter = ',')
    for linha in leitor:
      print(linha)
escreve_arquivo()
le_arquivo()