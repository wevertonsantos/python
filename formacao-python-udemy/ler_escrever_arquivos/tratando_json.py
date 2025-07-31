import json

idades = {
    'Rogerio':20,
    'Maria':30
}

print(json.dumps(idades)) #transformando dicionário em json

DadosPessoas = {
    'Rodrigo': {
        'CPF':'123456',
        'Sexo':'Masculino'
    },
    'Fernando': {
        'CPF':'123456',
        'Sexo':'Masculino'
    }
}

texto = json.dumps(DadosPessoas, indent=4) #identar objetos com 4 espaços
print(texto)
with open('exemplo.json','wt') as arquivo: # criando arquivo como json
    arquivo.write(texto) #escrevendo o dump no arquivo

#lendo arquivo json e transformando em dicionário
dicionario = None
with open('exemplo.json','rt') as arquivo:
    arquivo_lido = arquivo.read()
    dicionario = json.loads(arquivo_lido) # transformando arquivo lido para dicionário com load

print(dicionario)

# mesmo fluxo com classe

class Carro:
    def __init__(self,nome,potencia):
        self.nome = nome
        self.potencia = potencia
    
    @staticmethod
    def salva_carros(*carros):
        dicionario = dict()
        for carro in carros:
            dicionario[carro.nome] = carro.potencia
        texto = json.dumps(dicionario,indent=4)
        with open('carros.json','wt') as arquivo:
            arquivo.write(texto)
    
    @staticmethod
    def le_carros():
        lista = []
        texto = None
        with open('carros.json','rt') as arquivo:
            texto = arquivo.read()
        dicionario = json.loads(texto)
        for chave in dicionario:
            carro = Carro(chave,dicionario[chave])
            lista.append(carro)
        return lista