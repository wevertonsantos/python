import re
'''
1 - Faça uma expressão regular para reconhecer números de 20 até 35 apenas. O texto deve ser composto apenas destes números, nenhum outro caractere é permitido
'''

numero = '30'
info = re.search('^[2][0-9]|[3][0-5]$',numero)

if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")

'''
2 - Faça uma expressão regular para dizer se a palavra 'python' esta na frase.
'''

texto = "olá, python, aqui estou"
info = re.search('python',texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Encontrado  ", info.group())
else:
  print("Python não encontrado")