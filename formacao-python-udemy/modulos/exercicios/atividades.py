# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.

from random import randrange

numero_aleatorio = randrange(2,100)

if numero_aleatorio % 2 == 0:
    print(numero_aleatorio, "Número par")
else:
    print(numero_aleatorio, "Número ímpar")

