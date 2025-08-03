import re

texto = '01234 ABC'

info = re.search("\d",texto) # \d irá buscar qualquer número

if info != None:
    print("Encontrado ocorrência em:", info.span())
    print("O que foi encontrado:", info.group())


info = re.search("\D",texto) # \D irá buscar a não ocorrência de números

if info != None:
    print("Encontrado ocorrência em:", info.span())
    print("O que foi encontrado:", info.group())