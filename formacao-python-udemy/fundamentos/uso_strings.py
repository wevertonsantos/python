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

texto = "metro"
print(texto[::-1]) #inverter string
print(texto[3::])
print(texto[3:1:-1])

#substituição
texto = "023"
texto = "1" + texto[1:]
print(texto)

#remoção
texto = "abcdefg"
texto = texto[:3] + texto[4:]
print(texto)

#comparação de string
texto1 = "Olá"
texto2 = "Olá"
igual = texto1 == texto2
print("Textos são iguais?", igual)
print("a" != "b")

#verificação de existência
texto = "Programação"
print("a" in texto) #está contido?
print("Programa" in texto)
print("Programa" not in texto) #não está contido?