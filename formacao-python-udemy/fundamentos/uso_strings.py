#concatenação de strings
texto1 = "olá"
texto2 = ", "
texto3 = "tudo bem?"
texto_completo = texto1 + texto2 + texto3
print(texto_completo)

texto1 += " mundo" #atribuição com string
print(texto1)

#repetição de string
texto = "Python é bem produtivo,"
texto_repetido = texto * 3
print(texto_repetido)

#slicing strings
texto = "exemplo"
print(texto[0])
print(texto[1])
print(texto[1:3])
print(texto[3:])
print(texto[:5])

texto = "carro"
print(texto[-5]) #conta da direita para esquerda
print(texto[-5:])
print(texto[:-1])
print(texto[-5:-2])