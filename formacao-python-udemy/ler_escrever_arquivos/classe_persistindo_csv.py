import csv
class Pessoa:
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome

    @staticmethod
    def le_pessoas():
        pessoas = []
        with open('pessoas.csv','r') as arquivo:
            leitor = csv.reader(arquivo,delimiter=',')
            for linha in leitor:
                if linha != []:
                    pessoa = Pessoa(linha[0],linha[1])
                    pessoas.append(pessoa)
        return pessoas
    
    @staticmethod
    def salva_pessoas(*pessoas):
        with open('pessoas.csv','w') as arquivo:
            escritorCsv = csv.writer(arquivo,delimiter=',')
            for pessoa in pessoas:
                escritorCsv.writerow([pessoa.id,pessoa.nome])

pessoa1 = Pessoa('1','Fernando')
pessoa2 = Pessoa('2','André')

Pessoa.salva_pessoas(pessoa1,pessoa2)
lista_pessoas = Pessoa.le_pessoas()
for pessoa in lista_pessoas:
    print(pessoa.id,pessoa.nome)