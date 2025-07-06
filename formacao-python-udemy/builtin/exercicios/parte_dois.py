'''
6 - Crie uma função que receba uma string e uma letra do alfabeto.
Retorne a quantidade de vezes que essa letra tem na string. 
Caso não ocorra nenhuma vez, retorne 0.
'''

def ocorrencias(string,letra):
    return string.count(letra)

print(ocorrencias("olamundo","o"))

'''
7 - Crie uma função receba uma string e uma letra do alfabeto. 
Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.
'''

def ocorrencias(texto,caracter):
  indices = []
  indice =0
  for char in texto:
    if (char == caracter):
      indices.append(indice)
    indice += 1
  return indices

print(ocorrencias("abcaa","a"))