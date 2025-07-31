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