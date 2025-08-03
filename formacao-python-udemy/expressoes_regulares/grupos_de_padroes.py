import re

texto = 'abbabb'
info = re.search('(abb)+',texto) # '()+' - essa expressão irá buscar de 1 até N ocorrências desse grupo especificado no search

if info != None:
    print('Encontrado ocorrência em:',info.span())
    print('O que foi encontrado:',info.group())
else:
    print("Nada foi encontrado")

texto = 'abbabbabb'
info = re.search('(abb){2}',texto) # '{}' - essa expressão irá buscar até N ocorrências, dependendo do que você passar

if info != None:
    print('Encontrado ocorrência em:',info.span())
    print('O que foi encontrado:',info.group())
else:
    print("Nada foi encontrado")