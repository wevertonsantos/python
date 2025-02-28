# verificando tipo da variável

texto = "hello"
numero = 2
decimal = 2.2
boolean = True
print(type(texto))
print(type(numero))
print(type(decimal))
print(type(boolean))

# casting

texto1 = "2"
texto2 = "1.5"
numero1 = int(texto1) # convertendo para inteiro
numero2 = float(texto2) # convertendo para float

num = 21.45646
inteiro = int(num)
print("Parte inteira de %f é %d" % (num,inteiro))

texto = "O número é "
numero = 10.3
numero_string = str(numero) # convertendo para string
print(texto, numero_string)

numero = 123
texto = str(numero)
tamanho_texto = len(texto)
print("O número %s tem %d digitos " % (texto,tamanho_texto))