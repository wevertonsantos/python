import re

texto = '-10 C°'
info = re.search('^(-)?[0-9]+ C°$',texto)

if info != None:
    print("Temperatura válida")
else:
    print("Temperatura inválida")

telefone = '92224466'
info = re.search('^9([0-9]{7})$',telefone)

if info != None:
    print("Número válido")
else:
    print("Número inválido")

# DD/MM/AAAA
# O dia varia de 00 a 31
# O mês de 00 a 12
# o ano de 0000 a 9999
data = '31/09/2002'
info = re.search('^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$',data)

if info != None:
    print('Data válida:',info.span())
else:
    print("Data inválida")