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

'''
3 - Faça uma expressão regular para validar se uma string dada é um dia da semana. As
possibilidades são:
'''

texto = 'Terça-Feira'
info = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$', texto)

'''
4 - Faça uma expressão regular para detectar telefones que comecem com 95. Telefones que começam com 95 devem ser bloqueados. Um número de telefone deve ser válido para poder ser validado, na forma
XXXXXXXX onde X é um número. Primeiro diga se é um número válido. Caso seja diga se ele foi bloqueado
ou não.
'''

texto = '9645634'

info = re.search("^([0-9]{8})$", texto)

if info !=None:
  print("Número válido")
  info2 = re.search("^95([0-9]{6})$", texto)
  if info2 !=None:
    print("Telefone bloqueado")
  else:
    print("Telefone não bloqueado")
else:
  print("Número inválido")

'''
5 - Faça uma expressão regular para reconhecer palavrados no gerúndio. Normalmente essas palavras podem ser detectadas caso elas terminem com ando, endo, indo: Exemplo: sorrindo, andando. Usa a
função “find all” para retornar as ocorrências.
'''

texto = "Olá, eu estou dormindo, e não sorrindo"
info = re.findall("([\w]+indo|ando|endo)+", texto)
print(info)