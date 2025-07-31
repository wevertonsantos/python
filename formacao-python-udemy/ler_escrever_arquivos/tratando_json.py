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