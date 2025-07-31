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