#criar arquivo csv com a biblioteca
import csv

with open("pessoas.csv","w") as arquivo:
    escritorCsv = csv.writer(arquivo,delimiter=',') # permite criar arquivo csv e escrever nele (passando o arquivo e um delimitador)