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