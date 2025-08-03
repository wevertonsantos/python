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

# buscando grupos de padrões
texto = 'ABCDefgHI123'
# [] - representa que queremos um conjunto de caracteres
info = re.findall('[Ae3]',texto) # buscando 'A e 3'
info2 = re.findall('[A-Z]',texto) # buscando de A a Z maiúsculo 
info3 = re.findall('[a-z]',texto) # buscando de 'a' até 'z' minúsculo
info4 = re.findall('[0-9]',texto) # buscando de 0 até 9
info5 = re.findall('[A-Za-z]',texto) # buscando de A a Z maiúsculo e de a até z minúsculo
print(info)
print(info2)
print(info3)
print(info4)
print(info5)