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

# 4 - Percorra os números de 2 até 10 e diga se o número é par ou impar.

i = 2
while i <= 10:
    if i % 2 == 0:
        print("Número par %d" % i)
    else:
        print("Número impar %d" % i)
    i += 1

# 5 - Crie um programa que receba como input uma string. Em seguida percorra a string e diga quantos espaços em branco essa string tem.

string = input("Digite algo: ")
i = 0
espaco = 0
while i < len(string):
    if string[i] == " ":
        espaco += 1
    i += 1
print("A string tem %d espaços" % espaco)