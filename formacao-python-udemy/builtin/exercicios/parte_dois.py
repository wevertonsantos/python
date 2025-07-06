'''
6 - Crie uma função que receba uma string e uma letra do alfabeto.
Retorne a quantidade de vezes que essa letra tem na string. 
Caso não ocorra nenhuma vez, retorne 0.
'''

def ocorrencia(string,letra):
    return string.count(letra)

print(ocorrencia("olamundo","o"))