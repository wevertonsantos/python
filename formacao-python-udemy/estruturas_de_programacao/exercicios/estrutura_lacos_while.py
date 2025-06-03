# 1 - Crie um programa que receba 5 números e retorne a média aritmética entre esses números

i = 0
soma = 0
while i < 5:
    valor = float(input("Digite um valor: "))
    soma += valor
    i += 1
print("A média aritmética é: %.2f" % (soma / 5))