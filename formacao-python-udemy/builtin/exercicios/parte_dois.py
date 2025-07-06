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

'''
8 - Crie uma função que receba o que foi digitado pelo usuário no chat e 
também uma lista contendo todas as palavras não permitidas a serem digitadas. 
Essa função então retornara o que foi digitado pelo usuário mas no lugar 
das palavras não permitidas retorna o caractere '*’.
'''

def retira_palavras(texto,palavras):
    for palavra in palavras:
        if palavra in texto:
            texto = texto.replace(palavra,"*")
    return texto

print(retira_palavras("ola mundo",["mundo"]))

'''
9 - Crie uma função que retorne verdadeiro se uma string é totalmente 
maiúscula ou totalmente minúscula.
'''

def verificacao(string):
    return string.isupper() or string.islower()

print(verificacao("sada"))