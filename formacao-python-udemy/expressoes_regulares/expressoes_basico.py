import re # importando regular expressions

# método search (buscar ocorrência de um determinado caracter em um texto)
texto = '00123451'
info = re.search('1',texto) # procurar '1' em texto