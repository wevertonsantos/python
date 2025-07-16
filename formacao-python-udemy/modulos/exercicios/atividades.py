# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.

from random import randrange

numero_aleatorio = randrange(2,100)

if numero_aleatorio % 2 == 0:
    print(numero_aleatorio, "Número par")
else:
    print(numero_aleatorio, "Número ímpar")

# 2 - Da mesma forma que o exercício anterior, gere a soma de 100 números 
# aleatórios e mostre o resultado final.

i = 0
soma = 0
while i <= 100:
    soma += randrange(1,100)
    i += 1

print(soma)