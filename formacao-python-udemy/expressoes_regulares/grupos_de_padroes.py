import re

texto = 'abbabb'
info = re.search('(abb)+',texto) # '()+' - essa expressão irá buscar de 1 até N ocorrências desse grupo especificado no search

if info != None:
    print('Encontrado ocorrência em:',info.span())
    print('O que foi encontrado:',info.group())
else:
    print("Nada foi encontrado")