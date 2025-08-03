import re

texto = '-10 C°'
info = re.search('^(-)?[0-9]+ C°$',texto)

if info != None:
    print("Temperatura válida")
else:
    print("Temperatura inválida")

telefone = '99224466'
info = re.search('^99([0-9]{6})$',telefone)

if info != None:
    print("Número válido")
else:
    print("Número inválido")