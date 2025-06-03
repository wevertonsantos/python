# 1 - Crie um programa que receba 5 números e retorne a média aritmética entre esses números

i = 0
soma = 0
while i < 5:
    valor = float(input("Digite um valor: "))
    soma += valor
    i += 1
print("A média aritmética é: %.2f" % (soma / 5))

# 2 - Crie um programa que receba 5 números, realiza a soma destes números, mas caso um destes números seja negativo não considere ele na soma.

i = 0
soma = 0
while i < 5:
    valor = float(input("Digite um valor: "))
    if valor > 0:
        soma += valor
    i += 1
print("A soma é: %.2f" % soma)

# 3 - Crie um programa que receba um número arbitrário (definido pelo usuário) de números que serão lidos e retorne a soma de todos eles.

i = 0
soma = 0
quantidade = int(input("Digite a quantidade de números que serão lidos: "))
while i < quantidade:
    valor = float(input("Digite um valor: "))
    soma += valor
    i += 1
print("A total é: %.2f" % soma)