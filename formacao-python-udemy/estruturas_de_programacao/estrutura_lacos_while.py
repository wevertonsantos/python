#while True:
#    print("Isso não vai parar")

interacao = 10
while interacao > 0:
    print(interacao)
    interacao -= 1
print("Encerrou")

indice = 10
while indice >= 2:
    if indice % 2 == 0:
        print("O número %d é par" % indice)
    else:
        print("O número %d é impar" % indice)
    indice -= 1

i = 0
soma = 0
while i < 5:
    #valor = float(input("Digite um valor: "))
    #soma += valor
    i += 1
print("O resultado da soma é: %.2f" % soma)

texto = "Olá 123 _"
i = 0
while i < len(texto):
    print(texto[i])
    i += 1

atual = 0
while True:
    if atual == 5:
        break
    print(atual)
    atual += 1