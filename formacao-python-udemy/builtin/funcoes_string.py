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