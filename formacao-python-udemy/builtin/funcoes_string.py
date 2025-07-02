# Deixando primeira letra maiúscula
texto = "olá, mundo"
print(texto.capitalize())

texto = "IsTo é EsTranHo"
print(texto.lower()) # Texto tudo minúsculo
print(texto.upper()) # Texto tudo maiúsculo
print(texto.swapcase()) # Texto invertido

texto = "eu sou um ótimo programador python"
print(texto.title()) # Transforma cada primeira letra de cada palavra em maiúsculo

texto = "1234567"
print(texto.center(9)) # Centralizando texto
print(texto.center(14))
print(texto.center(14,'-'))

texto = "1234567"
print(texto.rjust(9)) # Justificando à direita
print(texto.ljust(9)) # Justificando à esquerda

texto = "12121212"
print(texto.count("12")) # Contando a ocorrência no texto
print(texto.startswith("12")) # Verificando se o texto começa com
print(texto.endswith("12")) # Verificando se o texto termina com

texto = "Me encontra 20 10 5"
pos = texto.find("10") # Encontrando a posição da ocorrência no texto
print(pos)
pos = texto.find("4")
print(pos) # Se ele não encontrar ele mostra -1
pos = texto.index("10") # Encontrando index da ocorrência no 

texto = "Ol@ eu sou @ ful@no!"
novo_texto = texto.replace("@","a") # Encontrando o texto que quero substituir e colocando texto que quero incluir 
print(texto,novo_texto)

texto = "10,20,30"
print(texto.split(',')) # Divindo texto através do split (cria uma lista)

texto = "Olá, bom dia,\n Esse é um curso de python.\n Boa aula!"
print(texto.splitlines()) # Divide o texto por quebra de linha