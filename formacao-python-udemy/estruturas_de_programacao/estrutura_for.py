for x in range(10):
    print(x)

for x in range(5,10):
    print(x)

for x in range(5,20,5):
    print(x)

for x in range(20,5,-5):
    print(x)

texto = "123456789"
for x in range(0,len(texto)):
    print(texto[x])

letra = input("Digite uma letra: ")

if len(letra) != 1:
    print("Precisa ter apenas um digito")
else:
    texto = input("Digite um texto: ")
    for i in range(0,len(texto)):
        if letra == texto[i]:
            print("Encontrei a letra %s na posição %d" % (letra, i))