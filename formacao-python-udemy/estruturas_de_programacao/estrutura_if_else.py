numero = 9
if (numero >= 10):
    print("É maior ou igual a 10")
else: #se não, se a condição for falsa
    print("É menor que 10")

numero = 10
if numero % 2 == 0:
    print("É par")
else:
    print("É impar")

valor = 11
if valor >= 0 and valor < 9:
    print(valor)
else:
    print("Valor não aceito")

texto = "a"
if len(texto) == 1:
    print("Tem um caractere")
else:
    print("Não tem um caractere")

numero = 1
if numero == 1 or numero == 0:
    print("É 1 ou 0")

numero = 11
if numero > 0:
    print("Absolutamente maior que zero")
    if numero > 10:
        print("Número é maior que 10")