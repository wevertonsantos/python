import re # importando regular expressions

# método search (buscar ocorrência de um determinado caracter em um texto)
texto = '00123451'
info = re.search('1',texto) # procurar '1' em texto

if info != None:
    print('Encontrado ocorrência em:',info.span())
    print('O que foi encontrado:',info.group())
else:
    print("Nada foi encontrado")

# encontrar todas as ocorrências no texto
print("Encontrando todas ocorrências:")
info = re.findall('1',texto)
print(info)

# utilizando split (divide a string antes e depois do padrão encontrado) para separar textos.
info = re.split('1',texto)
print(info)

# sub - substitui o que é encontrado pelo o que é passado
info = re.sub("1","#",texto)
print(info)